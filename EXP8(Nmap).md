# Experiment: Nmap Installation and Usage

## 🎯 Aim
To install and use Nmap for network scanning to identify active hosts, open ports, and running services.

---

## 🛠️ Software Used
- **Operating System**: Kali Linux / Ubuntu
- **Tool**: Nmap (Network Mapper)

---

## 📚 Theory
**Nmap** (Network Mapper) is an open-source tool used for network discovery and security auditing. It can scan large networks as well as single hosts. Nmap provides information like:

- Live hosts on the network
- Open and filtered ports
- Running services and versions
- Operating system detection
- Network vulnerabilities (via scripts)

---

## 🧪 Commands

| Task                          | Command                                 |
|-------------------------------|------------------------------------------|
| Scan a single IP              | `nmap 192.168.1.1`                       |
| Scan a range of IPs           | `nmap 192.168.1.1-10`                    |
| Detect OS and services        | `nmap -A 192.168.1.1`                    |
| Scan specific ports           | `nmap -p 22,80,443 192.168.1.1`          |
| Scan all ports                | `nmap -p- 192.168.1.1`                   |
| Fast scan (top 100 ports)     | `nmap -F 192.168.1.1`                    |
| Verbose output                | `nmap -v 192.168.1.1`                    |

---

## ✅ Conclusion
Nmap is an essential tool for ethical hacking and cybersecurity. It helps in network reconnaissance, identifying potential vulnerabilities, and securing systems by analyzing open services and ports. Understanding its commands and usage improves a network administrator's ability to assess security posture effectively.
