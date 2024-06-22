# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
heart_data = pd.read_csv('/home/develijah/Data Analysis Project/Heart Attack Analysis & Prediction/archive/heart.csv')  

# Display the entire dataset (be cautious with large datasets)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
print("Entire dataset:")
print(heart_data)

# Reset display options to default
pd.reset_option('display.max_rows')
pd.reset_option('display.max_columns')

# Display the first few rows of the dataset
print("First few rows of the dataset:")
print(heart_data.head())

# Display the last few rows of the dataset
print("Last few rows of the dataset:")
print(heart_data.tail())

# Display column names to ensure we are using the correct ones
print("\nColumn names in the dataset:")
print(heart_data.columns)

# Display summary statistics
print("\nSummary statistics of the dataset:")
print(heart_data.describe())

# Check for missing values
print("\nMissing values in each column:")
print(heart_data.isnull().sum())

# Check data types
print("\nData types of each column:")
print(heart_data.dtypes)

# Handle missing values if any (example: fill with median or drop rows/columns)
# (The dataset typically doesn't have missing values, but this is an example)
# heart_data.fillna(heart_data.median(), inplace=True)

# Verify cleaning
print("\nMissing values after cleaning:")
print(heart_data.isnull().sum())

# Descriptive statistics
print("\nUpdated summary statistics of the dataset:")
print(heart_data.describe())

# Visualize the distribution of age
plt.figure(figsize=(10, 6))
plt.hist(heart_data['age'], bins=30, edgecolor='black')
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()

# Visualize the target variable (heart attack occurrence)
plt.figure(figsize=(10, 6))
sns.countplot(x='target', data=heart_data)
plt.title('Heart Attack Occurrence')
plt.xlabel('Heart Attack')
plt.ylabel('Count')
plt.show()

# Visualize chest pain type distribution
plt.figure(figsize=(10, 6))
sns.countplot(x='cp', data=heart_data)
plt.title('Chest Pain Type Distribution')
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.show()

# Visualize correlation matrix
plt.figure(figsize=(12, 8))
corr_matrix = heart_data.corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()

# Additional analysis: Heart attack occurrence by age
plt.figure(figsize=(10, 6))
sns.histplot(data=heart_data, x='age', hue='target', multiple='stack')
plt.title('Heart Attack Occurrence by Age')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Additional analysis: Heart attack occurrence by maximum heart rate achieved
plt.figure(figsize=(10, 6))
sns.histplot(data=heart_data, x='thalach', hue='target', multiple='stack', bins=30)
plt.title('Heart Attack Occurrence by Maximum Heart Rate Achieved')
plt.xlabel('Maximum Heart Rate Achieved')
plt.ylabel('Count')
plt.show()

# Additional analysis: Heart attack occurrence by cholesterol level
plt.figure(figsize=(10, 6))
sns.histplot(data=heart_data, x='chol', hue='target', multiple='stack', bins=30)
plt.title('Heart Attack Occurrence by Cholesterol Level')
plt.xlabel('Cholesterol Level')
plt.ylabel('Count')
plt.show()

# Additional analysis: Boxplot of age by heart attack occurrence
plt.figure(figsize=(10, 6))
sns.boxplot(x='target', y='age', data=heart_data)
plt.title('Age Distribution by Heart Attack Occurrence')
plt.xlabel('Heart Attack')
plt.ylabel('Age')
plt.show()
