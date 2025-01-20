import numpy as np
import pandas as pd

def recommend_topics(model, current_data):
    # Safe extraction of features with null/missing key values
    current_data['accuracy'] = current_data.get('correct_answers', 0) / current_data.get('total_questions', 1)
    current_data['duration_minutes'] = (
        pd.to_datetime(current_data.get('ended_at', '1970-01-01')) -
        pd.to_datetime(current_data.get('started_at', '1970-01-01'))
    ).total_seconds()/60

    features = pd.DataFrame([{
        'score': current_data.get('score', 0),
        'accuracy': current_data['accuracy'],
        'duration_minutes': current_data['duration_minutes']
    }])
    
    # Predict weak topics
    predictions = model.predict(features)
    
    # Generate topic recommendation summary
    unique_topics, counts = np.unique(predictions, return_counts=True)
    topic_error_map = dict(zip(unique_topics, counts))
    sorted_topics = sorted(topic_error_map.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_topics[:3]  # Top 3 weak topics
