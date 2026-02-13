# Online Sales Analysis

## Opis projekta
Ovaj projekat predstavlja jednostavan sistem za upravljanje proizvodima i korpom kupca u online prodavnici. Projekat je razvijen u Pythonu koristeći objektno-orijentisano programiranje (OOP) i Git za upravljanje verzijama.

## Struktura projekta

### Product (product.py)
Klasa Product sadrži:
- name (naziv proizvoda)
- price (cena proizvoda)
- quantity (količina proizvoda)

Metode:
- prikaz informacija o proizvodu
- ažuriranje količine proizvoda

### ProductManager (product_manager.py)
Klasa ProductManager upravlja listom proizvoda.

Funkcionalnosti:
- dodavanje proizvoda
- prikaz svih proizvoda
- računanje ukupne vrednosti inventara
- uklanjanje proizvoda po imenu

### Cart (cart.py)
Klasa Cart upravlja korpom kupca.

Funkcionalnosti:
- dodavanje proizvoda u korpu
- prikaz sadržaja korpe
- računanje ukupne vrednosti za naplatu

## Rad sa Git granama
U projektu su korišćene sledeće grane:
- main
- add-product-removal
- add-cart-functionality

## Sigurnost podataka
Datoteka config.json i snimci ekrana su isključeni iz praćenja pomoću .gitignore datoteke.