from pysnmp.hlapi import *

for (errorIndication,
     errorStatus,
     errorIndex,
     varBinds) in nextCmd(SnmpEngine(),
                          CommunityData('public', mpModel=0),
                          UdpTransportTarget(('192.168.0.100', 161)),
                          ContextData(),
                          ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysContact')),
                          ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysObjectID')),
                          ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysUpTime')),
                          ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysContact')),
                          ObjectType(ObjectIdentity('SNMPv2-MIB', 'sysName')),
                          lexicographicMode=False):

    if errorIndication:
        print(errorIndication)
        break
    elif errorStatus:
        print('%s at %s' % (errorStatus.prettyPrint(),
                            errorIndex and varBinds[int(errorIndex)-1][0] or '?'))
        break
    else:
        for varBind in varBinds:
            print(' = '.join([x.prettyPrint() for x in varBind]))