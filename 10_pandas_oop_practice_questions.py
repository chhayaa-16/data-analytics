"""
=============================================================================
ASSIGNMENT: 25 OBJECT-ORIENTED PANDAS PRACTICE PROJECTS (STUDENT EDITION)
=============================================================================
Course: Python Masterclass - Data Analytics & Cyber Security
Module: Pandas (Data Manipulation, Analysis & Preprocessing)
Prerequisites: 10_pandas_complete_guide.py, Classes and Objects (OOP)

INSTRUCTIONS FOR STUDENTS:
-----------------------------------------------------------------------------
1. Do NOT write procedural script code. Every single problem MUST be implemented 
   as a Python Class using Object-Oriented Programming (OOP) principles.
2. The dataset must be passed to the constructor (__init__) and stored inside 
   instance attributes (e.g., self.df, self.data).
3. Implement easch task as an instance method inside the class.
4. Each problem contains 5 to 6 dedicated tasks covering:
   - Data Inspection & Summarization
   - Row/Column Indexing (.loc, .iloc) & Conditional Queries
   - Feature Engineering, Derived Columns & Column Operations
   - Missing Value Detection & Imputation
   - GroupBy & Multi-Metric Aggregations
   - Relational Joins, Merging & Concatenation
   - Categorical Encoding (One-Hot & Ordinal Mapping)
   - Feature Scaling (Min-Max Normalization & Z-Score Standardization)
   - Outlier Detection & IQR Clipping
   - Correlation Matrix & Multicollinearity
   - Discretization & Binning (pd.cut, pd.qcut)
   - Advanced .apply(), Lambda & DateTime Engineering
   - Reshaping & Multi-dimensional Pivot Tables
5. Write your solution code under each class definition by replacing 'pass'.
=============================================================================
"""

import pandas as pd
import numpy as np


# =============================================================================
# QUESTION 01: Employee Data Inspector (HR Analytics)
# Concepts: Series & DataFrame Creation, Data Inspection & Descriptive Stats
# =============================================================================
"""
Scenario:
You are hired by an IT firm's Human Resources department. You are provided with 
raw dictionary records of newly onboarded software engineers. You need to build 
an inspection utility class that ingests this data, validates its structure, 
and produces high-level summaries for the HR Director.

Class Name: EmployeeDataInspector
Constructor: __init__(self, data_dict)
  - Accepts a dictionary of employee data and converts it into self.df.

Tasks to Implement:
  1. def get_shape_and_dtypes(self)
     - Return a tuple containing: (number of rows, number of columns) and a Series 
       of column data types (dtypes).
  2. def preview_records(self, n=3, from_bottom=False)
     - If from_bottom is False, return the first n rows using .head(n).
     - If from_bottom is True, return the last n rows using .tail(n).
  3. def get_statistical_summary(self)
     - Return the numerical statistical summary using .describe().
  4. def extract_series_with_custom_index(self, value_column, index_column)
     - Extract value_column as a 1D Pandas Series, indexed by index_column.
     - Return the Series, along with the maximum value and the index label where 
       the maximum occurs (using .idxmax()).
  5. def audit_missing_values(self)
     - Check and return a Series containing the total count of null/NaN values 
       for every column in the dataset using .isna().sum().
"""

# class EmployeeDataInspector:
#     def __init__(self, data_dict):
#         self.df = pd.DataFrame(data_dict)
        

#     def get_shape_and_dtypes(self):
#         return self.df.shape, self.df.dtypes
        

#     def preview_records(self, n=3, from_bottom=False):
#         if from_bottom:
#             return self.df.tail(n)
#         return self.df.head(n)
        

#     def get_statistical_summary(self):
#         return self.df.describe()
        

#     def extract_series_with_custom_index(self, value_column, index_column):
#         series = pd.Series(
#             self.df[value_column].values,
#             index=self.df[index_column]
#         )
        
#         max_value = series.max()
#         max_index = series.idxmax()

#         return series, max_value, max_index

#     def audit_missing_values(self):
#         return self.df.isna().sum()








# employee_data = {
#     "Employee_ID": [101, 102, 103, 104, 105],
#     "Name": ["Rahul", "Priya", "Amit", "Sneha", "Vijay"],
#     "Age": [25, 30, 28, 35, 32],
#     "Salary": [40000, 55000, 48000, 70000, 60000]
# }

# employee = EmployeeDataInspector(employee_data)

# print(" Shape and Data Types ")
# print(employee.get_shape_and_dtypes())

# print(" First 3 Records ")
# print(employee.preview_records())

# print(" Last 2 Records ")
# print(employee.preview_records(2, from_bottom=True))

# print(" Statistical Summary ")
# print(employee.get_statistical_summary())

# print("Salary Series ")
# series, max_salary, max_salary_employee = employee.extract_series_with_custom_index(
#     "Salary",
#     "Name"
# )

# print(series)
# print("Maximum Salary:", max_salary)
# print("Employee:", max_salary_employee)

# print("Missing Value")
# print(employee.audit_missing_values())


# =============================================================================
# QUESTION 02: Hospital Patient Filter (Healthcare Records)
# Concepts: Selection (.loc vs .iloc), Boolean Indexing, Compound Queries
# =============================================================================
"""
Scenario:
A hospital management system stores patient admission details (Patient_ID, Name, 
Age, Department, Blood_Pressure, ICU_Admitted, Billing_Amount). The medical 
superintendent requires an object-oriented triage filter to locate and isolate 
high-risk emergency records.

Class Name: HospitalPatientFilter
Constructor: __init__(self, df_patients)
  - Ingests the patient DataFrame and assigns it to self.df.

Tasks to Implement:
  1. def select_by_position(self, row_start, row_end, col_indices)
     - Use .iloc to slice rows from row_start to row_end (exclusive/inclusive per 
       iloc standard) and specific column integer indices col_indices.
  2. def select_by_labels(self, row_labels, column_names)
     - Use .loc to extract specific rows and named columns.
  3. def filter_emergency_icu(self)
     - Return a DataFrame of patients who are marked as ICU_Admitted == True.
  4. def filter_high_risk_seniors(self, age_threshold=60, billing_threshold=50000)
     - Apply compound boolean condition (& operator) to retrieve all patients 
       where Age >= age_threshold AND Billing_Amount > billing_threshold.
  5. def filter_by_departments(self, dept_list)
     - Return patients admitted to any department present in dept_list using .isin().
  6. def query_critical_vitals(self, min_age, max_age)
     - Use Pandas .between() or boolean indexing to filter patients whose Age 
       falls within [min_age, max_age] and Blood_Pressure is categorized as 'High'.
"""

# class HospitalPatientFilter:
#     def __init__(self, df_patients):
#         self.df = df_patients

#     def select_by_position(self, row_start, row_end, col_indices):
#         return self.df.iloc[row_start:row_end, col_indices]

#     def select_by_labels(self, row_labels, column_names):
#          return self.df.loc[row_labels, column_names]

#     def filter_emergency_icu(self):
#         return self.df[self.df["ICU_Admitted"] == True]

#     def filter_high_risk_seniors(self, age_threshold=60, billing_threshold=50000):
#           return self.df[
#             (self.df["Age"] >= age_threshold) &
#             (self.df["Billing_Amount"] > billing_threshold)
#         ]

#     def filter_by_departments(self, dept_list):
#         return self.df[self.df["Department"].isin(dept_list)]

#     def query_critical_vitals(self, min_age, max_age):
#         return self.df[
#             self.df["Age"].between(min_age, max_age) &
#             (self.df["Blood_Pressure"] == "High")
#         ]






# # patient_data = {
# #     "Patient_ID": [101, 102, 103, 104, 105],
# #     "Name": ["Rahul", "Priya", "Amit", "Sneha", "Vijay"],
# #     "Age": [45, 65, 72, 55, 68],
# #     "Department": ["Cardiology", "Neurology", "Emergency", "Cardiology", "Emergency"],
# #     "Blood_Pressure": ["Normal", "High", "High", "Normal", "High"],
# #     "ICU_Admitted": [False, True, True, False, True],
# #     "Billing_Amount": [30000, 60000, 75000, 45000, 55000]
# # }

# # patients = pd.DataFrame(patient_data)

# # hospital = HospitalPatientFilter(patients)

# # print(" Select By Position ")
# # print(hospital.select_by_position(0, 3, [0, 1, 2]))

# # print("Select By Labels")
# # print(hospital.select_by_labels([0, 2], ["Patient_ID", "Name", "Department"]))

# # print(" Emergency ICU Patients ")
# # print(hospital.filter_emergency_icu())

# # print(" High Risk Seniors ")
# # print(hospital.filter_high_risk_seniors())

# # print("Selected Departments ")
# # print(hospital.filter_by_departments(["Emergency", "Cardiology"]))

# # print(" Critical Vitals ")
# # print(hospital.query_critical_vitals(60, 75))


# # =============================================================================
# # QUESTION 03: Payroll Compensation Engine (Corporate Finance)
# # Concepts: Column Creation, Math Operations, Renaming & Dropping Columns
# # =============================================================================
# """
# Scenario:
# An enterprise payroll division calculates monthly salary slips. They need a class 
# that takes raw salary data, adds statutory allowances and bonuses, renames legacy 
# column names into standard modern financial terms, and computes net payouts.

# Class Name: PayrollCompensationEngine
# Constructor: __init__(self, df_payroll)
#   - Stores a copy of df_payroll inside self.df.

# Tasks to Implement:
#   1. def add_allowances(self, hra_rate=0.20, da_rate=0.10)
#      - Create 'HRA' as hra_rate * Salary and 'DA' as da_rate * Salary.
#   2. def compute_performance_bonus(self, bonus_pct=0.08)
#      - Create 'Bonus' as Salary * bonus_pct for eligible employees (Experience_Yrs >= 2). 
#        Others receive 0 bonus.
#   3. def compute_total_compensation(self)
#      - Compute 'Gross_Salary' = Salary + HRA + DA + Bonus.
#      - Compute 'Tax_Deduction' = 12% of Gross_Salary.
#      - Compute 'Net_Salary' = Gross_Salary - Tax_Deduction.
#   4. def rename_legacy_columns(self, column_mapping)
#      - Rename columns using the provided dictionary column_mapping in place.
#   5. def drop_redundant_columns(self, columns_to_remove)
#      - Drop specified list of temporary or unneeded columns safely (checking 
#        if they exist in self.df).
#   6. def rank_by_net_salary(self)
#      - Add a 'Salary_Rank' column ranking employees by Net_Salary descending. 
#        Return the top 5 highest-paid employees.
# """

# class PayrollCompensationEngine:

#     def __init__(self, df_payroll):
#         self.df = df_payroll.copy()

#     def add_allowances(self, hra_rate=0.20, da_rate=0.10):
#         self.df["HRA"] = self.df["Salary"] * hra_rate
#         self.df["DA"] = self.df["Salary"] * da_rate
#         return self.df

#     def compute_performance_bonus(self, bonus_pct=0.08):
#         self.df["Bonus"] = np.where(
#             self.df["Experience_Yrs"] >= 2,
#             self.df["Salary"] * bonus_pct,
#             0
#         )
#         return self.df

#     def compute_total_compensation(self):
#         self.df["Gross_Salary"] = (
#             self.df["Salary"]
#             + self.df["HRA"]
#             + self.df["DA"]
#             + self.df["Bonus"]
#         )

#         self.df["Tax_Deduction"] = self.df["Gross_Salary"] * 0.12

#         self.df["Net_Salary"] = (
#             self.df["Gross_Salary"]
#             - self.df["Tax_Deduction"]
#         )

#         return self.df

#     def rename_legacy_columns(self, column_mapping):
#         self.df.rename(columns=column_mapping, inplace=True)
#         return self.df

#     def drop_redundant_columns(self, columns_to_remove):
#         existing_columns = [
#             col for col in columns_to_remove
#             if col in self.df.columns
#         ]

#         self.df.drop(columns=existing_columns, inplace=True)

#         return self.df

#     def rank_by_net_salary(self):
#         self.df["Salary_Rank"] = (
#             self.df["Net_Salary"]
#             .rank(method="dense", ascending=False)
#         )

#         return self.df.sort_values("Salary_Rank").head(5)








