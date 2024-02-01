# SEO Strategy AI Companion

SEO Strategy AI Companion is a web application designed to leverage the latest in natural language processing to help content creators, marketers, and SEO specialists find and utilize current trends in their articles and online content. This application uses the Cohere platform to analyze internet trends and provide insights for writing highly relevant and optimized articles.

## Features

- Analyze current internet trends relevant to your niche or industry for content creation
- Generate suggestions and insights for SEO-optimized articles using the Cohere model
- Get up-to-date recommendations on keywords and topics that are currently trending
- Learn how to structure your articles for better search engine visibility and engagement

## Installation

To run this application, you need to have Python 3.8 or higher installed on your system. Additionally, you'll need to obtain a Cohere API key and store it securely. Follow these steps to set up and run the application:

### Getting a Cohere API Key

- Visit the Cohere website at [https://cohere.com](https://cohere.com).
- Sign up for an account or log in if you already have one.
- Navigate to the API keys section and generate a new API key.
- Store this API key in the `.env` file as described in the next steps.

### Setup Instructions

#### For Mac

- Open a terminal and navigate to the directory where you want to clone this repository.
- Run the following command to clone this repository:

    ```bash
    git clone https://github.com/aiproduct-creators/seo-ai.git
    ```
- Navigate to the cloned repository:

    ```
    cd seo-ai
    ```
- Create a virtual environment and activate it:
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
- Install the required packages:
    ```
    pip install -r requirements.txt
    ```
- Copy the `.env.example` file to a new file named `.env` and set your Cohere API key:
    ```
    CO_API=your_api_key_here
    ```
- Run the application:
    ```
    streamlit run app.py
    ```
    Open your browser and go to http://localhost:8501 to see the app.

#### For Windows

- Open a command prompt and navigate to the directory where you want to clone this repository.
- Run the following command to clone this repository:
    ```
    git clone https://github.com/aiproduct-creators/seo-ai.git
    ```
- Navigate to the cloned repository:

    ```
    cd seo-ai
    ```
- Create a virtual environment and activate it:
    ```
    python -m venv venv
    venv\Scripts\activate
    ```
- Install the required packages:
    ```
    pip install -r requirements.txt
    ```
- Copy the `.env.example` file to a new file named `.env` and set your Cohere API key:
    ```
    CO_API=your_api_key_here
    ```
- Run the application:
    ```
    streamlit run app.py
    ```
Open your browser and go to http://localhost:8501 to see the app.

