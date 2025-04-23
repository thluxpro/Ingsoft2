import openai

# Configurar tu clave de API (reemplazá esto con tu clave real)
openai.api_key = "TU_API_KEY_AQUI"

# Guardamos la última consulta para poder reutilizarla si el usuario presiona ↑
ultima_consulta = ""

def enviar_consulta(prompt):
    """
    Envía un prompt a la API de OpenAI ChatGPT y muestra la respuesta.
    También gestiona errores de conexión o uso del API.
    """
    try:
        # Mostrar el mensaje que se enviará
        print("You:", prompt)

        # Llamar al modelo de lenguaje GPT
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "Sos un asistente útil."},
                {"role": "user", "content": prompt}
            ],
            temperature=1,
            max_tokens=500
        )

        # Obtener y mostrar la respuesta del modelo
        mensaje = response.choices[0].message["content"]
        print("chatGPT:", mensaje)

    except Exception as e:
        # Si ocurre un error con la API, se muestra el mensaje
        print("Error al invocar la API:", str(e))


def main():
    """
    Función principal que recibe la consulta del usuario,
    maneja errores de entrada y llama a la función que se conecta a la API.
    """
    global ultima_consulta

    try:
        # Pedimos la consulta del usuario
        consulta = input("Ingrese su consulta (o presione ↑ para repetir la última): ").strip()

        # Validamos si está vacía
        if not consulta:
            print("Consulta vacía. Intente nuevamente.")
            return

        # Si el usuario ingresa ↑ y hay una consulta anterior, la usamos
        if consulta == "↑" and ultima_consulta:
            consulta = ultima_consulta
        else:
            # Guardamos la nueva consulta como la última
            ultima_consulta = consulta

    except Exception as e:
        # Si hubo error al ingresar datos
        print("Error en la lectura de entrada:", str(e))
        return

    try:
        # Enviamos la consulta a ChatGPT
        enviar_consulta(consulta)
    except Exception as e:
        # Captura errores de procesamiento
        print("Error en el procesamiento:", str(e))


# Ejecutar el programa en bucle hasta que el usuario lo corte
if __name__ == "__main__":
    while True:
        try:
            main()
        except KeyboardInterrupt:
            print("\nSaliendo del programa.")
            break
