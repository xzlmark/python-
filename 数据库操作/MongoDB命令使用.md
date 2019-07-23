# 一、操作MongoDB数据库

1、创建数据库。语法：use 数据库名 

​		注意：如果数据库不存在，则创建数据库，否则，切换到指定的数据库.如果刚才创建的数据库没有在列表中，如果要显示它，需要向刚刚创建的数据库中插入一些数据。**(db.student.insert({name:'tom',age:18,gender:1,address:'北京',isDelete:0}))**

2、查看所有数据库。show dbs

3、查看当前正在使用的数据库。db 或 db.getName()

4、断开连接。exit

5、查看命令api。help

6.删除数据库。db.dropDatabase()

# 二、集合操作

1、查看当前数据库下有哪些集合。	show collections

2、创建集合。	db.createCollection('集合名')  或  	db.集合名.insert(document)

3、删除集合。db.集合名.drop()

# 三、文档操作

1、插入文档

​		a、使用insert()方法插入文档：db.集合名.insert(文档) 

​				插入一行：(db.student.insert({name:'jack',age:20,gender:1,address:'上海',isDelete:0}))

​				插入多行：(db.student.insert([{name:'xzl',age:30,gender:1,address:'深圳',isDelete:0},{name:'xzl',age:30,gender:1,address:'深圳',isDelete:0}]))   注意：多个要加列表

​		b、使用save（）方法插入文档。db.集合名.save(文档)

2、文档更新

​		a、update（）用于更新已存在的文档

```python
db.collection.update(
   <query>,
   <update>,
   {
     upsert: <boolean>,
     multi: <boolean>,
     writeConcern: <document>
   }
)
```

query:update的查询条件，类似于sql里update后面的where后面的内容

update：update的对象和一些更新的操作符（$set，$inc）等。$set直接更新$inc在原有基础上累加后更新。

upsert：可选，如果不存在update的记录，是否当新数据插入，true为插入，false为不插入，默认为false。

multi：可选，默认是false，只更新找到的第一条记录，true则会所有更新

writeConcern：可选，抛出异常的级别，一般不用。示例如下：

```
db.books.update(
   { _id: 1 },----条件
   {
     $inc: { stock: 5 },  ---更新操作
     $set: {
       item: "ABC123",
       "info.publisher": "2222",
       tags: [ "software" ],
       "ratings.1": { by: "xyz", rating: 3 }
     }
   }
)
```

b、save（）方法通过传入的文档替换已有文档

```
db.collection.save(
   <document>,
   {
     writeConcern: <document>
   }
)
```

例如：db.products.save( { item: "book", qty: 40 } )

3、文档删除

```
db.collection.remove(
   <query>,
   {
     justOne: <boolean>,
     writeConcern: <document>,
     collation: <document>
   }
)
```

如果想要删除一个集合中的所有文档记录，使用 `remove` 方法并传入一个空文档（ `{}` ）作为参数 。下面的操作会删除 [*bios collection*](http://www.mongoing.com/docs/reference/bios-example-collection.html) 集合中的所有文档记录：

```
db.bios.remove( { } )
```

如果想要删除一个集合中的所有文档记录，使用 [`drop()`](http://www.mongoing.com/docs/reference/method/db.collection.drop.html#db.collection.drop) 方法效率更加高，它会把整个集合和索引全都删掉，然后再重建集合和索引就行了。

### 删除匹配条件的所有文档记录

想要删除满足指定条件的文档记录，使用 `remove()` 方法并传入 `<query>` 参数：

下面的操作会删除所有 `qty` 大于 `20` 的文档记录：

```
db.products.remove( { qty: { $gt: 20 } } )
```

4、文档查询

​	a、db.collection.find(query, projection).参数为可选，如果返回所有数据，则不需要参数。

​			若需要返回指定的列，则需要配置projection。例如：

查询满足条件的记录：db.products.find( { qty: { $gt: 25 } } )；

查询指定的列：db.products.find( { qty: { $gt: 25 } }, { item: 1, qty: 1 } )

​	b、还可以在find()方法后加pretty()格式化方法显示：

​		db.products.find( { qty: { $gt: 25 } }, { item: 1, qty: 1 } ).pretty（）

​	c、`db.collection.``findOne`(*query***,** *projection*)。查询匹配的第一条数据：

```
db.bios.findOne(
    { },
    { name: 1, contribs: 1 }
)
```

5、查询条件操作符。用于比较两个表达式并从MongoDB集合总获取数据

| $eq 或： | Matches values that are equal to a specified value.          |
| -------- | ------------------------------------------------------------ |
| $gt      | 大于                                                         |
| $gte     | 大于等于                                                     |
| $lt      | 小于                                                         |
| $lte     | 小于等于                                                     |
| $ne      | Matches all values that are not equal to a specified value. 不等于 |
| $in      | Matches any of the values specified in an array.{ field: { $in: [<value1>, <value2>, ... <valueN> ] } } |
| $nin     | Matches none of the values specified in an array.            |

使用_id进行查询：db.student.find({"_id":ObjectId("id值")})。

查询所有条数：db.student.find().count()

查询某个字段的值当中是否包含另一个值：db.student.find({name:/xzl/})

查询某个字段的值是否以另一个值开头:db.student.find({name:/^xzl/})

6、条件查询  and 和 or

| [`$or`](http://www.mongoing.com/docs/reference/operator/query/or.html#op._S_or) | Joins query clauses with a logical `OR` returns all documents that match the conditions of either clause. |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| [`$and`](http://www.mongoing.com/docs/reference/operator/query/and.html#op._S_and) | Joins query clauses with a logical `AND` returns all documents that match the conditions of both clauses. |
| [`$not`](http://www.mongoing.com/docs/reference/operator/query/not.html#op._S_not) | Inverts the effect of a query expression and returns documents that do *not* match the query expression. |
| [`$nor`](http://www.mongoing.com/docs/reference/operator/query/nor.html#op._S_nor) | Joins query clauses with a logical `NOR` returns all documents that fail to match both clauses. |

```
{ $or: [ { <expression1> }, { <expression2> }, ... , { <expressionN> } ] }
```

```
db.inventory.find( { price: { $not: { $gt: 1.99 } } } )
```

7、limit和skip。limit（）读取指定数的记录。skip（）跳过指定数的记录。db.student.find().limit(3).

​	limit和skip。limit（）一起使用实现分页功能。

​		db.student.find().skip(3).limit(3)

8、排序。db.集合名.find().sort({<key>:1|-1}).1表示升序，-1表示降序