# payroll_data = {
#     "Emp_ID": [101, 102, 103, 104, 105, 106],
#     "Employee_Name": ["Rahul", "Priya", "Amit", "Sneha", "Vijay", "Neha"],
#     "Salary": [40000, 55000, 48000, 70000, 60000, 45000],
#     "Experience_Yrs": [1, 3, 5, 2, 7, 1],
#     "Legacy_Dept": [
#         "IT", "HR", "Finance", "IT", "Sales", "HR"
#     ]
# }

# payroll_df = pd.DataFrame(payroll_data)

# payroll = PayrollCompensationEngine(payroll_df)

# print("Add Allowances ")
# print(payroll.add_allowances())

# print( "Performance Bonus ")
# print(payroll.compute_performance_bonus())

# print("Total Compensation ")
# print(payroll.compute_total_compensation())

# print("Rename Legacy Columns")
# print(
#     payroll.rename_legacy_columns(
#         {"Legacy_Dept": "Department"}
#     )
# )

# print("Drop Redundant Columns")
# print(
#     payroll.drop_redundant_columns(
#         ["Department"]
#     )
# )

# print("Top 5 By Net Salary ")
# print(payroll.rank_by_net_salary())


# =============================================================================
# QUESTION 04: Data Hygiene Cleaner (Data Quality Assurance)
# Concepts: Missing Data Detection, dropna Strategies, Imputation (Mean/Median/Mode)
# =============================================================================
"""
Scenario:
Raw telemetry data from IoT weather sensors contains incomplete records with 
missing temperatures, humidity levels, and station IDs. Build a data hygiene 
class that audits, drops unusable rows, and imputes missing values using 
appropriate central tendency metrics.

Class Name: DataHygieneCleaner
Constructor: __init__(self, df_telemetry)
  - Stores a deep copy of df_telemetry in self.df.

Tasks to Implement:
  1. def inspect_null_summary(self)
     - Return a DataFrame reporting for each column: Total Missing Count (.isna().sum()) 
       and Percentage of Total Records that are missing.
  2. def drop_incomplete_identifiers(self, id_columns)
     - Drop rows where any of the critical id_columns have NaN values using .dropna(subset=...).
  3. def impute_numerical_median(self, numeric_columns)
     - For each column in numeric_columns, fill missing values with the column's 
       median value.
  4. def impute_numerical_mean(self, target_column, round_decimals=2)
     - Impute target_column with its mean rounded to round_decimals.
  5. def impute_categorical_mode(self, categorical_columns)
     - For each categorical column, impute missing values with the most frequent 
       value (mode()[0]).
  6. def forward_backward_fill_timeseries(self, timestamp_column)
     - Sort by timestamp_column and use .ffill() followed by .bfill() to handle 
       consecutive sensor dropouts.
"""

# class DataHygieneCleaner:

#     def __init__(self, df_telemetry):
#         self.df = df_telemetry.copy(deep=True)

#     def inspect_null_summary(self):
#         missing_count = self.df.isna().sum()
#         missing_percentage = (missing_count / len(self.df)) * 100

#         return pd.DataFrame({
#             "Total_Missing": missing_count,
#             "Missing_Percentage": missing_percentage
#         })

#     def drop_incomplete_identifiers(self, id_columns):
#         self.df.dropna(subset=id_columns, inplace=True)
#         return self.df

#     def impute_numerical_median(self, numeric_columns):
#         for column in numeric_columns:
#             self.df[column] = self.df[column].fillna(
#                 self.df[column].median()
#             )

#         return self.df

#     def impute_numerical_mean(self, target_column, round_decimals=2):
#         mean_value = round(
#             self.df[target_column].mean(),
#             round_decimals
#         )

#         self.df[target_column] = self.df[target_column].fillna(
#             mean_value
#         )

#         return self.df

#     def impute_categorical_mode(self, categorical_columns):
#         for column in categorical_columns:
#             mode_value = self.df[column].mode()[0]

#             self.df[column] = self.df[column].fillna(
#                 mode_value
#             )

#         return self.df

#     def forward_backward_fill_timeseries(self, timestamp_column):
#         self.df = self.df.sort_values(timestamp_column)

#         self.df = self.df.ffill().bfill()

#         return self.df








# telemetry_data = {
#     "Station_ID": ["S01", "S02", None, "S04", "S05", "S06"],
#     "Timestamp": [
#         "2026-01-03 10:00",
#         "2026-01-01 10:00",
#         "2026-01-02 10:00",
#         "2026-01-04 10:00",
#         "2026-01-05 10:00",
#         "2026-01-06 10:00"
#     ],
#     "Temperature": [25.5, None, 27.0, 26.5, None, 28.0],
#     "Humidity": [60.0, 65.0, None, 70.0, 68.0, None],
#     "Status": ["Normal", "Normal", None, "Warning", "Normal", "Normal"]
# }

# telemetry_df = pd.DataFrame(telemetry_data)

# cleaner = DataHygieneCleaner(telemetry_df)

# print("Null Summary ")
# print(cleaner.inspect_null_summary())

# print(" Drop Incomplete Identifiers ")
# print(
#     cleaner.drop_incomplete_identifiers(["Station_ID"])
# )

# print(" Median Imputation ")
# print(
#     cleaner.impute_numerical_median(
#         ["Temperature", "Humidity"]
#     )
# )

# print(" Mean Imputation ")
# print(
#     cleaner.impute_numerical_mean("Temperature")
# )

# print(" Mode Imputation ")
# print(
#     cleaner.impute_categorical_mode(["Status"])
# )

# print(" Forward Backward Fill ")
# print(
#     cleaner.forward_backward_fill_timeseries("Timestamp")
# )

# =============================================================================
# QUESTION 05: Retail Sales Aggregator (E-Commerce Analytics)
# Concepts: GroupBy, Multi-Metric Named Aggregations, Group Filtering
# =============================================================================
"""
Scenario:
An online retail platform logs sales across multiple store branches, product 
categories, and dates. Build an aggregation engine that groups records and 
computes executive metrics (mean, sum, min, max, count) to assess regional branch health.

Class Name: RetailSalesAggregator
Constructor: __init__(self, df_sales)
  - Stores the sales records DataFrame in self.df.

Tasks to Implement:
  1. def get_category_revenue(self)
     - Group by 'Category' and return the total sum of 'Sales_Amount' sorted descending.
  2. def multi_metric_dept_summary(self)
     - Group by 'Department' and use .agg() with named aggregations:
       * Total_Orders: ('Order_ID', 'count')
       * Total_Revenue: ('Sales_Amount', 'sum')
       * Avg_Order_Value: ('Sales_Amount', 'mean')
       * Max_Sale: ('Sales_Amount', 'max')
       Round monetary values to 2 decimal places.
  3. def multi_level_grouping(self, primary_col='Region', secondary_col='Category')
     - Group by [primary_col, secondary_col] and compute the mean of 'Profit' and 
       sum of 'Quantity'.
  4. def filter_high_volume_categories(self, min_order_count=50)
     - Use .filter() on groupby('Category') to retain only rows belonging to 
       categories with more than min_order_count orders.
  5. def compute_category_share_percentage(self)
     - For each category, compute its percentage contribution to total overall sales 
       revenue.
# """

# class RetailSalesAggregator:

#     def __init__(self, df_sales):
#         self.df = df_sales.copy()

#     def get_category_revenue(self):
#         return (
#             self.df.groupby("Category")["Sales_Amount"]
#             .sum()
#             .sort_values(ascending=False)
#         )

#     def multi_metric_dept_summary(self):
#         summary = (
#             self.df.groupby("Department")
#             .agg(
#                 Total_Orders=("Order_ID", "count"),
#                 Total_Revenue=("Sales_Amount", "sum"),
#                 Avg_Order_Value=("Sales_Amount", "mean"),
#                 Max_Sale=("Sales_Amount", "max")
#             )
#         )

#         summary[
#             ["Total_Revenue", "Avg_Order_Value", "Max_Sale"]
#         ] = summary[
#             ["Total_Revenue", "Avg_Order_Value", "Max_Sale"]
#         ].round(2)

#         return summary

#     def multi_level_grouping(
#         self,
#         primary_col="Region",
#         secondary_col="Category"
#     ):
#         return (
#             self.df.groupby(
#                 [primary_col, secondary_col]
#             )
#             .agg(
#                 Average_Profit=("Profit", "mean"),
#                 Total_Quantity=("Quantity", "sum")
#             )
#         )

#     def filter_high_volume_categories(self, min_order_count=50):
#         return self.df.groupby("Category").filter(
#             lambda group: len(group) > min_order_count
#         )

#     def compute_category_share_percentage(self):
#         category_revenue = (
#             self.df.groupby("Category")["Sales_Amount"]
#             .sum()
#         )

#         total_revenue = self.df["Sales_Amount"].sum()

#         share_percentage = (
#             category_revenue / total_revenue
#         ) * 100

#         return share_percentage.round(2)








# sales_data = {
#     "Order_ID": [1, 2, 3, 4, 5, 6, 7, 8],
#     "Category": [
#         "Electronics",
#         "Furniture",
#         "Electronics",
#         "Clothing",
#         "Furniture",
#         "Electronics",
#         "Clothing",
#         "Furniture"
#     ],
#     "Department": [
#         "Tech",
#         "Home",
#         "Tech",
#         "Fashion",
#         "Home",
#         "Tech",
#         "Fashion",
#         "Home"
#     ],
#     "Region": [
#         "North",
#         "South",
#         "North",
#         "West",
#         "South",
#         "East",
#         "West",
#         "East"
#     ],
#     "Sales_Amount": [
#         50000,
#         30000,
#         45000,
#         20000,
#         35000,
#         60000,
#         25000,
#         40000
#     ],
#     "Profit": [
#         10000,
#         6000,
#         9000,
#         5000,
#         7000,
#         12000,
#         5500,
#         8000
#     ],
#     "Quantity": [
#         5,
#         3,
#         4,
#         2,
#         4,
#         6,
#         3,
#         5
#     ]
# }

# sales_df = pd.DataFrame(sales_data)

# sales = RetailSalesAggregator(sales_df)

# print(" Category Revenue ")
# print(sales.get_category_revenue())

# print(" Department Summary ")
# print(sales.multi_metric_dept_summary())

# print(" Region + Category Grouping ")
# print(sales.multi_level_grouping())

# print(" High Volume Categories ")
# print(sales.filter_high_volume_categories(min_order_count=2))

# print(" Category Share Percentage ")
# print(sales.compute_category_share_percentage())

    

# # =============================================================================
# # QUESTION 06: Enterprise Project Merger (Corporate ERP)
# # Concepts: Merging (Inner, Left, Right, Outer) & Concatenation (pd.concat)
# # =============================================================================
# """
# Scenario:
# A multinational corporation maintains employee profiles, department listings, 
# and assigned IT projects across separate databases. Create an object-oriented 
# relational data integrator to join and consolidate these tables.

# Class Name: EnterpriseProjectMerger
# Constructor: __init__(self, df_employees, df_projects)
#   - Ingests df_employees and df_projects.

# Tasks to Implement:
#   1. def merge_assigned_staff_only(self, join_key='Emp_ID')
#      - Perform an INNER join between employees and projects to display only 
#        employees currently allocated to an active project.
#   2. def merge_all_employees(self, join_key='Emp_ID')
#      - Perform a LEFT join retaining all employees, displaying NaN for staff 
#        without an assigned project.
#   3. def audit_unassigned_projects(self, join_key='Emp_ID')
#      - Perform an OUTER join to identify projects with no employee assigned, 
#        and employees with no project assigned.
#   4. def vertical_concatenate_contractors(self, df_contractors)
#      - Concatenate df_contractors vertically below df_employees using pd.concat() 
#        with ignore_index=True.
#   5. def horizontal_concatenate_metrics(self, df_kpis)
#      - Concatenate df_kpis horizontally (axis=1) side-by-side with self.df_employees.
#   6. def handle_overlapping_columns(self, df_secondary, join_key, suffixes=('_core', '_ext'))
#      - Merge tables that share identical column names, applying distinct suffixes.
# """
# class EnterpriseProjectMerger:

#     def __init__(self, df_employees, df_projects):
#         self.df_employees = df_employees.copy()
#         self.df_projects = df_projects.copy()

#     def merge_assigned_staff_only(self, join_key='Emp_ID'):
#         return pd.merge(
#             self.df_employees,
#             self.df_projects,
#             on=join_key,
#             how='inner'
#         )

#     def merge_all_employees(self, join_key='Emp_ID'):
#         return pd.merge(
#             self.df_employees,
#             self.df_projects,
#             on=join_key,
#             how='left'
#         )

