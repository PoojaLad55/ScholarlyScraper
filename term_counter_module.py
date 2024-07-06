def scrape_data(article_text, serach_query):
    term_freq = {}
    
    article_text = article_text.lower()

    for word in article_text.split():
        if serach_query == word:
            if word not in term_freq:
                term_freq[word] = 1
            else:
                term_freq[word] += 1

    return term_freq