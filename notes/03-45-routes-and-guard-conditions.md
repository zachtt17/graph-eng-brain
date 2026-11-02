# Routes and Guard Conditions

**Timestamp:** 03:45

## Key Concepts

**Routes** (conditional edges) inspect state and decide the next node.

**Guard Conditions** are the rules inside those routes:
- Check if quality score > threshold → proceed
- Check if retries remaining → loop back
- Check if human approval needed → interrupt

Example:
```python
def route_after_review(state):
    if state["score"] >= 0.8:
        return "finalize"
    return "revise"
```

Guards turn soft LLM decisions into hard, auditable control flow.
