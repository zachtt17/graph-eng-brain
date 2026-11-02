# Checkpoints and Interrupts

**Timestamp:** 04:10

## Key Concepts

### Checkpoints
LangGraph persists state at each superstep. This enables:
- Resume after crash
- Time-travel debugging
- Multiple concurrent conversations (thread_id)

### Interrupts
`interrupt_before` or `interrupt_after` pause the graph for human input.

Use cases:
- Human approval before sending email or taking irreversible action
- Manual review of high-stakes outputs
- Providing missing information

Together they make long-running agents durable and safe.
