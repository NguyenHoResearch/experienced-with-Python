"""-----What will I learn in this project-----
- 1. What is Web Scraping?
- 2. Understanding HTML Structure
- 3. Using requests to Fetch Web Pages  
- 4. Using BeautifulSoup for Parsing
- 5. Project 21: Wikipedia Article Scraper
"""

# %% 1. What is Web Scraping?
# Web scraping is the process of extracting information from websites.
# It's commonly used for data collection, market research, content aggregation, automation tasks.

# %% 2. Understanding HTML Structure
# Create index.html file.

# %% 3. Using requests to Fetch Web Pages Using 
import requests

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
response = requests.get(url)

if response.status_code == 200:
    print(response.text[:500])
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

# %% 4. BeautifulSoup for Parsing
from bs4 import BeautifulSoup

html_content = "<h1>Main Title</h1><p>This is a sample paragraph</p><a href='https://example.com'>Click here</a>"
soup = BeautifulSoup(html_content, "html.parser")

print(soup.h1.text)
print(soup.p.text)

# %% 5. Project 21: Wikipedia Article Scraper
# Wikipedia Article Scraper
import requests
from bs4 import BeautifulSoup

# Step 1: Get Wikipedia Article URL
def get_wikipedia_page(topic):
  url = f"https://en.wikipedia.org/wiki/{topic.replace(' ', '_')}"
  response = requests.get(url)
  if response.status_code == 200:
    return response.text
  else:
    print(f"Failed to retrieve data. Status code: {response.status_code}. Check the topic and try again")
    return None

# Step 2: Extract Article Title
def get_article_title(soup):
  return soup.find('h1').text

# Step 3: Extract Article Summary
def get_article_summary(soup):
  paragraphs = soup.find_all('p')
  for para in paragraphs:
    if para.text.strip():
      return para.text.strip()
  return "No summary found"

# Step 4: Extract Headings
def get_headings(soup):
  headings = [heading.text.strip() for heading in soup.find_all(['h2', 'h3', 'h4'])]
  return headings

# Step 5: Extract Related Links
def get_related_links(soup):
  links = []
  for a_tag in soup.find_all('a', href=True):
    href = a_tag['href']
    if href.startswith('/wiki/') and ":" not in href:
      links.append(f"https://en.wikipedia.org{href}")
  return list(set(links))[:5]

# Step 6: Main Program
def main():
  topic = input("Enter a topic to search on Wikipedia: ").strip()
  page_content = get_wikipedia_page(topic)

  if page_content:
    soup = BeautifulSoup(page_content, 'html.parser')
    title = get_article_title(soup)
    summary = get_article_summary(soup)
    headings = get_headings(soup)
    related_links = get_related_links(soup)

    print("\n--- Wikipedia Article Details ---")
    print(f"\nTitle: {title}")
    print(f"\nSummary: {summary}")
    print("\nHeadings:")
    for heading in headings[:5]:
      print(f"- {heading}")

    print("\nRelated Links:")
    for link in related_links:
      print(f"- {link}")

# Run Program
if __name__ == "__main__":
  main()
# %%
