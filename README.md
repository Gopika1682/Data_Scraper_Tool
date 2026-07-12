# Data Scraper Tool

## Overview

Data Scraper Tool is a Python-based web scraping project that uses Playwright to extract data from the Tines Library. The scraper automates the collection of tools and stories information and exports the results into CSV files for further analysis.

## Features

* Scrapes all available tools from the Tines Library.
* Extracts the number of stories associated with each tool.
* Collects detailed story information, including:

  * Story Name
  * Tool Name
  * Works With Integrations
  * Number of Actions
  * Author Name
* Generates structured CSV output files.
* Handles pagination automatically.

## Technologies Used

* Python 3.x
* Playwright
* CSV Module

## Project Structure

```text
Data_Scraper_Tool/
│
├── code/
│   ├── main.py
│   └── requirements.txt
│
├── Output/
│   ├── scraper_tools.csv
│   ├── scraper_tool_stories.csv
│   └── scraper_all_stories.csv
│
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Gopika1682/Data_Scraper_Tool.git
```

2. Navigate to the project directory:

```bash
cd Data_Scraper_Tool
```

3. Install the required dependencies:

```bash
pip install -r code/requirements.txt
```

4. Install Playwright browsers:

```bash
playwright install
```

## Usage

Run the scraper using:

```bash
python code/main.py
```

The script will launch a browser, scrape the required data, and generate CSV files containing the extracted information.

## Output Files

### scraper_tools.csv

Contains:

* Tool Name
* Number of Stories

### scraper_tool_stories.csv

Contains:

* Tool Name
* Story Name
* Works With
* Number of Actions
* Author

### scraper_all_stories.csv

Contains:

* Story Name
* Works With
* Number of Actions
* Author

## Key Functionalities

### Task 1: Tools Extraction

Scrapes all tools from the Tines Library and records the number of associated stories.

### Task 2: Tool-wise Story Extraction

Visits each tool page and extracts detailed information about related stories.

### Task 3: Complete Stories Extraction

Scrapes all stories available in the Tines Library's "View All" section.

## Notes

* Pagination is handled automatically.
* Duplicate pages are avoided using page-content tracking.
* Data is exported in CSV format for easy analysis and reporting.

## Author

Gopika

## Repository

GitHub Repository: https://github.com/Gopika1682/Data_Scraper_Tool
