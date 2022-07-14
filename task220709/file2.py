# Example 2

import logging
logging.basicConfig(filename = "file2.log", level = logging.INFO, format="%(asctime)s %(name)s %(message)s")

class blog:
    logging.info("claas blog created")
    __host = "bluehost"

    def __init__(self,name,genere,posts):
        try:
            self.name = name
            self._genere = genere
            self.__posts = posts
        except Exception as e:
            logging.exception(e)

    def status(self,currentstatus):
        try:
           self.currentstatus = currentstatus
           logging.info("blog status %s", self.currentstatus)
        except Exception as e:
            logging.exception(e)

    def hostname(self):
        try:
            logging.info("host name is %s",self.__host)
        except Exception as e:
            logging.exception(e)

    def updatedhost(self,newhost):
        try:
            self.__host = newhost
            logging.info("new host name is %s",self.__host)
        except Exception as e:
            logging.exception(e)

    def maintainance_cost(self):
        try:
            logging.info("maintainance cost of blog is 1000")
        except Exception as e:
            logging.exception(e)

class blog2(blog):                                      #inheritance
    logging.info("class blog2 created")

    def income(self):
        try:
            logging.info("no income from blog2")
        except Exception as e:
            logging.exception(e)

    def maintainance_cost(self):
        try:
            logging.info("maintainance cost of blog2 is 2000")
        except Exception as e:
            logging.exception(e)

def costs(a):
    try:
        a.maintainance_cost()
    except Exception as e:
        logging.exception(e)


try:
    a = blog("technews","technology",20)
    b = blog2("political", "news",101)
    logging.info(a._genere)
    logging.info(a._blog__posts)
    logging.info(a.name)
    a.status("active")
    a.hostname()    # abstraction
    logging.info(b.name)
    logging.info(b._genere)
    logging.info(b._blog__posts)
    b.status("active")
    b.hostname()
    b.income()
    c = blog("sports","games",30)             # encapsulation
    c.__host = "bigdaddy"                     # encapsulation
    c.hostname()                # encapsulation
    c.updatedhost("bigdaddy")   # method over ridding
    c.hostname()                # method over ridding
    costs(a)                    # polymorphism
    costs(b)                    # polymorphism
except Exception as e:
    logging.exception(e)

