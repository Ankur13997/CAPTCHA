import random
c=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6','7','8','9']
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
    print("INVALID CAPTCHA")
else:
    print("VALID CAPTCHA")
