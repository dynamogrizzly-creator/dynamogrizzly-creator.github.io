# 📸 Come aggiungere un album fotografico

Guida per aggiungere nuovi album al sito **dodgeballravenna.it** senza toccare codice.

---

## Cosa ti serve

- Un account GitHub (chiedi le credenziali al responsabile del sito)
- Le foto dell'evento già caricate su Cloudinary

---

## STEP 1 — Carica le foto su Cloudinary

1. Vai su [cloudinary.com](https://cloudinary.com) e accedi
2. Apri **Media Library**
3. Crea una nuova cartella con questo formato: `ANNO/nome-evento`
   - Es: `2026/serie-a-bologna`
   - Es: `2026/allenamento-aperto-marzo`
   - Usa solo lettere minuscole, numeri e trattini. **Niente spazi o lettere accentate.**
4. Carica tutte le foto dell'evento in quella cartella
5. Prendi nota del percorso della cartella (ti servirà dopo)

> 💡 **Suggerimento:** scegli una foto bella come copertina, aprila e copia il suo URL  
> (click sulla foto → "Copy URL"). Ti servirà nel prossimo step.

---

## STEP 2 — Crea il file dell'album su GitHub

1. Vai su [github.com](https://github.com) e accedi
2. Apri il repository del sito: `dynamogrizzly-creator/dynamogrizzly-creator.github.io`
3. Entra nella cartella **`_pages/`**
4. Clicca su **"Add file" → "Create new file"**

### Dai un nome al file

In alto dove si scrive il nome del file, inserisci:

```
_pages/album-ANNO-MESE-GIORNO-nome-evento.md
```

Esempi:
- `_pages/album-2026-03-15-serie-a-bologna.md`
- `_pages/album-2026-06-20-torneo-estivo.md`

> ⚠️ Il nome deve iniziare con `album-`, usare solo lettere minuscole, numeri e trattini.

### Incolla il template

Vai al file **`TEMPLATE-album.md`** nel repository, copia tutto il contenuto e incollalo nell'editor.

### Compila i campi

Sostituisci tutti i valori in MAIUSCOLO con le informazioni reali dell'evento:

| Campo | Cosa inserire | Esempio |
|-------|--------------|---------|
| `title` | Nome dell'evento | `"GrizzCup"` |
| `permalink` | URL della pagina | `/album/2026-08-12-grizzcup/` |
| `cloudinary_folder` | Cartella Cloudinary | `"2026/grizzcup"` |
| `data` | Data evento | `2026-08-12` |
| `anno` | Anno evento | `2026` |
| `categoria` | Tipo evento | `"Torneo"` |
| `descrizione` | Frase descrittiva | `"Il torneo estivo dei Grizzlies."` |
| `cover` | URL foto copertina | `"https://res.cloudinary.com/..."` |
| `og_image` | Uguale alla cover | Vedi nota sotto |

> 💡 **Per `og_image`:** prendi l'URL della cover e aggiungi `w_1200,q_auto/` dopo `/upload/`  
> Es: `.../upload/v123456/foto.jpg` → `.../upload/w_1200,q_auto/v123456/foto.jpg`

---

## STEP 3 — Salva il file

1. Scorri in basso fino a **"Commit new file"**
2. Nel campo del messaggio scrivi: `feat: aggiungi album NOME-EVENTO`
3. Lascia selezionato **"Commit directly to the main branch"**
4. Clicca **"Commit new file"**

---

## STEP 4 — Avvia il sync delle foto

Il sistema importa le foto da Cloudinary automaticamente ogni notte, ma puoi forzarlo subito:

1. Vai su **Actions** (tab in alto nel repository)
2. Clicca su **"Sync Cloudinary Photos"** nella lista a sinistra
3. Clicca **"Run workflow" → "Run workflow"**
4. Aspetta circa 30 secondi che finisca (pallino verde ✅)

---

## STEP 5 — Controlla il risultato

Dopo 2-3 minuti il sito si aggiorna automaticamente. Vai su:

```
https://dodgeballravenna.it/album/ANNO/
```

Dovresti vedere il nuovo album nella griglia. Cliccaci sopra per verificare che le foto siano caricate correttamente.

---

## ❓ Domande frequenti

**Le foto non appaiono dopo il sync**  
Controlla che il campo `cloudinary_folder` nel file `.md` corrisponda esattamente al percorso della cartella su Cloudinary (maiuscole, spazi e trattini inclusi).

**Voglio cambiare la foto di copertina**  
Apri il file `.md` su GitHub → clicca l'icona matita ✏️ → modifica il campo `cover` → commit.

**Ho sbagliato qualcosa nel file**  
Apri il file su GitHub → clicca l'icona matita ✏️ → correggi → commit.

**Voglio eliminare un album**  
Apri il file su GitHub → clicca i tre puntini `...` → "Delete file" → commit.

**Il sito non si aggiorna**  
Vai su Actions → "pages build and deployment" → "Run workflow" per forzare il deploy.

---

## 📁 Struttura delle cartelle (per riferimento)

```
_pages/
  album-2026-08-12-grizzcup.md      ← file album
  album-2026-03-15-serie-a.md       ← altro album

album/
  2026/
    index.html                       ← pagina anno (creata una volta sola)

TEMPLATE-album.md                    ← template da copiare
COME-AGGIUNGERE-ALBUM.md            ← questa guida
```

> 💡 Se è il primo album di un anno nuovo (es. 2027), chiedi al responsabile del sito  
> di creare la cartella `album/2027/index.html` — si fa in 2 minuti.

---

*Guida aggiornata a marzo 2026 — Ravenna Grizzlies / Dynamo Grizzly ASD*