#     def audit_unassigned_projects(self, join_key='Emp_ID'):
#         return pd.merge(
#             self.df_employees,
#             self.df_projects,
#             on=join_key,
#             how='outer',
#             indicator=True
#         )

#     def vertical_concatenate_contractors(self, df_contractors):
#         return pd.concat(
#             [self.df_employees, df_contractors],
#             ignore_index=True
#         )

#     def horizontal_concatenate_metrics(self, df_kpis):
#         return pd.concat(
#             [self.df_employees, df_kpis],
#             axis=1
#         )

#     def handle_overlapping_columns(
#         self,
#         df_secondary,
#         join_key,
#         suffixes=('_core', '_ext')
#     ):
#         return pd.merge(
#             self.df_employees,
#             df_secondary,
#             on=join_key,
#             how='inner',
#             suffixes=suffixes
#         )
    






# employee_data = {
#     "Emp_ID": [101, 102, 103, 104],
#     "Name": ["Rahul", "Priya", "Amit", "Sneha"],
#     "Department": ["IT", "HR", "Finance", "Sales"]
# }

# project_data = {
#     "Emp_ID": [101, 103, 105],
#     "Project": ["ERP Migration", "Data Warehouse", "Cyber Security"],
#     "Status": ["Active", "Active", "Active"]
# }

# employees_df = pd.DataFrame(employee_data)
# projects_df = pd.DataFrame(project_data)

# merger = EnterpriseProjectMerger(
#     employees_df,
#     projects_df
# )








# print("\n--- Inner Join: Assigned Staff Only ---")
# print(merger.merge_assigned_staff_only())

# print("\n--- Left Join: All Employees ---")
# print(merger.merge_all_employees())

# print("\n--- Outer Join: Audit Unassigned ---")
# print(merger.audit_unassigned_projects())

# contractor_data = {
#     "Emp_ID": [106, 107],
#     "Name": ["Vijay", "Neha"],
#     "Department": ["IT", "HR"]
# }

# contractors_df = pd.DataFrame(contractor_data)

# print("\n--- Vertical Concatenation ---")
# print(merger.vertical_concatenate_contractors(contractors_df))

# kpi_data = {
#     "Performance_Score": [85, 90, 78, 88],
#     "Projects_Completed": [3, 4, 2, 5]
# }

# kpis_df = pd.DataFrame(kpi_data)

# print("\n--- Horizontal Concatenation ---")
# print(merger.horizontal_concatenate_metrics(kpis_df))

# secondary_data = {
#     "Emp_ID": [101, 102, 103, 104],
#     "Name": ["R. Patil", "P. Sharma", "A. Kumar", "S. Joshi"],
#     "Salary": [50000, 55000, 60000, 65000]
# }

# secondary_df = pd.DataFrame(secondary_data)

# print(" Overlapping Columns ")
# print(
#     merger.handle_overlapping_columns(
#         secondary_df,
#         "Emp_ID"
#     )
# )






# =============================================================================
# QUESTION 07: Customer Feature Encoder (ML Feature Engineering)
# Concepts: Categorical Encoding (pd.get_dummies) & Ordinal Mapping
# =============================================================================
"""
Scenario:
Machine learning models cannot directly process text strings such as customer 
subscription tiers or geographical regions. Create a feature encoding class 
to convert nominal and ordinal categorical attributes into numeric representations.

Class Name: CustomerFeatureEncoder
Constructor: __init__(self, df_customers)
  - Stores a copy of df_customers in self.df.

Tasks to Implement:
  1. def one_hot_encode_nominal(self, columns_to_encode, prefix_tags=None)
     - Apply pd.get_dummies(..., drop_first=True, dtype=int) on the specified columns 
       to prevent the Dummy Variable Trap.
#   2. def ordinal_encode_tier(self, tier_column, hierarchy_dict)
#      - Map ordered categories (e.g., {'Bronze': 1, 'Silver': 2, 'Gold': 3, 'Platinum': 4}) 
#        to an integer column using .map().
#   3. def encode_binary_flag(self, target_column, true_val, false_val)
#      - Convert a binary string column (e.g. 'Yes'/'No') to 1 and 0.
#   4. def frequency_encode_categories(self, column_name)
#      - Replace each category in column_name with its normalized frequency count (.value_counts(normalize=True)).
#   5. def get_encoded_dataframe(self)
#      - Return the fully transformed DataFrame, ensuring all object dtypes have 
#        been converted to numeric.
# """

# class CustomerFeatureEncoder:

#     def __init__(self, df_customers):
#         self.df = df_customers.copy()

#     def one_hot_encode_nominal(self, columns_to_encode, prefix_tags=None):
#         self.df = pd.get_dummies(
#             self.df,
#             columns=columns_to_encode,
#             prefix=prefix_tags,
#             drop_first=True,
#             dtype=int
#         )
#         return self.df

#     def ordinal_encode_tier(self, tier_column, hierarchy_dict):
#         encoded_column = tier_column + "_Encoded"

#         self.df[encoded_column] = self.df[tier_column].map(
#             hierarchy_dict
#         )

#         return self.df

#     def encode_binary_flag(self, target_column, true_val, false_val):
#         self.df[target_column] = self.df[target_column].map(
#             {
#                 true_val: 1,
#                 false_val: 0
#             }
#         )

#         return self.df

#     def frequency_encode_categories(self, column_name):
#         frequency = self.df[column_name].value_counts(
#             normalize=True
#         )

#         self.df[column_name + "_Frequency"] = (
#             self.df[column_name].map(frequency)
#         )

#         return self.df

#     def get_encoded_dataframe(self):
#         object_columns = self.df.select_dtypes(
#             include="object"
#         ).columns

#         for column in object_columns:
#             self.df[column] = pd.factorize(
#                 self.df[column]
#             )[0]

#         return self.df








# customer_data = {
#     "Customer_ID": [101, 102, 103, 104, 105, 106],
#     "Subscription": [
#         "Basic", "Premium", "Basic",
#         "Gold", "Premium", "Basic"
#     ],
#     "Region": [
#         "North", "South", "North",
#         "West", "East", "South"
#     ],
#     "Tier": [
#         "Bronze", "Gold", "Silver",
#         "Platinum", "Gold", "Bronze"
#     ],
#     "Active": [
#         "Yes", "Yes", "No",
#         "Yes", "No", "Yes"
#     ]
# }

# customers_df = pd.DataFrame(customer_data)

# encoder = CustomerFeatureEncoder(customers_df)

# =============================================================================
# QUESTION 08: Feature Scaler Normalizer (Math from Scratch)
# Concepts: Min-Max Normalization (0 to 1) & Z-Score Standardization (Mean=0, Std=1)
# =============================================================================
"""
Scenario:
Before feeding features into distance-based ML algorithms (KNN, SVM, K-Means), 
features with vastly different scales (e.g., Age 20-60 vs Salary 30k-150k) 
must be normalized. Implement scaling algorithms strictly from mathematical 
formulas using Pandas/Numpy without external sklearn packages.

Class Name: FeatureScalerNormalizer
Constructor: __init__(self, df_features)
  - Stores df_features in self.df.

Tasks to Implement:
  1. def min_max_scale_column(self, column_name)
     - Compute and return a Series scaled to [0, 1] using:
       Formula: (X - X_min) / (X_max - X_min)
  2. def z_score_standardize_column(self, column_name)
     - Compute and return a Series with Mean=0 and Std=1 using:
       Formula: (X - Mean) / Std
  3. def scale_all_numeric_min_max(self, numeric_cols)
     - Apply Min-Max scaling to all specified columns and store as new columns 
       with the suffix '_minmax'.
  4. def scale_all_numeric_z_score(self, numeric_cols)
     - Apply Z-score standardization to all specified columns and store with 
       the suffix '_zscore'.
  5. def verify_scaling_properties(self, scaled_column_name, method='zscore')
     - If method is 'zscore': assert that mean is approximately 0 and std is 
       approximately 1 (return actual mean and std rounded to 4 decimals).
     - If method is 'minmax': assert min is 0.0 and max is 1.0 (return min and max).
"""


class FeatureScalerNormalizer:

    def __init__(self, df_features):
        self.df = df_features.copy()

    def min_max_scale_column(self, column_name):
        min_value = self.df[column_name].min()
        max_value = self.df[column_name].max()

        scaled = (
            self.df[column_name] - min_value
        ) / (
            max_value - min_value
        )

        return scaled

    def z_score_standardize_column(self, column_name):
        mean_value = self.df[column_name].mean()
        std_value = self.df[column_name].std()

        standardized = (
            self.df[column_name] - mean_value
        ) / std_value

        return standardized

    def scale_all_numeric_min_max(self, numeric_cols):
        for column in numeric_cols:
            self.df[column + "_minmax"] = (
                self.min_max_scale_column(column)
            )

        return self.df

    def scale_all_numeric_z_score(self, numeric_cols):
        for column in numeric_cols:
            self.df[column + "_zscore"] = (
                self.z_score_standardize_column(column)
            )

        return self.df

    def verify_scaling_properties(
        self,
        scaled_column_name,
        method="zscore"
    ):
        if method == "zscore":

            actual_mean = self.df[scaled_column_name].mean()
            actual_std = self.df[scaled_column_name].std()

            assert np.isclose(actual_mean, 0, atol=1e-10)
            assert np.isclose(actual_std, 1, atol=1e-10)

            return (
                round(actual_mean, 4),
                round(actual_std, 4)
            )

        elif method == "minmax":

            actual_min = self.df[scaled_column_name].min()
            actual_max = self.df[scaled_column_name].max()

            assert np.isclose(actual_min, 0.0)
            assert np.isclose(actual_max, 1.0)

            return actual_min, actual_max
        




feature_data = {
    "Age": [20, 25, 30, 35, 40],
    "Salary": [30000, 50000, 70000, 90000, 110000],
    "Experience": [1, 3, 5, 7, 9]
}

features_df = pd.DataFrame(feature_data)

scaler = FeatureScalerNormalizer(features_df)







print("\n--- Min-Max Scaling ---")
print(
    scaler.min_max_scale_column("Salary")
)

print("\n--- Z-Score Standardization ---")
print(
    scaler.z_score_standardize_column("Salary")
)

print("\n--- All Numeric Min-Max ---")
print(
    scaler.scale_all_numeric_min_max(
        ["Age", "Salary", "Experience"]
    )
)

print("\n--- All Numeric Z-Score ---")
print(
    scaler.scale_all_numeric_z_score(
        ["Age", "Salary", "Experience"]
    )
)

print("\n--- Verify Z-Score ---")
print(
    scaler.verify_scaling_properties(
        "Salary_zscore",
        "zscore"
    )
)

print("\n--- Verify Min-Max ---")
print(
    scaler.verify_scaling_properties(
        "Salary_minmax",
        "minmax"
    )
)


# =============================================================================
# QUESTION 09: Outlier Detector IQR (Statistical Quality Control)
# Concepts: IQR Calculation (Q1, Q3), Fence Limits, Outlier Filtering & .clip()
# =============================================================================
"""
Scenario:
Outliers in industrial sensor readings or financial transactions can skew 
analytical models. You need to implement an automated statistical outlier 
detection and remediation engine utilizing the Interquartile Range (IQR) rule.

Class Name: OutlierDetectorIQR
Constructor: __init__(self, df_data)
  - Stores df_data in self.df.

Tasks to Implement:
  1. def calculate_iqr_bounds(self, column_name, factor=1.5)
     - Compute Q1 (25th percentile), Q3 (75th percentile), and IQR = Q3 - Q1.
     - Compute Lower Bound = Q1 - factor * IQR and Upper Bound = Q3 + factor * IQR.
     - Return a dictionary: {'Q1': ..., 'Q3': ..., 'IQR': ..., 'Lower_Bound': ..., 'Upper_Bound': ...}.
  2. def isolate_outliers(self, column_name, factor=1.5)
     - Return a DataFrame containing only rows where column_name values fall 
       strictly below Lower Bound or strictly above Upper Bound.
  3. def count_outlier_percentage(self, column_name, factor=1.5)
     - Calculate what percentage of total rows in column_name are classified as outliers.
  4. def cap_outliers(self, column_name, factor=1.5)
     - Use Pandas .clip(lower=lower_bound, upper=upper_bound) to cap extreme values. 
       Save the result into a new column '{column_name}_clipped'.
  5. def compare_spread_metrics(self, original_col, clipped_col)
     - Return a comparison summary showing (Mean, Std, Min, Max) for both the 
       original column and the clipped column.
  6. def remove_outlier_rows(self, column_name, factor=1.5)
     - Return a filtered DataFrame with all outlier rows pruned.
"""

