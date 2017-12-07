#Encoding a Message

class Encoding:

	def __init__(self, message):
		self.message = message

	def encode(self):
		list1 = list(self.message)
		


code1 = Encoding(str(input('What message would you like to encode?')))
code1.encode()
