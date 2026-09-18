import numpy as np
import pandas as pd

# ============================================================
# PART 1: NUMPY ARRAY OPERATIONS
# ============================================================

# ---------- Step 1: Create a 1D NumPy Array ----------
temperatures_w1 = np.array([22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9])
print("Week 1 Temperatures:", temperatures_w1)

# ---------- Step 2: Inspection and Properties ----------
print("\n--- Step 2: Inspection ---")
print("Shape:", temperatures_w1.shape)
print("Data type:", temperatures_w1.dtype)
print("Number of elements:", temperatures_w1.size)

# ---------- Step 3: Array Operations ----------
print("\n--- Step 3: Array Operations ---")

# Convert Celsius to Fahrenheit
temperatures_w1_f = (temperatures_w1 * 9/5) + 32
print("Week 1 Temperatures in Fahrenheit:", temperatures_w1_f)

# Max, min, mean
print("Maximum Temperature:", temperatures_w1.max())
print("Minimum Temperature:", temperatures_w1.min())
print("Mean Temperature:", temperatures_w1.mean())

# ---------- Step 4: Array Slicing and Indexing ----------
print("\n--- Step 4: Slicing and Indexing ---")

# First three days
first_three_days = temperatures_w1[0:3]
print("First 3 days:", first_three_days)

# Weekend (last two days)
weekend = temperatures_w1[-2:]
print("Weekend (last 2 days):", weekend)

# Middle three days (index 2, 3, 4)
middle_three_days = temperatures_w1[2:5]
print("Middle 3 days:", middle_three_days)

# ---------- Step 5: Create a 2D Array ----------
print("\n--- Step 5: 2D Array ---")
temperatures = np.array([
    [22.5, 25.3, 20.8, 23.4, 26.1, 24.8, 21.9],  # Week 1
    [19.2, 22.5, 21.3, 24.0, 23.5, 22.8, 20.1]   # Week 2
])
print("2D Temperatures Array:\n", temperatures)

# ---------- Step 6: Inspect and Slice the 2D Array ----------
print("\n--- Step 6: Inspect and Slice 2D Array ---")
print("Shape:", temperatures.shape)
print("Data type:", temperatures.dtype)
print("Total number of elements:", temperatures.size)

# Extract temperatures for each week
week1 = temperatures[0]
week2 = temperatures[1]
print("Week 1:", week1)
print("Week 2:", week2)

# Extract weekends (last two days) for both weeks
weekends_both_weeks = temperatures[:, -2:]
print("Weekends for both weeks:\n", weekends_both_weeks)


# ============================================================
# PART 2: PANDAS SERIES
# ============================================================

# ---------- Step 1: Creating Pandas Series ----------
print("\n\n=== PANDAS SERIES ===")
marks = pd.Series([95, 92, 89, 85, 80],
                   index=['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Rank5'])
print("\nMarks Series:\n", marks)

# ---------- Step 2: Indexing and Slicing ----------
print("\n--- Indexing and Slicing ---")

# Integer index position to access mark of 1st rank student
first_rank_mark = marks.iloc[0]
print("1st Rank student's mark (integer position):", first_rank_mark)

# loc accessor - top 3 ranks by index labels
top_3_ranks = marks.loc[['Rank1', 'Rank2', 'Rank3']]
print("Top 3 ranks (using loc):\n", top_3_ranks)

# iloc accessor - mark of 3rd rank student
third_rank_mark = marks.iloc[2]
print("3rd Rank student's mark (using iloc):", third_rank_mark)

# Boolean mask - ranks with marks greater than 90
high_scorers = marks[marks > 90]
print("Ranks with marks greater than 90:\n", high_scorers)

# ---------- Step 3: Manipulating Series ----------
print("\n--- Manipulating Series ---")

# Modify mark of 1st rank student to 100
marks['Rank1'] = 100
print("After modifying Rank1's mark to 100:\n", marks)

# Remove the entry corresponding to the last rank
marks = marks.drop('Rank5')
print("\nAfter removing Rank5:\n", marks)

# Compute CGPA by dividing each mark by 10
cgpa = marks / 10
print("\nCGPA (marks / 10):\n", cgpa)


# ============================================================
# PART 3: PANDAS DATAFRAME
# ============================================================

# ---------- Step 1: Creating Pandas DataFrame ----------
print("\n\n=== PANDAS DATAFRAME ===")
transactions = pd.DataFrame({
    'TransactionID': [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    'ProductCategory': ['Electronics', 'Clothing', 'Electronics', 'Furniture',
                         'Clothing', 'Electronics', 'Furniture', 'Clothing',
                         'Furniture', 'Electronics'],
    'Region': ['North', 'South', 'North', 'East', 'West',
               'North', 'East', 'West', 'South', 'North'],
    'Amount': [200, 150, 300, 450, 200, 250, 300, 180, 350, 400]
})
print("\nTransactions DataFrame:\n", transactions)

# ---------- Step 2: Data Exploration ----------
print("\n--- Data Exploration ---")

print("\nHead (first 5 rows):\n", transactions.head())
print("\nTail (last 5 rows):\n", transactions.tail())
print("\nShape:", transactions.shape)
print("\nColumn names:", transactions.columns.tolist())
print("\nData types:\n", transactions.dtypes)

# Display only 'ProductCategory' and 'Amount' columns
print("\nProductCategory and Amount columns:\n",
      transactions[['ProductCategory', 'Amount']])

# Retrieve the last 3 columns using iloc
last_3_columns = transactions.iloc[:, -3:]
print("\nLast 3 columns (using iloc):\n", last_3_columns)

# Filter rows where Region is 'North' and Amount > 200
north_high_amount = transactions[(transactions['Region'] == 'North') &
                                  (transactions['Amount'] > 200)]
print("\nRows where Region is North and Amount > 200:\n", north_high_amount)

# Value counts for 'ProductCategory'
category_counts = transactions['ProductCategory'].value_counts()
print("\nValue counts for ProductCategory:\n", category_counts)

# Unique values in 'Region'
unique_regions = transactions['Region'].unique()
print("\nUnique values in Region:", unique_regions)

# Group by 'Region' and find mean amount
mean_amount_by_region = transactions.groupby('Region')['Amount'].mean()
print("\nMean Amount by Region:\n", mean_amount_by_region)

# ---------- Step 3: Manipulating the DataFrame ----------
print("\n--- Manipulating the DataFrame ---")

# Modify Amount for TransactionID 102 to 165
transactions.loc[transactions['TransactionID'] == 102, 'Amount'] = 165
print("\nAfter modifying Amount for TransactionID 102:\n", transactions)

# Add a new column 'Discount' - 10% of Amount
transactions['Discount'] = transactions['Amount'] * 0.10
print("\nAfter adding Discount column:\n", transactions)

# Remove the row with TransactionID 109
transactions = transactions[transactions['TransactionID'] != 109]
print("\nAfter removing TransactionID 109:\n", transactions)

# Delete the 'Discount' column
transactions = transactions.drop(columns=['Discount'])
print("\nAfter deleting Discount column:\n", transactions)