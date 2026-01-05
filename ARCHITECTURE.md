# Architecture Overview

## Schema Validation

The schema defines the expected fields and their primitive data types (string, number, boolean).  
Incoming data is first validated for field presence and type correctness. This step ensures that all subsequent processing operates on well-formed data. Validation errors are collected and returned in a structured format without executing any rules.

## Computed Fields

Computed fields are resolved after successful base validation using simple template substitution.  
Each computed field references already validated data fields, ensuring predictable evaluation order and avoiding cyclic or dependency-based resolution.

## Rule Execution Model

Rules are expressed as declarative JSON objects and are executed at the field level.  
The rule engine supports two explicit action types:

- **Transform rules**: Mutate data in a controlled and deterministic manner.
- **Validation rules**: Evaluate conditions against data and emit validation errors.

Rule execution is intentionally split into two passes:
1. Transform rules are executed first to normalize or derive data.
2. Validation rules are executed afterward to enforce constraints on the transformed data.

This separation ensures clarity, determinism, and prevents unintended side effects during validation.

## Safety & Recursion Guard

To prevent infinite evaluation or unintended recursive execution, both computed field resolution and rule execution are protected by a depth guard.  
Evaluation depth is capped at five recursive calls. If the limit is exceeded, execution is halted and an error is returned.

## Determinism & Idempotency

The service is fully deterministic and idempotent.  
Given the same input payload, it always produces the same output. There is no external state, persistence layer, or randomness involved, making the system predictable and easy to reason about.

## Trade-offs & Extensions

The design prioritizes clarity, safety, and reviewability over flexibility.  
Potential future extensions include nested schema support, richer expression handling without `eval`, and additional rule action types while preserving the existing execution model.
