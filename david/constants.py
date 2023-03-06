import string


PUNCTUATION = string.punctuation

CONTEXT_STOPWORDS = ['same', 'other', 'url', 'subject', 'time', 'when', 'above', 'don', 'these', 'school', 'why', 'his', 'as', 'be', 'about', 'all', 'done', 'this', 'has', 'below', 'very', 'against', 'hour', 'such', 'will', 'day', 'the', 'should', 'it', 'too', 'ours', 'he', 'who', 'was', 'does', 'year', 'they', 'those', 'them', 'not', 'an', 'yourself', 'further', 'each', 'location', 'for', 'few', 'now', 'hers', 'were', 'playing', 'did', 'of', 'am', 'over', 'how', 'whom', 'herself', 'what', 'i', 'yourselves', 'on', 'month', 'down', 'if', 'that', 'do', 'after', 'themselves', 'than', 'between', 'its', 'versing', 'end', 'itself', 'having', 't', 'her', 'our', 'from', 'no', 'she', 'opponent', 'some', 'but', 'vs', 'second', 'venue', 'me', 'their', 'we', 'place', 'myself', 'site', 'been', 'until', 'here', 'website', 'my', 'once', 'under', 'by', 'with', 'while', 'address', 'during', 'out', 'nor', 'again', 'both', 'most', 'him', 'building', 'into', 'or', 'date', 'had', 'your', 'minute', 'link', 'page', 'doing', 'yours', 'theirs', 'there', 'have', 'any', 'only', 'title', 'to', 's', 'off', 'webpage', 'and', 'himself', 'can', 'a', 'so', 'up', 'verse', 'you', 'week', 'before', 'which', 'through', 'heading', 'in', 'more', 'being', 'is', 'just', 'ourselves', 'at', 'own', 'name', 'where', 'then', 'because', 'are', 'begin', 'label', 'start', 'whats']

NO_QC_RESPONSES_1 = ["I'm sorry, I don't understand your question.", "I'm sorry, I'm having trouble understanding what you're asking.", "I apologize, I don't understand what you're asking.", "I'm sorry, I don't think I understood your question properly.", "I'm sorry, I'm not sure what you're asking."]
NO_QC_RESPONSES_2 = ["Could you please rephrase it?", "Can you try asking me something else?", "Would you mind rephrasing it?", "Can you clarify it for me?", "Could you please try asking in a different way?"]