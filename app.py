import pandas as pd
import streamlit as st
import plotly.express as px
import datetime 
import plotly.graph_objects as go
import base64

file_path_batting = 'lahman_1871-2023_csv/Batting.csv'
file_path_teams = 'lahman_1871-2023_csv/Teams.csv'

df = pd.read_csv(file_path_batting)
df2 = pd.read_csv(file_path_teams)

df2['team'] = df2['franchID']
df['team'] = df['teamID']
df['avg_rbi_per_game'] = df['R'] / df['G']
df['batting_average'] = df['H'] / df['AB']

teams_count = df2['team'].value_counts()
valid_teams = teams_count[teams_count >= 5].index
filtered_df = df2[df2['team'].isin(valid_teams)]

merged_df = pd.merge(df, df2, on=['yearID', 'teamID'], how='inner')

merged_df.rename(columns={
    'R_x': 'R',
    'RA_y': 'RA',
    'HR_x': 'HR',
    'team_x': 'team',
    'H_x': 'H',
    'AB_x': 'AB'
}, inplace=True)

merged_df['rbi_contribution_rate'] = merged_df['R'] / (merged_df['R'] + merged_df['RA'])

st.set_page_config(layout="wide")
st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

with open('mlb_logo.png', 'rb') as img_file:
    img_base64 = base64.b64encode(img_file.read()).decode()

html_title = f"""
<style>
.title-container {{
    display: flex;
    align-items: center;
    justify-content:center;
}}
.title-container img {{
    width: 100px;
    margin-right: 15px;
}}
.title-test {{
    font-weight:bold;
    padding:5px;
    border-radius:6px;
}}
</style>
<div class="title-container">
    <img src="data:image/png;base64,{img_base64}" alt="MLB Logo">
    <h1 class="title-test">The Development of MLB Team Performance</h1>
</div>
"""
st.markdown("<br>", unsafe_allow_html=True)
st.markdown(html_title, unsafe_allow_html=True)

box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
st.write(f"Last updated by:  {box_date}")

grouped = merged_df.groupby(['yearID', 'team']).agg(
    HR=('HR', 'sum'), 
    H=('H', 'sum'),
    AB=('AB', 'sum')
).reset_index()

grouped = grouped.groupby('yearID').agg(
    HR=('HR', 'sum'),
    H=('H', 'sum'),
    AB=('AB', 'sum')
).reset_index()

grouped['Batting_Average'] = (grouped['H'] / grouped['AB']).round(3)

n_teams_per_year = merged_df.groupby('yearID')['team'].nunique()

grouped['HR_per_team'] = grouped['yearID'].map(n_teams_per_year) 
grouped['HR_per_team'] = grouped['HR'] / grouped['HR_per_team']
grouped['HR_per_team'].fillna(0, inplace=True) 

grouped['HR_per_team'] = grouped['HR_per_team'].round(0).astype(int) 

fig = go.Figure()

fig.add_trace(go.Bar(
    x=grouped['yearID'],
    y=grouped['HR_per_team'],
    name='Home Runs per Team',
    marker_color='lightblue',
    opacity=1
))

fig.add_trace(go.Scatter(
    x=grouped['yearID'],
    y=grouped['Batting_Average'],
    name='Batting Average',
    mode='lines+markers',
    yaxis='y2',
    line=dict(color='darkblue')
))

for year in range(1870, 2030, 20):
    fig.add_shape(
        type="rect",
        x0=year,
        x1=year + 10,
        y0=0,
        y1=1,
        yref="paper",
        fillcolor="#BBBBBB",
        opacity=0.2,
        layer="below",
        line=dict(width=0)
    )

fig.update_layout(
    title="Historical Trends in MLB Team Batting Performance: Contact vs Power (1969–2023)",
    xaxis=dict(title='Year'),
    yaxis=dict(
        title='Home Runs per Team (HR)',
        side='left',
        range=[0, grouped['HR_per_team'].max() * 1.1]
    ),
    yaxis2=dict(
        title='Batting Average (AVG)',
        overlaying='y',
        side='right',
        showgrid=False
    ),
    legend=dict(x=0, y=1.15)
)

st.plotly_chart(fig, use_container_width=True)

st.divider()

