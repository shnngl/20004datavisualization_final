
# The Development of MLB Team Performance

## Live Dashboard
 [Click here](https://20004datavisualizationfinal-shnngl.streamlit.app/) 

## Project Overview

As highlighted in the film *Moneyball* discussed in class, the use of statistics has significantly reshaped the game of baseball. I was fascinated by how extensively baseball has been quantified when I first began learning about it. For this reason, I believe baseball data serves as an excellent dataset for data visualization.

This project demonstrates interactive visualizations of MLB team performance data using Streamlit. 
Visualization 1: Dual-axis Line and Bar Chart
Visualization 2: Animated Quadrant Scatter Plot 


## Data Management
### Data Source
- [SABR Lahman Baseball Database](https://sabr.org/lahman-database/)  
> The Lahman Baseball Database, created by SABR member Sean Lahman, contains complete batting and pitching statistics back to 1871, plus fielding statistics, standings, team stats, managerial records, postseason data, and more.
> 
> Lahman’s database allows baseball researchers to perform complex queries across the entire history of the game. The Lahman Baseball Database has served as the foundation for many popular baseball research projects and simulation games, including Out of the Park Baseball and Baseball Mogul.

### Data Cleaning Process
1. Determine relevant raw datasets for my purpose of analysis:
    - player statistics (Available in Batting.csv) 
    - team statistics (Available in Teams.csv)
2. Select usable columns from the data set
    - Columns ('playerID', 'yearID', 'teamID', 'HR', 'H', 'AB', 'RBI') from Batting.csv
    - Columns ('yearID', 'teamID', 'franchID', 'R', 'RA') from Teams.csv
3. Drop missing values rows of usable data to avoid errors during calculation
4. Calculate custom metrics
    - Average RBI per Game: total RBI / games played in that year
    - RBI Contribution Rate: Team's runs scored (R) / (runs scored (R) + runs allowed (RA))

### Sampling methodology
Several important data cleaning decisions are made particularly for Visualization 2 to maximize its designing purpose to between-team comparison:
1. Selecting the Start Year based on the start of modern MLB format.
    I found out that data in the early stage after 1871 ranges way different from the data in the last one hundred years. Therefore I looked back on the history and determined the year to start for this plot.
2. Filtering MLB teams to current MLB Franchises only, excluding defunct teams and short-lived franchises.

---

## Methodology
### Rationale for visualization selection
1. **Dual-axis Line and Bar Chart** 

I believe that home runs reflect the increasing emphasis on individual power in baseball, while the batting average represents a more stable measure of a team's overall offensive performance. In an era where home runs have become a dominant factor, analyzing how these two metrics have evolved could provide insight into whether the balance between individual strength and team coordination still plays a decisive role in the game. 

2. **Animated Quadrant Scatter Plot** – To reveal correlations between variables.  

The x-axis represents the average RBI per game, which serves as a measure of a team's overall offensive productivity. The y-axis reflects the RBI contribution rate, capturing how efficiently a team converts scoring opportunities into runs. The chart is divided into four quadrants, allowing for the classification of teams into distinct strategic archetypes based on their offensive productivity and efficiency. An animation slider is included to track changes over time, providing insight into how teams’ strategies and performance have evolved.


---

## Critical Analysis
### Limitations:
- Using RBI to measure Offensive efficiency is incomplete as the overall offensive efficiency is complex and influenced by other factors like on-base percentage or slugging percentages as well.
- The quadrant chart assumes that high RBI production and high contribution rate are universally positive, whre in reallife cases there are teams actively adopt defensive strategies for winning as well. 
- The four quadrant are roughly defined by the mean, which might not be the best selection. 

### Future Improvements:
- Contextualize with rule changes and structural shifts during the history of MLB development to better understand what is going on behind the shifting of data.
- Adding more factors to make the offensive metrics more universal

