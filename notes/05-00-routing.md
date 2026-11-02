# Routing Pattern

**Timestamp:** 05:00

## Key Concepts

A classifier node inspects the input and routes to specialized handlers.

### Use Cases
- Support ticket classification → refund / tech / billing nodes
- Intent detection → different tool sets or agents
- Quality gates → pass / revise / escalate

Routing keeps context windows focused and prevents one model from trying to do everything.
