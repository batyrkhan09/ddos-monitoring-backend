import datetime
import random  # Используем для имитации IP

def log_to_file(message):
    with open("ddos_log.txt", "a", encoding="utf-8") as file:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        file.write(f"[{timestamp}] {message}\n")

def block_ip(ip):
    # Имитация блокировки — можно подключить iptables/firewall
    log_to_file(f"🚫 IP {ip} has been blocked due to high traffic.")

def detect_ddos(stats):
    threshold_packets = 300
    packets = stats["packets_recv"]
    is_attack = packets > threshold_packets

    fake_ip = f"192.168.1.{random.randint(2, 254)}"  # Имитация IP

    if is_attack:
        log_to_file(f"⚠️ DDoS detected! Packet rate: {packets} pkt/s from {fake_ip}")
        block_ip(fake_ip)
        return {
            "is_ddos": True,
            "ip": fake_ip,
            "details": f"⚠️ High packet rate: {packets} pkt/s from {fake_ip}"
        }
    else:
        log_to_file(f"✅ Normal traffic: {packets} pkt/s")
        return {
            "is_ddos": False,
            "ip": None,
            "details": f"✅ Normal traffic: {packets} pkt/s"
        }
