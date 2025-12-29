import os 
import logging
import shutil

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
    
    current_dir = os.getcwd()
    source_file = '\\'.join([current_dir,file])
    destination_file = '\\'.join([current_dir,dir_extension_name,file])
    print(source_file)
    print(destination_file)
    try:
        shutil.move(source_file, destination_file)
    except  Exception as e:
        logging.info(f"Erro: Ao tentar mover o arquivo localizado {source_file} para {destination_file} -- {e}")
    # print(os.path.splitext(file), "{}".format(os.stat(file).st_mtime))