# TV-Show-Popularity-Prediction-using-ML

# README: Data Analysis and Visualization of FlixPatrol Dataset

This project focuses on analyzing and visualizing the FlixPatrol dataset to explore trends, distributions, and correlations among various attributes such as watchtime, genres, and premiere year. Additionally, a linear regression model can be developed for prediction tasks.

---

## **Table of Contents**
1. [Installation](#installation)
2. [Dataset](#dataset)
3. [Project Workflow](#project-workflow)
4. [Visualizations](#visualizations)
5. [Dependencies](#dependencies)
6. [Usage](#usage)

---

## **Installation**

### **1. Clone the Repository**
```bash
git clone <repository_url>
cd <repository_directory>
```

### **2. Install Dependencies**
Install the required Python packages:
```bash
pip install -r requirements.txt
```

---

## **Dataset**

The dataset `flixpatrol.csv` is expected to contain information about movies and TV shows, including attributes like:
- `Title`: The name of the show/movie.
- `Genre`: The genre classification.
- `Premiere`: The premiere year.
- `Watchtime`: Total watch time (in millions).

Ensure the dataset is available in the project directory.

---

## **Project Workflow**

### **1. Data Loading**
The dataset is loaded using `pandas` and processed for analysis:
```python
df = pd.read_csv('flixpatrol.csv')
```

### **2. Data Cleaning**
- Convert the `Watchtime` column to numeric format after removing commas.
- Remove rows with missing or empty values in `Watchtime` and `Genre`.

### **3. Data Visualization**
Multiple visualizations are created using `matplotlib` and `seaborn`:
- Boxplot of `Watchtime` by `Genre`.
- Top 10 shows by `Watchtime`.
- Scatterplot of `Premiere` vs `Watchtime`.
- Countplot of shows by `Genre`.
- Correlation heatmap for numeric columns.

### **4. Machine Learning Preparation**
- Linear regression is set up to predict `Watchtime` using relevant features.

---

## **Visualizations**

### **Key Visualizations**
1. **Boxplot**: Distribution of watchtime across genres.
2. **Bar Plot**: Top 10 shows based on watchtime.
3. **Scatterplot**: Relationship between premiere year and watchtime, categorized by genre.
4. **Count Plot**: Number of shows per genre.
5. **Heatmap**: Correlation matrix of numerical features.
6. **Histogram**: Distribution of watchtime.
7. **Violin Plot**: Spread of watchtime across genres.
8. **Line Plot**: Average watchtime over years.

---

## **Dependencies**

The project uses the following Python libraries:
- `numpy`: For numerical computations.
- `pandas`: For data manipulation and analysis.
- `seaborn`: For statistical data visualization.
- `matplotlib`: For generating plots.
- `scikit-learn`: For machine learning tasks such as regression.
- `google.colab`: For file uploads (optional).

---

## **Usage**

1. **Run the Script**
   Execute the Python script in your preferred environment:
   ```bash
   python script_name.py
   ```

2. **Visualizations**
   Explore the generated plots to understand the data trends and distributions.

3. **Future Predictions**
   Integrate the linear regression model for predicting watchtime or other insights.

---

## **Notes**
- Ensure the dataset `flixpatrol.csv` is in the same directory as the script.
- Replace missing or incomplete data with appropriate preprocessing steps before proceeding with analysis.

For any issues or suggestions, feel free to reach out!
