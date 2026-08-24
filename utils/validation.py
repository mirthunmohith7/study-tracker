def validate_subject(subject):
    return bool(subject)

def validate_duration(duration):
    try:
        duration_minutes = int(duration)
        return duration_minutes > 0
    except ValueError:
        return False
