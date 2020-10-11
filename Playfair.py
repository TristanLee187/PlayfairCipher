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

        #Initialize the result of decryption or encryption
        self.ans=''

    #returns the ordered pair of the character in the array
    def indexOf(self,char):
        index=[]
        for i in range(5):
            if char in self.val[i]:
                index.append(i)
                index.append(self.val[i].index(char))
                return index


    def solve(self):
        if self.mode=='encode':
            self.encodeFix()
            self.solveAll()

    # if encoding, fix the plaintext to: add X in between double letters, add Z to the end of the text if odd length
    def encodeFix(self):
        ans = ''
        # store two characters at a time
        window = []
        for char in self.text:
            # add character to the window if it needs more
            if len(window) < 2:
                window.append('I' if char=='J' else char)
            if len(window) == 2:
                # fix duplicate letter problem
                if window[0] == window[1]:
                    ans += window[0] + 'X'
                    window[0] = window[1]
                    window.pop()
                # just append if no problem
                else:
                    ans += ''.join(window)
                    window.clear()
        ans += ''.join(window)
        # add Z if odd length
        if len(ans) % 2 == 1:
            ans += 'Z'
        self.text = ans

    #solve a single pair if they are in the same row
    def solveHorizontal(self,coors1,coors2):
        x = coors1[0]
        ans=''
        if self.mode=='encode':
            #use the row below
            ans += self.val[(x + 1) % 5][coors1[1]]
            ans += self.val[(x + 1) % 5][coors2[1]]
        else:
            #use the row above
            ans += self.val[(x - 1) % 5][coors1[1]]
            ans += self.val[(x - 1) % 5][coors2[1]]
        return ans

    #solve a single pair if they are in the same column
    def solveVertical(self,coors1,coors2):
        y = coors1[1]
        ans=''
        if self.mode=='encode':
            #use column to the right
            ans += self.val[coors1[0]][(y + 1) % 5]
            ans += self.val[coors2[0]][(y + 1) % 5]
        else:
            #use column to the left
            ans += self.val[coors1[0]][(y - 1) % 5]
            ans += self.val[coors2[0]][(y - 1) % 5]
        return ans

    #encode a single pair of letters
    def solveOne(self,pair):
        coors1=self.indexOf(pair[0])
        coors2=self.indexOf(pair[1])
        ans=''
        #same row -> use solveHorizontal
        if coors1[0]==coors2[0]:
            ans+=self.solveHorizontal(coors1,coors2)
        #same column -> use solveVertical
        elif coors1[1]==coors2[1]:
            ans+=self.solveVertical(coors1,coors2)
        #different column and row -> use the same row, column of the other letter
        else:
            ans+=self.val[coors1[0]][coors2[1]]
            ans+=self.val[coors2[0]][coors1[1]]
        return ans

    #iterate over all pairs, encoding each of them
    def solveAll(self):
        for i in range(0,len(self.text),2):
            self.ans+=self.solveOne(self.text[i:i+2])

    def print(self):
        print('You entered: ' + self.text)
        print('The result: ' + self.ans)


p=Playfair(sys.argv)
p.solve()
p.print()