class OutlierDetectorIQR:

    def __init__(self, df_data):
        self.df = df_data.copy()

    def calculate_iqr_bounds(self, column_name, factor=1.5):
        q1 = self.df[column_name].quantile(0.25)
        q3 = self.df[column_name].quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - factor * iqr
        upper_bound = q3 + factor * iqr

        return {
            "Q1": q1,
            "Q3": q3,
            "IQR": iqr,
            "Lower_Bound": lower_bound,
            "Upper_Bound": upper_bound
        }

    def isolate_outliers(self, column_name, factor=1.5):
        bounds = self.calculate_iqr_bounds(
            column_name,
            factor
        )

        lower_bound = bounds["Lower_Bound"]
        upper_bound = bounds["Upper_Bound"]

        return self.df[
            (self.df[column_name] < lower_bound) |
            (self.df[column_name] > upper_bound)
        ]

    def count_outlier_percentage(self, column_name, factor=1.5):
        outliers = self.isolate_outliers(
            column_name,
            factor
        )

        total_rows = len(self.df)

        percentage = (
            len(outliers) / total_rows
        ) * 100

        return percentage

    def cap_outliers(self, column_name, factor=1.5):
        bounds = self.calculate_iqr_bounds(
            column_name,
            factor
        )

        lower_bound = bounds["Lower_Bound"]
        upper_bound = bounds["Upper_Bound"]

        self.df[column_name + "_clipped"] = (
            self.df[column_name].clip(
                lower=lower_bound,
                upper=upper_bound
            )
        )

        return self.df

    def compare_spread_metrics(
        self,
        original_col,
        clipped_col
    ):
        return pd.DataFrame({
            "Original": [
                self.df[original_col].mean(),
                self.df[original_col].std(),
                self.df[original_col].min(),
                self.df[original_col].max()
            ],
            "Clipped": [
                self.df[clipped_col].mean(),
                self.df[clipped_col].std(),
                self.df[clipped_col].min(),
                self.df[clipped_col].max()
            ]
        }, index=[
            "Mean",
            "Std",
            "Min",
            "Max"
        ])

    def remove_outlier_rows(self, column_name, factor=1.5):
        bounds = self.calculate_iqr_bounds(
            column_name,
            factor
        )

        lower_bound = bounds["Lower_Bound"]
        upper_bound = bounds["Upper_Bound"]

        return self.df[
            (self.df[column_name] >= lower_bound) &
            (self.df[column_name] <= upper_bound)
        ]
    




outlier_data = {
    "Transaction_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Amount": [100, 120, 110, 130, 125, 115, 140, 1000]
}

outlier_df = pd.DataFrame(outlier_data)

detector = OutlierDetectorIQR(outlier_df)






print("\n--- IQR Bounds ---")
print(
    detector.calculate_iqr_bounds("Amount")
)

print("\n--- Outliers ---")
print(
    detector.isolate_outliers("Amount")
)

print("\n--- Outlier Percentage ---")
print(
    detector.count_outlier_percentage("Amount")
)

print("\n--- Capped Data ---")
print(
    detector.cap_outliers("Amount")
)

print("\n--- Spread Comparison ---")
print(
    detector.compare_spread_metrics(
        "Amount",
        "Amount_clipped"
    )
)

print("\n--- Data After Removing Outliers ---")
print(
    detector.remove_outlier_rows("Amount")
)










# =============================================================================
# QUESTION 10: Multicollinearity Analyzer (Statistical Modeling)
# Concepts: Pearson Correlation Matrix (.corr()), Strong Predictor Isolation
# =============================================================================
"""
Scenario:
In predictive regression analysis, highly correlated independent features cause 
multicollinearity, making model coefficients unstable. Build a statistical 
profiler that computes feature correlation matrices and flags redundant pairs.

Class Name: MulticollinearityAnalyzer
Constructor: __init__(self, df_dataset)
  - Stores df_dataset in self.df.

Tasks to Implement:
  1. def compute_correlation_matrix(self, numeric_cols=None)
     - Compute and return the pairwise Pearson correlation matrix (.corr()) 
       for numeric features rounded to 3 decimal places.
  2. def find_top_target_correlations(self, target_column)
     - Compute correlations of all numerical features with target_column.
     - Return the features sorted by absolute correlation strength descending 
       (excluding the target itself).
  3. def detect_high_collinearity_pairs(self, threshold=0.75)
     - Identify all unique pairs of features whose correlation coefficient is 
       greater than threshold or less than -threshold (ignoring self-correlations 1.0).
  4. def isolate_weak_predictors(self, target_column, min_threshold=0.10)
     - Return a list of columns whose absolute correlation with target_column 
       is below min_threshold.
  5. def filter_non_redundant_features(self, target_column, collinear_threshold=0.80)
     - Recommend which redundant features to drop to prevent collinearity while 
       preserving the highest correlation with the target.
"""
class MulticollinearityAnalyzer:

    def __init__(self, df_dataset):
        self.df = df_dataset.copy()

    def compute_correlation_matrix(self, numeric_cols=None):

        if numeric_cols is None:
            numeric_cols = self.df.select_dtypes(
                include=np.number
            ).columns

        return self.df[numeric_cols].corr().round(3)

    def find_top_target_correlations(self, target_column):

        correlation = self.df.select_dtypes(
            include=np.number
        ).corr()[target_column]

        correlation = correlation.drop(
            target_column
        )

        return correlation.reindex(
            correlation.abs().sort_values(
                ascending=False
            ).index
        )

    def detect_high_collinearity_pairs(
        self,
        threshold=0.75
    ):

        correlation_matrix = self.compute_correlation_matrix()

        pairs = []

        columns = correlation_matrix.columns

        for i in range(len(columns)):
            for j in range(i + 1, len(columns)):

                correlation = correlation_matrix.iloc[i, j]

                if abs(correlation) > threshold:
                    pairs.append(
                        (
                            columns[i],
                            columns[j],
                            round(correlation, 3)
                        )
                    )

        return pairs

    def isolate_weak_predictors(
        self,
        target_column,
        min_threshold=0.10
    ):

        correlation = self.df.select_dtypes(
            include=np.number
        ).corr()[target_column]

        correlation = correlation.drop(
            target_column
        )

        return correlation[
            correlation.abs() < min_threshold
        ].index.tolist()

    def filter_non_redundant_features(
        self,
        target_column,
        collinear_threshold=0.80
    ):

        correlation_matrix = self.compute_correlation_matrix()

        target_correlations = (
            correlation_matrix[target_column]
            .drop(target_column)
            .abs()
            .sort_values(ascending=False)
        )

        selected_features = []
        features_to_drop = []

        for feature in target_correlations.index:

            should_drop = False

            for selected in selected_features:

                pair_correlation = abs(
                    correlation_matrix.loc[
                        feature,
                        selected
                    ]
                )

                if pair_correlation > collinear_threshold:
                    should_drop = True
                    break

            if should_drop:
                features_to_drop.append(feature)
            else:
                selected_features.append(feature)

        return {
            "Selected_Features": selected_features,
            "Features_To_Drop": features_to_drop
        }

dataset = {
    "Age": [20, 25, 30, 35, 40, 45, 50, 55],
    "Experience": [1, 3, 5, 7, 9, 11, 13, 15],
    "Salary": [30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000],
    "Performance": [50, 55, 60, 65, 70, 75, 80, 85],
    "Sales": [100, 120, 140, 160, 180, 200, 220, 240]
}

dataset_df = pd.DataFrame(dataset)

analyzer = MulticollinearityAnalyzer(dataset_df)




print("\n--- Correlation Matrix ---")
print(
    analyzer.compute_correlation_matrix()
)

print("\n--- Target Correlations ---")
print(
    analyzer.find_top_target_correlations(
        "Salary"
    )
)

print("\n--- High Collinearity Pairs ---")
print(
    analyzer.detect_high_collinearity_pairs()
)

print("\n--- Weak Predictors ---")
print(
    analyzer.isolate_weak_predictors(
        "Salary"
    )
)

print("\n--- Non-Redundant Features ---")
print(
    analyzer.filter_non_redundant_features(
        "Salary"
    )
)

# =============================================================================
# QUESTION 11: Demographic Binner (Market Segmentation)
# Concepts: Discretization & Binning (pd.cut for Custom Bins, pd.qcut for Quantiles)
# =============================================================================
"""
Scenario:
A digital streaming platform wants to segment users into demographic and spending 
tiers. Create a discretization class to transform continuous variables (Age, 
Monthly Spend, Watch Hours) into distinct categorical cohorts.

Class Name: DemographicBinner
Constructor: __init__(self, df_users)
  - Stores df_users in self.df.

Tasks to Implement:
  1. def bin_by_custom_intervals(self, column_name, bins, labels, new_col_name)
     - Use pd.cut() to discretize column_name into user-defined bins with corresponding 
       labels. Store the result in self.df[new_col_name].
  2. def bin_by_quantiles(self, column_name, q=4, labels=None, new_col_name=None)
     - Use pd.qcut() to divide column_name into q equal-frequency quantiles (e.g. 
       quartiles or tertiles).
  3. def get_bin_distribution_counts(self, binned_column_name)
     - Return the frequency distribution count (.value_counts()) and percentage 
       breakdown for each bin in binned_column_name.
  4. def cross_tabulate_bins(self, bin_col_1, bin_col_2)
     - Use pd.crosstab() to display a matrix showing the intersection counts 
       between two discretized categories.
  5. def detect_out_of_bounds_records(self, column_name, binned_column_name)
     - Identify any rows where the binned value is NaN (indicating values fell 
       outside custom bin intervals).
"""


class DemographicBinner:

    def __init__(self, df_users):
        self.df = df_users.copy()

    def bin_by_custom_intervals(
        self,
        column_name,
        bins,
        labels,
        new_col_name
    ):
        self.df[new_col_name] = pd.cut(
            self.df[column_name],
            bins=bins,
            labels=labels
        )

        return self.df

    def bin_by_quantiles(
        self,
        column_name,
        q=4,
        labels=None,
        new_col_name=None
    ):
        if new_col_name is None:
            new_col_name = column_name + "_Quantile"

        self.df[new_col_name] = pd.qcut(
            self.df[column_name],
            q=q,
            labels=labels
        )

        return self.df

    def get_bin_distribution_counts(
        self,
        binned_column_name
    ):
        counts = self.df[
            binned_column_name
        ].value_counts()

        percentages = (
            self.df[binned_column_name]
            .value_counts(normalize=True)
            * 100
        ).round(2)

        return pd.DataFrame({
            "Count": counts,
            "Percentage": percentages
        })

    def cross_tabulate_bins(
        self,
        bin_col_1,
        bin_col_2
    ):
        return pd.crosstab(
            self.df[bin_col_1],
            self.df[bin_col_2]
        )

    def detect_out_of_bounds_records(
        self,
        column_name,
        binned_column_name
    ):
        return self.df[
            self.df[binned_column_name].isna()
        ]
    








user_data = {
    "User_ID": [101, 102, 103, 104, 105, 106, 107, 108],
    "Age": [18, 25, 32, 41, 55, 63, 72, 85],
    "Monthly_Spend": [
        100, 250, 400, 550,
        700, 900, 1200, 1500
    ],
    "Watch_Hours": [
        5, 10, 15, 20,
        25, 30, 35, 40
    ]
}

users_df = pd.DataFrame(user_data)

binner = DemographicBinner(users_df)








print("\n--- Custom Age Bins ---")
print(
    binner.bin_by_custom_intervals(
        "Age",
        [0, 30, 50, 70, 100],
        ["Young", "Adult", "Senior", "Elder"],
        "Age_Group"
    )
)

print("\n--- Quantile Spend Bins ---")
print(
    binner.bin_by_quantiles(
        "Monthly_Spend",
        q=4,
        labels=[
            "Low",
            "Medium",
            "High",
            "Very High"
        ],
        new_col_name="Spend_Group"
    )
)

print("\n--- Bin Distribution ---")
print(
    binner.get_bin_distribution_counts(
        "Age_Group"
    )
)

