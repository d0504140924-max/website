from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "main.db"
DB_PATH_STR = str(DB_PATH)


DEBUG = True
PORT = 5000
HOST = "127.0.0.1"

