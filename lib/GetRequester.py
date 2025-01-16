import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        """
        Fetches the response body from the URL as bytes.
        """
        response = requests.get(self.url)
        response.raise_for_status()  # Raise an error for HTTP status codes 4xx/5xx
        return response.content  # Returns the content in bytes

    def load_json(self):
        """
        Parses the JSON response body into a Python list of dictionaries.
        """
        response_body = self.get_response_body()
        return json.loads(response_body)  # Converts JSON bytes to a Python object
