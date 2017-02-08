# turing-chat 

![python](https://img.shields.io/badge/python-2.7-red.svg) ![python3.5](https://img.shields.io/badge/python-3.5-blue.svg) [![AllahBless](https://cdn.rawgit.com/LunaGao/BlessYourCodeTag/master/tags/ramen.svg)](https://github.com/LunaGao/BlessYourCodeTag) [![apm](https://img.shields.io/apm/l/vim-mode.svg)](/LICENSE)     **[English](/docs/README.md)**

turing-chat是一个开源的微信聊天机器人，基于 [littlecodersh](https://github.com/littlecodersh) 的 [ItChat](https://github.com/littlecodersh/ItChat) 项目， 接入[图灵机器人](http://www.tuling123.com/)提供自然语言回复。

## 快速开始
1. 下载/克隆所有文件

```bash
git clone git@github.com:CosmoGao/turing-chat.git
```

1. 安装Python及依赖包

    - requests

        ```bash
        pip install requests
        ```
    
    - ItChat

        ```bash
        pip install itchat
        ```
1. 注册图灵机器人API，并在同级目录建立“api.inf”文件，将API写入首行

1. 执行wechat.py


## 响应消息类型
### 私聊
| 消息类型 | 是否响应 | 响应方式 | 输出 | 
| --- | --- | --- | --- | 
| 文本(emoji) | √ | 图灵机器人回复 | 消息内容 | 
| 地图 | o | 图灵机器人回复 | 消息内容 | 
| 名片 | √ | 固定文本 | 消息内容 | 
| 通知 | × | - | - | 
| 分享链接 | √ | 图灵机器人回复 | 消息内容 | 
| 图片 | √ | 下载 & 回复表情 | 存储位置 | 
| 语音 | √ | 下载 & 回复表情 | 存储位置 | 
| 文件 | √ | 下载 & 固定文本 | 存储位置 | 
| 视频 | o | 下载 & 回复表情 | 存储位置 | 
| 添加好友 | √ | 加为好友 & 欢迎信息 | - | 

### 群聊
| 消息类型 | @我 | 是否响应 | 响应方式 | 输出 | 
| --- | --- | --- | --- | --- | 
| 文本(emoji) | 是 | √ | 图灵机器人回复 | 消息内容 | 
| 文本(emoji) | 否 | × | - | 消息内容 | 
| 图片 | - | √ | 回复表情 | 存储位置 | 
| 其他 | - | × | - | - | 


## TODO
 - 兼容性提升
 - 完善、增加新消息类型

## 实验性功能
尝试利用百度的语音识别API对好友语音进行识别并回复，需要安装 [ffmpeg](http://ffmpeg.org/) 和 [pydub](https://github.com/jiaaro/pydub) 包，并在 wechat.py 中将 `enable_voice_rec` 置为`True`。


## 问题建议
任何问题和建议均可提出 Issue 讨论。

## 协议
[MIT](./LICENSE)
