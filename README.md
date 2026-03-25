# 🐻 Ravenna Grizzlies — Sito Web

Sito ufficiale dei **Ravenna Grizzlies** — Dynamo Grizzly ASD.  
Dodgeball a Ravenna · Serie A Maschile, Femminile e Open · Est. 2024

🌐 **[dodgeballravenna.it](https://dodgeballravenna.it)**

---

## 📋 Indice

- [Come aggiungere una news](#-news)
- [Come aggiungere un album fotografico](#-album-fotografici)
- [Struttura del progetto](#-struttura-del-progetto)
- [Come funziona il sito](#-come-funziona-il-sito)
- [Per gli sviluppatori](#-per-gli-sviluppatori)

---

## 📰 News

Per pubblicare una nuova notizia sul sito leggi la guida completa:

👉 **[COME-AGGIUNGERE-NEWS.md](COME-AGGIUNGERE-NEWS.md)**

Template da copiare: **[TEMPLATE-news.md](TEMPLATE-news.md)**

**In breve:**
1. Carica l'immagine in `assets/images/` (opzionale)
2. Crea un file in `_posts/` con nome `ANNO-MESE-GIORNO-titolo.md`
3. Copia il template, compila i campi, scrivi il testo
4. Commit → il sito si aggiorna in 2-3 minuti

---

## 📸 Album Fotografici

Per aggiungere un nuovo album fotografico leggi la guida completa:

👉 **[COME-AGGIUNGERE-ALBUM.md](COME-AGGIUNGERE-ALBUM.md)**

Template da copiare: **[TEMPLATE-album.md](TEMPLATE-album.md)**

**In breve:**
1. Carica le foto su [Cloudinary](https://cloudinary.com) in una cartella `ANNO/nome-evento`
2. Crea un file in `_pages/` con nome `album-ANNO-MESE-GIORNO-nome.md`
3. Copia il template e compila i campi
4. Commit → vai su **Actions → Sync Cloudinary Photos → Run workflow**
5. Aspetta 2-3 minuti → le foto appaiono sul sito

> ⚠️ Se è il primo album di un anno nuovo (es. 2027), chiedi al responsabile  
> di creare la cartella `album/2027/index.html`

---

## 📁 Struttura del progetto

```
├── _layouts/              # Template HTML delle pagine
│   ├── default.html       # Layout base (navbar + footer)
│   ├── post.html          # Layout per le news
│   ├── album-anno.html    # Layout per la pagina anno album
│   └── album-detail.html  # Layout per il singolo album
│
├── _pages/                # Pagine del sito
│   ├── album.md           # Pagina /album/
│   ├── album-*.md         # Singoli album fotografici
│   ├── squadra.md         # Pagina /squadra/
│   ├── dodgeball.md       # Pagina /dodgeball/
│   └── ...
│
├── _posts/                # News e articoli
│   └── ANNO-MESE-GIORNO-titolo.md
│
├── album/                 # Pagine indice per anno
│   └── 2026/
│       └── index.html
│
├── assets/
│   ├── css/               # Stili CSS
│   ├── images/            # Immagini del sito
│   └── fonts/             # Font locali
│
├── .github/
│   ├── workflows/
│   │   └── sync-cloudinary.yml   # Sync automatico foto
│   └── scripts/
│       └── sync_cloudinary.py    # Script Python sync
│
├── _config.yml            # Configurazione Jekyll
├── TEMPLATE-album.md      # Template per nuovi album
├── TEMPLATE-news.md       # Template per nuove news
├── COME-AGGIUNGERE-ALBUM.md
└── COME-AGGIUNGERE-NEWS.md
```

---

## ⚙️ Come funziona il sito

| Tecnologia | Uso |
|-----------|-----|
| **Jekyll** | Generatore di siti statici |
| **GitHub Pages** | Hosting gratuito |
| **Cloudinary** | Storage e CDN per le foto degli album |
| **GitHub Actions** | Sync automatico foto da Cloudinary ogni notte alle 3:00 |

**Flusso delle foto:**
```
Cloudinary → GitHub Actions (sync notturno) → file .md aggiornato → GitHub Pages → sito
```

**Flusso delle news:**
```
Scrivi .md in _posts/ → commit → GitHub Pages → sito (2-3 min)
```

---

## 🛠 Per gli sviluppatori

### Prerequisiti

- Ruby 3.x
- Bundler

### Avvio locale

```bash
bundle install
bundle exec jekyll serve --watch
```

Il sito sarà disponibile su `http://localhost:4000`

### Deploy

Il deploy è automatico ad ogni push su `main` tramite GitHub Pages.

### Variabili d'ambiente (GitHub Secrets)

| Secret | Descrizione |
|--------|-------------|
| `CLOUDINARY_API_KEY` | API Key Cloudinary |
| `CLOUDINARY_API_SECRET` | API Secret Cloudinary |

### Sync Cloudinary manuale

```
GitHub → Actions → Sync Cloudinary Photos → Run workflow
```

---

## 📬 Contatti

**Dynamo Grizzly ASD**  
📧 [dynamo.grizzly@gmail.com](mailto:dynamo.grizzly@gmail.com)  
📱 [328 947 2121](tel:+393289472121)  
🌐 [dodgeballravenna.it](https://dodgeballravenna.it)

---

*Ravenna Grizzlies · Dynamo Grizzly ASD · Est. 2024*
