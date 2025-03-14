
# The Development of MLB Team Performance


## Project Overview

As highlighted in the film *Moneyball* discussed in class, the use of statistics has significantly reshaped the game of baseball. I was fascinated by how extensively baseball has been quantified when I first began learning about it. For this reason, I believe baseball data serves as an excellent dataset for data visualization.

This project demonstrates interactive visualizations of MLB team performance data using Streamlit. 



## Live Dashboard
 [Click here to view the Streamlit app](https://20004datavisualizationfinal-shnngl.streamlit.app/) 



## Data Management
### Data Source
- [SABR Lahman Baseball Database](https://sabr.org/lahman-database/)  
> The Lahman Baseball Database, created by SABR member Sean Lahman, contains complete batting and pitching statistics back to 1871, plus fielding statistics, standings, team stats, managerial records, postseason data, and more.
> 
> Lahman’s database allows baseball researchers to perform complex queries across the entire history of the game. The Lahman Baseball Database has served as the foundation for many popular baseball research projects and simulation games, including Out of the Park Baseball and Baseball Mogul.

### Data Cleaning
- Outliers were removed using the IQR (Interquartile Range) method.  
- Missing values were handled using interpolation.  

### Sampling Methodology
- A stratified sampling method was applied to balance data distribution.  

---

## Methodology
### Why These Visualization Techniques?
1. **Line chart** – To show trends over time.  
2. **Scatter plot** – To reveal correlations between variables.  
3. **Interactive elements** – Hover and zoom functions enhance data exploration.  

---

## Visualizations
Below are examples of the visualizations generated from the data:

### 1. Trend Over Time
- Line chart showing how the values change over time.  
![Trend Over Time](./images/visualization1.png)

---

### 2. Correlation Between Variables
- Scatter plot demonstrating the correlation between variables.  
![Correlation](./images/visualization2.png)

---

## Critical Analysis
### Limitations:
- The dataset is limited in size, which may reduce predictive accuracy.  
- Possible bias in the data collection process.  

### Future Improvements:
- Incorporate additional data sources to increase dataset size.  
- Use more advanced machine learning models to improve predictions.  

---

## Directory Structure
```text
my-streamlit-app
├── data               # Source data
├── images             # Generated plots and screenshots
├── scripts            # Data processing scripts
├── app.py             # Streamlit application
├── requirements.txt   # Dependencies
├── README.md          # Project documentation
---


