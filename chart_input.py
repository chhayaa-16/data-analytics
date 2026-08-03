
# # CYBER SECURITY ANALYSIS
# # 10 HARD PRACTICAL QUESTIONS
# # Python + Functions + Dictionaries + Matplotlib

# # Topics:
# # - Python Dictionary
# # - Nested Dictionary
# # - Functions
# # - Loops
# # - Conditions
# # - Modules
# # - Matplotlib
# # - Bar Chart
# # - Pie Chart


# # # ============================================================
# # # 1. FAILED LOGIN ANALYSIS
# # # ============================================================

# # # Create a dictionary containing 15 users and their number of failed login attempts.

# # # Create functions to:
# # # - Display all users
# # # - Find users with more than 5 failed attempts
# # # - Find the user with the highest failed attempts
# # # - Count normal vs suspicious users

# # # Create:
# # # - Bar chart: Failed login attempts per user
# # # - Pie chart: Normal vs Suspicious users



# # # -------------------------------
# # # CYBER SECURITY ANALYSIS
# # # -------------------------------

# users = {
#    "A": 6,
#     "B": 4,
#     "C": 6,
#     "D": 9,
#     "E": 1,
#     "F": 3,
#     "G": 3,
#     "H": 9,
#     "I": 3,
#     "J": 8,
#     "K": 2,
#     "L": 8,
#     "M": 4,
#     "N": 7,
#     "O": 6
# }


# def display():
#     for name, attempt in users.items():
#         print(f"{name} : {attempt}")

#     return users


# def suspicious_users():

#     suspicious = {}

#     for name, attempt in users.items():

#         if attempt > 5:
#             suspicious[name] = attempt

#     print(suspicious)

#     return suspicious


# def h_failed_attempt():

#     highest = max(users, key=users.get)

#     result = {
#         "User": highest,
#         "Attempts": users[highest]
#     }

#     print(result)

#     return result

# def normal_suspicious():

#     normal = 0
#     suspicious = 0

#     for attempt in users.values():

#         if attempt > 5:
#             suspicious += 1
#         else:
#             normal += 1

#     print("normal user : ", normal)
#     print("suspicious user",suspicious)

#     return normal,suspicious






# #quee... 2. IP ADDRESS ATTACK ANALYSIS

# # Create data containing IP addresses and the number of requests received from each IP.
# # Example:

# # 192.168.1.10 -> 120 requests
# # 192.168.1.20 -> 450 requests
# # 192.168.1.30 -> 80 requests

# # Create functions to:
# # - Find suspicious IPs where requests > 300
# # - Find the most active IP
# # - Count Normal vs Suspicious IPs

# # Create:
# # - Bar chart: Requests per IP
# # - Pie chart: Normal IP vs Suspicious IP



# ip = {
#     "192.168.1.10": 400,
#     "192.168.1.20": 170,
#     "192.168.1.30": 50,
#     "192.168.1.40": 550,
#     "192.168.1.50": 300,
#     "192.168.1.60": 700,
#     "192.168.1.70": 130,
#     "192.168.1.80": 70,
#     "192.168.1.90": 230,
#     "192.168.1.100": 435
# }

# def suspicious():

    
#     suspicious_ips = {}

#     for ip_address, requests in ip.items():
#         if requests > 300:
#             suspicious_ips[ip_address] = requests

#     return suspicious_ips


# def most_active_ip():
#     max_ip = max(ip, key=ip.get)
#     return max_ip, ip[max_ip]

# def count():
#     normal = 0
#     suspicious = 0

#     for requests in ip.values():
#         if requests > 300:
#             suspicious += 1
#         else:
#             normal += 1

#     return normal, suspicious





# # ============================================================
# # 3. MALWARE DETECTION ANALYSIS
# # ============================================================

# # Create a dictionary of 20 files containing:

# # - File Name
# # - File Size
# # - Detection Score

# # Create functions to classify files:

# # 0-30    -> Safe
# # 31-70   -> Suspicious
# # 71-100  -> Malicious

# # Create:
# # - Bar chart: Detection score of each file
# # - Pie chart: Safe vs Suspicious vs Malicious files




# files = {
#     "File1.exe": {"size": 1200, "score": 12},
#     "File2.dll": {"size": 850, "score": 45},
#     "File3.pdf": {"size": 430, "score": 78},
#     "File4.docx": {"size": 620, "score": 25},
#     "File5.zip": {"size": 1500, "score": 66},
#     "File6.exe": {"size": 980, "score": 90},
#     "File7.mp4": {"size": 5000, "score": 15},
#     "File8.jpg": {"size": 2100, "score": 34},
#     "File9.txt": {"size": 150, "score": 5},
#     "File10.exe": {"size": 1800, "score": 82},
#     "File11.dll": {"size": 900, "score": 55},
#     "File12.iso": {"size": 7200, "score": 95},
#     "File13.png": {"size": 780, "score": 20},
#     "File14.rar": {"size": 3400, "score": 70},
#     "File15.doc": {"size": 560, "score": 31},
#     "File16.exe": {"size": 1600, "score": 88},
#     "File17.xls": {"size": 450, "score": 28},
#     "File18.ppt": {"size": 980, "score": 60},
#     "File19.bat": {"size": 100, "score": 74},
#     "File20.sys": {"size": 1300, "score": 42}
# }


# # def classify():

# #     clasify={}

# #     for file,size,score in files.items():
# #         clasify[file]={}


