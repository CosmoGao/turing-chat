# turing-chat
![py27][py27]
turing-chat是一个开源的微信聊天机器人，基于[littlecodersh](https://github.com/littlecodersh)的[ItChat](https://github.com/littlecodersh/ItChat)项目， 接入[图灵机器人](http://www.tuling123.com/)提供自然语言回复。

## 使用方法
1. 下载项目中的wechat.py文件

1. 安装Python及依赖包

    - requests

        ```shell
        pip install requests
        ```
    
    - ItChat

        ```bash
        pip install ItChat
        ```
1. 注册图灵机器人API，并在同级目录建立“api.inf”文件，将API写入首行

1. 执行wechat.py

## 功能
- [x] 响应好友、群聊中的文本消息，并进行自动回复
- [x] 自动下载图片、表情消息
- [x] 在服务端显示消息记录
- [ ] 响应更多消息
- [ ] 完善兼容性