from flask import *
from test.testcase import testgo
""""
学习Flask
https://www.jianshu.com/p/0f528c47c5bf
https://blog.csdn.net/weixin_30553065/article/details/96045980
"""
#1.创建Flask实例
app = Flask(__name__)
#2.构建实例对象从URL到python函数的映射关系，路由
@app.route('/')
def index():
    return 'Hello index Page'
#业务逻辑和表现逻辑分离，先路由到模板内名为index,html后单独写index.html页面,Flask 会在 templates 文件夹里寻找模板,注意templates文件夹位置
@app.route('/login/<name>')
def ttPage(name):
    return render_template('index.html',name=name,title='主页')
#动态路由中，变量路径名称与python函数传参必须一致
@app.route('/go/<name>')
def goTest(name):
    return 'GoTest page'+name
#浏览器会默认以/结尾，故而路由中的path要以/结尾
@app.route('/go/projects/')
def projects():
    return 'The project page'
#定义统一路径不同的请求方法访问
@app.route('/go/posturl/',methods=['GET','POST'])
def posturl():
    if request.method=='POST':
        return 'PostMethod to page'
    else:
        return 'GetMethod to page'
# @app.error_handlers(404)
# def page_not_found(e):
#     return render_template('404.html'),404
@app.route('/test/img/')
def test():
    return testgo.imgCheck()
#3.启动服务器,程序实例用run方法来启动服务器，例如
if __name__ =='__main__':
    app.run(debug=True,port=8777)