import requests
from bs4 import BeautifulSoup
import re
import sys
import math
import csv
import os.path
from pathlib import Path


if os.path.exists('csfd_cookie.txt'):
  csfd_cookie = Path('csfd_cookie.txt').read_text()
else:
  csfd_cookie = ''

payload = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)\
            AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36',
            'cookie': csfd_cookie,
          }  
        
user_id = (sys.argv[1])
user_url = (f'https://www.csfd.cz/uzivatel/{user_id}')
grab = requests.get(user_url, headers=payload)
soup = BeautifulSoup(grab.text, 'html.parser')
user_name = soup.find('title')
nbsp = u'\xa0'


def get_csfd_ratings():
  rating_url = (f'https://www.csfd.cz/uzivatel/{user_id}/hodnoceni/')
  grab = requests.get(rating_url, headers=payload)
  soup = BeautifulSoup(grab.text, 'html.parser')
  
  pages = soup.find('header', {'class':'box-header'}).find('h2').text.split('(')[1].split(')')[0].replace(' ', '').replace('&nbsp;', '').replace(nbsp, '')
  number = int(pages) / 50
  p = math.ceil(number)
  
  f = open("csfd_ratings.csv", "w", encoding = "utf-8")
  
  for i in range (1, p+1):
    urls = (f'https://www.csfd.cz/uzivatel/{user_id}/hodnoceni/?page={i}')
    grab = requests.get(urls, headers=payload)
    soup = BeautifulSoup(grab.text, 'html.parser')
    
    for div in soup.find_all('div', {'class':'tab-content user-tab-rating'}):
      for ratings in div.find_all('tr'):
        a = ratings.find('a')
        name = ratings.find('a', {'class':'film-title-name'}).text
        year = ratings.find('span', {'class':'info'}).text
        date = ratings.find('td', {'class':'date-only'}).text
        stars = str(ratings.find('span', {'class':'star-rating'}))
        stars_help = stars.split('span class=\"stars ')[1].split('\">')[0]
        
        if stars_help == 'stars-5':
          rating = '100'
        elif stars_help == 'stars-4':
          rating = '80'
        elif stars_help == 'stars-3':
          rating = '60'
        elif stars_help == 'stars-2':
          rating = '40'
        elif stars_help == 'stars-1':
          rating = '20'
        else:
          rating = '0'
        
        f.write(a['href'].split('/film/')[1].split('-')[0] + ';\"' + name + '\";' + year.replace('(','').replace(')','') + ';' + date.replace('\n','').replace('\t','') + ';' + rating + '\n')

  f.close()
    
  print(32 * "-")
  num_lines_csfd = sum(1 for line in open('csfd_ratings.csv', encoding = "utf-8"))
  print(f"Nalezeno {num_lines_csfd} hodnoceni") 
  print(32 * "=")
  
def get_csfd_reviews():
  review_url = (f'https://www.csfd.cz/uzivatel/{user_id}/recenze/')
  grab = requests.get(review_url, headers=payload)
  soup = BeautifulSoup(grab.text, 'html.parser')
  
  pages = soup.find('header', {'class':'box-header'}).find('h2').text.split('(')[1].split(')')[0].replace(' ', '').replace('&nbsp;', '').replace(nbsp, '')
  number = int(pages) / 10
  p = math.ceil(number)
  
  f = open("csfd_reviews.csv", "w", encoding = "utf-8")
  
  for i in range (1, p+1):
    urls = (f'https://www.csfd.cz/uzivatel/{user_id}/recenze/?page={i}')
    grab = requests.get(urls, headers=payload)
    soup = BeautifulSoup(grab.text, 'html.parser')
    
    for div in soup.find_all('div', {'class':'tab-content'}):
      for reviews in div.find_all('div', {'class':'article-content article-content-justify'}):
        a = reviews.find('a')
        name = reviews.find('a', {'class':'film-title-name'}).text
        year = reviews.find('span', {'class':'info'}).text
        date = reviews.find('time').text
        review = reviews.find('div', {'class':'user-reviews-text'}).text
        try:
          stars = str(reviews.find('span', {'class':'star-rating'}))
          stars_help = stars.split('span class=\"stars ')[1].split('\">')[0]
        
          if stars_help == 'stars-5':
            rating = '100'
          elif stars_help == 'stars-4':
            rating = '80'
          elif stars_help == 'stars-3':
            rating = '60'
          elif stars_help == 'stars-2':
            rating = '40'
          elif stars_help == 'stars-1':
            rating = '20'
          else:
            rating = '0'
        except IndexError:
          rating = 'n/a'
        
        f.write(a['href'].split('/film/')[1].split('-')[0] + ';\"' + name + '\";' + year.replace('(','').replace(')','') + ';' + date.replace('\n','').replace('\t','') + ';' + rating + ';\"' + review.replace('\n','').replace('\t','') + '\"\n')

  f.close()
    
  print(32 * "-")
  num_lines_csfd = sum(1 for line in open('csfd_reviews.csv', encoding = "utf-8"))
  print(f"Nalezeno {num_lines_csfd} recenzi") 
  print(32 * "=")    

    
def print_menu():
  print('User:', user_name.string.split(' |')[0], '\nID:   ', user_id)
  print(32 * "-")
  print('1. Stahnout hodnoceni jako .csv')
  print('2. Stahnout recenze jako .csv')
  print('3. Exit')
  print(32 * '-')
  
loop=True      
  
while loop:
  print_menu()
  choice = input("Vyber [1-3]: ")
   
  if choice == '1':     
    print('...... vytvarim soubor csfd_ratings.csv')
    get_csfd_ratings()
  elif choice == '2':
    print('...... vytvarim soubor csfd_reviews.csv')
    get_csfd_reviews()
  elif choice == '3':
      print("Exiting... bye!")
      sys.exit()
  else:
      input('Spatne! Zmackni enter pro pokracovani... ')
      print(48 * '=')
