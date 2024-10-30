import csv
import os

'''
Write data to CSV file.
'''

def output_csv(articles_data):
    csv_data = []

    # Iterate through each article's details in the data dictionary
    for title, details in articles_data.items():
        authors = ', '.join(details['Author(s)']) if isinstance(details['Author(s)'], list) else details['Author(s)']
        link = details['Link']
        terms = details['Terms and Frequency']
       
        # Iterate through terms and frequencies, create a row for each term-frequency pair
        if not terms:
            csv_data.append([title, authors, 'NA', '0', link])
        else:
            for term, frequency in terms.items():
                csv_data.append([title, authors, term, frequency, link])

    header = ['Title', 'Author(s)', 'Term', 'Frequency', 'Link']
    
    output_file = os.path.expanduser('~/output.csv')

    # Open 'output.csv' file and write article data
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(csv_data)
