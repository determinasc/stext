## 1、session机制

是一种服务器端的机制，服务器使用一种类似于散列表的结构（也可能就是使用散列表）来保存信息。 

当程序需要为某个客户端的请求创建一个session的时候，服务器首先检查这个客户端的请求里是否已包含了一个session标识 - 称为session id，如果已包含一个session id则说明以前已经为此客户端创建过session，服务器就按照session id把这个session检索出来使用（如果检索不到，可能会新建一个），如果客户端请求不包含session id，则为此客户端创建一个session并且生成一个与此session相关联的session id，session id的值应该是一个既不会重复，又不容易被找到规律以仿造的字符串，这个session id将被在本次响应中返回给客户端保存。 保存这个session id的方式可以采用cookie，这样在交互过程中浏览器可以自动的按照规则把这个标识发挥给服务器。

## 2、session用途

一般用于登录验证。

## 3、session的周期

- 默认关闭浏览器，session就会消失。
-  在程序中设置session的过期时间

session是存在于服务器里，cookie是存在客户端。在浏览器生成一个cookie session_id时，也会在服务器里生产一个session id文件，假如在做身份证认证的时候就会在这个服务器里的文件写入要验证的内容。

在php里 session的存放位置是 在php.ini里设置的，也可以通过函数设置在其他位置

## 4、出现漏洞的情景

如果服务器的session-id 存在网站的其他目录，通过扫描目录获取 session 文件。
如果存放在数据库，可以通注入漏洞获取seesion信息
获取到session_id 就可以修改cookie 进行提交 验证就可以通过

```php+HTML
<?php
$path_parts = pathinfo(__FILE__);
$save_seesion=$path_parts['dirname'].'\tmp';
session_save_path($save_seesion);
session_start();

$username='moon';
$password='moon123';

if($_GET['c']=='login'){
	if($_SESSION['username']==$username){
		echo "欢迎回来!{$_SESSION['username']}";
		
	}else{
		if($_POST['username']==$username && $_POST['password']==$password){
			$_SESSION['username']=$username;
			isset($PHPSESSID)?session_id($PHPSESSID):$PHPSESSID = session_id();
			setcookie('PHPSESSID', $PHPSESSID, time()+24 * 3600);
			echo "登录成功 {$_SESSION['username']}";
		}else{
			echo "帐号或者密码出错<a href='session.php'>返回</a>";
		}
	}	
}else{
	echo '<meta charset="UTF-8">';
	echo"<form method='post' action='?c=login'>";
	echo"<label>帐号：</label><input type='text' name='username'><br>";
	echo"<label>密码：</label><input type='password' name='password'><br>";
	echo"<input type='submit' value='登录' name='submit'>";
	echo "</form>";
}
?>
```

默认帐号和密码 moon moon123

```php
setcookie('PHPSESSID', $PHPSESSID, time()+24 * 3600);
```

设置当前的SESSION的过期时间。

当用户访问当前的页面的时候就会在tmp目录下生成session_id 登录后的用户就会session_id 用户名。

验证绕过。检索所有当前的session_id 进行验证。 如果存在用户即可绕过。

```http
http://www.webtester.com/session.php
```

用burpsuite替换cookie PHPSESSID的值 就可以绕过。