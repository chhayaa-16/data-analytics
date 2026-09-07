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

n = int(input("Enter number of messages: "))

for i in range(n):
    speaker = input("Enter speaker: ")
    message = input("Enter message: ")

    messages.append((speaker, message))


user_count = 0
bot_count = 0

for speaker, message in messages:
    if speaker.lower() == "user":
        user_count += 1
    elif speaker.lower() == "bot":
        bot_count += 1

print("User messages:", user_count)
print("Bot messages:", bot_count)



questions = []
repeated_questions = set()

for speaker, message in messages:
    if speaker.lower() == "user":
        if message in questions:
            repeated_questions.add(message)
        else:
            questions.append(message)

print("\nRepeated Questions:")

for question in repeated_questions:
    print(question)



longest_message = ""

for speaker, message in messages:
    if len(message) > len(longest_message):
        longest_message = message

print("\nLongest Message:")
print(longest_message)



statistics = {
    "Message Count": {
        "Total": len(messages),
        "User": user_count,
        "Bot": bot_count
    },
    "Questions": {
        "Total Questions": len(questions),
        "Repeated Questions": len(repeated_questions)
    },
    "Longest Message": {
        "Text": longest_message,
        "Length": len(longest_message)
    }
}

print("\nChat Statistics:")

for category, data in statistics.items():
    print("\n", category)

    for key, value in data.items():
        print(key, ":", value)






# 5.  Face Recognition Attendance Logic Task 1: Accept recognized face
#     names. Task 2: Remove duplicate attendance. Task 3: Count unknown
#     faces. Task 4: Generate attendance percentage. Task 5: Display
#     absent students.



students = []

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    students.append(name)


m = int(input("\nEnter number of recognized faces: "))

attendance = []

for i in range(m):
    name = input("Enter recognized face name: ")
    attendance.append(name)




unique_attendance = set(attendance)

print("\nAttendance:")
for name in unique_attendance:
    print(name)




unknown_faces = 0

for name in attendance:
    if name not in students:
        unknown_faces += 1

print("\nUnknown faces:", unknown_faces)




attendance_count = len(unique_attendance)
total_students = len(students)

if total_students > 0:
    attendance_percentage = (attendance_count / total_students) * 100
else:
    attendance_percentage = 0

print("Attendance Percentage:", attendance_percentage, "%")




absent_students = []

for name in students:
    if name not in unique_attendance:
        absent_students.append(name)


print("\nAbsent Students:")

for name in absent_students:
    print(name)




attendance_data = {
    "Students": {
        "Total": total_students,
        "Present": attendance_count,
        "Absent": len(absent_students)
    },
    "Attendance": {
        "Percentage": attendance_percentage,
        "Unknown Faces": unknown_faces
    }
}


print("\nAttendance Statistics:")

for category, data in attendance_data.items():
    print("\n", category)

    for key, value in data.items():
        print(key, ":", value)





# 6.  AI Recommendation Engine Task 1: Accept watched movies of User A
#     and B. Task 2: Find common movies. Task 3: Find unique
#     recommendations. Task 4: Calculate similarity percentage. Task 5:
#     Recommend top movies.

movies_a = []
movies_b = []

n = int(input("Enter number of movies watched by User A: "))

for i in range(n):
    movie = input("Enter movie for User A: ")
    movies_a.append(movie)


m = int(input("\nEnter number of movies watched by User B: "))

for i in range(m):
    movie = input("Enter movie for User B: ")
    movies_b.append(movie)




set_a = set(movies_a)
set_b = set(movies_b)

common_movies = set_a.intersection(set_b)

print("\nCommon Movies:")

for movie in common_movies:
    print(movie)



unique_movies = set_b - set_a

print("\nUnique Recommendations for User A:")

for movie in unique_movies:
    print(movie)




total_movies = set_a.union(set_b)

if len(total_movies) > 0:
    similarity_percentage = (len(common_movies) / len(total_movies)) * 100
else:
    similarity_percentage = 0

