# State and Typed State

**Timestamp:** 02:40

## Key Concepts

State is the shared data structure that flows through the graph.

### Typed State
Using TypedDict, Pydantic, or dataclasses gives you:
- Schema validation
- Autocomplete and IDE support
- Clear contracts between nodes

Example in LangGraph:
```python
from typing import TypedDict

class AgentState(TypedDict):
    task: str
    plan: list[str]
    draft: str
    feedback: str
    approved: bool
```

Typed state makes the graph safer and easier to maintain as complexity grows.
