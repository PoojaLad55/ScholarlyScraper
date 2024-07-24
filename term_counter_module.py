import re
'''
Parses through user's list of search terms and identifies in article text.
Counts frequency of each search term and stores in dictionary.
'''

def term_counter(article_text, search_terms):
    term_freq = {}
    
    article_text = article_text.lower()
    words = re.findall(r'\b\w+\b', article_text)
    
    for word in words:
        if word in search_terms:
            if word not in term_freq:
                term_freq[word] = 1
            else:
                term_freq[word] += 1
    print(f'term freq dict: {term_freq}')
    return term_freq