print("\n--- Cross Tabulation ---")
print(
    binner.cross_tabulate_bins(
        "Age_Group",
        "Spend_Group"
    )
)

print("\n--- Out of Bounds Records ---")
print(
    binner.detect_out_of_bounds_records(
        "Age",
        "Age_Group"
    )
)

# =============================================================================
# QUESTION 12: Time Feature Extractor (Logistics & Delivery)
# Concepts: DateTime Conversion, .dt Accessor, Calendar Features & Turnaround
# =============================================================================
"""
Scenario:
A logistics fleet logs shipment dispatch and delivery events. To build route 
optimization models, you must parse raw timestamps and engineer cyclical 
calendar features, weekend markers, and delivery duration metrics.

Class Name: TimeFeatureExtractor
Constructor: __init__(self, df_logistics)
  - Stores df_logistics in self.df.

Tasks to Implement:
  1. def convert_to_datetime(self, timestamp_columns)
     - Convert all specified string columns to datetime64 format using pd.to_datetime().
  2. def extract_calendar_parts(self, date_column)
     - Create new feature columns:
       * '{date_column}_Year': .dt.year
       * '{date_column}_Month': .dt.month_name()
       * '{date_column}_Quarter': .dt.quarter
       * '{date_column}_DayOfWeek': .dt.day_name()
  3. def flag_weekends(self, date_column)
     - Create a boolean column '{date_column}_Is_Weekend' where day of week is 
       Saturday (5) or Sunday (6).
  4. def compute_duration_hours(self, start_time_col, end_time_col, new_duration_col)
     - Calculate turnaround time in hours: (end_time - start_time).dt.total_seconds() / 3600.
  5. def extract_hour_of_day(self, timestamp_col)
     - Extract hour (.dt.hour) and categorize into time blocks: 
       'Morning' (6-11), 'Afternoon' (12-16), 'Evening' (17-21), 'Night' (22-5).
  6. def filter_deliveries_by_date_range(self, date_column, start_date, end_date)
     - Filter and return shipments scheduled between start_date and end_date.
"""


class TimeFeatureExtractor:

    def __init__(self, df_logistics):
        self.df = df_logistics.copy()

    def convert_to_datetime(self, timestamp_columns):
        for column in timestamp_columns:
            self.df[column] = pd.to_datetime(
                self.df[column]
            )

        return self.df

    def extract_calendar_parts(self, date_column):

        self.df[date_column + "_Year"] = (
            self.df[date_column].dt.year
        )

        self.df[date_column + "_Month"] = (
            self.df[date_column].dt.month_name()
        )

        self.df[date_column + "_Quarter"] = (
            self.df[date_column].dt.quarter
        )

        self.df[date_column + "_DayOfWeek"] = (
            self.df[date_column].dt.day_name()
        )

        return self.df

    def flag_weekends(self, date_column):

        self.df[date_column + "_Is_Weekend"] = (
            self.df[date_column].dt.dayofweek.isin([5, 6])
        )

        return self.df

    def compute_duration_hours(
        self,
        start_time_col,
        end_time_col,
        new_duration_col
    ):

        self.df[new_duration_col] = (
            self.df[end_time_col]
            - self.df[start_time_col]
        ).dt.total_seconds() / 3600

        return self.df

    def extract_hour_of_day(self, timestamp_col):

        hour = self.df[timestamp_col].dt.hour

        self.df[timestamp_col + "_Hour"] = hour

        self.df[timestamp_col + "_Time_Block"] = np.select(
            [
                hour.between(6, 11),
                hour.between(12, 16),
                hour.between(17, 21)
            ],
            [
                "Morning",
                "Afternoon",
                "Evening"
            ],
            default="Night"
        )

        return self.df

    def filter_deliveries_by_date_range(
        self,
        date_column,
        start_date,
        end_date
    ):

        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        return self.df[
            self.df[date_column].between(
                start_date,
                end_date
            )
        ]
    






logistics_data = {
    "Shipment_ID": [101, 102, 103, 104, 105, 106],
    "Dispatch_Time": [
        "2026-01-05 08:30",
        "2026-01-06 14:00",
        "2026-01-10 19:30",
        "2026-01-11 23:00",
        "2026-01-15 10:00",
        "2026-01-20 16:30"
    ],
    "Delivery_Time": [
        "2026-01-05 18:30",
        "2026-01-07 02:00",
        "2026-01-11 04:30",
        "2026-01-12 09:00",
        "2026-01-16 08:00",
        "2026-01-20 22:30"
    ]
}

logistics_df = pd.DataFrame(logistics_data)

extractor = TimeFeatureExtractor(logistics_df)







print("\n--- Convert To Datetime ---")
print(
    extractor.convert_to_datetime(
        ["Dispatch_Time", "Delivery_Time"]
    )
)

print("\n--- Calendar Features ---")
print(
    extractor.extract_calendar_parts(
        "Dispatch_Time"
    )
)

print("\n--- Weekend Flag ---")
print(
    extractor.flag_weekends(
        "Dispatch_Time"
    )
)

print("\n--- Duration In Hours ---")
print(
    extractor.compute_duration_hours(
        "Dispatch_Time",
        "Delivery_Time",
        "Delivery_Duration_Hours"
    )
)

print("\n--- Hour And Time Block ---")
print(
    extractor.extract_hour_of_day(
        "Dispatch_Time"
    )
)

print("\n--- Date Range Filter ---")
print(
    extractor.filter_deliveries_by_date_range(
        "Dispatch_Time",
        "2026-01-05",
        "2026-01-15"
    )
)
# =============================================================================
# QUESTION 13: CrossTab Reshaper (Business Intelligence)
# Concepts: Pivot Tables (pivot_table), Custom aggfunc, fill_value, margins
# =============================================================================
"""
Scenario:
A retail store chain requires an analytical reporting class that reshapes flat 
transaction tables into multi-dimensional summary grids to compare product 
sales across different store tiers and regions.

Class Name: CrossTabReshaper
Constructor: __init__(self, df_transactions)
  - Stores df_transactions in self.df.

Tasks to Implement:
  1. def build_sales_pivot(self, index_col='Region', column_col='Category', val_col='Sales_Amount')
     - Build a pivot table showing mean sales, filling missing cells with 0.
  2. def build_multi_metric_pivot(self, index_col, column_col, metric_dict)
     - Create a pivot table supporting different aggfuncs per value column 
       (e.g., {'Sales': 'sum', 'Discount': 'mean'}).
  3. def add_grand_totals(self, index_col, column_col, val_col, agg_func='sum')
     - Build a pivot table with margins=True and margins_name='Grand Total'.
  4. def multi_index_pivot(self, row_levels, col_levels, val_col)
     - Build a hierarchical multi-index row and column pivot table.
  5. def flatten_pivot_table(self, pivot_df)
     - Reset the index and flatten multi-level column tuples into clean snake_case 
       column names (e.g. 'sales_sum', 'profit_mean').
"""

class CrossTabReshaper:

    def __init__(self, df_transactions):
        self.df = df_transactions.copy()

    def build_sales_pivot(
        self,
        index_col="Region",
        column_col="Category",
        val_col="Sales_Amount"
    ):
        return pd.pivot_table(
            self.df,
            index=index_col,
            columns=column_col,
            values=val_col,
            aggfunc="mean",
            fill_value=0
        )

    def build_multi_metric_pivot(
        self,
        index_col,
        column_col,
        metric_dict
    ):
        return pd.pivot_table(
            self.df,
            index=index_col,
            columns=column_col,
            values=list(metric_dict.keys()),
            aggfunc=metric_dict,
            fill_value=0
        )

    def add_grand_totals(
        self,
        index_col,
        column_col,
        val_col,
        agg_func="sum"
    ):
        return pd.pivot_table(
            self.df,
            index=index_col,
            columns=column_col,
            values=val_col,
            aggfunc=agg_func,
            fill_value=0,
            margins=True,
            margins_name="Grand Total"
        )

    def multi_index_pivot(
        self,
        row_levels,
        col_levels,
        val_col
    ):
        return pd.pivot_table(
            self.df,
            index=row_levels,
            columns=col_levels,
            values=val_col,
            aggfunc="sum",
            fill_value=0
        )

    def flatten_pivot_table(self, pivot_df):
        pivot_df = pivot_df.reset_index()

        new_columns = []

        for column in pivot_df.columns:
            if isinstance(column, tuple):
                column_name = "_".join(
                    str(value)
                    for value in column
                    if str(value) != ""
                )
            else:
                column_name = str(column)

            column_name = column_name.lower().replace(" ", "_")
            new_columns.append(column_name)

        pivot_df.columns = new_columns

        return pivot_df
    






transaction_data = {
    "Region": [
        "North", "North", "South", "South",
        "East", "East", "West", "West"
    ],
    "Category": [
        "Electronics", "Furniture", "Electronics", "Clothing",
        "Furniture", "Electronics", "Clothing", "Furniture"
    ],
    "Sales_Amount": [
        50000, 30000, 45000, 20000,
        35000, 60000, 25000, 40000
    ],
    "Profit": [
        10000, 6000, 9000, 5000,
        7000, 12000, 5500, 8000
    ],
    "Discount": [
        5, 10, 8, 12,
        7, 6, 15, 9
    ]
}

transactions_df = pd.DataFrame(transaction_data)

reshaper = CrossTabReshaper(transactions_df)




print("\n--- Sales Pivot ---")
print(
    reshaper.build_sales_pivot()
)

print("\n--- Multi Metric Pivot ---")
print(
    reshaper.build_multi_metric_pivot(
        "Region",
        "Category",
        {
            "Sales_Amount": "sum",
            "Discount": "mean"
        }
    )
)

print("\n--- Grand Totals Pivot ---")
print(
    reshaper.add_grand_totals(
        "Region",
        "Category",
        "Sales_Amount"
    )
)

print("\n--- Multi Index Pivot ---")
print(
    reshaper.multi_index_pivot(
        ["Region"],
        ["Category"],
        "Sales_Amount"
    )
)

print("\n--- Flatten Pivot ---")
pivot = reshaper.build_multi_metric_pivot(
    "Region",
    "Category",
    {
        "Sales_Amount": "sum",
        "Profit": "mean"
    }
)

print(
    reshaper.flatten_pivot_table(pivot)
)














# =============================================================================
# QUESTION 14: Cyber Security Log Analyzer (Threat Hunting)
# Concepts: Filtering Status Codes, IP Frequency Grouping, DateTime Hour Hunting
# =============================================================================
"""
Scenario:
A Security Operations Center (SOC) ingests web server access logs containing 
timestamp, source_ip, method, status_code, bytes_sent, and endpoint. Create an 
automated intrusion detection class to flag brute-force and scraping activities.

Class Name: CyberSecurityLogAnalyzer
Constructor: __init__(self, df_logs)
  - Stores server access logs in self.df.

Tasks to Implement:
  1. def filter_client_and_server_errors(self)
     - Return all logs with HTTP status_code >= 400 (4xx client errors & 5xx server errors).
  2. def detect_brute_force_ips(self, failure_threshold=10)
     - Group by 'source_ip' and count 401/403 Unauthorized status codes. Return 
       IPs that exceed failure_threshold.
  3. def extract_hourly_attack_trends(self, timestamp_col='timestamp')
     - Parse timestamps, extract the hour, and compute the total volume of failed 
       access attempts per hour.
  4. def identify_top_scraped_endpoints(self, top_n=5)
     - Return the top_n most frequently accessed endpoints and their total bandwidth 
       consumed (sum of 'bytes_sent').
  5. def flag_after_hours_logins(self, business_hours=(9, 18))
     - Flag logins where the hour falls outside business_hours on weekdays or occurs 
       on weekends.
  6. def generate_soc_executive_summary(self)
     - Return a dictionary reporting: Total Requests, Unique Visitors, Total Blocked 
       Attempts, and Most Targeted Endpoint.
"""


