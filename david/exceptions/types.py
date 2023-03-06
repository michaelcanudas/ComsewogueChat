class InvalidRequestException(Exception):
    pass


class NoQueryAndContextException(Exception):
    pass


class NoQueryException(Exception):
    def __init__(self, context):
        self.context = context


class NoContextException(Exception):
    def __init__(self, queries):
        self.query = queries


class NoResultsException(Exception):
    def __init__(self, queries, context):
        self.queries = queries
        self.context = context
