import ipaddress
import random
class Subnet:
    def __init__(self, n="0.0.0.0", p="/0"):
        self.network = n
        self.prefix = p
    def __str__(self):
        return self.network + self.prefix
    def getnet(self):
        return self.network

class AddrPlanEntry(Subnet):
    def __init__(self, n="0.0.0.0", p="/0", gw="0.0.0.0"):
        Subnet.__init__(self, n, p)
        self.gateway = gw
    def getgw(self):
        return self.gateway

class IPv4RandomNetwork:
    def __init__(self, n, p):
        Subnet.__init__(self, n, p)
        n = random.randint(0x0b000000, 0xdf000000)
        p = random.randint(8, 24)
        self.network = n
        self.prefix = p
    #def regular (self, r):
    #    if r = i:
    #        ipaddress.IPv4Network.is_private
    def  getRandomIP(self):
        return self.network + self.prefix

RandomIP = IPv4RandomNetwork.getRandomIP

for i in range(50): print(RandomIP(self=))







