import requests


def get_site():
    url = 'http://10.35.166.188:9200'
    resp = requests.get(url)
    print(resp.json())


def add_index(index_name):
    ''' 添加索引，类似创建库'''
    url = 'http://10.35.166.188:9200/%s' % index_name  # put
    params = {
        "settings": {
            "number_of_shards": 5,   # 主分片
            "number_of_replicas": 1  # 备份分片
        }
    }

    resp = requests.request('PUT', url, json=params)
    print(resp.json())


def get_index(index_name):
    url = 'http://10.35.166.188:9200/%s' % index_name  # get
    resp = requests.request('GET', url)
    print(resp.json())


if __name__ == '__main__':
    # get_site()
    # add_index('foods_site')
    get_index('foods_site')