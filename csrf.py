import requests
import warnings

warnings.simplefilter('ignore', requests.packages.urllib3.exceptions.InsecureRequestWarning)

class csrf_attack:
    def __init__(self):
        pass  # No need to return anything here

    def attack_get(self, target):
        result = False
        payload = {"query": "{ a }"}
        try:
            response = requests.get(target, verify=False, params=payload)
            json_response = response.json()
            error_list = json_response.get("errors", [])

            for error in error_list:
                if "Cannot query field" in error.get('message', ''):
                    return " [ GET based CSRF vulnerability might be present  🤗 ]"
                
                if any(word in ['undefined', 'error'] for word in error_list):
                    return " [ GET based CSRF vulnerability might be present  🤗 ]"
            
        except Exception as e:
            return f"Error during scanning: {e}"

        return "CSRF might not be present in the GET request"

    def attack_post(self, target):
        result = False
        payload = {"query": "{ a }"}
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        
        try:
            # Check for POST based CSRF
            response1 = requests.post(target, data=payload, verify=False)
            errors = response1.json().get("errors", [])

            for error in errors:
                if "Cannot query field" in error.get('message', ''):
                    return "--> [ POST based CSRF might be present  🤗 ]"
                
                if any(word in ['undefined', 'error'] for word in errors):
                    return "--> [ POST based CSRF might be present  🤗 ]"
            
            # Check if x-www-form-urlencoded is accepted
            r = requests.post(target, data=payload, headers=headers)
            if r.status_code == 200:
                return "--> [ Server accepts x-www-form-urlencoded data might be vulnerable to CSRF ]"
            else:
                return "Not vulnerable to POST based CSRF"

        except Exception as e:
            return f"Error during scanning: {e}"

        if not result:
            return f"--> CSRF might not be present in [{target}]"
