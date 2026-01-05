from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from pydantic import BaseModel
from app.validator import validate_schema_and_data
from app.computed import apply_computed_fields
from app.rules import execute_rules
from app.depth_guard import DepthGuardError

app = FastAPI(title="SummonMind Backend Screening")

class ValidateRequest(BaseModel):
    schema_def: dict
    rules: list
    data: dict
@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse("/docs")

@app.post("/validate")
def validate(payload: ValidateRequest):
    try:
        # 1. Validate schema + base data
        ok, result = validate_schema_and_data(payload.schema_def, payload.data)
        if not ok:
            return {"errors": result}

        validated_data = result

        # 2. Apply computed fields
        validated_data = apply_computed_fields(
            payload.schema_def.get("computed", {}),
            validated_data
        )

        # 3. Execute rules
        rule_errors = execute_rules(payload.rules, validated_data)
        if rule_errors:
            return {"errors": rule_errors}

        return {"validatedData": validated_data}

    except DepthGuardError:
        return {"error": "Max evaluation depth reached"}
