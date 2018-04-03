from Characters import Characters
#import json

class Quote:
	def __init__(self, quotesDict):
		self.id = quotesDict['quoteID']
		self.text = quotesDict['text']
		self.charactersObj = Characters(quotesDict['characters'])

	def getJSON(self):
		return {
			'quoteID':self.id,
			'text':self.text,
			'characters':self.charactersObj.getJSON(),
		}

	def getID(self):
		return self.id

	def getText(self):
		return self.text

	def getCharactersObj(self):
		return self.charactersObj

	def setID(self, quoteid):
		self.id = int(quoteid)

	def setText(self, text):
		self.text = text

	def setCharactersObj(self, charcterDict):
		self.charactersObj = Characters(charcterDict)
		

'''quote = Quote({'quoteID':'d90b9067-1f19-4dfd-9ee8-de57985e1765', 'text':'this is a quote','characters':{'person 1':'joey','person 2':'Ross'}})

print (quote.getCharactersObj()).getNameByKey('person 1')
print'''