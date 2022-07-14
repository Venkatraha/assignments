#Example 1

import logging
logging.basicConfig(filename="file1.log",level= logging.INFO,format="%(asctime)s %(name)s %(message)s")

class ineuron:                                 # class creation
    logging.info("class ineuron created")
    __discount = "10 percent"

    def __init__(self,name,rollno,batch_name): # constructor
        self.name = name                       # public
        self._rollno = rollno                  # protected
        self.__batch_name = batch_name         # private
        logging.info("init method, objs - name,rollno,batch_name")

    def course(self):                          # method
        try:
           logging.info("course name is data science")
        except Exception as e:
            logging.exception(e)

    def specialfee(self):
        try:
           logging.info("discounted fee %s", self.__discount)
        except Exception as e:
            logging.exception(e)

    def updated_specialfee(self, newdiscount):
        self.__discount = newdiscount
        try:
            logging.info("updated discount is %s", newdiscount)
        except Exception as e:
            logging.exception(e)

    def agelimit(self):
        try:
           logging.info("no age limit")
        except Exception as e:
            logging.exception(e)

class students(ineuron):                       # Inheritance
    logging.info("class students created")

    def fee(self):
        try:
           self.fee = 100
           logging.info("fee for each student is %s :",self.fee)
        except Exception as e:
            logging.exception(e)

    def agelimit(self):
        try:
            logging.info("30 is age limit")
        except Exception as e:
            logging.exception(e)

try:
    i = ineuron("ram",101,"weekend")
    logging.info(i.name)
    logging.info(i._rollno)
    logging.info(i._ineuron__batch_name)
except Exception as e:
    logging.exception(e)

try:
    j= students("krishna",102,"weekdays")
    logging.info(j.name)
    logging.info(j._rollno)
    logging.info(j._ineuron__batch_name)
    logging.info(j.fee())
except Exception as e:
    logging.exception(e)

try:                                               # abstraction
    i = ineuron("shiva",103,"weekend")
    i.specialfee()
except Exception as e:
    logging.exception(e)

try:                                               # encapsulation
    k = ineuron("durga",104,"weekdays")
    k.__discount = "20 percent"
    k.specialfee()
except Exception as e:
    logging.exception(e)

try:                                              # method over ridding
    l = ineuron("laxmi",105,"weekdays")
    l.updated_specialfee("20 percent")
    l.specialfee()
except Exception as e:
    logging.exception(e)

def agelimit_info(a):                             #polymorphism
    try:
        a.agelimit()
    except Exception as e:
        logging.exception(e)

try:
    a = ineuron("kamala",106,"weekends")
    b = students("padma",107,"weekends")
    agelimit_info(a)
    agelimit_info(b)
except Exception as e:
    logging.exception(e)