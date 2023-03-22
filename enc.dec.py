'''
lets have a word of string
# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
# now append three random characters at the starting and the end
# else:
# simply reverse the string

# Decoding:
according to the encoding
'''
import random
#print (random.randint(0,9))

s = "mamun"

#s= s.slice(0,3)
if(len(s)>=3):

    s=s+s[0]
    s3= s[1:len(s)]

    s2=''
    s2 += chr(random.randint(65,90))
    s2 += chr(random.randint(65,90))
    s2 += chr(random.randint(65,90))
    s3 = s2 + s3
    s2=''
    s2 += chr(random.randint(65,90))
    s2 += chr(random.randint(65,90))
    s2 += chr(random.randint(65,90))
    s3=s3+s2
else :
    rev = reversed(s)
    s3 = ''.join(rev)


print(f'encoded : {s3}')



if(len(s3)>=3):
    new2=''
    new = s3[3:len(s3) - 3]
    ch = new[len(new)-1]
    new2 += ch+new[0:len(new)-1]
    print(f'decoded : {new2}')
    