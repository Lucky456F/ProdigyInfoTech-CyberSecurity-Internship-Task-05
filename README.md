# ProdigyInfoTech-CyberSecurity-Internship-Task-05
Task 05: Network Packet Analyzer

This project is developed as part of the **Prodigy InfoTech Cyber Security Internship**.  
The objective of this task is to build a **basic network packet analyzer** using Python
that captures and analyzes live network traffic for educational and security learning purposes.

---

## 🎯 Task Objective
To monitor network traffic in real time and display important packet details such as:
- Source IP address
- Destination IP address
- Protocol type (TCP / UDP / ICMP)
- Source and destination ports (for TCP/UDP)

This helps in understanding how data flows across a network and how different protocols operate.

---

## 🧠 How It Works
- Network data travels in the form of **packets**
- Each packet contains header information such as protocol type and IP addresses
- The tool listens to live network traffic and extracts this information
- It prints a readable summary for each captured packet

The tool **does not modify data** and **does not capture sensitive content**.
It only analyzes packet headers.

---

## 🛠️ Technologies Used
- Python 3
- Scapy library
- Npcap (for packet capture on Windows)

---

## ⚙️ Features
- Captures live network packets
- Identifies TCP, UDP, and ICMP protocols
- Displays source and destination IP addresses
- Displays port numbers for TCP and UDP packets
- Runs in real-time until stopped by the user
- Educational and ethical implementation

---

## ▶️ How to Run the Program

### 1. Install required Python library:
```bash
pip install scapy
2. Install Npcap (Windows only):
Download from the official site:
https://nmap.org/npcap/
During installation, make sure to enable:
Install Npcap in WinPcap API-compatible Mode
Install Npcap for all users

3. Run the program (Administrator mode):
Open Command Prompt or PowerShell as Administrator and run:
python packet_analyzer.py
Press CTRL + C to stop packet capture.

🧪 Example Output
📦 New Packet Captured
Source IP      : 10.42.107.35
Destination IP : 10.42.107.195
Protocol       : TCP
Source Port    : 45860
Destination Port: 57621

📂 Project Structure
ProdigyInfoTech-CyberSecurity-Internship-Task-05/
│
├── packet_analyzer.py
├── README.md


📜 Disclaimer
This project is created strictly for educational and internship purposes.
Capturing or analyzing network traffic without proper authorization is illegal and unethical.
