import requests
from bs4 import BeautifulSoup
import os
import PyPDF2
from alive_progress import alive_bar
import fnmatch
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
#from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
import circlify
#import seaborn as sns
#import matplotlib.pyplot as plt

class BookAnalysis:


    def __init__(self, url, pdf_dir, txt_dir, png_dir):
        self._url = url
        self._pdf_dir = pdf_dir
        self._txt_dir = txt_dir
        self._png_dir = png_dir

    def get_urls(self):
        page = requests.get(self._url)
        soup = BeautifulSoup(page.content, 'html.parser')

        try:
            divs = soup.find_all('div', class_='bookContainer grow')
            with open(f'book_urls.txt', 'w') as fd:
                for div in divs:
                    book_url = div.findChild('a', href=True)['href']

                    download_url = self._url + book_url
                    download_page = requests.get(download_url)
                    download_soup = BeautifulSoup(download_page.content, 'html.parser')
                    footer = download_soup.find('div', {'id' : 'footer'})
                    file_name = footer.contents[0]

                    full_url = download_url + file_name
                    fd.write(full_url + '\n')
        except:
            pass
    
    def get_pdfs(self):
        os.system("./get_books.sh")

    def to_text(self):
    	total = len(fnmatch.filter(os.path.join(self._pdf_dir), '*.pdf'))
    	counter = 1
    	for filename in os.listdir(self._pdf_dir):
    		pdfFileObj = open(os.path.join(self._pdf_dir, filename), 'rb')
    		try:
    			pdfReader = PyPDF2.pdfReader(pdfFileObj)
    			text_filename = filename.replace('.pdf', '.txt')
    			with open(os.path.join(self._txt_dir, text_filename), "w") as f:
    				print(f'Book {counter}/{total} : {filename}...')
    				with alive_bar(pdfReader.numPages) as bar:
    					for page in range(pdfReader.pages):
    						pageObj = pdfReader.getPage(page)
    						f.write(pageObj.extractText() + '\n\n')
    						bar()
    				pdfFileObj.close()
    			counter += 1
    		except:
    			pass

if __name__ == '__main__':
    url =  'https://books.goalkicker.com/'
    pdf_dir = '/home/kali/Documents/Electiva3/pdfs/'
    txt_dir = '/txt'
    png_dir = '/figures'
    ba = BookAnalysis(url, pdf_dir, txt_dir, png_dir)
    #ba.get_urls()
    #ba.get_pdfs()
    ba.to_text()
    #ba.word_freq()
        