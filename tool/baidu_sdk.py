import requests
import json
import random
import numpy as np
import networkx as nx


def get_distance(url):
    # GET请求
    request = requests.get(url)
    result_byte = request.content
    result_str = str(result_byte, 'utf-8')
    result_js = json.loads(result_str)
    # print(result_js)
    print(result_js['result']['routes'][0]['distance'])
    return (result_js['result']['routes'][0]['distance'])

def load_G(fname):
    G = nx.Graph()
    d = json.load(open(fname))
    G.add_edges_from(d['edges'])
    return G

def save_G(G, fname):
    json.dump(dict(edges=[[u, v, G[u][v]] for u,v in G.edges()]),
       open(fname, 'w'), indent=2)

if __name__ == '__main__':
    # origin_lng = '%.5f' % (np.random.uniform(0.4, 0.8) + 29)  # 维度
    # origin_lat = '%.5f' % (np.random.uniform(0.4, 0.7) + 106)  # 经度
    # destination_lng = '%.5f' % (np.random.uniform(0.4, 0.8) + 29)
    # destination_lat = '%.5f' % (np.random.uniform(0.4, 0.7) + 106)

    dic = {0: [106.76904, 29.64979], 1: [106.74709, 29.65384], 2: [106.75477, 29.65503],
           3: [106.74136, 29.65038], 4: [106.74530, 29.64773], 5: [106.7484, 29.64580],
           6: [106.75312, 29.64412], 7: [106.77505, 29.63919], 8: [106.78444, 29.64583],
           9: [106.78762, 29.63693], 10: [106.78762, 29.63693]}

    keys = list(dic.keys())

    ak = '558KBa8tnUmPWo2GprmPVEOop82ynYWI'

    # 创建路线无向图
    G = nx.Graph()
    G.add_nodes_from(keys)
    for i in range(keys.__len__()):
        for j in range(keys.__len__()):
            if i == j or G.has_edge(i, j):
                continue
            origin_lng = '%.5f' % dic[i][1]
            origin_lat = '%.5f' % dic[i][0]
            destination_lng = '%.5f' % dic[j][1]
            destination_lat = '%.5f' % dic[j][0]
            url = 'https://api.map.baidu.com/directionlite/v1/driving?origin=' + origin_lng + ',' + origin_lat + '&destination=' + destination_lng + ',' + destination_lat + '&ak=' + ak
            len = get_distance(url)
            G.add_edge(i, j, length=len)

    print(G.edges.data())
    save_G(G, 'graph')
    # g = load_G('graph')
    # print(g.edges.data())

    # origin_key = random.choice(keys)
    # destination_key = random.choice(keys)

    # origin_lng = '%.5f' % dic[origin_key][1]  # 维度
    # origin_lat = '%.5f' % dic[origin_key][0]  # 经度
    # destination_lng = '%.5f' % dic[destination_key][1]
    # destination_lat = '%.5f' % dic[destination_key][0]

    # ak = '558KBa8tnUmPWo2GprmPVEOop82ynYWI'
    # url = 'https://api.map.baidu.com/directionlite/v1/driving?origin=' + origin_lng + ',' + origin_lat + '&destination=' + destination_lng + ',' + destination_lat + '&ak=' + ak
    # get_distance(url)
