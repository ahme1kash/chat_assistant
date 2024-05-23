import streamlit as st
from audio_recorder_streamlit import audio_recorder
import openai

# Setting page background color
page_bg_css = """
<style>
[data-testid="stAppViewContainer"] {
    background-color: #2B2B52; 
}
</style>
"""
def setup_openai_client(api_key):
    global client 
    client = openai.OpenAI(api_key=api_key)
    return client

def transcribe_audio(client,audio_path):
    with open(audio_path, "rb") as audio_file:
        transcript = client.audio.transcriptions.create(model="whisper-1",file=audio_file)
        return transcript.text

 
def openai_response(client,input_text):
    messages = [{"role":"user","content":input_text}]
    response = client.chat.completions.create(model="gpt-3.5-turbo-1106",messages=messages)
    return response.choices[0].message.content


def text_to_audio(client, text, audio_path):
    response = client.audio.speech.create(model="tts-1", voice="shimmer", input=text)
    if response:    
        with open(audio_path, "wb") as audio_file:
            audio_file.write(response.content)
        return True
    else:
        return False

def main():
    st.sidebar.title("API KEY CONFIG")
    api_key = st.sidebar.text_input("Enter Open API KEY",type= "password")
    st.markdown(page_bg_css, unsafe_allow_html=True)
    st.title("Chat Assistant  :  Lets Chat:- 🗣️🎙️")
    if api_key:
        try:
            setup_openai_client(api_key)
            st.success("API Key Provided")
            recorded_audio = audio_recorder()
            if recorded_audio:
                audio_file = "audio.mp3"
                with open(audio_file,"wb") as f:
                    f.write(recorded_audio)
                transcribe_text = transcribe_audio(client,audio_file)
                st.write("Text",transcribe_text)
                ai_resp = openai_response(client,transcribe_text)
                response_audio = "response.mp3" 
                text_to_audio(client,ai_resp,response_audio)
                st.audio(response_audio)
                st.write("OpenAI Response", ai_resp)
           
        except Exception as e:
            st.error(f"Key is Invalid")
            return
if __name__ == "__main__":
    main()