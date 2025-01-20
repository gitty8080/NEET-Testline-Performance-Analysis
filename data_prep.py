import pandas as pd

def prep_data(hist_df):
    hist_df['topic'] = hist_df['quiz'].apply(lambda x: x.get('topic', 'Unknown'))
    hist_df['accuracy'] = hist_df.get('correct_answers', 0) / hist_df.get('total_questions', 1)
    hist_df['duration_minutes'] = (
        pd.to_datetime(hist_df['ended_at'], errors='coerce') -
        pd.to_datetime(hist_df['started_at'], errors='coerce')
    ).dt.total_seconds() / 60

    #Topic-wise avg errors
    topic_error_counts = hist_df.groupby('topic')['incorrect_answers'].sum().reset_index()
    topic_error_counts.columns = ['topic', 'error_count']

    #Merge to label weak topics
    hist_df = hist_df.merge(topic_error_counts, on='topic', how='left')
    hist_df['weak_topic'] = hist_df.apply(
        lambda x: x['topic'] if x['error_count'] > 0 else 'None', axis=1
    )

    features = hist_df[['score', 'accuracy', 'duration_minutes']]
    labels = hist_df['weak_topic']

    return features, labels
