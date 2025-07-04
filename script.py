import requests, os, time, subprocess, cv2
import numpy as np

# Create all hex domains
if not os.path.exists("hex_domains.txt"):
    with open("hex_domain.txt", "w") as file:
        print("Creating hex domains. Please wait..\n")
        for i in range(0, 256):
            domains = "http://" + hex(i) + ".a.hackycorp.com/logo.png"
            file.write(domains + "\n")
        print("Hex domains created\n")

# Check valid domains (optional)
if not os.path.exists("valid_domains.txt"):
    with open("hex_domain.txt", "r") as f:
        print("Saving valid domains in the file. Please wait....\n")
        for lines in f.readlines():
            urls = lines.strip()
            try:
                response = requests.get(urls, timeout=10)
                if response.status_code == 200:
                    with open("valid_domains.txt", "a") as f:
                        f.write(urls + "\n")
            except:
                continue
        print("All valid domains downloaded\n")

# Create directory to save images
os.makedirs("images", exist_ok=True)

# Download images
with open("valid_domains.txt", "r") as f:
    for index, url in enumerate(f.readlines(), start=1):
        urls = url.strip()
        try:
            response = requests.get(urls, timeout=10)
            response.raise_for_status()
            ext = ".png"
            file_name = f"Image{index}{ext}"
            file_path = os.path.join("images", file_name)
            with open(file_path, "wb") as final_file:
                final_file.write(response.content)
            print(f"{index}: Downloaded {file_name} from {urls}")
        except Exception as e:
            print(f"❌ Failed: {urls} - {e}")

# Detect red color in images
folder_path = "images"
lower = np.array([0, 0, 150])
upper = np.array([100, 100, 255])

for filename in os.listdir(folder_path):
    if filename.lower().endswith(".png"):
        file_p = os.path.join(folder_path, filename)
        img = cv2.imread(file_p)
        mask = cv2.inRange(img, lower, upper)
        if np.count_nonzero(mask) > 0:  # checks if any red pixels found
            print(f"{filename} contains red color")
