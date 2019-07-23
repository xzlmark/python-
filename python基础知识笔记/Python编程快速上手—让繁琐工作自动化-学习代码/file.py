import os
print(os.getcwd())

file=open(os.getcwd()+'\\file.txt')
print(file.read())
file.close()

file1=open('file.txt','w')
file1.write('熊珍龙，你好呀\n')
file1.close()

file2=open('file.txt','a')
file2.write('周莉，你好')
file2.close()
