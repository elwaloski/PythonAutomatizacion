import json
import logging
import os
import sys
import time
import zipfile
from datetime import datetime

logging.basicConfig(
    filename="zip_service.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_base_path():
    if getattr(sys, "frozen", False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def load_config():
    config_path = os.path.join(get_base_path(), "config.json")

    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def create_zip(job):
    source_folder = job["source_folder"]
    output_folder = job["output_folder"]

    exclude_folders = set(job.get("exclude_folders", []))
    exclude_files = set(job.get("exclude_files", []))

    os.makedirs(output_folder, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    zip_path = os.path.join(
        output_folder,
        f"{job['zip_name']}_{timestamp}.zip"
    )

    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_folder):

            dirs[:] = [
                d for d in dirs
                if d not in exclude_folders
            ]

            for file in files:
                if file in exclude_files:
                    continue

                full_path = os.path.join(root, file)
                relative = os.path.relpath(full_path, source_folder)

                zipf.write(full_path, relative)

    print(f"ZIP creado: {zip_path}")
    logging.info(f"ZIP creado: {zip_path}")


def service_loop():
    print("Servicio ZIP iniciado")
    logging.info("Servicio ZIP iniciado")

    last_executions = {}

    while True:
        try:
            config = load_config()
            now = datetime.now().strftime("%H:%M")

            for job in config["jobs"]:
                job_name = job["zip_name"]
                schedule = job.get("schedule", {})

                if not schedule.get("enabled", False):
                    continue

                times = schedule.get("times", [])

                if now in times and last_executions.get(job_name) != now:
                    create_zip(job)
                    last_executions[job_name] = now

            interval = config.get("check_every_seconds", 30)
            time.sleep(interval)

        except Exception as ex:
            logging.exception(ex)
            print(ex)
            time.sleep(30)


if __name__ == "__main__":
    service_loop()