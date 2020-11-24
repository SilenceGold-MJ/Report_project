import time,os, shutil
from framework.logger import Logger
logger = Logger(logger="clean_html").getlog()
path_html=os.getcwd() + "\static\html"
shutil.rmtree(path_html)
os.makedirs(path_html)

while True:

    now=time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())
    if now.split("_")[-1] in '23-59-59':#23-59-59

        logger.info('%s时间到，执行清除无用的html……'%now.split("_")[-1] )


