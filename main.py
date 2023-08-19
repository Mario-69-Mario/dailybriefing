
import logging
# envSetup.env_setup()

global logger
logger = logging.getLogger(__name__)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(os.environ.get("logfilePath") + 'logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(module)s : %(message)s')

logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

logger.info('************* Started main *************')

def main():
    try:
        pring("Nothing ")

    except Exception as e:
        logger.error("Main error " + str(e))


    
if __name__ == "__main__":
    main()