import os
from langchain_groq import ChatGroq
from langchain_community.llms import LlamaCpp
from langchain_core.prompts import ChatPromptTemplate
import time
from langchain.chains import LLMChain

api_key_1 = "YOUR_API_KEY"


def chat_response_qroq(question):
  
  # Define Prompt
  prompt= ChatPromptTemplate.from_template("""
 You are a medical consultant AI chatbot designed to assist users in providing accurate and reliable answers and health advices based on questions asked. Your focus is on women's reproductive health, but you can also address general health concerns. 
 You can ask few follow up questions to gather more information about the user's symptoms or to get clarity in order to provide appropriate answer and advice.
 In a very brief and concise manner of about 200 words, provide the user with the necessary information and advice based on the chat history provided.
 Remember to be friendly, conversational and supportive in your tone, as users may be seeking help for sensitive health issues and Always make sure that you're returning the answer without much explanation. 
 Chat History: {input}
  """ )

  llm=ChatGroq(temperature=0, model_name="llama-3.3-70b-versatile", api_key = api_key_1 )
  llm_chain = LLMChain(llm=llm, prompt=prompt)
  response = llm_chain.invoke({'input': question})['text']
  return response


# Streamed response emulator
def response_generator(response):
    for word in response.split(" "):
        yield word + " "
        time.sleep(0.05)
