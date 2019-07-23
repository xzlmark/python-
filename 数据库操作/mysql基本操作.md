一、基本命令

1、启动服务：

​	说明：以管理员身份运行cmd

​	格式：net start 服务名称

​	例如：net start mysql

2、停止服务

​	说明：以管理员身份运行cmd

​	格式：net stop 服务名称

​	例如：net stop mysql

3、连接数据库

​	格式：mysql -u 用户名 -p

​	例如：mysql -u root -p

4、退出登录（断开连接）

​	quit 或 exit

5、查看版本（连接后操作）

​	示例：select version();

6、显示当前时间

​	示例：select now()

7、远程连接

​	格式：mysql -h ip地址 -u 用户名 -p



二、数据库操作

​	1、创建数据库

​		格式：create database 数据库名 charset=utf8;

​	2、删除数据库

​		drop database 数据库名;

​	3、切换数据库

​		use database 数据库名;

​	4、查看当前选择的数据库

​		selet database();

三、表操作

​	1、查看当前数据库中所有表

​		show tables;

​	2、创建表

​		格式：create table 表名 (列及类型 )

​		示例：**create table student(id int auto_increment primary key,name varchar(20) not null,age int not null,gender bit default 1,address varchar(64),isDelete bit default 0);**

​	3、删除表

​		drop table 表名;

​	4、查看表结构

​		desc 表名;

​	5、查看建表语句

​		格式：show create table 表名;

​	6、重命名表名

​		rename table 原表名 to 新表名;

​	7、修改表

​		alter table 表名 add|change|drop 列名 类型;

四、数据操作

1、增

​	a、全列插入：insert into 表名 values();  注意：主键列是自动增长，但是在全列插入时需要占位，通常使用0

​		例如：insert into student values(0,"tom",1,18,"四川省宣汉县");

​	b、缺省插入

​		insert into 表名(列1，列2...) valuses (值1，值2...);

​		insert into student(name,age,gender,address) values ('jack',33,0,'万源市');

​	c、同时插入多条数据

​		insert into 表名 values (...),(...),...

​		insert into student values (0,"tom3",18,1,"四川省宣汉县",0),(0,"lili",50,0,"四川省宣汉县东乡镇",0);

2、删

​	delete from 表名 where 条件；

4、改



5、查

​	select * from 表名

五、查

1、基本语法  

​		格式：select * from  表名

​		from 关键字后面是表名，表示数据来源于这张表；select后面写表中的列名，如果* 表示在结果集中显示所有的列；在select后面的列门部分，可以用as为列名起别名，这个别名显示在结果集中；如果要查询多个列，之间使用逗号分隔

2、消除重复行

​	在select后面列前面使用distinct可以消除重复的行；

3、条件查询

​	a.语法

​		select * from 表名 where  条件

​	b.比较运算符

​		等于（=）、大于、小于、大于等于（<=）、小于等于、不等于（！=）

​	c.逻辑运算符

​		and  or  not(非)

​	d、模糊查询

​		like: % 表示任意多个任意字符

​         __:表示一个任意字符

​	e、范围查询

​		in:查询一个非连续的范围内 select * from student where id in (1,6,9)*

​		between  and:连续的范围内

​	f、空判断

​			注意：null与""不同

​			判断空： is null

​			判断非空： is not  null

​	 	g、优先级：小括号、not 比较运算符、逻辑运算符

4、聚合

​	为了快速得到统计数据，提供了5个聚合函数

​	count(*):表示计算总行数，也可以用count(列名)

​	max(列)、min(列)、sub(列)、avg(列)：表示列的平均值

5、分组

​		按照字段分组，表示此字段相同的数据会被放到一个集合中。分组后，只能查询出相同的数据列，对于有差异的数据列无法显示在结果集中。可以对分组后的数据进行统计，做聚合运算。例如：

​	select 列1，列2，聚合....from 表名 group by 列1，列2，列3，....having  列1，...聚合....

​	where 与having的区别：where是对表from后面而指定的表进行筛选，属于对原始数据的筛选；having是对group by 的结果进行筛选。

6、排序

​		select * from 表名 order by 列1 asc|desc，列2 asc|desc,....。默认按照从小到到的顺序排序，asc降序，desc升序。

7、分页

​	select * from 表名 limit start,count

​	select * from student limit 0,3   :意思是从第几行开始，看多少行。

8、关联

​	select students.name,class.name from class inner join students on class.id=students.classid;

​	a.表A inner join 表B：表A与表B匹配的行会出现在结果集中；

​	b.表A left join 表B：表A与表B匹配的行会出现在结果集中，外加表A中独有的数据，未对应的数据使用null填充；

​	c.表A rightjoin 表B：表A与表B匹配的行会出现在结果集中，外加表B中独有的数据，未对应的数据使用null填充；



### python 连接数据库操作：

```python
import mysql.connector
'''
需要注意的是：1、在插入、更新、删除操作，在执行sql语句后，需要用cnn.commit()提交，
并且如果提交失败，需要回滚操作cnn.rollback()--用异常处理
2、查询后，接收的函数有：
    fetchone():获取下一个查询结果集，结果集是一个对象
    fetchall():接收全部的返回的行
    rowcount:是一个只读属性，返回execute()方法影响的行数
    
'''

try:
    cnn = mysql.connector.connect(host='localhost', user='root', password='123456', database='xzlmark')

except Exception:
    print('数据库连接错误：')
# 获得游标
cursor = cnn.cursor()
# cursor.execute('select version();')
# data = cursor.fetchone()
# print('获取的内容为：%s' % data)

cursor.execute('select * from student;')

data = cursor.fetchall()
for row in data:
    print('id={0}\t姓名={1}\t年龄={2}\t性别={3}\t地址={4}\t是否删除={5}'.format(row[0], row[1], row[2], row[3], row[4], row[5]))

cursor.close()
cnn.close()
```
