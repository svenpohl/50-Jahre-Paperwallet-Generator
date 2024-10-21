import secrets
import binascii
import bitcoin
from bitcoin import *
from datetime import datetime

def generate_bitcoin_addresses(total_addresses=25):
    addresses = []
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    start_year = 2025  # Startjahr
    month_index = 0  # Initialer Index für die Monate
    form_feed_counter = 0  # Zähler für Formfeed

    for address_index in range(total_addresses):
        # Berechne den aktuellen Monat basierend auf dem globalen Zähler
        month_name = months[month_index]
        current_date = datetime(start_year, month_index + 1, 1)  # Setze das aktuelle Datum auf den ersten des Monats
        
        # Erzeuge einen zufälligen privaten Schlüssel mit secrets
        private_key = binascii.hexlify(secrets.token_bytes(32)).decode()  # 32 Bytes für den privaten Schlüssel
        
        # Erzeuge den WIF-Private-Key
        wif_private_key = encode_privkey(private_key, 'wif')
        
        # Erzeuge die Bitcoin-Adresse auf Basis des öffentlichen Schlüssels
        public_key = privtopub(private_key)
        bitcoin_address = pubtoaddr(public_key)

        # Fülle das Datum auf 20 Zeichen auf
        month_year_formatted = f"{month_name} {start_year}".ljust(20)  # Format: "Januar 2025" und fülle mit Leerzeichen auf
        
        # Speichere den Index, formatiertes Monat Jahr, die Bitcoin-Adresse und den WIF Private Key
        index = address_index + 1  # Aktuellen Index berechnen
        addresses.append((index, month_year_formatted, bitcoin_address, wif_private_key))
        
        # Erhöhe den Monat-Index
        month_index += 1
        form_feed_counter += 1
        
        # Überprüfe, ob der Monat über 11 hinausgeht (also Januar 2026) und setze zurück
        if month_index > 11:
            addresses.append(("------", "------", "------", "------"))  # Separator hinzufügen
            month_index = 0  # Zurücksetzen des Monatsindex
            start_year += 1  # Erhöhe das Jahr

        # Füge nach jedem 12. Monat ein Formfeed hinzu
        if form_feed_counter == 12:
            addresses.append(("\f", "\f", "\f", "\f"))  # Formfeed hinzufügen
            form_feed_counter = 0  # Formfeed-Zähler zurücksetzen

    return addresses

# Generiere für 50 Jahre Bitcoin-Adressen
addresses_list = generate_bitcoin_addresses(total_addresses=12*50)

# Ausgabe der Adressen
header = f"{'Index':<5} {'Datum':<20} {'Bitcoin-Adresse':<35} {'WIF-Private Key':<45}"
print(header)
print('-' * len(header))  # Trenner für die Kopfzeile

# Dateinamen
with_wif_filename = "adressen_mit_wif.txt"
without_wif_filename = "adressen_ohne_wif.txt"

with open(with_wif_filename, 'w') as with_wif_file, open(without_wif_filename, 'w') as without_wif_file:
    with_wif_file.write(header + "\n")
    with_wif_file.write('-' * len(header) + "\n")  # Trenner für die Kopfzeile
    without_wif_file.write(f"{'Index':<5} {'Datum':<20} {'Bitcoin-Adresse':<35}\n")
    without_wif_file.write('-' * 65 + "\n")  # Trenner für die Kopfzeile

    for index, month_year, address, wif_key in addresses_list:
        # Ausgabe auf der Konsole
        if index == "\f":
            with_wif_file.write("\f")  # Formfeed in die Datei schreiben
            without_wif_file.write("\f")  # Formfeed in die Datei schreiben
        else:
            print(f"{index:<5} {month_year} {address:<35} {wif_key}\n\n", end='')
            
            # Schreibe in die Dateien
            with_wif_file.write(f"{index:<5} {month_year} {address:<35} {wif_key}\n\n")
            without_wif_file.write(f"{index:<5} {month_year} {address:<35}\n\n")

    # Füge Separator nach dem Abschluss der Schleife hinzu, falls nicht bereits vorhanden
    if addresses_list[-1][0] != "------":
        with_wif_file.write("\n\n------\n\n")
        without_wif_file.write("\n\n------\n\n")

print(f"\nAdressen wurden in '{with_wif_filename}' und '{without_wif_filename}' gespeichert.")
