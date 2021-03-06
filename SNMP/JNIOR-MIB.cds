g-- The JNIOR has implemented SNMP v1.
-- To enable SNMP on the JNIOR go to the JNIOR web page Configuration/Misc tab
-- or define the Device/SNMP registry key with 
-- the value of "enabled".  Furthermore you can define whether certain 
-- I/O points send traps for states and alarms by defining the 
-- IO/Inputs/din#/SnmpTrap or IO/Outputs/rout#/SnmpTrap registry keys with 
-- the "enabled" value.  SNMP Traps should not be defined for IO points 
-- that change state rapidly.
-- The community string can be set by defining the Snmp/CommunityString.  
-- By default the community string is "public".
-- It should be known that the JNIOR is not a high speed device therefore 
-- SNMP can be relatively slow.  SNMP traps can have a direct impact on I/O logging 
-- performance.  Therefore the JNIOR should not be configured for a large 
-- number of traps
 ;"This is sent when the JNIOR has general event information"                                                     Z"States of all inputs represented as a single byte.  MSB 
          representing input 8"                       ""                       ."An input entry containing state information."                       "The channel of the input"                       "The state of the input"                       Y"States of all outputs represented in two bytes.  MSB 
          representing output 16"                       ""                       /"An output entry containing state information."                       "The channel of the output"                       "The state of the output"                           "This is the unique serial number of the JNIOR.  The serial number is 
            assigned during the manufacturing process."                                  