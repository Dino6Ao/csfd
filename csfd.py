import requests
from bs4 import BeautifulSoup
import re
import sys
import math
import csv
import os.path
from pathlib import Path


if os.path.exists('csfd_cookie.txt'):
  csfd_cookie = Path('csfd_cookie.txt').read_text().strip('\n')
else:
  csfd_cookie = ''

if os.path.exists('imdb_cookie.txt'):
  imdb_cookie = Path('imdb_cookie.txt', encoding='latin-1').read_text().replace('\n', '').strip()
else:
  imdb_cookie = ''

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
        
        f.write(a['href'].split('/film/')[1].split('-')[0] + ';\"' + name + '\";' + year.replace('(','').replace(')','') + ';' + date.replace('\n','').replace('\t','') + ';' + rating + ';\"' + review.replace('\n','').replace('\t','').replace(';',',') + '\"\n')

  f.close()
    
  print(32 * "-")
  num_lines_csfd = sum(1 for line in open('csfd_reviews.csv', encoding = "utf-8"))
  print(f"Nalezeno {num_lines_csfd} recenzi") 
  print(32 * "=")    

def get_imdb_links():
  with open('csfd_ratings.csv', encoding="utf8") as movies:
    links = movies.read().splitlines()
    
  f = open("csfd_imdb_links.csv", "w+")
  fl = open("csfd_no_imdb_link.csv", "w+")
  
  for csfd in links:
    csfd_link = csfd.split(';')[0]
    urls = (f'https://www.csfd.cz/film/{csfd_link}')
    grab = requests.get(urls, headers=payload)
    soup = BeautifulSoup(grab.text, 'html.parser')

    try:
      csfd_rating = soup.select_one('a[href="#close-dropdown"]')['data-rating']
      imdb_link = soup.select_one('a.button.button-big.button-imdb')['href']
    except Exception:
      imdb_link = None
    
    if imdb_link is not None:
      f.write(csfd.split(';')[0] + "," + imdb_link.split('/title/tt')[1].split('/')[0] + "," + csfd_rating + "\n")
    else:
      fl.write(csfd.split(';')[0] + "," + "none" + "," + csfd_rating + "\n")
      
  f.close()
  fl.close()
    
  print(32 * "-")
  num_lines_imdb = sum(1 for line in open('csfd_imdb_links.csv', encoding = "utf-8"))
  num_lines_imdb_fl = sum(1 for line in open('csfd_no_imdb_link.csv', encoding = "utf-8"))
  print(f"Nalezeno {num_lines_imdb} linku") 
  print(f"Nenalezeno {num_lines_imdb_fl} linku") 
  print(32 * "=")  

def rate_imdb():
  with open('csfd_imdb_links.csv') as imdb:
    filmy = imdb.read().splitlines()
  
  f = open("imdb_fail.csv", "w+")
  suc = 0
    
  for film in filmy:
    rating_csfd = (film.split(','))[2]
    csfd_int = (int(rating_csfd))
    decimal = (int(10))
    rating_imdb = (int(csfd_int / decimal))
    imdb_id = (film.split(','))[1]
    
    req_body = { 'query': 'mutation UpdateTitleRating($rating: Int!, $titleId: ID!) { rateTitle(input: {rating: $rating, titleId: $titleId}) { rating { value __typename } __typename }}',
      'operationName': 'UpdateTitleRating',
      'variables': {
          'rating': rating_imdb,
          'titleId': "tt" + imdb_id
      }
    }
    headers = {
      "content-type": "application/json",
      "cookie": imdb_cookie
    }

    resp = requests.post("https://api.graphql.imdb.com/", json=req_body, headers=headers)
  
    soup = BeautifulSoup(resp.text, 'html.parser')

    if resp.status_code != 200:
      if resp.status_code == 429:
        f.write(film + ",IMDb Rate limit exceeded" + "\n")
        sleep(1)
      else:
        f.write(film + "," + resp.status_code + "\n")
        break

    json_resp = resp.json()
    
    if 'errors' in json_resp and len(json_resp['errors']) > 0:
      first_error_msg = json_resp['errors'][0]['message']

      if 'Authentication' in first_error_msg:
        print(f"Neplatna IMDb cookie")
        exit(1)
      else:
        f.write(film + "," + first_error_msg + "\n")
    else:
      suc += 1
          
  f.close()
  
  print(32 * "-")
  num_lines_imdb = sum(1 for line in open('csfd_imdb_links.csv', encoding = "utf-8"))
  num_lines_imdb_fl = sum(1 for line in open('imdb_fail.csv', encoding = "utf-8"))
  print(f"Nalezeno celkem {num_lines_imdb} filmu")
  print(f"Hodnoceno {suc} filmu") 
  print(f"Nehodnoceno {num_lines_imdb_fl} filmu, viz imdb_fail.csv") 
  print(32 * "=")  

