#!/usr/bin/env python3

import time, random, sys, os

G = "\033[92m"
R = "\033[91m"
W = "\033[0m"

def ascii_banner(text):
    os.system('echo -e "\\033[1;34m"')
    os.system(f'figlet "{text}" | lolcat')
    os.system('echo -e "\\033[0m"')

ascii_banner("DITZZISBACK")
print(f"{G}      Dengan Teknologi Kami Menentukan Takdir Dunia Digital{W}\n")
time.sleep(0.8)

def slow(text, d=0.04):
    for ch in text:
        print(G + ch + W, end='', flush=True)
        time.sleep(d)
    print()

def bar():
    for i in range(1, 41):
        bar = "█" * i
        percent = int((i / 40) * 100)
        print(f"\r{G}SCANNING [{bar.ljust(40)}] {percent:3d}%{W}", end='')
        time.sleep(0.06 + random.random()*0.05)
    print()

fake_pw = "04121979"

ip = input(f"{G}INPUT IP TARGET : {W}") or "192.168.1.1"
time.sleep(0.4)

slow("\nPreparing modules...", 0.05)
slow("Initializing network interface...", 0.05)
slow("Loading attack-engine simulator...", 0.05)
slow("Calibrating signal decoder...", 0.05)
time.sleep(0.6)

slow("\nEnter Command :", 0.03)
cmd = input(f"{G}> {W}").lower()

if cmd != "tracking in wifi":
    slow("Command not recognized. Shutting down.", 0.03)
    sys.exit()

slow("\nStarting WiFi Tracking...\n", 0.03)
time.sleep(0.4)

steps = [
    f"Connecting to {ip}...",
    "Bypassing gateway authentication...",
    "Extracting handshake data...",
    "Analyzing encrypted packets...",
    "Measuring signal consistency...",
    "Capturing key exchange frames...",
    "Decrypting access credentials..."
]

for s in steps:
    slow(s, 0.035)
    bar()
    time.sleep(0.4)

print(f"\n{G}[✓] Wifi Berhasil Di Retas{W}")
time.sleep(0.4)
print(f"{R}❌{G} [✓] Data Wifi Akan Di Kirim...{W}\n")
time.sleep(0.8)

ssid_fake = random.choice([
    "INDIHOME_5GHz",
    "RUMAHKU24",
    "KOST-PUTRA",
    "MYHOTSPOT-X",
    "FIBERHOME-ID",
    "WARUNG_WIFI",
    "INTER-NET",
    "GalaxyHome_2.4G"
])

print(f"""
{G}------------------ WIFI REPORT ------------------
 Target IP     : {W}{ip}{G}
 SSID Detected : {W}{ssid_fake}{G}
 Security Type : {W}WPA2-PSK{G}
 Signal Level  : {W}{random.randint(55, 98)}%{G}
 Status        : {W}ACCESS SIMULATED{G}
 Password Key  : {W}{fake_pw}{G}
----------------------------------------------------{W}
""")

slow("Process completed successfully.", 0.03)
slow("Session terminated.", 0.02)
