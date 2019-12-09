
import os
import logging
import pymysql

# 项目配置
basedir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 邮件配置
sender = 'jingshuai@kaiyuan.net'  # 发送方1
receiver = 'jingshuai@kaiyuan.net'
emailusername = 'jingshuai@kaiyuan.net'  # 登陆邮箱的用户名
emailpassword = 'Js1234...'  # 登陆邮箱的授权码
server = 'mail.kaiyuan.net'  # smtp服务器2017/6/22
# receiver2='wangle@kaiyuan.net,jingshuai@kaiyuan.net,zhanghao@kaiyuan.net,liucaiyu@kaiyuan.net'