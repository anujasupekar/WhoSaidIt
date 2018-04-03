from Character import Character

class Characters:
	def __init__(self, charInfo):
		self.listOfCharObj = []
		for key, val in charInfo.items():
			self.listOfCharObj.append(Character(key,val))

	def getListOfCharObj(self):
		return self.listOfCharObj

	def setListOfCharObj(self, charInfo):
		listOfCharObj = []
		for key, val in charInfo.items():
			self.listOfCharObj.append(Character(key,val))

	def getJSON(self):
		listOfKeys = []
		for char in self.listOfCharObj:
			listOfKeys.append(char.key)
		return listOfKeys

	def getNameByKey(self, key):
		for obj in self.listOfCharObj:
			if key == obj.key:
				return {'name':obj.name}

'''characters = Characters({'Person 1':'Joey','Person 2':'Ross'})
print characters.getNameByKey('Person 1')
print'''
