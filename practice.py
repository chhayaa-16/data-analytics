name = input("Enter Student Name: ")

marks = []
for i in range(5):
    mark = int(input(f"Enter Marks of Subject {i+1}: "))
    marks.append(mark)

display_result=(name, marks)









# #que=3
# # Employee Salary Analyzer

# def monthly_salary(basic):
#     print(basic)

# def annual_salary(monthly):
#     print( monthly * 12)

# def bonus(annual):
#     print( annual * 0.10)

# def tax(annual):
#     print( annual * 0.05)

# def display_report(name, basic):
#     monthly = monthly_salary(basic)
#     annual = annual_salary(monthly)
#     emp_bonus = bonus(annual)
#     emp_tax = tax(annual)
#     net_salary = annual + emp_bonus - emp_tax

#     print("\n------ Salary Report ------")
#     print("Employee Name :", name)
#     print("Monthly Salary :", monthly)
#     print("Annual Salary :", annual)
#     print("Bonus (10%) :", emp_bonus)
#     print("Tax (5%) :", emp_tax)
#     print("Net Annual Salary :", net_salary)



# name = input("Enter Employee Name: ")
# basic = float(input("Enter Monthly Salary: "))

# display_report(name, basic)




# #que -4
# # Sales Report Generator

# def total_sales(sales):
#     print( sum(sales))

# def average_sales(sales):
#     print (sum(sales) / len(sales))

# def highest_sales(sales):
#     print (max(sales))

# def lowest_sales(sales):
#     print( min(sales))

# def display_summary(sales):
#     print("\n------ Sales Summary ------")
#     print("Sales Data :", sales)
#     print("Total Sales :", total_sales(sales))
#     print("Average Sales :", round(average_sales(sales), 2))
#     print("Highest Sales :", highest_sales(sales))
#     print("Lowest Sales :", lowest_sales(sales))



# sales = []

# n = int(input("Enter Number of Sales: "))

# for i in range(n):
#     amount = float(input(f"Enter Sale {i+1}: "))
#     sales.append(amount)

# display_summary(sales)



# security_functions.py





# PRACTICAL 3: Cricket Performance Analyzer

# import statistics

# # Dictionary to store player names and their runs
# players = {
#     "Virat Kohli": 85,
#     "Rohit Sharma": 120,
#     "Shubman Gill": 65,
#     "KL Rahul": 45,
#     "Hardik Pandya": 90,
#     "Ravindra Jadeja": 55
# }

# # Function to display player statistics
# def display_player_statistics(players):
#     print("\nPlayer Statistics")
#     print("-" * 30)
#     for player, runs in players.items():
# 
#       print(f"{player:20} : {runs} runs")


# # Function to find the highest run scorer
# def highest_run_scorer(players):
#     player = max(players, key=players.get)
#     return player, players[player]


# # Function to find the lowest run scorer
# def lowest_run_scorer(players):
#     player = min(players, key=players.get)
#     return player, players[player]


# # Function to calculate average runs
# def average_runs(players):
#     return sum(players.values()) / len(players)


# Function to display players who scored above average
# def above_average_players(players):
#     avg = average_runs(players)

#     print("\nPlayers Scoring Above Average")
#     print("-" * 35)
#     for player, runs in players.items():
#         if runs > avg:
#             print(f"{player:20} : {runs} runs")


# # Main function
# def main():
#     print("=" * 50)
#     print("      CRICKET PERFORMANCE ANALYZER")
#     print("=" * 50)

#     # Display player statistics
#     display_player_statistics(players)

#     # Highest scorer
#     highest_player, highest_runs = highest_run_scorer(players)
#     print(f"\nHighest Run Scorer : {highest_player} ({highest_runs} runs)")

#     # Lowest scorer
#     lowest_player, lowest_runs = lowest_run_scorer(players)
#     print(f"Lowest Run Scorer  : {lowest_player} ({lowest_runs} runs)")

#     # Average runs
#     avg = average_runs(players)
#     print(f"Average Runs       : {avg:.2f}")

#     # Players above average
#     above_average_players(players)

#     # Statistics module
#     runs = list(players.values())

#     print("\nStatistical Analysis")
#     print("-" * 30)
#     print(f"Mean               : {statistics.mean(runs):.2f}")
#     print(f"Median             : {statistics.median(runs):.2f}")
#     print(f"Standard Deviation : {statistics.stdev(runs):.2f}")


# # Execute the program
# if __name__ == "__main__":
#     main()































# # Practical 4: IPL Player Performance Analyzer

# import statistics

# # Sample IPL player data
# players = {
#     "Virat Kohli": {"runs": 741, "matches": 15},
#     "Rohit Sharma": {"runs": 417, "matches": 14},
#     "Shubman Gill": {"runs": 890, "matches": 17},
#     "MS Dhoni": {"runs": 161, "matches": 14},
#     "KL Rahul": {"runs": 520, "matches": 14}
# }


# # Function to calculate runs per match
# def runs_per_match(player):
#     return player["runs"] / player["matches"]


# # Function to find the best-performing batsman
# def best_batsman(players):
#     return max(players, key=lambda name: runs_per_match(players[name]))


# # Function to find the lowest-performing player
# def lowest_player(players):
#     return min(players, key=lambda name: runs_per_match(players[name]))


# # Function to calculate team's average runs
# def team_average_runs(players):
#     total_runs = sum(player["runs"] for player in players.values())
#     return total_runs / len(players)


