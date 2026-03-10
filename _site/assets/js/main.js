/* ============================================
   RAVENNA GRIZZLIES — main.js
   Dynamo Grizzly ASD | dodgeball Ravenna
   ============================================ */

document.addEventListener('DOMContentLoaded', () => {

  // ── 1. NAVBAR: scroll effect + mobile burger ──
  const navbar  = document.getElementById('navbar');
  const burger  = document.getElementById('burger');
  const mobileMenu = document.getElementById('mobileMenu');

  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 40);
  }, { passive: true });

  burger.addEventListener('click', () => {
    mobileMenu.classList.toggle('open');
    // Animate burger spans
    const spans = burger.querySelectorAll('span');
    burger.classList.toggle('active');
    if (burger.classList.contains('active')) {
      spans[0].style.transform = 'translateY(7px) rotate(45deg)';
      spans[1].style.opacity   = '0';
      spans[2].style.transform = 'translateY(-7px) rotate(-45deg)';
    } else {
      spans.forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
    }
  });

  // Close mobile menu on link click
  mobileMenu.querySelectorAll('a').forEach(link => {
    link.addEventListener('click', () => {
      mobileMenu.classList.remove('open');
      burger.classList.remove('active');
      burger.querySelectorAll('span').forEach(s => { s.style.transform = ''; s.style.opacity = ''; });
    });
  });

  // ── 2. HERO: hide scroll indicator on scroll ──
  const scrollIndicator = document.getElementById('scrollIndicator');
  if (scrollIndicator) {
    window.addEventListener('scroll', () => {
      scrollIndicator.style.opacity = window.scrollY > 80 ? '0' : '';
    }, { passive: true });
  }

  // ── 3. PARTICLES in hero ──
  const particlesContainer = document.getElementById('particles');
  if (particlesContainer) {
    const colors = ['#7B2FBE', '#4A6FE3', '#C084FC', '#60A5FA', '#9B59E8'];
    const count  = 28;

    for (let i = 0; i < count; i++) {
      const p = document.createElement('div');
      p.classList.add('particle');

      const size     = Math.random() * 4 + 2;
      const left     = Math.random() * 100;
      const delay    = Math.random() * 8;
      const duration = Math.random() * 8 + 6;
      const color    = colors[Math.floor(Math.random() * colors.length)];
      const bottom   = Math.random() * 40;

      p.style.cssText = `
        width: ${size}px;
        height: ${size}px;
        left: ${left}%;
        bottom: ${bottom}%;
        background: ${color};
        animation-duration: ${duration}s;
        animation-delay: ${delay}s;
      `;
      particlesContainer.appendChild(p);
    }
  }

  // ── 4. SCROLL REVEAL ──
  const revealEls = document.querySelectorAll('[data-reveal]');

  const revealObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('revealed');
        revealObserver.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });

  revealEls.forEach(el => revealObserver.observe(el));

  // ── 5. STATS BAR: build from data attributes ──
  document.querySelectorAll('.stat').forEach(stat => {
    const count  = stat.dataset.count;
    const suffix = stat.dataset.suffix || '';
    const label  = stat.dataset.label  || '';
    const emoji  = stat.dataset.emoji;

    if (emoji) {
      stat.innerHTML = `
        <span class="stat-number">${emoji}</span>
        <span class="stat-label">${label}</span>
      `;
    } else if (count) {
      stat.innerHTML = `
        <span class="stat-number" data-target="${count}" data-suffix="${suffix}">0${suffix}</span>
        <span class="stat-label">${label}</span>
      `;
    }
  });

  // ── 6. COUNT-UP animation for stats ──
  const statsBar = document.querySelector('.stats-bar');
  if (statsBar) {
    const countObserver = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        document.querySelectorAll('[data-target]').forEach(el => {
          const target = parseInt(el.dataset.target);
          const suffix = el.dataset.suffix || '';
          const duration = 1200;
          const startTime = performance.now();

          function update(now) {
            const elapsed  = now - startTime;
            const progress = Math.min(elapsed / duration, 1);
            // Ease out cubic
            const eased    = 1 - Math.pow(1 - progress, 3);
            el.textContent = Math.round(target * eased) + suffix;
            if (progress < 1) requestAnimationFrame(update);
          }

          requestAnimationFrame(update);
        });
        countObserver.disconnect();
      }
    }, { threshold: 0.5 });

    countObserver.observe(statsBar);
  }

  // ── 7. SMOOTH active nav link on scroll ──
  const sections = document.querySelectorAll('section[id], div[id]');
  const navLinks = document.querySelectorAll('.nav-links a');

  const sectionObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const id = entry.target.getAttribute('id');
        navLinks.forEach(link => {
          link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
        });
      }
    });
  }, { threshold: 0.4 });

  sections.forEach(s => sectionObserver.observe(s));

  // ── 8. CAROSELLO GALLERIA ──
  const track  = document.getElementById('carouselTrack');
  const dotsEl = document.getElementById('carouselDots');
  const btnPrev = document.getElementById('carouselPrev');
  const btnNext = document.getElementById('carouselNext');

  if (track) {
    const slides = [...track.querySelectorAll('.carousel-slide')];
    const total  = slides.length;
    let current  = 0;
    let isAnimating = false;

    // Crea dots
    slides.forEach((_, i) => {
      const dot = document.createElement('button');
      dot.className = 'carousel-dot' + (i === 0 ? ' active' : '');
      dot.setAttribute('aria-label', `Foto ${i + 1}`);
      dot.addEventListener('click', () => goTo(i));
      dotsEl.appendChild(dot);
    });

    const dots = [...dotsEl.querySelectorAll('.carousel-dot')];

    function getClass(i) {
      const diff = ((i - current) % total + total) % total;
      if (diff === 0)                    return 'active';
      if (diff === 1)                    return 'next';
      if (diff === total - 1)            return 'prev';
      if (diff === 2)                    return 'far-next';
      if (diff === total - 2)            return 'far-prev';
      return 'hidden';
    }

    function loadImage(slide) {
      const img = slide.querySelector('img[data-src]');
      if (img) {
        img.src = img.dataset.src;
        img.removeAttribute('data-src');
      }
    }

    function updateSlides() {
      slides.forEach((slide, i) => {
        const cls = getClass(i);
        slide.className = 'carousel-slide ' + cls;
        // Carica subito le slide visibili o adiacenti
        if (['active', 'prev', 'next'].includes(cls)) {
          loadImage(slide);
        }
      });
      dots.forEach((dot, i) => {
        dot.classList.toggle('active', i === current);
      });
    }

    function goTo(index) {
      if (isAnimating) return;
      isAnimating = true;
      current = ((index % total) + total) % total;
      updateSlides();
      setTimeout(() => { isAnimating = false; }, 550);
    }

    function next() { goTo(current + 1); }
    function prev() { goTo(current - 1); }

    btnNext.addEventListener('click', next);
    btnPrev.addEventListener('click', prev);

    // Click su prev/next slide per navigare
    slides.forEach((slide, i) => {
      slide.addEventListener('click', () => {
        const cls = slide.className;
        if (cls.includes('next') || cls.includes('far-next')) next();
        if (cls.includes('prev') || cls.includes('far-prev')) prev();
      });
    });

    // Tastiera
    document.addEventListener('keydown', e => {
      if (e.key === 'ArrowLeft')  prev();
      if (e.key === 'ArrowRight') next();
    });

    // Touch swipe
    let touchStartX = 0;
    track.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, { passive: true });
    track.addEventListener('touchend',   e => {
      const diff = touchStartX - e.changedTouches[0].clientX;
      if (Math.abs(diff) > 50) diff > 0 ? next() : prev();
    });

    // Init — carica solo quando la sezione è visibile
    const carouselSection = document.getElementById('galleria');
    const carouselObserver = new IntersectionObserver((entries) => {
      if (entries[0].isIntersecting) {
        updateSlides();
        carouselObserver.disconnect();
      }
    }, { threshold: 0.1 });

    if (carouselSection) carouselObserver.observe(carouselSection);
    else updateSlides();
  }

  // ── FAQ ACCORDION ──
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.faq-item');
      const isOpen = item.classList.contains('open');
      // Chiudi tutte
      document.querySelectorAll('.faq-item.open').forEach(el => el.classList.remove('open'));
      // Apri quella cliccata (se era chiusa)
      if (!isOpen) item.classList.add('open');
      btn.setAttribute('aria-expanded', !isOpen);
    });
  });

});

// ============================================================
// SECTION SIDEBAR — aggiorna pallino attivo allo scroll
// ============================================================
(function() {
  const sidebar = document.getElementById('sectionSidebar');
  if (!sidebar) return;

  const dots = sidebar.querySelectorAll('.sidebar-dot');
  const sections = Array.from(dots).map(d => document.getElementById(d.dataset.section)).filter(Boolean);

  function updateActive() {
    const scrollY = window.scrollY + window.innerHeight * 0.4;
    let current = sections[0];
    for (const section of sections) {
      if (section.offsetTop <= scrollY) current = section;
    }
    dots.forEach(d => {
      d.classList.toggle('active', d.dataset.section === current.id);
    });
  }

  window.addEventListener('scroll', updateActive, { passive: true });
  updateActive();
})();

// ============================================================
// MOBILE PROGRESS BAR — aggiorna mentre si scrolla
// ============================================================
(function() {
  const bar = document.getElementById('mobileProgressBar');
  if (!bar) return;

  function updateProgress() {
    const scrollTop = window.scrollY;
    const docHeight = document.documentElement.scrollHeight - window.innerHeight;
    const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
    bar.style.width = pct + '%';
  }

  window.addEventListener('scroll', updateProgress, { passive: true });
  updateProgress();
})();