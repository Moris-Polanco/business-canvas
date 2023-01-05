import openai
import streamlit as st
import os

# Autenticación de OpenAI (oculta la clave en una variable de entorno)
openai.api_key = os.environ.get("OPENAI_API_KEY")

# Crear una interfaz de usuario con streamlit
st.title("Generador de planes de negocios")
st.caption("Por Moris Polanco")

# Solicitar al usuario que ingrese su idea de negocio
wish = st.text_input("¿Qué idea tienes? Pon un solo nombre o descríbela, o deja el espacio en blanco y espera. Si quieres generar un nuevo plan, cambia al menos una letra y vuelve a presionar Enter.")

# Utilizar GPT-3 para generar un plan de negocios para la idea del usuario
model_engine = "text-davinci-003"
prompt = (f"Generar una idea de negocio basada en '{wish}'. Incluir: nombre propuesto, propuesta de valor, persona objetivo, dolores de la persona objetivo, descripción detallada de la idea, pasos de validación de la idea, socios clave, actividades clave, recursos clave, relaciones con los clientes, canales, segmentos de clientes, estructura de costes y flujos de ingresos.")

completions = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=2024,
    n=1,
    stop=None,
    temperature=0.7,
)

# Obtén el texto del resultado del plan de negocios
business_plan = completions.choices[0].text

# Crea una tabla en formato markdown con dos columnas
table = "| Categoría | Descripción |\n| --- | --- |\n"

# Separa el texto en líneas
lines = business_plan.split("\n")

# Recorre cada línea del texto
for line in lines:
  # Dividir la línea en dos partes en base al carácter ":"
  parts = line.split(":", 1)
  # Agregar cada parte a una columna de la tabla
  if len(parts) == 2:
    table += f"| {parts[0]} | {parts[1]} |\n"
  else:
    table += f"| {parts[0]} | |\n"

# Muestra la tabla en la aplicación
st.markdown(table)
