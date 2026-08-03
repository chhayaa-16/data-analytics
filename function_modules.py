# PRACTICAL 1: CURRENT AFFAIRS DATA ANALYZER

# Create a Python program that analyzes current-affairs data using functions.

# Tasks:
# 1. Create a dictionary containing 10 current-affairs topics and their importance scores.
# 2. Create a function to display all topics and their scores.
# 3. Create a function to find the topic with the highest score.
# 4. Create a function to find the topic with the lowest score.
# 5. Create a function to calculate the average importance score.
# 6. Create a function to display topics having a score greater than 70.
# 7. Use the statistics module to calculate mean and median.
# 8. Create a main() function that calls all the functions and displays a complete report.

import statistics

current_affairs ={ 

"paper_leak" : 81,
"wanted_chil": 26,
"dowry_case":35,
"AI_jobs":48,
"securty":85,
"heavy_rain":68,
"climate":97,
"RObery":78,
"farmers":89,
"Health_issue":76,
}


def display ():
    for topic ,score in current_affairs.items():
      print(topic, ":" , score)


def high_score():

    for topic ,score in current_affairs.items():
        topic = max(score ,key=current_affairs.items)

        print(topic)

def lowest_score():
     for topic ,score in current_affairs.items():
         topic = min(score ,key=current_affairs.items)
    
         print(topic)
    

def average():      

    average = sum(current_affairs.values()) / len(current_affairs)
    print(average)


def greater():

 for topic, score in current_affairs.items():
         if score > 70:
             print(f"{topic:<25} : {score}")




def statistics():
    scores = list(current_affairs.values())
   
    print(f"Mean : {statistics.mean(scores):.2f}")
    print(f"Median : {statistics.median(scores)}")

      




# PRACTICAL 2: INDIAN STOCK MARKET ANALYZER

# Create a program to analyze sample stock-market data of companies such as TCS, Infosys, Reliance and HDFC.

# Tasks:
# 1. Create a dictionary containing company names and their stock prices.
# 2. Create a function to display all stock prices.
# 3. Create a function to find the company having the highest stock price.
# 4. Create a function to find the company having the lowest stock price.
# 5. Create a function to calculate the average stock price.
# 6. Create a function to classify stocks as High, Medium or Low based on price.
# 7. Use the statistics module to calculate mean and median.
# 8. Create a main() function to generate a complete stock-market summary.


# import statistics

# company = {
#      "TCS": 6543,
#      "Infosys": 4367,
#      "Reliance": 4576,
#      "HDFC": 2312
#  }



# def display_stock():
     
#      for name, price in company.items():
#          print(name ,":" , price)


# def high_stock():
#        company = max( price , key=company.items)
    
#        print(name ,":" , price)


 
# def low_stock():
#       company = min(price , key=company.get)
     
#       print(name, ":", price)



# def average_stock():
#     avg = sum(average.values()) / len(average)
#     print(avg)





# #-----3 question----




# # PRACTICAL 3: CRICKET PERFORMANCE ANALYZER

# # Create a program that analyzes cricket player performance.

# # Tasks:
# # 1. Store player names and their runs in a dictionary.
# # 2. Create a function to display player statistics.
# # 3. Create a function to find the highest run scorer.
# # 4. Create a function to find the lowest run scorer.
# # 5. Create a function to calculate average runs.
# # 6. Create a function to display players who scored above the average.
# # 7. Use the statistics module to calculate mean, median and standard deviation.
# # 8. Create a main() function to generate a complete player-performance report.


# import statistics

# performance = {

# " M.S.Dhoni" : 89,
# "sachin tendulkar" : 87,
# "virat kohli" : 78,
# "Shubhman Gill" : 67
# }






# def display():
     
#      for name, run in performance.items():
#          print(name ,":" , run)



# def high_score():
#     name = max( performance , key=performance.items)
#     print(name ,":" , performance)


# def lowest_score():
#     name = min(performance, key=performance.items)
#     print(name, ":", performance)

# def average():      

#     average = sum(performance.values()) / len(performance)
#     print(average)


    
# def above_average():
#  avg = sum(performance.values()) / len(performance)
#  for name, runs in performance.items():
#         if runs > avg:
#              print(name ,":", runs)



# def statistics():
#     scores = list(performance.values())
   
#     print(f"Mean : {statistics.mean(scores):.2f}")
#     print(f"Median : {statistics.median(scores)}")
#     print(f"Standard Deviation : {statistics.stdev(scores):.2f}")




# PRACTICAL 4: IPL PLAYER PERFORMANCE ANALYZER

# Create a program to analyze IPL player performance using sample data.

