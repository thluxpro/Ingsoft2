import openai
import readline

try:
    import readline
except ImportError:
    import pyreadline as readline

# Coloca tu API KEY aquí
openai.api_key = "tu-api-key"

def obtener_consulta():
    try:
        consulta = input("Ingrese su consulta: ").strip()
        if not consulta:
            raise ValueError("La consulta no puede estar vacía.")
        readline.add_history(consulta)  # Guarda en historial para usar ↑
        print(f"You: {consulta}")
        return consulta
    except Exception as e:
        print(f"Error en la entrada del usuario: {e}")
        return None

def procesar_consulta(consulta):
    try:
        mensajes = [
            {"role": "system", "content": "Eres un asistente útil."},
            {"role": "user", "content": consulta}
        ]
        return mensajes
    except Exception as e:
        print(f"Error al preparar los mensajes: {e}")
        return None

def invocar_chatgpt(mensajes):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=mensajes,
            temperature=1,
            max_tokens=150,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        respuesta_texto = response.choices[0].message["content"]
        print(f"chatGPT: {respuesta_texto}")
    except Exception as e:
        print(f"Error al invocar chatGPT: {e}")

def main():
    while True:
        consulta = obtener_consulta()
        if not consulta:
            continue
        mensajes = procesar_consulta(consulta)
        if not mensajes:
            continue
        invocar_chatgpt(mensajes)

if __name__ == "__main__":
    main()
