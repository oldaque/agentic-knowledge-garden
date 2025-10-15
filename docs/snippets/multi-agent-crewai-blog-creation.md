---
title: "Multi-Agent Blog Creation with CrewAI"
slug: "multi-agent-crewai-blog-creation"
summary: "Demonstrates multi-agent system using CrewAI with researcher and writer agents collaborating to produce a blog post about AI trends."
tags: ["crewai", "multi-agent", "collaboration", "research", "content-creation"]
status: "stable"
last_update: "2025-10-14"
origin_note: "docs/patterns/multi-agent.md"
languages: ["python"]
how_to_run: "Requires CrewAI, LangChain, and a Google API key. Run with `python your_script_name.py`."
related_patterns: ["docs/patterns/multi-agent.md"]
---

## Context

This snippet demonstrates a multi-agent collaboration pattern using CrewAI for content creation. It defines two specialized agents (researcher and writer) that work sequentially: the researcher finds and summarizes AI trends, then the writer creates a blog post based on those findings. The pattern showcases how agents with different roles can collaborate through task dependencies and context sharing.

## Snippet

```python
import os
from dotenv import load_dotenv
from crewai import Agent, Task, Crew, Process
from langchain_google_genai import ChatGoogleGenerativeAI


def setup_environment():
    """Loads environment variables and checks for the required API key."""
    load_dotenv()
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("GOOGLE_API_KEY not found. Please set it in your .env file.")


def main():
    """
    Initializes and runs the AI crew for content creation using the latest Gemini model.
    """
    setup_environment()

    # Define the language model to use.
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

    # Define Agents with specific roles and goals
    researcher = Agent(
        role='Senior Research Analyst',
        goal='Find and summarize the latest trends in AI.',
        backstory="You are an experienced research analyst with a knack for identifying key trends and synthesizing information.",
        verbose=True,
        allow_delegation=False,
    )

    writer = Agent(
        role='Technical Content Writer',
        goal='Write a clear and engaging blog post based on research findings.',
        backstory="You are a skilled writer who can translate complex technical topics into accessible content.",
        verbose=True,
        allow_delegation=False,
    )

    # Define Tasks for the agents
    research_task = Task(
        description="Research the top 3 emerging trends in Artificial Intelligence in 2024-2025. Focus on practical applications and potential impact.",
        expected_output="A detailed summary of the top 3 AI trends, including key points and sources.",
        agent=researcher,
    )

    writing_task = Task(
        description="Write a 500-word blog post based on the research findings. The post should be engaging and easy for a general audience to understand.",
        expected_output="A complete 500-word blog post about the latest AI trends.",
        agent=writer,
        context=[research_task],
    )

    # Create the Crew
    blog_creation_crew = Crew(
        agents=[researcher, writer],
        tasks=[research_task, writing_task],
        process=Process.sequential,
        llm=llm,
        verbose=2 # Set verbosity for detailed crew execution logs
    )

    # Execute the Crew
    print("## Running the blog creation crew with Gemini 2.0 Flash... ##")
    try:
        result = blog_creation_crew.kickoff()
        print("\n------------------\n")
        print("## Crew Final Output ##")
        print(result)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```

## Notes

Key implementation details:

- **Agent Specialization**: Researcher focuses on finding trends, writer on content creation
- **Sequential Process**: Writer task depends on researcher task via context parameter
- **Task Dependencies**: Writer receives researcher output through context array
- **Role-Based Design**: Each agent has distinct role, goal, and backstory
- **Error Handling**: Try-except block catches crew execution failures
- **Verbosity Control**: Different verbosity levels for agents and crew for debugging
