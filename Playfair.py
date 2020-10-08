import sys

class Playfair():
    def __init__(self,args):
        #Set to encryption or decryption mode
        self.mode=args[1]

        #Initialize the plain or ciphertext
        self.text=args[2]

        # Initialize key
        self.val = []
        for i in range(0, 25, 5):
            self.val.append(args[3][i:i + 5])

    #returns the ordered pair of the character in the array
    def indexOf(self,char):
        index=[]
        for i in range(5):
            if char in self.val[i]:
                index.append(i)
                index.append(self.val[i].index(char))
                return index

    #fix the plaintext to: add X in between double letters, add Z to the end of the text if odd length
    def fix(self):
        ans=''
        window=[]
        for char in self.text:
            if len(window)<2:
                window+=char
            if len(window)==2:
                if window[0]==window[1]:
                    ans+=window[0]+'X'
                    window[0]=window[1]
                    window.pop()
                else:
                    ans+=''.join(window)
                    window.clear()
        ans+=''.join(window)
        if len(ans)%2==1:
            ans+='Z'
        self.text=ans

    # def encode(self):


    def print(self):
        print(self.mode)
        print(self.text)
        print(self.val)

p=Playfair(sys.argv)
p.fix()
p.print()