def rate_fail_imdb():
  with open('imdb_fail.csv') as imdb:
    filmy = imdb.read().splitlines()
    
  suc = 0
    
  for film in filmy:
    rating_csfd = (film.split(','))[2]
    csfd_int = (int(rating_csfd))
    decimal = (int(10))
    rating_imdb = (int(csfd_int / decimal))
    imdb_id = (film.split(','))[1]
    
    req_body = { 'query': 'mutation UpdateTitleRating($rating: Int!, $titleId: ID!) { rateTitle(input: {rating: $rating, titleId: $titleId}) { rating { value __typename } __typename }}',
      'operationName': 'UpdateTitleRating',
      'variables': {
          'rating': rating_imdb,
          'titleId': "tt" + imdb_id
      }
    }
    headers = {
      "content-type": "application/json",
      "cookie": imdb_cookie
    }

    resp = requests.post("https://api.graphql.imdb.com/", json=req_body, headers=headers)
  
    soup = BeautifulSoup(resp.text, 'html.parser')

    if resp.status_code != 200:
      if resp.status_code == 429:
        sleep(1)
      else:
        break

    json_resp = resp.json()
    
    if 'errors' in json_resp and len(json_resp['errors']) > 0:
      first_error_msg = json_resp['errors'][0]['message']

      if 'Authentication' in first_error_msg:
        print(f"Neplatna IMDb cookie")
        exit(1)
      else:
        break
    else:
      suc += 1
        
  print(32 * "-")
  print(f"Hodnoceno {suc} filmu") 
  print(32 * "=")  

def csfd_cookie_validity():
  csfd_nastaveni = (f'https://www.csfd.cz/soukrome/nastaveni/')
  grab = requests.get(csfd_nastaveni, headers=payload)
  soup = BeautifulSoup(grab.text, 'html.parser')
  
  nastaveni = 'Nastavení - Účet'
  nastavenie = 'Nastavenie - Účet'
  meta_contents = [meta_tag.get('content', '') for meta_tag in soup.find_all('meta')]
  
  if any(nastaveni in content or nastavenie in content for content in meta_contents):
    print('CSFD cookie je v poradku.')
  else:
    print('CSFD cookie je neplatna!')
  
  print(32 * "=")

def print_menu():
  print('User:', user_name.string.split(' |')[0], '\nID:   ', user_id)
  print(32 * "-")
  print('1. Stahnout hodnoceni jako .csv')
  print('2. Stahnout recenze jako .csv')
  print('3. Stahnout IMDb ID jako .csv (po spusteni #1)')
  print('4. Ohodnotit na IMDb (po spusteni #3)')
  print('5. Ohodnotit znovu (imdb_fail.csv)')
  print('9. Kontrola CSFD cookie')
  print('0. Exit')
  print(32 * '-')
  
loop=True      
  
while loop:
  print_menu()
  choice = input("Vyber [1-6]: ")
   
  if choice == '1':     
    print('...... vytvarim soubor csfd_ratings.csv')
    get_csfd_ratings()
  elif choice == '2':
    print('...... vytvarim soubor csfd_reviews.csv')
    get_csfd_reviews()
  elif choice == '3':
    print('...... vytvarim soubor csfd_imdb_links.csv')
    get_imdb_links()
  elif choice == '4':
    print('...... hodnotim na IMDb')
    rate_imdb()
  elif choice == '5':
    print('...... hodnotim znovu na IMDb')
    rate_fail_imdb()
  elif choice == '9':
    print('...... kontroluji')
    csfd_cookie_validity()
  elif choice == '0':
      print("Exiting... bye!")
      sys.exit()
  else:
      input('Spatne! Zmackni enter pro pokracovani... ')
      print(48 * '=')
