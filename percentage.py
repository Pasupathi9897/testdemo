# Write a Python program to find the percentage of uppercase letters, lowercase letters, digits and special characters in a given string
str="HDG Vvhbnd V39 8&^%$ % ^& *(344 5 789987 865C jh( * &^%$#$% ^&*(vcg Xgc fxg GHH"
print("the length of the string",len(str))
j=0
a=0
b=0
c=0
d=len(str.split(" "))
for i in range(0,len(str)):
    if(str[i].isupper()):
        j=j+1
    elif(str[i].islower()):
        a=a+1
    elif(str[i].isdigit()):
        b=b+1
    else:
        c=c+1
print("no.of upper case in a string",j)
print("no.of lower case in a string",a)
print("no.of digit case in a string",b)
print("no.of special char in a string",c)
print("percentage of upper case",(j/len(str))*100)
print("percentage of lower",(a/len(str))*100)
print("percentage of digit",(b/len(str))*100)
print("percentage of special char",(c/len(str))*100)