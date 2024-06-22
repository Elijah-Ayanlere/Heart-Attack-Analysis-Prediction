# Heart Attack Analysis & Prediction

## Project Overview

This project aims to analyze and visualize the Heart Attack dataset to uncover patterns and insights. The dataset contains several features related to heart health, and the target variable indicates the occurrence of a heart attack. This analysis includes data cleaning, descriptive statistics, and various visualizations to understand the relationships between features and the likelihood of a heart attack.

## Dataset

The dataset used in this project is `heart.csv`, which contains the following columns:

- `age`: Age of the patient
- `sex`: Gender of the patient (1 = male, 0 = female)
- `cp`: Chest pain type (0: typical angina, 1: atypical angina, 2: non-anginal pain, 3: asymptomatic)
- `trestbps`: Resting blood pressure (in mm Hg)
- `chol`: Serum cholesterol in mg/dl
- `fbs`: Fasting blood sugar > 120 mg/dl (1 = true, 0 = false)
- `restecg`: Resting electrocardiographic results (0: normal, 1: having ST-T wave abnormality, 2: showing probable or definite left ventricular hypertrophy)
- `thalach`: Maximum heart rate achieved
- `exang`: Exercise-induced angina (1 = yes, 0 = no)
- `oldpeak`: ST depression induced by exercise relative to rest
- `slope`: The slope of the peak exercise ST segment (0: upsloping, 1: flat, 2: downsloping)
- `ca`: Number of major vessels (0-3) colored by fluoroscopy
- `thal`: Thalassemia (1: normal, 2: fixed defect, 3: reversible defect)
- `target`: Target variable (1: heart attack, 0: no heart attack)

## Project Structure

- `analysis.py`: Python script containing the data analysis and visualization code.
- `heart.csv`: The dataset file.
- `README.md`: This readme file.

## Setup and Requirements

To run the analysis, you need to have Python installed along with the following libraries:
- numpy
- pandas
- matplotlib
- seaborn

You can install these libraries using pip:

```sh
pip install numpy pandas matplotlib seaborn
```

## Analysis Steps

1. Load the Dataset: Load the dataset using pandas.
2. Display the Dataset: Display the entire dataset, first few rows, and last few rows.
3. Summary Statistics: Calculate and display summary statistics of the dataset.
4. Missing Values: Check for and handle any missing values in the dataset.
5. Data Types: Check the data types of each column.
6. Visualizations:
                    - Age distribution
                    - Heart attack occurrence
                    - Chest pain type distribution
                    - Correlation matrix
                    - Heart attack occurrence by age
                    - Heart attack occurrence by maximum heart rate achieved
                    - Heart attack occurrence by cholesterol level
                    - Boxplot of age by heart attack occurrence

## How to Run the Analysis

1. Ensure you have the dataset heart.csv in the same directory as the analysis.py script.
2. Run the analysis.py script:

```sh
python3 analysis.py
```

## Visualizations

### Age Distribution

### Heart Attack Occurrence

### Chest Pain Type Distribution

### Correlation Matrix

### Heart Attack Occurrence by Age

### Heart Attack Occurrence by Maximum Heart Rate Achieved

### Heart Attack Occurrence by Cholesterol Level

### Age Distribution by Heart Attack Occurrence

## Conclusion

This analysis provides a comprehensive overview of the heart attack dataset. The visualizations help in understanding the relationships between different features and the occurrence of heart attacks. Further analysis and modeling can be done to build predictive models based on this dataset.

For any questions or contributions, feel free to reach out.
