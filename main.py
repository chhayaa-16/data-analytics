# import sales 

# data= [45,3,24,67,64,34,76]

# print("total : ",sales.total(data))

# print("average :",sales.average(data))
# print("Highest number :",sales.highest(data))
# print("Lowest number :",sales.lowest(data))
# print("logic :",sales.logic(data))
# print("assending order :",sales.assending(data))
# print("descending order :",sales.descending(data))




#----- assignment--on fuction module--------

# question 1

# print( "Display : ",function_modules.display(current_affairs))
# print("high_score :",function_modules.high_score(current_affairs))
# print("lowest_score :",function_modules.lowest_score(current_affairs))
# print("average :",function_modules.average(current_affairs))
# print("greater than 70--:",function_modules.greater(current_affairs))
# print("statics : ",function_modules.statistics(current_affairs))

# import function_modules         <------ -------# correct code 
# def main():
#     function_modules.display()
#     function_modules.high_score()
#     function_modules.lowest_score()
#     function_modules.average()
#     function_modules.greater()
#     function_modules.statistics()
# main()



#que -----3------

# import function_modules
# def main():
#     function_modules.display()
#     function_modules.high_score()
#     function_modules.lowest_score()
#     function_modules.average()
#     function_modules.above_average()
#     function_modules.statistics()
# main()    



####  q 4 ------------------


from function_modules import *


players = {
    "Virat Kohli": {"runs": 745, "matches": 21},
    "Rohit Sharma": {"runs": 434, "matches": 12},
    "Shubman Gill": {"runs": 298, "matches": 15},
    
}

def main():

    for name, run in players.items():
        rpm = runs_per_match(run)

        print(name)
        print(f"Runs   : {run['runs']}")
        print(f"Matches: {run['matches']}")
        print(f"Runs/Match : {rpm:.2f}")
        print(f"Category   : {classify_player(rpm)}")
        

    print(" batsman",(players))
    print("loweest player",lowest_player(players))
    print ("average run",average_runs(players))

    avg, median = performance_statistics(players)

    print(f"Average Runs/Match : {avg:.2f}")
    print(f"Median Runs/Match  : {median:.2f}")

    print("=" * 60)

if __name__ == "__main__":
    main()

#que....5......




from function_modules import *


gold_prices = [
    5900, 5925, 5910, 5940, 5965,
    5980, 6000, 5995, 6025, 6040,
    6035, 6060, 6085, 6100, 6125
]

def main():

   
    for i in range(len(gold_prices)):
        print(f"Day {i+1} : ₹{gold_prices[i]}")

    print("\nAverage Gold Price :", average_price(gold_prices))
    print("Maximum Gold Price :", maximum_price(gold_prices))
    print("Minimum Gold Price :", minimum_price(gold_prices))

    print("\nPrice Changes")
    changes = price_changes(gold_prices)

    for i in range(len(changes)):
        print(f"Day {i+1} -> Day {i+2} : {changes[i]}")

    day, increase = highest_increase_day(gold_prices)

    print("\nHighest Price Increase")
    print("Day :", day)
    print("Increase :", increase)

    mean, median, std = price_statistics(gold_prices)

    
    print("Mean :", round(mean, 2))
    print("Median :", median)
    print("Standard Deviation :", round(std, 2))

    print("=" * 60)

if __name__ == "__main__":
    main()




 ############## que 6 #######################


from function_modules import *

weather_data = {
    "Mumbai": [32, 33, 31, 34, 32],
    "Delhi": [39, 40, 38, 41, 39],
    "Pune": [28, 29, 27, 30, 28],
    
}

def main():

    for city in weather_data:
        avg = average_temperature(weather_data[city])

        print(city)
        print("Average Temperature :", round(avg, 2))
        print("Weather :", classify_weather(avg))

    print( hottest_city(weather_data))
    print( coldest_city(weather_data))

    print( maximum_temperature(weather_data))
    print( minimum_temperature(weather_data))

    mean, median = temperature_statistics(weather_data)

    print("Mean Temperature :", round(mean, 2))
    print("Median Temperature :", median)

if __name__ == "__main__":
    main()