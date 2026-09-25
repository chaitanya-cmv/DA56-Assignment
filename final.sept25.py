import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# ============================================================
# STEP 1: LOADING THE TAXIS DATASET
# ============================================================

df = sns.load_dataset("taxis")
print("Dataset Shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nColumn Info:\n")
df.info()


# ============================================================
# STEP 2: HANDLING MISSING VALUES
# ============================================================

print("\n--- Missing Values Before Cleaning ---")
print(df.isnull().sum())

# Numerical columns: impute using median (robust to outliers, common for fare/tip data)
numerical_cols = ['fare', 'tip', 'tolls', 'total', 'distance']
for col in numerical_cols:
    if col in df.columns and df[col].isnull().sum() > 0:
        median_value = df[col].median()
        df[col] = df[col].fillna(median_value)
        print(f"Filled missing values in '{col}' with median: {median_value}")

# Categorical columns: impute using mode (most frequent value)
categorical_cols = ['payment', 'pickup_zone', 'dropoff_zone', 'pickup_borough', 'dropoff_borough']
for col in categorical_cols:
    if col in df.columns and df[col].isnull().sum() > 0:
        mode_value = df[col].mode()[0]
        df[col] = df[col].fillna(mode_value)
        print(f"Filled missing values in '{col}' with mode: {mode_value}")

# Critical columns (e.g., pickup/dropoff timestamps) cannot be reasonably imputed
# since a fabricated timestamp would distort time-based analysis - drop these rows instead
critical_cols = ['pickup', 'dropoff']
before_rows = df.shape[0]
df = df.dropna(subset=critical_cols)
after_rows = df.shape[0]
print(f"\nDropped {before_rows - after_rows} rows with missing critical timestamp data.")

print("\n--- Missing Values After Cleaning ---")
print(df.isnull().sum())


# ============================================================
# STEP 3: VISUALIZATIONS USING MATPLOTLIB / PANDAS PLOT
# ============================================================

# Convert pickup column to datetime format
df['pickup'] = pd.to_datetime(df['pickup'])

# ---------- Line Chart: Fare over time ----------
df_sorted = df.sort_values('pickup')
plt.figure(figsize=(12, 5))
plt.plot(df_sorted['pickup'], df_sorted['fare'], linewidth=0.8, color='steelblue')
plt.title("Fare Over Time")
plt.xlabel("Pickup Timestamp")
plt.ylabel("Fare ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------- Bar Chart: Total fare per pickup_borough ----------
fare_by_borough = df.groupby('pickup_borough')['fare'].sum().sort_values(ascending=False)
plt.figure(figsize=(8, 5))
fare_by_borough.plot(kind='bar', color='coral')
plt.title("Total Fare by Pickup Borough")
plt.xlabel("Pickup Borough")
plt.ylabel("Total Fare ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------- Pie Chart: Distribution of trips by payment method ----------
payment_counts = df['payment'].value_counts()
plt.figure(figsize=(7, 7))
plt.pie(payment_counts, labels=payment_counts.index, autopct='%1.1f%%', startangle=90,
        colors=sns.color_palette('pastel'))
plt.title("Distribution of Trips by Payment Method")
plt.tight_layout()
plt.show()

# ---------- Histogram: Distribution of distance ----------
plt.figure(figsize=(8, 5))
plt.hist(df['distance'], bins=30, color='seagreen', edgecolor='black')
plt.title("Distribution of Trip Distance")
plt.xlabel("Distance (miles)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()

# ---------- Box Plot: Tip amounts by pickup_borough ----------
plt.figure(figsize=(9, 5))
df.boxplot(column='tip', by='pickup_borough', grid=False)
plt.title("Distribution of Tip Amount by Pickup Borough")
plt.suptitle("")  # removes default pandas subtitle
plt.xlabel("Pickup Borough")
plt.ylabel("Tip ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


# ============================================================
# VISUALIZATIONS USING SEABORN
# ============================================================

# ---------- Count Plot: Number of trips per pickup_borough ----------
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='pickup_borough', order=df['pickup_borough'].value_counts().index,
              palette='viridis')
plt.title("Number of Trips per Pickup Borough")
plt.xlabel("Pickup Borough")
plt.ylabel("Count of Trips")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------- Scatter Plot: Distance vs Fare, colored by borough ----------
plt.figure(figsize=(9, 6))
sns.scatterplot(data=df, x='distance', y='fare', hue='pickup_borough', alpha=0.6)
plt.title("Distance vs Fare (Colored by Pickup Borough)")
plt.xlabel("Distance (miles)")
plt.ylabel("Fare ($)")
plt.legend(title='Pickup Borough', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()

# ---------- Heatmap: Correlation between numerical variables ----------
corr_cols = ['distance', 'fare', 'tip', 'tolls', 'total']
corr_matrix = df[corr_cols].corr()
plt.figure(figsize=(7, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
plt.title("Correlation Heatmap of Numerical Variables")
plt.tight_layout()
plt.show()

# ---------- Pair Plot: distance, fare, tip, total - colored by pickup_zone ----------
# Note: pickup_zone often has many unique categories, which can make the legend large.
# Consider limiting to top N zones if the plot becomes too cluttered.
pairplot_cols = ['distance', 'fare', 'tip', 'total', 'pickup_zone']
top_zones = df['pickup_zone'].value_counts().nlargest(5).index
df_top_zones = df[df['pickup_zone'].isin(top_zones)]

sns.pairplot(df_top_zones[pairplot_cols], hue='pickup_zone', diag_kind='hist')
plt.suptitle("Pairwise Relationships Colored by Pickup Zone (Top 5 Zones)", y=1.02)
plt.show()

# ---------- Violin Plot: Fare distribution by payment method ----------
plt.figure(figsize=(8, 5))
sns.violinplot(data=df, x='payment', y='fare', palette='muted')
plt.title("Fare Distribution by Payment Method")
plt.xlabel("Payment Method")
plt.ylabel("Fare ($)")
plt.tight_layout()
plt.show()