from linepy import *
import requests, json
host = 'https://gwk.line.naver.jp'
LA = "BIZIOS\t1.7.5\tiOS\t10.2"
udidHash = ""
header = {
    'Accept':"application/json",
    "x-lal":"ja-JP_JP",
    "X-LHM":'GET',
    "X-LPV":'1',
    'X-Line-Application':LA
}
line = LINE()
ch = line.channel.approveChannelAndIssueChannelToken('1526709289')

header.update({'X-LHM':'POST'})
endpoint = '/plc/api/core/auth/cmsToken'
payload = {"channelAccessToken":ch.channelAccessToken,"udidHash":udidHash}
res = requests.post(host+endpoint, data=json.dumps(payload), headers=header)
print(res.json()['accessToken'])
