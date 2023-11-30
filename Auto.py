import requests
from bs4 import BeautifulSoup
import time

def get_links_from_website(url):
    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')

            # Find all the 'a' (anchor) tags
            links = soup.find_all('a')

            # Extract and print the href attribute from each anchor tag
            for link in links:
                href = link.get('href')
                if href:
                    print(href)
        else:
            print(f"Failed to retrieve content. Status code: {response.status_code}")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage:
url_to_load = 'https://example.com'

# Load the URL the first time
print("First attempt:")
get_links_from_website(url_to_load)

# Introduce a time delay (e.g., 5 seconds) before the second attempt
time.sleep(5)

# Load the URL the second time
print("\nSecond attempt:")
get_links_from_website(url_to_load)
