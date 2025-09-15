import gradio as gr # Import the Gradio library for building UIs
from chatbot import chatbot # Import the AI chatbot function from the app module
import json # Import the json library for handling JSON data
import os # Import the os library for interacting with the operating system

# Load branding data from the branding.json file
with open(os.path.abspath(os.path.join(os.path.dirname(__file__), 'branding.json'))) as f:
    brand_info = json.load(f)['brand']

# Create the Gradio interface using gr.Blocks for custom layout
with gr.Blocks(theme='default', title=brand_info['organizationName']) as demo:
    # Embed the logo using HTML for centering and styling
    gr.HTML(f'''<div style="display: flex; justify-content: center; margin-bottom: 20px;">
            <img src="{brand_info['logo']['title']}" alt="{brand_info['organizationName']} Logo" style="height: 100px;">
        </div>''')
    # Create the chat interface with specified functions and branding
    gr.ChatInterface(
        fn=chatbot, # Function to call for chatbot responses
        chatbot=gr.Chatbot(height=500, avatar_images=(None, brand_info['chatbot']['avatar']), type="messages"), # Configure chatbot display
        title=brand_info['organizationName'], # Set the title of the chat interface
        description=brand_info['slogan'], # Set the description/slogan
        type="messages", # Specify the message format
        examples=[
                    ["How do you say 'hello' in French and which polite greetings should you use?"],
                    ["Can you explain the conjugation of the verb 'être' in the present tense?"],
                    ["What is the difference between 'tu' and 'vous' and when should you use each?"],
                    ["How do you form the passé composé? Give examples with regular and irregular verbs."],
                    ["When do we use the subjunctive in French? Give simple examples."],
                    ["Give me exercises to practice adjective agreement."],
                    ["Can you correct this sentence and explain the error: 'Je suis aller au marché.'?"],
                    ["How do you correctly pronounce the French 'r' sound? Practical tips."],
                    ["Translate into French: 'I have been learning French for two years.'"],
                    ["Explain the use of 'en' and 'y' with clear examples."],
                    ["Which French idiomatic expressions should I know? Give 5 examples with their meanings."],
                    ["Provide a short beginner-level dialogue for ordering at a café in French."]
                    ])

# Launch the Gradio interface when the script is executed
if __name__ == "__main__":
    demo.launch(favicon_path=brand_info['logo']['favicon']) # Launch the demo with the specified favicon path