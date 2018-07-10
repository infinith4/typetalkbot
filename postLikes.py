# https://typetalk.com/api/v2/likes/discover
import requests
import yaml
with open('typetalk_config.yml', 'r') as yml:
    config = yaml.load(yml)
    typetalkToken = config['typetalk']['typetalkToken']
    topicId = config['typetalk']['topicId']
    payload = {'typetalkToken': typetalkToken}
    postId = '18608871'
    r = requests.post('https://typetalk.com/api/v1/topics/' + topicId + '/posts/' + postId + '/like', params = payload)
    print(r.status_code)
    print(r.json())
