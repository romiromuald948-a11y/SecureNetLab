# Recréer SecureNetLab

## Prérequis
- VMware Workstation
- ISO pfSense 2.6
- ISO Debian 13 netinst

## Machines
1. SNL-FW : 1 Go RAM, 8 Go disque, 3 NICs (NAT + 2 LAN segments)
2. SNL-SRV : 1 Go RAM, 8 Go disque, 1 NIC (intnet-servers)
3. SNL-CLI : 1 Go RAM, 8 Go disque, 1 NIC (intnet-users)

## Réseaux VMware
- intnet-servers (LAN)
- intnet-users (OPT1)