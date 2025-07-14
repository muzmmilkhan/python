'''
Use Case: Web Scraping
Real World Example: Multithreading for I/O-bound tasks
Scenario: A web scraping application that collects data from multiple websites concurrently to improve efficiency and reduce overall scraping time.
'''

url1 = 'https://python.langchain.com/v0.2/docs/introduction/'
url2 = 'https://python.langchain.com/v0.2/docs/concepts/'
url3 = 'https://python.langchain.com/v0.2/docs/tutorials/'

import threading
import requests
from bs4 import BeautifulSoup

urls = [url1, url2, url3]

def fetch_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        soup = BeautifulSoup(response.content, 'html.parser')
        print(f"Fetched content from {url}: {len(soup.text)} characters")
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")

threads = []
for url in urls:
    thread = threading.Thread(target=fetch_content, args=(url,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All content fetched successfully.")