# Tasks:
# 1. Store player names, runs and number of matches using nested dictionaries.
# 2. Create a function to calculate runs per match.
# 3. Create a function to find the best-performing batsman.
# 4. Create a function to find the lowest-performing player.
# 5. Create a function to calculate the team's average runs.
# 6. Create a function to classify players as Excellent, Good, Average or Poor.
# 7. Use the statistics module to calculate average and median performance.
# 8. Create a main() function to display the complete performance report.



import statistics


def runs_per_match(player):
    return player["runs"] / player["matches"]


def batsman(data):
    return max(data, key=lambda x: runs_per_match(data[x]))


def lowest_player(data):
    return min(data, key=lambda x: runs_per_match(data[x]))

def average_runs(data):
    total_runs = sum(player["runs"] for player in data.values())
    return total_runs / len(data)


def classify_player(rpm):
    if rpm >= 50:
        print("Excellent")
    elif rpm >= 40:
        print ("Good")
    elif rpm >= 30:
       print ("Average")
    else:
        print ("Poor") 


def performance_statistics(data):
    performances = [runs_per_match(player) for player in data.values()]
    return statistics.mean(performances), statistics.median(performances)






# PRACTICAL 5: GOLD PRICE ANALYZER

# Create a program that analyzes sample gold prices for 15 days.

# Tasks:
# 1. Create a list containing gold prices for 15 days.
# 2. Create a function to calculate the average gold price.
# 3. Create a function to find the maximum gold price.
# 4. Create a function to find the minimum gold price.
# 5. Create a function to calculate the price change between consecutive days.
# 6. Create a function to find the day with the highest price increase.
# 7. Use the statistics module to calculate mean, median and standard deviation.
# 8. Create a main() function to generate a gold-market analysis.




import statistics


def average_price(prices):
    return sum(prices) / len(prices)


def maximum_price(prices):
    return max(prices)


def minimum_price(prices):
    return min(prices)


def price_changes(prices):
    changes = []
    for i in range(1, len(prices)):
        changes.append(prices[i] - prices[i - 1])
    return changes


def highest_increase_day(prices):
    changes = price_changes(prices)
    max_change = max(changes)
    day = changes.index(max_change) + 2
    return day, max_change


def price_statistics(prices):
    mean = statistics.mean(prices)
    median = statistics.median(prices)
    std = statistics.stdev(prices)
    return mean, median, std








# PRACTICAL 6: WEATHER DATA ANALYZER

# Create a program to analyze sample temperature data for different Indian cities.

# Tasks:
# 1. Create a dictionary containing cities and their temperature values.
# 2. Create a function to calculate the average temperature of each city.
# 3. Create a function to identify the hottest city.
# 4. Create a function to identify the coldest city.
# 5. Create a function to find the maximum and minimum temperature.
# 6. Create a function to classify weather as Hot, Moderate or Cold.
# 7. Use the statistics module to calculate mean and median.
# 8. Create a main() function to generate a complete weather report



import statistics


def average_temperature(temp):
    return sum(temp) / len(temp)


def hottest_city(data):
    highest = 0
    city = ""

    for c in data:
        avg = average_temperature(data[c])
        if avg > highest:
            highest = avg
            city = c

    return city


def coldest_city(data):
    city_list = list(data.keys())
    lowest = average_temperature(data[city_list[0]])
    city = city_list[0]

    for c in data:
        avg = average_temperature(data[c])
        if avg < lowest:
            lowest = avg
            city = c

    return city


def maximum_temperature(data):
    maximum = data[list(data.keys())[0]][0]

    for city in data:
        for temp in data[city]:
            if temp > maximum:
                maximum = temp

    return maximum


def minimum_temperature(data):
    minimum = data[list(data.keys())[0]][0]

    for city in data:
        for temp in data[city]:
            if temp < minimum:
                minimum = temp

    return minimum


def classify_weather(avg):
    if avg >= 35:
        return "Hot"
    elif avg >= 25:
        return "Moderate"
    else:
        return "Cold"


def temperature_statistics(data):
    temp_list = []

    for city in data:
        for temp in data[city]:
            temp_list.append(temp)

    mean = statistics.mean(temp_list)
    median = statistics.median(temp_list)

    return mean, median




# PRACTICAL 7: ELECTION SURVEY DATA ANALYZER

# Create a program to analyze fictional election-survey data.

# Use fictional data only. Do not make predictions about real elections.

# Tasks:
# 1. Create a dictionary containing candidate names and survey votes.
# 2. Create a function to calculate the total number of votes.
# 3. Create a function to calculate the vote percentage of each candidate.
# 4. Create a function to find the candidate with the highest votes.
# 5. Create a function to find the candidate with the lowest votes.
# 6. Create a function to rank candidates according to votes.
# 7. Use the statistics module to calculate average votes.
# 8. Create a main() function to generate a complete election-survey report.


