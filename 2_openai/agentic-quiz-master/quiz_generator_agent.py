from agents import Agent

from models import QuestionsAndAnswers
from constants import MODEL_NAME

INSTRUCTIONS = """
You are a questions generator. Generate a set of multiple-choice questions with four options each. Each question should have one correct answer. 
The questions should be clear and concise, and the options should be plausible to make the quiz challenging.
"""
questions_generator_agent = Agent(
    name="QuestionsGenerator",
    instructions=INSTRUCTIONS,
    output_type=QuestionsAndAnswers,
    model=MODEL_NAME
    )

questions_generator_agent_tool = questions_generator_agent.as_tool(tool_name="questions_generator", tool_description="Generates multiple-choice questions with four options each.")
