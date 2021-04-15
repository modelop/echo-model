// Echo model
#modelop.init
def begin():
    pass

#modelop.score
def action(datum):
    yield datum

#modelop.metrics
def metrics(data):
    yield dict(toy="output")
