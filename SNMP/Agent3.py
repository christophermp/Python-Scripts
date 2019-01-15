from easysnmp import snmp_get, snmp_set, snmp_walk

# Grab a single piece of information using an SNMP GET
snmp_get('sysDescr.0', hostname='192.168.0.100', community='public', version=1)

# Perform an SNMP SET to update data
snmp_set(
    'sysLocation.0', 'My Cool Place',
    hostname='localhost', community='public', version=1
)

# Perform an SNMP walk
snmp_walk('system', hostname='localhost', community='public', version=1)