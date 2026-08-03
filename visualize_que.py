# # #------------------asignment questions--------------


# import chart_input
# import matplotlib.pyplot as mp



# user_data = chart_input.display()
# print(user_data)

# sus = chart_input.suspicious_users()
# print(sus)

# highest = chart_input.h_failed_attempt()
# print(highest)

# count = chart_input.normal_suspicious()
# print(count)


# names = []
# attempts = []

# for name, value in user_data.items():

#     names.append(name)
#     attempts.append(value)



# mp.figure(figsize=(8,4))

# mp.bar(names, attempts)

# mp.title("Failed Attempts")

# mp.xlabel("Users")

# mp.ylabel("Failed Attempts")

# mp.show()


# labels = ["Normal Users", "Suspicious Users"]
# sizes = [count[0], count[1]]

# mp.figure(figsize=(6,6))

# mp.pie(
#     sizes,
#     labels=labels,
  
# )

# mp.title("Normal vs Suspicious Users")
# mp.axis("equal")

# mp.show()




#------------------que 2----------

# import chart_input

# print(chart_input.__file__)
# import matplotlib.pyplot as mp


# suspicious_ips = chart_input.suspicious()
# active_ip, active_requests = chart_input.most_active_ip()
# normal_count, suspicious_count = chart_input.count()


# print(active_ip)
# print(active_requests)

# print("\nSuspicious IPs")
# print(suspicious_ips)

# # print("\nMost Active IP")
# # print(active_ip, "->", active_requests, "requests")

# print("\nNormal IPs :", normal_count)
# print("Suspicious IPs :", suspicious_count)



# mp.figure(figsize=(15,6))
# mp.bar(chart_input.ip.keys(), chart_input.ip.values())
# mp.title("Requests per IP")
# mp.xlabel("IP Address")
# mp.ylabel("Requests")
# mp.show()



# mp.figure(figsize=(6,6))
# mp.pie(
#     [normal_count, suspicious_count],
#     labels=["Normal", "Suspicious"],
    
# )
# mp.title("Normal vs Suspicious IPs")
# mp.show()

#---------------que 3 

# import chart_input
# import matplotlib.pyplot as mp


# classify_data=chart_input.classify()
# print(classify_data)



# file_name=[]
# scores=[]

# for file,data in chart_input.files.items():


#     file_name.append(file)
#     scores.append(data["score"])

# print(file_name)
# print(scores)


# mp.figure(figsize=(10,12))

# mp.bar(file_name,scores)
# mp.title("score of each file")
# mp.xlabel("files Name")
# mp.ylabel("Scores")

# mp.show()



# mp.pie(
#     scores,labels=file_name)


# mp.show()





#que 4---

# import chart_input
# import matplotlib.pyplot as mp

# total=chart_input.total_packets(chart_input.network_traffic)
# print(total)




# most_used=chart_input.most_used_protocol(chart_input.network_traffic)
# print(most_used)


# above=chart_input.above_1000(chart_input.network_traffic)
# print(above)



# mp.figure(figsize=(8,5))
# mp.bar(chart_input.network_traffic.keys(), chart_input.network_traffic.values())
# mp.title("Packets per Protocol")
# mp.xlabel("Protocol")
# mp.ylabel("Packet Count")

# mp.show()


# mp.figure(figsize=(7,7))
# mp.pie(
#      chart_input.network_traffic.values(),
#     labels= chart_input.network_traffic.keys(),
    
# )
# mp.title("Protocol-Traffic Distribution")
# mp.show()

#---------QUE --5---------

# import chart_input
# import matplotlib.pyplot as mp



# high = chart_input.high_canned_ports(chart_input.port_scan)
# print(high)



# target = chart_input.most_targeted_port(chart_input.port_scan)
# print(target)

# risk = chart_input.risk_count(chart_input.port_scan)
# print(risk)


# mp.figure(figsize=(10,5))

# mp.bar(
#     [str(port) for port in chart_input.port_scan.keys()],
#     chart_input.port_scan.values()
# )

# mp.title("Scan Attempts Per Port")
# mp.xlabel("Port Number")
# mp.ylabel("Scan Attempts")

# mp.show()


# mp.figure(figsize=(6,6))

# mp.pie(
#     risk.values(),
#     labels=risk.keys(),
# )

# mp.title("Low Risk vs High Risk Ports")

# mp.show()


#-------------------------------q-6------------------------

import chart_input
import matplotlib.pyplot as mp


counts = chart_input.count_attack_types(
    chart_input.security_alerts
)



for attack, count in counts.items():
    print(f"{attack}: {count}")



attack, count = chart_input.most_common_attack(chart_input.security_alerts)

attack,count = chart_input.least_common_attack(chart_input.security_alerts)
















# -----------------------use numpy assignment que-----------------

import use_numpy 
import matplotlib.pyplot as mp


students =["student 1","student 2","student 3"]

overall_marks = total()
avg = average()
highest_marks = highest_student()
percentage = per()

print(overall_marks)
print(avg)
print(highest_marks)

mp.bar(students,totals)
mp.show

mp.pie(percentage, labels=students)
mp.show()
