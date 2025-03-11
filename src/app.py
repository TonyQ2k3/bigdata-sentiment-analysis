from flask import Flask, render_template, request
import requests
import re
from bs4 import BeautifulSoup
from textblob import TextBlob
from pyspark.sql import SparkSession


app = Flask(__name__)

# Initialize Spark
spark = SparkSession.builder \
    .appName("Yelp Sentiment Analysis") \
    .master("spark://localhost:7077") \
    .getOrCreate() 


@app.route('/', methods=['GET', 'POST'])
def index():
    reviews = []
    sentiments = []
    if request.method == 'POST':
        url = request.form['url']
        reviews = scrape_reviews(url)
        if reviews:
            sentiments = analyze_sentiment(reviews)
            df = create_dataframe(sentiments)
            return render_template('results.html', tables=[df.toPandas().to_html(classes='data')])
    return render_template('index.html', sentiments=sentiments)


def scrape_reviews(url):
    # Send a request to the Yelp URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    regex = re.compile('.*comment.*')
    
    # Extract reviews - this will depend on Yelp's HTML structure
    results = soup.find_all('p', {'class':regex})
    reviews = [result.text for result in results]
    return reviews


def analyze_sentiment(reviews):
    sentiments = []
    for review in reviews:
        blob = TextBlob(review)
        sentiment = blob.sentiment.polarity
        if sentiment > 0:
            sentiments.append('positive')
        elif sentiment < 0:
            sentiments.append('negative')
        else:
            sentiments.append('neutral')
    re = [(review, sentiment) for review, sentiment in zip(reviews, sentiments)]
    print(re[0])
    return re


def create_dataframe(reviews):
    df = spark.createDataFrame(reviews, schema=["review", "sentiment"])
    return df



if __name__ == '__main__':
    app.run(debug=True)