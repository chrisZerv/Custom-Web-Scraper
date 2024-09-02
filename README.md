# NBA Player Stats Scraper

This Python project allows users to scrape NBA player statistics from the Basketball Reference website for seasons from 2000 onwards. The script uses Selenium to navigate the website, scrape the data, and save it as a CSV file.

## Features

- Scrape NBA player stats from the year 2000 to the present.
- Select a specific season and player to retrieve detailed game statistics.
- Save the scraped data to a CSV file for easy analysis.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed on your machine.
- Google Chrome browser installed.
- ChromeDriver compatible with your installed version of Chrome.

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/yourusername/NBA-Player-Stats-Scraper.git
    cd NBA-Player-Stats-Scraper
    ```

2. **Install the required Python packages:**

    You can install the required packages using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

    **Note:** If `requirements.txt` is not available, you can manually install the dependencies:

    ```bash
    pip install selenium
    pip install beautifulsoup4
    pip install pandas
    ```

3. **Download ChromeDriver:**

    - Download the ChromeDriver that matches your Chrome version from the [official site](https://sites.google.com/chromium.org/driver/).
    - Make sure the `chromedriver` executable is in your system's PATH, or specify the path in the script.

## Usage

To use the NBA Player Stats Scraper:

1. **Run the script:**

    ```bash
    python main.py
    ```

2. **Follow the prompts:**

    - Enter a season from 2000 onwards (e.g., `2023`).
    - Enter the full name of the player you want to see stats for (e.g., `Russell Westbrook`).

3. **Output:**

    - The script will scrape the stats for the specified player and season and save them in a CSV file named `{player_name}_stats_{season}.csv` (e.g., `Russell_Westbrook_stats_2023.csv`).

## Troubleshooting

- Ensure that ChromeDriver is properly installed and matches your Chrome version.
- If you encounter issues with data extraction, check that the Basketball Reference website structure hasn't changed.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request to submit any improvements.

## License

This project is open-source and available under the [MIT License](LICENSE).


