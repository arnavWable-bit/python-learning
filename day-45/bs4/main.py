from bs4 import BeautifulSoup
import requests
# import lxml

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, 'html.parser')

articles = soup.find_all(name="a", class_ = "storylink")
article_texts = []
article_links = []
for article_tag in articles:     
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)
    
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name= "span", class_ ="score")]

# print(article_links)
# print(article_texts)
# print(article_upvotes)


largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)




# from bs4 import BeautifulSoup
# import requests

# # Live Website (will change over time)
# response = requests.get("https://news.ycombinator.com/")
# # Static practice website (below code will not work):
# # response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")

# yc_web_page = response.text
# soup = BeautifulSoup(yc_web_page, 'html.parser')
# articles = soup.find_all(name="span", class_="titleline")
# article_texts = []
# article_links = []
# for article_tag in articles:
#     text = article_tag.getText()
#     article_texts.append(text)
#     link = article_tag.find(name='a').get("href")
#     article_links.append(link)

# # Finding the upvotes
# # If all articles on the page have upvotes, this will work:
# # article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# # However, some submissions may not have any upvotes yet.
# # This uses a conditional expression to handle cases where there are no upvotes (span is None)
# subtexts = soup.findAll(class_="subtext")
# article_upvotes = [int(line.span.span.getText().strip(" points")) if line.span.span else 0 for line in subtexts]

# largest_number = max(article_upvotes)
# largest_index = article_upvotes.index(largest_number)

# print(
#     f"Most upvoted article: {article_texts[largest_index]}\n"
#     f"Number of upvotes: {article_upvotes[largest_index]} points\n"
#     f"Available at: {article_links[largest_index]}."
# )






# with open ("day-45/bs4/website.html") as file:
#     contents = file.read()
    
# soup = BeautifulSoup(contents ,"html.parser")
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

# print(soup)
# print(soup.prettify())

# print(soup.a)                 # prints first a tag in the code
# print(soup.li)
# print(soup.p)


# all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)

# all_para_tags = soup.find_all(name="p")
# print(all_para_tags)

# for tag in all_anchor_tags:
#     # print(tag.getText())
#     print(tag.get("href"))

# heading = soup.find(name="h1", id="name")
# print(heading)

# section_heading = soup.find(name='h3', class_ = "heading")
# print(section_heading)
# print(section_heading.getText())

# company_url = soup.select_one(selector= "p a")
# print(company_url)

# name = soup.select_one(selector= "#name")
# print(name)

# headings = soup.select(".heading")
# print(headings)