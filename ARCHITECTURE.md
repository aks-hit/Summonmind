# Architecture Overview

## Schema Validation

The schema defines the expected fields and their primitive data types (string, number, boolean).  
Incoming data is validated for field presence and type correctness before any rule execution or computed field evaluation occurs. Validation errors are collected and returned in a structured format.

## Rule Execution Model

Rules are expressed as declarative JSON objects and evaluated at the field level.  
Each rule condition is executed in a restricted evaluation context against the field value, ensuring deterministic behavior and preventing side effects. Multiple rules can be evaluated independently within a single request.

## Computed Fields

Computed fields are resolved after successful base validation using simple template substitution.  
Templates reference existing validated fields, ensuring predictable evaluation order and avoiding cyclic or dependency-based resolution.

## Safety & Recursion Guard

To prevent infinite evaluation loops, rule execution and computed field resolution are protected by a depth guard with a maximum depth of five. If the limit is exceeded, execution is halted and an error is returned.

## Determinism & Idempotency

The service is fully deterministic and idempotent. Given the same input payload, it always produces the same output. No external state, persistence layer, or randomness is involved.

## Trade-offs & Extensions

The design prioritizes clarity, safety, and reviewability over extensibility.  
Potential future enhancements include transform rules, richer expression support, and more advanced schema constraints.
