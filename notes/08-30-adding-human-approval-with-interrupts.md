# Adding Human Approval with Interrupts

**Timestamp:** 08:30

## Key Concepts

The demo inserts an interrupt before the final action so a human can approve or request changes.

### Implementation Sketch
```python
graph = builder.compile(interrupt_before=["finalize"])
```

When the graph pauses, you inspect the state, then resume with `Command(resume=...)`.

This is the practical pattern for keeping humans in control without writing custom pause logic.
