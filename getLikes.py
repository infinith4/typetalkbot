# https://typetalk.com/api/v2/likes/discover
import requests
import yaml
with open('typetalk_config.yml', 'r') as yml:
    config = yaml.load(yml)
    typetalkToken = config['typetalk']['typetalkToken']
    topicId = config['typetalk']['topicId']

    r = requests.get('https://typetalk.com/api/v2/likes/discover?spaceKey=69dNc2L20A&typetalkToken=' + typetalkToken)
    print(r.status_code)
    print(r.text)
