from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from agent import root_agent

# The Runner is responsible for serving the agent and handling sessions.
# This setup uses a simple in-memory session for demonstration.
runner = Runner(
    app_name="golang-tutor-app",
    agent=root_agent,
    session_service=InMemorySessionService()
)

if __name__ == "__main__":
    print("Golang Tutor Agent is ready.")
    print("To interact with this agent, you would typically use the ADK CLI or integrate it into a larger application.")
    # Example of how you might run a simple inference loop:
    #
    # print("Starting a new chat session. Type 'exit' to end.")
    # session_id = runner.start_session()
    # try:
    #     while True:
    #         user_input = input("You: ")
    #         if user_input.lower() == 'exit':
    #             break
    #         response_generator = runner.run(session_id=session_id, user_input=user_input)
    #         print("Tutor: ", end="")
    #         for chunk in response_generator:
    #             print(chunk, end="", flush=True)
    #         print()
    # finally:
    #     runner.end_session(session_id)
    #     print("\nSession ended.")

