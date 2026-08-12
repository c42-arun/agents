from agents import Runner, set_tracing_export_api_key
from quiz_master_agent import quiz_master_bot
import os
import gradio as gr
from styles import CSS, JS

last_response = None

async def chat(message, history):
    global last_response
    if last_response is None:
        # first turn - noting to carry forward
        agent_input = message
    else:
        # subsequent turns - carry forward the last response
        agent_input = last_response.to_input_list() + [{"role": "user", "content": message}]

    last_response = await Runner.run(quiz_master_bot, agent_input)
    return last_response.final_output

if __name__ == "__main__":
    os.environ["OPENAI_LOG"] = "debug"
    set_tracing_export_api_key(os.getenv("OPENAI_TRACING_KEY"))

    gr.ChatInterface(
        chat,
        title="Quiz Master",
        description="Hi! I am a quiz master. On what topic can I ask you questions today?",
        chatbot=gr.Chatbot(show_label=False),
    ).launch(css=CSS, js=JS, theme=gr.themes.Base())
