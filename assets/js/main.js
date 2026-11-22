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
    const imgs = [...roll.querySelectorAll('.roll__frame img, .roll__frame video')];
    const dotsWrap = roll.querySelector('.roll__dots');
    const capEl = roll.querySelector('[data-roll-cap]');
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
        if (img.tagName === 'VIDEO') {
          // A clip in a postcard: load it the first time it comes up, play it through, then move on
          if (j === cur && !reduceMotion) {
            if (img.dataset.src) { img.src = img.dataset.src; img.removeAttribute('data-src'); }
            img.currentTime = 0;
            img.play().catch(() => {});
          } else { img.pause(); }
        } else if (j === cur) { img.loading = 'eager'; }
      });
      dots.forEach((d, j) => d.setAttribute('aria-current', String(j === cur)));
      if (capEl && imgs[cur].dataset.cap) capEl.textContent = imgs[cur].dataset.cap;
    };
    // In a pile only the front card moves; when it runs out of images the pile may bring the next draft forward
    const asleep = () => roll.classList.contains('pile__card') && !roll.classList.contains('is-front');
    const tick = () => {
      if (paused || !visible || document.hidden || asleep()) return;
      const v = imgs[cur];
      if (v.tagName === 'VIDEO' && !v.paused && !v.ended) return; // let the clip finish first
      const next = (cur + 1) % imgs.length;
      if (next === 0 && !roll.dispatchEvent(new CustomEvent('roll:wrap', { bubbles: true, cancelable: true }))) return;
      show(next);
    };
    const restart = () => { clearInterval(timer); if (!reduceMotion) timer = setInterval(tick, 3800); };
    // Clicking the frame opens the current screenshot in the lightbox (hidden [data-lb] items, same order)
    const frame = roll.querySelector('.roll__frame');
    const lbItems = roll.querySelectorAll('[data-lb]');
    if (frame.tagName === 'BUTTON' && lbItems.length) frame.addEventListener('click', () => lbItems[cur]?.click());
    roll.addEventListener('roll:reset', () => { show(0); restart(); });
    imgs.forEach((v) => { if (v.tagName === 'VIDEO') v.addEventListener('ended', () => { if (!paused) { tick(); restart(); } }); });
    roll.addEventListener('mouseenter', () => { paused = true; });
    roll.addEventListener('mouseleave', () => { paused = false; });
    roll.addEventListener('focusin', () => { paused = true; });
    roll.addEventListener('focusout', () => { paused = false; });
    if ('IntersectionObserver' in window) {
      new IntersectionObserver(([en]) => { visible = en.isIntersecting; }).observe(roll);
    }
    show(0);
    // data-roll-offset staggers postcards that sit side by side so they don't all change at once
    setTimeout(restart, Number(roll.dataset.rollOffset) || 0);
  });

  // Stacked pile of postcards (one per draft): the tags or a click on a card behind bring that card to the front.
  // The front card rotates its own images; when it has shown them all, the next draft comes forward.
  document.querySelectorAll('[data-pile]').forEach((pile) => {
    const cards = [...pile.querySelectorAll('.pile__card')];
    const depth = ['is-front', 'is-mid', 'is-back'];
    // Story order for auto-advance: sketch, blockout, final, then round again
    const story = ['sketch', 'blockout', 'final'].map((k) => pile.querySelector(`.pile__card--${k}`)).filter(Boolean);
    let stack = depth.map((d) => pile.querySelector(`.pile__card.${d}`)).filter(Boolean);
    const sync = () => {
      stack.forEach((c, i) => {
        c.classList.remove(...depth);
        c.classList.add(depth[i] || 'is-back');
        const front = i === 0;
        c.querySelectorAll('.roll__frame, .roll__dots button').forEach((b) => { b.tabIndex = front ? 0 : -1; });
        const tab = pile.querySelector(`.pile__tabs [data-for="${c.className.match(/pile__card--(\w+)/)[1]}"]`);
        if (tab) tab.setAttribute('aria-pressed', String(front));
      });
    };
    const toFront = (card) => {
      if (stack[0] === card) return;
      stack = [card, ...stack.filter((c) => c !== card)];
      sync();
      card.dispatchEvent(new CustomEvent('roll:reset'));
    };
    cards.forEach((card) => {
      // A click anywhere on a card behind brings it forward instead of opening the lightbox
      card.addEventListener('click', (e) => {
        if (card === stack[0]) return;
        e.preventDefault(); e.stopImmediatePropagation();
        toFront(card);
      }, true);
    });
    pile.querySelectorAll('.pile__tabs [data-for]').forEach((tab) => {
      tab.addEventListener('click', () => toFront(pile.querySelector(`.pile__card--${tab.dataset.for}`)));
    });
    pile.addEventListener('roll:wrap', (e) => {
      e.preventDefault();
      toFront(story[(story.indexOf(e.target) + 1) % story.length]);
    });
    sync();
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
