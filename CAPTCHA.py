import random
c='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
l=len(c)

m=random.randrange(l+1)
n=random.randrange(l+1)
o=random.randrange(l+1)
p=random.randrange(l+1)
x=c[m]+c[n]+c[o]+c[p]
print(x)
print("")
y=input("ENTER CAPTCHA: ")
print("")
print("")
if x!=y:
    print("!!! INVALID CAPTCHA !!!")
else:
    print("### VALID CAPTCHA ###")