class CyberSecurityLogAnalyzer:

    def __init__(self, df_logs):
        self.df = df_logs.copy()

    def filter_client_and_server_errors(self):
        return self.df[
            self.df["status_code"] >= 400
        ]

    def detect_brute_force_ips(self, failure_threshold=10):
        failed_logs = self.df[
            self.df["status_code"].isin([401, 403])
        ]

        ip_counts = (
            failed_logs.groupby("source_ip")
            .size()
            .reset_index(name="Failure_Count")
        )

        return ip_counts[
            ip_counts["Failure_Count"] > failure_threshold
        ]

    def extract_hourly_attack_trends(
        self,
        timestamp_col="timestamp"
    ):
        self.df[timestamp_col] = pd.to_datetime(
            self.df[timestamp_col]
        )

        failed_logs = self.df[
            self.df["status_code"] >= 400
        ].copy()

        failed_logs["Hour"] = (
            failed_logs[timestamp_col].dt.hour
        )

        return (
            failed_logs.groupby("Hour")
            .size()
            .reset_index(name="Failed_Attempts")
            .sort_values("Hour")
        )

    def identify_top_scraped_endpoints(self, top_n=5):
        endpoint_summary = (
            self.df.groupby("endpoint")
            .agg(
                Access_Count=("endpoint", "count"),
                Total_Bandwidth=("bytes_sent", "sum")
            )
            .sort_values(
                "Access_Count",
                ascending=False
            )
        )

        return endpoint_summary.head(top_n)

    def flag_after_hours_logins(
        self,
        business_hours=(9, 18)
    ):
        self.df["timestamp"] = pd.to_datetime(
            self.df["timestamp"]
        )

        hour = self.df["timestamp"].dt.hour
        weekday = self.df["timestamp"].dt.dayofweek

        start_hour, end_hour = business_hours

        self.df["After_Hours"] = (
            (weekday >= 5) |
            (hour < start_hour) |
            (hour >= end_hour)
        )

        return self.df

    def generate_soc_executive_summary(self):
        total_requests = len(self.df)

        unique_visitors = self.df[
            "source_ip"
        ].nunique()

        total_blocked_attempts = len(
            self.df[
                self.df["status_code"].isin(
                    [401, 403]
                )
            ]
        )

        most_targeted_endpoint = (
            self.df["endpoint"]
            .value_counts()
            .idxmax()
        )

        return {
            "Total Requests": total_requests,
            "Unique Visitors": unique_visitors,
            "Total Blocked Attempts": total_blocked_attempts,
            "Most Targeted Endpoint":
                most_targeted_endpoint
        }
 





log_data = {
    "timestamp": [
        "2026-01-05 08:30",
        "2026-01-05 10:00",
        "2026-01-05 22:30",
        "2026-01-06 11:00",
        "2026-01-06 02:00",
        "2026-01-10 14:00",
        "2026-01-10 23:00",
        "2026-01-11 03:00"
    ],
    "source_ip": [
        "192.168.1.10",
        "192.168.1.11",
        "192.168.1.10",
        "192.168.1.12",
        "192.168.1.10",
        "192.168.1.13",
        "192.168.1.11",
        "192.168.1.10"
    ],
    "method": [
        "GET", "POST", "GET", "GET",
        "POST", "GET", "GET", "POST"
    ],
    "status_code": [
        200, 404, 401, 200,
        403, 500, 200, 403
    ],
    "bytes_sent": [
        1200, 800, 1500, 2000,
        900, 3000, 1800, 700
    ],
    "endpoint": [
        "/home",
        "/login",
        "/login",
        "/products",
        "/login",
        "/api/data",
        "/home",
        "/login"
    ]
}

logs_df = pd.DataFrame(log_data)

analyzer = CyberSecurityLogAnalyzer(logs_df)






print("\n--- Client And Server Errors ---")
print(
    analyzer.filter_client_and_server_errors()
)

print("\n--- Brute Force IPs ---")
print(
    analyzer.detect_brute_force_ips(
        failure_threshold=1
    )
)

print("\n--- Hourly Attack Trends ---")
print(
    analyzer.extract_hourly_attack_trends()
)

print("\n--- Top Scraped Endpoints ---")
print(
    analyzer.identify_top_scraped_endpoints()
)

print("\n--- After Hours Logins ---")
print(
    analyzer.flag_after_hours_logins()
)

print("\n--- SOC Executive Summary ---")
print(
    analyzer.generate_soc_executive_summary()
)


# =============================================================================
# QUESTION 15: Banking Fraud Detector (FinTech Risk Scoring)
# Concepts: Z-Score Outlier Flagging, Custom .apply() Logic, IQR Clipping
# =============================================================================
"""
Scenario:
A digital payments bank must inspect incoming credit card transactions for 
fraudulent patterns. Implement a risk scoring class that calculates statistical 
z-scores, flags rapid multi-swipes, and assigns composite suspicion ratings.

Class Name: BankingFraudDetector
Constructor: __init__(self, df_transactions)
  - Stores transactions in self.df.

Tasks to Implement:
  1. def compute_amount_z_scores(self)
     - Calculate Z-scores for 'transaction_amount'. Create a boolean column 
       'is_stat_anomaly' where abs(z_score) > 3.0.
  2. def flag_night_transactions(self, time_col='trans_time')
     - Flag transactions occurring between 1:00 AM and 5:00 AM as 'is_night_trans'.
  3. def assign_composite_risk_score(self)
     - Use .apply(axis=1) with a custom function or lambda to assign:
       * 'High Risk': if is_stat_anomaly is True AND is_night_trans is True
       * 'Medium Risk': if either is True
       * 'Low Risk': if neither is True
  4. def isolate_suspicious_accounts(self)
     - Group by 'account_number' and filter accounts that have 2 or more 'High Risk' 
       transactions.
  5. def clip_transaction_extremes(self)
     - Use the IQR method to cap extreme values in 'transaction_amount' so reports 
       are not distorted by fraudulent outliers.
  6. def generate_fraud_loss_exposure(self)
     - Compute the total potential financial exposure (sum of amounts) categorized 
       under 'High Risk'.
"""



class BankingFraudDetector:

    def __init__(self, df_transactions):
        self.df = df_transactions.copy()

    def compute_amount_z_scores(self):
        mean_value = self.df["transaction_amount"].mean()
        std_value = self.df["transaction_amount"].std()

        self.df["amount_z_score"] = (
            self.df["transaction_amount"] - mean_value
        ) / std_value

        self.df["is_stat_anomaly"] = (
            self.df["amount_z_score"].abs() > 3.0
        )

        return self.df

    def flag_night_transactions(
        self,
        time_col="trans_time"
    ):
        self.df[time_col] = pd.to_datetime(
            self.df[time_col]
        )

        hour = self.df[time_col].dt.hour

        self.df["is_night_trans"] = (
            hour.between(1, 5)
        )

        return self.df

    def flag_rapid_multi_swipes(
        self,
        time_col="trans_time",
        customer_col="customer_id",
        window_minutes=10
    ):
        self.df[time_col] = pd.to_datetime(
            self.df[time_col]
        )

        self.df = self.df.sort_values(
            [customer_col, time_col]
        )

        time_difference = (
            self.df.groupby(customer_col)[time_col]
            .diff()
            .dt.total_seconds()
            / 60
        )

        self.df["is_rapid_multi_swipe"] = (
            time_difference <= window_minutes
        )

        return self.df

    def assign_suspicion_rating(self):
        self.df["suspicion_rating"] = self.df.apply(
            lambda row: (
                "High"
                if (
                    row.get("is_stat_anomaly", False)
                    and row.get("is_night_trans", False)
                )
                else "Medium"
                if (
                    row.get("is_stat_anomaly", False)
                    or row.get("is_night_trans", False)
                    or row.get("is_rapid_multi_swipe", False)
                )
                else "Low"
            ),
            axis=1
        )

        return self.df

    def clip_transaction_amount(
        self,
        factor=1.5
    ):
        q1 = self.df["transaction_amount"].quantile(0.25)
        q3 = self.df["transaction_amount"].quantile(0.75)

        iqr = q3 - q1

        lower_bound = q1 - factor * iqr
        upper_bound = q3 + factor * iqr

        self.df["transaction_amount_clipped"] = (
            self.df["transaction_amount"].clip(
                lower=lower_bound,
                upper=upper_bound
            )
        )

        return self.df








fraud_data = {
    "transaction_id": [
        1001, 1002, 1003, 1004,
        1005, 1006, 1007, 1008
    ],
    "customer_id": [
        "C01", "C01", "C02", "C02",
        "C03", "C03", "C04", "C05"
    ],
    "transaction_amount": [
        500, 700, 1200, 1500,
        300, 450, 800, 50000
    ],
    "trans_time": [
        "2026-01-10 10:00",
        "2026-01-10 10:05",
        "2026-01-10 02:30",
        "2026-01-10 14:00",
        "2026-01-11 03:15",
        "2026-01-11 03:20",
        "2026-01-11 16:00",
        "2026-01-12 11:00"
    ]
}

fraud_df = pd.DataFrame(fraud_data)

fraud_detector = BankingFraudDetector(
    fraud_df
)

    








print("\n--- Amount Z-Scores ---")
print(
    fraud_detector.compute_amount_z_scores()
)

print("\n--- Night Transactions ---")
print(
    fraud_detector.flag_night_transactions()
)

print("\n--- Rapid Multi-Swipes ---")
print(
    fraud_detector.flag_rapid_multi_swipes()
)

print("\n--- Suspicion Rating ---")
print(
    fraud_detector.assign_suspicion_rating()
)

print("\n--- IQR Clipped Amounts ---")
print(
    fraud_detector.clip_transaction_amount()
)







# =============================================================================
# QUESTION 16: Student GradeBook Manager (EdTech Analytics)
# Concepts: Missing Data Imputation, pd.cut Grading Bands, Ranking & Grouping
# =============================================================================
"""
Scenario:
An EdTech academy records scores of students across multiple modules (Python, 
SQL, Machine Learning). Build an academic performance evaluation class that 
imputes absent test scores, assigns letter grades, and ranks top performers.

Class Name: StudentGradeBookManager
Constructor: __init__(self, df_grades)
  - Stores student grade records in self.df.

Tasks to Implement:
  1. def impute_absent_students(self, subject_cols, fill_penalty_score=0)
     - Fill missing marks in subject_cols with fill_penalty_score (marking absent).
  2. def compute_weighted_final_score(self, weights_dict)
     - Compute 'Final_Weighted_Score' using given weights (e.g. {'Python': 0.4, 'SQL': 0.3, 'ML': 0.3}).
  3. def assign_letter_grade_bands(self)
     - Use pd.cut() to assign Letter Grades based on Final_Weighted_Score:
       [0, 50): 'F', [50, 65): 'C', [65, 80): 'B', [80, 90): 'A', [90, 100]: 'A+'.
  4. def rank_students(self, scope='cohort', group_col='Section')
     - If scope == 'cohort': rank all students descending based on final score.
     - If scope == 'section': rank students within each group_col.
  5. def find_subject_toppers(self, subject_cols)
     - For each subject in subject_cols, identify the student with the highest score 
       using .idxmax().
  6. def section_performance_summary(self)
     - Group by 'Section' and calculate Mean, Median, and Pass Rate (percentage of 
       students with Grade != 'F').
"""







class StudentGradeBookManager:

    def __init__(self, df_grades):
        self.df = df_grades.copy()

    def impute_absent_students(
        self,
        subject_cols,
        fill_penalty_score=0
    ):
        for column in subject_cols:
            self.df[column] = self.df[column].fillna(
                fill_penalty_score
            )

        return self.df

    def compute_weighted_final_score(self, weights_dict):
        self.df["Final_Weighted_Score"] = 0

        for subject, weight in weights_dict.items():
            self.df["Final_Weighted_Score"] += (
                self.df[subject] * weight
            )

        return self.df

    def assign_letter_grade_bands(self):
        bins = [0, 50, 65, 80, 90, 100]
        labels = ["F", "C", "B", "A", "A+"]

        self.df["Grade"] = pd.cut(
            self.df["Final_Weighted_Score"],
            bins=bins,
            labels=labels,
            right=False,
            include_lowest=True
        )

        return self.df

    def rank_students(
        self,
        scope="cohort",
        group_col="Section"
    ):
        if scope == "cohort":
            self.df["Rank"] = (
                self.df["Final_Weighted_Score"]
                .rank(
                    ascending=False,
                    method="min"
                )
            )

        elif scope == "section":
            self.df["Rank"] = (
                self.df.groupby(group_col)[
                    "Final_Weighted_Score"
                ]
                .rank(
                    ascending=False,
                    method="min"
                )
            )

        return self.df.sort_values("Rank")

    def find_subject_toppers(self, subject_cols):
        toppers = {}

        for subject in subject_cols:
            top_index = self.df[subject].idxmax()

            toppers[subject] = {
                "Student": self.df.loc[
                    top_index, "Student_Name"
                ],
                "Score": self.df.loc[
                    top_index, subject
                ]
            }

        return toppers

    def section_performance_summary(self):
        summary = (
            self.df.groupby("Section")
            .agg(
                Mean_Score=(
                    "Final_Weighted_Score",
                    "mean"
                ),
                Median_Score=(
                    "Final_Weighted_Score",
                    "median"
                )
            )
        )

        pass_rate = (
            self.df["Grade"] != "F"
        ).groupby(
            self.df["Section"]
        ).mean() * 100

        summary["Pass_Rate"] = pass_rate

        return summary.round(2)

    

    grade_data = {
    "Student_ID": [101, 102, 103, 104, 105, 106],
    "Student_Name": [
        "Rahul",
        "Priya",
        "Amit",
        "Sneha",
        "Vijay",
        "Neha"
    ],
    "Section": [
        "A",
        "A",
        "B",
        "B",
        "A",
        "B"
    ],
    "Python": [
        85,
        72,
        None,
        91,
        65,
        78
    ],
    "SQL": [
        80,
        75,
        68,
        None,
        70,
        82
    ],
    "ML": [
        90,
        70,
        75,
        88,
        None,
        80
    ]
}

