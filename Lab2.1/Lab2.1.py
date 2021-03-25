import paramiko, time
import json, pprint, requests

r = requests.get('https://ya.ru/')
header = r.headers
code = r.status_code
# json = r.json()
hostIP = '10.31.70.209'
login = 'restapi'
password ='j0sg1280-7@'
HTTPSport = '55443'

BUF_SIZE = 20000
TIMEOUT = 1

# Создаем объект — соединение по ssh
ssh_connection = paramiko.SSHClient()
ssh_connection.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Инициируем соединение по ssh
ssh_connection.connect(hostIP, username=login, password=password, look_for_keys=False, allow_agent=False)
session = ssh_connection.invoke_shell()

session.send("\n")
session.recv(BUF_SIZE)
session.send("terminal length 0\n")
time.sleep(TIMEOUT)
session.send("\n")
session.recv(BUF_SIZE)
session.send("show run\n")
(session.send('show interface\n'))

packets = str(session.send('sho ip int brief'))
terminalLength = str(session.send('terminal length 0\n'))
time.sleep(TIMEOUT*2)
s = (session.recv('show interface\n'))

print('Show interface: ' + s)
print('Number of packets: ' + packets)
print('Terminal Length: ' + terminalLength)
# print('session.recv ' + s)
# Выход из SSH сессии
# session.close()