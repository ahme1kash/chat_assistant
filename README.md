# Chat Assistant OpenAI Based Application which can reply to the use on giving the prompt.

## Utilities
1. Streamlit- Streamlit is an open-source Python framework for machine learning and data science teams.Streamlit turns data scripts into shareable web apps in minutes.
All in pure Python. No front‑end experience required.

2. OpenAI- OpenAI is widely known for its Generative Pre-trained Transformer (GPT) models, such as GPT-3 and GPT-4. These models are capable of understanding and generating human-like text, making them useful for a wide range of applications, including natural language processing, content creation, and conversation agents.

3. audio_recorder_streamlit- Streamlit's audio library for recording voice  and procesing chat.



## Usage

A User can have one to one conversation with the chatbot powered by GPT3 model transformer API.
We can ask questions from daily chores and todos, from making of Pizza recipe to intriguing topics of physics,History,Genetics. Actually AskAnything!

## Installation and Application

Step 1. Clone the repository by entering command on cmd-prompt ```git clone https://github.com/ahme1kash/chat_assistant.git ```

Step 2. Execute ``` pip freeze > requirements.txt``` to get all the requirements and dependencies to successfully execute the application. It will generate a new ```requirements.txt``` file in the folder.

Step 3. Install all dependencies by running ```pip install -r requirements.txt```.
 
Step 4. Run the application by executing ``` streamlit run app.py```

Step 5. Input the OpenAI-ChatPT API key by purchasing key from https://openai.com/api/pricing/

## Application Interface

1. ![image](https://github.com/ahme1kash/chat_assistant/assets/48543242/808ecd11-4ac6-479f-8216-d5bf5a99056c)

2. ![image](https://github.com/ahme1kash/chat_assistant/assets/48543242/8c47545f-2c62-440c-a249-d9db8664f35c)



## Deployment

Chat Application is deployed on https://streamlit.io/cloud and one can see the deployed app on clicking the 
https://chatassistant.streamlit.app/

One can Deploy Streamlit Applications for showcase purpose very easily on Streamlit cloud community  just by signing up with the service and granting access to github repository.


## Scope of Improvements

This application can be further improved by storing all the chats on 3rd party NOSQL-Database and sending the entire chats to API so that user can do flowing conversation rather than one-time prompt and reply.
