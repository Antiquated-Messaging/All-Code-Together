class Numcode:
	def __init__(self, message):
		self.message=message.lower()
		self.translation = '' 
		self.alpha='abcdefghijklmnopqrstuvwxyz' 
		self.numb=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
		for x in range(len(self.message)):
			if self.message[x].isalpha(): 
				self.translation = self.translation + self.numb[self.alpha.find(self.message[x])]
			else:
				if self.message[x] == '.':
					self.numb[x] == '.'
				elif self.message[x] == ' ':
					self.numb[x] == ' '
				else: 
					self.numb[x] == ''
				self.translation= self.translation + self.message[x]

name = Numcode()
print(name.translation)

