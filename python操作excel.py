import os
import xlrd


file_name='test.xlsx'  # 打开的文件名

path = os.getcwd() + '\\' + file_name  # 文件的路径

rdata = xlrd.open_workbook(path)  # 打开文件，得到一个xlrd.book.Book对象
'''
sheets = rdata.nsheets  # sheet 个数

snames = rdata.sheet_names()  # sheets 每个名字,是列表 ['Sheet1', '改户主', 'Sheet2', '模板数据多余']

sheet1 = rdata.sheet_by_index(0)  # 第一个sheet表格
nrows = sheet1.nrows  # 行数
ncols = sheet1.ncols  # 列数
# print('行数有{0}行'.format(nrows)+';列数有{0}列'.format(ncols))

row_value = sheet1.row(0)  # 读取第一行的内容，格式是列表，里面是键值对 [text:'县（市、区）',empty:'']
row_values = sheet1.row_values(1)  # 获取第一行数据，格式是列表['宣汉县', '东乡镇', '南岸社区居委会']

col_value = sheet1.col(0)  # 读取第一列数据，列表格式[text:'县（市、区）', text:'宣汉县']
col_values = sheet1.col_values(0)  # 只读取值
_r = sheet1.row_values(1)[1:5]  # 读取第二行 第2列-5列数据 ['东乡镇', '南岸社区居委会', '6组', '513022197901287292']
_c = sheet1.col_values(1)[1:5]  # 读取第二列第2行-5行数据
_rs = sheet1.row_values(1,1,5)  # 这个与sheet1.row_values(1)[1:5] 是一样的功能


cell = sheet1.cell(1,1).value  # 读取（1,1）单元格的值
print(cell)
'''

'''
修改Excel
import xlutils
from xlutils import copy    # xlutils中导入copy

new_book=copy.copy(rdata)  # 然后用xlutils里面的copy功能，复制一个excel
sheet=new_book.get_sheet(0)  # 获取sheet页
sheet.write(0,1,'张三')  # 修改第0行，第一列
sheet.write(1,1,'小军')   # 修改第一行，第一列
new_book.save('stu.xls')
'''

import xlwt
import xlrd
import xlutils

# 写excel
book=xlwt.Workbook()
sheet=book.add_sheet('sheet1')
# sheet.write(0,0,'id')  #指定行和列内容
# sheet.write(0,1,'username')
# sheet.write(0,2,'password')
#
# sheet.write(1,0,'1')
# sheet.write(1,1,'niuhanyang')
# sheet.write(1,2,'123456')

stus=[
    [1,'njf','1234'],
    [2,'njf1','1234'],
    [3,'njf2','1234'],
    [4,'njf3','1234'],
    [5,'njf4','1234'],
    [6,'njf5','1234'],
    [7,'njf6','1234'],
    [8,'njf7','1234'],
    [9,'njf8','1234'],
    [10,'njf9','1234'],
]
line=0  #控制的是行
for stu in stus:
    col=0
    for s in stu:
        sheet.write(line,col,s)
        col+=1
    line+=1

book.save('stu.xls')