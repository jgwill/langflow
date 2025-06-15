# MiAct Agents Story

Langflow now offers MiAct agents—custom variants of the ReAct approach tailored for your own tooling. The new components `MiAct Agent for Chat Models` and `MiAct for LLMs` allow flows to invoke LangSmith prompts `jgwill/miact-chat` and `jgwill/miact-llms`. They are available as drop-in components alongside existing agents.

With these agents you can craft flows that leverage MiAct's reasoning pattern, expanding how you orchestrate tools with language models. Developers can build and test these flows locally using the `dev_start.sh` script, which now ensures dependencies are installed before launching backend and frontend servers.
