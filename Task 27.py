"""
PYTHON CONFIGURATION MANAGEMENT SYSTEM
Run this file directly, or paste the code into a Jupyter/Colab cell.

It automatically:
- Creates config.json with example development settings if it does not exist.
- Reads settings from config.json.
- Reads optional KEY=VALUE entries from .env.
- Lets system environment variables override file settings.
- Uses safe default values when a setting is missing.
"""

import json
import os
from pathlib import Path

# Use the current working folder. This works in normal Python and Jupyter/Colab.
BASE_DIR = Path.cwd()
CONFIG_FILE = BASE_DIR / "config.json"
ENV_FILE = BASE_DIR / ".env"

# Example development configuration
DEFAULT_CONFIG = {
    "APP_NAME": "My Python Application",
    "DEBUG": True,
    "PORT": 5000,
    "ENVIRONMENT": "development",
    "DATABASE_URL": ""
}


def create_config_file():
    """Create an example config.json automatically if it does not exist."""
    if not CONFIG_FILE.exists():
        with open(CONFIG_FILE, "w", encoding="utf-8") as file:
            json.dump(DEFAULT_CONFIG, file, indent=4)


def load_env_file():
    """Read optional settings from .env without replacing existing system variables."""
    if not ENV_FILE.exists():
        return

    with open(ENV_FILE, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue

            key, value = line.split("=", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")

            if key:
                os.environ.setdefault(key, value)


def load_config():
    """Load JSON settings, then apply .env and system environment overrides."""
    create_config_file()
    load_env_file()

    with open(CONFIG_FILE, "r", encoding="utf-8") as file:
        settings = json.load(file)

    if not isinstance(settings, dict):
        raise ValueError("config.json must contain a JSON object.")

    # Environment variables take priority over config.json.
    for key in DEFAULT_CONFIG:
        env_key = "APP_" + key
        if env_key in os.environ:
            settings[key] = os.environ[env_key]

    # Fill in any missing settings with defaults.
    for key, value in DEFAULT_CONFIG.items():
        settings.setdefault(key, value)

    return settings


def main():
    settings = load_config()

    # Convert values into the correct data types.
    debug_value = str(settings["DEBUG"]).lower()
    if debug_value in ("true", "1", "yes", "on"):
        debug = True
    elif debug_value in ("false", "0", "no", "off"):
        debug = False
    else:
        raise ValueError("DEBUG must be true or false.")

    try:
        port = int(settings["PORT"])
    except (TypeError, ValueError):
        raise ValueError("PORT must be a number.")

    print("\n" + "=" * 45)
    print("PYTHON CONFIGURATION MANAGEMENT SYSTEM")
    print("=" * 45)
    print("Application :", settings["APP_NAME"])
    print("Environment :", settings["ENVIRONMENT"])
    print("Debug Mode  :", debug)
    print("Port        :", port)
    print("Database URL:", "Configured" if settings["DATABASE_URL"] else "Not configured")
    print("-" * 45)
    print("Configuration loaded successfully!")
    print("Config file :", CONFIG_FILE)
    print("=" * 45)


if __name__ == "__main__":
    try:
        main()
    except (OSError, json.JSONDecodeError, ValueError) as error:
        print("Configuration error:", error)
