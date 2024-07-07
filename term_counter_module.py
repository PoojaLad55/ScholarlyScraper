'''
Parses through user's list of search terms and identifies in article text.
Counts frequency of each search term and stores in dictionary.
'''

def term_counter(article_text, search_terms):
    term_freq = {}
    
    article_text = article_text.lower()

    # Iterates through each word in article text to find search terms and their respective frequencies
    for word in article_text.split():
        for term in search_terms:
            if term == word:
                if word not in term_freq:
                    term_freq[word] = 1
                else:
                    term_freq[word] += 1

        return term_freq