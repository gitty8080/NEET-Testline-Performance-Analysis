import pandas as pd
from recomm_stats import recommend_topics
def generate_structured_insights(current_quiz_data, historical_df, model):
    # Process historical data
    historical_df['accuracy'] = historical_df['correct_answers'] / historical_df['total_questions'] * 100
    historical_df['submitted_at'] = pd.to_datetime(historical_df['submitted_at'])

    # Predict weak topics for the current quiz
    topic_predictions = recommend_topics(model, pd.DataFrame([current_quiz_data]))
    
    insights = {}
    for topic, count in topic_predictions:
        # Filter historical data for the topic
        topic_data = historical_df[historical_df['quiz'].apply(lambda x: x.get('topic') == topic)].sort_values('submitted_at')
        
        if topic_data.empty:
            continue
        
        # Performance trend
        trend = "improving" if topic_data['accuracy'].diff().mean() > 0 else "declining"
        
        # Historical performance table
        historical_performance = topic_data[['submitted_at', 'score', 'accuracy', 'total_questions', 'correct_answers', 'incorrect_answers']].to_dict(orient='records')
        
        # Historical scores for plotting
        historical_scores = topic_data[['submitted_at', 'score']]
        
        # Recommendations
        recommendations = [
            "Review the core concepts of this topic using notes or flashcards.",
            "Focus on practice questions for common mistakes.",
            "Use visual aids like flowcharts to understand better.",
            "Analyze trends and target specific subtopics."
        ]
        
        # Add insights for the topic
        insights[topic] = {
            "performance_trend": trend,
            "reason_for_weakness": f"The topic '{topic}' has been identified as weak due to frequent mistakes or low scores.",
            "historical_performance": historical_performance,
            "historical_scores": historical_scores,
            "recommendations": recommendations
        }
    return insights
