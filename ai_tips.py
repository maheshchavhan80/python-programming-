def generate_study_tips(difficulty):
    if difficulty == "high":
        return "Focus on thorough revision and plenty of practice problems."
    elif difficulty == "medium":
        return "Use a mix of revision and practice to strengthen understanding."
    elif difficulty == "low":
        return "Do some light revision to keep the material fresh."
    else:
        return "Difficulty level not recognized. Please use high, medium, or low."
