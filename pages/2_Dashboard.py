import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="EPL Dashboard",
                   page_icon=":soccer:", layout="wide")
st.title(":soccer: EPL Interactive Dashboard")

# Load data
df = pd.read_csv("matches.csv")

# Data Preprocessing and Transformation
df['date'] = pd.to_datetime(df['date'])
df['season'] = df['date'].dt.year
df['win'] = df['result'].apply(
    lambda x: 'Win' if x == 'W' else 'Loss' if x == 'L' else 'Draw')
df['poss'] = pd.to_numeric(df['poss'], errors='coerce')

# Date Filter
startDate, endDate = df['date'].min(), df['date'].max()
col1, col2 = st.columns(2)
with col1:
    date1 = st.date_input("Start Date", startDate)
with col2:
    date2 = st.date_input("End Date", endDate)
filtered_df = df[(df['date'] >= pd.to_datetime(date1)) &
                 (df['date'] <= pd.to_datetime(date2))]

# Sidebar Filters
st.sidebar.header("Filter Options")
team = st.sidebar.multiselect("Select Team", filtered_df['team'].unique())
if team:
    filtered_df = filtered_df[filtered_df['team'].isin(team)]

outcome = st.sidebar.multiselect("Match Outcome", ['Win', 'Draw', 'Loss'])
if outcome:
    filtered_df = filtered_df[filtered_df['win'].isin(outcome)]

formation = st.sidebar.multiselect(
    "Formation", filtered_df['formation'].unique())
if formation:
    filtered_df = filtered_df[filtered_df['formation'].isin(formation)]

matchweek = st.sidebar.multiselect(
    "Matchweek", sorted(filtered_df['round'].unique()))
if matchweek:
    filtered_df = filtered_df[filtered_df['round'].isin(matchweek)]

season = st.sidebar.multiselect(
    "Season", sorted(filtered_df['season'].unique()))
if season:
    filtered_df = filtered_df[filtered_df['season'].isin(season)]

# KPI Cards
st.subheader("Key Performance Insights")
total_matches = filtered_df.shape[0]
total_goals = filtered_df['gf'].sum()
win_percentage = round(
    (filtered_df[filtered_df['win'] == 'Win'].shape[0] / total_matches) * 100, 2)
avg_possession = round(filtered_df['poss'].mean(), 2)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Matches", total_matches)
col2.metric("Total Goals", total_goals)
col3.metric("Win Percentage", f"{win_percentage}%")
col4.metric("Average Possession", f"{avg_possession}%")

st.subheader("Match Insights")

# Win/Loss/Draw Distribution and Home vs Away Performance
row1_col1, row1_col2 = st.columns(2)
with row1_col1:
    win_distribution = filtered_df['win'].value_counts()
    fig_pie = px.pie(values=win_distribution.values,
                     names=win_distribution.index, title="Win/Loss/Draw Distribution")
    st.plotly_chart(fig_pie, use_container_width=True)

with row1_col2:
    home_away_goals = filtered_df.groupby('venue').agg(
        goals_for=('gf', 'sum'), goals_against=('ga', 'sum')).reset_index()
    fig_home_away = px.bar(home_away_goals, x='venue', y=[
                           'goals_for', 'goals_against'], barmode='group', title="Goals For and Against at Home vs. Away")
    st.plotly_chart(fig_home_away, use_container_width=True)

# Possession and Match Outcomes & Impact of Match Timing
row2_col1, row2_col2 = st.columns(2)
with row2_col1:
    possession_result = filtered_df.groupby('win').agg(
        avg_possession=('poss', 'mean')).reset_index()
    fig_possession = px.bar(possession_result, x='win', y='avg_possession',
                            title="Average Possession by Match Outcome")
    st.plotly_chart(fig_possession, use_container_width=True)

with row2_col2:
    filtered_df['match_day'] = pd.Categorical(filtered_df['date'].dt.day_name(),
                                              categories=[
                                                  "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                                              ordered=True)
    match_day_performance = filtered_df.groupby('match_day').agg(
        win_rate=('win', lambda x: (x == 'Win').mean())).reset_index()
    match_day_performance = match_day_performance.sort_values(by='match_day')
    fig_timing = px.line(match_day_performance, x='match_day',
                         y='win_rate', title="Win Rate by Match Day")
    st.plotly_chart(fig_timing, use_container_width=True)

# Formation and Match Outcomes & Theory of Home Advantage
row3_col1, row3_col2 = st.columns(2)
with row3_col1:
    formation_performance = filtered_df.groupby('formation').agg(
        win_rate=('win', lambda x: (x == 'Win').mean())).reset_index()
    fig_formation = px.bar(formation_performance, x='formation',
                           y='win_rate', title="Win Rate by Formation")
    st.plotly_chart(fig_formation, use_container_width=True)

with row3_col2:
    home_advantage = filtered_df.groupby(
        ['venue', 'win']).size().unstack(fill_value=0)
    home_advantage_percentage = home_advantage.div(
        home_advantage.sum(axis=1), axis=0) * 100
    home_advantage_percentage = home_advantage_percentage.reset_index().melt(
        id_vars='venue', var_name='Outcome', value_name='Percentage')
    fig_home_advantage_comparative = px.bar(home_advantage_percentage, x='Outcome', y='Percentage',
                                            color='venue', barmode='group', title="Match Outcome Playing Home vs. Away")
    st.plotly_chart(fig_home_advantage_comparative, use_container_width=True)

# Trends Across Seasons
st.subheader("Seasonal Trends")
seasonal_win_rate = filtered_df.groupby('season').agg(
    win_rate=('win', lambda x: (x == 'Win').mean())).reset_index()

fig_season_trend = px.line(seasonal_win_rate, x='season',
                           y='win_rate', title="Win Rate Trends Over Seasons")

fig_season_trend.update_xaxes(type='category')

st.plotly_chart(fig_season_trend, use_container_width=True)
