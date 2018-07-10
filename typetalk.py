import requests
import yaml
with open('typetalk_config.yml', 'r') as yml:
    config = yaml.load(yml)
    typetalkToken = config['typetalk']['typetalkToken']
    topicId = config['typetalk']['topicId']

    r = requests.post('https://typetalk.com/api/v1/topics/' + topicId + '?typetalkToken=' + typetalkToken, {'message':'Hello, Typetalk! test2'})
    print(r.status_code)
    print(r.json())
