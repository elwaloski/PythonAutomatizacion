import os
import sys

def obtener_directorio_ejecucion():
    """Retorna la ruta donde está el .exe o el .py ejecutándose."""
    if getattr(sys, 'frozen', False):  # Cuando está empaquetado como .exe
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def leer_configuracion(ruta):
    """
    Lee un archivo de configuración con formato:
    clave valor
    Ignora líneas vacías o que comiencen con '#'.
    """
    config = {}

    if not os.path.isfile(ruta):
        raise FileNotFoundError(f"No se encontró el archivo de configuración: {ruta}")

    with open(ruta, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            linea = linea.strip()
            if not linea or linea.startswith('#'):
                continue

            partes = linea.split(None, 1)
            if len(partes) == 2:
                clave, valor = partes
                config[clave.lower()] = valor.strip()

    return config


def listar_archivos_en_carpeta(carpeta):
    """Devuelve solo los archivos dentro de una carpeta."""
    try:
        return [
            f for f in os.listdir(carpeta)
            if os.path.isfile(os.path.join(carpeta, f))
        ]
    except Exception as e:
        raise RuntimeError(f"Error al listar archivos: {e}")


def abrir_archivo_windows(ruta):
    """Abre un archivo en Windows si existe."""
    try:
        os.startfile(ruta)
    except Exception:
        pass  # En un servicio podría fallar, así evitamos romper la ejecución.


def main():
    directorio = obtener_directorio_ejecucion()
    ruta_config = os.path.join(directorio, "config.txt")
    ruta_salida = os.path.join(directorio, "ListaDeArchivos.txt")

    try:
        config = leer_configuracion(ruta_config)
    except Exception as e:
        print(f"❌ Error al leer configuración: {e}")
        sys.exit(1)

    carpeta = config.get("carpeta")

    if not carpeta:
        print("❌ Error: Falta la clave 'carpeta' en config.txt")
        sys.exit(1)

    if not os.path.isdir(carpeta):
        print(f"❌ Error: La carpeta '{carpeta}' no existe.")
        sys.exit(1)

    try:
        archivos = listar_archivos_en_carpeta(carpeta)
    except Exception as e:
        print(f"❌ {e}")
        sys.exit(1)

    # Guardar archivo de salida
    try:
        with open(ruta_salida, "w", encoding="utf-8") as salida:
            for nombre in archivos:
                salida.write(nombre + "\n")

        print(f"✅ Se guardaron {len(archivos)} archivos en: {ruta_salida}")
        abrir_archivo_windows(ruta_salida)

    except Exception as e:
        print(f"❌ Error al escribir archivo de salida: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