modern_mlb_teams = [
    'ARI', 'ATL', 'BAL', 'BOS', 'CHC', 'CHW', 'CIN', 'CLE', 'COL', 'DET',
    'HOU', 'KCR', 'LAA', 'LAD', 'MIA', 'MIL', 'MIN', 'NYM', 'NYY', 'OAK',
    'PHI', 'PIT', 'SDP', 'SEA', 'SFG', 'STL', 'TBR', 'TEX', 'TOR', 'WSN'
]

filtered_team_stats = merged_df[
    (merged_df['team'].isin(modern_mlb_teams)) & 
    (merged_df['yearID'] >= 1969)
]

team_colors = {
    'ARI': '#A71930', 'ATL': '#CE1141', 'BAL': '#DF4601', 'BOS': '#BD3039', 'CHC': '#0E3386', 'CHW': '#27251F',
    'CIN': '#C6011F', 'CLE': '#0C2340', 'COL': '#33006F', 'DET': '#0C2340', 'HOU': '#EB6E1F', 'KCR': '#004687',
    'LAA': '#BA0021', 'LAD': '#005A9C', 'MIA': '#00A3E0', 'MIL': '#12284B', 'MIN': '#002B5C', 'NYM': '#002D72',
    'NYY': '#0C2340', 'OAK': '#003831', 'PHI': '#E81828', 'PIT': '#FDB827', 'SDP': '#2F241D', 'SEA': '#0C2C56',
    'SFG': '#FD5A1E', 'STL': '#C41E3A', 'TBR': '#8FBCE6', 'TEX': '#003278', 'TOR': '#134A8E', 'WSN': '#AB0003'
}

team_names = {
    'ARI': 'Arizona Diamondbacks', 'ATL': 'Atlanta Braves', 'BAL': 'Baltimore Orioles', 'BOS': 'Boston Red Sox',
    'CHC': 'Chicago Cubs', 'CHW': 'Chicago White Sox', 'CIN': 'Cincinnati Reds', 'CLE': 'Cleveland Guardians',
    'COL': 'Colorado Rockies', 'DET': 'Detroit Tigers', 'HOU': 'Houston Astros', 'KCR': 'Kansas City Royals',
    'LAA': 'Los Angeles Angels', 'LAD': 'Los Angeles Dodgers', 'MIA': 'Miami Marlins', 'MIL': 'Milwaukee Brewers',
    'MIN': 'Minnesota Twins', 'NYM': 'New York Mets', 'NYY': 'New York Yankees', 'OAK': 'Oakland Athletics',
    'PHI': 'Philadelphia Phillies', 'PIT': 'Pittsburgh Pirates', 'SDP': 'San Diego Padres', 'SEA': 'Seattle Mariners',
    'SFG': 'San Francisco Giants', 'STL': 'St. Louis Cardinals', 'TBR': 'Tampa Bay Rays', 'TEX': 'Texas Rangers',
    'TOR': 'Toronto Blue Jays', 'WSN': 'Washington Nationals'
}

team_stats = filtered_team_stats.groupby(['yearID', 'team']).agg(
    avg_rbi_per_game=('avg_rbi_per_game', 'mean'),
    rbi_contribution_rate=('rbi_contribution_rate', 'mean')
).reset_index()

team_stats['team_full'] = team_stats['team'].map(team_names)
team_stats['color'] = team_stats['team'].map(team_colors)

team_stats = team_stats.sort_values(by='yearID')

mean_rbi = team_stats['avg_rbi_per_game'].mean()
mean_contribution = team_stats['rbi_contribution_rate'].mean()

x_min = team_stats['avg_rbi_per_game'].min() * 0.95
x_max = team_stats['avg_rbi_per_game'].max() * 1.05
y_min = team_stats['rbi_contribution_rate'].min() * 0.95
y_max = team_stats['rbi_contribution_rate'].max() * 1.05

fig = px.scatter(
    team_stats,
    x='avg_rbi_per_game',
    y='rbi_contribution_rate',
    text='team', 
    animation_frame='yearID', 
    color='team_full', 
    hover_name='team_full', 
    color_discrete_map=team_colors,
    size_max=20
)

fig.add_shape(
    type="rect",
    x0=mean_rbi, x1=x_max, y0=mean_contribution, y1=y_max,
    fillcolor="rgba(230, 57, 70, 0.2)",  
    layer="below",
    line=dict(color="#777777", width=0) 
)

