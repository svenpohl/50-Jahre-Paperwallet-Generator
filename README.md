# 50-Jahre-Paperwallet-Generator
Ein Python-Script um für 50 Jahre Paperwallets zu generieren

Dieses Python-Script generiert 600 Paperwallet-Adressen und erzeugt zwei Text-Dateien. Eine mit WIF-Private-Key zum Ausdrucken und eine ohne WIF-Private-Key zum Vorhalten der Adressen. Die Idee ist dabei, einen Sparplan mit sehr kleinen Bitcoin-Beträgen in Selbstverwahrung zu erzeugen. Die Textdatei enthält nach 12 Monaten einen Formfeed, so dass für jedes Jahr eine Seite ausgedruckt wird. Bei sehr hohen Gebühren könnten kleine Beträge und UTXO's feststecken, so dass ggfs. der Private-Key in eine Bitcoin-Core-Wallet importiert und als Transaktion gebündelt werden muss, um effektiv die Bitcoins später wieder bewegen zu können. Wir wissen nicht, welche Gebühren in 50 Jahren auf dem Bitcoin-Netzwerk vorherrschen werden.

Hier ein Beispiel der Ausgabe - Datei mit WIF-Private Key. Die andere Datei ist identisch bis auf das Fehlen des WIF-Private Key's.

Benutzung auf eigene Gefahr! Das Script soll eine Inspiration für eine eigene Version sein. Der Code kann Fehler enthalten und MUSS selbst geprüft bzw. aktualisiert werden.

Beispiel MIT WIF-Private Key (zum Ausdrucken, danach löschen)
```
Index Datum                Bitcoin-Adresse                     WIF-Private Key                              
------------------------------------------------------------------------------------------------------------
1     January 2025         1LSUesVPKGa42C6QQ3ynTUrfB7bCEQo4qc  5J9eJQVynywDFz3Yn51dZoALxmbFMVaYKnQivwrqAVncGxD9bkt

2     February 2025        1s2mz82Z9c47f1mLmhdtfC8GzeQ2UbVX5   5HrmxHtEpa3qdLbMfU7jk2n1PHxyjgBi1gHx3cTwrGiJp5QjhCt

3     March 2025           1NxtCo9WZGHhBx7ZMTfvouDP816dFNeXan  5Jhk4yLdSMtyeeyt8FeGS55gwJZWBdHa1WrviJaFtcdkrMrUw7Y

4     April 2025           1JXGxkBN3z6mPxFjz3CQsBfYoAnpQR6cMC  5KHPypybqZ731ArNonpTGgvwcDj7zdhuys8G1eAYvF9r3oUBJHX

5     May 2025             1LDJqxkE4ZpsGAxozN1kLFrcS141yQFhvB  5JFtd9wYBkMvLbRgtHbfPGPLZFE4HRky8CafjMUjSN2jzP7y1EQ

6     June 2025            1HT5nducctA3ipm5L3rC48fb1y6Qt3hKiJ  5HuSVZy4E1nfsHz74kiQNpX8i9y9jfQgofkXenPpifKTow2fikz

7     July 2025            1HArGxkR2YmoqT1vHukVVvRXGh3E2teuxJ  5JyRWPzerjPduA9dvEB56NmoqzhBvqCzV9NFUzUfRJvorZ9Rhty

8     August 2025          13zp9AEA65dckjAXJFHTx1GjdrdVpai9KA  5KTe3Vp7aD8xFuh2fX6qr77MTwaQbjSQqbKWVC8dXx3ZT4fbscM

9     September 2025       1P5k4aG616f2BYkVPz42QNPaEPkKiaZDi5  5JMBDE3tBkD7xx5EpzsZAPnBtDqS32dEpaYiEd4M4f4HZNaJmHi

10    October 2025         15CEiCH2is5PdhC1huMKRVfnV7Ra2JBkAc  5JDZh3jPNGKxyfCEjr1P52rmHLKTU46usYhA1LxQ99hhDdTNVM5

11    November 2025        1AJDpjHKTTQxcve9rajfVo9XhejJGSaxL6  5HydizWsn4NcrGZ7hrqgrFAunYvjHvc4QfigoN7jdHyBdK23BqN

12    December 2025        1Lss2aHkSsnAoR7288b1gUsvCnk8sT21LB  5JZBDMLgFcDpaZYFfVy8ZC2SfWYK5o477Sho4WmsNA2gTwXjrxb

------ ------ ------                              ------

13    January 2026         1LUbmKtSL434QcC4mrJn1281tnd9kv4CVP  5KDDy3swU9ECDRnbH3UWCRqgn76fxcTe9tEjFuYJhnKLUQaeNXg

14    February 2026        17uVQQMmRNrEGHL2dcfYqVmkquVD6iKchK  5Ki7ymAexgz6QqrdBPNgqcBRqV98usKByHBbwfQgMRpW6xQ9TVY
```


Beispiel für eine Datei ohne den WIF-Private Key (nur die Adressen) zum Speichern und späterem Aufladen.
```
Index Datum                Bitcoin-Adresse                    
-----------------------------------------------------------------
1     January 2025         1LSUesVPKGa42C6QQ3ynTUrfB7bCEQo4qc 

2     February 2025        1s2mz82Z9c47f1mLmhdtfC8GzeQ2UbVX5  

3     March 2025           1NxtCo9WZGHhBx7ZMTfvouDP816dFNeXan 

4     April 2025           1JXGxkBN3z6mPxFjz3CQsBfYoAnpQR6cMC 

5     May 2025             1LDJqxkE4ZpsGAxozN1kLFrcS141yQFhvB 

6     June 2025            1HT5nducctA3ipm5L3rC48fb1y6Qt3hKiJ 

7     July 2025            1HArGxkR2YmoqT1vHukVVvRXGh3E2teuxJ 

8     August 2025          13zp9AEA65dckjAXJFHTx1GjdrdVpai9KA 

9     September 2025       1P5k4aG616f2BYkVPz42QNPaEPkKiaZDi5 

10    October 2025         15CEiCH2is5PdhC1huMKRVfnV7Ra2JBkAc 

11    November 2025        1AJDpjHKTTQxcve9rajfVo9XhejJGSaxL6 

12    December 2025        1Lss2aHkSsnAoR7288b1gUsvCnk8sT21LB 

------ ------ ------                             

13    January 2026         1LUbmKtSL434QcC4mrJn1281tnd9kv4CVP 

14    February 2026        17uVQQMmRNrEGHL2dcfYqVmkquVD6iKchK 

15    March 2026           19nsHrh6Kbmax2RFnyPDrh82FuW9JpCFha 

16    April 2026           1EuUitLzVUtNGwV5VLktzTYnr9Gph3jHRj 

17    May 2026             1Fh3YXbyWfkXtcHGu1oXDmeKgQ7Bf5jC6v 

```

