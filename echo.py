import pandas as pd
#Echo model
#modelop.init
def begin():
    pass

#modelop.score
def action(datum):
    yield datum

#modelop.metrics
def metrics(data):
    data = pd.DataFrame(data)
    yield data.to_dict(orient="records")
    
#adding a comment to test git sync -Test
#ADDING A COMMENT TO TEST GIT SYNCH -TEST
# Iterated Git Synch Test
# Test failure 3.0 Regression
