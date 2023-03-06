class InvalidRequestException(Exception):
    pass


class NoContextException(Exception):
    def __init__(self, query):
        self.query = query


class NoQueryException(Exception):
    def __init__(self, context):
        self.context = context


class NoResultsException(Exception):
    def __init__(self, context, query):
        self.context = context
        self.query = query
