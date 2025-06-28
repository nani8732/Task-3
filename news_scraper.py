import requests
from bs4 import BeautifulSoup

# URL of the news site (changeable)
URL = "https://www.bbc.com/news"

# Output file
OUTPUT_FILE = "headlines.txt"

def fetch_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return ""

def extract_headlines(html):
    soup = BeautifulSoup(html, "html.parser")
    # For BBC, headlines are mostly in <h3> tags with class "gs-c-promo-heading__title"
    headlines = soup.find_all(['h1', 'h2', 'h3'])
    titles = [tag.get_text(strip=True) for tag in headlines if tag.get_text(strip=True)]
    return titles

def save_headlines(headlines, filename):
    with open(filename, "w", encoding="utf-8") as file:
        for i, title in enumerate(headlines, start=1):
            file.write(f"{i}. {title}\n")
    print(f"Saved {len(headlines)} headlines to {filename}")

def main():
    print("Fetching news headlines...")
    html = fetch_html(URL)
    if html:
        headlines = extract_headlines(html)
        save_headlines(headlines, OUTPUT_FILE)
    else:
        print("No HTML fetched. Exiting.")

if __name__ == "__main__":
    main()
