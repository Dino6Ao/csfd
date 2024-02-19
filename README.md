# CSFD.cz
Skripty na CSFD.cz (Česko-slovenskou filmovou databázi) / Scripts related to CSFD.cz (Czech-Slovak movie database)

Otestováno / Tested:
  - CSFD ke dni 19-února-2024 / CSFD on 19-February-2024
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

3, Stáhne IMDb ID ve formátu .csv:  
csfd_id, imdb_id, hodnocení

Odkaz na IMDb je viditelný po příhlášení na jednotlivých profilech filmů v pravém menu (= proto je nutné mít správnou csfd_cookie, viz předchozí bod. Bez csfd_cookie nebude tato část skriptu fungovat!). Ne každý film tuto informaci ovšem má, v tom případě ji můžete později do vygenerovaného .csv souboru doplnit ručně.

Pokud vám tato část spadne hned u prvního filmu s hláškou "UnboundLocalError: cannot access local variable 'csfd_rating' where it is not associated with a value", znamená to, že nemáte správnou csfd_cookie. Můžete to ověřit např. tím, že změníte názvy filmů do jiného jazyka (popsáno v bodě #2) a pokud se stále budou stahovat česky, csfd_cookie je špatně.

4, Ohodnotí filmy na IMDb  

Jako zdrojový soubor se používá csfd_imdb_links.csv, který se vygeneroval v bodě #3. Zde jsem vycházel především z https://github.com/TobiasPankner/Letterboxd-to-IMDb (tímto děkuji jeho autorovi!). Aby tato funkce fungovala je potřeba mít uloženou imdb_cookie, která uživatele autentifikuje. Obrázkový návod je dostupný na uvedeném odkazu v sekci "Getting the IMDb cookie". Celou cookie pak jen zkopírujte do souboru imdb_cookie.txt. IMDb API není zrovna nejspolehlivější, takže je možné, že Vám nějaké filmy neprojdou. Pokud se tak stane, najdete je v souboru imdb_fail.csv.

5, Ohodnotí filmy na IMDb, které neprošly v bodě #4  

Jako zdrojový soubor se používá imdb_fail.csv, který můžete libovolně upravovat (pokud nechcete znovu pouštět celé hodnocení v bodě #4) a najdete v něm i chybovou hlášku, kvůli které nešel film ohodnotit na IMDb.

9, Zkontroluje platnost CSFD cookie  

Kontrola, zda uživatel správně zkopíroval csfd_cookie potřebnou v bodě #3

### EN  
1, Download ratings in .csv:  
csfd_id; name of the movie; year it was made; date when rated; rating itself  

2, Download reviews in .csv:  
csfd_id; name of the movie; year it was made; date when rated; rating itself; comment  

By default, CSFD shows the movie titles in Czech. If you want to export the data in a different language, you first need to login with your browser and change those settings in your profile (Profile -> Settings -> View -> Priority of the movie titles) and then copy the 'permanent_login_token' into the file csfd_cookie.txt. This token is generated with limited validity in a form of a cookie after the permanent login. Guide how to extract it can be found ie. here https://learn.microsoft.com/en-us/microsoft-edge/devtools-guide-chromium/storage/cookies If you want to export the data in Czech language, you can ignore this step.

3, Download IMDb ID in .csv:  
csfd_id, imdb_id, rating itself

Link to IMDb is visible after login on each individual movie profile page in the right menu (= it is therefore important to have the correct csfd_cookie, see the previous point. Without csfd_cookie this part of the script won't work!) Not all the movies have this information though, in that case you can fill it out manually into the generated .csv file

If this part of the script fails with the line "UnboundLocalError: cannot access local variable 'csfd_rating' where it is not associated with a value", it means you have an incorrect csfd_cookie. You can verify that by changing the names of the movies to a different language (as described in task #2) and if they are still downloading in czech, csfd_cookie is wrong.

4, Rate movies on IMDb  

Uses csfd_imdb_links.csv as the source file, which was genereted in the task #3. I have mainly used https://github.com/TobiasPankner/Letterboxd-to-IMDb for this (I hereby thank the author!). In order for this function to work correctly, you need to have imdb_cookie, which authenticates the user. Guide with pictures is available on the previous link under "Getting the IMDb cookie". You then have to copy the whole string into the file imdb_cookie.txt. IMDb API is not the most reliable one so it's therefore possible that some ratings will fail. If that happens, you can find them in the file imdb_fail.csv.

5, Rate movies on IMDb, which have failed in #4  

Uses imdb_fail.csv as the source file, which you can freely edit (if you don't want to run the entire database again as in point #4) and where you can find the error message stating why the movie wasn't possible to be rated.

9, Checks validity of the CSFD cookie  

Checks if the user has copied the csfd_cookie value properly which is needed to run #3


## Note  
V případě zájmu je možno rozšířit a přidat další funkce / In case of interest, further options can be added.  
Pokud najdete nějakou chybu či nesrovnalost, budu rád, když mě na ni upozorníte / If you find some error or inconsistency, please do let me know about it.

------

I have a day job, so this is really optional. If you think that any benefit you obtained here is worth some money and you are willing to pay for it, feel free to send any amount through PayPal

[![](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/donate/?hosted_button_id=QQCS64WL9MJV6)
