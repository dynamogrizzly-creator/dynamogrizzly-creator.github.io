# 📰 Come aggiungere una news

Guida per pubblicare nuove notizie sul sito **dodgeballravenna.it** senza toccare codice.

---

## Cosa ti serve

- Un account GitHub (chiedi le credenziali al responsabile del sito)
- Il testo della news pronto
- Un'immagine (opzionale ma consigliata)

---

## STEP 1 — Carica l'immagine (opzionale)

Se vuoi aggiungere un'immagine alla news:

1. Vai su [github.com](https://github.com) e accedi
2. Apri il repository: `dynamogrizzly-creator/dynamogrizzly-creator.github.io`
3. Entra nella cartella **`assets/images/`**
4. Clicca **"Add file" → "Upload files"**
5. Trascina l'immagine e clicca **"Commit changes"**

> 💡 **Suggerimento:** usa immagini in formato `.webp` o `.jpg`, non troppo pesanti (max 500KB).  
> Dai un nome descrittivo senza spazi: `vittoria-bologna-2026.webp`

---

## STEP 2 — Crea il file della news su GitHub

1. Entra nella cartella **`_posts/`**
2. Clicca **"Add file" → "Create new file"**

### Dai un nome al file

Il nome deve seguire questo formato esatto:

```
ANNO-MESE-GIORNO-titolo-breve.md
```

Esempi:
- `2026-03-15-vittoria-serie-a-bologna.md`
- `2026-06-01-nuovi-allenamenti-estivi.md`
- `2026-08-12-grizzcup-risultati.md`

> ⚠️ Il nome deve iniziare con la data nel formato `ANNO-MESE-GIORNO`.  
> Usa solo lettere minuscole, numeri e trattini. Niente spazi o accenti.

### Incolla il template

Vai al file **`TEMPLATE-news.md`** nel repository, copia tutto il contenuto e incollalo nell'editor.

### Compila i campi

Sostituisci tutti i valori in MAIUSCOLO con le informazioni reali:

| Campo | Cosa inserire | Esempio |
|-------|--------------|---------|
| `title` | Titolo della news | `"Vittoria a Bologna!"` |
| `date` | Data e ora | `2026-03-15 10:00:00 +0200` |
| `category` | Categoria | `"Risultati"` |
| `image` | Percorso immagine | `"/assets/images/vittoria-bologna.webp"` |
| `description` | Frase per Google | `"I Grizzlies vincono a Bologna..."` |
| `og_image` | Uguale a image | `/assets/images/vittoria-bologna.webp` |

### Scrivi il testo

Dopo il blocco `---` finale scrivi il testo della news in Markdown:

```markdown
Testo introduttivo della news.

## Titolo sezione

Altro testo qui...

**Parola in grassetto** e *parola in corsivo*.
```

---

## STEP 3 — Pubblica la news

1. Scorri in basso fino a **"Commit new file"**
2. Nel campo messaggio scrivi: `feat: aggiungi news TITOLO`
3. Lascia selezionato **"Commit directly to the main branch"**
4. Clicca **"Commit new file"**

Il sito si aggiorna automaticamente in 2-3 minuti. 🎉

---

## STEP 4 — Controlla il risultato

Vai su:
```
https://dodgeballravenna.it/news/
```

La tua news dovrebbe apparire in cima alla lista. Le ultime 3 news appaiono anche in **homepage**.

---

## Formattazione Markdown — riferimento rapido

| Vuoi | Scrivi |
|------|--------|
| **Grassetto** | `**testo**` |
| *Corsivo* | `*testo*` |
| Titolo sezione | `## Titolo` |
| Sottotitolo | `### Sottotitolo` |
| Link | `[testo](https://url.it)` |
| Immagine | `![descrizione]({{ site.baseurl }}/assets/images/foto.webp)` |
| Lista puntata | `- voce` |
| Lista numerata | `1. voce` |
| Separatore | `---` |

---

## ❓ Domande frequenti

**La news non appare sul sito**  
Aspetta 2-3 minuti dopo il commit. Se ancora non appare, vai su **Actions → pages build and deployment → Run workflow**.

**Ho fatto un errore nel testo**  
Apri il file in `_posts/` su GitHub → clicca l'icona matita ✏️ → correggi → commit.

**Voglio eliminare una news**  
Apri il file in `_posts/` → clicca i tre puntini `...` → "Delete file" → commit.

**Voglio cambiare l'immagine**  
Carica la nuova immagine in `assets/images/`, poi modifica il campo `image` nel file `.md`.

**La data è sbagliata**  
La data nel *nome del file* determina l'ordine delle news. Per cambiarla devi rinominare il file — elimina quello vecchio e ricrealo con il nome corretto.

---

## 📁 Dove si trovano i file (per riferimento)

```
_posts/
  2026-03-15-vittoria-bologna.md     ← file news
  2026-01-09-benvenuti-sul-sito.md   ← altra news

assets/
  images/
    vittoria-bologna-2026.webp       ← immagini delle news

TEMPLATE-news.md                     ← template da copiare
COME-AGGIUNGERE-NEWS.md             ← questa guida
```

---

*Guida aggiornata a marzo 2026 — Ravenna Grizzlies / Dynamo Grizzly ASD*
