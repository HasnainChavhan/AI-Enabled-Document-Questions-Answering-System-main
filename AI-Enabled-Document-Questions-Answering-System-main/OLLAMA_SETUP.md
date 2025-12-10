# Ollama Setup Instructions

## Prerequisites
1. Install Ollama from https://ollama.ai/
2. Pull the required model: `ollama pull mistral`

## Quick Start
```bash
# Start Ollama service
ollama serve

# In another terminal, install dependencies
pip install -r requirement.txt

# Run the application
streamlit run app.py
```

## Model Options
- Default: `mistral` (excellent multilingual support)
- Alternative: `llama3.2` (good general performance)
- Alternative: `llama3.2:1b` (faster, smaller model)

## Change Model
Edit `voice_functions.py` line 42:
```python
"model": "your-preferred-model"
```

## Troubleshooting
- Ensure Ollama is running on port 11434
- Check model is downloaded: `ollama list`
- Verify connection: `curl http://localhost:11434/api/tags`