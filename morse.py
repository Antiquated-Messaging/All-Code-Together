class morse:
	def __init__(self, message):
		self.message = message.lower()
		self.translation = ''
		self.alpha = 'abcdefghijklmnopqrstuvwxyz'
		self.code = [ '.- / ', '-... / ', '-.-. / ', '-.. / ', '. / ', '..-. / ', '--. / ', '.... / ', '.. / ', '.--- / ', '-.- / ', '.-.. / ', '-- / ', '-. / ', '--- / ', '.--. / ', '--.- / ', '.-. / ', '... / ', '- / ', '..- / ', '...- / ', '.-- / ', '-..- / ', '-.-- / ', '--.. / ']
		for x in range(len(self.message)):
			if self.message[x].isalpha():
				self.translation = self.translation + self.code[self.alpha.find(self.message[x].lower())]
			else:
				self.translation = self.translation + self.code[x]
