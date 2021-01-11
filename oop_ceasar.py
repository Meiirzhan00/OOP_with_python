class Ceasar:
    def __init__(self,text,key):
        self.text=text
        self.key=key

    def encrypt(self):
        enc=''
        for char in self.text:
            c=ord(char)
            p=chr(c+self.key)
            enc+=p
        return enc

    def decrypt(self):
        dec=''
        for i in self.encrypt():
            c1=ord(i)
            p1=chr(c1-self.key)
            dec+=p1
        return dec

p=Ceasar('Meiirzhan',7)
print(p.encrypt())
print(p.decrypt())
