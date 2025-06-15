from textwrap import dedent

from langflow.components.input_output import ChatOutput, TextInputComponent
from langflow.components.languagemodels import OpenAIModelComponent
from langflow.components.prompts import PromptComponent
from langflow.graph import Graph


def mianar_graph(template: str | None = None):
    if template is None:
        template = dedent(
            """You are assisting with implementing the MiaNar repository. The project aims to transform text into dynamic audio experiences and enable agent-driven workflows and real-time collaboration. Implement the following features:\n\n- Database Integration: persistent storage using providers such as Supabase, Neon, or MongoDB Atlas.\n- Authentication Enhancements: rate limiting, role-based access control, and OAuth integration.\n- Agent Communication Improvements: WebSocket transport with encryption and queued delivery.\n- Audio Generation System: server-side text-to-speech with advanced parameters.\n- Performance Export: downloadable audio files with metadata.\n- Real-Time Collaboration: multiple users editing simultaneously with conflict resolution.\n\nRespond to the user's request with guidance or code suggestions."""
        )

    user_input = TextInputComponent(_display_name="User Request")

    prompt_component = PromptComponent()
    prompt_component.set(template=template, user_input=user_input.text_response)

    llm = OpenAIModelComponent()
    llm.set(input_value=prompt_component.build_prompt)

    chat_output = ChatOutput()
    chat_output.set(input_value=llm.text_response)

    return Graph(
        start=user_input,
        end=chat_output,
        flow_name="MiaNar Implementation",
        description="Generate guidance for implementing MiaNar features.",
    )
