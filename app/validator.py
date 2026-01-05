def validate_schema_and_data(schema_def: dict, data: dict):
    errors = []

    fields = schema_def.get("fields", {})
    for field, field_type in fields.items():
        if field not in data:
            errors.append({
                "field": field,
                "message": "Field is missing"
            })
            continue

        value = data[field]

        if field_type == "string" and not isinstance(value, str):
            errors.append({"field": field, "message": "Expected string"})
        elif field_type == "number" and not isinstance(value, (int, float)):
            errors.append({"field": field, "message": "Expected number"})
        elif field_type == "boolean" and not isinstance(value, bool):
            errors.append({"field": field, "message": "Expected boolean"})

    if errors:
        return False, errors

    return True, data.copy()