grades_df = pd.DataFrame(grade_data)

gradebook = StudentGradeBookManager(
    grades_df
)





print("\n--- Impute Absent Students ---")
print(
    gradebook.impute_absent_students(
        ["Python", "SQL", "ML"]
    )
)

print("\n--- Weighted Final Score ---")
print(
    gradebook.compute_weighted_final_score(
        {
            "Python": 0.4,
            "SQL": 0.3,
            "ML": 0.3
        }
    )
)

print("\n--- Letter Grades ---")
print(
    gradebook.assign_letter_grade_bands()
)

print("\n--- Cohort Ranking ---")
print(
    gradebook.rank_students(
        scope="cohort"
    )
)

print("\n--- Section Ranking ---")
print(
    gradebook.rank_students(
        scope="section"
    )
)

print("\n--- Subject Toppers ---")
print(
    gradebook.find_subject_toppers(
        ["Python", "SQL", "ML"]
    )
)

print("\n--- Section Performance ---")
print(
    gradebook.section_performance_summary()
)








# =============================================================================
# QUESTION 17: Inventory Supply Chain Optimizer (Warehousing)
# Concepts: Stock Calculations, Reorder Level Alerts, Relational Merging
# =============================================================================
"""
Scenario:
A centralized warehouse tracks product inventory levels, reorder points, daily 
burn rates, and vendor lead times across multiple regional depots. Create an 
inventory optimizer to prevent stockouts and identify slow-moving products.

Class Name: InventorySupplyChainOptimizer
Constructor: __init__(self, df_inventory, df_suppliers)
  - Stores df_inventory and df_suppliers.

Tasks to Implement:
  1. def calculate_days_of_supply(self)
     - Create 'Days_Of_Supply' = Current_Stock / Daily_Burn_Rate. Handle division by 
       zero by replacing with np.nan.
  2. def flag_reorder_status(self)
     - Create a boolean column 'Needs_Reorder' where Current_Stock <= Reorder_Point.
  3. def merge_supplier_lead_times(self, join_key='Supplier_ID')
     - Merge inventory with supplier database (left join) to pull 'Lead_Time_Days' 
       and 'Supplier_Contact'.
  4. def identify_stockout_emergencies(self)
     - Filter items where Days_Of_Supply < Lead_Time_Days (stock will run out 
       before supplier order arrives).
  5. def group_valuation_by_warehouse(self)
     - Compute total inventory valuation (Current_Stock * Unit_Cost) grouped 
       by Warehouse_Location.
  6. def generate_purchase_order_manifest(self)
     - For items needing reorder, calculate 'Order_Quantity' = (Reorder_Point * 2) - Current_Stock. 
       Return a consolidated purchase list.
"""






class InventorySupplyChainOptimizer:

    def __init__(self, df_inventory, df_suppliers):
        self.df_inventory = df_inventory.copy()
        self.df_suppliers = df_suppliers.copy()

    def calculate_days_of_supply(self):
        self.df_inventory["Days_Of_Supply"] = (
            self.df_inventory["Current_Stock"]
            / self.df_inventory["Daily_Burn_Rate"].replace(
                0,
                np.nan
            )
        )

        return self.df_inventory

    def flag_reorder_status(self):
        self.df_inventory["Needs_Reorder"] = (
            self.df_inventory["Current_Stock"]
            <= self.df_inventory["Reorder_Point"]
        )

        return self.df_inventory

    def merge_supplier_lead_times(
        self,
        join_key="Supplier_ID"
    ):
        self.df_inventory = pd.merge(
            self.df_inventory,
            self.df_suppliers[
                [
                    join_key,
                    "Lead_Time_Days",
                    "Supplier_Contact"
                ]
            ],
            on=join_key,
            how="left"
        )

        return self.df_inventory

    def identify_stockout_emergencies(self):
        return self.df_inventory[
            self.df_inventory["Days_Of_Supply"]
            < self.df_inventory["Lead_Time_Days"]
        ]

    def group_valuation_by_warehouse(self):
        self.df_inventory["Inventory_Valuation"] = (
            self.df_inventory["Current_Stock"]
            * self.df_inventory["Unit_Cost"]
        )

        return (
            self.df_inventory
            .groupby("Warehouse_Location")[
                "Inventory_Valuation"
            ]
            .sum()
        )

    def generate_purchase_order_manifest(self):
        purchase_list = self.df_inventory[
            self.df_inventory["Needs_Reorder"]
        ].copy()

        purchase_list["Order_Quantity"] = (
            purchase_list["Reorder_Point"] * 2
            - purchase_list["Current_Stock"]
        )

        return purchase_list





    

inventory_data = {
    "Product_ID": [
        "P101", "P102", "P103",
        "P104", "P105", "P106"
    ],
    "Supplier_ID": [
        "S01", "S02", "S01",
        "S03", "S02", "S03"
    ],
    "Warehouse_Location": [
        "Mumbai", "Pune", "Mumbai",
        "Delhi", "Pune", "Delhi"
    ],
    "Current_Stock": [
        100, 20, 50, 200, 15, 80
    ],
    "Reorder_Point": [
        80, 30, 60, 100, 20, 70
    ],
    "Daily_Burn_Rate": [
        10, 5, 0, 20, 3, 8
    ],
    "Unit_Cost": [
        500, 800, 300, 450, 1000, 600
    ]
}

supplier_data = {
    "Supplier_ID": [
        "S01", "S02", "S03"
    ],
    "Lead_Time_Days": [
        8, 10, 5
    ],
    "Supplier_Contact": [
        "supplier1@email.com",
        "supplier2@email.com",
        "supplier3@email.com"
    ]
}

inventory_df = pd.DataFrame(inventory_data)
suppliers_df = pd.DataFrame(supplier_data)

inventory_optimizer = InventorySupplyChainOptimizer(
    inventory_df,
    suppliers_df
)





print("\n--- Days Of Supply ---")
print(
    inventory_optimizer.calculate_days_of_supply()
)

print("\n--- Reorder Status ---")
print(
    inventory_optimizer.flag_reorder_status()
)

print("\n--- Supplier Lead Times ---")
print(
    inventory_optimizer.merge_supplier_lead_times()
)

print("\n--- Stockout Emergencies ---")
print(
    inventory_optimizer.identify_stockout_emergencies()
)

print("\n--- Warehouse Valuation ---")
print(
    inventory_optimizer.group_valuation_by_warehouse()
)

print("\n--- Purchase Order Manifest ---")
print(
    inventory_optimizer.generate_purchase_order_manifest()
)











# ======
# =======================================================================
# QUESTION 18: Customer Churn Profiler (Telecom / SaaS)
# Concepts: Tenure Binning, One-Hot Encoding, Churn Groupby, Correlation Matrix
# =============================================================================
"""
Scenario:
A telecommunications provider experiences customer cancellations. The churn team 
requires an object-oriented profiling engine to analyze monthly charges, contract 
types, customer service calls, and tenure length to understand churn drivers.

Class Name: CustomerChurnProfiler
Constructor: __init__(self, df_churn)
  - Stores customer retention records in self.df.

Tasks to Implement:
  1. def bin_customer_tenure(self)
     - Bin 'Tenure_Months' using pd.cut() into 3 lifecycle cohorts:
       'New' (0-12 months), 'Established' (13-36 months), 'Loyal' (37+ months).
  2. def one_hot_encode_contract_plans(self)
     - Encode categorical columns like 'Contract_Type' and 'Payment_Method' using 
       pd.get_dummies(..., drop_first=True).
  3. def compute_churn_rates_by_segment(self, segment_col='Contract_Type')
     - Group by segment_col and calculate the churn rate (mean of binary 'Churn' column).
  4. def correlation_with_churn(self)
     - Compute Pearson correlation between all numeric features and the 'Churn' 
       target column, returning them sorted descending.
  5. def isolate_at_risk_cohort(self, min_calls=3, max_tenure=6)
     - Query and extract customers with Customer_Service_Calls >= min_calls AND 
       Tenure_Months <= max_tenure.
  6. def compute_revenue_at_risk(self)
     - Calculate the total monthly recurring revenue (sum of Monthly_Charges) of 
       customers identified as at-risk.
"""

class CustomerChurnProfiler:
    def __init__(self, df_churn):
        pass

    def bin_customer_tenure(self):
        pass

    def one_hot_encode_contract_plans(self):
        pass

    def compute_churn_rates_by_segment(self, segment_col='Contract_Type'):
        pass

    def correlation_with_churn(self):
        pass

    def isolate_at_risk_cohort(self, min_calls=3, max_tenure=6):
        pass

    def compute_revenue_at_risk(self):
        pass


# =============================================================================
# QUESTION 19: Ride-Sharing Fare Analyzer (Urban Mobility)
# Concepts: DateTime Features, Fare-per-KM, IQR Outlier Capping, Pivot Aggregations
# =============================================================================
"""
Scenario:
A ride-hailing startup records trip distance, fare amount, pickup timestamp, 
passenger count, and vehicle category. Build a fare analytics utility to detect 
anomalous rides, extract peak commute windows, and compute route yield.

Class Name: RideSharingFareAnalyzer
Constructor: __init__(self, df_rides)
  - Stores ride records in self.df.

Tasks to Implement:
  1. def extract_pickup_features(self, time_col='pickup_time')
     - Convert time_col to datetime and extract: 'pickup_hour', 'pickup_day', 
       and 'is_rush_hour' (True if hour in [8, 9, 10, 17, 18, 19]).
  2. def compute_fare_per_km(self)
     - Create 'Fare_Per_Km' = Fare_Amount / Trip_Distance_Km.
  3. def cap_fare_outliers_iqr(self)
     - Apply IQR rule on 'Fare_Amount' and clip extreme fare amounts to the upper 
       fence using .clip().
  4. def categorize_trip_distance(self)
     - Use pd.cut() to label trips: 'Short' (0-3 km), 'Medium' (3-10 km), 'Long' (10+ km).
  5. def pivot_fare_by_hour_and_vehicle(self)
     - Generate a pivot table showing mean Fare_Amount with pickup_hour on rows 
       and Vehicle_Type on columns.
  6. def top_revenue_generating_hours(self, top_n=3)
     - Identify the top_n pickup hours that generate the highest total fare revenue.
"""

class RideSharingFareAnalyzer:
    def __init__(self, df_rides):
        pass

    def extract_pickup_features(self, time_col='pickup_time'):
        pass

    def compute_fare_per_km(self):
        pass

    def cap_fare_outliers_iqr(self):
        pass

    def categorize_trip_distance(self):
        pass

    def pivot_fare_by_hour_and_vehicle(self):
        pass

    def top_revenue_generating_hours(self, top_n=3):
        pass


