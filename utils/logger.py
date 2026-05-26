from datetime import datetime

def register_log(message):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"

    with open("logs/app.log", "a", encoding="utf-8") as log_file:
        log_file.write(log_entry)