import requests
import warnings

warnings.simplefilter('ignore', requests.packages.urllib3.exceptions.InsecureRequestWarning)

class Intros:
    def __init__(self):
        pass  # No need to return anything here

    def introspection_query(self, target):
        intro_query = """
        query IntrospectionQuery {
          __schema {
            queryType { name }
            mutationType { name }
            types {
              ...FullType
            }
            directives {
              name
              description
              locations
              args {
                ...InputValue
              }
            }
          }
        }
        fragment FullType on __Type {
          kind
          name
          description
          fields(includeDeprecated: true) {
            name
            description
            args {
              ...InputValue
            }
            type {
              ...TypeRef
            }
            isDeprecated
            deprecationReason
          }
          inputFields {
            ...InputValue
          }
          interfaces {
            ...TypeRef
          }
          enumValues(includeDeprecated: true) {
            name
            description
            isDeprecated
            deprecationReason
          }
          possibleTypes {
            ...TypeRef
          }
        }
        fragment InputValue on __InputValue {
          name
          description
          type { ...TypeRef }
          defaultValue
        }
        fragment TypeRef on __Type {
          kind
          name
          ofType {
            kind
            name
            ofType {
              kind
              name
              ofType {
                kind
                name
                ofType {
                  kind
                  name
                  ofType {
                    kind
                    name
                  }
                }
              }
            }
          }
        }"""

        inter_query = False
        try:
            if not inter_query:
                response = requests.post(target, json=dict(query=intro_query), verify=False)
                json_response = response.json()
                if json_response.get("data"):
                    inter_query = True
                    return "introspection query allowed"
                    # Uncomment if you want to print the data
                    # print(json_response['data'])
                else:
                    return "introspection query not allowed"
        except Exception as e:
            return "Error while getting thes schema... [might be OFF]"
