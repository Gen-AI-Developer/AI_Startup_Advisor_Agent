from fastapi import FastAPI, HTTPException
from myagents import myagents
from pydantic import BaseModel

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
    result = await myagents.general_agent_response(message)
    return {"RESPONSE":result}
