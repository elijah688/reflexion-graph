
# Reflexion Graph

A Python project leveraging **LangGraph** to create a modular **AI research pipeline** with responder, reviewer, and formatter agents. It allows automated generation, critique, and refinement of AI-generated reports.

---

## Features

* **Responder Agent** – Generates an initial report based on user prompts.
* **Reviewer Agent** – Critiques and improves the report.
* **Formatter Agent** – Formats and structures the output into a defined object.
* **Graph-Based Flow** – Nodes for each agent with conditional edges for iterative refinement.
* **Visualization** – Generates a graph representation of the workflow and saves it as an image.

---

## Installation

1. Clone the repository:

```bash
git clone git@github.com:elijah688/reflexion-graph.git
cd reflexion-graph
```

2. Create a `.env` file with required environment variables, e.g.:

```env
OPENAI_API_KEY=your_api_key_here
```

3. Install dependencies (assuming you use pip):

```bash
uv sync --locked
```

---

## Usage

You can run the pipeline using the provided Makefile target:

```bash
make run
```

This executes:

```bash
export $$(cat .env | xargs) && uv run python main.py
```

The main script will:

1. Initialize the LLM (`ChatOpenAI`) and the agents.
2. Compile the graph connecting responder → reviewer → tools → formatter.
3. Execute the graph with an initial user prompt.
4. Save a visualization of the workflow (`save_graph`).
5. Print the final AI-generated report.

---

### Example

```python
from src.state.state import State
from langchain_core.messages import HumanMessage

res = app.invoke(
    input=State(
        iteration_count=0,
        messages=[HumanMessage("how to be a bodybuilder")]
    )
)

print(get_last_message(res))  # Prints the final AI output
```

---

## Project Structure

```
src/
├─ tools/
│  ├─ tools.py      # Serper Tool (Web Search)
├─ agents/
│  ├─ responder.py      # Responder agent setup
│  ├─ reviewer.py       # Reviewer agent setup
│  └─ formatter.py      # Formatter agent setup
├─ graph/
│  └─ graph.py          # Graph structure and compilation
│  └─ save.py           # Graph visualization saving
├─ state/
│  └─ state.py          # State object definition
├─ prompt_templates/
│  ├─ responder.py      # Initial Report
│  └─ reviewer.py       # Feedback and Search Term Generation
│  └─ formatter.py      # Structured Output
main.py                 # Entry point
makefile                # Commands (run)
```

---

## Key Functions

* `make_responder_agent(llm)` – Returns a responder agent.
* `make_reviewer(llm)` – Returns a reviewer agent.
* `make_formatter(llm)` – Returns a formatter agent.
* `get_last_message(res)` – Retrieves the last message text from a response.

---

## Customizing Prompts

* The project uses **ChatPromptTemplate** to define the behavior of each agent.
* You can modify `actor_prompt_template` for the responder or reviewer instructions.
* Timestamps are automatically injected into prompts for dynamic context.

---

## Graph Workflow

1. **Responder Node** – Generates initial report.
2. **Reviewer Node** – Critiques and improves the report using search tools.
3. **Tool Node** – Handles tools calls (search).
4. **Formatter Node** – Converts report + critique into structured output.
5. **Conditional Loop** – Formatter can trigger reviewer again if under max iterations (`should_continue`).

---

## License

MIT License
