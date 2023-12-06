#importing libraries
import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.bbc.com/news'

#retrieving content from the web
try:
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        headline_elements = soup.find_all('a', class_='gs-c-promo-heading')
        headlines = []  # List to store the headline text

        for element in headline_elements:
            if element.h3:
                headline_text = element.h3.text.strip()
                print("*" + headline_text + "\n")
                headlines.append(headline_text)  # Add the text to the list

    else:
        print("Failed to retrieve the webpage with status code:", response.status_code)

except:
    print("Oops, something went wrong!")

#function for saving the content
def save_to_csv(headlines, filename):
    with open(filename,'w') as file:
        writer = csv.writer(file)
        for item in headlines:
            writer.writerow([item])  # Write only the text to the CSV

if headlines:
    save_to_csv(headlines, 'headlines.csv')
