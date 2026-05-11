from imap_tools import MailBox
import os
from dotenv import load_dotenv
import logging
from datetime import datetime

# Configurar logging com datetime
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - RUN - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

logger = logging.getLogger(__name__)

has_loaded = load_dotenv(dotenv_path=".env_credentials")
logger.info("Carregando variáveis de ambiente")

email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

logger.info(f"Email: {email}")
logger.info(f"Password carregada com sucesso")

# print(email, password)
with MailBox('imap.gmail.com').login(username=email, password=password) as mailbox:
    for msg in mailbox.fetch():
        print(msg.date, msg.subject, len(msg.text or msg.html))