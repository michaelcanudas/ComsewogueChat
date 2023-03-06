import string


PUNCTUATION = string.punctuation

CONTEXT_STOPWORDS = ['same', 'other', 'url', 'subject', 'time', 'when', 'above', 'don', 'these', 'school', 'why', 'his', 'as', 'be', 'about', 'all', 'done', 'this', 'has', 'below', 'very', 'against', 'hour', 'such', 'will', 'day', 'the', 'should', 'it', 'too', 'ours', 'he', 'who', 'was', 'does', 'year', 'they', 'those', 'them', 'not', 'an', 'yourself', 'further', 'each', 'location', 'for', 'few', 'now', 'hers', 'were', 'playing', 'did', 'of', 'am', 'over', 'how', 'whom', 'herself', 'what', 'i', 'yourselves', 'on', 'month', 'down', 'if', 'that', 'do', 'after', 'themselves', 'than', 'between', 'its', 'versing', 'end', 'itself', 'having', 't', 'her', 'our', 'from', 'no', 'she', 'opponent', 'some', 'but', 'vs', 'second', 'venue', 'me', 'their', 'we', 'place', 'myself', 'site', 'been', 'until', 'here', 'website', 'my', 'once', 'under', 'by', 'with', 'while', 'address', 'during', 'out', 'nor', 'again', 'both', 'most', 'him', 'building', 'into', 'or', 'date', 'had', 'your', 'minute', 'link', 'page', 'doing', 'yours', 'theirs', 'there', 'have', 'any', 'only', 'title', 'to', 's', 'off', 'webpage', 'and', 'himself', 'can', 'a', 'so', 'up', 'verse', 'you', 'week', 'before', 'which', 'through', 'heading', 'in', 'more', 'being', 'is', 'just', 'ourselves', 'at', 'own', 'name', 'where', 'then', 'because', 'are', 'begin', 'label', 'start', 'whats']

NO_QC_RESPONSES_1 = [
    "I'm sorry, I don't understand your question.", "I'm sorry, I'm having trouble understanding what you're asking.",
    "I apologize, I don't understand what you're asking.", "I'm sorry, I don't think I understood your question properly.",
    "I'm sorry, I'm not sure what you're asking."
]
NO_QC_RESPONSES_2 = [
    "Could you please rephrase it?", "Can you try asking me something else?", "Would you mind rephrasing it?",
    "Can you clarify it for me?", "Could you please try asking in a different way?"
]

NO_Q_RESPONSES_1 = [
    "I'm not sure what you want to know about the ",
    "I'm not quite clear on what information you're looking for about the ",
    "I'm uncertain about what you're asking regarding the ",
    "Unfortunately, I don't fully understand your question about the "
]
NO_Q_RESPONSES_2 = [". Maybe try reformatting your question to include a question word?", ". One suggestion could be to include a question word in your question to make it more specific.", ". If you're having trouble getting the answer you're looking for, you could try reformatting your question with a question word.", ". You may want to try rephrasing your question to include a word like 'when' or 'where' to make your question clearer."]

NO_C_RESPONSES_1a = [
    "What do you want to know the ", "What specific information are you seeking regarding the ",
    "Do you have any particular questions about the "
]
NO_C_RESPONSES_1b = [" of? ", " ? ", " that you would like me to answer? "]
NO_C_RESPONSES_2 = [
    "Maybe try reformatting your question to include some context?",
    "Could you please provide some additional information to help me better understand your question?",
    "Could you give me some more details or background information about what you're looking for?",
    "It would be helpful if you could provide some context or clarify your question a bit more.",
    "Could you provide some additional context?",
    "Could you rephrase your question or provide some more context to help me understand?"
]