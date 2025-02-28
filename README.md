# Medical Assistant

## Overview
Medical Assistant is a Streamlit-based application designed to simulate a chat interface for medical assistance. It uses the LangChain framework to process and respond to user queries. The application stores chat history and displays both user inputs and assistant responses in a visually appealing chat format.

## Features
- **Chat Interface**: Engage in a conversation with the medical assistant.
- **Session Management**: Maintains chat history across user interactions.
- **Customizable Layout**: Responsive and wide layout configuration for enhanced user experience.

## Installation
To run this application, you'll need to have Python installed on your machine. Follow the steps below to set up the environment:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/medical-assistant.git
    cd medical-assistant
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Dependencies
The application relies on the following Python libraries:
- `streamlit`
- `streamlit_chat`
- `langchain_core`
- `langchain_chains`
- `langchain_groq`

You can find the complete list of dependencies in the `requirements.txt` file.

## Usage
Once the application is running, you can interact with it by entering your queries in the chat input box. The assistant will respond based on the input provided, and the entire conversation will be displayed in a chat message format.

### Example Queries
- "What are the symptoms of the menstrual cramps?"
- "How can I improve my diet during pregnancy?"

## Code Structure
- **app.py**: The main file containing the Streamlit application code.
- **function.py**: Additional functions used within the application.
