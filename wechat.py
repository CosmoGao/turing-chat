# ! /usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals

import json
import itchat
import requests
import platform
# 登录和初始化


def main():
    itchat.auto_login(enableCmdQR=True + (platform.system() == 'Linux'))
    itchat.run()


def checkapi():
    try:
        inf = open('api.inf', 'r')
        api = inf.readline().replace('\n','')
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
    md.update(str.encode('utf-8'))
    return md.hexdigest()

# 注册微信消息


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    reply = talk(msg['Text'], md5(msg['FromUserName']))
    User = itchat.search_friends(userName=msg['FromUserName'])
    if User['RemarkName'] == '':
        NickName = User['NickName']
    else:
        NickName = '%s(%s)' % (User['NickName'], User['RemarkName'])
    print('------------------------------------------------------------------------------')
    print('%s悄悄对您说：%s' % (NickName, msg['Text']))
    print('AI帮您回复%s：%s' % (NickName, reply))
    print('------------------------------------------------------------------------------')
    return reply


@itchat.msg_register(itchat.content.MAP)
def map_reply(msg):
    reply = talk(msg['Text'], md5(msg['FromUserName']))
    User = itchat.search_friends(userName=msg['FromUserName'])
    if User['RemarkName'] == '':
        NickName = User['NickName']
    else:
        NickName = '%s(%s)' % (User['NickName'], User['RemarkName'])
    print('------------------------------------------------------------------------------')
    print('%s向您分享了地点：%s' % (NickName, msg['Text']))
    print('AI帮您回复%s：%s' % (NickName, reply))
    print('------------------------------------------------------------------------------')
    return reply


@itchat.msg_register(itchat.content.CARD)
def card_reply(msg):
    reply = '谢谢你的推荐，我们会成为好朋友的！'
    User = itchat.search_friends(userName=msg['FromUserName'])
    if User['RemarkName'] == '':
        NickName = User['NickName']
    else:
        NickName = '%s(%s)' % (User['NickName'], User['RemarkName'])
    print('------------------------------------------------------------------------------')
    print('%s向您推荐了%s' % (NickName, msg['Text']['NickName']))
    print('AI帮您回复%s：%s' % (NickName, reply))
    print('------------------------------------------------------------------------------')
    return reply


@itchat.msg_register(itchat.content.NOTE)
def note_reply(msg):
    print(msg)


@itchat.msg_register(itchat.content.SHARING)
def sharing_reply(msg):
    reply = talk(msg['Text'], md5(msg['FromUserName']))
    User = itchat.search_friends(userName=msg['FromUserName'])
    if User['RemarkName'] == '':
        NickName = User['NickName']
    else:
        NickName = '%s(%s)' % (User['NickName'], User['RemarkName'])
    print('------------------------------------------------------------------------------')
    print('%s向您分享了链接：%s' % (NickName, msg['Text']))
    print('AI帮您回复%s：%s' % (NickName, reply))
    print('------------------------------------------------------------------------------')
    return reply


@itchat.msg_register(itchat.content.PICTURE)
def pic_reply(msg):
    msg['Text']('./images/' + msg['FileName'])
    User = itchat.search_friends(userName=msg['FromUserName'])
    if User['RemarkName'] == '':
        NickName = User['NickName']
    else:
        NickName = '%s(%s)' % (User['NickName'], User['RemarkName'])
    print('------------------------------------------------------------------------------')
    print('%s给您发送了一个表情/图片，已经存入images目录，文件名：%s' % (NickName, msg['FileName']))
    print('AI帮您回复%s默认表情default.gif' % NickName)
    print('------------------------------------------------------------------------------')
    return '@img@./images/default.gif'


