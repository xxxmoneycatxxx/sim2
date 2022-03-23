#参考
##Flask
https://dormousehole.readthedocs.io/en/latest/
##

#*其他事项
##更新包管理
```
pip freeze > requirements.txt
```
##环境变量设置
作为一个捷径，如果文件名为 app.py 或者 wsgi.py ，那么您不 需要设置 FLASK_APP 环境变量。

命令行接口说明 https://dormousehole.readthedocs.io/en/latest/cli.html
### BASH
```
$ export FLASK_APP=myapp
$ flask run
```
###CMD
```
> set FLASK_APP=myapp
> flask run
```
###PowerShell
```
> $env:FLASK_APP = "myapp"
> flask run
```