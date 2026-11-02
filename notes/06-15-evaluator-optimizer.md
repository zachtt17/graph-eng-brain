# Evaluator-Optimizer Pattern

**Timestamp:** 06:15

## Key Concepts

A generator produces output, an evaluator scores or critiques it, and a conditional edge decides whether to accept or revise.

### Loop Structure
1. Generate draft
2. Evaluate against criteria
3. If score low → revise (with feedback)
4. If score high → finalize

This is the graph version of self-refinement / Reflexion and is one of the highest-leverage patterns for quality.
