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


    try:
        age = int(age)

        if age <= 0 or age > 120:
            invalid_records += 1
            continue

    except ValueError:
        invalid_records += 1
        continue


    try:
        salary = float(salary)

        if salary < 0:
            invalid_records += 1
            continue

    except ValueError:
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
print("Duplicate records:", len(customers) - invalid_records - len(cleandata))


print("\nMissing Fields:")

for field, count in missing_count.items():
    print(field, ":", count)