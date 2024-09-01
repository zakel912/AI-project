from utils.db_agent_manager import db_agent_executor, memory

def main():
    print("Bot: Hello! How can I assist you today?")
    
    while True:
        user_message = input("You: ").strip().lower()
        # Retrieve the chat history from the memory buffer
        chat_history = memory.buffer_as_messages
        # Prepare the inputs for the AI model, including the user's message and chat history
        inputs = {
            "message": user_message,
            "chat_history" : chat_history,
        }
        
        try:
            # Invoke the AI model using the provided inputs
            response = db_agent_executor.invoke(inputs)
            print(f"Bot: {response['output']}")
        except Exception as e:
            print(f"Bot: Sorry, I encountered an error: {e}")

if __name__ == "__main__":
    main()
