def validate_student_data(data, required_fields=None):
    if required_fields is None:
        required_fields = ['name', 'age', 'email']

    errors = []

    # Check required fields
    for field in required_fields:
        if field not in data:
            errors.append(f"Missing required field: {field}")

    # Basic field validations
    if 'name' in data:
        if not isinstance(data['name'], str) or len(data['name'].strip()) == 0:
            errors.append("Name must be a non-empty string")

    if 'age' in data:
        if not isinstance(data['age'], int) or data['age'] < 0 or data['age'] > 150:
            errors.append("Age must be a valid integer between 0 and 150")

    if 'email' in data:
        if not isinstance(data['email'], str) or '@' not in data['email']:
            errors.append("Email must be a valid email address")

    # Optional: validate if interests, achievements, courses are lists of strings
    for list_field in ['interests', 'achievements', 'courses']:
        if list_field in data:
            value = data[list_field]
            if not isinstance(value, list):
                errors.append(f"{list_field.capitalize()} must be a list")
            elif not all(isinstance(item, str) for item in value):
                errors.append(f"All items in {list_field} must be strings")

    return errors
