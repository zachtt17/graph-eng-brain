# State Reducers

**Timestamp:** 03:30

## Key Concepts

Reducers control how state updates are merged when multiple nodes write to the same key.

### Common Patterns
- **Override** (default): New value replaces old.
- **Append** (`operator.add`): Lists accumulate.
- **Custom**: You define merge logic (e.g., keep highest score, merge dicts).

In LangGraph:
```python
from typing import Annotated
from operator import add

class AgentState(TypedDict):
    messages: Annotated[list, add]  # appends instead of overwriting
```

Reducers prevent race conditions and enable parallel node execution safely.
