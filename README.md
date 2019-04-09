# Python 实验室

继熟练掌握NodeJS后，突然对Python特别感兴趣。

## 初始化【windows】

1. 安装的时候可以勾选把python写入环境路径
2. 如果没有勾选，也可以自己导入

```
C:\Users\{user_name}\AppData\Local\Programs\Python\Python37
C:\Users\{user_name}\AppData\Local\Programs\Python\Python37\Scripts
```

3. 优化下载第三方包的速度，新建文件：`C:\Users\{user_name}\pip\pip.ini`，并写入：

```
[global]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple/
```

4. 如果在IDE里执行不了python或pip下载的指令，使用超级管理员身份打开IDE