fig.add_shape(
    type="rect",
    x0=x_min, x1=mean_rbi, y0=mean_contribution, y1=y_max,
    fillcolor="rgba(69, 123, 157, 0.2)",  
    layer="below",
    line=dict(width=0) 
)

fig.add_shape(
    type="rect",
    x0=x_min, x1=mean_rbi, y0=y_min, y1=mean_contribution,
    fillcolor="rgba(42, 157, 143, 0.2)",  
    layer="below",
    line=dict(width=0) 
)

fig.add_shape(
    type="rect",
    x0=mean_rbi, x1=x_max, y0=y_min, y1=mean_contribution,
    fillcolor="rgba(244, 162, 97, 0.2)",  
    layer="below",
    line=dict(width=0) 
)

fig.add_shape(type="line", x0=mean_rbi, x1=mean_rbi, y0=y_min, y1=y_max,
              line=dict(color="gray", width=1, dash="dash"))
fig.add_shape(type="line", x0=x_min, x1=x_max, y0=mean_contribution, y1=mean_contribution,
              line=dict(color="gray", width=1, dash="dash"))

fig.add_annotation(
    x=x_max, y=mean_contribution, 
    text="Mean RBI Contribution Rate",  
    showarrow=False,  
    font=dict(size=12, color="gray"),
    xshift=-70,  
    yshift=6
)

fig.add_annotation(
    x=mean_rbi, y=y_max, 
    text="Mean of the average RBI per Game", 
    showarrow=False,
    font=dict(size=12, color="gray"),
    xshift=-6,
    yshift=-87,
    textangle=-90 
)

fig.update_traces(
    hovertemplate="<b>%{hovertext}</b><br>RBI/Game: %{x:.3f}<br>Contribution Rate: %{y:.3%}",
    textposition="top center",
    marker=dict(size=10)
)

fig.update_xaxes(title_text="Average RBI per Game (RBI/Game)", range=[x_min, x_max])
fig.update_yaxes(title_text="RBI Contribution Rate (RBI%)", range=[y_min, y_max])

fig.update_layout(
    title="Offensive Efficiency Matrix of MLB Teams (1969-Present)",
    xaxis=dict(
        showgrid=True,
        showline=True,
        linecolor='#777777', 
        linewidth=1,
        gridcolor='#777777', 
        gridwidth=0.1 ), 
    yaxis=dict(
        showgrid=True,
        showline=True,
        linecolor='#777777',
        linewidth=1,
        gridcolor='#777777',
        gridwidth=0.5),
)

fig.update_layout(
    width=1000,
    height=700,
    margin=dict(l=40, r=40, t=40, b=40),
    legend=dict(title="MLB Team")
)

st.plotly_chart(fig, use_container_width=True)

quadrant_explanation = [
    ("High Avg RBI + High Contribution", "rgba(242, 142, 43, 0.3)",
     "Team excels in consistent scoring and significantly drives game outcomes through efficient batting."),

    ("High Avg RBI + Low Contribution", "rgba(225, 87, 89, 0.3)",
     "Team scores well but relies less on efficient batting, possibly benefiting more from opponent errors or strategic plays."),

    ("Low Avg RBI + Low Contribution", "rgba(89, 161, 79, 0.3)",
     "Team struggles in overall scoring and lacks effectiveness in converting batting opportunities into runs."),

    ("Low Avg RBI + High Contribution", "rgba(78, 121, 167, 0.3)",
     "Team maximizes scoring opportunities despite limited batting success, indicating efficiency under limited conditions.")
]

html_explanation = "<div style='line-height:1.8; font-size:14px;'>"

for text, color, detail in quadrant_explanation:
    html_explanation += (
        "<div style='display: flex; align-items: center; margin-bottom: 10px;'>"
        f"<div style='width: 40px; height: 20px; background-color: {color}; margin-right: 10px;'></div>"
        f"<span style='color: #555;'><strong>{text}:</strong> {detail}</span>"
        "</div>"
    )

html_explanation += "</div>"

st.markdown(html_explanation, unsafe_allow_html=True)

st.divider()

st.write("Data source: Lahman Baseball Database")
