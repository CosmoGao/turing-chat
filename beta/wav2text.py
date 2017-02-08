# ! /usr/bin/env python
# -*- coding:utf-8 -*-

import base64
import urllib2
import urllib
import json
import wave
from pydub import AudioSegment

def transcode(file):
    rec = AudioSegment.from_mp3(file)
    rec_wav = rec.export(file.replace('mp3','wav'), format = 'wav')
    rec_wav.close()

def get_token():
    URL = 'http://openapi.baidu.com/oauth/2.0/token'
    _params = urllib.urlencode({'grant_type': 'client_credentials',
                                'client_id': 'rqGfWFhPP9s9QQBXllQ7hpVM',#改成你自己的
                                'client_secret': '88cfa910869ae4c37bb804a0e431cd49'})#改成你自己的
    _res = urllib2.Request(URL, _params)
    _response = urllib2.urlopen(_res)
    _data = _response.read()
    _data = json.loads(_data)
    return _data['access_token']

def wav_to_text(wav_file):
    try:
        wav_file = open(wav_file, 'rb')
    except IOError:
        print u'文件错误啊，亲'
        return
    wav_file = wave.open(wav_file)
    n_frames = wav_file.getnframes()
    frame_rate = wav_file.getframerate()
    if n_frames == 1 or frame_rate not in (8000, 16000):
        print u'不符合格式'
        return
    audio = wav_file.readframes(n_frames)
    seconds = n_frames/frame_rate+1
    minute = seconds/60 + 1
    for i in range(0, minute):
        sub_audio = audio[i*60*frame_rate:(i+1)*60*frame_rate]
        base_data = base64.b64encode(sub_audio)
        data = {"format": "wav",
                "token": get_token(),
                "len": len(sub_audio),
                "rate": frame_rate,
                "speech": base_data,
                "cuid": "B8-AC-6F-2D-7A-94",
                "channel": 1}
        data = json.dumps(data)
        res = urllib2.Request('http://vop.baidu.com/server_api',
                              data,
                              {'content-type': 'application/json'})
        response = urllib2.urlopen(res)
        res_data = json.loads(response.read())
        print res_data['result'][0]

if __name__ == '__main__':
    wav_to_text('demo.wav')