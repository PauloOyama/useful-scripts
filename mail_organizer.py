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

        if not mailbox.folder.exists("TI VAGAS"):
            _,status_code = mailbox.folder.create('TI VAGAS')
            logger.info(f"Creation Folder TI VAGAS {status_code}")

        if not mailbox.folder.exists("ENTRETENIMENTO"):
            _,status_code = mailbox.folder.create('ENTRETENIMENTO')
            logger.info(f"Creation Folder ENTRETENIMENTO {status_code}")

        if not mailbox.folder.exists("TI ARTIGOS"):
            _,status_code = mailbox.folder.create('TI ARTIGOS')
            logger.info(f"Creation Folder TI ARTIGOS {status_code}")

    except Exception as e:
         logger.warning("Error: Creating Folders!")
         logger.warning("Terminating the program")
         raise Exception(e)

    logger.info("All folder created")
    return True


def email2move(sender:str,topic:str)->None:
    try:
            logging.info(f"Searching emails from {sender}")
            uids2move = mailbox.uids(AND(from_=sender), charset='utf8')

            logging.info(f"Moving emails from {sender} to {topic} - {len(uids2move)} Founded!")
            mailbox.move(uids2move, topic, chunks=100)
    except Exception as e:
            logging.warning("Error: When moving file...")

    logging.info(f"All email from {sender} to {topic} moved!")


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
    
    logging.info(f"Time Filtered - AFTER {date_filtered.strftime("%d-%b-%Y")}")

    email2move(sender='noreply@medium.com',topic='NOTÍCIAS')
    email2move(sender='',topic='NOTÍCIAS')
    email2move(sender='tesourodireto@b3.com.br',topic='INVESTIMENTOS')
    email2move(sender='todomundo@nubank.com.br',topic='INVESTIMENTOS')
    email2move(sender='contato@emkt.b3.com.br',topic='INVESTIMENTOS')
    email2move(sender='relacionamento@kineainvestimentos.com.br',topic='INVESTIMENTOS')
    email2move(sender='jobalerts-noreply@linkedin.com',topic='TI VAGAS')
    email2move(sender='.jobs2web.',topic='TI VAGAS')
    email2move(sender='glassdoor',topic='TI VAGAS')
    email2move(sender='tiktok',topic='ENTRETENIMENTO')
    email2move(sender='datatalks',topic='TI ARTIGOS')
    email2move(sender='filipedeschamps',topic='TI ARTIGOS')
    # for msg in mailbox.fetch(AND(date_gte=date_filtered.date())):
    #     print(msg.date, msg.subject, len(msg.text or msg.html))