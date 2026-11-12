# Recréer SecureNetLab

## Prérequis

- VMware Workstation
- ISO pfSense 2.6 (ou plus récent)
- ISO Debian 13 netinst

## 1. Création des réseaux VMware

Dans VMware :
- Crée deux réseaux internes :
  - intnet-servers (pour le LAN)
  - intnet-users (pour OPT1)

## 2. Création des machines

| Machine | RAM | Disque | NICs |
|---------|-----|--------|------|
| SNL-FW  | 1 Go | 8 Go | 3 (NAT + intnet-servers + intnet-users) |
| SNL-SRV | 1 Go | 8 Go | 1 (intnet-servers) |
| SNL-CLI | 1 Go | 8 Go | 1 (intnet-users) |

## 3. Installation de pfSense (SNL-FW)

1. Installe pfSense depuis l’ISO
2. Assigne les interfaces :
   - WAN → em0 (NAT)
   - LAN → em1 (intnet-servers)
   - OPT1 → em2 (intnet-users)
3. Configure les IP :
   - LAN : 10.10.10.1/24
   - OPT1 : 10.10.20.1/24

### Ajouter une règle ICMP (Shell pfSense)

easyrule pass opt1 icmp any any

Vérifier :
pfctl -sr | grep opt1

## 4. Installation de SNL-SRV (Debian)

1. Installe Debian 13
2. Configure l’IP statique :
   ip addr add 10.10.10.10/24 dev ens33
   ip route add default via 10.10.10.1
3. Installe les services :
   apt update
   apt install -y nginx suricata

### Règle Suricata personnalisée

echo 'alert icmp any any -> any any (msg:"ICMP Ping Detected"; sid:1000001; rev:1;)' > /var/lib/suricata/rules/local.rules

Ajoute dans /etc/suricata/suricata.yaml :
rule-files:
  - local.rules

Puis :
systemctl restart suricata

## 5. Installation de SNL-CLI (Debian)

1. Installe Debian 13
2. Configure l’IP :
   ip addr add 10.10.20.10/24 dev ens33
   ip route add default via 10.10.20.1

## 6. Tests

### Depuis SNL-CLI
ping -c 3 10.10.10.10
curl http://10.10.10.10

### Depuis SNL-SRV
tail -n 10 /var/log/suricata/fast.log
python3 /root/suricata_report.py

## 7. Script d’analyse

Copie le script scripts/suricata_report.py sur SNL-SRV et lance-le :
python3 /root/suricata_report.py

## Notes

- Les règles easyrule sont temporaires (elles disparaissent au reboot).
- Pour les rendre permanentes, utilise l’interface web de pfSense.
- Pense à corriger la route par défaut sur SNL-SRV si elle devient 169.254.x.x.