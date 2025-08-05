import datetime
 import numpy as np 

#Echo model
#modelop.init
def begin():
    pass

#modelop.score
def action(datum):
    yield datum

#modelop.metrics
def metrics(data):
    arr = np.array([1, 2, 3, 4, 5])
    to_be_yielded = {"test_date": datetime.datetime.now(), "test_ndarray": arr}
    yield to_be_yielded
