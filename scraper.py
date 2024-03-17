from selenium import webdriver

class ArticleScraper:
  
  def __init__(self, ticker, driver, base_url):
    self.ticker = ticker
    self.driver = webdriver.Chrome
    self.base_url = base_url

  # initializes webdriver instance
  def initializeScraper():
    pass

  # uses ticker instance variable and return a list of article links
  def getArticleLinks():
    pass

  # scrapes the article at the given link and returns the text
  # could also just scrape the article headlines rather than full articles
  # would make this method irrelevant
  def scrapeArticle(articleLink):
    pass
  
  # destroys webdriver instance
  def closeScraper():
    pass

