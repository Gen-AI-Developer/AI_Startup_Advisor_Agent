from fastapi import FastAPI, HTTPException
from myagents import myagents
from pydantic import BaseModel
from agents import Agent, set_tracing_disabled, function_tool, Runner
from agents.extensions.models.litellm_model import LitellmModel
import os
gemini_api_key = os.getenv('GEMINI_API_KEY')
set_tracing_disabled(disabled=True)
agent : Agent = Agent(
    name="Assitant",
    instructions="You Are Helpfull Assistant, you answer every question will short and breif to the point answer.",
    model=LitellmModel(model="gemini/gemini-2.0-flash",api_key=gemini_api_key),
    )

async def agent_response(user_query:str):
    result = await Runner.run(agent,user_query)
    return result.final_output

app = FastAPI(
    title="AI Startup Tech Advisor",
    description="An AI-powered advisor for startup technology decisions",
    version="1.0.0"
)


@app.get("/")
async def root():
    return {"message": "Welcome to AI Startup Tech Advisor API"}

@app.get("/{message}")
async def agentic_response(message:str):
    result = await agent_response(message)
    return {"RESPONSE":result}
