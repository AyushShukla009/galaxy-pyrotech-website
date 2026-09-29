# JavaScript engine module for Galaxy Pyrotech Traders
def get_javascript():
    return '''
  <script>
    (function () {
      'use strict';

      /* ======================================================================
         1. SITE CONFIG & DATA
         ====================================================================== */
      var SITE = {
        phone: '+919582673570',
        phoneDisplay: '+91 95826 73570',
        whatsapp: '919582673570',
        email: 'galaxypyrotech@gmail.com',
        address: '12, Amaltash Marg, Chaura Raghunathpur, Sector 22, Noida, Uttar Pradesh 201307',
        instagram: 'https://www.instagram.com/galaxypyrotechtraders'
      };

      var GALLERY_DATA = [
        {
          src: 'assets/varmala_stage.jpg',
          title: 'Palace Varmala Exchange',
          desc: 'Synchronized cold pyro spark fountains and heavy dry ice low fog clouds on the royal stage.',
          category: 'varmala',
          venue: 'Grand Heritage Banquet, Noida'
        },
        {
          src: 'assets/wedding_entry.jpg',
          title: 'Candlelit Aisle Walk',
          desc: 'Bridal entry framed by 100% smokeless, non-hazardous golden cold pyro fountains.',
          category: 'entry',
          venue: 'Saffron Lawn & Farmhouse, Greater Noida'
        },
        {
          src: 'assets/low_fog.jpg',
          title: 'Dancing On The Clouds',
          desc: 'High-density pure dry ice low fog keeping the clouds strictly bounded to the floor.',
          category: 'fog',
          venue: 'Luxury Ballroom, South Delhi'
        },
        {
          src: 'assets/sparkular_stage.jpg',
          title: 'Sparkular Waterfall Curtain',
          desc: 'DMX-controlled electronic cold spark waterfall curtain framing a celebration stage.',
          category: 'sparkular',
          venue: 'Corporate Gala Celebration, Noida'
        },
        {
          src: 'assets/sky_fireworks.jpg',
          title: 'Royal Heritage Sky Shells',
          desc: 'High-altitude panoramic aerial fireworks shells detonating across the night sky.',
          category: 'fireworks',
          venue: 'Destination Palace, Rajasthan'
        },
        {
          src: 'assets/colour_smoke.jpg',
          title: 'Vibrant Baraat & Haldi Plumes',
          desc: 'Organic, non-toxic daytime colour smoke bomb plumes for daytime wedding arrivals.',
          category: 'smoke',
          venue: 'Open Farmhouse Lawn, Sector 22 Noida'
        }
      ];

      var DEFAULT_REVIEWS = [
        {
          name: 'Rohit & Sneha Verma',
          event: 'Wedding at Saffron Banquet, Noida',
          rating: 5,
          text: 'Galaxy Pyrotech made our varmala entry in Noida unforgettable. The cold pyro spark fountains and dry ice clouds were timed down to the exact second of our song. Zero smoke, completely safe, and our guests were stunned!',
          date: 'Verified Client'
        },
        {
          name: 'Karan Singhania',
          event: 'Destination Wedding Planner, Delhi NCR',
          rating: 5,
          text: 'Extremely professional team. We booked sparkular machines and color smoke for our daytime Mehendi in Greater Noida. The crew was polite, arrived well in advance, and coordinated seamlessly with the decorators.',
          date: 'Verified Event Planner'
        },
        {
          name: 'Ananya Sharma',
          event: 'Grand Reception, Sector 22 Noida',
          rating: 5,
          text: 'We called at 11 PM for an urgent reception requirement the following day. Galaxy Pyrotech responded immediately, gave a fair quotation on WhatsApp, and delivered a 10/10 show. Genuine 24/7 service!',
          date: 'Verified Client'
        }
      ];

      /* Helper query functions */
      var $ = function (sel, root) { return (root || document).querySelector(sel); };
      var $$ = function (sel, root) { return Array.prototype.slice.call((root || document).querySelectorAll(sel)); };

      /* ======================================================================
         2. WEB AUDIO API SYNTHESIZER (SOUND FX ENGINE)
         ====================================================================== */
      var soundEnabled = localStorage.getItem('gp_sfx') !== 'off';
      var audioCtx = null;

      function getAudioContext() {
        if (!audioCtx && (window.AudioContext || window.webkitAudioContext)) {
          var AudioCtxClass = window.AudioContext || window.webkitAudioContext;
          audioCtx = new AudioCtxClass();
        }
        if (audioCtx && audioCtx.state === 'suspended') {
          audioCtx.resume();
        }
        return audioCtx;
      }

      function updateSoundUI() {
        var labels = $$('.sound-label, #sim-sound-label');
        labels.forEach(function (el) {
          el.textContent = soundEnabled ? 'SFX: ON' : 'SFX: OFF';
        });
        var btns = $$('#global-sound-toggle, #sim-sound-btn');
        btns.forEach(function (b) {
          b.classList.toggle('is-active', soundEnabled);
          var use = b.querySelector('use');
          if (use) {
            use.setAttribute('href', soundEnabled ? '#i-sound' : '#i-mute');
          }
        });
      }

      function toggleSound() {
        soundEnabled = !soundEnabled;
        localStorage.setItem('gp_sfx', soundEnabled ? 'on' : 'off');
        updateSoundUI();
        if (soundEnabled) {
          playSparkleChime();
        }
      }

      function playSparkleChime() {
        if (!soundEnabled) return;
        var ctx = getAudioContext();
        if (!ctx) return;
        var now = ctx.currentTime;
        var freqs = [587.33, 880, 1174.66, 1760]; // D chord harmonics
        freqs.forEach(function (f, i) {
          var osc = ctx.createOscillator();
          var gain = ctx.createGain();
          osc.type = 'sine';
          osc.frequency.setValueAtTime(f, now + i * 0.04);
          gain.gain.setValueAtTime(0.04, now + i * 0.04);
          gain.gain.exponentialRampToValueAtTime(0.0001, now + i * 0.04 + 0.35);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + i * 0.04);
          osc.stop(now + i * 0.04 + 0.4);
        });
      }

      function playPyroWhoosh() {
        if (!soundEnabled) return;
        var ctx = getAudioContext();
        if (!ctx) return;
        var bufferSize = ctx.sampleRate * 0.4;
        var buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
        var data = buffer.getChannelData(0);
        for (var i = 0; i < bufferSize; i++) {
          data[i] = Math.random() * 2 - 1;
        }
        var noise = ctx.createBufferSource();
        noise.buffer = buffer;

        var filter = ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(350, ctx.currentTime);
        filter.frequency.exponentialRampToValueAtTime(1400, ctx.currentTime + 0.3);
        filter.Q.setValueAtTime(2, ctx.currentTime);

        var gain = ctx.createGain();
        gain.gain.setValueAtTime(0.12, ctx.currentTime);
        gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.4);

        noise.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);
        noise.start();
      }

      function playConfettiPop() {
        if (!soundEnabled) return;
        var ctx = getAudioContext();
        if (!ctx) return;
        var now = ctx.currentTime;
        var osc = ctx.createOscillator();
        var gain = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(220, now);
        osc.frequency.exponentialRampToValueAtTime(60, now + 0.15);
        gain.gain.setValueAtTime(0.2, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.16);
      }

      function playFanfare() {
        if (!soundEnabled) return;
        var ctx = getAudioContext();
        if (!ctx) return;
        var now = ctx.currentTime;
        var notes = [440, 554.37, 659.25, 880];
        notes.forEach(function (n, i) {
          var osc = ctx.createOscillator();
          var gain = ctx.createGain();
          osc.type = 'triangle';
          osc.frequency.setValueAtTime(n, now + i * 0.08);
          gain.gain.setValueAtTime(0.08, now + i * 0.08);
          gain.gain.exponentialRampToValueAtTime(0.001, now + i * 0.08 + 0.5);
          osc.connect(gain);
          gain.connect(ctx.destination);
          osc.start(now + i * 0.08);
          osc.stop(now + i * 0.08 + 0.55);
        });
      }

      /* ======================================================================
         3. INTERACTIVE FX LIVE STAGE SIMULATOR
         ====================================================================== */
      var canvas = $('#sim-canvas');
      var ctx = canvas ? canvas.getContext('2d') : null;
      var currentFx = 'coldpyro';
      var simParticles = [];
      var simAnimId = null;
      var stageWidth = 960;
      var stageHeight = 480;

      var simHeightSlider = $('#sim-height');
      var simDensitySlider = $('#sim-density');
      var simThemeSlider = $('#sim-theme');
      var simStatusText = $('#sim-status-text');

      function resizeSimCanvas() {
        if (!canvas) return;
        var box = canvas.parentElement;
        var rect = box.getBoundingClientRect();
        var dpr = window.devicePixelRatio || 1;
        canvas.width = rect.width * dpr;
        canvas.height = rect.height * dpr;
        stageWidth = rect.width;
        stageHeight = rect.height;
        if (ctx) {
          ctx.setTransform(1, 0, 0, 1, 0, 0);
          ctx.scale(dpr, dpr);
        }
      }

      /* Particle Constructors */
      function createColdPyroSparks(originX, originY, count, maxH) {
        for (var i = 0; i < count; i++) {
          var angle = (Math.random() * 0.5 - 0.25) - Math.PI / 2;
          var speed = (Math.random() * 0.45 + 0.75) * (maxH / 22);
          simParticles.push({
            type: 'spark',
            x: originX + (Math.random() * 8 - 4),
            y: originY,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed,
            gravity: 0.18,
            decay: Math.random() * 0.02 + 0.015,
            alpha: 1,
            size: Math.random() * 2.8 + 1.2,
            color: Math.random() > 0.3 ? '#E3C9A8' : '#DE8026'
          });
        }
      }

      function createLowFogClouds(count) {
        var w = canvas ? canvas.parentElement.clientWidth : 960;
        var h = canvas ? canvas.parentElement.clientHeight : 480;
        for (var i = 0; i < count; i++) {
          var fromLeft = Math.random() > 0.5;
          simParticles.push({
            type: 'fog',
            x: fromLeft ? -40 : w + 40,
            y: h - Math.random() * 50 - 10,
            vx: fromLeft ? (Math.random() * 1.5 + 0.8) : -(Math.random() * 1.5 + 0.8),
            vy: (Math.random() - 0.5) * 0.3,
            radius: Math.random() * 35 + 25,
            maxRadius: Math.random() * 80 + 70,
            growth: 0.4,
            alpha: Math.random() * 0.35 + 0.2,
            decay: 0.003
          });
        }
      }

      function createSparkularWaterfall(count) {
        var w = canvas ? canvas.parentElement.clientWidth : 960;
        var podCount = 6;
        for (var p = 0; p < podCount; p++) {
          var px = (w / (podCount + 1)) * (p + 1);
          for (var i = 0; i < count / podCount; i++) {
            simParticles.push({
              type: 'waterfall',
              x: px + (Math.random() * 20 - 10),
              y: 40,
              vx: (Math.random() - 0.5) * 1.2,
              vy: Math.random() * 3 + 2,
              gravity: 0.08,
              alpha: 1,
              decay: Math.random() * 0.02 + 0.012,
              size: Math.random() * 2.5 + 1.2,
              color: Math.random() > 0.4 ? '#E3C9A8' : '#CBA482'
            });
          }
        }
      }

      function createFireworksBurst(targetX, targetY) {
        var colors = ['#DE8026', '#E3C9A8', '#F0EEEC', '#8C4A1A', '#FF9A3C'];
        var count = 80;
        for (var i = 0; i < count; i++) {
          var angle = (Math.PI * 2 / count) * i + (Math.random() * 0.1);
          var speed = Math.random() * 5 + 2.5;
          simParticles.push({
            type: 'rocket',
            x: targetX,
            y: targetY,
            vx: Math.cos(angle) * speed,
            vy: Math.sin(angle) * speed,
            gravity: 0.07,
            alpha: 1,
            decay: Math.random() * 0.018 + 0.012,
            size: Math.random() * 2.8 + 1.2,
            color: colors[Math.floor(Math.random() * colors.length)]
          });
        }
      }

      function createColourSmokePuffs(count) {
        var w = canvas ? canvas.parentElement.clientWidth : 960;
        var h = canvas ? canvas.parentElement.clientHeight : 480;
        var smokeColors = ['rgba(222, 128, 38, ', 'rgba(219, 48, 105, ', 'rgba(203, 164, 130, ', 'rgba(235, 130, 60, '];
        var origins = [w * 0.25, w * 0.5, w * 0.75];
        origins.forEach(function (ox) {
          for (var i = 0; i < count; i++) {
            var colBase = smokeColors[Math.floor(Math.random() * smokeColors.length)];
            simParticles.push({
              type: 'csmoke',
              x: ox + (Math.random() * 20 - 10),
              y: h - 20,
              vx: (Math.random() - 0.5) * 1.8,
              vy: -(Math.random() * 2.5 + 1.8),
              radius: Math.random() * 15 + 10,
              growth: 0.5,
              alpha: 0.5,
              decay: 0.007,
              colorBase: colBase
            });
          }
        });
      }

      function createConfettiBlast(count) {
        var w = canvas ? canvas.parentElement.clientWidth : 960;
        var h = canvas ? canvas.parentElement.clientHeight : 480;
        var confettiColors = ['#DE8026', '#E3C9A8', '#CBA482', '#FFFFFF', '#8C4A1A'];
        for (var i = 0; i < count; i++) {
          var fromLeft = Math.random() > 0.5;
          simParticles.push({
            type: 'confetti',
            x: fromLeft ? w * 0.15 : w * 0.85,
            y: h - 40,
            vx: (fromLeft ? 1 : -1) * (Math.random() * 6 + 3),
            vy: -(Math.random() * 10 + 7),
            gravity: 0.2,
            drag: 0.98,
            rotation: Math.random() * 360,
            rotSpeed: (Math.random() - 0.5) * 12,
            width: Math.random() * 9 + 5,
            height: Math.random() * 5 + 3,
            alpha: 1,
            decay: 0.005,
            color: confettiColors[Math.floor(Math.random() * confettiColors.length)]
          });
        }
      }

      /* Trigger Effects Dispatcher */
      function triggerFx(effectName) {
        var w = canvas ? canvas.parentElement.clientWidth : 960;
        var h = canvas ? canvas.parentElement.clientHeight : 480;
        var heightFactor = simHeightSlider ? Number(simHeightSlider.value) : 40;
        var densityFactor = simDensitySlider ? Number(simDensitySlider.value) : 2;

        if (effectName === 'coldpyro') {
          playPyroWhoosh();
          var podPositions = [w * 0.2, w * 0.35, w * 0.5, w * 0.65, w * 0.8];
          podPositions.forEach(function (x) {
            createColdPyroSparks(x, h - 30, 24 * densityFactor, heightFactor);
          });
          simStatusText.textContent = 'Cold Pyro Fountains Firing \u2022 100% Smokeless';
        } else if (effectName === 'lowfog') {
          playPyroWhoosh();
          createLowFogClouds(18 * densityFactor);
          simStatusText.textContent = 'Heavy Dry Ice Low Fog Rolling Across Floor';
        } else if (effectName === 'sparkular') {
          playPyroWhoosh();
          createSparkularWaterfall(36 * densityFactor);
          simStatusText.textContent = 'Sparkular Waterfall Flowing from Stage Truss';
        } else if (effectName === 'fireworks') {
          playPyroWhoosh();
          createFireworksBurst(w * 0.3, h * 0.35);
          setTimeout(function () {
            createFireworksBurst(w * 0.7, h * 0.28);
            playPyroWhoosh();
          }, 250);
          setTimeout(function () {
            createFireworksBurst(w * 0.5, h * 0.2);
            playPyroWhoosh();
          }, 550);
          simStatusText.textContent = 'Sky Fireworks Display Illuminating Night Sky';
        } else if (effectName === 'smoke') {
          playPyroWhoosh();
          createColourSmokePuffs(16 * densityFactor);
          simStatusText.textContent = 'Vibrant Daytime Colour Smoke Billowing';
        } else if (effectName === 'confetti') {
          playConfettiPop();
          createConfettiBlast(70 * densityFactor);
          simStatusText.textContent = 'High-Pressure Metallic Confetti Blast!';
        } else if (effectName === 'finale') {
          playFanfare();
          createLowFogClouds(20);
          simStatusText.textContent = 'Grand Finale: Stage Fog \u2022 Cold Pyro \u2022 Sparkular \u2022 Confetti!';
          setTimeout(function () { triggerFx('coldpyro'); }, 300);
          setTimeout(function () { triggerFx('sparkular'); }, 700);
          setTimeout(function () { triggerFx('confetti'); }, 1200);
          setTimeout(function () { triggerFx('fireworks'); }, 1800);
        }
      }

      /* Simulator Animation Loop */
      function simLoop() {
        if (!ctx || !canvas) return;
        var w = canvas.parentElement.clientWidth;
        var h = canvas.parentElement.clientHeight;

        // Stage Background
        ctx.fillStyle = '#050302';
        ctx.fillRect(0, 0, w, h);

        // Stage Floor Perspective
        var stageDeckY = h - 35;
        var gradFloor = ctx.createLinearGradient(0, stageDeckY, 0, h);
        gradFloor.addColorStop(0, '#190B05');
        gradFloor.addColorStop(1, '#0B0704');
        ctx.fillStyle = gradFloor;
        ctx.fillRect(0, stageDeckY, w, 35);

        // Gold Rim on Stage Deck
        ctx.strokeStyle = 'rgba(222, 128, 38, 0.4)';
        ctx.lineWidth = 2;
        ctx.beginPath();
        ctx.moveTo(0, stageDeckY);
        ctx.lineTo(w, stageDeckY);
        ctx.stroke();

        // Stage Overhead Truss
        ctx.fillStyle = 'rgba(25, 11, 5, 0.6)';
        ctx.fillRect(0, 0, w, 24);
        ctx.strokeStyle = 'rgba(89, 43, 14, 0.5)';
        ctx.beginPath();
        ctx.moveTo(0, 24);
        ctx.lineTo(w, 24);
        ctx.stroke();

        // Ambient Stage Spotlights Cones
        var cone1 = ctx.createRadialGradient(w * 0.25, 20, 10, w * 0.25, h * 0.6, w * 0.4);
        cone1.addColorStop(0, 'rgba(222, 128, 38, 0.08)');
        cone1.addColorStop(1, 'transparent');
        ctx.fillStyle = cone1;
        ctx.fillRect(0, 0, w, h);

        var cone2 = ctx.createRadialGradient(w * 0.75, 20, 10, w * 0.75, h * 0.6, w * 0.4);
        cone2.addColorStop(0, 'rgba(203, 164, 130, 0.07)');
        cone2.addColorStop(1, 'transparent');
        ctx.fillStyle = cone2;
        ctx.fillRect(0, 0, w, h);

        // Update and draw particles
        for (var i = simParticles.length - 1; i >= 0; i--) {
          var p = simParticles[i];
          p.alpha -= p.decay;

          if (p.alpha <= 0) {
            simParticles.splice(i, 1);
            continue;
          }

          if (p.type === 'spark' || p.type === 'waterfall' || p.type === 'rocket') {
            p.x += p.vx;
            p.y += p.vy;
            p.vy += p.gravity;

            ctx.save();
            ctx.globalAlpha = p.alpha;
            ctx.fillStyle = p.color;
            ctx.shadowColor = p.color;
            ctx.shadowBlur = 8;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.size, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
          } else if (p.type === 'fog') {
            p.x += p.vx;
            p.y += p.vy;
            if (p.radius < p.maxRadius) p.radius += p.growth;

            ctx.save();
            ctx.globalAlpha = p.alpha;
            var fogGrad = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.radius);
            fogGrad.addColorStop(0, 'rgba(240, 238, 236, 0.35)');
            fogGrad.addColorStop(0.6, 'rgba(203, 164, 130, 0.15)');
            fogGrad.addColorStop(1, 'transparent');
            ctx.fillStyle = fogGrad;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
          } else if (p.type === 'csmoke') {
            p.x += p.vx;
            p.y += p.vy;
            p.radius += p.growth;

            ctx.save();
            ctx.globalAlpha = p.alpha;
            var sGrad = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, p.radius);
            sGrad.addColorStop(0, p.colorBase + '0.5)');
            sGrad.addColorStop(1, p.colorBase + '0)');
            ctx.fillStyle = sGrad;
            ctx.beginPath();
            ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fill();
            ctx.restore();
          } else if (p.type === 'confetti') {
            p.x += p.vx;
            p.y += p.vy;
            p.vy += p.gravity;
            p.vx *= p.drag;
            p.rotation += p.rotSpeed;

            ctx.save();
            ctx.translate(p.x, p.y);
            ctx.rotate(p.rotation * Math.PI / 180);
            ctx.globalAlpha = p.alpha;
            ctx.fillStyle = p.color;
            ctx.fillRect(-p.width / 2, -p.height / 2, p.width, p.height);
            ctx.restore();
          }
        }

        simAnimId = requestAnimationFrame(simLoop);
      }

      /* ======================================================================
         4. PACKAGE & COST CALCULATOR ENGINE
         ====================================================================== */
      var RATES = {
        pyroUnit: 750,      // per cold pyro unit
        fogUnit: 6500,      // per heavy dry ice machine
        sparkularUnit: 4000,// per sparkular unit
        smokeUnit: 600,     // per smoke canister
        confettiUnit: 3500, // per confetti cannon
        baseCrew: 2500,     // base transport & operator console
        citySurcharge: {
          noida: 0,
          delhi: 1500,
          gurugram: 2500,
          ghaziabad: 1000,
          destination: 6000
        }
      };

      function updateCalculator() {
        var pyro = Number($('#range-pyro').value) || 0;
        var fog = Number($('#range-fog').value) || 0;
        var sparkular = Number($('#range-sparkular').value) || 0;
        var smoke = Number($('#range-smoke').value) || 0;
        var confetti = Number($('#range-confetti').value) || 0;
        var cityKey = $('#calc-city').value || 'noida';
        var cityCost = RATES.citySurcharge[cityKey] || 0;
        var eventType = $('#calc-event-type').options[$('#calc-event-type').selectedIndex].text;

        // Update count badges
        $('#count-pyro').textContent = pyro + ' Units';
        $('#count-fog').textContent = fog + (fog === 1 ? ' Machine' : ' Machines');
        $('#count-sparkular').textContent = sparkular + ' Units';
        $('#count-smoke').textContent = smoke + (smoke === 1 ? ' Canister' : ' Canisters');
        $('#count-confetti').textContent = confetti + (confetti === 1 ? ' Cannon' : ' Cannons');

        // Subtotals
        var pyroCost = pyro * RATES.pyroUnit;
        var fogCost = fog * RATES.fogUnit;
        var sparkularCost = sparkular * RATES.sparkularUnit;
        var smokeCost = smoke * RATES.smokeUnit;
        var confettiCost = confetti * RATES.confettiUnit;

        var total = pyroCost + fogCost + sparkularCost + smokeCost + confettiCost + RATES.baseCrew + cityCost;

        // Display Total in INR
        $('#calc-total-display').textContent = '\u20b9' + total.toLocaleString('en-IN') + '*';

        // Populate itemized breakdown
        var list = $('#calc-summary-list');
        list.innerHTML = '';

        function addRow(label, qty, price) {
          if (qty <= 0) return;
          var div = document.createElement('div');
          div.className = 'calc-summary-row';
          div.innerHTML = '<span>' + label + ' (' + qty + ')</span><span>\u20b9' + price.toLocaleString('en-IN') + '</span>';
          list.appendChild(div);
        }

        addRow('Cold Pyro Fountains', pyro, pyroCost);
        addRow('Low Fog (Dry Ice)', fog, fogCost);
        addRow('Sparkular Stage Gerbs', sparkular, sparkularCost);
        addRow('Colour Smoke Grenades', smoke, smokeCost);
        addRow('Confetti Blasters', confetti, confettiCost);

        var crewDiv = document.createElement('div');
        crewDiv.className = 'calc-summary-row';
        crewDiv.innerHTML = '<span>Certified Crew &amp; Console</span><span>\u20b9' + (RATES.baseCrew + cityCost).toLocaleString('en-IN') + '</span>';
        list.appendChild(crewDiv);

        // Pre-fill WhatsApp URL
        var waLines = [
          'Hello Galaxy Pyrotech Traders, I calculated a package on your website:',
          '\u2022 Event: ' + eventType,
          '\u2022 Venue Area: ' + $('#calc-city').options[$('#calc-city').selectedIndex].text,
          pyro > 0 ? ('\u2022 Cold Pyro Fountains: ' + pyro + ' units') : '',
          fog > 0 ? ('\u2022 Low Fog (Dry Ice): ' + fog + ' machine(s)') : '',
          sparkular > 0 ? ('\u2022 Sparkular Waterfall: ' + sparkular + ' units') : '',
          smoke > 0 ? ('\u2022 Colour Smoke: ' + smoke + ' canister(s)') : '',
          confetti > 0 ? ('\u2022 Confetti Cannons: ' + confetti + ' cannon(s)') : '',
          '\u2022 Estimated Total: \u20b9' + total.toLocaleString('en-IN'),
          'Please confirm availability for my date.'
        ].filter(Boolean).join('\\n');

        $('#calc-wa-btn').setAttribute('href', 'https://wa.me/' + SITE.whatsapp + '?text=' + encodeURIComponent(waLines));
      }

      window.setPreset = function (type) {
        $$('.calc-preset-chip').forEach(function (c) { c.classList.remove('is-active'); });
        if (type === 'varmala') {
          $('#range-pyro').value = 8;
          $('#range-fog').value = 2;
          $('#range-sparkular').value = 0;
          $('#range-smoke').value = 0;
          $('#range-confetti').value = 1;
          $('#preset-varmala').classList.add('is-active');
        } else if (type === 'baraat') {
          $('#range-pyro').value = 12;
          $('#range-fog').value = 0;
          $('#range-sparkular').value = 0;
          $('#range-smoke').value = 8;
          $('#range-confetti').value = 1;
          $('#preset-baraat').classList.add('is-active');
        } else if (type === 'gala') {
          $('#range-pyro').value = 6;
          $('#range-fog').value = 2;
          $('#range-sparkular').value = 4;
          $('#range-smoke').value = 0;
          $('#range-confetti').value = 2;
          $('#preset-gala').classList.add('is-active');
        } else {
          $('#preset-custom').classList.add('is-active');
        }
        updateCalculator();
      };

      /* ======================================================================
         5. FILTERABLE GALLERY & FULLSCREEN LIGHTBOX
         ====================================================================== */
      var currentGalleryIndex = 0;

      function openLightbox(index) {
        currentGalleryIndex = index;
        var item = GALLERY_DATA[index];
        if (!item) return;

        $('#lightbox-img').src = item.src;
        $('#lightbox-img').alt = item.title;
        $('#lightbox-title').textContent = item.title;
        $('#lightbox-desc').textContent = item.desc + ' (' + item.venue + ')';
        $('#lightbox-wa-btn').href = 'https://wa.me/' + SITE.whatsapp + '?text=' + encodeURIComponent('Hi Galaxy Pyrotech, I am inquiring about the ' + item.title + ' setup.');

        $('#lightbox-modal').classList.add('is-open');
        document.body.classList.add('no-scroll');
      }

      function closeLightbox() {
        $('#lightbox-modal').classList.remove('is-open');
        document.body.classList.remove('no-scroll');
      }

      function nextLightbox() {
        currentGalleryIndex = (currentGalleryIndex + 1) % GALLERY_DATA.length;
        openLightbox(currentGalleryIndex);
      }

      function prevLightbox() {
        currentGalleryIndex = (currentGalleryIndex - 1 + GALLERY_DATA.length) % GALLERY_DATA.length;
        openLightbox(currentGalleryIndex);
      }

      /* ======================================================================
         6. REVIEWS & ADD REVIEW MODAL
         ====================================================================== */
      var userReviews = [];
      try {
        var stored = localStorage.getItem('gp_reviews');
        if (stored) userReviews = JSON.parse(stored);
      } catch (e) {}

      function renderReviews() {
        var container = $('#reviews-grid');
        if (!container) return;
        container.innerHTML = '';

        var allReviews = userReviews.concat(DEFAULT_REVIEWS);
        allReviews.forEach(function (r) {
          var card = document.createElement('div');
          card.className = 'review-card';

          var starsHtml = '';
          for (var i = 0; i < 5; i++) {
            starsHtml += '<svg class="icon icon--fill" style="width:16px;height:16px;color:' + (i < r.rating ? 'var(--amber)' : '#592B0E') + '"><use href="#i-star"/></svg>';
          }

          var newBadge = r.isUser ? '<span class="review-badge-new">New Client</span>' : '';

          card.innerHTML =
            '<div class="review-card__stars">' + starsHtml + '</div>' +
            '<p class="review-card__text">"' + r.text + '"</p>' +
            '<div class="review-card__footer">' +
              '<div><div class="review-card__author">' + r.name + newBadge + '</div>' +
              '<div class="review-card__meta">' + r.event + '</div></div>' +
              '<span style="font-size:0.75rem;color:var(--champagne);">' + (r.date || 'Verified') + '</span>' +
            '</div>';
          container.appendChild(card);
        });
      }

      /* ======================================================================
         7. DIRECT BOOKING & CALLBACK LOGIC
         ====================================================================== */
      function showToast(msg) {
        var toast = $('#toast');
        var text = $('#toast-msg');
        if (!toast || !text) return;
        text.textContent = msg;
        toast.classList.add('is-show');
        setTimeout(function () {
          toast.classList.remove('is-show');
        }, 3000);
      }

      function handleBookingWhatsApp() {
        var name = $('#book-name').value.trim();
        var phone = $('#book-phone').value.trim();
        var date = $('#book-date').value;
        var venue = $('#book-venue').value.trim();
        var type = $('#book-type').value;
        var notes = $('#book-notes').value.trim();

        if (!name || !phone || !date || !venue) {
          alert('Please fill in your name, phone number, event date, and venue.');
          return;
        }

        var fxList = [];
        $$('input[name="fx"]:checked').forEach(function (cb) {
          fxList.push(cb.value);
        });

        var message = [
          'Hello Galaxy Pyrotech Traders, I would like to book special effects:',
          '\u2022 Name: ' + name,
          '\u2022 Phone: ' + phone,
          '\u2022 Event Date: ' + date,
          '\u2022 Venue: ' + venue,
          '\u2022 Occasion: ' + type,
          '\u2022 Effects Required: ' + (fxList.length ? fxList.join(', ') : 'All Recommended'),
          notes ? ('\u2022 Notes: ' + notes) : '',
          'Please send confirmation and contract details.'
        ].filter(Boolean).join('\\n');

        window.open('https://wa.me/' + SITE.whatsapp + '?text=' + encodeURIComponent(message), '_blank');
      }

      function handleInstantCallback() {
        var name = $('#book-name').value.trim();
        var phone = $('#book-phone').value.trim();
        var date = $('#book-date').value;
        var venue = $('#book-venue').value.trim();

        if (!name || !phone) {
          alert('Please enter your full name and phone number to request a callback.');
          return;
        }

        var ticketNum = '#GP-' + Math.floor(1000 + Math.random() * 9000);
        $('#callback-ref-ticket').textContent = ticketNum;
        $('#callback-instant-wa').href = 'https://wa.me/' + SITE.whatsapp + '?text=' + encodeURIComponent('Hi Galaxy Pyrotech, I requested an urgent callback for Ticket ' + ticketNum + ' (' + name + ', ' + phone + ').');

        // Play celebration audio and open modal
        playFanfare();
        createConfettiBlast(80);
        $('#callback-modal').classList.add('is-open');
        document.body.classList.add('no-scroll');
      }

      /* ======================================================================
         8. SEARCHABLE FAQ FILTER
         ====================================================================== */
      function filterFaq(query) {
        var q = query.toLowerCase().trim();
        $$('.acc').forEach(function (item) {
          var text = item.textContent.toLowerCase() + ' ' + (item.getAttribute('data-faq') || '');
          if (!q || text.indexOf(q) !== -1) {
            item.style.display = 'block';
            if (q) item.classList.add('is-open');
          } else {
            item.style.display = 'none';
          }
        });
      }

      /* ======================================================================
         9. HERO SPARKS GENERATOR
         ====================================================================== */
      function initHeroSparks() {
        var container = $('#hero-sparks');
        if (!container) return;
        var count = window.innerWidth < 640 ? 10 : 22;
        for (var i = 0; i < count; i++) {
          var s = document.createElement('i');
          s.className = 'spark';
          var dur = (Math.random() * 6 + 7).toFixed(1) + 's';
          var delay = (Math.random() * -10).toFixed(1) + 's';
          var dx = (Math.random() * 80 - 40).toFixed(0) + 'px';
          var size = (Math.random() * 2 + 1.6).toFixed(1) + 'px';
          s.style.cssText = 'left:' + (Math.random() * 96 + 2).toFixed(1) + '%;--dur:' + dur + ';--delay:' + delay + ';--dx:' + dx + ';--size:' + size + ';';
          container.appendChild(s);
        }
      }

      /* ======================================================================
         10. EVENT LISTENERS INITIALIZATION
         ====================================================================== */
      function bindEvents() {
        // Sound toggles
        $('#global-sound-toggle').addEventListener('click', toggleSound);
        $('#sim-sound-btn').addEventListener('click', toggleSound);
        updateSoundUI();

        // Mobile Menu Drawer
        var menuBtn = $('#menu-toggle-btn');
        var mobileMenu = $('#mobile-menu');
        menuBtn.addEventListener('click', function () {
          var isOpen = mobileMenu.classList.contains('is-open');
          mobileMenu.classList.toggle('is-open', !isOpen);
          $('.header').classList.toggle('menu-open', !isOpen);
          menuBtn.setAttribute('aria-expanded', String(!isOpen));
          document.body.classList.toggle('no-scroll', !isOpen);
        });

        $$('.mobile-menu__list a').forEach(function (link) {
          link.addEventListener('click', function () {
            mobileMenu.classList.remove('is-open');
            $('.header').classList.remove('menu-open');
            document.body.classList.remove('no-scroll');
          });
        });

        // Header Scroll Shadow
        window.addEventListener('scroll', function () {
          var y = window.scrollY || window.pageYOffset;
          $('.header').classList.toggle('is-scrolled', y > 15);
        }, { passive: true });

        // Simulator FX buttons
        $$('.sim-trigger-btn').forEach(function (btn) {
          btn.addEventListener('click', function () {
            $$('.sim-trigger-btn').forEach(function (b) { b.classList.remove('is-active'); });
            btn.classList.add('is-active');
            var fx = btn.getAttribute('data-fx');
            currentFx = fx;
            triggerFx(fx);
          });
        });

        // Simulator Sliders
        if (simHeightSlider) {
          simHeightSlider.addEventListener('input', function () {
            $('#sim-height-val').textContent = (simHeightSlider.value / 10).toFixed(1) + ' Meters';
          });
        }
        if (simDensitySlider) {
          simDensitySlider.addEventListener('input', function () {
            var val = Number(simDensitySlider.value);
            $('#sim-density-val').textContent = val === 1 ? 'Subtle' : (val === 2 ? 'High (Grand)' : 'Spectacular');
          });
        }
        if (simThemeSlider) {
          simThemeSlider.addEventListener('input', function () {
            var val = Number(simThemeSlider.value);
            $('#sim-theme-val').textContent = val === 1 ? 'Amber \u00d7 Champagne' : (val === 2 ? 'Royal Palace Night' : 'Open Lawn Warmth');
          });
        }

        // Clear Stage Button
        $('#sim-clear-btn').addEventListener('click', function () {
          simParticles = [];
          simStatusText.textContent = 'Stage Cleared';
        });

        // Stage Canvas Click & Mobile Touch to Fire
        if (canvas) {
          function fireAt(clientX, clientY) {
            var rect = canvas.getBoundingClientRect();
            var x = clientX - rect.left;
            var y = clientY - rect.top;
            playSparkleChime();
            createColdPyroSparks(x, y, 30, 45);
          }

          canvas.addEventListener('click', function (e) {
            fireAt(e.clientX, e.clientY);
          });

          canvas.addEventListener('touchstart', function (e) {
            if (e.touches && e.touches.length > 0) {
              fireAt(e.touches[0].clientX, e.touches[0].clientY);
            }
          }, { passive: true });

          canvas.addEventListener('touchmove', function (e) {
            if (e.touches && e.touches.length > 0) {
              var rect = canvas.getBoundingClientRect();
              var x = e.touches[0].clientX - rect.left;
              var y = e.touches[0].clientY - rect.top;
              if (Math.random() > 0.45) {
                createColdPyroSparks(x, y, 12, 35);
              }
            }
          }, { passive: true });
        }

        // Calculator Range Sliders & Inputs
        ['range-pyro', 'range-fog', 'range-sparkular', 'range-smoke', 'range-confetti', 'calc-city', 'calc-event-type'].forEach(function (id) {
          var el = $('#' + id);
          if (el) el.addEventListener('input', updateCalculator);
        });

        // Presets
        $('#preset-varmala').addEventListener('click', function () { setPreset('varmala'); });
        $('#preset-baraat').addEventListener('click', function () { setPreset('baraat'); });
        $('#preset-gala').addEventListener('click', function () { setPreset('gala'); });
        $('#preset-custom').addEventListener('click', function () { setPreset('custom'); });

        // Copy quotation button
        $('#calc-copy-btn').addEventListener('click', function () {
          var total = $('#calc-total-display').textContent;
          var text = 'Galaxy Pyrotech Traders Quotation:\\n' +
            'Cold Pyro: ' + $('#count-pyro').textContent + '\\n' +
            'Low Fog: ' + $('#count-fog').textContent + '\\n' +
            'Sparkular: ' + $('#count-sparkular').textContent + '\\n' +
            'Colour Smoke: ' + $('#count-smoke').textContent + '\\n' +
            'Confetti: ' + $('#count-confetti').textContent + '\\n' +
            'Location: ' + $('#calc-city').options[$('#calc-city').selectedIndex].text + '\\n' +
            'Estimated Total: ' + total + '\\n' +
            'Phone / WhatsApp: +91 95826 73570';
          navigator.clipboard.writeText(text).then(function () {
            showToast('Quotation copied to clipboard!');
          }).catch(function () {
            showToast('Quotation ready!');
          });
        });

        // Gallery Filter Buttons
        $$('.gallery-filter-btn').forEach(function (btn) {
          btn.addEventListener('click', function () {
            $$('.gallery-filter-btn').forEach(function (b) { b.classList.remove('is-active'); });
            btn.classList.add('is-active');
            var filter = btn.getAttribute('data-filter');
            $$('.gallery-card').forEach(function (card) {
              if (filter === 'all' || card.getAttribute('data-category') === filter) {
                card.style.display = 'block';
              } else {
                card.style.display = 'none';
              }
            });
          });
        });

        // Gallery Card Click to open Lightbox
        $$('.gallery-card').forEach(function (card) {
          card.addEventListener('click', function () {
            var idx = Number(card.getAttribute('data-index')) || 0;
            openLightbox(idx);
          });
        });

        // Lightbox Navigation & Close + Touch Swipe
        $('#lightbox-close-btn').addEventListener('click', closeLightbox);
        $('#lightbox-prev-btn').addEventListener('click', prevLightbox);
        $('#lightbox-next-btn').addEventListener('click', nextLightbox);
        var lbModal = $('#lightbox-modal');
        lbModal.addEventListener('click', function (e) {
          if (e.target === lbModal) closeLightbox();
        });

        var lbTouchStartX = 0;
        var lbTouchStartY = 0;
        lbModal.addEventListener('touchstart', function (e) {
          if (e.touches && e.touches.length > 0) {
            lbTouchStartX = e.touches[0].clientX;
            lbTouchStartY = e.touches[0].clientY;
          }
        }, { passive: true });

        lbModal.addEventListener('touchend', function (e) {
          if (e.changedTouches && e.changedTouches.length > 0) {
            var diffX = e.changedTouches[0].clientX - lbTouchStartX;
            var diffY = e.changedTouches[0].clientY - lbTouchStartY;
            if (Math.abs(diffX) > 40 && Math.abs(diffX) > Math.abs(diffY)) {
              if (diffX < 0) {
                nextLightbox();
              } else {
                prevLightbox();
              }
            }
          }
        }, { passive: true });

        document.addEventListener('keydown', function (e) {
          if ($('#lightbox-modal').classList.contains('is-open')) {
            if (e.key === 'Escape') closeLightbox();
            if (e.key === 'ArrowLeft') prevLightbox();
            if (e.key === 'ArrowRight') nextLightbox();
          }
          if ($('#review-modal').classList.contains('is-open') && e.key === 'Escape') {
            $('#review-modal').classList.remove('is-open');
            document.body.classList.remove('no-scroll');
          }
          if ($('#callback-modal').classList.contains('is-open') && e.key === 'Escape') {
            $('#callback-modal').classList.remove('is-open');
            document.body.classList.remove('no-scroll');
          }
        });

        // Booking actions
        $('#submit-booking-wa').addEventListener('click', handleBookingWhatsApp);
        $('#submit-callback').addEventListener('click', handleInstantCallback);
        $('#callback-modal-close').addEventListener('click', function () {
          $('#callback-modal').classList.remove('is-open');
          document.body.classList.remove('no-scroll');
        });

        // Review Modal
        var currentStarRating = 5;
        $('#open-review-modal-btn').addEventListener('click', function () {
          $('#review-modal').classList.add('is-open');
          document.body.classList.add('no-scroll');
        });

        $('#review-modal-close').addEventListener('click', function () {
          $('#review-modal').classList.remove('is-open');
          document.body.classList.remove('no-scroll');
        });

        $$('.star-btn').forEach(function (btn) {
          btn.addEventListener('click', function () {
            var val = Number(btn.getAttribute('data-val')) || 5;
            currentStarRating = val;
            $$('.star-btn').forEach(function (b) {
              var v = Number(b.getAttribute('data-val'));
              b.classList.toggle('is-active', v <= val);
            });
          });
        });

        $('#add-review-form').addEventListener('submit', function (e) {
          e.preventDefault();
          var name = $('#rev-name').value.trim();
          var evt = $('#rev-event').value.trim();
          var text = $('#rev-text').value.trim();
          if (!name || !text) return;

          var newRev = {
            name: name,
            event: evt,
            rating: currentStarRating,
            text: text,
            date: 'Today',
            isUser: true
          };

          userReviews.unshift(newRev);
          try {
            localStorage.setItem('gp_reviews', JSON.stringify(userReviews));
          } catch (err) {}

          renderReviews();
          $('#review-modal').classList.remove('is-open');
          document.body.classList.remove('no-scroll');
          showToast('Thank you! Your review has been published.');
          playSparkleChime();
          $('#add-review-form').reset();
        });

        // FAQ Accordions
        $$('.acc__btn').forEach(function (btn) {
          btn.addEventListener('click', function () {
            var item = btn.closest('.acc');
            var isOpen = item.classList.contains('is-open');
            $$('.acc.is-open').forEach(function (other) {
              if (other !== item) other.classList.remove('is-open');
            });
            item.classList.toggle('is-open', !isOpen);
          });
        });

        // FAQ Search
        $('#faq-search').addEventListener('input', function (e) {
          filterFaq(e.target.value);
        });

        // Year update
        var yr = $('#current-year');
        if (yr) yr.textContent = new Date().getFullYear();

        // Window resize
        window.addEventListener('resize', resizeSimCanvas);
      }

      /* Initialize everything */
      function init() {
        initHeroSparks();
        resizeSimCanvas();
        simLoop();
        updateCalculator();
        renderReviews();
        bindEvents();
      }

      if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
      } else {
        init();
      }
    })();
  </script>
</body>
</html>
'''
