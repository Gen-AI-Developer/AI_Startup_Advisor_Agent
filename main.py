from fastapi import FastAPI
from myagents import myagents
from fastapi.responses import StreamingResponse
from openai.types.responses import ResponseTextDeltaEvent

app = FastAPI(
    title="AI Startup Tech Advisor",
    description="An AI-powered advisor for startup technology decisions",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome  to AI Startup Tech Advisor API"}

async def generate_response(message: str):
    result = myagents.main_agent_response(message)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            yield f"data: {event.data.delta}\n\n"

@app.get("/message/{message}")
async def agentic_response(message: str):
    """
    This endpoint receives a message and returns a streaming response from the main agent.
    """
    return StreamingResponse(
        generate_response(message[1:]),
        media_type="text/event-stream"
    )
