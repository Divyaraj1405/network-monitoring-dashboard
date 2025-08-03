import csv
import random
from datetime import datetime

ips = ["192.168.1.1", "10.0.0.5", "172.16.0.3", "192.168.0.4"]
protocols = ["TCP", "UDP", "ICMP"]
ports = [22, 80, 443, 8080, 3306]

with open("logs.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["timestamp", "ip", "protocol", "port", "status"])

    for _ in range(100):
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            random.choice(ips),
            random.choice(protocols),
            random.choice(ports),
            random.choice(["OK", "SUSPICIOUS", "FAILED"])
        ])