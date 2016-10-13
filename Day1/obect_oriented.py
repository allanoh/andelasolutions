class School(object):  # main class .
    def __init__(self, country, city):  # instantiation
        self.country = country
        self.city = city


class Student(School):  # inheritance                                 # second class that inherits from super.
    def __init__(self, country, city, fname, lname, year, fees, ):
        super(self.__class__, self).__init__(country, city)
        self.fname = fname  # other class declarations not main.
        self.lname = lname
        self.year = year
        self.fees = fees
        self.username = fname + lname + '@cuea,edu'

    def permanent(self):  # Abstract method, defined by convention only
        raise NotImplementedError("Subclass must implement abstract method")
