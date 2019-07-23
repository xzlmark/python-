from XzlMysql import XzlMysql

xzl = XzlMysql('localhost', 'root', '123456', 'xzlmark')
xzl.connect()


# 查询操作-所有结果
# res = xzl.get_all('select * from student;')
# for row in res:
#     print('id={0}\t姓名={1}\t年龄={2}\t性别={3}\t地址={4}\t是否删除={5}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))

# # 插入操作，要注意后面括号中字符串需要用引号
# sql = r'insert into student(name,age,gender,address,isDelete) values ("向天秀",55,0,"万源市玉带乡",0);'
# res = xzl.insert(sql)
# print(res)


# 修改操作，
# sql = r'update student set name ="熊林祥" where id =1;'
# res = xzl.insert(sql)
# print(res)


# 删除操作，
sql = r'delete from student where id=1;'
res = xzl.insert(sql)
print(res)