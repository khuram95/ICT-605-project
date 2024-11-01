import streamlit as st


st.set_page_config(
    page_title="Home",
    page_icon="	:house:"
)


def show_homepage():
    st.title("Premier League Data Analysis Dashboard")

    # Introduction Section
    st.header("Introduction")
    st.write("This interactive dashboard provides an in-depth view of team performances, "
             "match outcomes, and trends across the English Premier League. Through data visualizations and interactive tools, "
             "you can explore how teams perform based on formations, possession rates, and home/away factors.")

    # Problem Definition Section
    st.header("Problem Definition")
    st.write("Our goal is to uncover patterns in team performance in the EPL based on factors such as venue, formations, "
             "and possession. By analyzing these elements, we aim to reveal insights that can be useful for fans, analysts, "
             "and researchers interested in understanding the dynamics of EPL matches.")

    # Goal Section
    st.header("Goal")
    st.write("To provide users with a data-driven tool to explore EPL match data, analyze trends, and visualize team performances.")

    # Dataset Introduction Section
    st.header("Dataset Summary")
    st.write("The dataset includes detailed information on EPL matches, such as match results, team formations, possession statistics, "
             "and more. This dataset allows us to study trends and gain insights into factors that influence match outcomes.")

    # Target Audience Section
    st.header("Target Audience")
    st.write("This dashboard is designed for EPL fans, sports analysts, data enthusiasts, and researchers interested in exploring "
             "the factors that impact match results and team performances.")

    # Hypotheses Section
    st.header("Hypotheses")
    st.write("Below are some hypotheses that this analysis aims to explore:")
    st.markdown("""
    - Teams with higher ball possession rates are more likely to win matches.
    - Home teams have a higher win rate compared to away teams, indicating a 'home advantage.'
    - Teams with a consistent winning streak have better win/loss ratios over time.
    - Defensive formations result in fewer goals conceded but also fewer goals scored.
    - Weekend matches have a different outcome pattern compared to weekday matches.
    """)

    # FAQs Section
    st.header("FAQs")
    st.write(
        "Here are some common questions about the dashboard and its functionality:")

    # FAQ items
    faqs = [
        ("What is the purpose of this dashboard?",
         "This dashboard provides insights into EPL team performances, trends, and statistics based on match data, helping fans and analysts explore match outcomes, formations, and other factors that impact results."),

        ("What data is used in this dashboard?",
         "The dashboard is built using EPL match data, including details such as match outcomes, team formations, possession percentages, and venue information."),

        ("How often is the data updated?",
         "The data is static and represents a specific dataset provided for this analysis. For real-time or regularly updated data, a direct connection to an EPL data API would be required."),

        ("Who is this dashboard intended for?",
         "The dashboard is designed for EPL fans, sports analysts, and researchers interested in understanding match dynamics and team performance across seasons."),

        ("How can I interpret the win rate trends?",
         "Win rate trends are shown over time, by day of the week, and by formation. They reveal patterns in team performance based on different conditions."),

        ("What insights can I gain from the Home vs. Away comparison?",
         "This section allows users to explore how teams perform differently when playing at home versus away, which can be useful for understanding the 'home advantage' concept."),

        ("Can I filter data to view specific teams or seasons?",
         "Yes, use the sidebar filters to select specific teams, seasons, formations, and other parameters to refine the data shown in the dashboard."),

        ("How is possession linked to match outcomes?",
         "The possession and match outcomes chart shows the average possession rate for wins, draws, and losses, highlighting any correlation between possession control and match results."),
    ]

    # Display FAQs
    for question, answer in faqs:
        with st.expander(question):
            st.write(answer)


show_homepage()
