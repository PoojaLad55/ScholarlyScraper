import output_module

def scrape_data(article_text):
    
    term_freq = {}
    
    for word in article_text.split():
                    if term in word:
                        if word not in term_freq:
                            term_freq[word] = 1
                        else:
                            term_freq[word] += 1

    return term_freq