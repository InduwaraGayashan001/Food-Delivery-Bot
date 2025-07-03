# FoodieBite

An AI-powered restaurant ordering assistant built with Chainlit that helps customers place food orders through natural language conversation.

![im](/resources/start.png)

## Features

- **Interactive Menu Browsing** - Explore pizzas, burgers, salads, desserts, and beverages
- **Smart Order Taking** - Natural language order processing with customization options
- **Order Calculation** - Automatic total calculation
- **Conversational Interface** - Friendly, chat-based ordering experience

## Tech Stack

- **Framework**: Chainlit
- **AI Model**: OpenAI GPT-4.1-mini (via GitHub Models)
- **Backend**: Python


## Getting Started

### Prerequisites

- [Conda](https://docs.conda.io/en/latest/miniconda.html) (for backend Python environment)
- [OpenAI API Key](https://platform.openai.com/account/api-keys) **or** a GitHub access token (see note below)
- [pip](https://pip.pypa.io/en/stable/)

> **Note:**  
> You can use a GitHub access token as the API key for the OpenAI client in this project.  
> See [here](https://github.com/marketplace/models/azure-openai/gpt-4o-mini) for more details.

### **Installation**

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd Food-Delivery-Bot
   ```

2. **Create conda environment**
   ```bash
   conda create -n foodiebite python=3.9 -y
   conda activate foodiebite
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in your project root:
     ```
     OPENAI_API_KEY=your_openai_api_key_or_github_token
     ```

5. **Run the application**
   ```bash
   chainlit init
   chainlit run app.py
   ```

## Usage

1. Open your browser to `http://localhost:8000`

    ![im](/resources/start.png)

2. Start a conversation with FoodieBite

    ![im](/resources/ask.png)

3. Browse the menu and place your order

    ![im](/resources/menu.png)

4. Choose pickup or delivery

    ![im](/resources/delivery.png)

5. Complete your order with payment

    ![im](/resources/pay.png)

---

>**Note**: This project is for educational purposes only to explore Chainlit framework capabilities through a simple chatbot application.