print("\nSimilarity Percentage:", similarity_percentage, "%")




movie_ratings = {}

for movie in unique_movies:
    rating = float(input("Enter rating for " + movie + ": "))
    movie_ratings[movie] = rating


top_movies = []

for movie, rating in movie_ratings.items():
    if rating >= 4:
        top_movies.append(movie)


print("\nTop Movie Recommendations:")

for movie in top_movies:
    print(movie)



recommendation_data = {
    "Users": {
        "User A Movies": len(set_a),
        "User B Movies": len(set_b)
    },
    "Movies": {
        "Common Movies": len(common_movies),
        "Unique Recommendations": len(unique_movies)
    },
    "Similarity": {
        "Percentage": similarity_percentage
    }
}


print("\nRecommendation Statistics:")

for category, data in recommendation_data.items():
    print("\n", category)

    for key, value in data.items():
        print(key, ":", value)



    #     7.  Fraud Transaction Detection Task 1: Accept transactions. Task 2:
    # Detect duplicates, high-value and repeated-account transactions.
    # Task 3: Assign risk score. Task 4: Display suspicious transactions.
    # Task 5: Generate fraud report.



  

transactions = []

n = int(input("Enter number of transactions: "))

for i in range(n):
    account = input("Enter account number: ")
    amount = float(input("Enter transaction amount: "))

    transaction = (account, amount)
    transactions.append(transaction)




duplicate_transactions = set()
high_value_transactions = set()
repeated_accounts = set()

accounts = []

for transaction in transactions:
    account, amount = transaction

    
    if account in accounts:
        repeated_accounts.add(account)
    else:
        accounts.append(account)

    
    if amount >= 50000:
        high_value_transactions.add(transaction)

        

for transaction in transactions:
    if transactions.count(transaction) > 1:
        duplicate_transactions.add(transaction)


print("\nDuplicate Transactions:")

for transaction in duplicate_transactions:
    print(transaction)


print("\nHigh-Value Transactions:")

for transaction in high_value_transactions:
    print(transaction)


print("\nRepeated Accounts:")

for account in repeated_accounts:
    print(account)




risk_scores = {}

for transaction in transactions:
    account, amount = transaction
    score = 0

    if transaction in duplicate_transactions:
        score += 40

    if transaction in high_value_transactions:
        score += 40

    if account in repeated_accounts:
        score += 20

    risk_scores[transaction] = score




suspicious_transactions = []

for transaction, score in risk_scores.items():
    if score >= 40:
        suspicious_transactions.append(transaction)


print("\nSuspicious Transactions:")

for transaction in suspicious_transactions:
    print(transaction, "Risk Score:", risk_scores[transaction])




fraud_report = {
    "Transactions": {
        "Total": len(transactions),
        "Suspicious": len(suspicious_transactions)
    },

    "Fraud Detection": {
        "Duplicate Transactions": len(duplicate_transactions),
        "High-Value Transactions": len(high_value_transactions),
        "Repeated Accounts": len(repeated_accounts)
    }
}


print("\nFraud Report:")

for category, data in fraud_report.items():
    print("\n", category)

    for key, value in data.items():
        print(key, ":", value)





# 8.  AI Email Spam Filter Task 1: Accept emails. Task 2: Count spam
#     keywords. Task 3: Calculate spam score. Task 4: Classify Spam/Safe.
#     Task 5: Generate report.




emails = []

n = int(input("Enter number of emails: "))

for i in range(n):
    sender = input("Enter sender email: ")
    subject = input("Enter email subject: ")
    message = input("Enter email message: ")

    email = (sender, subject, message)
    emails.append(email)




spam_keywords = {
    "free",
    "win",
    "winner",
    "offer",
    "prize",
    "urgent",
    "money"
}

spam_counts = {}

for email in emails:
    sender, subject, message = email

    text = (subject + " " + message).lower()
    count = 0

    for word in spam_keywords:
        if word in text:
            count += 1

    spam_counts[email] = count




spam_scores = {}

for email, count in spam_counts.items():

    score = count * 20

    spam_scores[email] = score




