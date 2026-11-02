# Conditional Routing and Revision Loops

**Timestamp:** 09:15

## Key Concepts

After evaluation, a conditional edge decides:
- Score high enough → go to human approval / finalize
- Score too low and retries remain → send feedback back to the writer node

### Stop Conditions
Always include a max-retry guard so the loop cannot run forever.

This pattern (evaluator-optimizer + interrupt) is one of the most reliable ways to raise quality while staying controllable.
