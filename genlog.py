import time ,os ,logging ,random
# create logger
logger = logging.getLogger('org.archive.jmx.Client')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
# 10/31/2018 09:52:03 +0700 org.archive.jmx.Client ThreadCount: 176
FORMAT = '%(asctime)s %(name)s %(message)s'
formatter = logging.Formatter('%(asctime)s %(name)s %(message)s')
logging.basicConfig(format=FORMAT,filename="thread.log", level=logging.INFO)
# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# 'application' code
m = 60 # sec
now = time.time()
timer = now + m
while (True): 
    now = time.time()
    if now > timer : 
        timer += m
        # logger.debug('debug message')
        message = "ThreadCount : "+str(random.randint(50, 200))
        logger.info(str(message))
        # logger.warn('warn message')
        # logger.error('error message')
        # logger.critical('critical message')