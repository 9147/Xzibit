import pandas as pd
import re

def check_domain(url):
    domains = pd.read_csv('domains.csv')
    url= re.search(r"(?:https:\/\/)?(?:www\.)?(?:[a-z-0-9]*\.)*(?:com|in|edu|gov|gov\.in|com\.in|org|net|eu|co)",url).group(0)
    domain = ''
    for b in domains['domain']:
        if re.search(b, url) != None:
            domain = b
            break
    domain
    if domain != '':
        return 1
    else:
        return 0


