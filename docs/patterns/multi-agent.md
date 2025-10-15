---
title: "Pattern: Multi-Agent Collaboration"
slug: "multi-agent-collaboration"
tags: ["multi-agent", "collaboration", "teamwork", "agentic-pattern", "crewai", "google-adk"]
themes: ["architecture/coordination", "workflow/orchestration"]
source:
  origin_note: "notes/2025-10-13_book-agentic-design-patterns.md"
  author: "Antonio Gulli"
  org: "Google"
  url: "https://docs.google.com/document/d/1RZ5-2fykDQKOBx01pwfKkDe0GCs5ydca7xW9Q4wqS_M/edit?tab=t.0"
status: "stable"
last_update: "2025-10-14"
summary: "Orquestra vários agentes especializados para quebrar problemas grandes em papéis claros, alinhando comunicação, coordenação e síntese."
relationships:
  snippets:
    - "snippets/multi-agent/multi-agent-crewai-blog-creation.md"
    - "snippets/multi-agent/multi-agent-google-adk-loop-agent.md"
    - "snippets/multi-agent/multi-agent-google-adk-hierarchical-structure.md"
  examples:
    - "examples/multi-agent/README.md"
  resources: []
---

### Problem

Um único agente generalista não consegue dominar todas as habilidades ou manter qualidade em demandas complexas (pesquisa + escrita + revisão + execução). Falta especialização e coordenação explícita.

### Pattern

Estruturar o sistema como equipe: cada agente assume papel específico (pesquisador, executor, crítico, gerente). Um coordenador distribui tarefas, agenda a comunicação (sequential, paralelo, debate) e consolida entregas. Kanban interno e protocolos claros evitam conflitos.

Formas comuns:
- handoff sequencial (producer → reviewer → publisher);
- execução paralela com merge posterior;
- debates/consenso quando há desacordo;
- hierarquia (manager + workers).

### Trade_offs

- **Pró:** especialização aumenta qualidade e throughput.  
- **Pró:** escalável — adicionar nova habilidade = novo agente.  
- **Contra:** coordenação ruim causa conflitos e loops.  
- **Contra:** custo maior (várias execuções) e observabilidade mais difícil.

### When_to_use

- Projetos multidisciplinares (pesquisa + escrita + validação).  
- Sistemas que exigem redundância ou defesa (agente crítico).  
- Experimentos com diversas abordagens simultâneas.

### Minimal_example

- [`snippets/multi-agent-crewai-blog-creation.md`](../snippets/multi-agent-crewai-blog-creation.md) — pipeline de conteúdo com CrewAI.  
- [`snippets/multi-agent-google-adk-loop-agent.md`](../snippets/multi-agent-google-adk-loop-agent.md) — loop colaborativo no Google ADK.

### Further_reading

- [Agentic Design Patterns — Capítulo 7](https://docs.google.com/document/d/1RZ5-2fykDQKOBx01pwfKkDe0GCs5ydca7xW9Q4wqS_M/edit?tab=t.0)
- [CrewAI Docs — Multi-Agent Crews](https://docs.crewai.com/)
*   **Network Analysis & Remediation:** Multiple agents collaborating to triage and remediate issues in autonomous operations.

## MULTI-AGENT COLLABORATION: EXPLORING INTERRELATIONSHIPS AND COMMUNICATION STRUCTURES

Understanding how agents interact and communicate is fundamental. A spectrum of interrelationship and communication models exists:

1.  **Single Agent:** Operates autonomously, limited by its individual scope.
2.  **Network:** Multiple agents interact directly in a decentralized fashion.
3.  **Supervisor:** A dedicated agent oversees and coordinates subordinate agents.
4.  **Supervisor as a Tool:** Supervisor provides resources or guidance rather than direct command.
5.  **Hierarchical:** Multi-layered organizational structure with multiple levels of supervisors.
6.  **Custom:** Unique interrelationship and communication structures tailored to specific requirements.


## HANDS-ON CODE EXAMPLE (CREW AI)

This example defines an AI-powered crew using CrewAI to generate a blog post about AI trends, with a researcher and a writer agent.

[Code Example: CrewAI Blog Creation Crew](../snippets/multi-agent-crewai-blog-creation.md)

## HANDS-ON CODE EXAMPLE (GOOGLE ADK)

This section demonstrates the establishment of a hierarchical agent structure within the Google ADK through the creation of a parent-child relationship.

[Code Example: Google ADK Hierarchical Agent Structure](../snippets/multi-agent-google-adk-hierarchical-structure.md)

### LoopAgent Example (Google ADK)

This code illustrates the employment of the `LoopAgent` within the Google ADK framework to establish iterative workflows.

[Code Example: Google ADK LoopAgent](../snippets/multi-agent-google-adk-loop-agent.md)

### SequentialAgent Example (Google ADK)

This code excerpt elucidates the `SequentialAgent` pattern within the Google ADK, engineered for the construction of linear workflows.

[Code Example: Google ADK SequentialAgent](../snippets/multi-agent-google-adk-sequential-agent.md)

### ParallelAgent Example (Google ADK)

This code example illustrates the `ParallelAgent` pattern within the Google ADK, which facilitates the concurrent execution of multiple agent tasks.

[Code Example: Google ADK ParallelAgent](../snippets/multi-agent-google-adk-parallel-agent.md)

### Agent as a Tool Example (Google ADK)

This code segment exemplifies the "Agent as a Tool" paradigm within the Google ADK, enabling an agent to utilize the capabilities of another agent.

[Code Example: Google ADK Agent as a Tool](../snippets/multi-agent-google-adk-agent-as-tool.md)

## AT A GLANCE

**What:** Complex problems often exceed the capabilities of a single, monolithic LLM-based agent, leading to inefficiency and suboptimal outcomes.

**Why:** The Multi-Agent Collaboration pattern creates a system of multiple, cooperating agents. A complex problem is broken down into smaller, manageable sub-problems, each assigned to a specialized agent with precise tools and capabilities.

**Rule of thumb:** Use this pattern when a task is too complex for a single agent and can be decomposed into distinct sub-tasks requiring specialized skills or tools. Ideal for problems benefiting from diverse expertise, parallel processing, or structured workflows.

## VISUAL SUMMARY


## KEY TAKEAWAYS

*   Multi-agent collaboration involves multiple agents working together to achieve a common goal.
*   This pattern leverages specialized roles, distributed tasks, and inter-agent communication.
*   Collaboration can take forms like sequential handoffs, parallel processing, debate, or hierarchical structures.
*   This pattern is ideal for complex problems requiring diverse expertise or multiple distinct stages.

## CONCLUSION

This chapter explored the Multi-Agent Collaboration pattern, demonstrating the benefits of orchestrating multiple specialized agents within systems. We examined various collaboration models, emphasizing the pattern's essential role in addressing complex, multifaceted problems across diverse domains. Understanding agent collaboration naturally leads to an inquiry into their interactions with the external environment.

## REFERENCES

1.  [Multi-Agent Collaboration Mechanisms: A Survey of LLMs](https://arxiv.org/abs/2501.06322)
2.  [Multi-Agent System — The Power of Collaboration](https://aravindakumar.medium.com/introducing-multi-agent-frameworks-the-power-of-collaboration-e9db31bba1b6)
