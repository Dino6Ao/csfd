# CSFD.cz
Skripty na CSFD.cz (Česko-slovenskou filmovou databázi) / Scripts related to CSFD.cz (Czech-Slovak movie database)

Otestováno / Tested:
  - CSFD ke dni 27 ledna 2023 / CSFD on 27 January 2023
  - Python 3.6, 3.11
  - Windows 10, Red Hat 6  

## Co skript dělá / Purpose of the script
Stáhne hodnocení/recenze uživatele z webu csfd.cz do formátu .csv, se kterým pak můžete dále pracovat např. v Excelu / Script downloads ratings/comments of the csfd.cz user to .csv format, which can be then opened in ie. Excel and worked with further  


## Jak spustit / How to run
python csfd.py user_id, ie. python csfd.py 61731  

User ID (číslo) najdete v URL na profilu uživatele, např. moje / User ID (number) can be found in the URL of the profile, ie. mine  
https://www.csfd.cz/uzivatel/61731-barak/prehled/  
    
Dále pak postupujte podle možností v menu, ktere je v češtině / Just follow the options in the menu, which is in Czech language due to majority of Czech speaking users  

## Možnosti / Options
### CZ  
1, Stáhne hodnocení ve formátu .csv:  
csfd_id, název filmu, rok vzniku, datum hodnocení, hodnocení samotné  

2, Stáhne recenze ve formátu .csv:  
csfd_id,název filmu, rok vzniku, datum hodnocení, hodnocení samotné, komentář  


### EN  
1, Download ratings in .csv:  
csfd_id, name of the movie, year it was made, date when rated, rating itself  

2, Download reviews in .csv:  
csfd_id, name of the movie, year it was made, date when rated, rating itself, comment  



## Note  
V případě zájmu je možno rozšířit a přidat funkce / In case of interest, further options can be added  
