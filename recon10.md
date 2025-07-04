# 🧠 PentesterLab — Recon 10 (Without Aquatone)

🔗 **Challenge:** [https://pentesterlab.com/exercises/recon-10](https://pentesterlab.com/exercises/recon-10)

## 🎯 Objective

Identify a subdomain of `a.hackycorp.com` that hosts a `logo.png` image containing a flag written in **red text**.

This solution avoids using tools like **Aquatone** and instead uses pure Python automation for domain generation, image downloading, and red text detection.

---

## ✅ Prerequisites

Before running the script, make sure you have the required Python packages installed:

```bash
pip3 install requests
pip3 install numpy
pip3 install opencv-python


Solution Steps
1. 🔢 Generate Hex Subdomains
The script generates all hex values from 0x00 to 0xff and appends them to the base domain a.hackycorp.com, forming URLs like:

`http://0x00.a.hackycorp.com/logo.png`
http://0x01.a.hackycorp.com/logo.png
...
http://0xff.a.hackycorp.com/logo.png
These are saved in hex_domain.txt.

2. 🌐 Optional: Check Which URLs Are Valid
If desired, you can run a check to see which URLs return HTTP 200 OK. These are saved in valid_domains.txt.


3. 📥 Download All Valid Logo Images
The script downloads the logo.png file from each valid domain and saves it in an images/ folder as:
Image1.png, Image2.png, ..., ImageN.png


4. 🔍 Detect Red Text in Images Using OpenCV
Each image is checked for red text using this simple red BGR color mask:
lower = np.array([0, 0, 150])
upper = np.array([100, 100, 255])




You can find the full script here:[Link Text](https://github.com/Thebanday/ctf-writeups/blob/Pentesterlab/recon_script.py)




