from flask import Flask, render_template
from scraper import ArticleScraper
from textprocessor import TextProcessor

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

@app.route("/display")
def display():
    ticker = "ABCD"
    return render_template('display.html', ticker=ticker)