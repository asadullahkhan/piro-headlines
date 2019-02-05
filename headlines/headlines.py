#piro-headlines {get real time news along with analysis }
import feedparser
from flask import Flask, render_template, request

app = Flask(__name__)

RSS_FEEDS = {'ent':'https://economictimes.indiatimes.com/small-biz/entrepreneurship/rssfeeds/11993034.cms',
             'fin': 'https://economictimes.indiatimes.com/industry/banking/finance/rssfeeds/13358259.cms',
             'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest',
             'iol': 'http://www.iol.co.za/cmlink/1.640',
             'bs': 'https://www.business-standard.com/rss/news-ians-education-15009.rss'}


@app.route("/")
def get_news():
        query = request.args.get("publication")
        if not query or query.lower() not in RSS_FEEDS:
                publication = "cnn"
        else:
                publication = query.lower()
        feed = feedparser.parse(RSS_FEEDS[publication])
        return render_template("home.html",articles=feed['entries'])


if __name__ == "__main__":
    app.run(port=8000, debug = True)