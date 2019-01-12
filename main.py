import requests                         # Some modules to import
from bs4 import BeautifulSoup           # This module allows the python to crawl through the pages

file = open('names.xls', 'w')
def crawler(max_pages):     # max_pages defines the number of web pages to crawl before terminating
    page = 1
    while page <= max_pages:
        url = 'https://paytmmall.com/iphone-7-lowest-price-llpid-117718'
        print(url)
        code = requests.get(url)     # the request function gets the source code of the web page whose url is mentioned
        plain = code.text            # The  .text library extracts only the text from that code, it excludes headers, unnecessary code
        soup  = BeautifulSoup(plain, "html.parser")
        # Now to allow the code to crawl through the page using BeautifulSoup function
        # we need to convert that code into a format that Beautiful Soup can understand
        # The BeautifulSoup(this) does that and converts that code into readable format for the Beautiful Soup library


        for data in soup.findAll('a', {'class': '_8vVO'}):      # This line basically searches through the code for <mentioned> tags having class name = <mentioned> and fetches that piece of code
            #print(data)

           # print(data.string + "\t" + str(data.get('href')))

            lurl = "https://www.paytmmall.com" + str(data.get('href'))
            print(str(data.get('title')) + '\t')
            file.write(data.get('title') + '\t')
            get_cost(lurl)



        page += 1
    file.close()

def get_cost(url):
    code  = requests.get(url)
    plain = code.text
    soup  = BeautifulSoup(plain, 'html.parser')
    for data in soup.findAll('span', {'class': '_1y_y'}):
        print(str(data.get('content'))+ "\n")
        file.write("Rs. " + str(data.get('content')) + "\n")


crawler(1)


