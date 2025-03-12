# systemPatterns.md

This file documents system-wide patterns, design patterns, and architectural patterns used in the project.

## System Patterns

### 1. Modular Application Design
* **Description:** Django application is designed with modular apps to promote maintainability and scalability.
* **Context:** Web framework layer.
* **Details:** Each feature or component is implemented as a separate Django app.

### 2. LLM Orchestration with Langgraph
* **Description:** Langgraph is used to orchestrate interactions with multiple LLM providers.
* **Context:** LLM integration layer.
* **Details:** Langgraph workflows are defined to manage conversations and interactions with LLMs.