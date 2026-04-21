"""Example: Agno Agent with Finance tools

This example shows how to create an Agno Agent with tools (YFinanceTools) and expose it in an AG-UI compatible way.
"""

from agno.agent.agent import Agent
from agno.models.openrouter import OpenRouter
from agno.tools.yfinance import YFinanceTools

from .tools.backend import get_weather
from .tools.frontend import add_proverb, set_theme_color

agent = Agent(
    model=OpenRouter(id="x-ai/grok-4.1-fast", max_tokens=1500000),
    tools=[
        # Example of backend tools, defined and handled in your agno agent
        YFinanceTools(),
        get_weather,
        # Example of frontend tools, handled in the frontend Next.js app
        add_proverb,
        set_theme_color,
    ],
    description="You are an demonstrative agent for Agno and CopilotKit's integration.",
    instructions="Format your response using markdown and use tables to display data where possible.",
)
