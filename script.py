import json
from usuario import Usuario  # Importar la clase Usuario del módulo usuarios

def crear_instancias_usuarios(archivo: str) -> list:
    """Lee el archivo de usuarios y crea instancias de Usuario.

    Lee el archivo de usuarios línea por línea, intenta convertir cada línea en un diccionario JSON
    y crea una instancia de Usuario a partir de los datos de cada línea.

    Args:
        archivo (str): El nombre del archivo de usuarios.

    Returns:
        list: Una lista de instancias de Usuario creadas a partir de los datos del archivo.
    """
    lista_usuarios = []

    try:
        with open(archivo, 'r') as f:
            for linea in f:
                # Intenta convertir la línea en un diccionario JSON
                try:
                    datos_usuario = json.loads(linea)
                except json.JSONDecodeError as e:
                    registrar_error(f'Error al decodificar: {str(e)}')
                    continue
                
                # Crea una instancia de Usuario a partir de los datos del diccionario
                try:
                    usuario = Usuario(datos_usuario['nombre'], datos_usuario['apellido'], 
                                      datos_usuario['email'], datos_usuario['genero'])
                    lista_usuarios.append(usuario)
                except KeyError as e:
                    registrar_error(f'Error: Clave faltante en el diccionario: {str(e)}')
                    continue

    except FileNotFoundError:
        registrar_error('Error: Archivo no encontrado')
    except Exception as e:
        registrar_error(f'Error inesperado: {str(e)}')

    return lista_usuarios


def registrar_error(mensaje: str) -> None:
    """Registra un mensaje de error en el archivo error.log.

    Args:
        mensaje (str): El mensaje de error a registrar.
    """
    with open('error.log', 'a') as f:
        f.write(f'{mensaje}\n')


if __name__ == "__main__":
    # Nombre del archivo de usuarios
    archivo_usuarios = 'usuarios.txt'

    # Crear instancias de usuarios
    lista_usuarios = crear_instancias_usuarios(archivo_usuarios)

    # Imprimir las instancias de usuarios creadas
    for usuario in lista_usuarios:
        print(f'Nombre: {usuario.nombre}, Apellido: {usuario.apellido}, Email: {usuario.email}, Género: {usuario.genero}')
