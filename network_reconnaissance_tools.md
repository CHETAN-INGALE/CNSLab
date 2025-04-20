# Experiment: Study of Network Reconnaissance Tools

## 🎯 Aim
To study and use tools like WHOIS, dig, traceroute, and nslookup for gathering information about networks, domain registrars, and DNS infrastructure.

---

## 🛠️ Software Used
- **Operating System**: Kali Linux / Ubuntu / Windows
- **Tools**: WHOIS, dig, traceroute, nslookup

---

## 📚 Theory
**Network reconnaissance** involves gathering information about a target network or domain. These tools help in passive information gathering before launching active attacks or penetration tests.

- **WHOIS**: Retrieves domain registration details such as owner, registrar, creation/expiry dates.
- **dig**: Queries DNS servers to obtain domain IP addresses and DNS records.
- **traceroute**: Traces the path packets take from source to destination across networks.
- **nslookup**: Queries DNS to obtain domain-related information such as IP addresses and mail servers.

---

## 🧪 Commands

| Tool       | Purpose                                | Example Command               |
|------------|----------------------------------------|-------------------------------|
| WHOIS      | Get domain registration info           | `whois example.com`           |
| dig        | Get DNS records                        | `dig example.com`             |
| dig        | Get specific record (e.g., MX)         | `dig example.com MX`          |
| traceroute | Trace network path to host             | `traceroute example.com`      |
| nslookup   | Get IP for a domain                    | `nslookup example.com`        |
| nslookup   | Query specific DNS server              | `nslookup example.com 8.8.8.8`|

---

## ✅ Conclusion
Reconnaissance tools like WHOIS, dig, traceroute, and nslookup are crucial for understanding network topologies, DNS setups, and domain ownership. They aid in mapping target infrastructure and identifying potential entry points during ethical hacking or network auditing.

