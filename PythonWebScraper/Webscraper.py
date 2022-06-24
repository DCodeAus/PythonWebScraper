#first part of this script is to install the python requeusts library, insert the line below in powershell (you need to ensure you have admin settings)
#python -m pip install requests

import requests
#this imports the package requests
#to use beautiful soup you will need to install another package
#python -mpip install beautifulsoup4
#this package is a library for passing structured data
from bs4 import BeautifulSoup

#pointing at a fake site for this test script
URL="https://realpython.github.io/fake-jobs/"
#uses the HTTP get request from the URL stated above, retreives the data and stores it in a python object
page = requests.get(URL)
#takes page.content, and creates a beautiful soup object as its input.
soup = BeautifulSoup(page.content, "html.parser")
#finds the specific html element by its ID, in this case Results Container
results = soup.find(id="ResultsContainer")
#prints the text
print(results.prettify())