from imap_tools import AND, MailBox
import os
from dotenv import load_dotenv
import logging
from datetime import datetime, timedelta
from typing import Tuple

# Configurar logging com datetime
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - RUN - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)



def create_folder(mailbox:MailBox) -> bool:
    try:
        if not mailbox.folder.exists("PAGAMENTOS"):
            _,status_code = mailbox.folder.create('PAGAMENTOS')
            logger.info(f"Creation Folder PAGAMENTOS {status_code}")

        if not mailbox.folder.exists("NOTÍCIAS"):
            _,status_code = mailbox.folder.create('NOTÍCIAS')
            logger.info(f"Creation Folder NOTÍCIAS {status_code}")

        if not mailbox.folder.exists("INVESTIMENTOS"):
            _,status_code = mailbox.folder.create('INVESTIMENTOS')
            logger.info(f"Creation Folder INVESTIMENTOS {status_code}")

    except Exception as e:
         logger.warning("Error: Creating Folders!")
         logger.warning("Terminating the program")
         raise Exception(e)

    logger.info("All folder created")
    return True


logger = logging.getLogger(__name__)

has_loaded = load_dotenv(dotenv_path=".env_credentials")
logger.info("Carregando variáveis de ambiente")

email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

logger.info(f"Email: {email}")
logger.info(f"Password carregada com sucesso")

# print(email, password)
with MailBox('imap.gmail.com').login(username=email, password=password) as mailbox:
    current_folder = mailbox.folder.get()
    logger.info(f"Current Folder - {current_folder}")
    
    
    create_folder(mailbox=mailbox)
    
    date_filtered = datetime.now() - timedelta(days=60)
    
    print(date_filtered.strftime("%d-%b-%Y"))
    for msg in mailbox.fetch(AND(date_gte=date_filtered.date())):
        print(msg.date, msg.subject, len(msg.text or msg.html))