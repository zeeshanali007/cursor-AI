# Poem Flow (CrewAI)

Small CrewAI Flow that generates a light-hearted poem about how awesome CrewAI
is. The flow delegates the creative work to the `PoemCrew`, which is configured
with YAML for easy tweaks.

## Setup
- Python `>=3.10,<3.14`
- Install [uv](https://docs.astral.sh/uv/): `pip install uv`
- Install deps: `uv install`
- Set `OPENAI_API_KEY` in your environment before running

## Run
- Generate a poem (random 1-5 sentences): `uv run kickoff`
- Choose a sentence count: `uv run python -m hello_flow.main --sentences 3`
- Visualize the flow (Mermaid diagram): `uv run plot` or `uv run python -m hello_flow.main --plot`

## Customize
- Agents: `src/hello_flow/crews/poem_crew/config/agents.yaml`
- Tasks: `src/hello_flow/crews/poem_crew/config/tasks.yaml`
- Flow logic: `src/hello_flow/main.py`
- Tools template: `src/hello_flow/tools/custom_tool.py`

## Notes
- Console scripts are defined in `pyproject.toml` (`kickoff`, `run_crew`, `plot`).
- The flow returns the poem, sentence count, and author metadata; you can extend
  `save_poem` to persist the output wherever you like.
