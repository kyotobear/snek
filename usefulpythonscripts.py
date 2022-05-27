"""
Write a Python program to access and print a URL's content to the console.
"""
import requests
url = requests.get("http://google.com")
htmltext = url.text
# from http.client import HTTPConnection
# conn = HTTPConnection("https://twitter.com/home")
# conn.request("GET", "/")
# result = conn.getresponse()
# contents = result.read()
# print(contents)