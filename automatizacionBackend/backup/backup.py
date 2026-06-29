import json
import logging
import os
import subprocess
import sys
import time
from datetime import datetime

# Configuración del log
logging.basicConfig(
    filename="backups.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_base_path():
    """Obtiene la ruta donde está el ejecutable o el script."""
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def load_config():
    """Carga el archivo config.json."""
    config_path = os.path.join(get_base_path(), "config.json")

    if not os.path.exists(config_path):
        raise FileNotFoundError(f"No existe el archivo: {config_path}")

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def backup_database(database, config):
    """Realiza el respaldo de una base de datos."""

    folder = config["backup"]["folder"]
    os.makedirs(folder, exist_ok=True)

    output_file = os.path.join(folder, f"{database}.sql")

    command = [
        "docker",
        "exec",
        "-i",
        config["container"],
        "mysqldump",
        "-u",
        config["mysql"]["user"],
        f"-p{config['mysql']['password']}",
        database
    ]

    print(f"[{datetime.now()}] Respaldando {database}...")

    try:
        with open(output_file, "wb") as output:

            result = subprocess.run(
                command,
                stdout=output,
                stderr=subprocess.PIPE
            )

        if result.returncode == 0:
            print(f"✓ {database} OK")
            logging.info(f"{database} respaldada correctamente.")

        else:
            error = result.stderr.decode("utf-8", errors="ignore")
            print(f"✗ {database} ERROR")
            print(error)
            logging.error(f"{database}: {error}")

    except Exception as ex:
        logging.exception(ex)
        print(ex)


def backup_all():
    """Respalda todas las bases."""

    config = load_config()

    print("===================================")
    print(f"Inicio de respaldo {datetime.now()}")
    print("===================================")

    logging.info("Inicio de respaldo")

    for database in config["databases"]:
        backup_database(database, config)

    logging.info("Respaldo finalizado")

    print("===================================")
    print("Respaldo finalizado")
    print("===================================")


def service_loop():
    """Loop principal del servicio."""

    print("===================================")
    print("Servicio iniciado")
    print("===================================")

    logging.info("Servicio iniciado")

    # Guarda la última ejecución realizada
    last_execution = ""

    while True:

        try:

            config = load_config()

            if not config["schedule"]["enabled"]:
                time.sleep(30)
                continue

            now = datetime.now().strftime("%H:%M")

            # Ejecuta solo una vez por horario
            if now in config["schedule"]["times"] and last_execution != now:

                backup_all()

                last_execution = now

            # Espera configurable
            interval = config["schedule"].get("check_every_seconds", 30)

            time.sleep(interval)

        except Exception as ex:

            logging.exception(ex)

            print(ex)

            time.sleep(30)


if __name__ == "__main__":
    service_loop()