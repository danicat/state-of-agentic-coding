# State of Agentic Coding

Companion repository for the talk **"State of Agentic Coding"** presented at **Google I/O Extended London 2026** by [Daniela Petruzalek](https://github.com/danicat), Developer Relations Engineer at Google Cloud.

## Overview

As AI-assisted coding evolves from simple autocomplete to autonomous agents, developers need new mental models and tools to maintain productivity and trust. This repository demonstrates the "Agentic Toolbox"—a set of techniques used to guide AI agents through complex software engineering tasks.

### The 7 Stages of Agentic Coding
The talk explores the progression of human-AI collaboration:
1. **Gemini in the Browser**: Manual copy-paste, low trust.
2. **Coding Agent with Manual Approval**: Every tool call is reviewed.
3. **The Guarded Collaborator**: Automated file edits, manual shell commands.
4. **The Hands-Off Director**: High trust, focusing on end results.
5. **YOLO Mode**: Complete trust, high-speed autonomous iteration.
6. **The Orchestrator**: Coordinating a fleet of specialized subagents.
7. **The Architect**: Designing systems that design systems.

---

## Repository Structure

The project is organized into folders representing different tools in the agentic toolbox:

### [01a_prompts](file:///Users/petruzalek/projects/state-of-agentic-coding/01a_prompts)
Examples of high-fidelity prompts, including a complete specification for building a **Pac-Man clone in Go** using the Ebiten engine.

### [01b_prompts](file:///Users/petruzalek/projects/state-of-agentic-coding/01b_prompts)
Visual prompting and architectural sketches, including the **Speedgrapher 2.0** blogging agent design.

### [02_rules](file:///Users/petruzalek/projects/state-of-agentic-coding/02_rules)
Demonstrates how project-level rules (e.g., [GEMINI.md](file:///Users/petruzalek/projects/state-of-agentic-coding/02_rules/GEMINI.md)) shape agent behavior. This folder includes the "Zen of Python" as a set of guiding principles for the agent.

### [03_hooks](file:///Users/petruzalek/projects/state-of-agentic-coding/03_hooks)
Using automated triggers for routine operations, such as resetting the environment or running cleanup scripts.

### [04_subagents](file:///Users/petruzalek/projects/state-of-agentic-coding/04_subagents)
Advanced orchestration patterns. Demonstrates how a root agent can spawn specialized subagents (Engineering Manager, Backend Engineer, Frontend Engineer) to build a hotel booking application.

### [05_skills](file:///Users/petruzalek/projects/state-of-agentic-coding/05_skills)
Custom capabilities and modular tools that can be dynamically added to an agent's repertoire.

### [06_mcp](file:///Users/petruzalek/projects/state-of-agentic-coding/06_mcp)
Integration with the **Model Context Protocol (MCP)**, showing how to build and connect custom tool servers to agents using the Go SDK.

---

## Tools Used

- **[Antigravity](https://antigravity.google)**: The command center for managing multiple local agents in parallel.
- **Gemini**: The underlying model powering the agentic reasoning.
- **MCP (Model Context Protocol)**: For extending agent capabilities with custom tools.

## Getting Started

To explore these examples, we recommend using an agentic-aware IDE or CLI (like Antigravity). You can point the agent to any of the `PROMPT.md` files to see them in action.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](file:///Users/petruzalek/projects/state-of-agentic-coding/LICENSE) file for details.
