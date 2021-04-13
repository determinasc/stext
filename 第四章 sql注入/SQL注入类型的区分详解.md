## 1、 **首先按照常用接收方式的不同可以分为以下三种**

### GET

GET请求的参数是放在URL里，GET请求的URL传参有长度限制 中文需要URL编码

URL最长的长度 https://www.cnblogs.com/cuihongyu3503319/p/5892257.html

### POST

POST请求参数是放在请求body里，长度没有限制

### COOKIE

cookie参数放在请求头信息，提交的时候 服务器会从请求头获取参数。
request.php

```php
<?php
print_r($_GET);
print "<hr>";
print_r($_POST);
print "<hr>";
print_r($_COOKIE);
?>
```

## 2、 **注入数据类型的区分**

### int 整型 

```sql
select * from user where id=1
```

### sting 字符型 

```sql
select * from user where username='admin'
```

### like 搜索型

```sql
select * from news where title like '%标题%'
```

以上除了第一种以外,其余在判断注入或查询语句的时候都要进行闭合,不闭合 SQL语句不仅会出错,可能与原意不一样,会造成错误的判断。

### 字符型 注入闭合

```sql
select * from user where username='admin' and 'x'='x' 
```

' and 'x'='x 这个部分就是闭合的部分

### like 模糊型 注入闭合

```sql
select * from news where title like '%标题%' and '1%' = '1%' 
```

%' and '1%' = '1 这个是闭合的部分

```sql
select * from news where title like '%s%' and '1%' = '1%'
```

## 3、 **注入方法区分**

### 联合查询注入 union select联合两个表

### 报错注入 数据库报错信息 进行注入

### 盲注入 

- 布尔型注入

- 时间型注入