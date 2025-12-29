import os 
import logging

# Configuracao basica 
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

download_dir = r"C:\Users\papal\Downloads"
os.chdir(download_dir)

for file in os.listdir(os.getcwd()):

    if not os.path.isfile(file):
        logging.info(f"Arquivo \"{file}\" eh uma diretorio")
    
    _, *extension = os.path.splitext(file)
    dir_extension_name = ''.join(extension)

    if os.path.exists(dir_extension_name):
        logging.info(f"A pasta {dir_extension_name} já está criada.")
    else:
        try:
            os.mkdir(dir_extension_name)
        except Exception as e :
            logging.error(f"Error: Ao tentar criar um diretorio da extensao {dir_extension_name} -- {e}")
    
    # print(os.path.splitext(file), "{}".format(os.stat(file).st_mtime))