# # Function to classify player performance
# def classify_player(rpm):
#     if rpm >= 50:
#         return "Excellent"
#     elif rpm >= 40:
#         return "Good"
#     elif rpm >= 30:
#         return "Average"
#     else:
#         return "Poor"


# # Main function
# def main():
#     print("=" * 55)
#     print("        IPL PLAYER PERFORMANCE REPORT")
#     print("=" * 55)

#     performance = []

#     for name, data in players.items():
#         rpm = runs_per_match(data)
#         performance.append(rpm)

#         print(f"\nPlayer : {name}")
#         print(f"Runs   : {data['runs']}")
#         print(f"Matches: {data['matches']}")
#         print(f"Runs/Match: {rpm:.2f}")
#         print(f"Performance: {classify_player(rpm)}")

#     # Best and lowest performers
#     best = best_batsman(players)
#     lowest = lowest_player(players)

#     print("\n" + "=" * 55)
#     print(f"Best Performing Batsman : {best}")
#     print(f"Lowest Performing Player: {lowest}")

#     # Team average
#     print(f"Team Average Runs       : {team_average_runs(players):.2f}")

#     # Statistics module
#     print(f"Average Runs/Match      : {statistics.mean(performance):.2f}")
#     print(f"Median Runs/Match       : {statistics.median(performance):.2f}")
#     print("=" * 55)


# # Run the program
# if __name__ == "__main__":
#     main()














# import matplotlib.pyplot as plt

# # -----------------------------
# # Network Traffic Data
# # -----------------------------
# network_traffic = {
#     "HTTP": 1200,
#     "HTTPS": 3500,
#     "FTP": 650,
#     "SSH": 900,
#     "DNS": 1800,
#     "SMTP": 1100
# }

# # -----------------------------
# # Function to calculate total packets
# # -----------------------------
# def total_packets(data):
#     return sum(data.values())

# # -----------------------------
# # Function to find the most-used protocol
# # -----------------------------
# def most_used_protocol(data):
#     protocol = max(data, key=data.get)
#     return protocol, data[protocol]

# # -----------------------------
# # Function to find protocols having
# # more than 1000 packets
# # -----------------------------
# def protocols_above_1000(data):
#     return {protocol: packets
#             for protocol, packets in data.items()
#             if packets > 1000}

# # -----------------------------
# # Display Results
# # -----------------------------
# print("Network Traffic Data")
# print("-----------------------------")
# for protocol, packets in network_traffic.items():
#     print(f"{protocol}: {packets} packets")

# print("\nTotal Packets:", total_packets(network_traffic))

# protocol, packets = most_used_protocol(network_traffic)
# print(f"Most Used Protocol: {protocol} ({packets} packets)")

# print("\nProtocols having more than 1000 packets:")
# for protocol, packets in protocols_above_1000(network_traffic).items():
#     print(f"{protocol}: {packets}")

# # -----------------------------
# # Bar Chart
# # -----------------------------
# plt.figure(figsize=(8,5))
# plt.bar(network_traffic.keys(), network_traffic.values())
# plt.title("Packets per Protocol")
# plt.xlabel("Protocol")
# plt.ylabel("Packet Count")
# plt.grid(axis='y')
# plt.show()

# # -----------------------------
# # Pie Chart
# # -----------------------------
# plt.figure(figsize=(7,7))
# plt.pie(
#     network_traffic.values(),
#     labels=network_traffic.keys(),
#     autopct='%1.1f%%',
#     startangle=90
# )
# plt.title("Protocol-wise Traffic Distribution")
# plt.show()




def count_attack_types(alerts):
    return Counter(alerts)


def most_common_attack(alerts):
    counts = count_attack_types(alerts)
    attack = max(counts, key=counts.get)
    return attack, counts[attack]


def least_common_attack(alerts):
    counts = count_attack_types(alerts)
    attack = min(counts, key=counts.get)
    return attack, counts[attack]


def risk_count(alerts):
    counts = count_attack_types(alerts)

    low = 0
    high = 0

    for value in counts.values():
        if value > 5:
            high += 1
        else:
            low += 1

    return {
        "Low Risk": low,
        "High Risk": high
    }













import security_functions
import matplotlib.pyplot as mp


# Display Attack Counts
counts = security_functions.count_attack_types(
    security_functions.security_alerts
)

print("Security Alert Counts\n")

for attack, count in counts.items():
    print(f"{attack}: {count}")


# Most Common Attack
attack, count = security_functions.most_common_attack(
    security_functions.security_alerts
)

print(f"\nMost Common Attack: {attack} ({count} alerts)")


# Least Common Attack
attack, count = security_functions.least_common_attack(
    security_functions.security_alerts
)

print(f"Least Common Attack: {attack} ({count} alerts)")


# Risk Count
risk = security_functions.risk_count(
    security_functions.security_alerts
)

print("\nRisk Count")
print(risk)


# Bar Chart
mp.figure(figsize=(8,5))

mp.bar(
    counts.keys(),
    counts.values()
)

mp.title("Attack Type vs Number of Alerts")
mp.xlabel("Attack Type")
mp.ylabel("Number of Alerts")

mp.show()


# Pie Chart
mp.figure(figsize=(6,6))

mp.pie(
    risk.values(),
    labels=risk.keys(),
   
)

mp.title("Low Risk vs High Risk Attack Types")

mp.show()