(() => {
  const reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  document.querySelectorAll('.year').forEach((el) => { el.textContent = new Date().getFullYear(); });

  // Header border once the page scrolls
  const top = document.querySelector('.top');
  if (top) {
    const onScroll = () => top.classList.toggle('is-scrolled', window.scrollY > 8);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  // Videos: load only when on screen, pause when off screen, never autoplay with reduced motion
  const videos = document.querySelectorAll('video[data-autoplay]');
  if (!reduceMotion && 'IntersectionObserver' in window) {
    const vo = new IntersectionObserver((entries) => {
      entries.forEach(({ target: v, isIntersecting }) => {
        if (isIntersecting) {
          const s = v.querySelector('source[data-src]');
          if (s) { s.src = s.dataset.src; s.removeAttribute('data-src'); v.load(); }
          v.play().catch(() => {});
        } else { v.pause(); }
      });
    }, { threshold: 0.25 });
    videos.forEach((v) => vo.observe(v));
  }

  // Rolling postcards: cross-fade every few seconds; pause on hover/focus, off screen or in a hidden tab.
  // With reduced motion it never advances by itself, but the dots still work.
  document.querySelectorAll('[data-roll]').forEach((roll) => {
    const imgs = [...roll.querySelectorAll('.roll__frame img')];
    const dotsWrap = roll.querySelector('.roll__dots');
    if (imgs.length < 2) return;
    let cur = 0, timer = null, paused = false, visible = true;
    const dots = imgs.map((img, i) => {
      const b = document.createElement('button');
      b.type = 'button';
      b.setAttribute('aria-label', `Screenshot ${i + 1} of ${imgs.length}`);
      b.addEventListener('click', () => { show(i); restart(); });
      dotsWrap.append(b);
      return b;
    });
    const show = (i) => {
      cur = (i + imgs.length) % imgs.length;
      imgs.forEach((img, j) => {
        img.classList.toggle('is-on', j === cur);
        if (j === cur) img.loading = 'eager';
      });
      dots.forEach((d, j) => d.setAttribute('aria-current', String(j === cur)));
    };
    const tick = () => { if (!paused && visible && !document.hidden) show(cur + 1); };
    const restart = () => { clearInterval(timer); if (!reduceMotion) timer = setInterval(tick, 3800); };
    // Clicking the frame opens the current screenshot in the lightbox (hidden [data-lb] items, same order)
    const frame = roll.querySelector('.roll__frame');
    const lbItems = roll.querySelectorAll('[data-lb]');
    if (frame.tagName === 'BUTTON' && lbItems.length) frame.addEventListener('click', () => lbItems[cur]?.click());
    roll.addEventListener('mouseenter', () => { paused = true; });
    roll.addEventListener('mouseleave', () => { paused = false; });
    roll.addEventListener('focusin', () => { paused = true; });
    roll.addEventListener('focusout', () => { paused = false; });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([en]) => { visible = en.isIntersecting; }).observe(roll);
    }
    show(0);
    restart();
  });

  // Lightbox: any element with data-lb="group" and data-src opens; groups are built from the page
  const box = document.querySelector('.lightbox');
  if (!box) return;
  const stage = box.querySelector('.lightbox__stage');
  const triggers = [...document.querySelectorAll('[data-lb]')];
  const groups = {};
  triggers.forEach((t) => { (groups[t.dataset.lb] ||= []).push(t); });
  let items = [], idx = 0, opener = null;

  const render = () => {
    const t = items[idx];
    stage.innerHTML = '';
    let el;
    if (t.dataset.type === 'video') {
      el = document.createElement('video');
      Object.assign(el, { src: t.dataset.src, controls: true, loop: true, muted: true, playsInline: true, autoplay: !reduceMotion });
    } else {
      el = document.createElement('img');
      el.src = t.dataset.src;
      el.alt = t.dataset.caption || '';
    }
    const cap = document.createElement('figcaption');
    cap.textContent = (t.dataset.caption || '') + (items.length > 1 ? `  (${idx + 1}/${items.length})` : '');
    stage.append(el, cap);
  };
  const step = (d) => { idx = (idx + d + items.length) % items.length; render(); };

  triggers.forEach((t) => t.addEventListener('click', (e) => {
    e.preventDefault();
    items = groups[t.dataset.lb]; idx = items.indexOf(t); opener = t;
    box.classList.toggle('single', items.length < 2);
    render();
    box.showModal();
  }));
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
    if (Math.abs(dx) > 50 && items.length > 1) step(dx < 0 ? 1 : -1);
    touchX = null;
  });
  box.addEventListener('close', () => { stage.innerHTML = ''; if (opener) opener.focus(); });
})();
