"""
Small LangGraph agent that loads Markdown notes from the notes/ directory
as persistent memory (the living brain map).

Git history of this repo is the brain map. Pull the notes into any AI workflow
by cloning or by reading this agent's memory loader.
"""

import os
from pathlib import Path
from typing import Annotated, TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

# ---------------------------------------------------------------------------
# Memory loader — reads every Markdown note as persistent knowledge
# ---------------------------------------------------------------------------

NOTES_DIR = Path(__file__).parent / "notes"

def load_brain_notes() -> dict[str, str]:
    """Load all Markdown notes into a dict keyed by filename."""
    notes = {}
    if not NOTES_DIR.exists():
        return notes
    for md_file in sorted(NOTES_DIR.glob("*.md")):
        notes[md_file.stem] = md_file.read_text(encoding="utf-8")
    return notes

BRAIN = load_brain_notes()

# ---------------------------------------------------------------------------
# Agent state
# ---------------------------------------------------------------------------

class BrainState(TypedDict):
    query: str
    relevant_notes: list[str]
    answer: str

# ---------------------------------------------------------------------------
# Nodes
# ---------------------------------------------------------------------------

def retrieve_notes(state: BrainState) -> dict:
    """Simple keyword retrieval over the loaded notes."""
    query_lower = state["query"].lower()
    hits = []
    for name, content in BRAIN.items():
        if any(word in content.lower() for word in query_lower.split() if len(word) > 3):
            hits.append(f"## {name}\n{content[:800]}...")
    return {"relevant_notes": hits[:5]}

def answer_from_brain(state: BrainState) -> dict:
    """Synthesize an answer from the retrieved notes (stub — replace with real LLM)."""
    notes_text = "\n\n".join(state["relevant_notes"]) or "No relevant notes found."
    answer = (
        f"From the Graph Engineering brain map:\n\n{notes_text}\n\n"
        "(This is a lightweight retrieval agent. Swap the body for a real LLM call.)"
    )
    return {"answer": answer}

# ---------------------------------------------------------------------------
# Graph
# ---------------------------------------------------------------------------

builder = StateGraph(BrainState)
builder.add_node("retrieve", retrieve_notes)
builder.add_node("answer", answer_from_brain)

builder.add_edge(START, "retrieve")
builder.add_edge("retrieve", "answer")
builder.add_edge("answer", END)

# Persistent memory via checkpointer
checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)

if __name__ == "__main__":
    config = {"configurable": {"thread_id": "demo"}}
    result = graph.invoke(
        {"query": "What is the evaluator-optimizer pattern?"},
        config=config,
    )
    print(result["answer"])
