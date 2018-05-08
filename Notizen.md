 - UseCase schicken
 - Netzwerk Design schicken
 - Frage: DNA Center
 - Materialliste
 - Degration 

# IP Adressen
DNA Center Netze
10.22.0.0/16

10.22.0.0/24 

| NET      | Use |
| 10.22.0.0/24 


# Passwörter

DNA-Center 
maglev hallo@1234
admin hallo@1234

# Befehle First 
hostname <>
snmp-server community hallo@1234 ro
username dnaadmin privilege 15 password 0 hallo@1234
interface Loopback 0 
ip address 10.22.0.73 255.255.255.0

# DHCP Options

## DHCP Option 43
5A1N;B2;K4;I10.22.0.100;J80

## DHCP Option 60
ciscopnp


# Infoblox

 - Select IPAM and add Network for Fabric
 - Select DHCP
 - Select Network => Edit
 - Add DHCP Options 43 and 60
 - Add DHCP IP Pool

# DNA PNP Error 
Hardware: WS-C3850-12XS-S

https://quickview.cloudapps.cisco.com/quickview/bug/CSCvh73089

Verursachte: ERROR_DURING_CERTIFICATE_INSTALL

Lösung: Delete and wait until reapeears.

# DNA Center Stuck Updates
(Siehe Screenshot)

# Probleme beim Update Prozess
- Updates können nicht automatisch installiert werden.
- D.h. die einzelnen Updates müssen ausgewählt werden und manuell Installiert werden. 

# TFTP Server für Update
01.05.2018
Weil das Update für den DNA Server nicht geklappt haben:
- tftpd-hap installiert auf OrangePi
- (rest siehe Screenshots)
- Installation via tftp war erfolgreich
