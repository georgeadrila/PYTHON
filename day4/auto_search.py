from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
import time

search_query = input("Enter a search query: ")

edge_driver_path = "C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe"

edge_service = EdgeService(edge_driver_path)

browser = webdriver.Edge(service=edge_service)

google_search_url = f"https://www.google.com/search?q={search_query}"

browser.get(google_search_url)
