# Hack The Box - Cap Write-Up

You can access the machine [here](https://www.hackthebox.com/machines/Cap) on Hack The Box.

* **Target IP:** `10.10.10.245`

---

## 🌐 Initial Scanning

1. **Checked if the machine is up:**

   ```bash
   ping 10.10.10.245
   ```

2. **Ran an Nmap TCP scan:**

   ```bash
   nmap -sT -A 10.10.10.245
   ```

   **Key Nmap Findings:**

   * **FTP (21/tcp):** vsftpd 3.0.3
   * **SSH (22/tcp):** OpenSSH 8.2p1 (Ubuntu)
   * **HTTP (80/tcp):** Gunicorn server running a web app called *Security Dashboard*

---

## 🔍 Enumeration

### 🧭 Web Service (Port 80)

* Visited `http://10.10.10.245` and found a **Security Dashboard** interface.

* Noted several features on the page:

  * Ifconfig
  * Security Snapshot (5-second PCAP + Analysis)
  * IP Config
  * Network Status

* Observed that the **Security Snapshot** section triggered a GET request with a parameter like `/data/1`.

---

## 🕵️ IDOR Vulnerability

* Tested the `cap` parameter:

  * Changing `cap=1` to `cap=2`, etc., revealed **different PCAP files**.
  * **Insecure Direct Object Reference (IDOR)** was present.
  * Could access PCAP files of other sessions.
  * Downloaded and inspected these `.pcap` files using **Wireshark**.

### 🧠 Key Discovery

* At `cap=0`, found a PCAP file containing **plaintext credentials** during a captured HTTP or FTP session.

---

## 🔐 Gaining Access

* Used the discovered credentials to log in via SSH:

  ```bash
  ssh <user>@10.10.10.245
  ```
* Successfully gained shell access as the user and captured the **user flag**.

---

## ⚙️ Privilege Escalation

* Performed local enumeration and found:

  * **Python 3.8** installed
  * A **capability set** on the Python binary:

    ```bash
    getcap -r / 2>/dev/null
    ```

    Output:

    ```bash
    /usr/bin/python3.8 = cap_setuid+ep
    ```

* Used [GTFOBins Python Capabilities](https://gtfobins.github.io/gtfobins/python/#capabilities) to escalate privileges:

  ```bash
  /usr/bin/python3.8 -c 'import os; os.setuid(0); os.system("/bin/bash")'
  ```

* Became **root**, accessed `/root/root.txt`, and retrieved the **root flag**.

---

## ✅ Summary

* Exploited an **IDOR vulnerability** to extract PCAP files.
* Recovered **plaintext credentials** from network traffic.
* Gained user access via **SSH**.
* Escalated to **root** using Python capabilities.


