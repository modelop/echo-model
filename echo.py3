#Echo model
#modelop.init
def begin():
    pass

#modelop.score
def action(datum):
    print(type(datum))
    print(datum)
    yield datum

#modelop.metrics
def metrics(data):
    print(type(datum))
    print(datum)
    yield dict(toy="output")
    
#adding a comment to test git sync -Test
#ADDING A COMMENT TO TEST GIT SYNCH -TEST
# Iterated Git Synch Test
# Test failure 3.0 Regression
