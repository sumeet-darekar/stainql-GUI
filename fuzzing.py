import requests
import warnings

warnings.simplefilter('ignore', requests.packages.urllib3.exceptions.InsecureRequestWarning)

class Fuzz:
    def __init__(self):
        pass  # No need to return anything here
    def fuzzing_graphql(self, target):
        output = []
        try:
            with open('graphql-wordlist.txt', "r") as f:
                words = [line.strip() for line in f.readlines()]
                #print(words)
                print(f"Scanning the graphql endpoints/directories... \n")
                for word in words:
                    print(f": {word}")
                    response = requests.get(url=f"{target}/{word}", verify=False)
                    #print(response.url)
                    #print(response.status_code)
                    if(response.status_code >= 200 and response.status_code < 304 or response.status_code==400):
                        output.append(word)
                        print(f"\n --> Endpoint : {word} [ Response code : {response.status_code} ]")
                        print(f"       URL : {response.url} \n\n")
                    print("\033[A\033[K", end="")
            return [ "Endpoint: /"+word for word in output]
        except :
            return ("Interruption Occur during scanning...")

