
# 1. Library imports
import uvicorn
from fastapi import FastAPI

import numpy as np
from iris import IRISD
import pickle
import pandas as pd
# 2. Create the app object
app = FastAPI()
pickle_in = open('model1/cir.pkl','rb')
classifier=pickle.load(pickle_in)

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'use /docs whth the url,enter float value in the input json'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere


# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_flower(data:IRISD):
    data = data.dict()
    s_length=data['s_length']
    s_width=data['s_width']
    p_length=data['p_length']
    p_width=data['p_width']
   # print(classifier.predict([[variance,skewness,curtosis,entropy]]))
    prediction = classifier.predict([[s_length,s_width,p_length,p_width]])
    if(prediction[0]==0):
        prediction="Sitosa"
    elif(prediction[0]==1):
        prediction="versicolor"
    else:
        prediction="verginica"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload