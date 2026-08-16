import os
from openai import OpenAI

key=input("enter the api_key: ")

messages=[]
client=OpenAI( api_key=key,)
def completion(message):
    global messages
    messages.append({
        "role":"user",
        "content": message
    })
    chat_completion=client.chat.completions.create(messages=messages,model="gpt-4o")

    message={
        "role":"assitant",
        "content": chat_completion.choice[0].message.content 
    }
    messages.append(message)
    print(f"jarvis:{message["content"]}")
if __name__=="__main__":
    print(f"jarvis: hey i am jarvis , how can i help you?\n")
    while True:
        user_question=input()
        print(f"user: {user_question}")
        completion(user_question)
