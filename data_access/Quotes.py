from Quote import Quote
import json

class Quotes:
	def __init__(self, quotesList):
		self.quoteObjList = []
		for quotes in quotesList:
			self.quoteObjList.append(Quote(quotes))

	def getQuote(self, quoteid):
		for obj in self.quoteObjList:
			if obj.id == quoteid:
				return obj

	def getJSON(self):
		IDList = []
		for obj in self.quoteObjList:
			IDList.append(obj.getID())
		return IDList

	def getListOfQuoteObj(self):
		return self.quoteObjList

	def setListOfQuoteObj(self, quotesList):
		self.quoteObjList = []
		for quotes in quotesList:
			self.quoteObjList.append(Quotes(quotes))

'''info = [{'quoteID':'d90b9067-1f19-4dfd-9ee8-de57985e1765', 'text':'this is a quote','characters':{'person1':'joey'}}, {'quoteID':'09c85b96-173f-4fae-8380-f742c08fb25f', 'text':'this is also a quote','characters':{'person1':'rach'}}]

quotes = Quotes(info)
print ((quotes.getQuote('d90b9067-1f19-4dfd-9ee8-de57985e1765')).getCharactersObj()).getNameByKey('person1')

#print (quotes.getQuote('d90b9067-1f19-4dfd-9ee8-de57985e1765')).getJSON()'''
