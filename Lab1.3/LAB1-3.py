from pysnmp.hlapi import *

snmpVarVersion = ObjectIdentity('SNMPv2-MIB', 'sysDescr', 0)
snmpVarVersionNext = ObjectIdentity('1.3.6.1.2.1.2.2.1.2')
result = getCmd(SnmpEngine(),
                CommunityData("public", mpModel=0),
                UdpTransportTarget(("10.31.70.107", 161)),
                ContextData(),
                ObjectType(snmpVarVersion))
for r in result:
    for s in r[3]:
        print(s)
# print(result)

resultNext = nextCmd(SnmpEngine(),
                CommunityData("public", mpModel=0),
                UdpTransportTarget(("10.31.70.107", 161)),
                ContextData(),
                ObjectType(snmpVarVersionNext),
                lexicographicMode=False)
print("--------------------------")
print(resultNext)
print("--------------------------")
for r in resultNext:
    for s in r[3]:
        print(s)


##  errorIndication, errorStatus, errorIndex, varBindTable = cmdgen.CommandGenerator().nextCmd(
##  cmdgen.CommunityData('test-agent', 'public'),
##  cmdgen.UdpTransportTarget(('10.31.70.107', 161)),
##  ('SNMPv2-MIB', 'sysDescr', 0))
