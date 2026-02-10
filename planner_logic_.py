def study_planner(subjects, days_left, total_daily_hours):
    """
    subjects: dict -> {subject_name: difficulty (1–5)}
    days_left: int
    total_daily_hours: float or int
    """

    # Calculate priority for each subject
    priorities = {
        subject: difficulty / days_left
        for subject, difficulty in subjects.items()
    }

    total_priority = sum(priorities.values())
    num_subjects = len(subjects)

    # Reserve minimum 1 hour per subject
    remaining_hours = total_daily_hours - num_subjects
    if remaining_hours < 0:
        raise ValueError("Not enough total hours to allocate minimum 1 hour per subject.")

    # Allocate hours based on priority
    allocation = {}
    for subject, priority in priorities.items():
        extra_hours = (priority / total_priority) * remaining_hours
        allocation[subject] = round(1 + extra_hours, 2)

    return allocation


# Example usage
subjects = {
    "Math": 5,
    "Physics": 4,
    "History": 2
}

days_left = 10
total_daily_hours = 8

plan = study_planner(subjects, days_left, total_daily_hours)
print(plan)
