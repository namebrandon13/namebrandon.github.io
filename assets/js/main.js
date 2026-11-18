(() => {
  document.documentElement.classList.add('js');
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const year = document.getElementById('year');
  if (year) year.textContent = new Date().getFullYear();

  // Nav: shadow on scroll + mobile toggle
  const nav = document.querySelector('.nav');
  const onScroll = () => nav.classList.toggle('is-scrolled', window.scrollY > 8);
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  const toggle = document.querySelector('.nav__toggle');
  const links = document.getElementById('nav-links');
  const setMenu = (open) => {
    toggle.setAttribute('aria-expanded', String(open));
    toggle.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    links.classList.toggle('is-open', open);
  };
  toggle.addEventListener('click', () => setMenu(toggle.getAttribute('aria-expanded') !== 'true'));
  links.addEventListener('click', (e) => { if (e.target.closest('a')) setMenu(false); });

  // Reveal on scroll
  const revealEls = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window && !reduceMotion) {
    const io = new IntersectionObserver((entries) => {
      entries.forEach((en) => { if (en.isIntersecting) { en.target.classList.add('is-in'); io.unobserve(en.target); } });
    }, { rootMargin: '0px 0px -8% 0px' });
    revealEls.forEach((el) => io.observe(el));
  } else {
    revealEls.forEach((el) => el.classList.add('is-in'));
  }

  // Lazy autoplay videos: load only when on screen, pause when off screen
  const loadVideo = (v) => {
    const s = v.querySelector('source[data-src]');
    if (s) { s.src = s.dataset.src; s.removeAttribute('data-src'); v.load(); }
  };
  const videos = document.querySelectorAll('video.autoplay');
  if (!reduceMotion && 'IntersectionObserver' in window) {
    const vo = new IntersectionObserver((entries) => {
      entries.forEach(({ target: v, isIntersecting }) => {
        if (isIntersecting) { loadVideo(v); v.play().catch(() => {}); } else { v.pause(); }
      });
    }, { threshold: 0.25 });
    videos.forEach((v) => vo.observe(v));
  }

  // Lightbox
  const galleries = {
    coach: [
      ['assets/img/coach1.webp', 'Coach Number 11: sleeper coach interior'],
      ['assets/img/coach2.webp', 'Coach Number 11: coach doorway'],
      ['assets/img/coach3.webp', 'Coach Number 11: aisle view'],
    ],
    cosmic: [
      ['assets/img/cosmic1.webp', 'Cosmic Chaos: gameplay'],
      ['assets/img/cosmic2.webp', 'Cosmic Chaos: gameplay'],
      ['assets/img/cosmic3.webp', 'Cosmic Chaos: pause menu'],
    ],
    oml: [['assets/img/oml.webp', 'One More Lesson: cover art']],
    art: [
      ['assets/img/mall_08.webp', 'Supermarket interior'],
      ['assets/img/f1_11.webp', 'Sports car on a wet track'],
      ['assets/img/upwork_desktop.webp', 'Gaming desk setup'],
      ['assets/video/loop_sound.mp4', 'Mechanical hand animation', 'video'],
      ['assets/img/upwork_jeep.webp', 'Off-road jeep'],
      ['assets/img/upwork_room.webp', 'Living room interior'],
      ['assets/img/upwork_laptop.webp', 'Laptop scene'],
      ['assets/img/13.webp', 'Gaming laptop close-up'],
      ['assets/img/upwork_packaging.webp', 'Product packaging'],
    ],
  };

  const box = document.querySelector('.lightbox');
  const stage = box.querySelector('.lightbox__stage');
  let current = null, idx = 0, opener = null;

  const render = () => {
    const [src, caption, type] = current[idx];
    stage.innerHTML = '';
    let el;
    if (type === 'video') {
      el = document.createElement('video');
      Object.assign(el, { src, controls: true, loop: true, muted: true, playsInline: true, autoplay: !reduceMotion });
    } else {
      el = document.createElement('img');
      el.src = src; el.alt = caption;
    }
    const cap = document.createElement('figcaption');
    cap.textContent = current.length > 1 ? `${caption} (${idx + 1}/${current.length})` : caption;
    stage.append(el, cap);
  };
  const open = (key, i, from) => {
    current = galleries[key]; idx = i || 0; opener = from;
    box.classList.toggle('single', current.length < 2);
    render();
    box.showModal();
  };
  const step = (d) => { idx = (idx + d + current.length) % current.length; render(); };

  document.querySelectorAll('[data-gallery]').forEach((b) => b.addEventListener('click', () => open(b.dataset.gallery, 0, b)));
  document.querySelectorAll('[data-gallery-root] [data-index]').forEach((b) => {
    b.addEventListener('click', () => open(b.closest('[data-gallery-root]').dataset.galleryRoot, +b.dataset.index, b));
  });
  box.querySelector('.lightbox__close').addEventListener('click', () => box.close());
  box.querySelector('.lightbox__prev').addEventListener('click', () => step(-1));
  box.querySelector('.lightbox__next').addEventListener('click', () => step(1));
  box.addEventListener('click', (e) => { if (e.target === box || e.target === stage) box.close(); });
  box.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowRight') step(1);
    if (e.key === 'ArrowLeft') step(-1);
  });
  let touchX = null;
  box.addEventListener('touchstart', (e) => { touchX = e.touches[0].clientX; }, { passive: true });
  box.addEventListener('touchend', (e) => {
    if (touchX === null) return;
    const dx = e.changedTouches[0].clientX - touchX;
    if (Math.abs(dx) > 50 && current.length > 1) step(dx < 0 ? 1 : -1);
    touchX = null;
  });
  box.addEventListener('close', () => { stage.innerHTML = ''; if (opener) opener.focus(); });
})();
