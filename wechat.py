# ! /usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import json
import itchat
import requests

# 登录和初始化
def main():
    itchat.auto_login(enableCmdQR=True)
    itchat.run()

def checkapi():
    try:
        inf = open('api.inf', 'r')
        api = inf.readline()
        inf.close()
    except:
        print('请前往 http://www.tuling123.com 申请机器人API，并填写在相同目录下的“api.inf”文件首行！')
        input()

# 图灵机器人回复部分
def talk(info, userid=None):
    url = 'http://www.tuling123.com/openapi/api'
    inf = open('api.inf', 'r')
    api = inf.readline()
    inf.close()
    param = json.dumps(
        {"key": api, "info": info, "userid": userid})
    callback = requests.post(url, data=param)
    result = eval(callback.text)
    code = result['code']
    if code == 100000:
        recontent = result['text']
    elif code == 200000:
        recontent = result['text'] + result['url']
    elif code == 302000:
        recontent = result['text'] + result['list'][0]['info'] + \
            result['list'][0]['detailurl']
    elif code == 308000:
        recontent = result['text'] + result['list'][0]['info'] + \
            result['list'][0]['detailurl']
    else:
        recontent = '这货还没学会怎么回复这句话'
    return recontent

# userid通过用户名的md5产生
def md5(str):
    import hashlib
    md = hashlib.md5()
    md.update(str)
    return md.hexdigest()

# 注册微信消息
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    reply = talk(msg['Text'],md5(msg['FromUserName']))
    User = itchat.search_friends(userName=msg['FromUserName'])
    if User['RemarkName'] == '':
        NickName = User['NickName']
    else:
        NickName = '%s(%s)' % (User['NickName'],User['RemarkName'])
    print('------------------------------------------------------------------------------')
    print('%s悄悄对您说：%s' % (NickName, msg['Text']))
    print('AI帮您回复%s：%s' % (NickName, reply))
    print('------------------------------------------------------------------------------')
    return reply

@itchat.msg_register(itchat.content.PICTURE)
def pic_reply(msg):
    msg['Text'](msg['FileName'])
    return talk(msg['Text'](msg['FileName']))

@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_reply(msg):
    if msg['isAt']:
        reply = talk(msg['Content'],md5(msg['ActualUserName']))
        print('------------------------------------------------------------------------------')
        print('%s在群聊中对您说：%s' % (msg['ActualNickName'], msg['Content']))
        print('AI帮您回复%s：%s' % (msg['ActualNickName'], reply))
        print('------------------------------------------------------------------------------')
        itchat.send(u'@%s\u2005 %s' % (msg['ActualNickName'], reply), msg['FromUserName'])
    else:
        print('------------------------------------------------------------------------------')
        print('%s在群聊中说：%s' % (msg['ActualNickName'], msg['Content']))
        print('------------------------------------------------------------------------------')

if __name__ == '__main__':
    checkapi()
    main()