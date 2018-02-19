
class mydata(object):

    def __init__(self):
        self.x = "what"
        self.y = ""

    @classmethod
    def anotherway(cls):
        x,y = "hey","ho"

one = mydata()
print("first" + one.x + " " + one.y)
two = mydata.anotherway()
print("second" + two.x + " " + two.y)
