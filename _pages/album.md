---
layout: default
title: "Album Fotografici | Ravenna Grizzlies Dodgeball Ravenna"
description: "Guarda le foto dei Ravenna Grizzlies: partite, allenamenti ed eventi. Il dodgeball di Ravenna in immagini."
keywords: "foto dodgeball Ravenna, album Ravenna Grizzlies, fotografie dodgeball"
permalink: /album/
---

<style>
/* ============================================================
   ALBUM LOBBY — HERO STACK
   ============================================================ */

.album-lobby-header {
  padding: 8rem 0 4rem;
  position: relative;
  border-bottom: 1px solid rgba(123,47,190,.2);
}
.album-lobby-header::before {
  content: '';
  position: absolute;
  inset: 0;
  background: radial-gradient(ellipse at 60% 50%, rgba(123,47,190,.18) 0%, transparent 60%);
  pointer-events: none;
}
.album-lobby-header .container { position: relative; z-index: 1; }
.album-lobby-header h1 {
  font-family: var(--font-display);
  font-size: clamp(3.5rem, 9vw, 7rem);
  line-height: .92;
  letter-spacing: 4px;
  color: var(--white);
  margin: .5rem 0 1rem;
}
.album-lobby-header h1 span {
  color: transparent;
  -webkit-text-stroke: 2px var(--purple-light);
}

/* Back home link */
.album-lobby-back {
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: var(--text-muted);
  text-decoration: none;
  transition: color .2s;
  margin-bottom: 1.5rem;
}
.album-lobby-back:hover { color: var(--purple-light); }
.album-lobby-back svg { width: 14px; height: 14px; }

/* ============================================================
   HERO STACK — un blocco full-width per anno
   ============================================================ */
.album-year-stack {
  display: flex;
  flex-direction: column;
  position: relative;
}

/* Indicatore scroll — appare solo su mobile se ci sono 2+ anni */
.album-scroll-hint {
  display: none;
  position: sticky;
  bottom: 1.2rem;
  left: 0; right: 0;
  z-index: 10;
  justify-content: center;
  pointer-events: none;
}
.album-scroll-hint__pill {
  display: inline-flex;
  align-items: center;
  gap: .5rem;
  background: rgba(8,8,16,.85);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(123,47,190,.4);
  color: var(--purple-light);
  font-size: .72rem;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: .55rem 1.2rem;
  border-radius: 100px;
  box-shadow: 0 4px 20px rgba(0,0,0,.4);
  animation: hintBounce 2s ease-in-out infinite;
}
.album-scroll-hint__pill svg { width: 14px; height: 14px; }
@keyframes hintBounce {
  0%, 100% { transform: translateY(0); }
  50%       { transform: translateY(-5px); }
}

.album-year-hero {
  position: relative;
  width: 100%;
  height: 52vh;
  min-height: 320px;
  max-height: 520px;
  overflow: hidden;
  cursor: pointer;
  display: block;
  text-decoration: none;
  color: inherit;
  border-bottom: 1px solid rgba(123,47,190,.15);
}

/* Foto di sfondo */
.album-year-hero__bg {
  position: absolute;
  inset: 0;
  background-size: cover;
  background-position: center;
  transition: transform .7s cubic-bezier(.4,0,.2,1);
  will-change: transform;
}
.album-year-hero:hover .album-year-hero__bg,
.album-year-hero:focus .album-year-hero__bg {
  transform: scale(1.04);
}

/* Overlay */
.album-year-hero__overlay {
  position: absolute;
  inset: 0;
  background: rgba(8,8,16,.52);
  transition: background .45s ease;
}
.album-year-hero:hover .album-year-hero__overlay,
.album-year-hero:focus .album-year-hero__overlay {
  background: rgba(8,8,16,.80);
}

/* Striscia viola bottom */
.album-year-hero__stripe {
  position: absolute;
  bottom: 0; left: 0; right: 0;
  height: 3px;
  background: linear-gradient(90deg, var(--purple), var(--blue));
  transform: scaleX(0);
  transform-origin: left;
  transition: transform .5s cubic-bezier(.4,0,.2,1);
  z-index: 3;
}
.album-year-hero:hover .album-year-hero__stripe,
.album-year-hero:focus .album-year-hero__stripe {
  transform: scaleX(1);
}

