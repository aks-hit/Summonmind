from app.depth_guard import guarded

@guarded
def apply_computed_fields(computed: dict, data: dict, depth=0):
    result = data.copy()

    for key, template in computed.items():
        value = template
        for field, field_value in result.items():
            value = value.replace(f"{{{{{field}}}}}", str(field_value))

        if "{{" in value or "}}" in value:
            raise Exception(f"Unresolved field in computed value: {key}")

        result[key] = value

    return result
