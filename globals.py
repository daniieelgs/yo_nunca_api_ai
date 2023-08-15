from dotenv import load_dotenv
import os

load_dotenv()

DEFAULT_CATEGORIES = ["Pregunta incómodas", "Preguntas picantes y hot", "Preguntas sexuales", "Preguntas intimas", "Preguntas de revelacion de secretos"]
DEFAULT_EXAMPLES = ["Nunca he dicho el nombre equivocado durante las relaciones sexuales.", "Nunca he estado con nadie de mi familia.", "Nunca he hecho un trío.", "Nunca he tenido sexo más de 5 veces en una noche.", "Nunca he sido infiel.", "Nunca me he liado con el ex de un/a amigo/a.", "Nunca he estado con alguien este grupo.", "Nunca he trabajado borracho.", "Nunca he hecho o recibido un baile erótico."]

DEFAULT_DATABASE_URI = 'sqlite:///data.db'
DEFAULT_SECRET_JWT = '303333537232571254035672536717968198213'
DEFAULT_API_PREFIX = 'api'

DEBUG = os.getenv('FLASK_DEBUG', 'False') == '1' or os.getenv('FLASK_DEBUG', 'False') == 1 or os.getenv('FLASK_DEBUG', 'False') == 'True'

API_KEY_OPENAI = os.getenv('API_KEY_OPENAI')
ENGINE_MODEL_OPENAI = os.getenv('ENGINE_MODEL_OPENAI')

DB_MYSQL_USER = os.getenv('DB_MYSQL_USER', None)
DB_MYSQL_PASS = os.getenv('DB_MYSQL_PASS', None)
DB_MYSQL_HOST = os.getenv('DB_MYSQL_HOST', None)
DB_MYSQL_NAME = os.getenv('DB_MYSQL_NAME', None)

MYSQL_DATABASE_URI = f'mysql+mysqlconnector://{DB_MYSQL_USER}:{DB_MYSQL_PASS}@{DB_MYSQL_HOST}/{DB_MYSQL_NAME}' if DB_MYSQL_USER and DB_MYSQL_PASS and DB_MYSQL_HOST and DB_MYSQL_NAME else None

DATABASE_URI = os.getenv("DATABASE_URI", MYSQL_DATABASE_URI or DEFAULT_DATABASE_URI)
SECRET_JWT = os.getenv('SECRET_JWT', DEFAULT_SECRET_JWT)

API_PREFIX = os.getenv('API_PREFIX', DEFAULT_API_PREFIX)
