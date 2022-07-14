import logging
logging.basicConfig(filename = "file3.log",level=logging.INFO,format="%(asctime)s %(name)s %(message)s")

class internship:
    __department = "development"

    def __init__(self,name,language,age):
        try:
            self.name = name
            self._language = language
            self.__age = age
        except Exception as e:
            logging.exception(e)

    def location(self):
        try:
            logging.info("location is Bangalore")
        except Exception as e:
            logging.exception(e)

    def department1(self):
        try:
            logging.info("department is %s",self.__department)
        except Exception as e:
            logging.exception(e)

    def departmentupdate(self,newdept):
        try:
            self.__department = newdept
            logging.info("updated department is %s", self.__department)
        except Exception as e:
            logging.exception(e)

    def duration(self):
        try:
            logging.info("duration is 6 months")
        except Exception as e:
            logging.exception(e)

class internship2(internship):

    def duration(self):
        try:
            logging.info("duration is 12 months")
        except Exception as e:
            logging.exception(e)

def durationperiod(a):
    try:
        logging.info(a.duration())
    except Exception as e:
        logging.exception(e)

try:
    a=internship("muni","c++",23)
    b=internship2("rishi","java",25)
    c=internship("tapasvi","python",28)
    logging.info(a.name)
    logging.info(a._language)
    logging.info(a._internship__age)
    logging.info(b.name)
    logging.info(b._language)
    logging.info(b._internship__age)
    logging.info(c.name)
    logging.info(c._language)
    logging.info(c._internship__age)
    a.department1()                             # abstraction
    a.__department = "program management"       # encapsulation
    a.department1()                             # encapsulation
    a.departmentupdate("program management")    #method over ridding
    a.department1()                             #method over ridding
    durationperiod(a)                           # polymorphism
    durationperiod(b)                           # polymorphism
except Exception as e:
    logging.exception(e)


