import pandas as pd

df = pd.read_csv('PJ.csv.csv')
user_ids= df['Nome'].tolist()
print(user_ids)

openai_api_key = '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'


import openai

openai.api_key =  openai_api_key

def generate_ai_news(user):
  completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo-16k",
  messages=[
    {
        "role": "system",
        "content": "você vendedor imobiliario"
        },
    {
      "role": "user",
        "content": f"(Crie uma menssagem para {user} sobre ofertas de imoveis(máximo de 100 caracteres))"
        },
  ]
  )
  return  completion.choices[0].message.content.strip('/"')

for user in user_ids:
   news= generate_ai_news(user)
   print(news)


import csv 

with open('extrair.csv','w',newline='') as csvfile:
   campos_head=['menssage']
   writer =csv.DictWriter(csvfile, fieldnames=campos_head)
   writer.writeheader()
   writer.writerow({'menssage':news})