# =============================================================================
# QUESTION 20: Real Estate Valuation Engine (Property Analytics)
# Concepts: Price-per-sqft, Missing Imputation, Correlation Matrix, Min-Max Scaling
# =============================================================================
"""
Scenario:
A real estate valuation platform ingests property listings containing house 
prices, square footage, bedroom count, property age, and neighborhood. Build 
a valuation class that cleans data, engineers unit metrics, and standardizes features.

Class Name: RealEstateValuationEngine
Constructor: __init__(self, df_properties)
  - Stores real estate listings in self.df.

Tasks to Implement:
  1. def clean_and_impute_specs(self)
     - Impute missing values in 'Bedrooms' with mode, and missing 'Square_Feet' 
       with neighborhood-level median.
  2. def derive_unit_pricing(self)
     - Create 'Price_Per_SqFt' = Price / Square_Feet.
  3. def bin_properties_by_size(self)
     - Use pd.qcut() to categorize Square_Feet into 3 equal-frequency tiers: 
       'Compact', 'Medium', 'Spacious'.
  4. def evaluate_price_correlations(self)
     - Return the Pearson correlation between Price and (Square_Feet, Bedrooms, Age_Years).
  5. def scale_features_for_ml(self, feature_cols)
     - Apply Min-Max scaling from scratch ((X - min)/(max - min)) to feature_cols, 
       returning a standardized feature subset.
  6. def find_undervalued_bargains(self, neighborhood, max_price_per_sqft)
     - Query and return properties in neighborhood where Price_Per_SqFt is 
       below max_price_per_sqft.
"""

class RealEstateValuationEngine:
    def __init__(self, df_properties):
        pass

    def clean_and_impute_specs(self):
        pass

    def derive_unit_pricing(self):
        pass

    def bin_properties_by_size(self):
        pass

    def evaluate_price_correlations(self):
        pass

    def scale_features_for_ml(self, feature_cols):
        pass

    def find_undervalued_bargains(self, neighborhood, max_price_per_sqft):
        pass


# =============================================================================
# QUESTION 21: Digital Marketing Campaign Tracker (AdTech Analytics)
# Concepts: CTR/CPC KPIs, Relational Merge, Channel Groupby, Temporal Aggregation
# =============================================================================
"""
Scenario:
A performance marketing agency runs campaigns across Google Ads, Meta, and 
LinkedIn. You are tasked with developing a marketing analytics pipeline class 
that computes key ad efficiency metrics (CTR, CPC, ROAS) and joins spend with sales.

Class Name: DigitalMarketingCampaignTracker
Constructor: __init__(self, df_ad_spend, df_conversions)
  - Ingests df_ad_spend and df_conversions.

Tasks to Implement:
  1. def compute_marketing_kpis(self)
     - Inside df_ad_spend, calculate:
       * 'CTR' (Click-Through Rate) = (Clicks / Impressions) * 100
       * 'CPC' (Cost Per Click) = Total_Spend / Clicks
  2. def merge_spend_and_revenue(self, join_key='Campaign_ID')
     - Merge ad spend with conversions (inner join) to match spend against actual sales revenue.
  3. def calculate_roas(self)
     - Create 'ROAS' (Return on Ad Spend) = Revenue_Generated / Total_Spend.
  4. def aggregate_by_channel(self)
     - Group merged data by 'Channel' (Google, Meta, LinkedIn) and compute total spend, 
       total revenue, and average ROAS.
  5. def filter_underperforming_campaigns(self, min_roas=2.0)
     - Filter campaigns whose ROAS is strictly less than min_roas.
  6. def extract_weekly_performance_trends(self, date_col='Campaign_Date')
     - Convert date_col to datetime and aggregate weekly total revenue and spend.
"""

class DigitalMarketingCampaignTracker:
    def __init__(self, df_ad_spend, df_conversions):
        pass

    def compute_marketing_kpis(self):
        pass

    def merge_spend_and_revenue(self, join_key='Campaign_ID'):
        pass

    def calculate_roas(self):
        pass

    def aggregate_by_channel(self):
        pass

    def filter_underperforming_campaigns(self, min_roas=2.0):
        pass

    def extract_weekly_performance_trends(self, date_col='Campaign_Date'):
        pass


# =============================================================================
# QUESTION 22: Hospitality Booking Manager (Hotel & Tourism)
# Concepts: Lead Time Calculation, Missing Value Imputation, Seasonality, Pivot
# =============================================================================
"""
Scenario:
A hotel chain records reservations, arrival dates, room rates, guest counts, 
and cancellation status. Construct a hospitality analytics class to evaluate 
cancellation trends, lead-time behaviors, and room occupancy rates.

Class Name: HospitalityBookingManager
Constructor: __init__(self, df_bookings)
  - Stores reservation records in self.df.

Tasks to Implement:
  1. def compute_lead_time_days(self, booking_date_col, arrival_date_col)
     - Convert both columns to datetime and compute 'Lead_Time' = (arrival - booking) in days.
  2. def impute_missing_requests(self)
     - Impute missing values in 'Special_Requests' with 0, and missing 'Room_Type' with mode.
  3. def flag_seasonal_stays(self, arrival_date_col)
     - Extract arrival month and create 'Season':
       * 'Winter' (Dec, Jan, Feb), 'Spring' (Mar, Apr, May), 
       * 'Summer' (Jun, Jul, Aug), 'Autumn' (Sep, Oct, Nov).
  4. def pivot_occupancy_by_season_and_room(self)
     - Pivot table showing total nights stayed with Season on rows and Room_Type on columns.
  5. def cancellation_rate_by_deposit_type(self)
     - Group by 'Deposit_Type' (No Deposit, Non Refundable, Refundable) and calculate 
       percentage of bookings cancelled.
  6. def filter_long_lead_cancellations(self, lead_threshold=90)
     - Return reservations that were cancelled AND had a lead time greater than lead_threshold days.
"""

class HospitalityBookingManager:
    def __init__(self, df_bookings):
        pass

    def compute_lead_time_days(self, booking_date_col, arrival_date_col):
        pass

    def impute_missing_requests(self):
        pass

    def flag_seasonal_stays(self, arrival_date_col):
        pass

    def pivot_occupancy_by_season_and_room(self):
        pass

    def cancellation_rate_by_deposit_type(self):
        pass

    def filter_long_lead_cancellations(self, lead_threshold=90):
        pass


# =============================================================================
# QUESTION 23: Streaming Media Analytics (OTT Platform)
# Concepts: Completion Rates, Discretization, Multi-Metric Groupby, Pivot Table
# =============================================================================
"""
Scenario:
An OTT streaming platform logs user viewing sessions across movies, documentaries, 
and web series. Build an engagement analytics class to measure completion rates, 
bucket viewers into engagement personas, and identify binge-watching patterns.

Class Name: StreamingMediaAnalytics
Constructor: __init__(self, df_streams)
  - Stores stream records in self.df.

Tasks to Implement:
  1. def calculate_completion_percentage(self)
     - Create 'Completion_Rate' = (Minutes_Watched / Total_Duration_Minutes) * 100. 
       Cap values at 100.0.
  2. def segment_viewer_engagement(self)
     - Use pd.cut() on Completion_Rate to categorize viewing:
       'Abandoned' (0-20%), 'Casual' (21-60%), 'Engaged' (61-90%), 'Completed' (91-100%).
  3. def genre_engagement_summary(self)
     - Group by 'Genre' and calculate:
       * Total_Streams: count of session IDs
       * Avg_Minutes: mean of Minutes_Watched
       * High_Completion_Count: count of sessions with Completion_Rate >= 90%
  4. def pivot_watch_time_by_device_and_tier(self)
     - Build a pivot table of total Minutes_Watched with Device_Type on rows and 
       Subscription_Tier on columns.
  5. def identify_top_trending_titles(self, top_n=5)
     - Find the top_n content titles with the highest unique viewer count and 
       average completion rate > 75%.
"""

class StreamingMediaAnalytics:
    def __init__(self, df_streams):
        pass

    def calculate_completion_percentage(self):
        pass

    def segment_viewer_engagement(self):
        pass

    def genre_engagement_summary(self):
        pass

    def pivot_watch_time_by_device_and_tier(self):
        pass

    def identify_top_trending_titles(self, top_n=5):
        pass


# =============================================================================
# QUESTION 24: Credit ScoreCard Builder (Banking & Risk Modeling)
# Concepts: Financial Ratios, Ordinal Mapping, IQR Clipping, Z-Score Scaling
# =============================================================================
"""
Scenario:
A commercial bank evaluates loan applicants. You are required to design an 
OOP credit scoring pipeline that derives debt burden ratios, maps credit bands, 
caps extreme balances, and normalizes risk indicators.

Class Name: CreditScoreCardBuilder
Constructor: __init__(self, df_applicants)
  - Stores loan applicant records in self.df.

Tasks to Implement:
  1. def compute_financial_ratios(self)
     - Create 'DTI' (Debt-to-Income Ratio) = Monthly_Debt_Payments / Monthly_Income.
     - Create 'Credit_Utilization' = Outstanding_Balance / Credit_Limit.
  2. def encode_credit_rating_tiers(self, rating_col='Credit_Rating')
     - Map qualitative credit ratings:
       {'Poor': 1, 'Fair': 2, 'Good': 3, 'Very Good': 4, 'Exceptional': 5}.
  3. def cap_debt_outliers_iqr(self, target_col='Outstanding_Balance')
     - Use the IQR fence method to cap extreme balances using .clip().
  4. def standardize_risk_features(self, feature_cols)
     - Apply Z-Score Standardization ((X - Mean) / Std) from scratch to feature_cols.
  5. def evaluate_default_correlations(self, target_col='Has_Defaulted')
     - Return the Pearson correlation of all continuous ratios against target_col.
  6. def assign_credit_approval_status(self)
     - Use .apply() with custom rules:
       Approve if DTI < 0.40 AND Credit_Rating_Encoded >= 3; otherwise Reject.
"""

class CreditScoreCardBuilder:
    def __init__(self, df_applicants):
        pass

    def compute_financial_ratios(self):
        pass

    def encode_credit_rating_tiers(self, rating_col='Credit_Rating'):
        pass

    def cap_debt_outliers_iqr(self, target_col='Outstanding_Balance'):
        pass

    def standardize_risk_features(self, feature_cols):
        pass

    def evaluate_default_correlations(self, target_col='Has_Defaulted'):
        pass

    def assign_credit_approval_status(self):
        pass


# =============================================================================
# QUESTION 25: Omnichannel Retail Pipeline (End-to-End Master Project)
# Concepts: Comprehensive Master Pipeline (All 15 Parts of Pandas Guide Integrated)
# =============================================================================
"""
Scenario:
An international enterprise retailer operates both physical brick-and-mortar stores 
and an online mobile app. You are required to engineer an end-to-end master analytics 
class combining data hygiene, feature engineering, relational joins, scaling, 
outlier capping, datetime extraction, and pivot table executive dashboards.

Class Name: OmnichannelRetailPipeline
Constructor: __init__(self, df_customers, df_orders, df_products)
  - Stores the three relational DataFrames.

Tasks to Implement:
  1. def clean_and_impute_datasets(self)
     - Check and impute missing customer ages with median, missing product categories 
       with mode, and drop orders with missing Order_ID or Customer_ID.
  2. def relational_three_way_merge(self)
     - Merge df_orders with df_customers on 'Customer_ID' (inner), then merge 
       with df_products on 'Product_ID' (inner) into self.df_master.
  3. def engineer_transaction_metrics(self)
     - On self.df_master:
       * Calculate 'Total_Cost' = Quantity * Unit_Price.
       * Calculate 'Net_Margin' = Total_Cost - (Quantity * Wholesale_Cost).
       * Extract Order_Year, Order_Month, and Is_Weekend from Order_Date.
  4. def treat_outliers_and_scale(self)
     - Detect and cap Total_Cost outliers using IQR clipping.
     - Create a Min-Max scaled feature for Net_Margin.
  5. def encode_channel_and_bin_spend(self)
     - One-hot encode 'Order_Channel' (Store, Web, Mobile App) with drop_first=True.
     - Discretize Total_Cost into 3 spending tiers: 'Bronze', 'Silver', 'Gold' using pd.qcut().
  6. def build_executive_kpi_dashboard(self)
     - Return a multi-dimensional pivot table displaying Total Net_Margin and Mean Order Value 
       with Store_Region on rows and Order_Channel on columns, including margins=True (Grand Totals).
"""

class OmnichannelRetailPipeline:
    def __init__(self, df_customers, df_orders, df_products):
        pass

    def clean_and_impute_datasets(self):
        pass

    def relational_three_way_merge(self):
        pass

    def engineer_transaction_metrics(self):
        pass

    def treat_outliers_and_scale(self):
        pass

    def encode_channel_and_bin_spend(self):
        pass

    def build_executive_kpi_dashboard(self):
        pass


# =============================================================================
# END OF ASSIGNMENT: 25 OOP PANDAS QUESTIONS
# =============================================================================
