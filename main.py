from fastapi import FastAPI
app = FastAPI()

def get_agent_response(message: str):
    return f"user asked about {message} and Agent Response is this =====>"

@app.get("/")
async def home():
    return {"message": "Welcome to AI Startup Tech Advisor build on Open AI Agent SDK"}
@app.get("/{message}")
async def hello(message: str):
    result = get_agent_response(message)
    return {"user_message": message,"agent_response": result}