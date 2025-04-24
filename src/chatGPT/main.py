import openai

"""
Script principal que permite enviar consultas a la API de ChatGPT.
Gestiona errores, permite reusar la última consulta y entrega la respuesta en consola.
"""

import openai

# Clave de API (reemplazar con tu propia key)
openai.api_key = "TU_API_KEY_AQUI"

# Variable para recordar la última consulta ingresada
ultima_consulta = ""

def enviar_consulta(prompt):
    """Envía un prompt a ChatGPT y muestra la respuesta."""
    try:
        print("You:", prompt)
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sos un asistente útil."},
                {"role": "user", "content": prompt}
            ],
            temperature=1,
            max_tokens=500
        )
        mensaje = response.choices[0].message["content"]
        print("chatGPT:", mensaje)

    except openai.error.OpenAIError as e:
        print("Error con la API de OpenAI:", str(e))
    except Exception as e:
        print("Error inesperado:", str(e))  # Aún usamos broad catch como respaldo

def main():
    """Solicita una consulta del usuario y llama a la API."""
    global ultima_consulta

    try:
        consulta = input("Ingrese su consulta (o ↑ para repetir la última): ").strip()
        if not consulta:
            print("Consulta vacía.")
            return
        if consulta == "↑" and ultima_consulta:
            consulta = ultima_consulta
        else:
            ultima_consulta = consulta
    except Exception as e:
        print("Error en la entrada:", str(e))
        return

    try:
        enviar_consulta(consulta)
    except Exception as e:
        print("Error en el procesamiento:", str(e))

if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("\nSaliendo.")
            break
