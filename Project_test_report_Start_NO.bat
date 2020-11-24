@echo off 

if "%1" == "h" goto label 
mshta vbscript:createobject("wscript.shell").run("""%~nx0"" h",0)(window.close)&&exit 
:label 

python manage.py runserver 192.168.1.55:9002