#How do you remove a key-value pair from a dictionary if and only if the specified key is currently dictionaryped to given value
dict={'name':'pasupathi','age':'20'}
print(dict)
e=str(input("enter the key"))
if(dict.__contains__(e)):
  print("There")
  del dict[e]
else:
    print("we cant remove the key")
print(dict)

