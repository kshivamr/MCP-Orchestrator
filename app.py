import asyncio

from dotenv import load_dotenv
from langchain_groq import Groq

from mcp_use import MCPAgent, MCPClient
import os

async def run_memory_chat():
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    config_file = "browser_mcp.json"

    print("Initializing chat...")

    client = MCPClient.from_config_file(config_file)
    llm = Groq(model="qwen-qwq-32b")

    agent = MCPAgent(
        client=client, 
        llm=llm,
        max_steps = 15,
        memory_enabled = True
        )
    
    print("\n==== Interactive MCP Agent ====\n")
    print("Type 'exit' to quit to end the chat.\n")
    print("Type 'clear' to clear chat history.\n")
    print("===================================\n")

    try:
    # Main chat loop
        while True:
        # Get user input
            user_input = input("\nYou: ")

        # Check for exit command
            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation...")
                break

        # Check for clear history command
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared.")
                continue

        # Get agent response
            print("\Assistant: ", end="", flush=True)
 
            try:
            # Run the agent with the user input
                response = await agent.run(user_input)
                print(response)

            except Exception as e:
                print(f"\nError: {e}")

    finally:
        if client and client.session:
            await client.close_session()

if __name__ == "__main__":
    asyncio.run(run_memory_chat())
            
