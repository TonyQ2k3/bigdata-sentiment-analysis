FROM python:3.10.10

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

# Run the application
CMD ["python", "crawl_product_reviews.py"]