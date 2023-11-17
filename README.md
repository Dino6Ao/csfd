# CSFD.cz
Skripty na CSFD.cz (Česko-slovenskou filmovou databázi) / Scripts related to CSFD.cz (Czech-Slovak movie database)

Otestováno / Tested:
  - CSFD ke dni 29 ledna 2023 / CSFD on 29 January 2023
  - Python 3.6, 3.11
  - Windows 10, Red Hat 6  

## Co skript dělá / Purpose
### CZ  
Stáhne hodnocení/recenze uživatele z webu csfd.cz do formátu .csv, se kterým pak můžete dále pracovat např. v Excelu a importovat výsledek do dalších databází (IMDb, Letterboxd, Trakt...)  


### EN 
Script downloads ratings/comments of the csfd.cz user to .csv format, which can be then opened in ie. Excel and worked with further to import the list to other databases (IMDb, Letterboxd, Trakt...)  


## Jak spustit / How to run
### CZ 
python csfd.py user_id, např. python csfd.py 95  

User ID (číslo) najdete v URL na profilu uživatele, např. uživatel 'golfista' ma ID 95  
https://www.csfd.cz/uzivatel/95-golfista/prehled/
    
Dále pak postupujte podle možností v menu, ktere je v češtině   


### EN 
python csfd.py user_id, ie. python csfd.py 95  

User ID (number) can be found in the URL of the profile, ie. user 'golfista' has ID 95    
https://www.csfd.cz/uzivatel/95-golfista/prehled/

Just follow the options in the menu, which is in Czech language due to majority of Czech speaking users 

## Možnosti / Options
### CZ  
1, Stáhne hodnocení ve formátu .csv:  
csfd_id; název filmu; rok vzniku; datum hodnocení; hodnocení samotné  

2, Stáhne recenze ve formátu .csv:  
csfd_id; název filmu; rok vzniku; datum hodnocení; hodnocení samotné; komentář  

Defaultně CSFD zobrazuje názvy filmů v češtině. Pokud chcete data exportovat v jiném jazyce, je nedříve potřeba toto nastavení po příhlášení v prohlížeči přepnout ve Vašem profilu (Profil -> Nastavení -> Zobrazení -> Priorita názvů filmů) a poté zkopírovat 'permanent_login_token' do souboru csfd_cookie.txt. Tento token se vygeneruje s omezenou platností ve formě cookies po trvalém přihlášení. Návod na jeho nalezení např. zde https://learn.microsoft.com/cs-cz/microsoft-edge/devtools-guide-chromium/storage/cookies Pokud chcete data exportovat v češtině, tento krok můžete ignorovat.


### EN  
1, Download ratings in .csv:  
csfd_id; name of the movie; year it was made; date when rated; rating itself  

2, Download reviews in .csv:  
csfd_id; name of the movie; year it was made; date when rated; rating itself; comment  

By default, CSFD shows the movie titles in Czech. If you want to export the data in a different language, you first need to login with your browser and change those settings in your profile (Profile -> Settings -> View -> Priority of the movie titles) and then copy the 'permanent_login_token' into the file csfd_cookie.txt. This token is generated with limited validity in a form of a cookie after the permanent login. Guide how to extract it can be found ie. here https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/storage/cookies If you want to export the data in Czech language, you can ignore this step.  

## Note  
V případě zájmu je možno rozšířit a přidat další funkce / In case of interest, further options can be added

I have a day job, so this is really optional. If you think that any benefit you obtained here is worth some money and you are willing to pay for it, feel free to send any amount through PayPal

[![](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=QQCS64WL9MJV6)
