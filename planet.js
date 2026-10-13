import * as THREE from './vendor/three.module.min.js';

const host = document.getElementById('planet');
const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

function webglOK() {
  try { const c = document.createElement('canvas'); return !!(c.getContext('webgl2') || c.getContext('webgl')); }
  catch (e) { return false; }
}

if (host && webglOK()) {
  const mobile = window.matchMedia('(max-width: 760px)').matches;
  const renderer = new THREE.WebGLRenderer({ antialias: !mobile, alpha: true, powerPreference: 'low-power' });
  renderer.setPixelRatio(Math.min(window.devicePixelRatio, mobile ? 1.5 : 2));
  host.appendChild(renderer.domElement);
  host.classList.add('has-3d');

  const scene = new THREE.Scene();
  const camera = new THREE.PerspectiveCamera(32, 1, 0.1, 100);
  camera.position.set(0, 0, mobile ? 14 : 10.5);

  // Procedural monochrome surface texture (value noise, no network)
  const W = mobile ? 512 : 1024, H = W / 2;
  const cv = document.createElement('canvas'); cv.width = W; cv.height = H;
  const ctx = cv.getContext('2d');
  const img = ctx.createImageData(W, H);
  const rnd = (x, y) => { const s = Math.sin(x * 127.1 + y * 311.7) * 43758.5453; return s - Math.floor(s); };
  const sm = t => t * t * (3 - 2 * t);
  function noise(x, y, per) {
    const xi = Math.floor(x), yi = Math.floor(y), xf = x - xi, yf = y - yi;
    const w = k => ((k % per) + per) % per;
    const a = rnd(w(xi), yi), b = rnd(w(xi + 1), yi), c = rnd(w(xi), yi + 1), d = rnd(w(xi + 1), yi + 1);
    const u = sm(xf), v = sm(yf);
    return a + (b - a) * u + (c - a) * v + (a - b - c + d) * u * v;
  }
  for (let y = 0; y < H; y++) for (let x = 0; x < W; x++) {
    let f = 0, amp = 0.5, fr = 4;
    for (let o = 0; o < 6; o++) { f += amp * noise(x / W * fr, y / H * fr / 2, fr); amp *= 0.5; fr *= 2; }
    const band = 0.06 * Math.sin(y / H * Math.PI * 14 + f * 6);
    let v = Math.max(0, Math.min(1, (f - 0.35) * 1.6 + band));
    v = 18 + v * 150;
    const i = (y * W + x) * 4; img.data[i] = img.data[i + 1] = img.data[i + 2] = v; img.data[i + 3] = 255;
  }
  ctx.putImageData(img, 0, 0);
  const tex = new THREE.CanvasTexture(cv);
  tex.colorSpace = THREE.SRGBColorSpace;
  tex.wrapS = THREE.RepeatWrapping;

  const seg = mobile ? 64 : 128;
  const planet = new THREE.Mesh(
    new THREE.SphereGeometry(2, seg, seg / 2),
    new THREE.MeshStandardMaterial({ map: tex, roughness: 0.95, metalness: 0 })
  );
  planet.rotation.z = 0.25;
  scene.add(planet);

  // Atmosphere: fresnel glow (back side, additive)
  const atmo = new THREE.Mesh(
    new THREE.SphereGeometry(2.25, seg, seg / 2),
    new THREE.ShaderMaterial({
      side: THREE.BackSide, transparent: true, blending: THREE.AdditiveBlending, depthWrite: false,
      uniforms: { uColor: { value: new THREE.Color(0xB89878) } },
      vertexShader: `varying vec3 vN; varying vec3 vP;
        void main(){ vN = normalize(normalMatrix*normal); vec4 mv = modelViewMatrix*vec4(position,1.0); vP = mv.xyz; gl_Position = projectionMatrix*mv; }`,
      fragmentShader: `uniform vec3 uColor; varying vec3 vN; varying vec3 vP;
        void main(){ float d = dot(vN, normalize(-vP)); float i = pow(clamp(-d / 0.43, 0.0, 1.0), 2.6) * 0.55; gl_FragColor = vec4(uColor, 1.0) * i; }`
    })
  );
  scene.add(atmo);
  // Inner rim on the lit limb
  const rim = new THREE.Mesh(
    new THREE.SphereGeometry(2.01, seg, seg / 2),
    new THREE.ShaderMaterial({
      transparent: true, blending: THREE.AdditiveBlending, depthWrite: false,
      vertexShader: `varying vec3 vN; varying vec3 vP;
        void main(){ vN = normalize(normalMatrix*normal); vec4 mv = modelViewMatrix*vec4(position,1.0); vP = mv.xyz; gl_Position = projectionMatrix*mv; }`,
      fragmentShader: `varying vec3 vN; varying vec3 vP;
        void main(){ float f = pow(1.0 - max(0.0, dot(vN, normalize(-vP))), 3.0); gl_FragColor = vec4(vec3(1.0,0.82,0.62)*f*0.4, 1.0); }`
    })
  );
  scene.add(rim);

  const sun = new THREE.DirectionalLight(0xfff1dd, 3.0);
  sun.position.set(-4, 3, 2.5);
  scene.add(sun, new THREE.AmbientLight(0xffffff, 0.04));

  function resize() {
    const w = host.clientWidth, h = host.clientHeight;
    renderer.setSize(w, h, false);
    camera.aspect = w / h; camera.updateProjectionMatrix();
  }
  resize();
  window.addEventListener('resize', resize);

  let visible = true;
  new IntersectionObserver(([e]) => { visible = e.isIntersecting; }).observe(host);
  const clock = new THREE.Clock();
  (function loop() {
    requestAnimationFrame(loop);
    if (!visible) return;
    const dt = clock.getDelta();
    if (!reduced) planet.rotation.y += dt * 0.05;
    renderer.render(scene, camera);
  })();
}
