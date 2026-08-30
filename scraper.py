import requests
import csv
from bs4 import BeautifulSoup

base_url = "https://quotes.toscrape.com/page/{}/"

with open("data/quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote", "Author", "Tags"])

    total = 0

    for page in range(1, 4):
        response = requests.get(base_url.format(page))
        soup = BeautifulSoup(response.text, "html.parser")

        for quote in soup.find_all("div", class_="quote"):
            text = quote.find("span", class_="text").text.strip()
            author = quote.find("small", class_="author").text.strip()
            tags = ", ".join(tag.text for tag in quote.find_all("a", class_="tag"))

            writer.writerow([text, author, tags])
            total += 1

print(f"{total} quotes scraped successfully!")