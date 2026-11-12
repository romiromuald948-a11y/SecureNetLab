# SecureNetLab

Laboratoire de cybersécurité personnel simulant un réseau d'entreprise segmenté avec détection d'intrusion.

## Objectif

Construire un environnement isolé permettant de :
- Comprendre la segmentation réseau
- Configurer un firewall (pfSense)
- Détecter du trafic suspect avec Suricata
- Analyser les alertes avec un script Python

## Architecture


### Machines

| Machine   | Rôle                    | OS        | IP           |
|-----------|-------------------------|-----------|--------------|
| SNL-FW    | Firewall / Routeur      | pfSense   | 10.10.10.1 / 10.10.20.1 |
| SNL-SRV   | Serveur web + IDS       | Debian 13 | 10.10.10.10  |
| SNL-CLI   | Poste client            | Debian 13 | 10.10.20.10  |

## Fonctionnalités réalisées

- Segmentation réseau LAN / OPT1 avec pfSense
- Règles firewall pour autoriser le trafic contrôlé
- Serveur web nginx
- IDS Suricata avec règle personnalisée ICMP
- Script Python d’analyse des logs Suricata
- Génération d’alertes détectées et rapportées

## Captures d’écran

| Fichier | Description |
|---------|-------------|
| `screenshots/01-pfsense-console.png` | Interfaces du firewall |
| `screenshots/02-ping-client.png` | Communication client → serveur |
| `screenshots/03-suricata-alert.png` | Alertes dans `fast.log` |
| `screenshots/04-script-report.png` | Rapport généré par le script |

## Script d’analyse

Le script `scripts/suricata_report.py` lit `/var/log/suricata/fast.log` et génère un résumé des alertes.

Exemple de sortie :

SECURENETLAB - RAPPORT D'ALERTES SURICATA

Nombre total d'alertes : 11

Résumé par type d'alerte:

ICMP Ping Detected : 11 fois


## Comment recréer le labo

Voir le fichier `docs/setup.md`.

## Technologies utilisées

- VMware Workstation
- pfSense 2.6
- Debian 13
- nginx
- Suricata
- Python 3

## Auteur

Romuald Brice SOH  