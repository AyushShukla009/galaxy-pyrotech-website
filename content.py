# HTML content markup module for Galaxy Pyrotech Traders
def get_svg_sprites():
    return '''
  <!-- =====================================================================
       SVG ICON SPRITES
       ===================================================================== -->
  <svg style="display:none;" aria-hidden="true">
    <defs>
      <symbol id="i-phone" viewBox="0 0 24 24"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></symbol>
      <symbol id="i-whatsapp" viewBox="0 0 24 24"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></symbol>
      <symbol id="i-coldpyro" viewBox="0 0 24 24"><path d="M12 2v6M12 18v4M4.93 4.93l4.24 4.24M14.83 14.83l4.24 4.24M2 12h6M18 12h4M4.93 19.07l4.24-4.24M14.83 9.17l4.24-4.24"/><circle cx="12" cy="12" r="3"/></symbol>
      <symbol id="i-sparkular" viewBox="0 0 24 24"><path d="M12 2l2.4 7.2h7.6l-6 4.8 2.4 7.2-6.4-4.8-6.4 4.8 2.4-7.2-6-4.8h7.6z"/></symbol>
      <symbol id="i-lowfog" viewBox="0 0 24 24"><path d="M17.7 7.7a2.5 2.5 0 1 1 1.8 4.3H2"/><path d="M9.6 4.6A2 2 0 1 1 11 8H2"/><path d="M12.6 19.4A2 2 0 1 0 14 16H2"/></symbol>
      <symbol id="i-fireworks" viewBox="0 0 24 24"><circle cx="12" cy="12" r="2"/><path d="M12 2v4M12 18v4M2 12h4M18 12h4M4.9 4.9l2.8 2.8M16.3 16.3l2.8 2.8M19.1 4.9l-2.8 2.8M7.7 16.3l-2.8 2.8"/></symbol>
      <symbol id="i-smoke" viewBox="0 0 24 24"><path d="M8 20c-2.5 0-4-1.6-4-3.5 0-1.7 1.3-3 3-3.3C7.3 10.7 9.4 9 12 9c2.5 0 4.5 1.6 5 3.6 1.9.2 3 1.5 3 3.2 0 2-1.6 4.2-4 4.2z"/><path d="M12 5c0-1 1-1.5 1-2.5"/></symbol>
      <symbol id="i-bubble" viewBox="0 0 24 24"><circle cx="8" cy="15" r="4.5"/><circle cx="16.5" cy="8" r="3"/><circle cx="17" cy="17.5" r="2"/></symbol>
      <symbol id="i-confetti" viewBox="0 0 24 24"><path d="M4 14l6-6M9 4l1 3M14 9l3 1M3 21l3-1 2-5-4-1-1 7zM18 12l2 2M21 3l-3 1-1 3 3 1 1-5z"/></symbol>
      <symbol id="i-star" viewBox="0 0 24 24"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/></symbol>
      <symbol id="i-check" viewBox="0 0 24 24"><polyline points="20 6 9 17 4 12"/></symbol>
      <symbol id="i-close" viewBox="0 0 24 24"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></symbol>
      <symbol id="i-menu" viewBox="0 0 24 24"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></symbol>
      <symbol id="i-chevron" viewBox="0 0 24 24"><polyline points="6 9 12 15 18 9"/></symbol>
      <symbol id="i-pin" viewBox="0 0 24 24"><path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"/><circle cx="12" cy="10" r="3"/></symbol>
      <symbol id="i-mail" viewBox="0 0 24 24"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></symbol>
      <symbol id="i-clock" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></symbol>
      <symbol id="i-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></symbol>
      <symbol id="i-sound" viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></symbol>
      <symbol id="i-mute" viewBox="0 0 24 24"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><line x1="23" y1="9" x2="17" y2="15"/><line x1="17" y1="9" x2="23" y2="15"/></symbol>
      <symbol id="i-spark" viewBox="0 0 24 24"><path d="M12 2l1.8 5.5L19 9.3l-5.2 1.8L12 17l-1.8-5.9L5 9.3l5.2-1.8L12 2z"/></symbol>
      <symbol id="i-instagram" viewBox="0 0 24 24"><rect x="2" y="2" width="20" height="20" rx="5" ry="5"/><path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"/><line x1="17.5" y1="6.5" x2="17.51" y2="6.5"/></symbol>
      <symbol id="i-play" viewBox="0 0 24 24"><polygon points="5 3 19 12 5 21 5 3"/></symbol>
    </defs>
  </svg>
'''

