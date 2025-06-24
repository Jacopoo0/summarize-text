# Servizi di Analisi Testo con FastAPI e HuggingFace

Questo progetto offre un semplice servizio web per l'analisi del testo, tra cui riassunto e analisi del sentimento, utilizzando FastAPI e i modelli di HuggingFace Transformers.

## Struttura della Cartella

```
huggingface/
│
├── main.py                  # Applicazione FastAPI principale
├── requirements.txt         # Dipendenze Python necessarie
└── templete/
    ├── index.html           # Pagina principale con form di input
    └── summary.html         # Pagina di visualizzazione del risultato
```

## Requisiti

- Python 3.8+
- Le dipendenze elencate in `requirements.txt`:
  - fastapi
  - transformers
  - jinja2
  - uvicorn

## Installazione

1. **Clona la repository o copia i file nella tua cartella di lavoro.**
2. **Installa le dipendenze:**
   ```sh
   pip install -r requirements.txt
   ```

## Avvio del Server

Per avviare il server FastAPI, esegui:

```sh
uvicorn main:app --reload
```

Il server sarà disponibile su [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Come Funziona

1. **Accesso alla Home:**  
   Vai su `http://127.0.0.1:8000` per visualizzare la pagina principale (`index.html`), dove puoi inserire il testo da analizzare e scegliere il tipo di servizio (riassunto o analisi del sentimento).

2. **Invio del Testo:**  
   Dopo aver inserito il testo e selezionato il servizio, premi "Invia". Il form invia una richiesta POST a `/summary`.

3. **Elaborazione:**  
   - Se scegli "Riassunto", viene utilizzato il pipeline di HuggingFace per generare un riassunto del testo.
   - (Da implementare: se scegli "Analisi del Sentimento", verrà eseguita l'analisi del sentimento.)

4. **Risultato:**  
   Il risultato viene mostrato in una nuova pagina (`summary.html`).

## Note

- Puoi aggiungere altri servizi modificando la logica in `main.py` e aggiornando il template HTML.
- Assicurati che la cartella `templete` sia scritta correttamente e contenga i file HTML necessari.

## Esempio di requirements.txt

```
fastapi
transformers
jinja2
uvicorn
```

---

