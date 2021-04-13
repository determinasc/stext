# nmap的审计脚本

脚本更新

```
nmap --script-updatedb
```

XSS检测

```
Nmap -sV --script=http-unsafe-output-escaping target_ip
```

snmp默认团体名/弱口令漏洞及安全加固

```
nmap –sU –p161 –script=snmp-brute target_ip
```

iis短文件名泄露

```
nmap -p 80 --script http-iis-short-name-brute target_ip
```

Memcached未授权访问漏洞

```
nmap -sV -p 11211 -script memcached-info target_ip
```

验证https.sys远程代码执行漏洞

```
nmap -sV - (-) script http-vuln-cve2015-1635 target_ip
```

心脏出血

```
nmap -sV --scipt=ssl-heartbleed target_ip
```

mongodb未授权访问

```
nmap -p 27017 --script mongodb-info target_ip
```

redis未授权访问

```
nmap -p 6370 --script redis-info target_ip
```

elastticsearch未授权访问

```
nmap --script=http-vuln-cve2015-1427 --script-args command='ls' target_ip
```

rsync未授权漏洞

```
nmap -p 873 --script rsync=brute ==script=args 'rsync-brute.module=www'
```

http拒绝服务

```
nmap --max-paralleism 800-script http=slowloris siteaddress
```

ftp弱口令暴力破解

```
nmap --script ftp-brute --script-args brute.emptypass=true,ftp-brute.timeout=30,userdb=/root/dirtionary/usernames.txt,brute.useraspass=true,passdb=/root/dirtionary/passwords.txt,brute.threads=3,brute.delay=6 target_ip
```

检测CVE-2011-2523中的ftp-vsftpd-backdoor

```
nmap -T2 --script ftp-vsftpd-backdoor target_ip
```

验证http中开启的-methods 方法

```
nmap -T3 --script http-methods --script-args http.test-all=true,http.url-path=/siteaddress
```

验证HTTP.sys 远程代码执行

```
nmap -sV --script http-vuln-cve2015-1635 target_ip
```

验证 SSL POODLE information leak

```
nmap -sV -p 443 --version-light --script ssl-poodle target_ip
```

验证http 中开启了put 方法

```
nmap --script http-put --script-args http-put.url=/uploads/testput.txt,http-put.file=/root/put.txt target_ip
```

验证mysql 匿名访问

```
nmap --script mysql-empty-password target_ip
```

验证cve2015-1427 漏洞

```
nmap --script http-vuln-cve2015-1427 --script-args command=ls target_ip
```

验证cve2014-8877漏洞

```
nmap -Pn --script http-vuln-cve2014-8877 --script-args http-vuln-cve2014-8877.cmd=dir,http-vuln-cve2014-8877.uri=/wordpress target_ip
```

验证Cisco ASA中的CVE-2014-2126,CVE-2014-2127,CVE-2014-21,CVE-2014-2129漏洞

```
nmap -p 443 --script http-vuln-cve2014-2126,http-vuln-cve2014-2127,http-vuln-cve2014-2128,http-vuln-cve2014-2129 target_ip
```

验证低安全的 SSHv1，sslv2协议

```
nmap --script sshv1,sslv2 siteadress
```

验证CVE-2014-0224 ssl-ccs-injection

```
nmap -Pn --script ssl-ccs-injection target_ip
```

验证ssl-cert证书问题

```
nmap -v -v --script ssl-cert target_ip
```

验证SSL证书的有限期

```
nmap -Pn --script ssl-date siteadress
```

验证 Debian OpenSSL keys

```
nmap -p 443 --script ssl-known-key target_ip
```

验证弱加密SSL套件

```
nmap --script ssl-enum-ciphers target_ip
```

验证CVE 2015-4000

```
nmap --script ssl-dh-params siteadress
```

验证多种SSL漏洞问题

```
nmap 203.195.139.153 --vv --script sshv1,ssl-ccs-injection,ssl-cert,ssl-date,ssl-dh-params,ssl-enum-ciphers,ssl-google-cert-catalog,ssl-heartbleed,ssl-known-key,sslv2
```

在网络中检测某主机是否存在窃听他人流量

```
nmap --script sniffer-detect target_ip
```

暴力破解telnet

```
nmap -p 23 --script telnet-brute --script-args userdb=myusers.lst,passdb=mypwds.lst --script-args telnet-brute.timeout=8s target_ip
```

验证telnet是否支持加密

```
nmap --script telnet-encryption target_ip
```

精准地确认端口上运行的服务

```
nmap -sV --script unusual-port target_ip
```

收集VNC信息

```
nmap --script vnc-info target_ip
```

暴力破解VNC

```
nmap --script vnc-brute --script-args brute.guesses=6,brute.emptypass=true,userdb=/root/dictionary/user.txt,brute.useraspass=true,passdb=/root/dictionary/pass.txt,brute.retries=3,brute.threads=2,brute.delay=3 target_ip
```