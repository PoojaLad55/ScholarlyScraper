def scrape_data(search_terms, sources):

    words_freq = {}

    print(f"Scraping data for terms: {search_terms}, from sources: {sources}")

    for source in sources:
        for word in source:
            if search_terms in word and not words_freq:
                words_freq[word] = 1
            elif search_terms in word:
                words_freq[word] += 1
            
