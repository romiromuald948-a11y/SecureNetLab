#!/usr/bin/env python3
"""
SecureNetLab - Analyseur de logs Suricata
Génère un résumé des alertes à partir de fast.log
"""

from collections import Counter
from datetime import datetime

def parse_fast_log(filepath):
    alerts = []
    try:
        with open(filepath, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                if "ICMP Ping Detected" in line:
                    alerts.append("ICMP Ping Detected")
    except FileNotFoundError:
        print(f"Fichier non trouvé : {filepath}")
        return []
    return alerts

def generate_report(alerts):
    print("=" * 55)
    print("SECURENETLAB - RAPPORT D'ALERTES SURICATA")
    print(f"Généré le : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("=" * 55)

    if not alerts:
        print("Aucune alerte trouvée dans le log.")
        return

    print(f"Nombre total d'alertes : {len(alerts)}")
    print()

    counter = Counter(alerts)
    print("Résumé par type d'alerte :")
    for msg, count in counter.most_common():
        print(f"  • {msg} : {count} fois")

    print()
    print("Dernières alertes détectées :")
    for msg in alerts[-5:]:
        print(f"  - {msg}")

if __name__ == "__main__":
    log_path = "/var/log/suricata/fast.log"
    alerts = parse_fast_log(log_path)
    generate_report(alerts)