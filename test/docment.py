import requests


def add_docment(index_name, doc_name, id_=None, **data):
    url = 'http://10.35.166.188:9200/%s/%s/' %(index_name, doc_name)  # post
    if id_:
        url += '%s/' % id_

    print(data)
    resp = requests.post(url, json=data)
    print(resp.json())

def get_docment(index_name, doc_name, id_=None):
    url = 'http://10.35.166.188:9200/%s/%s/' % (index_name, doc_name)  # post
    if id_:
        url += '%s/' % id_

    resp = requests.get(url)
    print(resp.json())

if __name__ == '__main__':
    data = {
        'name': '油条',
        'price': 1.5,
        'date': '2019.3.20'
    }
    get_docment('foods_site', 'foods',1)