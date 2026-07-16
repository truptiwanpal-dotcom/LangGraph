# LangGraph Chatbot

A conversational AI chatbot built with LangGraph and Streamlit, powered by OpenAI's language models.

## Features

- Real-time chat interface using Streamlit
- LangGraph-based state management for conversations
- OpenAI integration for intelligent responses
- Message history tracking
- Thread-based conversation checkpointing

## Project Structure

```
├── langgraph_backend.py      # LangGraph chatbot logic
├── streamlit_frontend.py     # Streamlit user interface
├── requirements.txt          # Python dependencies
├── .env                      # Environment variables (not committed)
└── README.md                 # This file
```

## Setup

### Prerequisites

- Python 3.8 or higher
- OpenAI API key

### Installation

1. Clone the repository:
```bash
git clone https://github.com/truptiwanpal-dotcom/LangGraph.git
cd LangGraph
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your API keys:
```
OPENAI_API_KEY=your_openai_api_key_here
```

## Usage

Run the Streamlit app:
```bash
streamlit run streamlit_frontend.py
```

The app will open in your default browser at `http://localhost:8501`

## Components

### langgraph_backend.py
- Defines the `ChatState` typed dictionary
- Implements the `chat_node` function for processing messages
- Sets up the LangGraph with checkpointing support
- Compiles the graph with an in-memory checkpointer

### streamlit_frontend.py
- Provides the user interface for chat interactions
- Manages message history in Streamlit session state
- Displays chat messages with proper roles
- Sends messages to the backend for processing

## Architecture

The chatbot uses LangGraph to manage conversation state:
1. User input is captured through Streamlit
2. Messages are passed to the LangGraph chatbot
3. The LangGraph processes the state through the chat node
4. The AI generates a response using OpenAI
5. The response is displayed and stored in history

## Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `ANTHROPIC_API_KEY`: Anthropic API key (optional)
- `GOOGLE_API_KEY`: Google API key (optional)
- `HUGGINGFACEHUB_API_TOKEN`: Hugging Face API token (optional)

## License

This project is open source and available under the MIT License.

## Author

Trupti Wanpal
