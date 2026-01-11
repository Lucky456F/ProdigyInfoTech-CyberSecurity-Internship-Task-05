from scapy.all import sniff, IP, TCP, UDP, ICMP

def analyze_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("\n📦 New Packet Captured")
        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")

        if TCP in packet:
            print("Protocol       : TCP")
            print(f"Source Port    : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif UDP in packet:
            print("Protocol       : UDP")
            print(f"Source Port    : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        elif ICMP in packet:
            print("Protocol       : ICMP")

        else:
            print(f"Protocol       : Other ({protocol})")

def start_sniffing():
    print("🔐 Network Packet Analyzer Started 🔐")
    print("Press CTRL + C to stop\n")
    sniff(prn=analyze_packet, store=False)

if __name__ == "__main__":
    start_sniffing()
