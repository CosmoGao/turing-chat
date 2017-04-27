import itchat
IDandMESSAGE={}
IDandTUN={}
IDandFUN={}

itchat.auto_login(True)
mydata=[]
############     self     ##############
while mydata==[]:
    inputname=input('please input your wechat user name:')
    mydata=itchat.search_friends(name=inputname)
    print(mydata)
loca1=str(mydata).find('UserName')+12
loca2=str(mydata).find('NickName')-4
myusrname=str(mydata)[loca1:loca2]
print (myusrname)

#############----->Friend Chat<-----#############
@itchat.msg_register(['Text'])
def ch_regist(msg):
    print(msg['MsgId'])
    IDandMESSAGE[str(msg['MsgId'])]=msg['Text']
    IDandTUN[str(msg['MsgId'])]=msg['ToUserName']
    IDandFUN[str(msg['MsgId'])]=msg['FromUserName']
@itchat.msg_register(['Note'])
def ch_reply(msg):
    chcont=msg['Content']
    if chcont.find('<revokemsg><')>0:
        loc1=chcont.find('</oldmsgid><msgid>')+18
        loc2=chcont.find('</msgid><replacemsg><![CDATA')
        messageid=chcont[loc1:loc2]
        print(messageid)
        try:#friend chat only
            oritun=IDandTUN[str(messageid)]
            orifun=IDandFUN[str(messageid)]
            fname=itchat.search_friends(userName=orifun)
            ##print(fname)
            itchat.send("[Autoreply] The message revoked by '"+fname['NickName']+"' just now is :"+IDandMESSAGE[messageid],oritun)
            itchat.send("[Autoreply] The message revoked by '"+fname['NickName']+"' just now is :"+IDandMESSAGE[messageid],orifun)
        except:
            print("-----Can't find original msg")

#############----->Group Chat<-----#############
@itchat.msg_register(['Text'],isGroupChat=True)
def chgr_regist(msg):
    print(msg['MsgId'])
    #print(msg)
    IDandMESSAGE[str(msg['MsgId'])]=msg['Text']
    IDandTUN[str(msg['MsgId'])]=msg['ToUserName']
    IDandFUN[str(msg['MsgId'])]=msg['FromUserName']
    print(IDandMESSAGE)
@itchat.msg_register(['Note'],isGroupChat=True)
def chgr_reply(msg):
    #print(msg)
    chcont=msg['Content']
    if chcont.find('revokemsg')>0:
        loc1=max(chcont.find('/oldmsgid&gt;&lt;msgid&gt;')+26,chcont.find('</oldmsgid><msgid>')+18)
        loc2=max(chcont.find('&lt;/msgid&gt;&lt;replacemsg&gt;&lt;![CDATA'),chcont.find('</msgid><replacemsg><![CDATA'))
        messageid=chcont[loc1:loc2]
        print(messageid)
        chtext=msg['Text']
        print(chtext)
        chlen=len(chtext)
        aname=chtext[:chlen-7]
        try:
            oritun=IDandTUN[str(messageid)]
            orifun=IDandFUN[str(messageid)]
        except:
            print('dont chehui twice')
        if (oritun==myusrname or orifun==myusrname)and (chtext.find('You')>0 or chtext.find('你')>0) or chtext=="You've recalled a message.":
            aname='myself'
        else:
            aname=aname + '[not me]'
        try:
            itchat.send("[Autoreply] The message revoked by '"+aname+"' just now is :"+IDandMESSAGE[str(messageid)],oritun)
            itchat.send("[Autoreply] The message revoked by '"+aname+"' just now is :"+IDandMESSAGE[str(messageid)],orifun)
        except:
            print("-----Can't find original msg")

itchat.run(debug=False)
