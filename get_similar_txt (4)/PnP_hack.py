#Note: The openai-python library support for Azure OpenAI is in preview.
import os
import openai
openai.api_type = "azure"
openai.api_base = "https://hackathon-coreteam-poc.openai.azure.com/"
openai.api_version = "2022-12-01"
openai.api_key = "e51568c5adb2410f9e5747317871c3d9"
import time

import get_similar_txt as sim_txt

start_time = time.time()

# url_domain = "financialservices"

def get_ai_response(url_domain,query):
  # url_domain = "incometaxindia"

  # file1 = open(f"./webData/{url_domain}.txt","r+", encoding="utf-8")
  # data = file1.read()
  # file1.close()

  # query = "what is the minimum pension?"
  # query = "who can benefit from new tax regime?"

  data = sim_txt.get_similarity(url_domain,query)

  if len(data) > 4000:
      data = data[:4000]

  # openai.api_base = "https://acchackathonopenai03.openai.azure.com/"
  # openai.api_version = "2022-12-01"
  # openai.api_key = "8e2bb8ee70904a9c8da53148bfe66dd7"
  # # "gpt-35-turbo"c
  # oscar_chatbot

  # Endpoint: https://hackathon-coreteam-poc.openai.azure.com/
  # Key: e51568c5adb2410f9e5747317871c3d9
  # "gpt35turbo"


  prompt_data=f'''Context: {data}
      
      Question: {query}'''




  response = openai.chat.Completion.create(
    engine="oscar_chatbot",
    prompt=prompt_data,
    temperature=0,
    max_tokens=100,
    top_p=0.5,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)

  # print("response -----",response)  
  # print("response---",response["choices"][0]["text"])
  response_txt = response["choices"][0]["text"]
  response_txt = response_txt.strip()
  response_txt = response_txt.strip("Answer:")
  print("--execution time-----",time.time()-start_time)

  return response_txt


# url_domain = "incometaxindia"
# query = "who can benefit from new tax regime?"
# get_ai_response(url_domain,query)