#Echo model
#modelop.init
def begin():
    pass

#modelop.score
def action(datum):
    raise ValueError("I'm throwing errors over here") 
    yield datum

#modelop.metrics
def metrics(data):
    raise ValueError("I'm throwing errors over here") 
    yield dict(toy="output")
    
#adding a comment to test git sync -Test
#ADDING A COMMENT TO TEST GIT SYNCH -TEST
# Iterated Git Synch Test
# Test failure 3.0 Regression
