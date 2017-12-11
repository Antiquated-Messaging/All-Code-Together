class Numcode: #This class is for the number converter and is in the same folder as the other programs.
	def __init__(self, message): #message is the only input carried over and is a string.
		self.message=message.lower()#turns all inputted messages into lower case, since numbers are not dependent on the letter's case. 
		self.translation = '' #Translation is a string 
		self.alpha='abcdefghijklmnopqrstuvwxyz' 
		self.numb=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26'] #list of numbers that will be compared to the letters
		for x in range(len(self.message)): #goes through the message string
			if self.message[x].isalpha(): #if any character in the message is a letter, the translation string adds the number to the string that is at the same position as the letter is in its alpha index.
				self.translation = self.translation + self.numb[self.alpha.find(self.message[x])]
			else:
				self.translation= self.translation + self.message[x] #otherwise, if message isn't a letter, maintain its character in the translation. 
