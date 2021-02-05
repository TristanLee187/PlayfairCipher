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

    #Set the answer depending on the mode. Print the answer with messages. Also detect for extra Xs
    def solve(self):
        print('You entered: \n' + self.text)
        self.fix()
        if self.mode=='encode':
            self.encodeFix()
            self.solveAll()
            self.print()
        else:
            self.solveAll()
            self.print()
            self.xDetect()


    #general fixing: make the text all capital letters and remove punctuation
    def fix(self):
        text=''
        for char in self.text:
            if char.isalpha():
                text+=char.upper()
        self.text=text

    #If encoding, fix the plaintext to: add X in between double letters, add Z to the end of the text if odd length
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
        # if odd length, add Z if the last letter isn't a Z,
        if len(ans) % 2 == 1:
            ans += 'Z' if ans[-1] != 'Z' else 'X'
        self.text = ans

    # Returns the ordered pair representing the position of the character in the array
    def indexOf(self, char):
        index = []
        for i in range(5):
            if char in self.val[i]:
                index.append(i)
                index.append(self.val[i].index(char))
                return index

    #Solve a single pair if they are in the same row
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

    #Solve a single pair if they are in the same column
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

    #Encode or decode a single pair of letters
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

    #Iterate over all pairs, encoding or decoding each of them
    def solveAll(self):
        for i in range(0,len(self.text),2):
            self.ans+=self.solveOne(self.text[i:i+2])

    #detect extra Xs (Xs between duplicate letters) if in decoding mode.
    #Removes all of the Xs and returns True if they exist, otherwise return False
    #Prints a corresponding message
    def xDetect(self):
        if 'X' in self.ans and self.mode == 'decode':
            pass
        else:
            return False
        ans=''
        for i in range(len(self.ans)):
            #if current character is an x and characters on either side are the same, don't put the X in the answer
            if 0<i<len(self.ans) and self.ans[i]=='X' and self.ans[i-1]==self.ans[i+1]:
                pass
            #otherwise, put it in the answer
            else:
                ans+=self.ans[i]
        self.ans=ans
        print('Possible extra Xs were detected in the result. A possible alternate message is: \n' + self.ans)
        return True

    #Print the result of the encryption or straightforward decryption (no removal of extra Xs or Zs)
    def print(self):
        print('The ' + self.mode + 'd ' + 'result: \n' + self.ans)


p=Playfair(sys.argv)
p.solve()

#TEST TEST Test