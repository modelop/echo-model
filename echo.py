import os
#Echo model
#modelop.init
def begin():
    print(os.environ)

#modelop.score
def action(datum):
    yield datum

#modelop.metrics
def metrics(data):
    yield dict(toy="output")
    
#adding a comment to test git sync -Test
#ADDING A COMMENT TO TEST GIT SYNCH -TEST
# Iterated Git Synch Test
# Test failure 3.0 Regression
