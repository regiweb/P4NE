import requests, json, pprint
from flask import render_template, jsonify, Flask

def newticket ():
    url = 'https://sandboxapic.cisco.com/api/v1/ticket'
    body = {"username": "devnetuser", "password": "Cisco123!"}
    header = {"content-type": "application/json"}
    r = requests.post(url, data=json.dumps(body), headers = header, verify = False)
    t = r.json()['response']['serviceTicket']
    return t


def get_topology(token):
    if token:
        topologyURL = 'https://sandboxapicem.cisco.com/api/v1/topology/physical-topology'
        topologyHeader = {"content-type": "application/json", 'X-Auth-Token': token}

        r = requests.get(topologyURL, headers=topologyHeader)
        return (r.json()['response'])
    else:
        return('No token exists')

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('topology.html')

@app.route('/api/topology')
def topology():
    return (jsonify(topology))

if __name__ == '__main__':
    t1 = get_topology(newticket())
    app.run(debug=True)

