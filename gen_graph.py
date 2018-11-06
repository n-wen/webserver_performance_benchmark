# encoding:'utf8'
"""
"""
import numpy as np
import matplotlib.pyplot as plt

data = {
    'clojure': {'ring': {
        'concurrency': 273652,
        'throughput': 9.29,
        'rps': 4293.75
    },
        'http-kit': {
            'concurrency': 395016,
            'throughput': 12.11,
            'rps': 5349.35
        }},
    'go': {'gin': {
        'concurrency': 268529,
        'throughput': 7,
        'rps': 3375.30
    },
        'echo': {
            'concurrency': 272800,
            'throughput': 7.22,
            'rps': 3491.51,
        }},
    'python3': {'sanic': {
        'concurrency': 499578,
        'throughput': 13.01,
        'rps': 6662.17
    },
        'flask_eventlet': {
            'concurrency': 189017,
            'throughput': 8.02,
            'rps': 3828.57,
        },
        'flask_gevent': {
            'concurrency': 232241,
            'throughput': 8.74,
            'rps': 4149.91
        }},
}

concurrency = []
throughput = []
rps = []
x = []

server_list = []


class ServerBench(object):
    name = None
    concurrency = None
    throughput = None
    rps = None

    def __init__(self, name, concurrency, throughput, rps):
        self.name = name
        self.concurrency = concurrency
        self.throughput = throughput
        self.rps = rps


for lang, server_data in data.items():
    for server_name, server_bench in server_data.items():
        server_list.append(ServerBench(
            name="{}_{}".format(lang, server_name),
            concurrency=server_bench.get("concurrency"),
            throughput=server_bench.get("throughput"),
            rps=server_bench.get("rps"),
        ))

server_list = sorted(server_list, key=lambda x: x.concurrency, reverse=True)
for i in server_list:
    concurrency.append(i.concurrency)
    throughput.append(i.throughput)
    rps.append(i.rps)
    x.append(i.name)

concurrency = np.array(concurrency)
throughput = np.array(throughput)
rps = np.array(rps)

concurrency = concurrency * 1. / np.max(concurrency, axis=0)
throughput = throughput * 1. / np.max(throughput, axis=0)
rps = rps * 1. / np.max(rps, axis=0)

ind = np.arange(len(concurrency))
width = 0.2

fig, ax = plt.subplots()
concurrency_rests = ax.bar(ind - width, concurrency, width, color='SkyBlue', label='concurrency')
throughput_rests = ax.bar(ind, throughput, width, label='throughput')
rps_rests = ax.bar(ind + width, rps, width, label='rps')

ax.set_ylabel("amount")
ax.set_title("benchmark for webservers")
ax.set_xticks(ind)
ax.set_xticklabels(x, rotation=15)
ax.legend()


def autolabel(rects, xpos='center'):
    """
    Attach a text label above each bar in *rects*, displaying its height.

    *xpos* indicates which side to place the text w.r.t. the center of
    the bar. It can be one of the following {'center', 'right', 'left'}.
    """

    xpos = xpos.lower()  # normalize the case of the parameter
    ha = {'center': 'center', 'right': 'left', 'left': 'right'}
    offset = {'center': 0.5, 'right': 0.57, 'left': 0.43}  # x_txt = x + w*off

    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width() * offset[xpos], 1.01 * height,
                '{}'.format(height), ha=ha[xpos], va='bottom')


# autolabel(concurrency_rests, "left")
# autolabel(throughput_rests, "center")
# autolabel(rps, "right")
# plt.show()
plt.subplots_adjust(bottom=0.2)
plt.savefig('./static/bench.png')
