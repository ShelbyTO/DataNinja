# DataNinja Package

## Overview
`DataNinja` is an all-in-one data analysis toolkit designed to simplify data manipulation, statistical analysis, and visualization. It integrates popular libraries like `pandas`, `numpy`, `matplotlib`, and others into a single package, making it easier for data analysts and scientists to perform common data tasks.

## Features
- **DataFrame Creation:** Create DataFrames with ease.
- **Statistics Calculation:** Compute basic statistics such as mean, median, variance, and standard deviation.
- **Data Profiling:** Generate comprehensive data profile reports.
- **Missing Data Visualization:** Visualize missing data patterns in your DataFrame.
- **Missing Value Handling:** Handle missing values using different methods.
- **Visualization:** Create various plots to analyze and visualize your data.

## Installation
To install the `DataNinja` package, use pip:

```
pip install dataninja
```

## Usage
1. DataFrame Creation
Create a DataFrame using the create_dataframe function:

```
import dataninja

data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, None, 4]
}

df = dataninja.create_dataframe(data)
print(df)
```

2. Statistics Calculation
Calculate basic statistics using the calculate_statistics function:

```
# Assuming df is already created
stats = dataninja.calculate_statistics(df)
print(stats)
```

3. Data Profiling
Generate a data profile report using the generate_data_profile function. This can be rendered in Jupyter Notebooks:

```
# Assuming df is already created
report = dataninja.generate_data_profile(df)
report.to_notebook_iframe()  # For Jupyter Notebooks
```

4. Missing Data Visualization
Visualize missing data patterns with the plot_missing_data function:

```
# Assuming df is already created
dataninja.plot_missing_data(df)
```

5. Missing Value Handling
Fill missing values using different methods:

```
# Assuming df is already created
df_filled = dataninja.fill_missing_values(df, method='mean')
print(df_filled)
```

## Example
Here’s a complete example of using the DataNinja package:

```
import dataninja

# Create a DataFrame
data = {
    'A': [1, 2, None, 4],
    'B': [None, 2, 3, 4],
    'C': [1, None, None, 4]
}
df = dataninja.create_dataframe(data)

# Calculate statistics
stats = dataninja.calculate_statistics(df)
print("Statistics:\n", stats)

# Generate data profile report
report = dataninja.generate_data_profile(df)
report.to_notebook_iframe()  # For Jupyter Notebooks

# Visualize missing data
dataninja.plot_missing_data(df)

# Fill missing values
df_filled = dataninja.fill_missing_values(df, method='mean')
print("Filled DataFrame:\n", df_filled)
```

## Development
To contribute to the DataNinja package:

1. Clone the Repository:

```
<<<<<<< HEAD
git clone https://github.com/YourUsername/DataNinja.git
=======
git clone https://github.com/ShelbyTO/DataNinja.git
>>>>>>> dd9f3b2 (Initial commit)
```

2. Navigate to the Project Directory:

```
cd DataNinja
```

3. Install Dependencies:

```
pip install -r requirements.txt
```

4. Run Tests:

```
pytest
```

5. Make Your Changes and submit a pull request.

## License
This package is licensed under the MIT License. See the LICENSE file for details.

## Contact
For any issues or questions, please contact:

Author: Nicolas Prieur
<<<<<<< HEAD
Email: prieur.nicolas@outlook.com

=======
Email: pu-zle@live.fr
>>>>>>> dd9f3b2 (Initial commit)
