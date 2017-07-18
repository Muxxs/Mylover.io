#coding=utf-8
import os,shutil
#域名 user ftp密码 数据库名 数据库用户名 数据库密码 网站类型 API密码 方式
text="yuming.com,x.tecplaces.com x ftppassword dbname dbusername dbpassword apikey type webtype"
def changetext(text):
    text=text.split(" ")
    return text
def madewebsite(webtype):
    file = os.listdir("img/bad")
    for i in file:
        shutil.copyfile("img/bad/" + i, "img/good/" + i)
def connectweb(weburl):
    import urllib
    content = urllib.open(weburl).read()
    print content
def sendmessage(text):
    text=changetext(text)
    domain=text[0]
    name=text[1]
    ftppw=text[2]
    dbname=text[3]
    dbuser=text[4]
    dbpw=text[5]
    apikey=text[6]
    webtype=text[-1]
    type=text[-2]
    for i in range(0,6):
        print (text[i])
    import urllib2
    import urllib
    data = {}
    data['domain'] = domain.split(",")[0]
    data['domains'] =domain
    data['dbname'] = dbname
    data['dbuser']=dbuser
    data['db_flag']=1
    data['ftp_flag']=1
    data['ftpuser']=name
    data['ftppasswd']=ftppw
    data['cftppasswd']=ftppw
    data['dbpasswd']=dbpw
    data['cdbpasswd']=dbpw
    # 定义post的地址
    url = 'http://www.test.com/post/'
    post_data = urllib.urlencode(data)
    # 提交，发送数据
    req = urllib2.urlopen(url, post_data)
    # 获取提交后返回的信息
    content = req.read()
if text[-1]=="1":
    sendmessage(text)
connectweb("http://tecplaces.com/")