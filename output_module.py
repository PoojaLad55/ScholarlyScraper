import csv

def output_csv(data):
    csv_data = []
    for title, details in data.items():
        authors = ', '.join(details['Author(s)']) if isinstance(details['Author(s)'], list) else details['Author(s)']
        terms = details['Terms and Frequency']
        for term, frequency in terms.items():
            csv_data.append([title, authors, term, frequency])

    header = ['Title', 'Authors', 'Term', 'Frequency']

    with open('articles_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(csv_data)
