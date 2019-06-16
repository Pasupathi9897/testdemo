#How do you replace a value associated with the given key if and only if it is currently dictionaryped to given value
dict={'name':'pasupathi','age':'20'}
print(dict)
e=str(input("enter the key"))
if(dict.__contains__(e)):
  print("There")
  dict[e]=input("enter the value")
else:
    print("we cant remove the key")
print(dict)
