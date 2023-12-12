import streamlit as st
from selenium import webdriver

st.title("Proxy scrape testing")

if st.button("Start scrape"):

    # Start selenium webdriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)

    driver.get("https://webscraper.io/test-sites/e-commerce/allinone")



