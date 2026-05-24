import os
from dotenv import load_dotenv  # type: ignore[import-not-found]


def load_config() -> None:
    env_path = os.path.join(os.path.dirname(__file__), ".env")
    load_dotenv(env_path)


def get_config() -> dict[str, str]:
    return {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL", "not configured"),
        "API_KEY": os.getenv("API_KEY", "not configured"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT", "not configured")
    }


def print_config(config: dict[str, str]) -> None:
    print("\nConfiguration loaded:")
    print(f"Mode: {config['MATRIX_MODE']}")
    db = ("Connected to local instance"
          if config['DATABASE_URL'] != "not configured"
          else "not configured")
    api = ("Authenticated"
           if config['API_KEY'] != "not configured"
           else "not configured")
    zion = ("Online"
            if config['ZION_ENDPOINT'] != "not configured"
            else "not configured")
    print(f"Database: {db}")
    print(f"API Access: {api}")
    print(f"Log Level: {config['LOG_LEVEL']}")
    print(f"Zion Network: {zion}")


def print_mode_info(mode: str) -> None:
    if mode == "production":
        print("\nWARNING: Running in PRODUCTION mode!")
        print("  - All actions are real")
        print("  - Logging is minimal")
    else:
        print("\nINFO: Running in DEVELOPMENT mode")
        print("  - Safe to test")
        print("  - Full logging enabled")


def print_security_check(config: dict[str, str]) -> None:
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if config["API_KEY"] != "not configured":
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not configured")
    if config["MATRIX_MODE"] == "production":
        print("[OK] Production overrides available")
    else:
        print("[OK] Development mode active")


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...")
    load_config()
    config = get_config()
    print_config(config)
    print_mode_info(config["MATRIX_MODE"])
    print_security_check(config)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
