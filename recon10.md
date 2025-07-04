

````markdown
# 🧠 PentesterLab — Recon 10 (Without Aquatone)

🔗 **Challenge URL:** [https://pentesterlab.com/exercises/recon-10](https://pentesterlab.com/exercises/recon-10)

---

## 🎯 Challenge Goal

You're given a wildcard domain: `*.a.hackycorp.com`.  
Your objective is to find a **hex-based subdomain** where the image `/logo.png` contains a **flag in red text**.

This write-up solves the challenge without using Aquatone or brute-force DNS tools, relying solely on Python scripting and OpenCV.

---

## ✅ Requirements

Before running the script, install the required Python libraries:

```bash
pip3 install requests
pip3 install numpy
pip3 install opencv-python
````

> `os` and `time` are part of Python’s standard library — no installation needed.

---

## 🛠️ Tools Used

* Python 3
* `requests` — to send HTTP GET requests
* `opencv-python` — to detect red pixels in images
* `numpy` — for working with image arrays
* `os`, `time` — for file handling and delays

---

##  Solution Steps

### 1. 🔢 Generate Hex Subdomains

The script generates subdomains from `0x00` to `0xff` and constructs image URLs like:

```
http://0x00.a.hackycorp.com/logo.png  
http://0x01.a.hackycorp.com/logo.png  
...  
http://0xff.a.hackycorp.com/logo.png
```

Saved to `hex_domain.txt`.

---

### 2.  Check Which URLs Are Valid (Optional)

It checks which URLs return HTTP 200 OK and saves those to `valid_domains.txt`.

---

### 3.  Download All Valid Logo Images

Each valid `/logo.png` is downloaded and saved in a local `images/` directory as:

```
Image1.png, Image2.png, ..., ImageN.png
```

---

### 4.  Detect Red Text Using OpenCV

Using a red color mask in BGR format:

```python
lower = np.array([0, 0, 150])
upper = np.array([100, 100, 255])
```

Images containing red pixels are printed to the console for manual inspection.

---

### 5. 🏁 Final Step

Open the image(s) printed by the script — the red text will contain the **flag**.

---

---

## 📂 GitHub Link

📎 View the full working script here:
👉 [Recon 10 Python Script on GitHub](https://github.com/Thebanday/ctf-writeups/blob/Pentesterlab/recon_script.py)

---