email_classification = {}

for email, score in spam_scores.items():

    if score >= 40:
        email_classification[email] = "Spam"
    else:
        email_classification[email] = "Safe"


print("\nEmail Classification:")

for email, classification in email_classification.items():
    print(email, ":", classification)




spam_emails = []
safe_emails = []

for email, classification in email_classification.items():

    if classification == "Spam":
        spam_emails.append(email)
    else:
        safe_emails.append(email)


spam_report = {
    "Emails": {
        "Total": len(emails),
        "Spam": len(spam_emails),
        "Safe": len(safe_emails)
    },

    "Spam Analysis": {
        "Spam Keywords": len(spam_keywords),
        "Spam Emails": len(spam_emails)
    }
}


print("\nSpam Filter Report:")

for category, data in spam_report.items():

    print("\n", category)

    for key, value in data.items():
        print(key, ":", value)





# 9.  Smart Hospital AI Queue Task 1: Accept patient details. Task 2:
#     Assign priority. Task 3: Group by priority. Task 4: Sort queue. Task
#     5: Generate emergency report.



patients = []

n = int(input("Enter number of patients: "))

for i in range(n):
    name = input("Enter patient name: ")
    age = int(input("Enter patient age: "))
    condition = input("Enter condition (Emergency/Serious/Normal): ")

    patient = (name, age, condition)
    patients.append(patient)




patient_priority = {}

for patient in patients:

    name, age, condition = patient

    if condition.lower() == "emergency":
        priority = 1
    elif condition.lower() == "serious":
        priority = 2
    else:
        priority = 3

    patient_priority[patient] = priority




priority_groups = {
    1: [],
    2: [],
    3: []
}

for patient, priority in patient_priority.items():
    priority_groups[priority].append(patient)


print("\nPatients Grouped By Priority:")

for priority, patient_list in priority_groups.items():

    print("\nPriority", priority)

    for patient in patient_list:
        print(patient)




sorted_queue = []

for priority in [1, 2, 3]:

    for patient in priority_groups[priority]:
        sorted_queue.append(patient)


print("\nSorted Hospital Queue:")

for patient in sorted_queue:
    print(patient)




emergency_patients = []

for patient in patients:

    name, age, condition = patient

    if condition.lower() == "emergency":
        emergency_patients.append(patient)


emergency_report = {
    "Patients": {
        "Total": len(patients),
        "Emergency": len(emergency_patients)
    },

    "Queue": {
        "Priority 1": len(priority_groups[1]),
        "Priority 2": len(priority_groups[2]),
        "Priority 3": len(priority_groups[3])
    }
}


print("\nEmergency Report:")

for category, data in emergency_report.items():

    print("\n", category)

    for key, value in data.items():
        print(key, ":", value)




    #     10. AI Shopping Recommendation Task 1: Accept purchase history. Task 2:
    # Find frequent products. Task 3: Recommend products. Task 4:
    # Calculate buying score. Task 5: Generate report.




purchase_history = []

n = int(input("Enter number of customers: "))

for i in range(n):

    customer = input("Enter customer name: ")
    products = []

    m = int(input("Enter number of products purchased: "))

    for j in range(m):
        product = input("Enter product: ")
        products.append(product)

    purchase = (customer, products)
    purchase_history.append(purchase)



product_count = {}

for purchase in purchase_history:

    customer, products = purchase

    for product in products:

        if product in product_count:
            product_count[product] += 1
        else:
            product_count[product] = 1


frequent_products = set()

for product, count in product_count.items():

    if count >= 2:
        frequent_products.add(product)


print("\nFrequent Products:")

for product in frequent_products:
    print(product)


recommendations = {}

for purchase in purchase_history:

    customer, products = purchase
    customer_recommendations = []

    for product in frequent_products:

        if product not in products:
            customer_recommendations.append(product)

    recommendations[customer] = customer_recommendations


print("\nProduct Recommendations:")

for customer, products in recommendations.items():

    print(customer, ":", products)


