from inputformat import format
from autocorrect import Speller
spell = Speller()

req = input()

res = format(req, False)

print(res)