import os
import pickle

initial_urls_db_file = os.path.join(os.getcwd(), 'db', 'initial_urls.db')
initial_urls_text_file = os.path.join(os.getcwd(), 'initial-urls.txt')

initial_urls = set(line.strip() for line in open(initial_urls_text_file))

print(initial_urls)

with open(initial_urls_db_file, mode='wb') as f:
    pickle.dump(initial_urls, f)