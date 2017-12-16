import textwrap

class cipher():

    def __init__(self,plain_text,key):
        self.plain_text=plain_text
        self.key=key

    def matrix(self,key):
        if 'i' in key or 'j' in key:
            key=key+'abcdefghklmnopqrstuvwxyz'
        else:
            key=key+'abcdefghiklmnopqrstuvwxyz'

        mat=''
        for i in key:
            if i not in mat:
                mat=mat+i
        matrix=[[0 for j in range(5)] for i in range(5)]
        k=0
        for i in range(5):
            for j in range(5):
                matrix[i][j]=mat[k]
                k=k+1
        return(matrix,mat)

    def repetation_correction(self,plain_text):
        if len(plain_text)%2!=0:
            plain_text=plain_text+'x'
        text=textwrap.wrap(plain_text,2)
        return(text)

    def check(self,plain_text,key):
        text=self.repetation_correction(plain_text)
        matrix,mat=self.matrix(key)

        c=''
        for i in range(len(text)):
            temp=[]
            temp2=[]

            if text[i][0]==text[i][1]:
                text[i]=text[i][0]+'x'

            temp.append(int(mat.index(text[i][0])/5))
            temp.append(mat.index(text[i][0])%5)
            temp2.append(int(mat.index(text[i][1])/5))
            temp2.append(mat.index(text[i][1])%5)

            if temp[0]==temp2[0]:
                c=c+ matrix[temp[0]][(temp[1]+1)%5]
                c=c+ matrix[temp2[0]][(temp2[1]+1)%5]
        
            elif temp[1]==temp2[1]:
                c=c+ matrix[(temp[0]+1)%5][temp[1]]
                c=c+ matrix[(temp2[0]+1)%5][temp2[1]]
        
            else:
                c=c+ matrix[temp[0]][temp2[1]]
                c=c+ matrix[temp2[0]][temp[1]]
        return(c)

    def display(self,plain_text,key):
        print('Ciphered text:',self.check(plain_text,key))

            
plain_text="".join(input("Enter plain text: ").split())
key=input("Enter the key: ")
k=cipher(plain_text,key)
k.display(plain_text,key)
