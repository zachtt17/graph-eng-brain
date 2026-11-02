# Core Components of Graph Engineering

**Timestamp:** 02:00

## The Three Primitives

1. **Nodes** — Units of work. Can be:
   - LLM calls
   - Deterministic Python functions
   - Tool invocations
   - Human approval steps

2. **Edges** — Decide what runs next.
   - Fixed edges (always go to X)
   - Conditional edges (route based on state)

3. **State** — Shared data object that travels through the graph. Every node reads what it needs and writes updates.

Nodes do the work. Edges decide what happens next. State carries the information.
