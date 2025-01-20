def determine_learning_levels(topics):
    learning_levels = {}
    for topic in topics:
        if topic == "Unknown" or topic == "None":
            level = "Review basics"
        elif "advanced" in topic.lower():
            level = "Advanced focus"
        else:
            level = "Intermediate practice"
        
        learning_levels[topic] = level
    return learning_levels