buying_scores = {}

for purchase in purchase_history:

    customer, products = purchase

    score = len(products) * 10

    buying_scores[customer] = score


print("\nBuying Scores:")

for customer, score in buying_scores.items():

    print(customer, ":", score)




shopping_report = {
    "Customers": {
        "Total Customers": len(purchase_history),
        "Frequent Products": len(frequent_products)
    },

    "Shopping Analysis": {
        "Total Products": len(product_count),
        "Total Recommendations": sum(
            len(products) for products in recommendations.values()
        )
    },

    "Buying Score": {
        "Highest Score": max(buying_scores.values()),
        "Lowest Score": min(buying_scores.values())
    }
}


print("\nShopping Recommendation Report:")

for category, data in shopping_report.items():

    print("\n", category)

    for key, value in data.items():

        print(key, ":", value)



# 11. AI Student Performance Predictor Task 1: Accept attendance,
#     assignments, test scores. Task 2: Calculate Performance Index. Task
#     3: Classify performance. Task 4: Predict final result. Task 5:
#     Generate report.



students = []

n = int(input("Enter number of students: "))

for i in range(n):

    name = input("Enter student name: ")
    attendance = float(input("Enter attendance percentage: "))
    assignments = float(input("Enter assignment percentage: "))
    test_score = float(input("Enter test score percentage: "))

    student = (name, attendance, assignments, test_score)
    students.append(student)




performance_index = {}

for student in students:

    name, attendance, assignments, test_score = student

    index = (attendance + assignments + test_score) / 3

    performance_index[name] = index


print("\nPerformance Index:")

for name, index in performance_index.items():

    print(name, ":", index)



performance_classification = {}

for name, index in performance_index.items():

    if index >= 75:
        classification = "Excellent"
    elif index >= 50:
        classification = "Good"
    else:
        classification = "Poor"

    performance_classification[name] = classification


print("\nPerformance Classification:")

for name, classification in performance_classification.items():

    print(name, ":", classification)




final_result = {}

for name, index in performance_index.items():

    if index >= 50:
        result = "Pass"
    else:
        result = "Fail"

    final_result[name] = result


print("\nPredicted Final Result:")

for name, result in final_result.items():

    print(name, ":", result)


performance_report = {
    "Students": {
        "Total Students": len(students),
        "Passed": 0,
        "Failed": 0
    },

    "Performance": {
        "Excellent": 0,
        "Good": 0,
        "Poor": 0
    }
}


for name, result in final_result.items():

    if result == "Pass":
        performance_report["Students"]["Passed"] += 1
    else:
        performance_report["Students"]["Failed"] += 1


for name, classification in performance_classification.items():

    if classification == "Excellent":
        performance_report["Performance"]["Excellent"] += 1

    elif classification == "Good":
        performance_report["Performance"]["Good"] += 1

    else:
        performance_report["Performance"]["Poor"] += 1


print("\nStudent Performance Report:")

for category, data in performance_report.items():

    print("\n", category)

    for key, value in data.items():

        print(key, ":", value)



# 12. Network Log Analyzer Task 1: Accept IP addresses. Task 2: Count
#     repeated IPs. Task 3: Detect suspicious logins. Task 4: Display top
#     attackers. Task 5: Generate security report.



logs = []

n = int(input("Enter number of network logs: "))

for i in range(n):

    ip = input("Enter IP address: ")
    username = input("Enter username: ")
    status = input("Enter login status (Success/Failed): ")

    log = (ip, username, status)
    logs.append(log)




ip_count = {}

for log in logs:

    ip, username, status = log

    if ip in ip_count:
        ip_count[ip] += 1
    else:
        ip_count[ip] = 1


repeated_ips = set()

for ip, count in ip_count.items():

    if count > 1:
        repeated_ips.add(ip)


print("\nRepeated IP Addresses:")

for ip in repeated_ips:
    print(ip, ":", ip_count[ip], "times")




suspicious_logins = []

for log in logs:

    ip, username, status = log

    if status.lower() == "failed":
        suspicious_logins.append(log)


