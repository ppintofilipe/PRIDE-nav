import os
from datetime import datetime

HOME = os.getcwd()
DATA_DIR = os.path.join(HOME, 'data')

DATABASE_FILE = ''

DATABASE_DATE = datetime.now().strftime('%Y%m%d_%H%M')