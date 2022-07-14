import logging
logging.basicConfig(filename="add.log",level=logging.INFO, format="%(asctime)s %(name)s %(message)s")

def sum(a,b):
    try:
        logging.info("sum of numbers is %s", a+b)
    except exception as e:
        logging.expection(e)