print("\nSuspicious Logins:")

for log in suspicious_logins:
    print(log)




top_attackers = []

for ip, count in ip_count.items():

    if count >= 2:
        top_attackers.append((ip, count))


print("\nTop Attackers:")

for attacker in top_attackers:
    print(attacker)



security_report = {
    "Network Logs": {
        "Total Logs": len(logs),
        "Unique IPs": len(ip_count)
    },

    "Security Analysis": {
        "Repeated IPs": len(repeated_ips),
        "Suspicious Logins": len(suspicious_logins),
        "Top Attackers": len(top_attackers)
    }
}


print("\nSecurity Report:")

for category, data in security_report.items():

    print("\n", category)

    for key, value in data.items():

        print(key, ":", value)





# 13. Password Leak Detector Task 1: Accept passwords. Task 2: Detect weak
#     passwords. Task 3: Find duplicates. Task 4: Generate strength score.
#     Task 5: Display secure/insecure users.



users = []

n = int(input("Enter number of users: "))

for i in range(n):

    username = input("Enter username: ")
    password = input("Enter password: ")

    user = (username, password)
    users.append(user)




weak_passwords = set()

for user in users:

    username, password = user

    if len(password) < 8:
        weak_passwords.add(password)

    elif password == "password":
        weak_passwords.add(password)

    elif password == "12345678":
        weak_passwords.add(password)


print("\nWeak Passwords:")

for password in weak_passwords:
    print(password)




password_count = {}

for user in users:

    username, password = user

    if password in password_count:
        password_count[password] += 1
    else:
        password_count[password] = 1


duplicate_passwords = set()

for password, count in password_count.items():

    if count > 1:
        duplicate_passwords.add(password)


print("\nDuplicate Passwords:")

for password in duplicate_passwords:
    print(password)



password_scores = {}

for user in users:

    username, password = user

    score = 0

    if len(password) >= 8:
        score += 40

    if any(character.isupper() for character in password):
        score += 20

    if any(character.islower() for character in password):
        score += 20

    if any(character.isdigit() for character in password):
        score += 20

    password_scores[username] = score


print("\nPassword Strength Scores:")

for username, score in password_scores.items():

    print(username, ":", score)




secure_users = []
insecure_users = []

for username, score in password_scores.items():

    if score >= 60:
        secure_users.append(username)
    else:
        insecure_users.append(username)


print("\nSecure Users:")

for username in secure_users:
    print(username)


print("\nInsecure Users:")

for username in insecure_users:
    print(username)



password_report = {
    "Users": {
        "Total Users": len(users),
        "Secure Users": len(secure_users),
        "Insecure Users": len(insecure_users)
    },

    "Password Analysis": {
        "Weak Passwords": len(weak_passwords),
        "Duplicate Passwords": len(duplicate_passwords)
    }
}


print("\nPassword Security Report:")

for category, data in password_report.items():

    print("\n", category)

    for key, value in data.items():

        print(key, ":", value)


# 14. AI Voice Command Analyzer Task 1: Accept commands. Task 2: Normalize
#     commands. Task 3: Count frequency. Task 4: Detect unknown commands.
#     Task 5: Generate usage statistics.




commands = []

n = int(input("Enter number of voice commands: "))

for i in range(n):

    command = input("Enter voice command: ")

    command_record = (command, "Voice")
    commands.append(command_record)




normalized_commands = []

for command_record in commands:

    command, command_type = command_record

    command = command.lower()
    command = command.strip()

    normalized_commands.append(command)


print("\nNormalized Commands:")

for command in normalized_commands:
    print(command)




command_count = {}

for command in normalized_commands:

    if command in command_count:
        command_count[command] += 1
    else:
        command_count[command] = 1


print("\nCommand Frequency:")

for command, count in command_count.items():
    print(command, ":", count)




known_commands = {
    "open music",
    "play music",
    "stop music",
    "open camera",
    "call home",
    "send message"
}

unknown_commands = set()

