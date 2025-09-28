from pathlib import Path

# ---- Paths ----
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"
DATA_DIR.mkdir(exist_ok=True)

DB_PATH = DATA_DIR / "main.db"
DB_PATH_STR = str(DB_PATH)  # some classes expect str

# ---- Server ----
DEBUG = True
PORT = 5000
HOST = "127.0.0.1"

# ---- Client ----
API_BASE = f"http://{HOST}:{PORT}/api"
TIMEOUT_DEFAULT = 10
TIMEOUTS = {
    "inventory": 10,
    "manager": 10,
    "money": 10,
}