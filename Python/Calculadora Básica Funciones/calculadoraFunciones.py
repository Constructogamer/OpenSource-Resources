# Sustituir el valor de x en la función y devolver el resultado
def evaluar_funcion(funcion, x):
    try:
        # Evalúa la función reemplazando 'x' por el valor proporcionado
        resultado = eval(funcion.replace('x', str(x)))
        return resultado
    except Exception as e:
        # Captura cualquier error que pueda ocurrir al evaluar la función
        return f"Error al evaluar la función: {e}"

def main():

    # Título
    print("\n###############################################")
    print("#                                             #")
    print("#            CALCULADORA DE FUNCIONES         #")
    print("#                                             #")
    print("###############################################\n")

    # Solicita al usuario que introduzca una función
    funcion = input("Introduce una función (CTRL + C para salir): ")
    while True:
        try:
            # Solicita al usuario que introduzca un valor para 'x'
            x = float(input("Introduce un valor para x (CTRL + C para salir): "))
            # Llama a la función para evaluar la función con el valor de 'x'
            resultado = evaluar_funcion(funcion, x)
            # Muestra el resultado
            print(f"Resultado para x = {x}: {resultado}")
        except ValueError:
            # Captura errores si el usuario no introduce un valor numérico válido para 'x'
            print("Por favor, introduce un valor numérico válido para x.")
        except KeyboardInterrupt:
            # Maneja la interrupción del usuario (Ctrl+C) para salir del bucle
            print("\n¡Hasta luego!")
            break

if __name__ == "__main__":
    main()