# #         if 0 <= score <= 30:
# #                 print("Safe")
# #         elif 31 <= score <= 70:
# #                 print("Suspicious")
# #         elif 71 <= score <= 100:
# #                 print("Malicious")
# #         else:
# #                 print("Invalid")

# #     return classify()       

# def classify():

#     clasify_data={}

#     for file, data in files.items():
#         score = data["score"]

#         # for size, score in data.items():

#         if score <= 30:
#             clasify_data[file] = "Safe"
#         elif 31 <= score <= 70:
#             clasify_data[file] = "Suspicious"
#         elif 71 <= score <= 100:
#             clasify_data[file] = "Malicious"
#         else:
#             clasify_data[file] = "Invalid"
 
#     return clasify_data








# # 4. NETWORK PROTOCOL ANALYSIS
# # ============================================================

# # Create network traffic data containing:

# # HTTP
# # HTTPS
# # FTP
# # SSH
# # DNS
# # SMTP

# # and their packet counts.

# # Create functions to:
# # - Calculate total packets
# # - Find the most-used protocol
# # - Find protocols having more than 1,000 packets

# # Create:
# # - Bar chart: Packets per protocol
# # - Pie chart: Protocol-wise traffic distribution



# network_traffic = {
#     "HTTP": 500,
#     "HTTPS": 6500,
#     "FTP": 300,
#     "SSH": 700,
#     "DNS": 1200,
#     "SMTP": 900
# }


# def total_packets(data):
#     return sum(data.values())

# def most_used_protocol(data):
#     protocol = max(data, key=data.get)
#     return protocol, data[protocol]



# def above_1000(data):
#     return {protocol: packets
#             for protocol, packets in data.items()
#             if packets > 1000}


# for protocol, packets in network_traffic.items():
#     print(f"{protocol}: {packets} packets")

# print("\nTotal Packets:", total_packets(network_traffic))

# protocol, packets = most_used_protocol(network_traffic)
# print(f"Most Used Protocol: {protocol} ({packets} packets)")

# for protocol, packets in above_1000(network_traffic).items():
#     print(f"{protocol}: {packets}")




# # ============================================================
# # 5. PORT SCAN ANALYSIS
# # ============================================================

# # Create a dictionary containing 15 ports and their scan attempts.

# # Example:

# # 22   -> 120
# # 80   -> 450
# # 443  -> 380
# # 21   -> 50
# # 3389 -> 700

# # Create functions to:
# # - Identify highly scanned ports
# # - Find the most targeted port
# # - Count low-risk vs high-risk ports

# # Create:
# # - Bar chart: Scan attempts per port
# # - Pie chart: Low-risk vs High-risk ports


# port_scan = {
#     21: 50,
#     22: 120,
#     23: 90,
#     25: 70,
#     53: 180,
#     80: 450,
#     110: 60,
#     135: 200,
#     139: 170,
#     143: 80,
#     443: 380,
#     445: 320,
#     8080: 250,
#     3306: 150,
#     3389: 700
# }



# def high_scanned_ports(data):
#     return {port: scans for port, scans in data.items() if scans > 200}


# def most_targeted_port(data):
#     port = max(data, key=data.get)
#     return port, data[port]


# def risk_count(data):
#     low_risk = 0
#     high_risk = 0

#     for scans in data.values():
#         if scans > 200:
#             high_risk += 1
#         else:
#             low_risk += 1

#     return {
#         "Low Risk": low_risk,
#         "High Risk": high_risk
#     }



# print("Port Scan Attempts\n")

# for port, scans in port_scan.items():
#     print(f"Port {port}: {scans} scans")


# print(high_scanned_ports(port_scan))

# port, scans = most_targeted_port(port_scan)
# print(f"\nMost Targeted Port: {port} ({scans} scans)")

# print("\nRisk Count")
# print(risk_count(port_scan))





# 6. SECURITY ALERT ANALYSIS
# ============================================================

# Create security alert data for 30 events.

# Categories:

# Brute Force
# Malware
# Phishing
# Port Scan
# Unauthorized Access
# DDoS

# Create functions to:
# - Count each attack type
# - Find the most common attack
# - Find the least common attack

# Create:
# - Bar chart: Attack type vs number of alerts
# - Pie chart: Percentage of each attack type

# Condition:
# Do not manually count anything. Everything must be calculated using functions.


security_alerts = [
    "Brute Force",
    "Malware",
    "Phishing",
    "Port Scan",
    "Unauthorized Access",
    "DDoS",
    "Malware",
    "Phishing",
    "Brute Force",
    "Port Scan",
    "Malware",
    "DDoS",
    "Unauthorized Access",
    "Brute Force",
    "Malware",
    "Port Scan",
    "Phishing",
    "Brute Force",
    "DDoS",
    "Unauthorized Access",
    "Malware",
    "Phishing",
    "Port Scan",
    "Brute Force",
    "Malware",
    "DDoS",
    "Unauthorized Access",
    "Port Scan",
    "Phishing",
    "Malware"
]





def count(alerts):
    return Counter(alerts)




def most_common_attack(alerts):
    counts = count(alerts)
    attack = max(counts, key=counts.get)
    return attack, counts[attack]

def least_common_attack(alerts):
    counts = count(alerts)
    attack =min(counts, key=count.get)
    return attack,counts[attack]


def most_common_attack(alerts):
    counts = count(alerts)
    







