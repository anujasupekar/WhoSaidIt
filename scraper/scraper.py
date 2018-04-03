import bs4
from urllib import urlopen
import uuid
import json

URL = "http://www.imdb.com/title/tt0108778/trivia?tab=qt&ref_=tt_trv_qu"
FILE_PATH = '/Users/gautam/anuja/WhoSaidIt/data/quoteData.json'

def getCharacters(quote):
	characters = quote.find_all('a')
	characterDict = {}
	for character in characters:
		characterDict[character['href']] = character.get_text().encode('utf8')
	mappingNames = {}
	i = 1
	for val in characterDict.values():
		mappingNames['Person '+str(i)] = val
		i += 1
	return mappingNames

def extractQuote(quote):
	quote = quote.find(class_='sodatext')
	text = quote.get_text().encode('utf8').strip()
	nameOfChars = getCharacters(quote)
	for key, value in nameOfChars.items():
		text = text.replace(value, key)
	quoteDict = {
		'quoteID' : str(uuid.uuid4()),
		'text' : text,
		'characters' : getCharacters(quote)
	}
	return quoteDict

def main():
	print 'Connecting to the URL'
	webpage = urlopen(URL)
	soup = bs4.BeautifulSoup(webpage, "lxml")
	print 'Scraping the webpage'
	quotes = soup.find_all(class_='quote')
	cleanedQuotes = []
	print 'Extracting the data'
	for quote in quotes:
		cleanedQuotes.append(extractQuote(quote))
	print 'Converting to json'
	quotesData = json.dumps(cleanedQuotes)
	print 'Writing data to the file'
	f = open(FILE_PATH , 'w')
	f.write(quotesData)
	f.close()

if __name__ == '__main__':
	main() 