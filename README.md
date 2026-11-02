# graph-eng-brain

Living brain map for **Graph Engineering** concepts using LangGraph.

## What this is

- `notes/` — Markdown notes for each timestamp section of the Analytics Vidhya video *Graph Engineering Explained in 10 Minutes*.
- Each note was committed separately so the **git history itself is the brain map**.
- `agent.py` — a small LangGraph agent that loads those notes as persistent memory.

## How to use the brain

```bash
git clone https://github.com/zachtt17/graph-eng-brain.git
cd graph-eng-brain
pip install langgraph
python agent.py
```

Pull the notes into any other AI workflow by reading the `notes/` directory or by importing `load_brain_notes()` from `agent.py`.

## Source video

[Graph Engineering Explained in 10 Minutes | AI Agents & LangGraph](https://www.youtube.com/watch?v=ZVDAt3pzU5M) (Analytics Vidhya)

---

*Built as a living knowledge graph. Commit history = memory.*
