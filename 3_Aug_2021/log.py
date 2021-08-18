#logging
import logging
# logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.DEBUG) #this is used for printing the info and debug
logging.basicConfig(filename='demo.log',level=logging.DEBUG)
logging.error("an unknown error happened")     #priority value 50
logging.warning("Expected value is an error")#40
logging.critical("Crtical error happened")#30
logging.info("Normal message")#20
logging.debug("for developers")#10


