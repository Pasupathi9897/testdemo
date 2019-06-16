''''
#open a file
fo=open("C:\\Users\\DELL\\Desktop\\first.txt","wb")
print("name of the file:",fo.name)
print("closef or not :",fo.closed)
print("opening mode:",fo.mode)



'''
'''

fh=open("pasu2.txt","w+")
fh.write("put the text you want to add here")
fh.write("and more lines if need be")
fh.close()
'''
'''
fh=open("pashu_new_list.txt","w")
line=["one line of the text here","another line of text here","and yet another line"]
fh.writelines(line)
fh.close
'''
'''
fh=open("pasu2.txt","a")
fh.write("pasupathi nadh")
fh.close
'''
fh=open("pashu_new_list.txt","r+")
#test=fo.readlines()
for line in fh:
 print(line)
fh.close()