const COMPANY_NAME = 'Alkoriom';

document.title = COMPANY_NAME;
document.querySelectorAll('[data-name]').forEach((el) => {
  el.textContent = COMPANY_NAME;
});

// Scroll reveal

const prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

if (!prefersReducedMotion && 'IntersectionObserver' in window) {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
  );

  document.querySelectorAll('.reveal').forEach((el) => observer.observe(el));
} else {
  document.querySelectorAll('.reveal').forEach((el) => el.classList.add('is-visible'));
}

// Starfield

const canvas = document.getElementById('starfield');

if (canvas) {
  const ctx = canvas.getContext('2d');
  let stars = [];
  let width = 0;
  let height = 0;

  const STAR_COUNT = 260;
  const DRIFT_SPEED = prefersReducedMotion ? 0 : 0.015;

  function resize() {
    width = canvas.width = window.innerWidth;
    height = canvas.height = window.innerHeight;
  }

  function makeStars() {
    stars = Array.from({ length: STAR_COUNT }, () => ({
      x: Math.random() * width,
      y: Math.random() * height,
      r: Math.random() * 1.2 + 0.2,
      a: Math.random() * 0.6 + 0.3,
      speed: Math.random() * 0.4 + 0.2,
    }));
  }

  function draw() {
    ctx.clearRect(0, 0, width, height);
    ctx.fillStyle = '#f5f6f7';

    for (const star of stars) {
      ctx.globalAlpha = star.a;
      ctx.beginPath();
      ctx.arc(star.x, star.y, star.r, 0, Math.PI * 2);
      ctx.fill();

      star.y += DRIFT_SPEED * star.speed;
      if (star.y > height) {
        star.y = 0;
        star.x = Math.random() * width;
      }
    }

    ctx.globalAlpha = 1;
    requestAnimationFrame(draw);
  }

  resize();
  makeStars();
  draw();

  window.addEventListener('resize', () => {
    resize();
    makeStars();
  });
}

// Join form -> mailto

const joinForm = document.getElementById('join-form');

if (joinForm) {
  joinForm.addEventListener('submit', (event) => {
    event.preventDefault();

    const email = document.getElementById('email').value.trim();
    const role = document.getElementById('role').value;

    const subject = `${COMPANY_NAME} — Interest from a ${role || 'contact'}`;
    const body = `Email: ${email}\nRole: ${role}\n\nMessage:\n`;

    const mailtoUrl = `mailto:leandre.rivas@mail.grokbot.com?subject=${encodeURIComponent(
      subject
    )}&body=${encodeURIComponent(body)}`;

    window.location.href = mailtoUrl;
  });
}