@itchat.msg_register(itchat.content.RECORDING)
def rec_reply(msg):
    # 是否开启语音识别，需要安装ffmpeg和pydub
    enable_voice_rec = False
    msg['Text']('./records/' + msg['FileName'])
    User = itchat.search_friends(userName=msg['FromUserName'])
    if User['RemarkName'] == '':
        NickName = User['NickName']
    else:
        NickName = '%s(%s)' % (User['NickName'], User['RemarkName'])

    if enable_voice_rec:
        msg['Text']('./records/' + msg['FileName'])
        from beta import wav2text
        wav2text.transcode('./records/' + msg['FileName'])
        filename = msg['FileName'].replace('mp3','wav')
        text = wav2text.wav_to_text('./records/' + filename)        # 此处出现问题，返回值会出现一个None
        print text      
        reply = talk(text, md5(msg['FromUserName']))       
        print('------------------------------------------------------------------------------')
        print('%s给您发送了一条语音，已经存入records目录，文件名：%s' % (NickName, msg['FileName']))
        print('智能识别该消息内容为：%s' % text)
        print('AI帮您回复%s：%s' % (NickName, reply))
        print('------------------------------------------------------------------------------')
        return reply
    else:
        print('------------------------------------------------------------------------------')
        print('%s给您发送了一条语音，已经存入records目录，文件名：%s' % (NickName, msg['FileName']))
        print('AI帮您回复%s默认表情default.gif' % NickName)
        print('------------------------------------------------------------------------------')
        return '@img@./records/default.gif'


@itchat.msg_register(itchat.content.ATTACHMENT)
def att_reply(msg):
    msg['Text']('./attachments/' + msg['FileName'])
    User = itchat.search_friends(userName=msg['FromUserName'])
    if User['RemarkName'] == '':
        NickName = User['NickName']
    else:
        NickName = '%s(%s)' % (User['NickName'], User['RemarkName'])
    print('------------------------------------------------------------------------------')
    print('%s给您发送了一个文件，已经存入attachments目录，文件名：%s' % (NickName, msg['FileName']))
    print('AI帮您回复% s：这是什么东西？我收下了。' % NickName)
    print('------------------------------------------------------------------------------')
    return '这是什么东西？我收下了。'


@itchat.msg_register(itchat.content.VIDEO)
def video_reply(msg):
    msg['Text']('./videos/' + msg['FileName'])
    User = itchat.search_friends(userName=msg['FromUserName'])
    if User['RemarkName'] == '':
        NickName = User['NickName']
    else:
        NickName = '%s(%s)' % (User['NickName'], User['RemarkName'])
    print('------------------------------------------------------------------------------')
    print('%s给您发送了一个视频，已经存入videos目录，文件名：%s' % (NickName, msg['FileName']))
    print('AI帮您回复% s默认表情default.gif' % NickName)
    print('------------------------------------------------------------------------------')
    return '@img@./videos/default.gif'


@itchat.msg_register(itchat.content.FRIENDS)
def fri_reply(msg):
    itchat.add_friend(**msg['Text'])
    itchat.send_msg('你好，我的人类朋友！', msg['RecommendInfo']['UserName'])


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_reply(msg):
    if msg['isAt']:
        reply = talk(msg['Content'], md5(msg['ActualUserName']))
        print(
            '------------------------------------------------------------------------------')
        print('%s在群聊中对您说：%s' % (msg['ActualNickName'], msg['Content'].replace('\u2005',' ')))
        print('AI帮您回复%s：%s' % (msg['ActualNickName'], reply))
        print(
            '------------------------------------------------------------------------------')
        itchat.send('@%s %s' % (msg['ActualNickName'], reply), msg['FromUserName'])
    else:
        print(
            '------------------------------------------------------------------------------')
        print('%s在群聊中说：%s' % (msg['ActualNickName'], msg['Content']))
        print(
            '------------------------------------------------------------------------------')


@itchat.msg_register(itchat.content.PICTURE, isGroupChat=True)
def grouppic_reply(msg):
    msg['Text']('./images/group/' + msg['FileName'])
    print('------------------------------------------------------------------------------')
    print('%s在群聊中发了一个表情/图片，已经帮您存入images/group目录，文件名为：%s' % (msg['ActualNickName'], msg['FileName']))
    print('------------------------------------------------------------------------------')
    itchat.send('@img@./images/default.gif', msg['FromUserName'])

if __name__ == '__main__':
    checkapi()
    main()