for command in normalized_commands:

    if command not in known_commands:
        unknown_commands.add(command)


print("\nUnknown Commands:")

for command in unknown_commands:
    print(command)



usage_statistics = {
    "Commands": {
        "Total Commands": len(normalized_commands),
        "Unique Commands": len(command_count)
    },

    "Command Analysis": {
        "Known Commands": len(set(normalized_commands) - unknown_commands),
        "Unknown Commands": len(unknown_commands)
    }
}


print("\nVoice Command Usage Statistics:")

for category, data in usage_statistics.items():

    print("\n", category)

    for key, value in data.items():

        print(key, ":", value)




# 15. Mini AI Data Pipeline Task 1: Accept mixed customer dataset. Task 2:
#     Clean and validate data. Task 3: Extract AI features. Task 4:
#     Generate analytics. Task 5: Build AI-ready dataset and preprocessing
#     report.




customers = []

n = int(input("Enter number of customers: "))

for i in range(n):

    name = input("Enter customer name: ")
    age = input("Enter age: ")
    city = input("Enter city: ")
    purchases = input("Enter number of purchases: ")
    amount = input("Enter total purchase amount: ")

    customer = (name, age, city, purchases, amount)
    customers.append(customer)



clean_data = []
invalid_data = []

for customer in customers:

    name, age, city, purchases, amount = customer

    name = name.strip()
    city = city.strip()

    if age.isdigit() and purchases.isdigit():

        age = int(age)
        purchases = int(purchases)

        try:
            amount = float(amount)

            if age > 0 and purchases >= 0 and amount >= 0:
                clean_customer = (
                    name,
                    age,
                    city,
                    purchases,
                    amount
                )

                clean_data.append(clean_customer)

            else:
                invalid_data.append(customer)

        except ValueError:
            invalid_data.append(customer)

    else:
        invalid_data.append(customer)


print("\nClean Data:")

for customer in clean_data:
    print(customer)


print("\nInvalid Data:")

for customer in invalid_data:
    print(customer)




features = []

cities = set()

for customer in clean_data:

    name, age, city, purchases, amount = customer

    cities.add(city)

    if amount >= 50000:
        spending_level = "High"
    elif amount >= 20000:
        spending_level = "Medium"
    else:
        spending_level = "Low"

    feature = (
        name,
        age,
        purchases,
        amount,
        spending_level
    )

    features.append(feature)


print("\nAI Features:")

for feature in features:
    print(feature)




total_customers = len(clean_data)

total_purchases = 0
total_amount = 0

for customer in clean_data:

    name, age, city, purchases, amount = customer

    total_purchases += purchases
    total_amount += amount


if total_customers > 0:
    average_purchase = total_amount / total_customers
else:
    average_purchase = 0


analytics = {
    "Customers": {
        "Total Customers": total_customers,
        "Invalid Customers": len(invalid_data),
        "Cities": len(cities)
    },

    "Purchases": {
        "Total Purchases": total_purchases,
        "Total Amount": total_amount,
        "Average Amount": average_purchase
    }
}


print("\nAnalytics:")

for category, data in analytics.items():

    print("\n", category)

    for key, value in data.items():
        print(key, ":", value)




ai_ready_dataset = []

for feature in features:

    name, age, purchases, amount, spending_level = feature

    ai_record = {
        "Name": name,
        "Age": age,
        "Purchases": purchases,
        "Amount": amount,
        "Spending_Level": spending_level
    }

    ai_ready_dataset.append(ai_record)


preprocessing_report = {
    "Input Data": {
        "Total Records": len(customers),
        "Valid Records": len(clean_data),
        "Invalid Records": len(invalid_data)
    },

    "AI Ready Data": {
        "Features Created": len(ai_ready_dataset),
        "Unique Cities": len(cities)
    }
}


print("\nAI-Ready Dataset:")

for record in ai_ready_dataset:
    print(record)


print("\nPreprocessing Report:")

for category, data in preprocessing_report.items():

    print("\n", category)

    for key, value in data.items():
        print(key, ":", value)
