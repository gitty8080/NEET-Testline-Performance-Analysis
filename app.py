import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from get_data import fetch_data
from data_prep import prep_data
from model import train_model
from recomm_stats import recommend_topics
from generate_insights import generate_structured_insights

# Fetch data
current_quiz_data, historical_df = fetch_data()

# Prepare data
features, labels = prep_data(historical_df)

# Train and evaluate model
model, report = train_model(features, labels)

# Display model performance
st.title("NEET Testline Performance Analysis Report")
st.subheader("Model Performance")
st.json(report)

# Generate insights for all weak topics
weak_topics_insights = generate_structured_insights(current_quiz_data, historical_df, model)

# Display overall performance graph
st.subheader("Overall Historical Quiz Scores")
plt.figure(figsize=(10, 6))
plt.plot(historical_df['submitted_at'], historical_df['score'], marker='o', label='Quiz Scores')
plt.title('Historical Quiz Performance')
plt.xlabel('Date')
plt.ylabel('Score')
plt.legend()
st.pyplot(plt)

# Display insights for weak topics
st.subheader("AI-Generated Insights for Weak Topics")
for topic, insights in weak_topics_insights.items():
    st.text(f"Topic: {topic}")
    st.text(f"Performance Trend: {insights['performance_trend']}")
    st.text(f"Reason for Weakness: {insights['reason_for_weakness']}")
    st.text("Previous Performance:")
    st.table(insights['historical_performance'])
    st.text("Recommended Actions:")
    for rec in insights['recommendations']:
        st.text(f"- {rec}")
    
    # Display performance graph for each weak topic
    st.subheader(f"Performance Trend: {topic}")
    topic_scores = insights['historical_scores']
    plt.figure(figsize=(8, 4))
    plt.plot(topic_scores['submitted_at'], topic_scores['score'], marker='o', label=f'{topic} Scores')
    plt.title(f'Performance Trend for {topic}')
    plt.xlabel('Date')
    plt.ylabel('Score')
    plt.legend()
    st.pyplot(plt)
