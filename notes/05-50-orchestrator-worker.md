# Orchestrator-Worker Pattern

**Timestamp:** 05:50

## Key Concepts

An orchestrator node breaks a large task into subtasks and delegates them to specialized worker nodes (or subgraphs).

### Structure
- Orchestrator: Plans and assigns
- Workers: Execute focused pieces
- Aggregator: Combines results

This is the multi-agent version of divide-and-conquer.
