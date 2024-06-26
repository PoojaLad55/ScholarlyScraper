import csv

def output_csv(all_articles):
    output_file = 'ScholarlyScraperOutput.csv'

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['search_term', 'title', 'href', 'snippet', 'term_frequencies']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for entry in all_articles:
            search_term = entry['search_term']
            articles = entry['articles']
            for article in articles:
                writer.writerow({
                    'search_term': search_term,
                    'title': article['title'],
                    'href': article['href'],
                    'snippet': article['snippet'],
                    'term_frequencies': article['term_frequencies']
                })