# Human-in-the-Loop Pattern

**Timestamp:** 06:30

## Key Concepts

Insert explicit human decision points into the graph using interrupts.

### When to Use
- High-stakes actions (payments, emails, deployments)
- Ambiguous cases the model shouldn't decide alone
- Final quality gate before customer-facing output

LangGraph's interrupt + Command resume makes this first-class instead of a hack.
