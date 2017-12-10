class morse:
	def __init__(self, message):
		self.message = message.lower() #Original message, lower case the entire message.
		self.translation = '' # Stores the translation into the output morse code.
		self.alpha = 'abcdefghijklmnopqrstuvwxyz' #directory for alphabet letters
		self.code = [ '.- / ', '-... / ', '-.-. / ', '-.. / ', '. / ', '..-. / ', '--. / ', '.... / ', '.. / ', '.--- / ', '-.- / ', '.-.. / ', '-- / ', '-. / ', '--- / ', '.--. / ', '--.- / ', '.-. / ', '... / ', '- / ', '..- / ', '...- / ', '.-- / ', '-..- / ', '-.-- / ', '--.. / ']
		#Above is the directory for all the morse code translations from letters. 
		

		for x in range(len(self.message)):
			#translate the characters one by one by finding the index of the character in the alphabet 
			#and corresponding it with the same index in the morse code directory
			if self.message[x].isalpha():
				self.translation = self.translation + self.code[self.alpha.find(self.message[x].lower())]
			else:
				self.translation = self.translation + self.code[x]
