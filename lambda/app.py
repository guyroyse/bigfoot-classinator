import os

from nexosisapi import Client

def classinate_bigfoot(event, context):
    # extract the report text from the passed in JSON
    report_text = event['reportText']

    # create the Nexosis API client using the API key in an environment variable
    nexosis_api_key = os.environ['NEXOSIS_API_KEY']
    nexosis_client = Client(nexosis_api_key)

    # the API can make several predictions at a time but we only want one so make this array
    features = [{ 'observed': report_text }]

    # invoke the model to make a prediction using the model ID in an environment variable
    model_id = os.environ['BIGFOOT_MODEL_ID']
    results = nexosis_client.models.predict(model_id, features)

    # since we only asked for one prediction, we only get one back
    prediction = results.data[0]

    # map the prediction to something a little more front-end friendly
    classination = {
        'reportText': prediction['observed'],
        'reportClass': prediction['reportClass']
    }

    ## return all our hard work
    return classination
