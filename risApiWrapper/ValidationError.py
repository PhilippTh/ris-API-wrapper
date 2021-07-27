class ValidationError():
    '''
    Raised when argument is not accepted by the API.
    '''
    def __init__(self, argumentDescription:str, possibleArguments:list):
        self.error = 'Please provide a valid argument for "{}". The API accepts "{}" or "{}"'.format(argumentDescription, '", "'.join(possibleArguments[0:-2]), possibleArguments[-1])
        
 
    def __str__(self):
        return self.error