# Advanced Python Collections + AI-Oriented Practice (15 Questions)

# Rules - Accept all input from the user. - Use List, Tuple, Set,
# Dictionary, Nested Dictionary. - Do not use pandas, NumPy, or AI
# libraries. - Use only core Python. - Complete all 5 tasks.

# 1.  AI Dataset Cleaning System Task 1: Accept N customer records (Name,
#     Age, City, Salary). Task 2: Remove duplicates, empty values, invalid
#     ages, negative salaries. Task 3: Find missing fields and count them.
#     Task 4: Generate cleaned dataset. Task 5: Print preprocessing
#     report.



n = int(input("Enter number of customers: "))

customers = []

for i in range(n):

    print("\nCustomer", i + 1)

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    city = input("Enter City: ")
    salary = input("Enter Salary: ")

    record = (name, age, city, salary)

    customers.append(record)


cleandata = []

unique_records = set()

missing_count = {
    "Name": 0,
    "Age": 0,
    "City": 0,
    "Salary": 0
}

invalid_records = 0

for record in customers:

    name, age, city, salary = record

    if name == "":
        missing_count["Name"] += 1



    if age == "":
        missing_count["Age"] += 1



    if city == "":
        missing_count["City"] += 1

    if salary == "":
        missing_count["Salary"] += 1


    if name == "" or age == "" or city == "" or salary == "":

        invalid_records += 1

        continue


    age = int(age)

    if age <= 0 or age > 120:

        invalid_records += 1

        continue

    salary = float(salary)

    if salary < 0:

        invalid_records += 1

        continue

    cleaned_record = (name, age, city, salary)


    if cleaned_record not in unique_records:

        unique_records.add(cleaned_record)

        cleandata.append(cleaned_record)



dataset = {

    "customers": {

        i + 1: {

            "Name": record[0],
            "Age": record[1],
            "City": record[2],
            "Salary": record[3]

        }

        for i, record in enumerate(cleandata)

    }

}



print("\n=== CLEANED DATASET ==========")

for customer_id, customer in dataset["customers"].items():

    print(customer_id, customer)




print("\n=== PREPROCESSING REPORT ==========")

print("Original records :", len(customers))

print("Cleaned records  :", len(cleandata))

print("Removed records  :", invalid_records)

print(
    "Duplicate records:",
    len(customers) - invalid_records - len(cleandata)
)



print("\nMissing Fields:")

for field, count in missing_count.items():

    print(field, ":", count)





# 2.  Fake News Detection Preprocessing Task 1: Accept multiple news
#     headlines. Task 2: Convert to lowercase and remove punctuation. Task
#     3: Remove duplicate words using sets. Task 4: Count frequency of
#     every word. Task 5: Display Top 10 frequent words.


n = int(input("Enter number of news headlines: "))

headlines = []

for i in range(n):

    print("\nEnter News Headline", i + 1)

    news = input("Headline: ")

    headlines.append(news)




cleaned_headlines = []

for news in headlines:

    news = news.lower()

    news = news.replace(".", "")
    news = news.replace(",", "")
    news = news.replace("!", "")
    news = news.replace("?", "")
    news = news.replace(":", "")
    news = news.replace(";", "")
    news = news.replace("'", "")
    news = news.replace('"', "")
    news = news.replace("-", "")

    cleaned_headlines.append(news)



all_words = []

for news in cleaned_headlines:

    words = news.split()

    for word in words:

        all_words.append(word)


unique_words = set(all_words)





word_frequency = {}

for word in all_words:

    if word in word_frequency:

        word_frequency[word] += 1

    else:

        word_frequency[word] = 1



news_data = {
    "News": {
        "Original Headlines": headlines,
        "Cleaned Headlines": cleaned_headlines,
        "Unique Words": unique_words,
        "Word Frequency": word_frequency
    }
}




top_words = []

for word in word_frequency:

    top_words.append((word, word_frequency[word]))




for i in range(len(top_words)):

    for j in range(i + 1, len(top_words)):

        if top_words[i][1] < top_words[j][1]:

            temp = top_words[i]

            top_words[i] = top_words[j]

            top_words[j] = temp



print("TOP 10 FREQUENT WORDS")


limit = 10

if len(top_words) < 10:

    limit = len(top_words)


for i in range(limit):

    print(
        i + 1,
        top_words[i][0],
        ":",
        top_words[i][1]
    )



print("NEWS DATA")


print("Original Headlines:")

for news in news_data["News"]["Original Headlines"]:

    print(news)


print("\nCleaned Headlines:")

for news in news_data["News"]["Cleaned Headlines"]:

    print(news)


print("\nUnique Words:")

print(news_data["News"]["Unique Words"])


print("\nWord Frequency:")

print(news_data["News"]["Word Frequency"])





# 3.  Resume Keyword Matching System Task 1: Accept Job Skills. Task 2:
#     Accept Candidate Skills. Task 3: Calculate Matching Percentage. Task
#     4: Display Missing, Extra and Common Skills. Task 5: Recommend
#     Eligible or Not.



job_skills = input("Enter job skills : ")

candidate_skills = input("Enter candidate skills : ")

job_set =set(job_skills)


candidate_set = set(candidate_skills)

common_skills = job_set & candidate_set

matching_percentage = (len(common_skills) / len(job_set)) *100

missing_skills = job_set - candidate_set
extra_skills = candidate_set - job_set

result = {
    "job_skills": job_skills,
    "candidate_skills": candidate_skills,
    "common_skills": common_skills,
    "missing_skills": missing_skills,
    "extra_skills": extra_skills,
    "matching_percentage": matching_percentage,

    } 

if matching_percentage >=50:
    recommend = "Eligible"
else:
    recommend = "Not Eligible"


print("Job Skills:", result["job_skills"])
print("Candidate Skills:", result["candidate_skills"])
print("Common Skills:", result["common_skills"])
print("Missing Skills:", result["missing_skills"])
print("Extra Skills:", result["extra_skills"])
print("Matching Percentage:", result["matching_percentage"])



# 4.  AI Chat History Analyzer Task 1: Accept conversation messages. Task
#     2: Count User/Bot messages. Task 3: Find repeated questions. Task 4:
#     Find longest message. Task 5: Generate statistics.

messages = []

number_of_msg = int(input("Enter number of messages: "))
