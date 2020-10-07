import sys

class Playfair():
    def __init__(self,keytext,pctext):
        #Initialize key
        self.val=[]
        for i in range(0,25,5):
            self.val.append(keytext[i:i+5])

        #Initialize the plain or ciphertext
        self.text=pctext

    def indexOf(self,char):
        index=[]
        for i in range(5):
            if char in self.val[i]:
                index.append(i)
                index.append(self.val[i].index(char))
                return index

    def print(self):
        print(self.val)
        #print(self.indexOf('M'))

p=Playfair(sys.argv[3],sys.argv[2])
p.print()