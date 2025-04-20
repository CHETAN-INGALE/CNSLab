# Experiment: Study of Network Reconnaissance Tools

## 🎯 Aim
To study and use tools like WHOIS, dig, traceroute, and nslookup for gathering information about networks, domain registrars, and DNS infrastructure.

---

## 🛠️ Software Used
- **Operating System**: Kali Linux / Ubuntu / Windows  
- **Tools**: WHOIS, dig, traceroute, nslookup

---

## 📚 Theory
**Network reconnaissance** involves gathering information about a target network or domain. These tools help in passive information gathering before any attack or security audit.

---

### 🔍 WHOIS
- **Purpose**: Retrieves domain registration info.
- **Theory**: WHOIS queries the global domain registry databases to get the domain owner's details, such as registrar, creation & expiry date, nameservers, and contact info.
- **Command**:
  ```bash
  whois example.com
  ```

---

### 🔍 dig (Domain Information Groper)
- **Purpose**: Gets detailed DNS records.
- **Theory**: `dig` is used to query DNS servers for records like A (IP), MX (mail), NS (nameserver), and TXT. It helps in understanding how DNS is configured for a domain.
- **Commands**:
  ```bash
  dig example.com        # Default A record
  dig example.com MX     # Fetches mail server records
  ```

---

### 🔍 traceroute
- **Purpose**: Traces the packet path from your system to a host.
- **Theory**: It sends packets with increasing TTL values to discover each hop (router) on the route to the destination. Helps locate bottlenecks and latency issues.
- **Command**:
  ```bash
  traceroute example.com
  ```

---

### 🔍 nslookup
- **Purpose**: Resolves domain names and queries DNS records.
- **Theory**: It helps check how DNS resolves a domain name to IP and can be used to query different types of DNS records using a specific DNS server.
- **Commands**:
  ```bash
  nslookup example.com
  nslookup example.com 8.8.8.8
  ```

---

## ✅ Conclusion
These reconnaissance tools are essential in cybersecurity to gather public domain and network information. They assist ethical hackers and analysts in mapping infrastructure, identifying potential vulnerabilities, and performing DNS diagnostics.
