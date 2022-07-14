import logging
logging.basicConfig(filename="multiply.log",level=logging.INFO, format="%(asctime)s %(name)s %(message)s")

def mul(a,b):
    try:
        logging.info("multiplication of numbers is %s", a*b)
    except exception as e:
        logging.expection(e)