/* Contenuto centrato */
.album-year-hero__content {
  position: absolute;
  inset: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 2rem;
  z-index: 2;
}

/* Anno enorme */
.album-year-hero__year {
  font-family: var(--font-display);
  font-size: clamp(6rem, 18vw, 16rem);
  line-height: 1;
  letter-spacing: 8px;
  color: var(--white);
  text-shadow: 0 4px 60px rgba(0,0,0,.5);
  transition: letter-spacing .5s cubic-bezier(.4,0,.2,1), transform .5s cubic-bezier(.4,0,.2,1);
  will-change: transform;
}
.album-year-hero:hover .album-year-hero__year {
  letter-spacing: 20px;
  transform: scale(.94);
}

/* Contatore eventi */
.album-year-hero__sub {
  font-size: .8rem;
  font-weight: 700;
  letter-spacing: 5px;
  text-transform: uppercase;
  color: var(--purple-light);
  margin-top: 1rem;
  opacity: 0;
  transform: translateY(10px);
  transition: opacity .4s ease .12s, transform .4s ease .12s;
}
.album-year-hero:hover .album-year-hero__sub {
  opacity: 1;
  transform: translateY(0);
}

/* CTA desktop */
.album-year-hero__cta {
  position: absolute;
  bottom: 1.8rem;
  right: 2.2rem;
  display: flex;
  align-items: center;
  gap: .5rem;
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  color: rgba(255,255,255,.45);
  opacity: 0;
  transform: translateX(-10px);
  transition: opacity .35s ease .2s, transform .35s ease .2s, color .2s;
  z-index: 2;
}
.album-year-hero__cta svg { width: 16px; height: 16px; transition: transform .25s; }
.album-year-hero:hover .album-year-hero__cta {
  opacity: 1;
  transform: translateX(0);
  color: var(--purple-light);
}
.album-year-hero:hover .album-year-hero__cta svg { transform: translateX(5px); }

/* CTA mobile — sempre visibile */
.album-year-hero__mobile-cta {
  display: none;
  position: absolute;
  bottom: 1.4rem;
  left: 50%;
  transform: translateX(-50%);
  z-index: 3;
  background: linear-gradient(135deg, var(--purple), var(--blue));
  color: #fff;
  font-size: .75rem;
  font-weight: 700;
  letter-spacing: 2px;
  text-transform: uppercase;
  padding: .6rem 1.4rem;
  border-radius: 100px;
  box-shadow: 0 4px 20px rgba(123,47,190,.4);
  white-space: nowrap;
}

