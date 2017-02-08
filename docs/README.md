# turing-chat 

![python](https://img.shields.io/badge/python-2.7-red.svg) ![python3.5](https://img.shields.io/badge/python-3.5-blue.svg) [![AllahBless](https://cdn.rawgit.com/LunaGao/BlessYourCodeTag/master/tags/ramen.svg)](https://github.com/LunaGao/BlessYourCodeTag) [![apm](https://img.shields.io/apm/l/vim-mode.svg)](/LICENSE)     **[中文版](/README.md)**

**turing-chat** is an open source WeChat robot based on  [littlecodersh](https://github.com/littlecodersh)'s [ItChat](https://github.com/littlecodersh/ItChat) project, and access to the [tuling123](http://www.tuling123.com/) service to provide natural language response (which only support Chinese).

## Quick Start
1. Download/Clone all the files

```bash
git clone git@github.com:CosmoGao/turing-chat.git
```

1. Install Python and dependent packages:

    - requests

        ```shell
        pip install requests
        ```
    
    - ItChat

        ```bash
        pip install itchat
        ```

1. Register the Tuling123 API and create the "api.inf" file at the same path, the writing the API at the first line

1. execute wechat.py


## Responsed Message Type
### Private Message
| Message Type | Responsed | Way | Output | 
| --- | --- | --- | --- | 
| Text(emoji) | √ | tuling123 response | message details | 
| Map | o | tuling123 response | message details | 
| Card | √ | static text | message details | 
| Note | × | - | - | 
| Sharing | √ | tuling123 response | message details | 
| Picture | √ | download & send img | storage path | 
| Recoring | √ | download & send img | storage path | 
| Attachments | √ | download & static text | storage path | 
| Video | o | download & send img | storage path | 
| Friend | √ | add friend & welcome message | - | 

### Group chat
| Message Type | @me | Responsed | Way | Output | 
| --- | --- | --- | --- | --- | 
| Text(emoji) | yes | √ | tuling123 response | message details | 
| Text(emoji) | no | × | - | message details | 
| Picture | - | √ | send img | storage path | 
| Others | - | × | - | - | 


## TODO
 - Enhance compatibility
 - Improve and add new message types

## Experimental Feature
Try to recongnize friends' recording messages with Baidu's REST API. To enable the feature, [ffmpeg](http://ffmpeg.org/) and [pydub](https://github.com/jiaaro/pydub) package is required, and you have to set the value of enable_voice_rec to True in wechat.py file.

## Issues and Suggestions
Any issues and suggestions may be discussed.

## License
[MIT](/LICENSE)
