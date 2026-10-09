 House Price Prediction using Machine Learning

A simple Machine Learning project that predicts the price of a house based on its **area in square feet**.

The project uses **Linear Regression** and is implemented using **Python and Jupyter Notebook**.

## Project Overview

House prices generally increase as the size of the house increases. In this project, we train a Linear Regression model using historical house area and price data.

The trained model can then predict the estimated price of a house when the user provides its area.

### Example

```text
Input:
House Area = 1200 sq ft

Output:
Predicted House Price = Rs. 10,600,000
```

## Objectives

- Understand the basics of Machine Learning.
- Learn how Linear Regression works.
- Create a dataset containing house areas and prices.
- Train a Machine Learning model.
- Predict house prices based on area.
- Visualize the relationship between area and price.

## Technologies Used

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Scikit-learn

## Project Structure

```text
house-price-prediction/
│
├── House_Price_Prediction.ipynb
├── data.csv
└── README.md
```

## Dataset

The dataset contains two main columns:
<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/5e276674-5650-4260-871e-17449a090d7b" />



## Machine Learning Algorithm

This project uses **Linear Regression**.

The basic Linear Regression equation is:

```text
y = mx + b
```

For this project:

```text
Price = (Coefficient × Area) + Intercept
```

Where:

- `Price` = predicted house price
- `Area` = house area in square feet
- `Coefficient` = price change for each additional square foot
- `Intercept` = base value learned by the model

## Machine Learning Workflow

```text
Collect Data
     ↓
Load Dataset
     ↓
Explore Data
     ↓
Visualize Data
     ↓
Separate Features and Target
     ↓
Create Linear Regression Model
     ↓
Train Model
     ↓
Make Predictions
     ↓
Evaluate / Visualize Results
```

## Visualization

The project creates a scatter plot showing the relationship between:

```text
House Area → House Price
```

It also displays the Linear Regression prediction line.

## How to Run

### 1. Install Python

Make sure Python is installed on your computer.

### 2. Install required libraries

Open your terminal and run:

```bash
pip install pandas numpy matplotlib scikit-learn jupyter
```

### 3. Start Jupyter Notebook

```bash
jupyter notebook
```

### 4. Open the notebook

Open:

```text
House_Price_Prediction.ipynb
```

### 5. Run the cells

Run each notebook cell from top to bottom.

## Prediction Example

The user can enter the house area:

```python
area = float(input("Enter house area in square feet: "))

prediction = model.predict([[area]])

print(f"Estimated House Price: Rs. {prediction[0]:,.2f}")
```

Example:

```text
Enter house area in square feet: 1200

Estimated House Price: Rs. 10,600,000.00
```

##  Key Concepts Learned

Through this project, you can learn:

- Dataset creation
- DataFrames
- Features and targets
- Data visualization
- Linear Regression
- Model training
- Model prediction
- Coefficient
- Intercept
- Basic Machine Learning workflow

## Future Improvements

The current model uses only **house area**. It can be improved by adding more features such as:

- Number of bedrooms
- Number of bathrooms
- Location
- Number of floors
- House age
- Parking availability
- Distance to city
- Land size

A more advanced version could use multiple features:

```text
Area
Bedrooms
Bathrooms
Location
House Age
      ↓
Machine Learning Model
      ↓
Predicted House Price
```

## Disclaimer

This project is created for **educational and demonstration purposes**. The dataset is a small sample dataset and the predictions should not be considered real-world property valuations.
<img width="1920" height="1080" alt="Screenshot From 2026-10-09 09-07-03" src="https://github.com/user-attachments/assets/18d7901b-9463-4a5a-8027-063906f706a9" />


## Author

**Dimalsha Kinkini**

Data Science Undergraduate  
Sri Lanka Technological Campus (SLTC)
