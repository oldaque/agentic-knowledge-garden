---
name: "Multi-Agent Blog Creation with CrewAI"
objective: "Demonstrates a multi-agent system using CrewAI to research and write a blog post."
how_to_run: "Requires CrewAI, LangChain, and a Google API key. Run with `python your_script_name.py`."
from_note: "../patterns/multi-agent.md"
---

# Multi-Agent Blog Creation with CrewAI

This snippet illustrates a multi-agent system for content creation using CrewAI. It defines two agents, a researcher and a writer, who collaborate to produce a blog post about AI trends.

## Code Example

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

## How It Works

1.  **Environment Setup**: The script first loads environment variables, ensuring a Google API key is available.
2.  **Agent Definition**: Two distinct agents, a `researcher` and a `writer`, are created with specific roles, goals, and backstories.
3.  **Task Definition**: Each agent is assigned a `Task`. The `research_task` is to find AI trends, and the `writing_task` is to write a blog post based on the context of the research task.
4.  **Crew Formation**: A `Crew` is formed with the agents and their tasks. The process is set to `sequential`, meaning the tasks will be executed one after the other.
5.  **Execution**: The `kickoff` method starts the crew's work. The researcher will first execute its task, and its output will be passed as context to the writer's task. The final result is the completed blog post.

```