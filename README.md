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

1. **Clone the repository:**
    ```sh
    git clone https://github.com/PoojaLad55/ScholarlyScraper.git
    cd ScholarlyScraper
2. **Create a virtual environment:**
   ```sh
   python -m venv venv
3. **Activate the environment:**
    ```sh
    On Windows:
    venv\Scripts\activate
    On macOS/Linux: 
    source venv/bin/activate
4. **Install the necessary dependencies:**
    ```sh
    pip install -r requirements.txt

## Usage
1. **Run with Command-Line Arguments**
    ```sh
    python main.py --base-query "base query" --terms "search terms" --sources "google scholar" --pages number
2. **Arguments:**
    - `--base-query`: Base Google Scholar search query (e.g., "coral reefs")
    - `--terms`: Comma-separated list of search terms (e.g., "coral, reef, climate")
    - `--sources`: Comma-separated list of sources (e.g., "google scholar").
    - `--pages`: Number of pages to scrape (default is 5).
3. **Path:**
    Enter path to chromedriver when prompted.
4. **Output:**
    The extracted output information will be saved in output.csv in root directory.

### Example
    ```sh
    python main.py --base-query "coral reef" --terms "juvenile, corals, coral, reefs, reef" --sources "google scholar" --pages 7
    
### Notes
- The script currently only supports "Google Scholar" as a source and skips books.
- Ensure that the required Python libraries are installed (e.g., selenium, requests). Ensure compatible chrome driver using the following link: https://getwebdriver.com/chromedriver#stable -- copy path of chromedriver into utils.py

## Contributions
Contributions in the form of feedback, bug reports, and suggestions are welcome! However, please note that under the terms of the [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](LICENSE), modifications to the codebase are not permitted.

## License
This project is licensed under the [Creative Commons Attribution-NoDerivatives 4.0 International (CC BY-ND 4.0)](LICENSE) - see the [LICENSE](LICENSE) file for details.