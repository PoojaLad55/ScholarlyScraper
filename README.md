# ScholarlyScraper

## Description
A Python program for data scraping research papers from Google Scholar, extracting selected terms/values and exporting them into a CSV file.

## Features
- Data scrapes research papers from Google Scholar.
- Searches for user-defined specific terms/values within the papers.
- Extracts and compiles the information into a CSV file.
- Easy to use and customizable.

## Installation

### Prerequisites
- Python 3.0 or higher

### Virtual Environment Setup
It is recommended to use a virtual environment to manage dependencies.

1. **Create a virtual environment:**
   ```sh
   python -m venv venv
2. **Activate the environment:**
    On Windows: 
    ```sh
    venv\Scripts\activate
    On macOS/Linux: 
    ```sh
    source venv/bin/activate
3. **Install the necessary dependencies:**
    ```sh
    pip install -r requirements.txt

### Usage
1. **Run the Scraper:**
    ```sh
    python scraper.py
2. **User Input:**
    - You will be prompted to enter a list of search terms, separated by commas.
    - You will be prompted to enter a list of sources (Google Scholars, Web Science, etc.), separated by commas.
3. **Output:**
    The extracted output information will be saved in ScholarlyScraperOutput.csv in root directory.

### Contributions
Contributions in the form of feedback, bug reports, and suggestions are welcome! However, please note that under the terms of the [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](LICENSE), modifications to the codebase are not permitted.

## License
This project is licensed under the [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](LICENSE) - see the [LICENSE](LICENSE) file for details.