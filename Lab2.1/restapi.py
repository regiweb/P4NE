import json, pprint, requests

hostIP = '10.31.70.210'
login = 'restapi'
password ='j0sg1280-7@'
HTTPSport = ':55443'

URL = 'https://' + hostIP + HTTPSport

r = requests.post(URL + '/api/v1/auth/token-services', auth=(login, password), verify=False)
token = r.json()["token-id"]

header = {"content-type": "application/json", "X-Auth-Token": token}
r = requests.get(URL + '/api/v1/interfaces/GigabitEthernet1/statistics', headers=header, verify=False)

"""
for interface in r:
    interface = 'interface'
    pprint.pprint(r.json(interface))
"""
pprint.pprint(r.json())
