class saver:
    def __init__(self, message,sender,location):
        self.f=open('message_from_'+sender+'_to_'+location+'.txt','w+')
        self.f.write(message)
