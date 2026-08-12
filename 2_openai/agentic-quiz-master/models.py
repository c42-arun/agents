from pydantic import BaseModel, Field

class Choice(BaseModel):
    optionId: str = Field(..., description="The unique identifier for the choice option. Foe example, 'A', 'B', 'C', etc.")
    text: str = Field(..., description="The text of the choice option.")

class QuestionAndAnswer(BaseModel):
    question: str = Field(..., description="The question to be answered.")
    choices: list[Choice] = Field(..., description="The list of choice options for the question.")
    answer: str = Field(..., description="The correct answer to the question, represented by the optionId of the correct choice.")

class QuestionsAndAnswers(BaseModel):
    questions: list[QuestionAndAnswer] = Field(..., description="A list of questions and their corresponding answers.")