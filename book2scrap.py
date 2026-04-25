
import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd

st.set_page_config(page_title="Book Analyzer",layout="wide")

st.title("Book price & Rating Analyzer")


url="https://books.toscrape.com/"
response=requests.get(url)

soup = BeautifulSoup(response.text,"html.parser")

books = soup.find_all("article",class_="product_pod")

data = []

for book in books:
    title = book.h3.a["title"]

    price = book.find("p",class_="price_color").text

    rating=book.p["class"][1]

    data.append([title,price,rating])

df = pd.DataFrame(data,columns=['title','price','rating'])

st.dataframe(df)