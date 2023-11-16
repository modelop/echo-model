#Echo model
#modelop.init
def begin():
    pass

#modelop.score
def action(datum):
    yield datum

#modelop.metrics
def metrics(data):
    yield dict(toy="output")
    
#adding a comment to test git sync -Test
# Iterated Git Synch Test
# Test failure 3.0 Regression
