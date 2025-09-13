# BTech4thYear-Agentic-AI-Your-Financial-Copilot
  
## Agentic AI: Your Financial Copilot

**Description:**
GenAI assistant answering finance questions using Agentic AI, LLM, and prompt engineering. Includes a basic Flask frontend for user interaction.

## Features
- Ask finance questions to an AI assistant
- Simple web interface
- Demonstrates a sample bug for learning

## Installation
1. Clone the repository:
	```powershell
	git clone https://github.com/finvediclabs/BTech4thYear-Agentic-AI-Your-Financial-Copilot.git
	cd BTech4thYear-Agentic-AI-Your-Financial-Copilot
	```
2. Install requirements:
	```powershell
	pip install -r requirements.txt
	```
3. Set your OpenAI API key (fixes the bug):
	- Open `app/main.py` and replace `openai.api_key = None` with:
	  ```python
	  import os
	  openai.api_key = os.getenv('OPENAI_API_KEY')
	  ```
	- Or set the environment variable:
	  ```powershell
	  $env:OPENAI_API_KEY = "your-api-key-here"
	  ```

## Running the App
```powershell
python app/main.py
```

## How to Fix the Bug
- The bug is in `app/main.py`: `openai.api_key = None`.
- Fix by setting the API key from an environment variable as shown above.

## Requirements
- Python 3.8+
- Flask
- OpenAI

## Theme
Agentic AI + LLM + Prompt Engineering