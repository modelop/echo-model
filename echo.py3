#Echo model
#modelop.init
def begin():
    pass

#modelop.score
def action(datum):
    print(datum)

#modelop.metrics
def metrics(data):
    print(dict(toy="output"))
