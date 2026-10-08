import pandas as pd

# ============================================
# 1. Load the raw dataset
# ============================================

data = pd.read_csv("/home/kinkini/house-price-prediction/dataset/Housing.csv")

print("Columns in the dataset:")
print(data.columns)
print("================================")

print("\nData types of each column:")
print(data.dtypes)
print("================================")

print("\nOriginal dataset:")
print(data.head())
print("================================")


# ============================================
# 2. Check missing values
# ============================================

print("\nMissing values:")
print(data.isnull().sum())
print("================================")


# ============================================
# 3. Remove duplicate rows
# ============================================

data = data.drop_duplicates()

print("\nDataset after removing duplicates:")
print(data.head())
print("================================")


# ============================================
# 4. Remove invalid values
# ============================================

data = data[data["price"] > 0]
data = data[data["area"] > 0]
data = data[data["bedrooms"] > 0]
data = data[data["bathrooms"] > 0]
data = data[data["stories"] > 0]
data = data[data["parking"] >= 0]


# ============================================
# 5. Check dataset after cleaning
# ============================================

print("\nDataset after cleaning:")
print(data.head())
print("================================")

print("\nDataset shape:")
print(data.shape)
print("================================")


# ============================================
# 6. Save cleaned dataset
# ============================================

data.to_csv(
    "dataset/houses_clean.csv",
    index=False
)

print("\nCleaned dataset saved successfully!")
print("File: dataset/houses_clean.csv")