def get_body():
    return '''
  <!-- Ambient background glow layers -->
  <div class="sky" aria-hidden="true">
    <div class="sky__glow sky__glow--1"></div>
    <div class="sky__glow sky__glow--2"></div>
    <div class="sky__glow sky__glow--3"></div>
  </div>

  <!-- =====================================================================
       1. TOP NAVIGATION
       ===================================================================== -->
  <header class="header" id="top">
    <div class="container header__bar">
      <!-- Brand Logo with Golden Rim -->
      <a class="brand" href="#home" aria-label="Galaxy Pyrotech Traders, Home">
        <div class="brand__logo-frame">
          <img class="brand__logo" src="assets/logo.jpg" alt="Galaxy Pyrotech Logo" width="48" height="48">
        </div>
        <div class="brand__text">
          <span class="brand__name">Galaxy Pyrotech</span>
          <span class="brand__tag">Light up the moments</span>
        </div>
      </a>

      <!-- Desktop Nav -->
      <nav class="nav" aria-label="Primary navigation">
        <ul class="nav__list">
          <li><a href="#services" data-nav="services">Services</a></li>
          <li><a href="#reels" data-nav="reels">Live Reels</a></li>
          <li><a href="#simulator" data-nav="simulator">Simulator</a></li>
          <li><a href="#calculator" data-nav="calculator">Calculator</a></li>
          <li><a href="#gallery" data-nav="gallery">Showcase</a></li>
          <li><a href="#reviews" data-nav="reviews">Reviews</a></li>
          <li><a href="#contact" data-nav="contact">Contact</a></li>
        </ul>
      </nav>

      <!-- Header Action Buttons -->
      <div class="header__actions">
        <!-- Web Audio SFX Toggle -->
        <button class="sound-toggle" id="global-sound-toggle" type="button" aria-label="Toggle Sound Effects">
          <svg class="icon" aria-hidden="true"><use href="#i-sound"/></svg>
          <span class="sound-label">SFX: ON</span>
        </button>

        <a class="btn btn--call btn--sm" href="tel:+919582673570" aria-label="Call Galaxy Pyrotech at +91 95826 73570">
          <svg class="icon" aria-hidden="true"><use href="#i-phone"/></svg>
          <span>Call</span>
        </a>

        <a class="btn btn--wa btn--sm" href="https://wa.me/919582673570?text=Hello%20Galaxy%20Pyrotech%2C%20I%20would%20like%20to%20inquire%20about%20event%20special%20effects." target="_blank" rel="noopener" aria-label="WhatsApp Galaxy Pyrotech">
          <svg class="icon" aria-hidden="true"><use href="#i-whatsapp"/></svg>
          <span>WhatsApp</span>
        </a>

        <button class="nav__toggle" id="menu-toggle-btn" type="button" aria-expanded="false" aria-label="Toggle navigation menu">
          <svg class="icon i-menu" aria-hidden="true"><use href="#i-menu"/></svg>
          <svg class="icon i-close" aria-hidden="true"><use href="#i-close"/></svg>
        </button>
      </div>
    </div>
  </header>

  <!-- Mobile Drawer Menu -->
  <div class="mobile-menu" id="mobile-menu" aria-hidden="true">
    <nav class="mobile-menu__list">
      <a href="#home">Home</a>
      <a href="#services">Services</a>
      <a href="#reels">Live Video Reels</a>
      <a href="#simulator">Live FX Simulator</a>
      <a href="#calculator">Instant Cost Calculator</a>
      <a href="#gallery">Showcase Gallery</a>
      <a href="#reviews">Client Testimonials</a>
      <a href="#booking">Book Your Event</a>
      <a href="#faq">Frequently Asked Questions</a>
      <a href="#contact">Contact &amp; Location</a>
    </nav>
    <div class="mobile-menu__actions">
      <a class="btn btn--wa btn--lg" href="https://wa.me/919582673570?text=Hello%20Galaxy%20Pyrotech%2C%20I%20would%20like%20to%20inquire%20about%20event%20special%20effects." target="_blank" rel="noopener">
        <svg class="icon" aria-hidden="true"><use href="#i-whatsapp"/></svg>
        <span>Chat on WhatsApp (24/7)</span>
      </a>
      <a class="btn btn--call btn--lg" href="tel:+919582673570">
        <svg class="icon" aria-hidden="true"><use href="#i-phone"/></svg>
        <span>Call Now: +91 95826 73570</span>
      </a>
    </div>
  </div>

  <main id="main">
    <!-- =====================================================================
         2. HERO SECTION
         ===================================================================== -->
    <section class="hero" id="home">
      <!-- Floating amber ember particles -->
      <div class="hero__sparks" id="hero-sparks" aria-hidden="true"></div>

      <div class="container hero__inner">
        <div class="hero__copy">
          <div class="hero__badge">
            <span class="hero__badge-dot"></span>
            <span>24/7 Instant Response &bull; Pan-India Service</span>
          </div>

          <h1 class="hero__title">
            Transform Your Event Into A <span class="hero__title-accent">Royal Spectacle</span>
          </h1>

          <p class="hero__lead">
            Premier special effects for luxury weddings, royal varmala entries, grand sangeets, and celebrations. 100% smokeless Cold Pyro, Sparkular waterfalls, heavy Low Fog dry ice clouds, and sky fireworks.
          </p>

          <p class="hero__area">
            <svg class="icon" aria-hidden="true"><use href="#i-pin"/></svg>
            <span>Based in Sector 22, Noida &bull; Serving Noida, Delhi NCR &amp; Destination Weddings</span>
          </p>

          <div class="hero__actions">
            <a class="btn btn--primary btn--pulse btn--lg" href="#calculator">
              <svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg>
              <span>Instant Cost Calculator</span>
            </a>

            <a class="btn btn--wa btn--lg" href="https://wa.me/919582673570?text=Hello%20Galaxy%20Pyrotech%2C%20I%20would%20like%20to%20get%20a%20quotation%20for%20my%20upcoming%20event." target="_blank" rel="noopener">
              <svg class="icon" aria-hidden="true"><use href="#i-whatsapp"/></svg>
              <span>WhatsApp Us 24/7</span>
            </a>

            <a class="btn btn--outline" href="#simulator">
              <svg class="icon" aria-hidden="true"><use href="#i-sparkular"/></svg>
              <span>Test FX Live Simulator</span>
            </a>
          </div>

          <div class="hero__assure">
            <div class="hero__assure-item">
              <svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>
              <span>100% Smokeless Cold Pyro</span>
            </div>
            <div class="hero__assure-item">
              <svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>
              <span>Certified Pyrotechnic Crew</span>
            </div>
            <div class="hero__assure-item">
              <svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>
              <span>Digital Wireless Firing Consoles</span>
            </div>
            <div class="hero__assure-item">
              <svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>
              <span>Open 24 Hours</span>
            </div>
          </div>
        </div>

        <!-- Hero Visual Showcase Card -->
        <div class="hero__visual-wrap">
          <div class="hero__visual-card">
            <img class="hero__visual-img" src="assets/hero_varmala_palace.jpg" alt="Galaxy Pyrotech grand royal varmala stage special effects with cold pyro and sky fireworks">
            <a class="hero__reel-pill" href="#reels" aria-label="Watch 4 Live Pyrotechnic Reels">
              <span class="hero__reel-pill-icon"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg></span>
              <span>Watch 4 Live Reels</span>
            </a>
            <div class="hero__visual-caption">
              <div>
                <p class="hero__visual-title">Royal Mandap Varmala &amp; Sky Fireworks</p>
                <p class="hero__visual-sub">Towering Cold Pyro &times; Royal Sky Shells &times; Rose Shower</p>
              </div>
              <a class="btn btn--wa btn--sm" href="https://wa.me/919582673570?text=Hi%20Galaxy%20Pyrotech%2C%20I%20saw%20your%20Royal%20Varmala%20Stage%20setup%20and%20want%20details." target="_blank" rel="noopener">
                Book
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         3. TRUST BAR
         ===================================================================== -->
    <section class="section section--tight" aria-label="Our core promises">
      <div class="container">
        <ul class="trust__grid">
          <li class="trust__cell">
            <div class="trust__icon"><svg class="icon" aria-hidden="true"><use href="#i-coldpyro"/></svg></div>
            <h3>100% Indoor Safe</h3>
            <p>Non-pyrotechnic titanium cold gerbs. Cool to the touch, zero hot fallout, and banquet friendly.</p>
          </li>
          <li class="trust__cell">
            <div class="trust__icon"><svg class="icon" aria-hidden="true"><use href="#i-check"/></svg></div>
            <h3>Trained Technicians</h3>
            <p>Every event is operated on-site by certified pyrotechnicians with multi-channel digital consoles.</p>
          </li>
          <li class="trust__cell">
            <div class="trust__icon"><svg class="icon" aria-hidden="true"><use href="#i-clock"/></svg></div>
            <h3>24/7 Immediate Dispatch</h3>
            <p>Located at Sector 22, Noida. Emergency bookings and last-minute wedding setups accommodated.</p>
          </li>
          <li class="trust__cell">
            <div class="trust__icon"><svg class="icon" aria-hidden="true"><use href="#i-star"/></svg></div>
            <h3>Unmatched Elegance</h3>
            <p>Choreographed to your entry music cues, down to the exact second of your varmala or first dance.</p>
          </li>
        </ul>
      </div>
    </section>

    <!-- =====================================================================
         4. SERVICES SHOWCASE
         ===================================================================== -->
    <section class="section" id="services">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="section-tag"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg>Our Signature Special Effects</span>
            <h2>Engineered For Breathtaking Celebrations</h2>
          </div>
          <p>Choose individual effects or combine them into a synchronized package tailored to your venue and timing.</p>
        </div>

        <div class="services__grid">
          <!-- 1. Cold Pyro -->
          <article class="service-card">
            <div class="service-card__media">
              <img class="service-card__img" src="assets/cold_pyro_fan_stage.jpg" alt="Fan-burst cold pyro sparkular fountains at luxury wedding stage" loading="lazy">
              <span class="service-card__badge">Indoor &amp; Outdoor</span>
            </div>
            <div class="service-card__body">
              <div class="service-card__header">
                <span class="service-card__icon"><svg class="icon" aria-hidden="true"><use href="#i-coldpyro"/></svg></span>
                <h3>Cold Pyro Fountains</h3>
              </div>
              <p>Brilliant upward fountains of non-hazardous golden sparks. Cool to touch, safe for delicate bridal attire, and banquet-approved.</p>
              <div class="service-card__specs">
                <span class="service-card__spec">Height: 2m &ndash; 5m</span>
                <span class="service-card__spec">Duration: 30s &ndash; 60s</span>
                <span class="service-card__spec">Smokeless</span>
              </div>
              <div class="service-card__actions">
                <a class="btn btn--outline btn--sm" href="#calculator" onclick="setPreset('varmala')">Calculate</a>
                <a class="btn btn--wa btn--sm" href="https://wa.me/919582673570?text=Hi%20Galaxy%20Pyrotech%2C%20I%20am%20interested%20in%20Cold%20Pyro%20Fountains%20for%20my%20event." target="_blank" rel="noopener">WhatsApp</a>
              </div>
            </div>
          </article>

          <!-- 2. Low Fog -->
          <article class="service-card">
            <div class="service-card__media">
              <img class="service-card__img" src="assets/low_fog_sparkler_entry.jpg" alt="Couple walking through heavy dry ice low fog with sparkler archway" loading="lazy">
              <span class="service-card__badge">Zero Residue</span>
            </div>
            <div class="service-card__body">
              <div class="service-card__header">
                <span class="service-card__icon"><svg class="icon" aria-hidden="true"><use href="#i-lowfog"/></svg></span>
                <h3>Heavy Low Fog / Dry Ice</h3>
              </div>
              <p>Dense, ground-hugging dry ice clouds that envelope the dance floor knee-deep without rising. Creates the iconic walking-on-clouds effect.</p>
              <div class="service-card__specs">
                <span class="service-card__spec">Coverage: 1500+ sq ft</span>
                <span class="service-card__spec">Does not trigger alarms</span>
                <span class="service-card__spec">Odourless</span>
              </div>
              <div class="service-card__actions">
                <a class="btn btn--outline btn--sm" href="#calculator" onclick="setPreset('varmala')">Calculate</a>
                <a class="btn btn--wa btn--sm" href="https://wa.me/919582673570?text=Hi%20Galaxy%20Pyrotech%2C%20I%20am%20interested%20in%20Low%20Fog%20Dry%20Ice%20for%20my%20event." target="_blank" rel="noopener">WhatsApp</a>
              </div>
            </div>
          </article>

          <!-- 3. Sparkular Waterfall -->
          <article class="service-card">
            <div class="service-card__media">
              <img class="service-card__img" src="assets/rotating_catherine_wheels.jpg" alt="Twin rotating cold pyro Catherine wheels and golden spark waterfalls" loading="lazy">
              <span class="service-card__badge">DMX Controlled</span>
            </div>
            <div class="service-card__body">
              <div class="service-card__header">
                <span class="service-card__icon"><svg class="icon" aria-hidden="true"><use href="#i-sparkular"/></svg></span>
                <h3>Sparkular Waterfall &amp; Wheels</h3>
              </div>
              <p>Electronic cold spark machines and rotating Catherine wheels mounted to form cascading curtains of starlight and spinning spark pinwheels.</p>
              <div class="service-card__specs">
                <span class="service-card__spec">Rotating Wheels</span>
                <span class="service-card__spec">Continuous Output</span>
                <span class="service-card__spec">Zero Gunpowder</span>
              </div>
              <div class="service-card__actions">
                <a class="btn btn--outline btn--sm" href="#calculator" onclick="setPreset('gala')">Calculate</a>
                <a class="btn btn--wa btn--sm" href="https://wa.me/919582673570?text=Hi%20Galaxy%20Pyrotech%2C%20I%20am%20interested%20in%20Sparkular%20Waterfall%20for%20my%20event." target="_blank" rel="noopener">WhatsApp</a>
              </div>
            </div>
          </article>

          <!-- 4. Sky Fireworks -->
          <article class="service-card">
            <div class="service-card__media">
              <img class="service-card__img" src="assets/sky_fireworks_mandap.jpg" alt="High-altitude aerial fireworks bursting above royal wedding floral mandap" loading="lazy">
              <span class="service-card__badge">Outdoor Spectacular</span>
            </div>
            <div class="service-card__body">
              <div class="service-card__header">
                <span class="service-card__icon"><svg class="icon" aria-hidden="true"><use href="#i-fireworks"/></svg></span>
                <h3>Sky Fireworks &amp; Shells</h3>
              </div>
              <p>Panoramic aerial fireworks displays, multi-shot cake barrages, and glittering willow shells for farmhouse and palace wedding finales.</p>
              <div class="service-card__specs">
                <span class="service-card__spec">High Altitude Shells</span>
                <span class="service-card__spec">Licensed Setup</span>
                <span class="service-card__spec">Grand Finale</span>
              </div>
              <div class="service-card__actions">
                <a class="btn btn--outline btn--sm" href="#calculator">Calculate</a>
                <a class="btn btn--wa btn--sm" href="https://wa.me/919582673570?text=Hi%20Galaxy%20Pyrotech%2C%20I%20am%20interested%20in%20Sky%20Fireworks%20for%20my%20event." target="_blank" rel="noopener">WhatsApp</a>
              </div>
            </div>
          </article>

          <!-- 5. Colour Smoke -->
          <article class="service-card">
            <div class="service-card__media">
              <img class="service-card__img" src="assets/colour_smoke_rainbow_mandap.jpg" alt="Vibrant rainbow daytime colour smoke plumes shooting behind wedding mandap" loading="lazy">
              <span class="service-card__badge">Daytime Special</span>
            </div>
            <div class="service-card__body">
              <div class="service-card__header">
                <span class="service-card__icon"><svg class="icon" aria-hidden="true"><use href="#i-smoke"/></svg></span>
                <h3>Vibrant Colour Smoke</h3>
              </div>
              <p>High-density non-staining organic colour smoke canisters. Stunning visual backdrop for daytime Baraat entries, Haldi ceremonies, and reveals.</p>
              <div class="service-card__specs">
                <span class="service-card__spec">Multiple Tones</span>
                <span class="service-card__spec">Non-Toxic</span>
                <span class="service-card__spec">Fabric Safe</span>
              </div>
              <div class="service-card__actions">
                <a class="btn btn--outline btn--sm" href="#calculator" onclick="setPreset('baraat')">Calculate</a>
                <a class="btn btn--wa btn--sm" href="https://wa.me/919582673570?text=Hi%20Galaxy%20Pyrotech%2C%20I%20am%20interested%20in%20Colour%20Smoke%20for%20my%20event." target="_blank" rel="noopener">WhatsApp</a>
              </div>
            </div>
          </article>

          <!-- 6. Royal Varmala Package -->
          <article class="service-card">
            <div class="service-card__media">
              <img class="service-card__img" src="assets/royal_ghodi_flame_entry.jpg" alt="Grand Ghodi Baraat entry on red carpet with vertical flame machines and sparkulars" loading="lazy">
              <span class="service-card__badge">Most Popular</span>
            </div>
            <div class="service-card__body">
              <div class="service-card__header">
                <span class="service-card__icon"><svg class="icon" aria-hidden="true"><use href="#i-confetti"/></svg></span>
                <h3>Royal Stage &amp; Baraat</h3>
              </div>
              <p>Our flagship synchronized experience: Ghodi entry flame fx, rotating cold pyros, dual heavy low fog, and high-pressure metallic confetti cannons.</p>
              <div class="service-card__specs">
                <span class="service-card__spec">Synchronized Cues</span>
                <span class="service-card__spec">Complete Stage Coverage</span>
                <span class="service-card__spec">Full Crew Included</span>
              </div>
              <div class="service-card__actions">
                <a class="btn btn--outline btn--sm" href="#calculator" onclick="setPreset('varmala')">Calculate</a>
                <a class="btn btn--wa btn--sm" href="https://wa.me/919582673570?text=Hi%20Galaxy%20Pyrotech%2C%20I%20am%20interested%20in%20the%20Complete%20Royal%20Stage%20Package." target="_blank" rel="noopener">WhatsApp</a>
              </div>
            </div>
          </article>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         4B. LIVE VIDEO REELS SHOWCASE (REAL MOMENTS IN MOTION)
         ===================================================================== -->
    <section class="section section--shaded" id="reels">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="section-tag"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg>Real Moments in Motion</span>
            <h2>Watch Our Pyrotechnics Live</h2>
          </div>
          <p>Watch raw, unedited footage of our cold pyro waterfalls, rotating Catherine wheels, low fog clouds, and sky fireworks in action across real weddings.</p>
        </div>

        <div class="reels__grid">
          <!-- Reel 1: Rotating Catherine Wheel Varmala -->
          <div class="reel-card" data-reel-index="0" data-video="assets/reels/reel_varmala_rotating_wheel.mp4">
            <video class="reel-card__video" muted loop playsinline preload="metadata" poster="assets/reels/reel_varmala_rotating_wheel_poster.jpg">
              <source src="assets/reels/reel_varmala_rotating_wheel.mp4" type="video/mp4">
            </video>
            <div class="reel-card__overlay">
              <div class="reel-card__top">
                <span class="reel-card__badge"><span class="reel-card__badge-live"></span> Live Reel</span>
                <span class="reel-card__duration">0:19</span>
              </div>
              <div class="reel-card__play">
                <svg class="icon" aria-hidden="true"><use href="#i-play"/></svg>
              </div>
              <div class="reel-card__meta">
                <h3 class="reel-card__title">Rotating Catherine Wheel</h3>
                <p class="reel-card__sub">Glass Runway Varmala &times; Cold Pyro</p>
                <p class="reel-card__venue">Grand Varmala Stage, Noida</p>
              </div>
            </div>
          </div>

          <!-- Reel 2: Heritage Palace Cold Pyro Fountains -->
          <div class="reel-card" data-reel-index="1" data-video="assets/reels/reel_palace_stage_pyro.mp4">
            <video class="reel-card__video" muted loop playsinline preload="metadata" poster="assets/reels/reel_palace_stage_pyro_poster.jpg">
              <source src="assets/reels/reel_palace_stage_pyro.mp4" type="video/mp4">
            </video>
            <div class="reel-card__overlay">
              <div class="reel-card__top">
                <span class="reel-card__badge"><span class="reel-card__badge-live"></span> Live Reel</span>
                <span class="reel-card__duration">0:10</span>
              </div>
              <div class="reel-card__play">
                <svg class="icon" aria-hidden="true"><use href="#i-play"/></svg>
              </div>
              <div class="reel-card__meta">
                <h3 class="reel-card__title">Heritage Palace Pyro</h3>
                <p class="reel-card__sub">Towering 5M Fountains &times; Petal Rain</p>
                <p class="reel-card__venue">Heritage Palace Lawn, Delhi NCR</p>
              </div>
            </div>
          </div>

          <!-- Reel 3: Midnight Sky Fireworks Finale -->
          <div class="reel-card" data-reel-index="2" data-video="assets/reels/reel_midnight_sky_fireworks.mp4">
            <video class="reel-card__video" muted loop playsinline preload="metadata" poster="assets/reels/reel_midnight_sky_fireworks_poster.jpg">
              <source src="assets/reels/reel_midnight_sky_fireworks.mp4" type="video/mp4">
            </video>
            <div class="reel-card__overlay">
              <div class="reel-card__top">
                <span class="reel-card__badge"><span class="reel-card__badge-live"></span> Live Reel</span>
                <span class="reel-card__duration">0:11</span>
              </div>
              <div class="reel-card__play">
                <svg class="icon" aria-hidden="true"><use href="#i-play"/></svg>
              </div>
              <div class="reel-card__meta">
                <h3 class="reel-card__title">Midnight Sky Fireworks</h3>
                <p class="reel-card__sub">Golden Willow Aerial Shells</p>
                <p class="reel-card__venue">Farmhouse Lawn Celebration</p>
              </div>
            </div>
          </div>

          <!-- Reel 4: Aerial Pyrotechnic Cake Barrage -->
          <div class="reel-card" data-reel-index="3" data-video="assets/reels/reel_aerial_pyro_shells.mp4">
            <video class="reel-card__video" muted loop playsinline preload="metadata" poster="assets/reels/reel_aerial_pyro_shells_poster.jpg">
              <source src="assets/reels/reel_aerial_pyro_shells.mp4" type="video/mp4">
            </video>
            <div class="reel-card__overlay">
              <div class="reel-card__top">
                <span class="reel-card__badge"><span class="reel-card__badge-live"></span> Live Reel</span>
                <span class="reel-card__duration">0:11</span>
              </div>
              <div class="reel-card__play">
                <svg class="icon" aria-hidden="true"><use href="#i-play"/></svg>
              </div>
              <div class="reel-card__meta">
                <h3 class="reel-card__title">Pyrotechnic Sky Barrage</h3>
                <p class="reel-card__sub">High Altitude Multi-Shot Shells</p>
                <p class="reel-card__venue">Open Grounds, Noida</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
      </div>
    </section>

    <!-- =====================================================================
         5. INTERACTIVE FX LIVE STAGE SIMULATOR
         ===================================================================== -->
    <section class="section section--shaded" id="simulator">
      <div class="container">
        <div class="section-head">
          <span class="section-tag"><svg class="icon" aria-hidden="true"><use href="#i-sparkular"/></svg>Interactive Virtual Experience</span>
          <h2>Live FX Stage Simulator</h2>
          <p>Preview our pyrotechnic effects on a virtual illuminated concert stage before your big event. Click buttons below or tap directly on the stage to fire!</p>
        </div>

        <div class="sim-wrap">
          <div class="sim-header">
            <div class="sim-status">
              <span class="sim-status-dot"></span>
              <span id="sim-status-text">Stage Ready &bull; Select an effect below</span>
            </div>
            <div class="sim-tools">
              <button class="sound-toggle" id="sim-sound-btn" type="button" aria-label="Toggle Simulator Audio">
                <svg class="icon" aria-hidden="true"><use href="#i-sound"/></svg>
                <span id="sim-sound-label">Audio: ON</span>
              </button>
              <button class="btn btn--call btn--sm" id="sim-clear-btn" type="button">Clear Stage</button>
            </div>
          </div>

          <div class="sim-stage-box" id="sim-stage-box">
            <canvas class="sim-canvas" id="sim-canvas" width="960" height="480"></canvas>
            <div class="sim-overlay-hint" id="sim-hint">
              Tap stage anywhere to trigger sparks &bull; Choose effects below
            </div>
          </div>

          <div class="sim-stage-footer">
            <!-- Trigger button rack -->
            <div class="sim-btn-rack">
              <button class="sim-trigger-btn is-active" data-fx="coldpyro" type="button">
                <svg class="icon" aria-hidden="true"><use href="#i-coldpyro"/></svg>
                <span>Cold Pyro Fountains</span>
              </button>
              <button class="sim-trigger-btn" data-fx="lowfog" type="button">
                <svg class="icon" aria-hidden="true"><use href="#i-lowfog"/></svg>
                <span>Low Fog Clouds</span>
              </button>
              <button class="sim-trigger-btn" data-fx="sparkular" type="button">
                <svg class="icon" aria-hidden="true"><use href="#i-sparkular"/></svg>
                <span>Sparkular Waterfall</span>
              </button>
              <button class="sim-trigger-btn" data-fx="fireworks" type="button">
                <svg class="icon" aria-hidden="true"><use href="#i-fireworks"/></svg>
                <span>Sky Fireworks</span>
              </button>
              <button class="sim-trigger-btn" data-fx="smoke" type="button">
                <svg class="icon" aria-hidden="true"><use href="#i-smoke"/></svg>
                <span>Colour Smoke</span>
              </button>
              <button class="sim-trigger-btn" data-fx="confetti" type="button">
                <svg class="icon" aria-hidden="true"><use href="#i-confetti"/></svg>
                <span>Confetti Blast</span>
              </button>
              <button class="sim-trigger-btn sim-trigger-btn--finale" data-fx="finale" type="button">
                <svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg>
                <span>Grand Finale Show</span>
              </button>
            </div>

            <!-- Parameters Sliders -->
            <div class="sim-sliders">
              <div class="sim-control-group">
                <label for="sim-height">
                  <span>Effect Height</span>
                  <span id="sim-height-val">4.0 Meters</span>
                </label>
                <input id="sim-height" type="range" min="20" max="60" value="40">
              </div>

              <div class="sim-control-group">
                <label for="sim-density">
                  <span>Particle Intensity</span>
                  <span id="sim-density-val">High (Grand)</span>
                </label>
                <input id="sim-density" type="range" min="1" max="3" value="2">
              </div>

              <div class="sim-control-group">
                <label for="sim-theme">
                  <span>Stage Lighting</span>
                  <span id="sim-theme-val">Amber &times; Champagne</span>
                </label>
                <input id="sim-theme" type="range" min="1" max="3" value="1">
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         6. INSTANT PACKAGE & COST CALCULATOR
         ===================================================================== -->
    <section class="section" id="calculator">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="section-tag"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg>Instant Transparent Pricing</span>
            <h2>Event Package &amp; Cost Calculator</h2>
          </div>
          <p>Choose your equipment, customize quantities, and get an immediate transparent quotation formatted for WhatsApp.</p>
        </div>

        <div class="calc-layout">
          <!-- Left: Configurator Controls -->
          <div class="calc-box">
            <h3 class="calc-presets-title">Quick Preset Packages</h3>
            <div class="calc-presets">
              <button class="calc-preset-chip is-active" id="preset-varmala" type="button">👑 Royal Varmala Setup</button>
              <button class="calc-preset-chip" id="preset-baraat" type="button">🥁 Grand Baraat Blast</button>
              <button class="calc-preset-chip" id="preset-gala" type="button">✨ Celebrity Stage Gala</button>
              <button class="calc-preset-chip" id="preset-custom" type="button">🛠️ Custom Dream Setup</button>
            </div>

            <!-- Equipment Sliders -->
            <div class="calc-items-grid">
              <!-- Item 1: Cold Pyro -->
              <div class="calc-item">
                <div class="calc-item-top">
                  <div class="calc-item-info">
                    <span class="calc-item-icon"><svg class="icon" aria-hidden="true"><use href="#i-coldpyro"/></svg></span>
                    <div>
                      <h4 class="calc-item-name">Cold Pyro Fountains</h4>
                      <p class="calc-item-rate">&#8377;1,500 per pair (&#8377;750/unit)</p>
                    </div>
                  </div>
                  <span class="calc-item-count-badge" id="count-pyro">8 Units</span>
                </div>
                <input class="calc-item-range" id="range-pyro" type="range" min="0" max="24" step="2" value="8">
              </div>

              <!-- Item 2: Low Fog -->
              <div class="calc-item">
                <div class="calc-item-top">
                  <div class="calc-item-info">
                    <span class="calc-item-icon"><svg class="icon" aria-hidden="true"><use href="#i-lowfog"/></svg></span>
                    <div>
                      <h4 class="calc-item-name">Heavy Low Fog / Dry Ice</h4>
                      <p class="calc-item-rate">&#8377;6,500 per high-capacity machine</p>
                    </div>
                  </div>
                  <span class="calc-item-count-badge" id="count-fog">2 Machines</span>
                </div>
                <input class="calc-item-range" id="range-fog" type="range" min="0" max="4" step="1" value="2">
              </div>

              <!-- Item 3: Sparkular Waterfall -->
              <div class="calc-item">
                <div class="calc-item-top">
                  <div class="calc-item-info">
                    <span class="calc-item-icon"><svg class="icon" aria-hidden="true"><use href="#i-sparkular"/></svg></span>
                    <div>
                      <h4 class="calc-item-name">Sparkular Stage Waterfall</h4>
                      <p class="calc-item-rate">&#8377;4,000 per DMX truss unit</p>
                    </div>
                  </div>
                  <span class="calc-item-count-badge" id="count-sparkular">0 Units</span>
                </div>
                <input class="calc-item-range" id="range-sparkular" type="range" min="0" max="8" step="2" value="0">
              </div>

              <!-- Item 4: Colour Smoke -->
              <div class="calc-item">
                <div class="calc-item-top">
                  <div class="calc-item-info">
                    <span class="calc-item-icon"><svg class="icon" aria-hidden="true"><use href="#i-smoke"/></svg></span>
                    <div>
                      <h4 class="calc-item-name">Daytime Colour Smoke Bombs</h4>
                      <p class="calc-item-rate">&#8377;600 per canister</p>
                    </div>
                  </div>
                  <span class="calc-item-count-badge" id="count-smoke">0 Canisters</span>
                </div>
                <input class="calc-item-range" id="range-smoke" type="range" min="0" max="20" step="2" value="0">
              </div>

              <!-- Item 5: Confetti Cannons -->
              <div class="calc-item">
                <div class="calc-item-top">
                  <div class="calc-item-info">
                    <span class="calc-item-icon"><svg class="icon" aria-hidden="true"><use href="#i-confetti"/></svg></span>
                    <div>
                      <h4 class="calc-item-name">Confetti Blaster Cannons</h4>
                      <p class="calc-item-rate">&#8377;3,500 per pressurized cannon</p>
                    </div>
                  </div>
                  <span class="calc-item-count-badge" id="count-confetti">1 Cannon</span>
                </div>
                <input class="calc-item-range" id="range-confetti" type="range" min="0" max="4" step="1" value="1">
              </div>
            </div>

            <!-- Location & Event Type Selection -->
            <div class="calc-select-row">
              <div class="calc-select-group">
                <label for="calc-city">Event Location</label>
                <select class="calc-select" id="calc-city">
                  <option value="noida" selected>Noida &amp; Greater Noida (Base)</option>
                  <option value="delhi">South &amp; Central Delhi (+&#8377;1,500)</option>
                  <option value="gurugram">Gurugram &amp; Manesar (+&#8377;2,500)</option>
                  <option value="ghaziabad">Ghaziabad &amp; East Delhi (+&#8377;1,000)</option>
                  <option value="destination">Pan-India Destination Wedding (+&#8377;6,000)</option>
                </select>
              </div>

              <div class="calc-select-group">
                <label for="calc-event-type">Celebration Type</label>
                <select class="calc-select" id="calc-event-type">
                  <option value="varmala" selected>Royal Wedding &amp; Varmala</option>
                  <option value="baraat">Baraat Grand Entry</option>
                  <option value="sangeet">Sangeet &amp; Cocktail Night</option>
                  <option value="reception">Grand Reception</option>
                  <option value="corporate">Corporate Gala &amp; Award Show</option>
                  <option value="birthday">Birthday / Private Celebration</option>
                </select>
              </div>
            </div>
          </div>

          <!-- Right: Summary Card -->
          <aside class="calc-summary-card">
            <div class="calc-summary-header">
              <p class="calc-summary-title">Estimated Investment</p>
              <div class="calc-summary-total" id="calc-total-display">&#8377;25,000*</div>
              <p class="calc-summary-note">Includes complete on-site execution crew &bull; All-inclusive</p>
            </div>

            <!-- Breakdown list -->
            <div class="calc-summary-list" id="calc-summary-list">
              <!-- Dynamically populated rows -->
            </div>

            <div class="calc-inclusions">
              <p class="calc-inclusions-title">Package Inclusions</p>
              <ul class="calc-inclusions-list">
                <li><svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>Certified pyrotechnicians on-site</li>
                <li><svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>Wireless digital multi-channel firing console</li>
                <li><svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>Pre-event sound &amp; cue coordination</li>
                <li><svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>Venue safety inspection &amp; clearance</li>
              </ul>
            </div>

            <div class="calc-actions">
              <a class="btn btn--wa btn--lg" id="calc-wa-btn" href="#" target="_blank" rel="noopener">
                <svg class="icon" aria-hidden="true"><use href="#i-whatsapp"/></svg>
                <span>Book This Setup on WhatsApp</span>
              </a>
              <button class="btn btn--call" id="calc-copy-btn" type="button">
                <svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg>
                <span>Copy Quotation Summary</span>
              </button>
            </div>
          </aside>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         7. FILTERABLE SHOWCASE GALLERY
         ===================================================================== -->
    <section class="section" id="gallery">
      <div class="container">
        <div class="section-head">
          <span class="section-tag"><svg class="icon" aria-hidden="true"><use href="#i-star"/></svg>Real Moments We Light Up</span>
          <h2>Luxury Celebration Portfolio</h2>
          <p>Explore real weddings and events lit up by Galaxy Pyrotech Traders across Noida, Delhi NCR &amp; Destination venues.</p>
        </div>

        <!-- Filter Buttons -->
        <div class="gallery-filters">
          <button class="gallery-filter-btn is-active" data-filter="all" type="button">All Showcases (26)</button>
          <button class="gallery-filter-btn" data-filter="varmala" type="button">Royal Stage &amp; Varmala</button>
          <button class="gallery-filter-btn" data-filter="entry" type="button">Baraat &amp; Entries</button>
          <button class="gallery-filter-btn" data-filter="sangeet" type="button">Sangeet &amp; First Dance</button>
          <button class="gallery-filter-btn" data-filter="fireworks" type="button">Sky Fireworks</button>
          <button class="gallery-filter-btn" data-filter="smoke" type="button">Daytime Colour Smoke</button>
          <button class="gallery-filter-btn" data-filter="reels" type="button"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg> Live Reels (4)</button>
        </div>

        <!-- Gallery Grid -->
        <div class="gallery-grid" id="gallery-grid">
          <!-- 0. Palace Varmala & Fireworks -->
          <div class="gallery-card" data-category="varmala" data-index="0">
            <img class="gallery-card__img" src="assets/hero_varmala_palace.jpg" alt="Royal Varmala Mandap Exchange with Cold Pyro, Sky Fireworks and Rose Shower" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Royal Stage &amp; Varmala</span>
              <h3 class="gallery-card__title">Palace Varmala &amp; Fireworks</h3>
              <p class="gallery-card__venue">Grand Temple Stage, Noida</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 1. Fan-Burst Cold Pyro Stage -->
          <div class="gallery-card" data-category="varmala" data-index="1">
            <img class="gallery-card__img" src="assets/cold_pyro_fan_stage.jpg" alt="Spectacular fan-burst cold pyro sparkular fountains on wedding stage" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Royal Stage &amp; Varmala</span>
              <h3 class="gallery-card__title">Fan-Burst Cold Pyro Stage</h3>
              <p class="gallery-card__venue">Grand Celebration Lawn</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 2. Rotating Catherine Wheels -->
          <div class="gallery-card" data-category="varmala" data-index="2">
            <img class="gallery-card__img" src="assets/rotating_catherine_wheels.jpg" alt="Rotating cold pyro Catherine wheels and golden spark waterfalls" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Royal Stage &amp; Varmala</span>
              <h3 class="gallery-card__title">Rotating Catherine Wheels</h3>
              <p class="gallery-card__venue">Floral Stage, Noida</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 3. Royal Bridal Aisle Entry -->
          <div class="gallery-card" data-category="entry" data-index="3">
            <img class="gallery-card__img" src="assets/bridal_entry_sparkular_aisle.jpg" alt="Bride walking down aisle lined with towering vertical sparkular fountains" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Baraat &amp; Entries</span>
              <h3 class="gallery-card__title">Royal Bridal Aisle Entry</h3>
              <p class="gallery-card__venue">Palace Walkway, Greater Noida</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 4. Grand Ghodi Baraat with Flame FX -->
          <div class="gallery-card" data-category="entry" data-index="4">
            <img class="gallery-card__img" src="assets/royal_ghodi_flame_entry.jpg" alt="Groom on white horse on red carpet flanked by vertical flame machines and sparkulars" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Baraat &amp; Entries</span>
              <h3 class="gallery-card__title">Ghodi Baraat with Flame FX</h3>
              <p class="gallery-card__venue">Red Carpet Royal Lawn, Noida</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 5. Royal Carriage Entry with Pyro Guns -->
          <div class="gallery-card" data-category="entry" data-index="5">
            <img class="gallery-card__img" src="assets/baraat_carriage_sparkler_gun.jpg" alt="Groom in vintage floral carriage with handheld sparkler guns and confetti" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Baraat &amp; Entries</span>
              <h3 class="gallery-card__title">Royal Carriage &amp; Pyro Guns</h3>
              <p class="gallery-card__venue">Floral Carriage Procession, Delhi NCR</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 6. Royal Banner Guard of Honour -->
          <div class="gallery-card" data-category="entry" data-index="6">
            <img class="gallery-card__img" src="assets/royal_banner_entry.jpg" alt="Royal groom entry flanked by velvet banners topped with cold pyro fountains" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Baraat &amp; Entries</span>
              <h3 class="gallery-card__title">Royal Banner Guard of Honour</h3>
              <p class="gallery-card__venue">Heritage Palace Courtyard</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 7. Vintage Rolls-Royce Grand Entry -->
          <div class="gallery-card" data-category="entry" data-index="7">
            <img class="gallery-card__img" src="assets/rolls_royce_pyro_entry.jpg" alt="Groom in vintage Rolls-Royce with dual cold pyro sparkler torches" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Baraat &amp; Entries</span>
              <h3 class="gallery-card__title">Vintage Rolls-Royce Entry</h3>
              <p class="gallery-card__venue">Private Estate, Delhi NCR</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 8. Flower Carriage with Cold Spark Wings -->
          <div class="gallery-card" data-category="entry" data-index="8">
            <img class="gallery-card__img" src="assets/royal_carriage_baraat_fan.jpg" alt="Groom in floral carriage with fan-spread cold spark wings" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Baraat &amp; Entries</span>
              <h3 class="gallery-card__title">Floral Carriage Spark Wings</h3>
              <p class="gallery-card__venue">Royal Heritage Lawn</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 9. Mirrored Ramp Bridal Walk -->
          <div class="gallery-card" data-category="entry" data-index="9">
            <img class="gallery-card__img" src="assets/bridal_glass_ramp_pyro.jpg" alt="Bride smiling on glass runway surrounded by sparkling cold fireworks" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Baraat &amp; Entries</span>
              <h3 class="gallery-card__title">Mirrored Ramp Bridal Walk</h3>
              <p class="gallery-card__venue">Grand Banquet Walkway</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 10. Low Fog Dance with Sparkler Arch -->
          <div class="gallery-card" data-category="sangeet" data-index="10">
            <img class="gallery-card__img" src="assets/low_fog_sparkler_entry.jpg" alt="Couple walking through knee-deep low fog with sparkler arch overhead" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Sangeet &amp; First Dance</span>
              <h3 class="gallery-card__title">Low Fog &amp; Sparkler Arch</h3>
              <p class="gallery-card__venue">Grand Ballroom, South Delhi</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 11. Couple Twirl in Dry Ice Clouds -->
          <div class="gallery-card" data-category="sangeet" data-index="11">
            <img class="gallery-card__img" src="assets/low_fog_twirl_dance.jpg" alt="Couple twirling in heavy dry ice clouds under sparkler guns" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Sangeet &amp; First Dance</span>
              <h3 class="gallery-card__title">Twirling On Clouds</h3>
              <p class="gallery-card__venue">Luxury Banquet, Noida</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 12. First Dance in Falling Snow & Sparks -->
          <div class="gallery-card" data-category="sangeet" data-index="12">
            <img class="gallery-card__img" src="assets/ballroom_first_dance_snow.jpg" alt="Couple first dance on mirrored floor with cold spark fountains and falling simulated snow" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Sangeet &amp; First Dance</span>
              <h3 class="gallery-card__title">Dance in Snow &amp; Cold Sparks</h3>
              <p class="gallery-card__venue">Crystal Ballroom, Delhi NCR</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 13. Sangeet Sparkler Gun Tunnel -->
          <div class="gallery-card" data-category="sangeet" data-index="13">
            <img class="gallery-card__img" src="assets/sangeet_pyro_gun_tunnel.jpg" alt="High energy couple dancing through sparkler gun tunnel" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Sangeet &amp; First Dance</span>
              <h3 class="gallery-card__title">Sangeet Sparkler Gun Tunnel</h3>
              <p class="gallery-card__venue">Courtyard Stage, Greater Noida</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 14. Celebration Dance under Sparkler Arches -->
          <div class="gallery-card" data-category="sangeet" data-index="14">
            <img class="gallery-card__img" src="assets/sangeet_gold_couple_dance.jpg" alt="Couple dancing in gold outfits under sparkler arches" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Sangeet &amp; First Dance</span>
              <h3 class="gallery-card__title">Sparkler Arch Celebration</h3>
              <p class="gallery-card__venue">Evening Sangeet Lawn, Noida</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 15. Fairytale Reception Walk -->
          <div class="gallery-card" data-category="sangeet" data-index="15">
            <img class="gallery-card__img" src="assets/reception_fairy_light_arch.jpg" alt="Couple entry under fairy light canopy with sparkler torches" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Sangeet &amp; First Dance</span>
              <h3 class="gallery-card__title">Fairytale Light Canopy Walk</h3>
              <p class="gallery-card__venue">Open Lawn Reception</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 16. Red Carpet Sparkler Gun Walk -->
          <div class="gallery-card" data-category="sangeet" data-index="16">
            <img class="gallery-card__img" src="assets/sangeet_red_lehenga_pyro.jpg" alt="Couple walking hand in hand with sparkler guns forming an arch" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Sangeet &amp; First Dance</span>
              <h3 class="gallery-card__title">Red Carpet Sparkler Walk</h3>
              <p class="gallery-card__venue">Sangeet Night Courtyard</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 17. Royal Mandap Aerial Sky Fireworks -->
          <div class="gallery-card" data-category="fireworks" data-index="17">
            <img class="gallery-card__img" src="assets/sky_fireworks_mandap.jpg" alt="Multi-color aerial fireworks bursting high above floral wedding mandap" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Sky Fireworks</span>
              <h3 class="gallery-card__title">Royal Mandap Sky Fireworks</h3>
              <p class="gallery-card__venue">Destination Heritage Mandap, Rajasthan</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 18. Daytime Rainbow Smoke Mandap -->
          <div class="gallery-card" data-category="smoke" data-index="18">
            <img class="gallery-card__img" src="assets/colour_smoke_rainbow_mandap.jpg" alt="Towering rainbow color smoke plumes shooting into blue sky behind mandap" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Daytime Colour Smoke</span>
              <h3 class="gallery-card__title">Daytime Rainbow Smoke Mandap</h3>
              <p class="gallery-card__venue">Open Garden Lawn, Sector 22 Noida</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 19. Haldi & Holi Color Smoke Celebration -->
          <div class="gallery-card" data-category="smoke" data-index="19">
            <img class="gallery-card__img" src="assets/haldi_procession_smoke.png" alt="Vibrant yellow pink purple smoke clouds dancing at Haldi ceremony" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Daytime Colour Smoke</span>
              <h3 class="gallery-card__title">Haldi &amp; Holi Smoke Carnival</h3>
              <p class="gallery-card__venue">Poolside Lawn, Delhi NCR</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 20. Lake Palace Crescent Varmala Smoke -->
          <div class="gallery-card" data-category="smoke" data-index="20">
            <img class="gallery-card__img" src="assets/lake_palace_colour_smoke.jpg" alt="Circular floral crescent stage overlooking lake with multi-color day smoke" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Daytime Colour Smoke</span>
              <h3 class="gallery-card__title">Lake Palace Crescent Smoke</h3>
              <p class="gallery-card__venue">Lake Palace Terrace, Udaipur</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 21. Beachside Varmala Color Smoke -->
          <div class="gallery-card" data-category="smoke" data-index="21">
            <img class="gallery-card__img" src="assets/colour_smoke_beach_varmala.jpg" alt="Color smoke plumes behind beachfront floral mandap during sunset pheras" loading="lazy">
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Daytime Colour Smoke</span>
              <h3 class="gallery-card__title">Beachside Varmala Color Smoke</h3>
              <p class="gallery-card__venue">Coastal Beach Resort</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg></div>
          </div>

          <!-- 22. Reel 1: Rotating Catherine Wheel (Video) -->
          <div class="gallery-card gallery-card--video" data-category="reels" data-index="22">
            <img class="gallery-card__img" src="assets/reels/reel_varmala_rotating_wheel_poster.jpg" alt="Rotating Sparkular Catherine Wheel during Varmala" loading="lazy">
            <div class="gallery-card__video-badge"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg> 0:19</div>
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Live Video Reel</span>
              <h3 class="gallery-card__title">Rotating Catherine Wheel</h3>
              <p class="gallery-card__venue">Grand Varmala Stage, Noida</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg></div>
          </div>

          <!-- 23. Reel 2: Palace Stage Cold Pyro (Video) -->
          <div class="gallery-card gallery-card--video" data-category="reels" data-index="23">
            <img class="gallery-card__img" src="assets/reels/reel_palace_stage_pyro_poster.jpg" alt="Palace Stage Cold Pyro Fountains" loading="lazy">
            <div class="gallery-card__video-badge"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg> 0:10</div>
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Live Video Reel</span>
              <h3 class="gallery-card__title">Palace Stage Cold Pyro</h3>
              <p class="gallery-card__venue">Heritage Palace Lawn, Delhi NCR</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg></div>
          </div>

          <!-- 24. Reel 3: Midnight Sky Fireworks (Video) -->
          <div class="gallery-card gallery-card--video" data-category="reels" data-index="24">
            <img class="gallery-card__img" src="assets/reels/reel_midnight_sky_fireworks_poster.jpg" alt="Midnight Sky Fireworks Finale" loading="lazy">
            <div class="gallery-card__video-badge"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg> 0:11</div>
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Live Video Reel</span>
              <h3 class="gallery-card__title">Midnight Sky Fireworks</h3>
              <p class="gallery-card__venue">Farmhouse Lawn Celebration</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg></div>
          </div>

          <!-- 25. Reel 4: Pyrotechnic Sky Barrage (Video) -->
          <div class="gallery-card gallery-card--video" data-category="reels" data-index="25">
            <img class="gallery-card__img" src="assets/reels/reel_aerial_pyro_shells_poster.jpg" alt="Pyrotechnic Sky Barrage Shells" loading="lazy">
            <div class="gallery-card__video-badge"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg> 0:11</div>
            <div class="gallery-card__overlay">
              <span class="gallery-card__category">Live Video Reel</span>
              <h3 class="gallery-card__title">Pyrotechnic Sky Barrage</h3>
              <p class="gallery-card__venue">Open Grounds, Noida</p>
            </div>
            <div class="gallery-card__zoom"><svg class="icon" aria-hidden="true"><use href="#i-play"/></svg></div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         8. DIRECT EVENT BOOKING & 24/7 CALLBACK REQUEST
         ===================================================================== -->
    <section class="section section--shaded" id="booking">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="section-tag"><svg class="icon" aria-hidden="true"><use href="#i-clock"/></svg>Open 24 Hours &bull; Direct Service</span>
            <h2>Book Your Event Special Effects</h2>
          </div>
          <p>Fill out the form below to receive a guaranteed response in minutes, or request an instant callback from our chief pyrotechnician.</p>
        </div>

        <div class="booking-card">
          <form class="booking-form" id="direct-booking-form">
            <!-- Name -->
            <div class="form-group">
              <label class="form-label" for="book-name">Your Full Name *</label>
              <input class="form-input" id="book-name" type="text" placeholder="e.g. Rahul Sharma" required>
            </div>

            <!-- WhatsApp Number -->
            <div class="form-group">
              <label class="form-label" for="book-phone">WhatsApp / Phone Number *</label>
              <input class="form-input" id="book-phone" type="tel" placeholder="e.g. +91 98765 43210" required>
            </div>

            <!-- Event Date -->
            <div class="form-group">
              <label class="form-label" for="book-date">Event Date *</label>
              <input class="form-input" id="book-date" type="date" required>
            </div>

            <!-- City / Venue -->
            <div class="form-group">
              <label class="form-label" for="book-venue">Venue &amp; City *</label>
              <input class="form-input" id="book-venue" type="text" placeholder="e.g. Sector 22 Noida / Radisson Blu" required>
            </div>

            <!-- Event Type -->
            <div class="form-group">
              <label class="form-label" for="book-type">Occasion Type</label>
              <select class="form-select" id="book-type">
                <option value="Royal Wedding & Varmala">Royal Wedding &amp; Varmala</option>
                <option value="Baraat Entry">Baraat Grand Entry</option>
                <option value="Sangeet & Cocktail">Sangeet &amp; Cocktail Night</option>
                <option value="Reception">Grand Reception</option>
                <option value="Corporate Event">Corporate Gala</option>
                <option value="Birthday / Anniversary">Birthday / Anniversary</option>
              </select>
            </div>

            <!-- Desired Effects Checklist -->
            <div class="form-group booking-full">
              <label class="form-label">Special Effects Required (Select all that apply)</label>
              <div class="fx-chips-grid">
                <label>
                  <input class="fx-chip-checkbox" type="checkbox" name="fx" value="Cold Pyro" checked>
                  <span class="fx-chip-label">Cold Pyro Fountains</span>
                </label>
                <label>
                  <input class="fx-chip-checkbox" type="checkbox" name="fx" value="Low Fog Dry Ice" checked>
                  <span class="fx-chip-label">Heavy Low Fog (Dry Ice)</span>
                </label>
                <label>
                  <input class="fx-chip-checkbox" type="checkbox" name="fx" value="Sparkular Waterfall">
                  <span class="fx-chip-label">Sparkular Stage Waterfall</span>
                </label>
                <label>
                  <input class="fx-chip-checkbox" type="checkbox" name="fx" value="Sky Fireworks">
                  <span class="fx-chip-label">Sky Fireworks Displays</span>
                </label>
                <label>
                  <input class="fx-chip-checkbox" type="checkbox" name="fx" value="Colour Smoke">
                  <span class="fx-chip-label">Daytime Colour Smoke</span>
                </label>
                <label>
                  <input class="fx-chip-checkbox" type="checkbox" name="fx" value="Confetti Blast" checked>
                  <span class="fx-chip-label">Metallic Confetti Cannons</span>
                </label>
                <label>
                  <input class="fx-chip-checkbox" type="checkbox" name="fx" value="Bubble Machine">
                  <span class="fx-chip-label">Bubble Machines</span>
                </label>
              </div>
            </div>

            <!-- Notes -->
            <div class="form-group booking-full">
              <label class="form-label" for="book-notes">Special Instructions / Timing Notes</label>
              <textarea class="form-textarea" id="book-notes" placeholder="Tell us about your entry song, stage layout, or any venue specific requirements..."></textarea>
            </div>

            <!-- Action Buttons -->
            <div class="booking-actions booking-full">
              <button class="btn btn--wa btn--lg" id="submit-booking-wa" type="button">
                <svg class="icon" aria-hidden="true"><use href="#i-whatsapp"/></svg>
                <span>Send Booking via WhatsApp</span>
              </button>

              <button class="btn btn--primary btn--lg" id="submit-callback" type="button">
                <svg class="icon" aria-hidden="true"><use href="#i-phone"/></svg>
                <span>Request 24/7 Instant Callback</span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         9. CUSTOMER REVIEWS & ADD REVIEW MODAL
         ===================================================================== -->
    <section class="section" id="reviews">
      <div class="container">
        <div class="reviews__header">
          <div>
            <span class="section-tag"><svg class="icon" aria-hidden="true"><use href="#i-star"/></svg>Client Satisfaction</span>
            <h2>Words From Our Couples &amp; Clients</h2>
          </div>
          <button class="btn btn--call" id="open-review-modal-btn" type="button">
            <svg class="icon" aria-hidden="true"><use href="#i-spark"/></svg>
            <span>Write a Client Review</span>
          </button>
        </div>

        <div class="reviews-grid" id="reviews-grid">
          <!-- Dynamically populated / pre-rendered testimonials -->
        </div>
      </div>
    </section>

    <!-- =====================================================================
         10. SEARCHABLE FAQ ACCORDION
         ===================================================================== -->
    <section class="section section--shaded" id="faq">
      <div class="container">
        <div class="section-head">
          <span class="section-tag"><svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>Got Questions?</span>
          <h2>Frequently Asked Questions</h2>
          <p>Everything you need to know about safety, permissions, electricity, and booking timeline.</p>
        </div>

        <!-- Live Search Bar -->
        <div class="faq-search-wrap">
          <svg class="icon faq-search-icon" aria-hidden="true"><use href="#i-search"/></svg>
          <input class="faq-search-input" id="faq-search" type="search" placeholder="Search questions (e.g. indoor safe, dry ice, permissions)...">
        </div>

        <div class="faq-list" id="faq-list">
          <div class="acc" data-faq="indoor cold pyro safety banquet hall">
            <button class="acc__btn" type="button">
              <span>Is Cold Pyro 100% safe for indoor banquet halls?</span>
              <svg class="icon acc__icon" aria-hidden="true"><use href="#i-chevron"/></svg>
            </button>
            <div class="acc__panel">
              <div class="acc__body">
                Yes, absolutely. Our Cold Pyro fountains utilize non-pyrotechnic titanium-zirconium composite granules that operate at an ultra-low temperature (&lt;36&deg;C). You can literally pass your hand through the sparks without feeling heat. It produces zero black smoke, leaves no ash or burnt residue, and is widely approved by major hotel ballrooms and banquet halls across Delhi NCR.
              </div>
            </div>
          </div>

          <div class="acc" data-faq="low fog dry ice trigger smoke alarms optical sensors">
            <button class="acc__btn" type="button">
              <span>Does Low Fog / Dry Ice trigger venue fire alarms?</span>
              <svg class="icon acc__icon" aria-hidden="true"><use href="#i-chevron"/></svg>
            </button>
            <div class="acc__panel">
              <div class="acc__body">
                No. Our heavy low fog machines use pure food-grade solid carbon dioxide (dry ice) submerged in boiling distilled water. Because dry ice vapour is heavier than atmospheric air, it strictly rolls across the floor and remains bounded below knee height. It will not rise to ceiling optical smoke sensors or fire sprinklers.
              </div>
            </div>
          </div>

          <div class="acc" data-faq="who operates the machines on site crew certified technicians">
            <button class="acc__btn" type="button">
              <span>Do you provide certified technicians with the setup?</span>
              <svg class="icon acc__icon" aria-hidden="true"><use href="#i-chevron"/></svg>
            </button>
            <div class="acc__panel">
              <div class="acc__body">
                Yes. Every Galaxy Pyrotech setup is deployed and managed on-site by our trained pyrotechnicians. We coordinate with your event manager, DJ, and family coordinator to trigger the effects down to the exact split-second of your entry song or varmala garland exchange using encrypted wireless digital consoles.
              </div>
            </div>
          </div>

          <div class="acc" data-faq="advance notice booking timeline last minute emergency 24 hours">
            <button class="acc__btn" type="button">
              <span>How much advance notice is needed for booking?</span>
              <svg class="icon acc__icon" aria-hidden="true"><use href="#i-chevron"/></svg>
            </button>
            <div class="acc__panel">
              <div class="acc__body">
                While we recommend booking 2 to 4 weeks in advance for auspicious wedding dates (sava lakshna dates), our base in Sector 22 Noida operates 24 Hours. We regularly accommodate same-day emergency bookings across Noida, Greater Noida, and Delhi NCR subject to crew availability.
              </div>
            </div>
          </div>

          <div class="acc" data-faq="sky fireworks licenses permissions police fire clearances">
            <button class="acc__btn" type="button">
              <span>Do you handle permissions for grand sky fireworks?</span>
              <svg class="icon acc__icon" aria-hidden="true"><use href="#i-chevron"/></svg>
            </button>
            <div class="acc__panel">
              <div class="acc__body">
                Yes. For high-altitude aerial shells and sky fireworks at farmhouses, open lawns, and heritage venues, our team assists in coordinating necessary local administration and venue safety clearances.
              </div>
            </div>
          </div>

          <div class="acc" data-faq="colour smoke bombs stain bridal lehenga clothes non-toxic">
            <button class="acc__btn" type="button">
              <span>Are your colour smoke bombs non-staining for designer clothes?</span>
              <svg class="icon acc__icon" aria-hidden="true"><use href="#i-chevron"/></svg>
            </button>
            <div class="acc__panel">
              <div class="acc__body">
                Yes. We strictly use premium organic, non-toxic corn-starch based colour smoke grenades. When deployed outdoors with normal air clearance, they do not stain bridal lehengas, sherwanis, or skin.
              </div>
            </div>
          </div>

          <div class="acc" data-faq="power electrical generator requirements 15A 16A">
            <button class="acc__btn" type="button">
              <span>What electrical power supply is required at the venue?</span>
              <svg class="icon acc__icon" aria-hidden="true"><use href="#i-chevron"/></svg>
            </button>
            <div class="acc__panel">
              <div class="acc__body">
                Standard 15A / 16A single-phase power points are all that is required for our dry ice machines and sparkulars. Our firing consoles are wireless battery-operated units, ensuring flawless execution even during sudden venue power fluctuations.
              </div>
            </div>
          </div>

          <div class="acc" data-faq="cancellation rescheduling date change policy rain">
            <button class="acc__btn" type="button">
              <span>What is your cancellation and rescheduling policy?</span>
              <svg class="icon acc__icon" aria-hidden="true"><use href="#i-chevron"/></svg>
            </button>
            <div class="acc__panel">
              <div class="acc__body">
                We understand event schedules shift. You can reschedule your booking date with at least 72 hours prior notice at no additional charge, subject to date availability.
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- =====================================================================
         11. CONTACT & GOOGLE MAP SECTION
         ===================================================================== -->
    <section class="section" id="contact">
      <div class="container">
        <div class="section-head section-head--split">
          <div>
            <span class="section-tag"><svg class="icon" aria-hidden="true"><use href="#i-pin"/></svg>Direct Communication</span>
            <h2>Talk To Us About Your Event</h2>
          </div>
          <p>Reach out anytime via phone or WhatsApp. We are available 24/7 to provide instant quotes and plan your setup.</p>
        </div>

        <div class="contact__grid">
          <!-- Contact Details Card -->
          <div class="contact__card">
            <h3>Galaxy Pyrotech Traders</h3>
            <p style="color: var(--soft-beige); margin-top: 0.35rem;">Official Special Effects &amp; Pyrotechnic Specialists</p>

            <div class="contact__items">
              <div class="contact__item">
                <div class="contact__item-icon"><svg class="icon" aria-hidden="true"><use href="#i-phone"/></svg></div>
                <div>
                  <p class="contact__item-label">Phone Hotline</p>
                  <p class="contact__item-val"><a href="tel:+919582673570">+91 95826 73570</a></p>
                </div>
              </div>

              <div class="contact__item">
                <div class="contact__item-icon"><svg class="icon" aria-hidden="true"><use href="#i-whatsapp"/></svg></div>
                <div>
                  <p class="contact__item-label">WhatsApp (24/7 Direct)</p>
                  <p class="contact__item-val"><a href="https://wa.me/919582673570" target="_blank" rel="noopener">+91 95826 73570</a></p>
                </div>
              </div>

              <div class="contact__item">
                <div class="contact__item-icon"><svg class="icon" aria-hidden="true"><use href="#i-mail"/></svg></div>
                <div>
                  <p class="contact__item-label">Official Email</p>
                  <p class="contact__item-val"><a href="mailto:galaxypyrotech@gmail.com">galaxypyrotech@gmail.com</a></p>
                </div>
              </div>

              <div class="contact__item">
                <div class="contact__item-icon"><svg class="icon" aria-hidden="true"><use href="#i-pin"/></svg></div>
                <div>
                  <p class="contact__item-label">Business Address</p>
                  <p class="contact__item-val">
                    <a href="https://www.google.com/maps/search/?api=1&query=12,+Amaltash+Marg,+Chaura+Raghunathpur,+Sector+22,+Noida,+Uttar+Pradesh+201307" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:0.35rem;">
                      <span>12, Amaltash Marg, Chaura Raghunathpur, Sector 22, Noida, UP 201307</span>
                      <svg class="icon" style="width:14px;height:14px;" aria-hidden="true"><use href="#i-spark"/></svg>
                    </a>
                  </p>
                </div>
              </div>

              <div class="contact__item">
                <div class="contact__item-icon"><svg class="icon" aria-hidden="true"><use href="#i-clock"/></svg></div>
                <div>
                  <p class="contact__item-label">Operating Hours</p>
                  <p class="contact__item-val">Open 24 Hours &bull; 7 Days a Week</p>
                </div>
              </div>

              <div class="contact__item">
                <div class="contact__item-icon"><svg class="icon" aria-hidden="true"><use href="#i-instagram"/></svg></div>
                <div>
                  <p class="contact__item-label">Official Instagram</p>
                  <p class="contact__item-val"><a href="https://www.instagram.com/galaxypyrotechtraders" target="_blank" rel="noopener">@galaxypyrotechtraders</a></p>
                </div>
              </div>
            </div>

            <div style="margin-top: 2rem; display: flex; gap: 1rem; flex-wrap: wrap;">
              <a class="btn btn--wa" href="https://wa.me/919582673570?text=Hello%20Galaxy%20Pyrotech%2C%20I%20am%20contacting%20you%20from%20your%20website." target="_blank" rel="noopener">
                <svg class="icon" aria-hidden="true"><use href="#i-whatsapp"/></svg>
                <span>WhatsApp Now</span>
              </a>
              <a class="btn btn--call" href="tel:+919582673570">
                <svg class="icon" aria-hidden="true"><use href="#i-phone"/></svg>
                <span>Direct Call</span>
              </a>
            </div>
          </div>

          <!-- Sector 22 Noida Google Map Embed -->
          <div class="map-box">
            <div class="map-overlay-card">
              <div class="map-overlay-title">
                <span class="brand__logo-frame" style="width:26px;height:26px;padding:2px;">
                  <img class="brand__logo" src="assets/logo.jpg" alt="Galaxy Pyrotech" width="26" height="26">
                </span>
                <span>Galaxy Pyrotech Traders</span>
              </div>
              <p class="map-overlay-address">12, Amaltash Marg, Sector 22, Noida, Uttar Pradesh 201307</p>
              <div class="map-overlay-actions">
                <a class="btn btn--wa btn--sm" href="https://www.google.com/maps/dir/?api=1&destination=12,+Amaltash+Marg,+Chaura+Raghunathpur,+Sector+22,+Noida,+Uttar+Pradesh+201307" target="_blank" rel="noopener">
                  <svg class="icon" aria-hidden="true"><use href="#i-pin"/></svg>
                  <span>Get Directions</span>
                </a>
                <a class="btn btn--call btn--sm" href="https://www.google.com/maps/search/?api=1&query=12,+Amaltash+Marg,+Chaura+Raghunathpur,+Sector+22,+Noida,+Uttar+Pradesh+201307" target="_blank" rel="noopener">
                  <span>Open in Google Maps</span>
                </a>
              </div>
            </div>
            <iframe
              title="Galaxy Pyrotech Traders Sector 22 Noida Location"
              src="https://maps.google.com/maps?q=12,+Amaltash+Marg,+Chaura+Raghunathpur,+Sector+22,+Noida,+Uttar+Pradesh+201307&t=&z=15&ie=UTF8&iwloc=&output=embed"
              loading="lazy"
              allowfullscreen>
            </iframe>
          </div>
        </div>
      </div>
    </section>
  </main>

  <!-- =====================================================================
       12. FOOTER
       ===================================================================== -->
  <footer class="footer">
    <div class="container">
      <div class="footer__grid">
        <div class="footer__brand">
          <a class="brand" href="#home">
            <div class="brand__logo-frame brand__logo-frame--lg">
              <img class="brand__logo" src="assets/logo.jpg" alt="Galaxy Pyrotech logo" width="64" height="64">
            </div>
            <div class="brand__text">
              <span class="brand__name">Galaxy Pyrotech</span>
              <span class="brand__tag">Traders</span>
            </div>
          </a>
          <p>
            Premier special effects for luxury weddings, royal entries, receptions, and corporate celebrations across Noida, Delhi NCR &amp; Pan-India destination events.
          </p>
        </div>

        <div>
          <h4 class="footer__title">Quick Navigation</h4>
          <ul class="footer__list">
            <li><a href="#home">Home</a></li>
            <li><a href="#services">Our Special Effects</a></li>
            <li><a href="#simulator">Live FX Stage Simulator</a></li>
            <li><a href="#calculator">Instant Cost Calculator</a></li>
            <li><a href="#gallery">Showcase Portfolio</a></li>
            <li><a href="#booking">Book Your Event</a></li>
            <li><a href="#faq">Frequently Asked Questions</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer__title">Special Effects</h4>
          <ul class="footer__list">
            <li><a href="#services">Indoor Cold Pyro</a></li>
            <li><a href="#services">Heavy Dry Ice Low Fog</a></li>
            <li><a href="#services">Sparkular Waterfall</a></li>
            <li><a href="#services">Sky Fireworks Shells</a></li>
            <li><a href="#services">Daytime Colour Smoke</a></li>
            <li><a href="#services">Confetti Blasters</a></li>
            <li><a href="#services">Bubble Machines</a></li>
          </ul>
        </div>

        <div>
          <h4 class="footer__title">Contact &amp; Support</h4>
          <ul class="footer__list">
            <li><a href="tel:+919582673570">+91 95826 73570</a></li>
            <li><a href="https://wa.me/919582673570" target="_blank" rel="noopener">WhatsApp 24/7 Available</a></li>
            <li><a href="mailto:galaxypyrotech@gmail.com">galaxypyrotech@gmail.com</a></li>
            <li>Sector 22, Noida, UP 201307</li>
            <li><a href="https://www.instagram.com/galaxypyrotechtraders" target="_blank" rel="noopener">@galaxypyrotechtraders</a></li>
          </ul>
        </div>
      </div>

      <div class="footer__bottom">
        <p>&copy; <span id="current-year">2026</span> Galaxy Pyrotech Traders. All rights reserved.</p>
        <p>12, Amaltash Marg, Sector 22, Noida &bull; galaxypyrotech.com</p>
      </div>
    </div>
  </footer>

  <!-- =====================================================================
       13. MODALS, LIGHTBOX & TOAST
       ===================================================================== -->
  <!-- Fullscreen Lightbox Modal -->
  <div class="lightbox" id="lightbox-modal" role="dialog" aria-modal="true" aria-hidden="true">
    <button class="lightbox__close" id="lightbox-close-btn" type="button" aria-label="Close Lightbox">
      <svg class="icon" aria-hidden="true"><use href="#i-close"/></svg>
    </button>
    <button class="lightbox__nav-btn lightbox__nav-btn--prev" id="lightbox-prev-btn" type="button" aria-label="Previous Image">
      <svg class="icon" aria-hidden="true" style="transform:rotate(90deg)"><use href="#i-chevron"/></svg>
    </button>
    <button class="lightbox__nav-btn lightbox__nav-btn--next" id="lightbox-next-btn" type="button" aria-label="Next Image">
      <svg class="icon" aria-hidden="true" style="transform:rotate(-90deg)"><use href="#i-chevron"/></svg>
    </button>
    <div class="lightbox__content">
      <img class="lightbox__img" id="lightbox-img" src="assets/hero_varmala_palace.jpg" alt="Galaxy Pyrotech showcase preview">
      <video class="lightbox__video" id="lightbox-video" controls playsinline style="display:none;"></video>
      <div class="lightbox__caption">
        <h3 class="lightbox__title" id="lightbox-title"></h3>
        <p class="lightbox__desc" id="lightbox-desc"></p>
        <a class="btn btn--wa btn--sm" id="lightbox-wa-btn" href="#" target="_blank" rel="noopener">
          <svg class="icon" aria-hidden="true"><use href="#i-whatsapp"/></svg>
          <span>Enquire About This Setup</span>
        </a>
      </div>
    </div>
  </div>

  <!-- Write A Review Modal -->
  <div class="modal-backdrop" id="review-modal" role="dialog" aria-modal="true" aria-hidden="true">
    <div class="modal-dialog">
      <button class="modal-close" id="review-modal-close" type="button" aria-label="Close Review Dialog">
        <svg class="icon" aria-hidden="true"><use href="#i-close"/></svg>
      </button>
      <h3 style="margin-bottom: 0.5rem; font-size: 1.4rem;">Share Your Experience</h3>
      <p style="color: var(--soft-beige); font-size: 0.92rem; margin-bottom: 1.5rem;">Your review helps other families and wedding planners create magical moments.</p>

      <form id="add-review-form" style="display: flex; flex-direction: column; gap: 1.2rem;">
        <div class="form-group">
          <label class="form-label" for="rev-name">Your Name *</label>
          <input class="form-input" id="rev-name" type="text" placeholder="e.g. Karan &amp; Riya" required>
        </div>

        <div class="form-group">
          <label class="form-label" for="rev-event">Occasion / Venue *</label>
          <input class="form-input" id="rev-event" type="text" placeholder="e.g. Wedding at Sector 22, Noida" required>
        </div>

        <div class="form-group">
          <label class="form-label">Your Rating *</label>
          <div class="star-rating-select" id="star-rating-select">
            <span class="star-btn is-active" data-val="1"><svg class="icon icon--fill" aria-hidden="true"><use href="#i-star"/></svg></span>
            <span class="star-btn is-active" data-val="2"><svg class="icon icon--fill" aria-hidden="true"><use href="#i-star"/></svg></span>
            <span class="star-btn is-active" data-val="3"><svg class="icon icon--fill" aria-hidden="true"><use href="#i-star"/></svg></span>
            <span class="star-btn is-active" data-val="4"><svg class="icon icon--fill" aria-hidden="true"><use href="#i-star"/></svg></span>
            <span class="star-btn is-active" data-val="5"><svg class="icon icon--fill" aria-hidden="true"><use href="#i-star"/></svg></span>
          </div>
        </div>

        <div class="form-group">
          <label class="form-label" for="rev-text">Your Feedback *</label>
          <textarea class="form-textarea" id="rev-text" placeholder="Tell us how Galaxy Pyrotech made your celebration special..." required></textarea>
        </div>

        <button class="btn btn--primary btn--lg" type="submit" style="margin-top: 0.5rem;">
          <svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>
          <span>Publish Review</span>
        </button>
      </form>
    </div>
  </div>

  <!-- Callback Requested Confirmation Modal -->
  <div class="modal-backdrop" id="callback-modal" role="dialog" aria-modal="true" aria-hidden="true">
    <div class="modal-dialog" style="text-align: center;">
      <button class="modal-close" id="callback-modal-close" type="button" aria-label="Close Dialog">
        <svg class="icon" aria-hidden="true"><use href="#i-close"/></svg>
      </button>
      <div style="width: 64px; height: 64px; border-radius: 50%; background: rgba(196, 164, 130, 0.2); border: 1px solid var(--soft-gold); display: flex; align-items: center; justify-content: center; margin: 0 auto 1.25rem; color: var(--forest-green);">
        <svg class="icon" style="width: 32px; height: 32px;" aria-hidden="true"><use href="#i-check"/></svg>
      </div>
      <h3 style="font-size: 1.5rem; margin-bottom: 0.5rem;">Callback Request Confirmed!</h3>
      <p style="color: var(--soft-beige); margin-bottom: 1.2rem;">Reference Ticket: <strong style="color: var(--light-gold);" id="callback-ref-ticket">#GP-7821</strong></p>
      <p style="color: var(--ivory); font-size: 0.95rem; line-height: 1.6; margin-bottom: 1.8rem;">
        Thank you! Our chief pyrotechnic coordinator at Sector 22, Noida has received your details and will call your phone shortly.
      </p>
      <a class="btn btn--wa btn--lg" id="callback-instant-wa" href="#" target="_blank" rel="noopener">
        <svg class="icon" aria-hidden="true"><use href="#i-whatsapp"/></svg>
        <span>Or Chat Immediately on WhatsApp</span>
      </a>
    </div>
  </div>

  <!-- Toast Notification Bar -->
  <div class="toast-container" id="toast-container" aria-live="polite">
    <div class="toast" id="toast">
      <svg class="icon" aria-hidden="true"><use href="#i-check"/></svg>
      <span id="toast-msg">Quotation copied to clipboard!</span>
    </div>
  </div>

  <!-- Floating 24/7 WhatsApp Pill -->
  <a class="float-wa" href="https://wa.me/919582673570?text=Hello%20Galaxy%20Pyrotech%2C%20I%20am%20inquiring%20about%20event%20effects." target="_blank" rel="noopener" aria-label="WhatsApp 24/7 Live Support">
    <svg class="icon" aria-hidden="true"><use href="#i-whatsapp"/></svg>
    <span>Online 24/7 &bull; Instant Quote</span>
  </a>

  <!-- Mobile Bottom Sticky Dock -->
  <nav class="dock" aria-label="Mobile quick contact">
    <a class="btn btn--call" href="tel:+919582673570">
      <svg class="icon" aria-hidden="true"><use href="#i-phone"/></svg>
      <span>Call Now</span>
    </a>
    <a class="btn btn--wa" href="https://wa.me/919582673570?text=Hello%20Galaxy%20Pyrotech%2C%20I%20would%20like%20to%20inquire%20about%20event%20special%20effects." target="_blank" rel="noopener">
      <svg class="icon" aria-hidden="true"><use href="#i-whatsapp"/></svg>
      <span>WhatsApp</span>
    </a>
  </nav>
'''
