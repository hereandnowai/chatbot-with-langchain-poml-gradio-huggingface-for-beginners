import os
from huggingface_hub import HfApi

# Use environment variable for token (safer approach)
token = os.getenv('HUGGINGFACE_TOKEN')
if not token:
    raise ValueError("Please set HUGGINGFACE_TOKEN environment variable")

api = HfApi(token=token)

repo_id = "hereandnowai/chatbot-202509142153"

api.create_repo(
    repo_id=repo_id,
    repo_type="space",          # specifies it's a Space, not a model
    space_sdk="gradio",         # SDK type = Gradio
    private=False               # or True if you want it private
)

print(f"Space {repo_id} created successfully.")
# You can now push your local files to this repository using git commands
