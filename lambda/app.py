import os

from nexosisapi import Client

def classinate_bigfoot(event, context):
    api_key = os.environ['NEXOSIS_API_KEY']
    model_id = os.environ['BIGOOT_MODEL_ID']

    report_text = event['reportText']
    client = Client(api_key)
    features = [{ 'observed': report_text }]
    results = client.models.predict(model_id, features)

    return {
        'reportText': report_text,
        'reportClass': results.data[0]['reportClass']
    }