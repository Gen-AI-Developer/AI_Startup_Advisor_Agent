from agents import Agent, set_tracing_disabled, Runner
from agents.extensions.models.litellm_model import LitellmModel
import _asyncio
import os
gemini_api_key = os.getenv('GEMINI_API_KEY')
# from pydantic import BaseModel
# import litellm
# litellm._turn_on_debug()
MODEL = LitellmModel(
    model="gemini/gemini-2.0-flash",
    api_key=gemini_api_key,
    )
set_tracing_disabled(disabled=True)
# agent : Agent = Agent(
#     name="Assitant",
#     instructions="You Are Helpfull Assistant, you answer every question will short and breif to the point answer.",
#     model=LitellmModel(model="gemini/gemini-2.0-flash",api_key=gemini_api_key),
#     )
# class AgentOutput(BaseModel):
#         overview_of_the_startup_idea : str
#         business_model : str
#         swot_analysis : str
#         gtm_strategy : str
#         suitable_tech_stack : str
#         tips_and_suggestions_for_the_startup : str

generate_business_model_deve_analyst_agent : Agent = Agent(
    name="Business Model Development Analyst",
    handoff_description="""
        You are a business strategist AI Agent. Given a startup idea, generate a business model canvas including:
        - Value Proposition
        - Customer Segments
        - Revenue Streams
        - Key Activities
        - Channels
        - Cost Structure
        """,
    instructions="""
        You are a business strategist AI Agent. Given a startup idea, generate a business model canvas including:
        - Value Proposition
        - Customer Segments
        - Revenue Streams
        - Key Activities
        - Channels
        - Cost Structure
        """,
    model=MODEL
    )
generate_swot_analysis_agent : Agent = Agent(
    handoff_description="""
        You are a market analysis agent. For a given startup idea, return a SWOT analysis with:
        - Strengths
        - Weaknesses
        - Opportunities
        - Threats
        """,
    name="SWOT Analysis Agent",
    instructions="""
        You are a market analysis agent. For a given startup idea, return a SWOT analysis with:
        - Strengths
        - Weaknesses
        - Opportunities
        - Threats
        """,
    model=MODEL,
    )
generate_gtm_strategy_deve_agent : Agent = Agent(
    name="GTM Strategy Development Analyst Agent",
    handoff_description="""
        You are a go-to-market strategist Agent. For a given startup idea, provide a GTM strategy including:
        - Target Audience
        - Marketing Channels
        - Launch Strategy
        - Sales Funnel
        """,
    instructions="""
        You are a go-to-market strategist Agent. For a given startup idea, provide a GTM strategy including:
        - Target Audience
        - Marketing Channels
        - Launch Strategy
        - Sales Funnel
        """,
     model=MODEL,
    )
recommend_tech_stack_agent : Agent = Agent(
    name="Tech Stack Analyst Agent",
    handoff_description="""
        You are a technology stack expert analyst advisor. Based on a startup idea, suggest a full tech stack:
        - Design Architecture
        - Frontend (Nextjs/astrojs/Angular)
        - Backend (Supabase,Vercel,Custom)
        - Database (MangoDB,Vercel,SupaBase)
        - DevOps (GitOps,Google)
        - Optional: AI/ML tools if needed
        """,
    # handoff_description="""
    instructions="""
        You are a technology stack expert analyst advisor. Based on a startup idea, suggest a full tech stack:
        - Design Architecture
        - Frontend (Nextjs/astrojs/Angular)
        - Backend (Supabase,Vercel,Custom)
        - Database (MangoDB,Vercel,SupaBase)
        - DevOps (GitOps,Google)
        - Optional: AI/ML tools if needed
        """,
     model=MODEL,
    )

MainAgent_AIStartupAdvisor : Agent= Agent( 
    name="AI Startup Tech Advisor",
    instructions="""
        You are an intelligent startup advisor that coordinates between multiple expert agents / Tools.
        For a given startup idea, you must return:
        1. A detialed Overview of the startup idea
        2. Generate a business model
        3. Conduct a SWOT analysis
        4. Provide a GTM (Go-to-Market) strategy
        5. Recommend a suitable tech stack
        6. Provide tips and suggestions for the startup

        Note: Respond with complete layout plane / structure / business plane and generate a detailed structure output as described.
        """,
    model=MODEL,
    # output_type=AgentOutput,
    tools = [
        generate_business_model_deve_analyst_agent.as_tool(
            tool_name="generate_business_model_deve_analyst_agent",
            tool_description="Generates a detailed business model canvas including value proposition, customer segments, revenue streams, and cost structure based on the startup idea.",
        ),
        generate_swot_analysis_agent.as_tool(
            tool_name="generate_swot_analysis_agent",
            tool_description="Performs a full SWOT (Strengths, Weaknesses, Opportunities, Threats) analysis for a given startup idea to identify strategic factors.",
        ),
        generate_gtm_strategy_deve_agent.as_tool(
            tool_name="generate_gtm_strategy_deve_agent",
            tool_description="Creates a go-to-market strategy including launch plan, target audience, marketing channels, and sales funnel for a startup idea.",
        ),
        recommend_tech_stack_agent.as_tool(
            tool_name="recommend_tech_stack_agent",
            tool_description="Recommends a suitable technology stack (frontend, backend, database, DevOps, and AI/ML if applicable) based on the startup's needs.",
        )
    ],
    # output_type= AgentOutput,

)
def main_agent_response(user_query:str):
    result =  Runner.run_streamed(MainAgent_AIStartupAdvisor,user_query)
    return result