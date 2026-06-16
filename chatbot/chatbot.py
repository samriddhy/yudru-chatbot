#import ollama

#messages = []
#print("Chatbot ready! Type 'quit' to exit.")

"""while True:
    user_input = input("You: ")
    if user_input.lower() == 'quit':
        break
    
    messages.append({"role": "user", "content": user_input})
    
    response = ollama.chat(
        model="llama3.2:1b",
        messages=messages
    )
    
    reply = response['message']['content']
    print(f"Bot: {reply}\n")
    
    messages.append({"role": "assistant", "content": reply})"""
import ollama

# Load startup info from file
with open("startup_info.txt", "r") as f:
    startup_info = f.read()

SYSTEM_PROMPT = f"""You are Maya, assistant for your drone startup.

Here is everything you need to know about the startup:
{startup_info}

Never say you are made by Meta or any other company.
You are Maya, a helpful assistant for a Yudru technologies.
You help new visitors, potential clients, and team members understand the startup.
Always introduce yourself as Maya when greeted.
If asked about specific drone projects, say the details are in our project documents.
Never say you are an AI made by Meta or any other company.
You are Maya, the startup's dedicated assistant."""


# System prompt goes here as the FIRST message
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

print("Drone Startup Assistant is ready!")
print("Type 'quit' to exit\n")

while True:
    user_input = input("You: ")
    
    if user_input.lower() == 'quit':
        break
    
    messages.append({
        "role": "user",
        "content": user_input
    })
    
    response = ollama.chat(
        model="llama3.2:1b",
        messages=messages
    )
    
    reply = response['message']['content']
    
    print(f"\nBot: {reply}\n")
    print("-" * 50)
    
    messages.append({
        "role": "assistant",
        "content": reply
    })
