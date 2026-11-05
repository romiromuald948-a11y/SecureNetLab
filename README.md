# SecureNetLab

Labo de cybersécurité avec segmentation réseau (pfSense) et détection d'intrusion (Suricata).

## Architecture

- **SNL-FW** : pfSense (firewall + routage)
  - WAN : NAT
  - LAN : 10.10.10.0/24
  - OPT1 : 10.10.20.0/24
- **SNL-SRV** : Debian 13 (serveur)
  - IP : 10.10.10.10
  - Services : nginx + Suricata
- **SNL-CLI** : Debian 13 (client)
  - IP : 10.10.20.10

## Fonctionnalités

- Segmentation réseau LAN / OPT1
- Serveur web (nginx)
- IDS Suricata avec règles personnalisées
- Communication contrôlée entre les segments

## Captures

Voir le dossier `screenshots/`.

## Recréer le labo

Voir `docs/setup.md`.