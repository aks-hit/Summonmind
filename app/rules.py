from app.depth_guard import guarded

@guarded
def execute_rules(rules: list, data: dict, depth=0):
    errors = []

    # First pass: TRANSFORM rules
    for rule in rules:
        if rule.get("action") != "transform":
            continue

        field = rule.get("field")
        expression = rule.get("expression")

        if field not in data:
            continue

        value = data[field]

        try:
            new_value = eval(
                expression,
                {"__builtins__": {}},
                {
                    "value": value,
                    "len": len
                }
            )
            data[field] = new_value
        except Exception:
            errors.append({
                "ruleId": rule.get("id"),
                "message": f"Transform failed for field '{field}'"
            })

    # Second pass: VALIDATION rules
    for rule in rules:
        if rule.get("action") != "validate":
            continue

        field = rule.get("field")
        condition = rule.get("condition")

        if field not in data:
            continue

        value = data[field]

        try:
            passed = eval(
                condition,
                {"__builtins__": {}},
                {
                    "value": value,
                    "len": len
                }
            )
        except Exception:
            passed = False

        if not passed:
            errors.append({
                "ruleId": rule.get("id"),
                "message": f"Rule failed for field '{field}'"
            })

    return errors

