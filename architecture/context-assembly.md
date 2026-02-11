# Context Assembly Layer
## AI-Assisted Client Onboarding & Product Eligibility

---

## Purpose

The Context Assembly Layer is responsible for constructing a governed, minimal, and policy-compliant context artifact for AI reasoning.

This layer ensures:

- Data minimization
- Access control enforcement
- Masking and redaction of sensitive attributes
- Deterministic and auditable context construction
- Clear separation between enterprise data and AI models

The LLM never directly accesses enterprise systems.

---

## Architectural Role

This layer sits between:

Business Request → Enterprise Data Sources → LLM Reasoning Service

It acts as a **control boundary**, ensuring only appropriate, policy-aligned information is passed to the model.

---

## High-Level Flow

Client Request
↓
Determine Applicable Policy Scope
↓
Retrieve Structured Product Rules
↓
Retrieve Relevant Policy Documents
↓
Apply Filtering & Masking Rules
↓
Generalize Sensitive Fields
↓
Construct Context Artifact
↓
Send to LLM


---

## Retrieval Strategy

### Hybrid Retrieval Approach

The system uses a hybrid retrieval mechanism:

1. Deterministic Retrieval (Structured Rules)
2. Semantic Retrieval (Unstructured Policy Documents)

This ensures both precision and contextual reasoning capability.

---

## 1. Deterministic Retrieval (Structured Policy Data)

Structured data includes:

- Product eligibility matrices
- Fee structures
- Limit thresholds
- Approval rules

Retrieval filters include:

- Client segment
- Geography
- Risk category
- Product type requested

Only relevant structured rules are retrieved.

This step ensures:
- Reduced noise
- Predictable behavior
- Audit-friendly traceability

---

## 2. Semantic Retrieval (Policy Documents)

Unstructured documents include:

- Onboarding policy text
- Exception handling clauses
- Compliance documentation

Semantic retrieval (via vector embeddings) will:

- Identify relevant clauses
- Retrieve contextual policy excerpts
- Limit scope to applicable product and segment

Important constraint:

Semantic retrieval operates only on pre-approved, sanitized documents.

It does not bypass governance rules.

---

## Data Minimization & Transformation Rules

The system enforces strict data handling principles before passing context to the LLM.

### Field Handling Rules

| Field | Action | Reason |
|--------|--------|--------|
| Account Number | Redact | PII protection |
| Tax ID | Redact | Regulatory compliance |
| Exact Revenue | Convert to Band | Minimize sensitive exposure |
| Exposure Amount | Convert to Tier | Policy-based reasoning only |
| Internal Notes | Drop | Not required for eligibility |
| Historical Overrides | Summarize | Avoid bias amplification |

---

## Masking & Generalization Principles

- No raw PII is included in the context artifact.
- Sensitive numeric values are converted into logical bands.
- Data is limited to fields required for eligibility reasoning.
- Internal operational notes are excluded unless policy-relevant.

The goal is to pass only what is necessary — nothing more.

---

## Context Artifact Schema

The context passed to the LLM must follow a structured, deterministic schema:


client_summary:
  segment:
  industry:
  geography:
  risk_category:
  revenue_band:
  exposure_tier:
  existing_products:

policy_summary:
  eligible_products:
  fee_ranges:
  limit_constraints:
  exception_rules:

risk_flags:
  - flag_type:
  - reason:

decision_constraints:
  approval_required:
  escalation_level:
