from dotenv import load_dotenv
import os
from newsapi import NewsApiClient
from flask import Flask

load_dotenv()
api_env = "API_KEY"
key = os.getenv(api_env)
#init
newsapi = NewsApiClient(key)
countries = ["gb", "de", "us", "no"]

def news_loop(land):
    news = newsapi.get_top_headlines(country=land )
    for item in news["articles"]:
        return ("<h2>" +item["title"] + 
                """</h2> 
                <br>""" + item["description"] + "<br>" + item["url"] + "<br><br>")

app= Flask(__name__)

@app.route("/")

def index():
    returnstr=""
    for land in countries:
        print(land)
        news = newsapi.get_top_headlines(country=land )
        for item in news["articles"]:
            returnstr += "<h2>" + str(item["title"]) + "</h2><br>" + str(item["description"]) + "<br>" + """
            <a href="
            """ +str(item["url"]) + """
            ">"
             """ + str(item["url"]) + "</a>" + "<br><br>"
    return returnstr
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)