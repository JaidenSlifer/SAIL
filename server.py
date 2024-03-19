from flask import Flask, render_template, request
from scraper import ArticleScraper
from textprocessor import TextProcessor

class ServerController:
    
    def __init__(self, name):
        self.app = Flask(name)


    # add all server endpoints using this method
    # endpoint is the route to attach to the handler
        # '/example'
    # route parameters are defined inside angle brackets in the endpoint
        # '/index/<param>'
    # and in the handler function as an argument
        # index(param)
    # route methods are GET, HEAD by default, additional can be defined in the methods param as a list of strings
        # methods=['GET', 'POST', etc]
    def add_endpoint(self, endpoint: str, endpoint_name: str, handler, methods=None):
        self.app.add_url_rule(rule=endpoint, endpoint=endpoint_name, view_func=handler, methods=methods)

    # add all routes here
    def init_routes(self):
        self.add_endpoint('/', 'index', index, methods=['GET', 'POST'])
        self.add_endpoint('/display', 'display', display)

    def run(self, debug: bool):
        self.app.run(debug=debug)

def index():
    return render_template('index.html')

def display():
    if request.method == 'POST':
        print(request.form['text'])
    ticker = "ABCD"
    return render_template('display.html', ticker=ticker)