import time ,os ,logging ,random
# create logger
logger = logging.getLogger('ThreadCount')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
FORMAT = '%(asctime)s %(name)s %(message)s'
formatter = logging.Formatter('%(asctime)s %(name)s %(message)s')
logging.basicConfig(format=FORMAT,filename="thread.log", level=logging.INFO)
# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
m = 5 # sec
now = time.time()
timer = now + m
while (True): 
    now = time.time()
    if now > timer : 
        timer += m
        # logger.debug('debug message')
        message = random.randint(50, 100)
        logger.info(str(message))
        # logger.warn('warn message')
        # logger.error('error message')
        # logger.critical('critical message')