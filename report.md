# Relazione Tecnica: Realizzazione di un Web Server minimale in Python e pubblicazione di un sito statico

## 1. Introduzione e obiettivi
Questo elaborato ha come obiettivo lo sviluppo di un server HTTP minimale utilizzando il modulo `socket` di Python, in grado di servire contenuti web statici (HTML, CSS, immagini) attraverso la porta `8080` di `localhost`. Il server è progettato per rispondere a richieste HTTP di tipo `GET`, restituendo file come HTML, CSS e immagini dal file system.
Le estensioni opzionali implementate sono:
- la gestione dei MIME types, in modo da poter inviare l'intestazione `Content-Type` corretta,
- il logging delle richieste HTTP in un file di log,
- aggiunta di animazioni.

### Tecnologie utilizzate
- **Socket programming**: per la gestione delle connessioni di rete.
- **Python**: per l'implementazione del server.
- **HTML/CSS**: per la realizzazione del sito web statico.
- **File I/O**: per la lettura dei file richiesti e il logging.

## 2. Progettazione del Web Server

### Descrizione generale
Il server HTTP è realizzato in Python e utilizza **socket TCP** per ricevere richieste dai browser web. Gestisce richieste `GET` e restituisce il contenuto richiesto o una pagina di errore 404, se il file non esiste.

### Struttura del server
- Crea un socket TCP che ascolta su `localhost:8080`.
- Accetta connessioni entranti e gestisce ogni richiesta in un thread separato.
- Serve i file statici presenti nella directory `www/`.
- Se la risposta HTTP è andata a buon fine invia `200 OK`, altrimenti `404 Not Found`.

### Gestione degli errori
Quando il file richiesto non esiste, il server genera una pagina HTML di errore e restituisce una risposta HTTP con codice `404 Not Found`.

## 3. Funzionalità del Server 

### 3.1 Apertura del socket
Il server crea un socket TCP in ascolto sulla porta 8080 di localhost.

### 3.2 Parsing delle richieste
Le richieste HTTP vengono ricevute in formato testuale e viene effettuato il parsing per determinare il metodo (GET) e la risorsa richiesta.

### 3.3 Gestione delle risposte
- Se il file esiste, viene restituito con `200 OK` e il corretto `Content-Type`.
- Se il file non esiste, viene restituita una pagina HTML generica con codice `404 Not Found`.

### 3.4 MIME Types
È presente una mappatura base per estensioni comuni: `.html`, `.css`, `.jpg` e `.png`.

### 3.5 Logging
Tutte le richieste gestite vengono registrate nel file `log.txt`, riportando il tipo di richiesta, la risorsa e il risultato (200 o 404).

## 4. Descrizione del sito 

### 4.1 Pagine HTML
- `index.html`: pagina principale, presenta il sito relativo all'ACMilan,
- `biglietti.html`: link per l’acquisto delle diverse tipologie di biglietti,
- `contatti.html`: link riguardanti le pagine social del Milan,
- `storia.html`: storia della società, dello stadio e del logo,
- `trofei.html`: palmares delle vittorie.

### 4.2 Stile e layout
- Utilizzo del foglio di stile `style.css` per la definizione di colori, spaziature e layout grafico.
- Inclusione di numerose immagini che rendono il sito visivamente ricco.

### 4.3 Immagini
Sono presenti due sottocartelle:
- `coppe/`: contiene immagini relative a trofei,
- `loghi/`: contiene tutti i loghi della storia del Milan.

## 5. Esecuzione del server

### 5.1 Prerequisiti
- Python 3 installato nel sistema.

### 5.2 Esecuzione
1. Aprire il terminale nella directory contenente `main.py` ed avviare il servere con **python main.py**.
2. Accedere da browser a: `http://localhost:8080`.

## 6. Considerazioni finali
Questo progetto ha permesso di comprendere:
- le basi del protocollo HTTP e della comunicazione tra client e server,
- l’utilizzo dei socket in Python per creare un server personalizzato,
- le fondamenta della pubblicazione di un sito web statico.

Il server funziona correttamente, risponde alle richieste GET e gestisce con semplicità il caricamento di file HTML, CSS e immagini. Sono state inoltre implementate funzionalità aggiuntive richieste dalla traccia, rendendo il progetto completo e funzionale.
