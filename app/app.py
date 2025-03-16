from flask import Flask, render_template, request
from scraper.__main__ import main as twitter_scraper
import pandas as pd

app = Flask(__name__)

# Initialize Spark
# spark = SparkSession.builder \
#     .appName("Yelp Sentiment Analysis") \
#     .master("spark://localhost:7077") \
#     .getOrCreate() 

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        # Call the scraping function and get the DataFrame
        df = twitter_scraper(query)

        # Convert DataFrame to HTML
        data_html = df.to_html(classes='data', header="true", index=False)
        return render_template('index.html', data=data_html)

    return render_template('index.html', data=None)



if __name__ == '__main__':
    # twitter_scraper()
    app.run(debug=True)