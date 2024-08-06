from config.settings import OPENAI_API_KEY
from utils.intent_analysis import get_intent
from utils.db_agent_manager import db_agent_executor


def main():
    print("Bot: Hello! How can I assist you today?")
    
    while True:
        user_message = input("You: ").strip().lower()

        print(f"intent: {get_intent(user_message)}")    
        
        inputs = {
            "message": user_message,
            "agent_scratchpad": ""
        }
        
        try:
            response = db_agent_executor.invoke(inputs)
            print(f"Bot: {response['output']}")
        except Exception as e:
            print(f"Bot: Sorry, I encountered an error: {e}")

if __name__ == "__main__":
    main()
