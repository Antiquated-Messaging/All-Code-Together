class Numcode:
	def __init__(self, message):
		self.message=message.lower()
		self.translation = '' 
		self.alpha='abcdefghijklmnopqrstuvwxyz' 
		self.numb=['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26']
		for x in range(len(self.message)):
			if self.message[x].isalpha(): 
				self.numb[x]=self.alpha[x]
				self.translation = self.numb[x]
			else:
				if self.message[x] == '.':
					self.numb[x] == '.'
				elif self.message[x] == ' ':
					self.numb[x] == ' '
				else: 
					self.numb[x] == ''
				self.translation= self.numb[x]
				

		'''for x in range(len(self.message)):
		    if x.isalpha():
		        self.translation.append(str(ord(x)-ord('a') + 1))
		    else:
		        self.translation.append(x)'''

name = Numcode('Test Message...')
print(name.translation)

