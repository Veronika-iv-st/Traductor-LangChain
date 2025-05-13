from langchain.prompts import PromptTemplate
from langchain_community.llms import OpenAI
from langchain.chains import LLMChain
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

texto = input ("introduce el texto")
idioma = input ("A que idioma lo quieres traducir?")
estilo = input ("Define el estilo en el que quieres que se traduzca")

plantilla = PromptTemplate(
 input_variables=["texto", "idioma", "estilo"],
 template="traduce el siguiente texto a {idioma} con un {estilo}: {texto}"
)

llm = OpenAI(openai_api_key=openai_api_key)
cadena = LLMChain(llm=llm, prompt=plantilla)

resultado = cadena.run({
 "texto": texto,
 "idioma": idioma,
 "estilo": estilo
})

print("\nTraducción generada:")
print(resultado)