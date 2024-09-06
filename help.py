# help_module.py

class Help:
    def __init__(self):
        pass  # No need to return anything here

    def greet(self):
    	text = '''\
        🛠️ What's StainQL?

        StainQL is a simple GraphQL API testing tool.

        🔍 **Features Provided by StainQL**:

        	- ✅ Introspection query check.
        	- ✅ GraphQL endpoint detection using in-built wordlist.
        	- ✅ CSRF (Cross-Site Request Forgery) check.
        	- ✅ Query-based batching attack check.
        	- ✅ Execute custom GraphQL queries.

        Default Interface
        '''
    	return text
    def greet2(self):
    	text = '''\
        Fuzzing Page
        	- ✅ Endpoints fuzzing.
        '''
    	return text