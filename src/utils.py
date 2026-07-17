def health_score_rule(row):
    score = 0

    if row["Protein"] > 15:
        score += 1
    if row["Iron"] > 5:
        score += 1
    if row["Sugar"] > 20:
        score -= 1
    if row["TotalFat"] > 20:
        score -= 1
    if row["Sodium"] > 600:
        score -= 1

    if score <= -1:
        return 0  # Unhealthy
    elif score == 0:
        return 1  # Moderate
    else:
        return 2  # Healthy