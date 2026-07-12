from playwright.sync_api import sync_playwright
import csv

# ------------------------------
# Helper: Scrape a tools table
# ------------------------------
def scrape_tools_table(page):
    tools = []
    seen_pages = set()

    while True:
        table_html = page.inner_html("div.lj6icyk table tbody")
        if table_html in seen_pages:
            break
        seen_pages.add(table_html)

        for row in page.query_selector_all("div.lj6icyk table tbody tr"):
            name_cell = row.query_selector("th a")
            tool_name = name_cell.inner_text().strip() if name_cell else ""
            href = name_cell.get_attribute("href") if name_cell else None
            tool_url = "https://tines.com" + href if href else ""

            stories_cell = row.query_selector("td:nth-child(3)")
            stories = stories_cell.inner_text().strip() if stories_cell else "0"

            print(f"[Task 1] Tool: {tool_name} | Stories: {stories}")
            tools.append((tool_name, stories, tool_url))

        next_btn = page.query_selector("button:has-text('Next'):not([disabled])")
        if next_btn:
            next_btn.click()
            page.wait_for_timeout(1500)
            page.wait_for_selector("div.lj6icyk table tbody tr", timeout=60000)
        else:
            break

    return tools

# ------------------------------
# Helper: Scrape a stories table
# ------------------------------
def scrape_stories_table(page, tool_name=None):
    stories = []
    seen_pages = set()

    while True:
        table_html = page.inner_html("div.lj6icyk table tbody")
        if table_html in seen_pages:
            break
        seen_pages.add(table_html)

        for row in page.query_selector_all("div.lj6icyk table tbody tr"):
            story_name = row.query_selector("th a").inner_text().strip() if row.query_selector("th a") else ""
            works_with_list = [icon.inner_text().strip() for icon in row.query_selector_all("td.lnfq6m a div span")]
            works_with = ", ".join(works_with_list) if works_with_list else "null"
            actions = row.query_selector("td.l15yppem").inner_text().strip() if row.query_selector("td.l15yppem") else ""
            author = row.query_selector("td.lak4zbu strong")
            author_name = author.inner_text().strip() if author else "null"

            if tool_name:
                print(f"[Task 2] Tool: {tool_name} | Story: {story_name} | Works With: {works_with} | Actions: {actions} | Author: {author_name}")
                stories.append((tool_name, story_name, works_with, actions, author_name))
            else:
                print(f"[Task 3] Story: {story_name} | Works With: {works_with} | Actions: {actions} | Author: {author_name}")
                stories.append((story_name, works_with, actions, author_name))

        next_btn = page.query_selector("button:has-text('Next'):not([disabled])")
        if next_btn:
            next_btn.click()
            page.wait_for_timeout(1500)
            page.wait_for_selector("div.lj6icyk table tbody tr", timeout=60000)
        else:
            break

    return stories

# ------------------------------
# Task 1: Tools list
# ------------------------------
def scrape_task1(page):
    page.goto("https://tines.com/library/tools", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_selector("div.lj6icyk table tbody tr", timeout=60000)
    tools = scrape_tools_table(page)

    with open("tines_tools.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Tool Name", "Number of Stories"])
        for name, stories, _ in tools:
            writer.writerow([name, stories])

    print(f"Task 1 completed: {len(tools)} tools saved to tines_tools.csv")
    return tools

# ------------------------------
# Task 2: Stories per tool
# ------------------------------
def scrape_task2(page, tools):
    all_stories = []

    for name, _, url in tools:
        if not url:
            continue
        page.goto(url, wait_until="domcontentloaded", timeout=60000)
        page.wait_for_selector("div.lj6icyk table tbody tr", timeout=60000)
        all_stories.extend(scrape_stories_table(page, tool_name=name))

    with open("tines_tool_stories.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Tool Name", "Story", "Works with", "No.of actions", "Author"])
        writer.writerows(all_stories)

    print(f"Task 2 completed: {len(all_stories)} stories saved to tines_tool_stories.csv")
    return all_stories

# ------------------------------
# Task 3: All stories view
# ------------------------------
def scrape_task3(page):
    page.goto("https://tines.com/library?view=all", wait_until="domcontentloaded", timeout=60000)
    page.wait_for_selector("div.lj6icyk table tbody tr", timeout=60000)
    stories = scrape_stories_table(page)

    with open("tines_all_stories.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Story", "Works with", "No.of actions", "Author"])
        writer.writerows(stories)

    print(f"Task 3 completed: {len(stories)} stories saved to tines_all_stories.csv")
    return stories

# ------------------------------
# Run all tasks
# ------------------------------
def scrape_all_tasks():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        tools = scrape_task1(page)
        scrape_task2(page, tools)
        scrape_task3(page)

        browser.close()

if __name__ == "__main__":
    scrape_all_tasks()
