from app.depth_guard import guarded

@guarded
def execute_rules(rules: list, data: dict, depth=0):
    errors = []

    for rule in rules:
        rule_id = rule.get("id")
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
                    "len": len  # allow simple safe helpers
                }
            )
        except Exception:
            passed = False

        if not passed:
            errors.append({
                "ruleId": rule_id,
                "message": f"Rule failed for field '{field}'"
            })

    return errors
