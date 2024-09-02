from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import pandas as pd
import requests

# Function to fetch available seasons from 2000 onwards
def fetch_available_seasons():
    url = "https://www.basketball-reference.com/leagues/"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    seasons = []
    for link in soup.find_all('a'):
        href = link.get('href', '')
        if '/leagues/NBA_' in href and href.endswith('.html'):
            season_year = href.split('_')[1].split('.')[0]
            if season_year.isdigit() and int(season_year) >= 2000:
                seasons.append(season_year)

    return seasons


# Function to fetch player stats using Selenium with Chrome
def fetch_player_stats_with_selenium(season, player_name):
    # Initialize the Chrome WebDriver
    driver = webdriver.Chrome()  # Ensure ChromeDriver is installed and in your PATH
    url = f"https://www.basketball-reference.com/leagues/NBA_{season}_per_game.html"
    driver.get(url)

    try:
        # Wait explicitly for the table to be present
        element_present = EC.presence_of_element_located((By.ID, 'per_game_stats'))
        WebDriverWait(driver, 20).until(element_present)

        # Get the page source after JavaScript has loaded
        soup = BeautifulSoup(driver.page_source, 'html.parser')

    except Exception as e:
        print(f"An error occurred: {e}")
        driver.quit()
        return

    driver.quit()  # Close the browser window

    # Now parse the table as before
    table = soup.find('table', {'id': 'per_game_stats'})

    if table is None:
        print(f"No table found on the page for season {season}.")
        return

    # Extract the first row of headers, ensuring no duplicates or extra headers
    headers = [th.text.strip() for th in table.find('thead').find_all('th')][1:]
    rows = table.find_all('tr', class_='full_table')
    correct_column_count = len(headers)
    player_stats = []

    player_name_lower = player_name.lower()

    for row in rows:
        player_cell = row.find('td', {'data-stat': 'player'})
        if player_cell:
            scraped_player_name = player_cell.text.strip().lower()

            if player_name_lower == scraped_player_name:
                player_data = [cell.text for cell in row.find_all('td')]

                # Debugging: Print the number of columns in each data row
                print(f"Extracted data row length: {len(player_data)}, Headers length: {correct_column_count}")

                player_stats.append(player_data)

    # Debug: Check the first row of player stats and headers
    if player_stats:
        print(f"\nFirst row of player stats: {player_stats[0]}")
        print(f"Headers: {headers}")

    if player_stats and len(player_stats[0]) == correct_column_count:
        df = pd.DataFrame(player_stats, columns=headers)
        df.to_csv(f'{player_name}_stats_{season}.csv', index=False)
        print(f"Data for {player_name} in season {season} has been saved to '{player_name}_stats_{season}.csv'")
    else:
        print(
            f"No data found or data does not match the expected number of columns for {player_name} in season {season}.")


# Main function to run the scraper
def main():
    # Fetch available seasons from 2000 onwards
    seasons = fetch_available_seasons()

    # Let the user select a season
    selected_season = input("Please select a season (2000 onwards): ")
    if selected_season not in seasons:
        print("Invalid season selected or data not available for this season.")
        return

    # Let the user select a player
    selected_player = input("\nPlease enter the full name of the player you want to see stats for: ")

    # Fetch and save the player's stats for the selected season
    fetch_player_stats_with_selenium(selected_season, selected_player)


if __name__ == "__main__":
    main()
