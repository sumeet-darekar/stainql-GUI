import requests
import warnings
import time

warnings.simplefilter('ignore', requests.packages.urllib3.exceptions.InsecureRequestWarning)

class Batching:
    def __init__(self):
        pass  # No need to return anything here

    def query_batching(self, target):
        payload = """[
            {
                "query": "..."
            },
            {
                "query": "..."
            },
            {
                "query": "..."
            },
            {
                "query": "..."
            }
        ]"""
        try:
            time.sleep(2)
            headers = {'content-type': 'application/json'}
            response = requests.post(target, data=payload, headers=headers, verify=False)
            response_json = response.json()
            if len(response_json.get('errors', [])) > 1:
                return "[ Query based batching vulnerability is present 🤗]\n" + f"Payload is : {payload}"
            else:
                return "NOT VULNERABLE to query based batching attack"
        except Exception as e:
            return f"Something went wrong. Error: [{e}]"

