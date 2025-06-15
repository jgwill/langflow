from langchain.agents.react.agent import create_react_agent
from langchain_core.prompts import ChatPromptTemplate

from langflow.base.agents.agent import LCToolsAgentComponent
from langflow.inputs.inputs import DataInput, HandleInput, MessageTextInput
from langflow.schema.data import Data


class MiActAgentForChatModelsComponent(LCToolsAgentComponent):
    display_name: str = "MiAct Agent for Chat Models"
    description: str = "Agent that uses the MiAct prompting strategy with chat models."
    icon = "LangChain"
    name = "MiActAgentChat"

    inputs = [
        *LCToolsAgentComponent._base_inputs,
        HandleInput(
            name="llm",
            display_name="Chat Model",
            input_types=["LanguageModel"],
            required=True,
            info="Chat model that the agent utilizes to perform tasks effectively.",
        ),
        MessageTextInput(
            name="system_prompt",
            display_name="System Prompt",
            info="System prompt to guide the agent's behavior.",
            value="You are a helpful assistant that can use tools to answer questions and perform tasks.",
        ),
        DataInput(
            name="chat_history",
            display_name="Chat Memory",
            is_list=True,
            advanced=True,
            info="This input stores the chat history, allowing the agent to remember previous conversations.",
        ),
    ]

    def get_chat_history_data(self) -> list[Data] | None:
        return self.chat_history

    def create_agent_runnable(self):
        messages = [
            ("system", "{system_prompt}"),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
        prompt = ChatPromptTemplate.from_messages(messages)
        self.validate_tool_names()
        return create_react_agent(self.llm, self.tools or [], prompt)


class MiActAgentForLLMsComponent(LCToolsAgentComponent):
    display_name: str = "MiAct for LLMs"
    description: str = "Agent that uses the MiAct prompting strategy with LLMs."
    icon = "LangChain"
    name = "MiActAgentLLM"

    inputs = [
        *LCToolsAgentComponent._base_inputs,
        HandleInput(
            name="llm",
            display_name="Language Model",
            input_types=["LanguageModel"],
            required=True,
            info="Language model that the agent utilizes to perform tasks effectively.",
        ),
        MessageTextInput(
            name="system_prompt",
            display_name="System Prompt",
            info="System prompt to guide the agent's behavior.",
            value="You are a helpful assistant that can use tools to answer questions and perform tasks.",
        ),
        DataInput(
            name="chat_history",
            display_name="Chat Memory",
            is_list=True,
            advanced=True,
            info="This input stores the chat history, allowing the agent to remember previous conversations.",
        ),
    ]

    def get_chat_history_data(self) -> list[Data] | None:
        return self.chat_history

    def create_agent_runnable(self):
        messages = [
            ("system", "{system_prompt}"),
            ("placeholder", "{chat_history}"),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
        prompt = ChatPromptTemplate.from_messages(messages)
        self.validate_tool_names()
        return create_react_agent(self.llm, self.tools or [], prompt)
