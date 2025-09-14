# Hugging Face Space Creation

## Setup

To use the `create_space.py` script, you need to set your Hugging Face token as an environment variable:

1. Get your token from: https://huggingface.co/settings/tokens
2. Set the environment variable:

```bash
export HUGGINGFACE_TOKEN="hf_your_token_here"
```

Or create a `.env` file (which is already gitignored):
```
HUGGINGFACE_TOKEN=hf_your_token_here
```

## Usage

```bash
python create_space.py
```

This will create a new Hugging Face Space for your Gradio chatbot application.

## Security Note

Never commit tokens or API keys to git repositories. Always use environment variables or secure configuration files that are excluded from version control.
