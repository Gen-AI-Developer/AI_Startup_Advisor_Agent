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
business_model_dev_analyst_agent : Agent = Agent(
    name="Business Model Development Analyst",
    instructions="",
    model=LitellmModel(model="gemini/gemini-2.0-flash",api_key=gemini_api_key),
    )
swot_analysis_agent : Agent = Agent(
    name="SWOT Analysis Agent",
    instructions="",
    model=LitellmModel(model="gemini/gemini-2.0-flash",api_key=gemini_api_key),
    )
gtm_strategy_agent : Agent = Agent(
    name="GTM Strategy Analyst Agent",
    instructions="",
    model=LitellmModel(model="gemini/gemini-2.0-flash",api_key=gemini_api_key),
    )
tech_stack_agent : Agent = Agent(
    name="Tech Stack Analyst Agent",
    instructions="",
    model=LitellmModel(model="gemini/gemini-2.0-flash",api_key=gemini_api_key),
    )
async def general_agent_response(user_query:str):
    result = await Runner.run(agent,user_query)
    return result.final_output