/* Fallback senza foto */
.album-year-hero--no-photo .album-year-hero__bg {
  background:
    radial-gradient(rgba(123,47,190,.2) 1px, transparent 1px),
    linear-gradient(135deg, #1a0535 0%, #0d1535 100%);
  background-size: 28px 28px, 100% 100%;
}

/* Empty state */
.album-lobby-empty {
  padding: 10rem 2rem;
  text-align: center;
  color: var(--text-muted);
}
.album-lobby-empty-icon { font-size: 4rem; display: block; margin-bottom: 1.5rem; opacity: .3; }
.album-lobby-empty h2 {
  font-family: var(--font-display);
  font-size: 2rem;
  color: var(--white);
  margin-bottom: .8rem;
  letter-spacing: 3px;
}
.album-lobby-empty a { color: var(--purple-light); }

/* ============================================================
   MOBILE
   ============================================================ */
@media (max-width: 768px) {
  .album-year-hero {
    height: 45vh;
    min-height: 260px;
    max-height: 380px;
  }

  /* Su mobile mostra sempre anno + sub + bottone */
  .album-year-hero__sub {
    opacity: 1;
    transform: translateY(0);
  }
  .album-year-hero__year {
    font-size: clamp(4.5rem, 22vw, 8rem);
  }

  /* Nascondi CTA desktop, mostra quello mobile */
  .album-year-hero__cta { display: none; }
  .album-year-hero__mobile-cta { display: block; }

  /* Riduci altezza header */
  .album-lobby-header { padding: 7rem 0 3rem; }

  /* Mostra hint scroll se ci sono 2+ anni */
  .album-scroll-hint { display: flex; }
}
</style>

<!-- HEADER PAGINA -->
<header class="album-lobby-header">
  <div class="container">
    <a href="{{ site.baseurl }}/" class="album-lobby-back">
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
           stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M19 12H5M12 19l-7-7 7-7"/>
      </svg>
      Home
    </a>
    <span class="section-tag">Memorie</span>
    <h1>ALBUM<br><span>FOTOGRAFICI</span></h1>
    <div class="divider"></div>
    <p class="page-lead">Partite, allenamenti e momenti fuori dal campo. La storia dei Grizzlies in immagini.</p>
  </div>
</header>

<!-- HERO STACK ANNI -->
{% assign all_albums = site.pages | where: "layout", "album-detail" %}

{% if all_albums.size == 0 %}

<div class="album-lobby-empty">
  <span class="album-lobby-empty-icon">📷</span>
  <h2>IN ARRIVO</h2>
  <p>I primi album arrivano presto.<br>
  Seguici su <a href="{{ site.social.instagram }}" target="_blank" rel="noopener">Instagram</a> per non perdere nulla!</p>
</div>

{% else %}

{% assign anni = all_albums | map: "anno" | uniq | sort: "date" | reverse %}

<div class="album-year-stack" id="yearStack">
  {% for anno in anni %}

    {% assign albums_anno = all_albums | where: "anno", anno | sort: "data" | reverse %}
    {% assign primo_album = albums_anno | first %}

    <a href="{{ site.baseurl }}/album/{{ anno }}/"
       class="album-year-hero{% unless primo_album.cover %} album-year-hero--no-photo{% endunless %}"
       aria-label="Album {{ anno }} — {{ albums_anno.size }} {% if albums_anno.size == 1 %}evento{% else %}eventi{% endif %}">

      <div class="album-year-hero__bg"
        {% if primo_album.cover %}style="background-image: url('{{ primo_album.cover }}')"{% endif %}>
      </div>
      <div class="album-year-hero__overlay"></div>
      <div class="album-year-hero__stripe"></div>

      <div class="album-year-hero__content">
        <span class="album-year-hero__year">{{ anno }}</span>
        <span class="album-year-hero__sub">
          {{ albums_anno.size }} {% if albums_anno.size == 1 %}evento{% else %}eventi{% endif %}
        </span>
      </div>

      <!-- CTA desktop -->
      <span class="album-year-hero__cta" aria-hidden="true">
        Guarda gli album
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
             stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
          <path d="M5 12h14M12 5l7 7-7 7"/>
        </svg>
      </span>

      <!-- CTA mobile — sempre visibile -->
      <span class="album-year-hero__mobile-cta" aria-hidden="true">
        Guarda gli album →
      </span>

    </a>

  {% endfor %}
</div>

<!-- Hint scroll — appare su mobile solo se ci sono 2+ anni -->
{% if anni.size > 1 %}
<div class="album-scroll-hint" id="scrollHint">
  <span class="album-scroll-hint__pill">
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="none"
         stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
      <path d="M12 5v14M5 12l7 7 7-7"/>
    </svg>
    Scorri per altri anni
  </span>
</div>

<script>
(function() {
  var hint = document.getElementById('scrollHint');
  if (!hint) return;
  // Nascondi l'hint dopo che l'utente ha scrollato un po'
  window.addEventListener('scroll', function() {
    if (window.scrollY > 120) {
      hint.style.opacity = '0';
      hint.style.transition = 'opacity .4s';
      hint.style.pointerEvents = 'none';
    } else {
      hint.style.opacity = '1';
    }
  }, { passive: true });
})();
</script>
{% endif %}

{% endif %}
