import os
#利用os.walk()函数遍历目录树,返回有三个值：第一个是当前文件夹名称的字符串；
#第二个是当前文件夹中子文件夹的字符串的列表
#第三个是当前文件夹中文件的字符串的列表
for folderName,subfolders,filenames in os.walk('C:\\test'):
    print('当前目录是：'+folderName)

    for subfolder in subfolders:
        print('subfolder of '+folderName+':'+subfolder)
    for filename in filenames:
        print('file inside '+folderName+':'+filename)
    print(' ')
