import os

from unittest.mock import patch
from unittest.mock import Mock
from unittest.mock import MagicMock

from app import classinate_bigfoot
from nexosisapi import Client

REPORT_TEXT = 'I saw bigfoot in the woods near the ridge hiding behind a tree. My dogs went crazy'
API_KEY = 'API_KEY'
MODEL_ID = 'MODEL_ID'
REPORT_CLASS = 'REPORT_CLASS'

class TestClassinator(object):
    @patch('app.Client')
    def setup_method(self, method, mock_client):
        os.environ['NEXOSIS_API_KEY'] = API_KEY
        os.environ['BIGOOT_MODEL_ID'] = MODEL_ID

        mock_client.return_value.models.predict.return_value.data = [{ 'reportClass': REPORT_CLASS }]
        self.mock_client = mock_client
        self.result = classinate_bigfoot({ 'reportText': REPORT_TEXT }, {})

    def test_it_creates_client_with_expected_api_key(self):
        self.mock_client.assert_called_with(API_KEY)

    def test_it_predicts_with_expected_model_and_features(self):
        self.mock_client.return_value.models.predict.assert_called_with(MODEL_ID, [{ 'observed': REPORT_TEXT }])

    def test_it_returns_the_report_text(self):
        assert self.result['reportText'] == REPORT_TEXT

    def test_it_returns_the_report_class(self):
        assert self.result['reportClass'] == REPORT_CLASS
