# SummonMind Backend

This repository contains a minimal FastAPI-based backend service built as part of the SummonMind backend screening exercise.

The focus of this implementation is **clarity, correctness, deterministic behavior, and safety**, rather than completeness or over-engineering.

The service validates input data against a declarative schema, applies computed fields, executes field-level rules, and returns either validated data or structured errors.

---

## Tech Stack

- Python 3.10+
- FastAPI
- Pydantic
- Uvicorn

---

## Setup

### 1. Create and activate virtual environment

```bash
python -m venv venv
```

**Windows (PowerShell):**
```powershell
.\venv\Scripts\Activate
```

**macOS / Linux:**
```bash
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Server

Start the FastAPI server using:

```bash
uvicorn app.main:app --reload
```

The service will be available at:
```
http://127.0.0.1:8000
```

---

## API Endpoint

### POST /validate

Validates input data against a schema, applies computed fields, executes rules, and returns either validated data or errors.

#### Request Body Structure

```json
{
  "schema_def": { ... },
  "rules": [ ... ],
  "data": { ... }
}
```

#### Response (Success)

```json
{
  "validatedData": { ... }
}
```

#### Response (Failure)

```json
{
  "errors": [
    {
      "ruleId": "r1",
      "message": "Rule failed for field 'age'"
    }
  ]
}
```

---

## How to Test the Service

The service can be tested in two simple ways.

### Option 1: Using Swagger UI (Recommended)

1. Ensure the server is running:
   ```bash
   uvicorn app.main:app --reload
   ```

2. Open Swagger UI in the browser:
   ```
   http://127.0.0.1:8000/docs
   ```

3. Open the `/validate` endpoint and paste the contents of:
   - `samples/valid.json` → Expected: success response
   - `samples/invalid.json` → Expected: validation errors

This allows quick interactive testing without any additional setup.

### Option 2: Using the Demo Script

A simple demo script is included to programmatically demonstrate both valid and invalid cases.

1. Start the server in one terminal:
   ```bash
   uvicorn app.main:app --reload
   ```

2. In another terminal, run:
   ```bash
   python tests/demo.py
   ```

The script sends requests to the live `/validate` endpoint and prints responses for both scenarios.

---

## Features Implemented

- Schema-based field validation (string, number, boolean)
- Computed fields using template substitution
- Field-level declarative rule evaluation
- Multiple rules per request
- Structured validation errors
- Transform rules that safely mutate data before validation
- Depth guard to prevent infinite evaluation (max depth = 5)
- Deterministic and idempotent execution

---

## Project Structure

```
summonmind-backend/
│
├── app/
│   ├── main.py
│   ├── validator.py
│   ├── rules.py
│   ├── computed.py
│   └── depth_guard.py
│
├── samples/
│   ├── valid.json
│   └── invalid.json
│
├── tests/
│   └── demo.py
│
├── README.md
├── ARCHITECTURE.md
├── requirements.txt
```

---

