from dotenv import load_dotenv
from poml.integration.langchain import LangchainPomlTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0.7)

conversation_history = []

def chatbot(user_input, history=None):
    global conversation_history
    prompt = LangchainPomlTemplate.from_file("prompt.poml")
    history_text = "\n".join([f"Human: {h['user']}\nAssistant: {h['bot']}" for h in conversation_history[-5:]])
    context = {"question": user_input, "history": history_text}
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke(context)
    conversation_history.append({"user": user_input, "bot": response})
    if len(conversation_history) > 10:
        conversation_history.pop(0)
    return response

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        response = chatbot(user_input)
        print(f"Bot: {response}")