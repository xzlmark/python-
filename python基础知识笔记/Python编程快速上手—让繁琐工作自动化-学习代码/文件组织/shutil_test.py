import shutil,os
os.chdir('C:\\')
#copy第一参数即文件和第二个参数（目录）必须存在，否则会报FileNotFoundError错误；第二个参数如果为文件名，
#则是修改文件名称;返回值是复制后的文件路径
print(shutil.copy('C:\\test.txt','C:\\1.txt'))
print(shutil.copy('C:\\test.txt','C:\\test\\1.txt'))

#批量删除.txt结尾的文件
'''  os.unlink(path)  删除path处的文件；
    os.rmdir(path)    删除空文件夹
    shutil.rmtree(path)删除ahth处的所有文件和文件夹,在运用这个函数时，要注意
    可以先用打印语句打出要删除的文件，然后在执行，如下例
'''
for name in os.listdir('C:\\test'):
    if name.endswith('.txt'):
      print(name)
      os.unlink(name)



