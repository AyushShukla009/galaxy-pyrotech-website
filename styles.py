# CSS styles module for Galaxy Pyrotech Traders
def get_css():
    return '''
  <style>
    /* ==========================================================================
       1. OFFICIAL PALETTE VARIABLES & SYSTEM
       ========================================================================== */
    :root {
      /* Official Color Scheme */
      --black:          #030201; /* Primary Background: Deep Black */
      --black-soft:     #0B0704; /* Navbar / elevated soft black */
      --espresso:       #190B05; /* Secondary Background / Card surface */
      --dark-brown:     #34190A; /* Rich Coffee Brown: depth, secondary overlays */
      --warm-brown:     #592B0E; /* Burnt Brown: Card borders, subtle structure */
      --amber:          #DE8026; /* Primary Accent: Warm Amber (CTAs, highlights) */
      --burnt-gold:     #8C4A1A; /* Secondary Accent: Burnt Gold (lines, glow) */
      --champagne:      #CBA482; /* Gold Highlight: Champagne Gold (icons, accents) */
      --light-gold:     #E3C9A8; /* Light Gold: Warm Champagne (glints, highlights) */
      --ivory:          #F0EEEC; /* Primary Text: Warm Ivory */
      --soft-beige:     #C5B6A7; /* Secondary Text: Soft Beige */
      --muted-brown:    rgba(203, 164, 130, 0.4);

      /* Semantic Tokens */
      --bg-primary:     var(--black);
      --bg-secondary:   var(--espresso);
      --bg-card:        var(--espresso);
      --bg-elevated:    var(--dark-brown);
      --border-color:   var(--warm-brown);
      --border-glow:    rgba(222, 128, 38, 0.35);
      --accent:         var(--amber);
      --accent-hover:   #ea8e35;
      --accent-glow:    rgba(222, 128, 38, 0.45);
      --gold:           var(--champagne);
      --text:           var(--ivory);
      --text-muted:     var(--soft-beige);

      /* Typography */
      --font-display:   "Sora", ui-sans-serif, system-ui, -apple-system, sans-serif;
      --font-body:      "Manrope", ui-sans-serif, system-ui, -apple-system, sans-serif;

      /* Dimensions & Transitions */
      --header-h:       66px;
      --gutter:         16px;
      --container:      1240px;
      --radius-sm:      8px;
      --radius:         16px;
      --radius-lg:      24px;
      --ease:           cubic-bezier(0.16, 1, 0.3, 1);
    }

    @media (min-width: 768px) {
      :root {
        --gutter: 32px;
        --header-h: 84px;
      }
    }

    /* ==========================================================================
       2. RESET & BASE
       ========================================================================== */
    *, *::before, *::after {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    html {
      scroll-behavior: smooth;
      scroll-padding-top: calc(var(--header-h) + 16px);
      -webkit-text-size-adjust: 100%;
      background-color: var(--black);
      color: var(--ivory);
      overflow-x: hidden;
      width: 100%;
      max-width: 100%;
    }

    body {
      min-height: 100vh;
      width: 100%;
      max-width: 100%;
      overflow-x: hidden;
      font-family: var(--font-body);
      font-size: 1rem;
      line-height: 1.6;
      background: var(--black);
      color: var(--ivory);
      -webkit-font-smoothing: antialiased;
      position: relative;
    }

    main {
      width: 100%;
      max-width: 100%;
      display: block;
      overflow-x: hidden;
    }

    .container,
    .hero__inner,
    .hero__copy,
    .hero__visual-wrap,
    .hero__visual-card,
    .trust__grid,
    .trust__cell,
    .services__grid,
    .service-card,
    .sim-wrap,
    .calc-layout,
    .calc-box,
    .calc-summary-card,
    .gallery-grid,
    .gallery-card,
    .booking-card,
    .booking-form,
    .reviews-grid,
    .review-card,
    .faq-list,
    .contact__grid,
    .contact__card,
    .map-box,
    .footer__grid {
      min-width: 0;
      max-width: 100%;
      box-sizing: border-box;
    }

    @media (max-width: 767px) {
      body {
        padding-bottom: calc(74px + env(safe-area-inset-bottom, 0px));
      }
    }

    body.no-scroll {
      overflow: hidden;
    }

    img, svg, video {
      display: block;
      max-width: 100%;
    }

    a {
      color: inherit;
      text-decoration: none;
      transition: color 0.2s ease, opacity 0.2s ease;
    }

    button, input, select, textarea {
      font: inherit;
      color: inherit;
      background: transparent;
      border: none;
      outline: none;
    }

    button {
      cursor: pointer;
    }

    ul, ol {
      list-style: none;
    }

    .sr-only {
      position: absolute;
      width: 1px;
      height: 1px;
      padding: 0;
      margin: -1px;
      overflow: hidden;
      clip: rect(0, 0, 0, 0);
      white-space: nowrap;
      border: 0;
    }

    .container {
      width: 100%;
      max-width: var(--container);
      margin-left: auto;
      margin-right: auto;
      padding-left: var(--gutter);
      padding-right: var(--gutter);
      box-sizing: border-box;
    }

    /* ==========================================================================
       3. AMBIENT SKY & BACKGROUND PARTICLES
       ========================================================================== */
    .sky {
      position: fixed;
      inset: 0;
      pointer-events: none;
      z-index: 0;
      overflow: hidden;
    }

    .sky__glow {
      position: absolute;
      border-radius: 50%;
      filter: blur(100px);
      opacity: 0.14;
      pointer-events: none;
    }

    .sky__glow--1 {
      top: -10%;
      right: 10%;
      width: 50vw;
      height: 50vw;
      background: radial-gradient(circle, var(--amber) 0%, transparent 70%);
    }

    .sky__glow--2 {
      top: 40%;
      left: -15%;
      width: 60vw;
      height: 60vw;
      background: radial-gradient(circle, var(--burnt-gold) 0%, transparent 70%);
      opacity: 0.10;
    }

    .sky__glow--3 {
      bottom: -10%;
      right: -10%;
      width: 55vw;
      height: 55vw;
      background: radial-gradient(circle, var(--dark-brown) 0%, transparent 70%);
      opacity: 0.20;
    }

    /* Ambient embers container */
    .hero__sparks {
      position: absolute;
      inset: 0;
      pointer-events: none;
      overflow: hidden;
      z-index: 1;
    }

    .spark {
      position: absolute;
      bottom: -10px;
      width: var(--size, 2.4px);
      height: var(--size, 2.4px);
      border-radius: 50%;
      background: var(--light-gold);
      box-shadow: 0 0 6px 1px var(--amber);
      animation: floatSpark var(--dur, 10s) linear infinite;
      animation-delay: var(--delay, 0s);
    }

    @keyframes floatSpark {
      0% {
        transform: translate3d(0, 0, 0);
        opacity: 0;
      }
      10% {
        opacity: 0.9;
      }
      90% {
        opacity: 0.7;
      }
      100% {
        transform: translate3d(var(--dx, 20px), -100vh, 0);
        opacity: 0;
      }
    }

    /* ==========================================================================
       4. TYPOGRAPHY & SECTION HEADINGS
       ========================================================================== */
    h1, h2, h3, h4, h5, h6 {
      font-family: var(--font-display);
      font-weight: 700;
      line-height: 1.2;
      color: var(--ivory);
    }

    .section-head {
      margin-bottom: 3rem;
      text-align: center;
      position: relative;
    }

    .section-head--split {
      text-align: left;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    @media (min-width: 768px) {
      .section-head--split {
        flex-direction: row;
        justify-content: space-between;
        align-items: flex-end;
      }
      .section-head--split h2 {
        max-width: 60%;
      }
      .section-head--split p {
        max-width: 35%;
        margin-bottom: 0.3rem;
      }
    }

    .section-tag {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--amber);
      margin-bottom: 0.75rem;
      background: rgba(222, 128, 38, 0.1);
      padding: 0.35rem 0.85rem;
      border-radius: 999px;
      border: 1px solid rgba(222, 128, 38, 0.3);
      max-width: 100%;
      box-sizing: border-box;
      white-space: normal;
      text-align: center;
    }

    .section-head h2 {
      font-size: clamp(1.65rem, 5.5vw, 3rem);
      letter-spacing: -0.02em;
      margin-bottom: 0.8rem;
    }

    .section-head p {
      color: var(--soft-beige);
      font-size: 1.06rem;
      max-width: 680px;
      margin-left: auto;
      margin-right: auto;
    }

    .section-head--split p {
      margin-left: 0;
      margin-right: 0;
    }

    .section {
      padding-top: 5.5rem;
      padding-bottom: 5.5rem;
      position: relative;
      z-index: 1;
    }

    .section--tight {
      padding-top: 3.5rem;
      padding-bottom: 3.5rem;
    }

    @media (max-width: 767px) {
      .section {
        padding-top: 3.5rem;
        padding-bottom: 3.5rem;
      }
      .section--tight {
        padding-top: 2rem;
        padding-bottom: 2rem;
      }
      .section-head {
        margin-bottom: 2rem;
      }
      .section-head p {
        font-size: 0.94rem;
      }
    }

    .section--shaded {
      background: linear-gradient(180deg, transparent 0%, rgba(25, 11, 5, 0.6) 50%, transparent 100%);
    }

    /* ==========================================================================
       5. BUTTONS & UI CONTROLS
       ========================================================================== */
    .btn {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.6rem;
      padding: 0.85rem 1.6rem;
      border-radius: 999px;
      font-family: var(--font-display);
      font-size: 0.95rem;
      font-weight: 600;
      letter-spacing: 0.01em;
      white-space: nowrap;
      transition: all 0.25s var(--ease);
      cursor: pointer;
      position: relative;
      user-select: none;
    }

    .btn--primary, .btn--call {
      background: linear-gradient(180deg, var(--light-gold) 0%, var(--amber) 100%);
      color: #030201;
      font-weight: 700;
      border: 1px solid rgba(255, 255, 255, 0.25);
      box-shadow: 0 6px 24px rgba(222, 128, 38, 0.4);
    }

    .btn--primary:hover, .btn--call:hover {
      box-shadow: 0 8px 32px rgba(222, 128, 38, 0.6);
      transform: translateY(-2px);
      color: #000;
    }

    /* WhatsApp = Espresso/Charcoal with warm Champagne Gold border */
    .btn--wa {
      background: linear-gradient(180deg, var(--espresso) 0%, #0B0704 100%);
      color: var(--ivory);
      font-weight: 700;
      border: 1px solid rgba(203, 164, 130, 0.5);
      box-shadow: 0 6px 20px rgba(0, 0, 0, 0.6);
    }

    .btn--wa svg {
      color: var(--amber);
    }

    .btn--wa:hover {
      background: linear-gradient(180deg, var(--dark-brown) 0%, var(--espresso) 100%);
      border-color: var(--amber);
      color: #fff;
      box-shadow: 0 8px 28px rgba(222, 128, 38, 0.35);
      transform: translateY(-2px);
    }

    .btn--outline {
      border: 1px solid var(--border-color);
      color: var(--ivory);
      background: rgba(25, 11, 5, 0.4);
    }

    .btn--outline:hover {
      border-color: var(--amber);
      color: var(--amber);
      transform: translateY(-2px);
    }

    .btn--sm {
      padding: 0.55rem 1.1rem;
      font-size: 0.85rem;
    }

    .btn--lg {
      padding: 1.05rem 2.2rem;
      font-size: 1.05rem;
    }

    .btn--pulse {
      animation: pulseGlow 2.5s infinite;
    }

    @keyframes pulseGlow {
      0%, 100% {
        box-shadow: 0 4px 20px rgba(222, 128, 38, 0.35);
      }
      50% {
        box-shadow: 0 4px 32px rgba(222, 128, 38, 0.65);
      }
    }

    .icon {
      width: 1.25rem;
      height: 1.25rem;
      fill: none;
      stroke: currentColor;
      stroke-width: 2;
      stroke-linecap: round;
      stroke-linejoin: round;
      flex-shrink: 0;
    }

    .icon--fill {
      fill: currentColor;
      stroke: none;
    }

    /* ==========================================================================
       6. HEADER & NAVIGATION
       ========================================================================== */
    .header {
      position: sticky;
      top: 0;
      left: 0;
      width: 100%;
      height: var(--header-h);
      z-index: 100;
      transition: background 0.3s ease, border-color 0.3s ease, backdrop-filter 0.3s ease;
      background: rgba(3, 2, 1, 0.88);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid rgba(89, 43, 14, 0.35);
    }

    .header.is-scrolled {
      background: rgba(11, 7, 4, 0.96);
      border-bottom-color: rgba(222, 128, 38, 0.25);
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.6);
    }

    .header .container {
      width: 100%;
      max-width: 1360px;
      padding-left: var(--gutter);
      padding-right: var(--gutter);
      box-sizing: border-box;
    }

    .header__bar {
      display: flex;
      align-items: center;
      justify-content: space-between;
      height: 100%;
      width: 100%;
      box-sizing: border-box;
    }

    /* Official Logo Frame */
    .brand {
      display: inline-flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      flex-shrink: 0;
    }

    .brand__logo-frame {
      width: 46px;
      height: 46px;
      border-radius: 50%;
      padding: 2px;
      background: linear-gradient(135deg, var(--light-gold) 0%, var(--amber) 50%, var(--dark-brown) 100%);
      box-shadow: 0 0 14px rgba(222, 128, 38, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      flex-shrink: 0;
    }

    .brand__logo-frame--lg {
      width: 64px;
      height: 64px;
      padding: 3px;
    }

    .brand__logo {
      width: 100%;
      height: 100%;
      border-radius: 50%;
      object-fit: cover;
      display: block;
    }

    .brand__text {
      display: flex;
      flex-direction: column;
    }

    .brand__name {
      font-family: var(--font-display);
      font-weight: 800;
      font-size: 1.15rem;
      letter-spacing: -0.01em;
      color: var(--ivory);
      line-height: 1.15;
      white-space: nowrap;
    }

    .brand__tag {
      font-size: 0.72rem;
      color: var(--champagne);
      font-weight: 500;
      letter-spacing: 0.04em;
      white-space: nowrap;
    }

    @media (max-width: 1240px) {
      .brand__tag {
        display: none;
      }
    }

    .nav {
      display: none;
    }

    @media (min-width: 1140px) {
      .nav {
        display: flex;
        align-items: center;
        justify-content: center;
        flex: 1;
        margin: 0 1.5rem;
        min-width: 0;
      }

      .nav__list {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: clamp(0.75rem, 1.4vw, 1.8rem);
        margin: 0;
        padding: 0;
        list-style: none;
      }

      .nav__list li {
        display: inline-flex;
      }

      .nav__list a {
        font-family: var(--font-display);
        font-size: 0.88rem;
        font-weight: 600;
        color: var(--soft-beige);
        position: relative;
        padding: 0.4rem 0.2rem;
        white-space: nowrap;
        letter-spacing: 0.01em;
        transition: color 0.2s ease;
      }

      .nav__list a:hover,
      .nav__list a[aria-current="true"] {
        color: var(--ivory);
      }

      .nav__list a[aria-current="true"]::after {
        content: "";
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 100%;
        height: 2px;
        background: var(--amber);
        border-radius: 999px;
      }
    }

    .header__actions {
      display: inline-flex;
      align-items: center;
      gap: 0.65rem;
      flex-shrink: 0;
    }

    /* Sound FX Toggle */
    .sound-toggle {
      display: inline-flex;
      align-items: center;
      justify-content: center;
      gap: 0.4rem;
      padding: 0.45rem 0.85rem;
      border-radius: 999px;
      font-size: 0.8rem;
      font-weight: 700;
      white-space: nowrap;
      flex-shrink: 0;
      background: rgba(89, 43, 14, 0.4);
      border: 1px solid var(--warm-brown);
      color: var(--champagne);
      transition: all 0.2s ease;
      user-select: none;
      cursor: pointer;
    }

    .sound-toggle:hover {
      background: rgba(89, 43, 14, 0.65);
      border-color: var(--amber);
      color: #fff;
    }

    .sound-toggle.is-active {
      background: rgba(222, 128, 38, 0.25);
      border-color: var(--amber);
      color: var(--light-gold);
    }

    @media (max-width: 768px) {
      .header .btn--call,
      .header .btn--wa {
        display: none !important;
      }
      .sound-toggle .sound-label {
        display: none;
      }
      .sound-toggle {
        padding: 0;
        width: 40px;
        height: 40px;
        border-radius: 50%;
      }
      .brand__name {
        font-size: 1.05rem;
      }
      .brand__logo-frame {
        width: 40px;
        height: 40px;
      }
    }

    .nav__toggle {
      display: flex;
      align-items: center;
      justify-content: center;
      width: 40px;
      height: 40px;
      border-radius: 50%;
      border: 1px solid var(--warm-brown);
      background: rgba(25, 11, 5, 0.6);
      color: var(--ivory);
      flex-shrink: 0;
    }

    @media (max-width: 1139px) {
      .nav__toggle {
        display: flex !important;
      }
      .nav {
        display: none !important;
      }
    }

    @media (min-width: 1140px) {
      .nav__toggle {
        display: none !important;
      }
    }

    .nav__toggle .i-close { display: none; }
    .header.menu-open .nav__toggle .i-menu { display: none; }
    .header.menu-open .nav__toggle .i-close { display: block; }

    /* Mobile Drawer */
    .mobile-menu {
      position: fixed;
      top: var(--header-h);
      left: 0;
      right: 0;
      bottom: 0;
      background: rgba(3, 2, 1, 0.98);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
      z-index: 99;
      padding: 1.75rem var(--gutter) calc(5.5rem + env(safe-area-inset-bottom, 0px));
      display: flex;
      flex-direction: column;
      gap: 1.5rem;
      overflow-y: auto;
      -webkit-overflow-scrolling: touch;
      transform: translateY(-100%);
      opacity: 0;
      pointer-events: none;
      transition: transform 0.35s var(--ease), opacity 0.35s ease;
    }

    .mobile-menu.is-open {
      transform: translateY(0);
      opacity: 1;
      pointer-events: auto;
    }

    .mobile-menu__list {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .mobile-menu__list a {
      font-family: var(--font-display);
      font-size: 1.4rem;
      font-weight: 700;
      color: var(--ivory);
      display: block;
      border-bottom: 1px solid rgba(89, 43, 14, 0.3);
      padding-bottom: 0.75rem;
    }

    .mobile-menu__actions {
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      margin-top: 1rem;
    }

    /* ==========================================================================
       7. HERO SECTION
       ========================================================================= */
    .hero {
      position: relative;
      padding-top: calc(var(--header-h) * 0.4);
      padding-bottom: 5.5rem;
      overflow: hidden;
      min-height: calc(100vh - var(--header-h));
      display: flex;
      align-items: center;
      width: 100%;
    }

    .hero__inner {
      display: grid;
      grid-template-columns: 1fr;
      gap: 3rem;
      align-items: center;
      position: relative;
      z-index: 2;
      width: 100%;
      box-sizing: border-box;
    }

    @media (min-width: 992px) {
      .hero__inner {
        grid-template-columns: 1.15fr 0.85fr;
        gap: 4rem;
      }
    }

    .hero__copy {
      max-width: 650px;
      width: 100%;
      box-sizing: border-box;
    }

    .hero__badge {
      display: inline-flex;
      align-items: center;
      gap: 0.6rem;
      padding: 0.4rem 1rem;
      border-radius: 999px;
      font-size: 0.85rem;
      font-weight: 700;
      letter-spacing: 0.08em;
      text-transform: uppercase;
      color: var(--light-gold);
      background: rgba(52, 25, 10, 0.6);
      border: 1px solid rgba(222, 128, 38, 0.4);
      margin-bottom: 1.5rem;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.3);
    }

    .hero__badge-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--amber);
      box-shadow: 0 0 8px var(--amber);
    }

    .hero__title {
      font-size: clamp(1.65rem, 4.5vw, 4.2rem);
      font-weight: 800;
      letter-spacing: -0.03em;
      line-height: 1.08;
      margin-bottom: 1.4rem;
      color: var(--ivory);
    }

    @media (max-width: 767px) {
      .hero {
        display: block !important;
        width: 100% !important;
        padding-top: 1.8rem;
        padding-bottom: 3rem;
        min-height: auto;
      }
      .hero__inner {
        display: flex !important;
        flex-direction: column !important;
        width: 100% !important;
        gap: 2.2rem;
      }
      .hero__copy {
        width: 100% !important;
        max-width: 100% !important;
      }
      .hero__title {
        font-size: clamp(1.5rem, 5.8vw, 1.85rem);
        line-height: 1.2;
        word-break: break-word;
        overflow-wrap: break-word;
      }
      .hero__badge {
        font-size: 0.72rem;
        padding: 0.35rem 0.75rem;
        max-width: 100%;
        white-space: normal;
        text-align: center;
      }
      .hero__lead {
        font-size: 0.98rem;
      }
      .hero__actions {
        display: flex;
        flex-direction: column;
        width: 100% !important;
      }
      .hero__actions .btn {
        width: 100% !important;
      }
      .hero__assure {
        gap: 0.85rem;
      }
      .hero__assure-item {
        font-size: 0.82rem;
      }
      .hero__visual-wrap {
        order: -1;
        width: 100% !important;
        margin-bottom: 0.5rem;
      }
      .hero__visual-card {
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box;
      }
      .hero__visual-img {
        width: 100% !important;
        height: clamp(220px, 55vw, 320px);
      }
    }

    .hero__title-accent {
      background: linear-gradient(135deg, var(--light-gold) 0%, var(--amber) 70%, var(--burnt-gold) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero__lead {
      font-size: clamp(1.05rem, 1.4vw, 1.25rem);
      line-height: 1.6;
      color: var(--soft-beige);
      margin-bottom: 1.5rem;
    }

    .hero__area {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 0.92rem;
      color: var(--champagne);
      font-weight: 600;
      margin-bottom: 2rem;
    }

    .hero__actions {
      display: flex;
      flex-wrap: wrap;
      gap: 1rem;
      margin-bottom: 2.2rem;
    }

    .hero__assure {
      display: flex;
      flex-wrap: wrap;
      gap: 1.5rem;
      padding-top: 1.5rem;
      border-top: 1px solid rgba(89, 43, 14, 0.4);
    }

    .hero__assure-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--soft-beige);
    }

    .hero__assure-item svg {
      color: var(--amber);
    }

    /* Hero Visual Card / Constellation */
    .hero__visual-wrap {
      position: relative;
      display: flex;
      justify-content: center;
      align-items: center;
    }

    .hero__visual-card {
      position: relative;
      width: 100%;
      max-width: 480px;
      border-radius: var(--radius-lg);
      padding: 10px;
      background: linear-gradient(145deg, rgba(89, 43, 14, 0.4) 0%, rgba(25, 11, 5, 0.8) 100%);
      border: 1px solid rgba(203, 164, 130, 0.25);
      box-shadow: 0 20px 50px rgba(0, 0, 0, 0.7), 0 0 30px rgba(222, 128, 38, 0.15);
      overflow: hidden;
    }

    .hero__visual-img {
      width: 100%;
      height: 380px;
      object-fit: cover;
      border-radius: calc(var(--radius-lg) - 6px);
      filter: brightness(0.95);
    }

    .hero__visual-caption {
      position: absolute;
      bottom: 24px;
      left: 24px;
      right: 24px;
      padding: 1.2rem;
      background: rgba(11, 7, 4, 0.85);
      backdrop-filter: blur(12px);
      border-radius: var(--radius);
      border: 1px solid rgba(222, 128, 38, 0.3);
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .hero__visual-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--ivory);
    }

    .hero__visual-sub {
      font-size: 0.8rem;
      color: var(--champagne);
    }

    /* ==========================================================================
       8. TRUST BAR
       ========================================================================== */
    .trust__grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.5rem;
    }

    @media (min-width: 640px) {
      .trust__grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (min-width: 1024px) {
      .trust__grid {
        grid-template-columns: repeat(4, 1fr);
      }
    }

    .trust__cell {
      background: rgba(25, 11, 5, 0.6);
      border: 1px solid var(--warm-brown);
      border-radius: var(--radius);
      padding: 1.6rem;
      transition: all 0.3s var(--ease);
      position: relative;
    }

    .trust__cell:hover {
      border-color: var(--amber);
      transform: translateY(-3px);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.4), 0 0 16px rgba(222, 128, 38, 0.15);
    }

    .trust__icon {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: rgba(52, 25, 10, 0.8);
      border: 1px solid rgba(222, 128, 38, 0.35);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--amber);
      margin-bottom: 1rem;
    }

    .trust__cell h3 {
      font-size: 1.05rem;
      margin-bottom: 0.4rem;
      color: var(--ivory);
    }

    .trust__cell p {
      font-size: 0.88rem;
      color: var(--soft-beige);
      line-height: 1.5;
    }

    /* ==========================================================================
       9. SERVICES SECTION
       ========================================================================== */
    .services__grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.8rem;
    }

    @media (min-width: 640px) {
      .services__grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (min-width: 1024px) {
      .services__grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .service-card {
      background: var(--espresso);
      border: 1px solid var(--warm-brown);
      border-radius: var(--radius);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all 0.3s var(--ease);
      position: relative;
    }

    .service-card:hover {
      border-color: var(--amber);
      transform: translateY(-4px);
      box-shadow: 0 16px 36px rgba(0, 0, 0, 0.6), 0 0 20px rgba(222, 128, 38, 0.18);
    }

    .service-card__media {
      position: relative;
      height: 220px;
      overflow: hidden;
      background: #000;
    }

    .service-card__img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.5s var(--ease);
    }

    .service-card:hover .service-card__img {
      transform: scale(1.06);
    }

    .service-card__badge {
      position: absolute;
      top: 14px;
      right: 14px;
      background: rgba(3, 2, 1, 0.85);
      backdrop-filter: blur(8px);
      padding: 0.3rem 0.75rem;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 700;
      color: var(--light-gold);
      border: 1px solid rgba(203, 164, 130, 0.3);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .service-card__body {
      padding: 1.6rem;
      display: flex;
      flex-direction: column;
      flex: 1;
    }

    .service-card__header {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      margin-bottom: 0.75rem;
    }

    .service-card__icon {
      width: 36px;
      height: 36px;
      border-radius: 10px;
      background: rgba(52, 25, 10, 0.8);
      border: 1px solid rgba(222, 128, 38, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--amber);
      flex-shrink: 0;
    }

    .service-card h3 {
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--ivory);
    }

    .service-card p {
      font-size: 0.92rem;
      color: var(--soft-beige);
      line-height: 1.55;
      margin-bottom: 1.25rem;
      flex: 1;
    }

    .service-card__specs {
      display: flex;
      flex-wrap: wrap;
      gap: 0.5rem;
      margin-bottom: 1.4rem;
      padding-top: 0.85rem;
      border-top: 1px solid rgba(89, 43, 14, 0.35);
    }

    .service-card__spec {
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--champagne);
      background: rgba(52, 25, 10, 0.4);
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      border: 1px solid rgba(89, 43, 14, 0.5);
    }

    .service-card__actions {
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 0.6rem;
    }

    /* ==========================================================================
       10. INTERACTIVE FX LIVE STAGE SIMULATOR
       ========================================================================== */
    .sim-wrap {
      background: linear-gradient(160deg, #190B05 0%, #0B0704 60%, #030201 100%);
      border: 1px solid rgba(222, 128, 38, 0.3);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: 0 24px 60px rgba(0, 0, 0, 0.8), 0 0 30px rgba(222, 128, 38, 0.12);
      position: relative;
    }

    .sim-header {
      padding: 1.25rem 1.6rem;
      background: rgba(11, 7, 4, 0.9);
      border-bottom: 1px solid rgba(89, 43, 14, 0.5);
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
    }

    .sim-status {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 0.88rem;
      font-weight: 700;
      color: var(--light-gold);
    }

    .sim-status-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #DE8026;
      box-shadow: 0 0 10px #DE8026;
      animation: pulseDot 1.5s infinite;
    }

    @keyframes pulseDot {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.4; transform: scale(0.85); }
    }

    .sim-tools {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .sim-stage-box {
      position: relative;
      background: #000;
      width: 100%;
      height: 480px;
      max-height: 60vh;
      overflow: hidden;
      cursor: crosshair;
    }

    @media (max-width: 768px) {
      .sim-stage-box {
        height: 290px;
        max-height: 42vh;
      }
      .sim-header {
        padding: 0.85rem 1rem;
      }
      .sim-stage-footer {
        padding: 1rem;
        gap: 1rem;
      }
      .sim-btn-rack {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 0.5rem;
      }
      .sim-trigger-btn {
        padding: 0.55rem 0.75rem;
        font-size: 0.82rem;
        justify-content: center;
        white-space: nowrap;
      }
      .sim-trigger-btn--finale {
        grid-column: 1 / -1;
      }
      .sim-sliders {
        gap: 0.85rem;
      }
    }

    .sim-canvas {
      width: 100%;
      height: 100%;
      display: block;
    }

    .sim-overlay-hint {
      position: absolute;
      top: 12px;
      left: 12px;
      right: 12px;
      max-width: calc(100% - 24px);
      width: auto;
      box-sizing: border-box;
      background: rgba(3, 2, 1, 0.75);
      backdrop-filter: blur(8px);
      padding: 0.35rem 0.75rem;
      border-radius: 999px;
      font-size: 0.76rem;
      font-weight: 600;
      color: var(--champagne);
      border: 1px solid rgba(203, 164, 130, 0.25);
      pointer-events: none;
      transition: opacity 0.5s ease;
      text-align: center;
      white-space: normal;
    }

    .sim-stage-footer {
      padding: 1.4rem 1.6rem;
      background: rgba(25, 11, 5, 0.85);
      border-top: 1px solid rgba(89, 43, 14, 0.4);
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
    }

    .sim-btn-rack {
      display: flex;
      flex-wrap: wrap;
      gap: 0.65rem;
      justify-content: center;
    }

    .sim-trigger-btn {
      display: inline-flex;
      align-items: center;
      gap: 0.5rem;
      padding: 0.65rem 1.2rem;
      border-radius: 999px;
      font-size: 0.88rem;
      font-weight: 700;
      background: rgba(52, 25, 10, 0.6);
      border: 1px solid var(--warm-brown);
      color: var(--ivory);
      transition: all 0.2s ease;
    }

    .sim-trigger-btn:hover {
      background: rgba(89, 43, 14, 0.7);
      border-color: var(--amber);
      color: #fff;
      transform: translateY(-2px);
    }

    .sim-trigger-btn.is-active {
      background: linear-gradient(135deg, var(--amber) 0%, var(--burnt-gold) 100%);
      border-color: var(--light-gold);
      color: #fff;
      box-shadow: 0 4px 16px rgba(222, 128, 38, 0.4);
    }

    .sim-trigger-btn--finale {
      background: linear-gradient(135deg, #DE8026 0%, #8C4A1A 100%);
      border-color: #E3C9A8;
      color: #fff;
      font-weight: 800;
    }

    .sim-sliders {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.2rem;
      padding-top: 1rem;
      border-top: 1px solid rgba(89, 43, 14, 0.35);
    }

    @media (min-width: 640px) {
      .sim-sliders {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .sim-control-group {
      display: flex;
      flex-direction: column;
      gap: 0.4rem;
    }

    .sim-control-group label {
      display: flex;
      justify-content: space-between;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--champagne);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .sim-control-group input[type="range"] {
      width: 100%;
      height: 6px;
      border-radius: 999px;
      background: rgba(52, 25, 10, 0.8);
      outline: none;
      -webkit-appearance: none;
    }

    .sim-control-group input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: var(--amber);
      border: 2px solid #fff;
      box-shadow: 0 0 10px var(--amber);
      cursor: pointer;
    }

    /* ==========================================================================
       11. PACKAGE & COST CALCULATOR
       ========================================================================== */
    .calc-layout {
      display: grid;
      grid-template-columns: minmax(0, 1fr);
      gap: 2.2rem;
      width: 100%;
      min-width: 0;
    }

    @media (min-width: 992px) {
      .calc-layout {
        grid-template-columns: minmax(0, 1.4fr) minmax(0, 1fr);
        align-items: start;
      }
    }

    .calc-box {
      background: var(--espresso);
      border: 1px solid var(--warm-brown);
      border-radius: var(--radius-lg);
      padding: 1.8rem;
      width: 100%;
      min-width: 0;
      max-width: 100%;
      box-sizing: border-box;
      overflow: hidden;
    }

    .calc-presets-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--champagne);
      text-transform: uppercase;
      letter-spacing: 0.08em;
      margin-bottom: 1rem;
    }

    .calc-presets {
      display: flex;
      flex-wrap: wrap;
      gap: 0.65rem;
      margin-bottom: 2rem;
      width: 100%;
      max-width: 100%;
      min-width: 0;
    }

    .calc-preset-chip {
      padding: 0.65rem 1.15rem;
      border-radius: 999px;
      font-size: 0.86rem;
      font-weight: 700;
      background: rgba(52, 25, 10, 0.5);
      border: 1px solid var(--warm-brown);
      color: var(--soft-beige);
      transition: all 0.2s ease;
    }

    .calc-preset-chip:hover {
      border-color: var(--amber);
      color: #fff;
    }

    .calc-preset-chip.is-active {
      background: rgba(222, 128, 38, 0.2);
      border-color: var(--amber);
      color: var(--light-gold);
      box-shadow: 0 0 14px rgba(222, 128, 38, 0.25);
    }

    .calc-items-grid {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      margin-bottom: 2rem;
    }

    .calc-item {
      background: rgba(52, 25, 10, 0.35);
      border: 1px solid rgba(89, 43, 14, 0.4);
      border-radius: var(--radius);
      padding: 1.2rem;
      display: flex;
      flex-direction: column;
      gap: 0.8rem;
    }

    .calc-item-top {
      display: flex;
      align-items: center;
      justify-content: space-between;
    }

    .calc-item-info {
      display: flex;
      align-items: center;
      gap: 0.75rem;
    }

    .calc-item-icon {
      width: 32px;
      height: 32px;
      border-radius: 8px;
      background: rgba(89, 43, 14, 0.6);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--amber);
      flex-shrink: 0;
    }

    .calc-item-name {
      font-weight: 700;
      font-size: 1rem;
      color: var(--ivory);
    }

    .calc-item-rate {
      font-size: 0.8rem;
      color: var(--champagne);
    }

    .calc-item-count-badge {
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 800;
      color: var(--light-gold);
      background: rgba(3, 2, 1, 0.6);
      padding: 0.25rem 0.75rem;
      border-radius: 8px;
      border: 1px solid rgba(203, 164, 130, 0.3);
      min-width: 52px;
      text-align: center;
    }

    .calc-item-range {
      width: 100%;
      height: 6px;
      border-radius: 999px;
      background: rgba(3, 2, 1, 0.6);
      outline: none;
      -webkit-appearance: none;
    }

    .calc-item-range::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: var(--amber);
      border: 2px solid #fff;
      cursor: pointer;
    }

    @media (max-width: 768px) {
      .calc-box {
        padding: 1.25rem;
      }
      .calc-presets {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 0.5rem;
        margin-bottom: 1.25rem;
        width: 100%;
        max-width: 100%;
        box-sizing: border-box;
      }
      .calc-preset-chip {
        padding: 0.5rem 0.85rem;
        font-size: 0.8rem;
      }
      .calc-item {
        padding: 1rem;
      }
      .calc-item-range::-webkit-slider-thumb {
        width: 28px;
        height: 28px;
      }
      .calc-summary-card {
        position: static;
        padding: 1.25rem;
      }
    }

    .calc-select-row {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1rem;
    }

    @media (min-width: 640px) {
      .calc-select-row {
        grid-template-columns: 1fr 1fr;
      }
    }

    .calc-select-group label {
      display: block;
      font-size: 0.82rem;
      font-weight: 700;
      color: var(--champagne);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.4rem;
    }

    .calc-select {
      width: 100%;
      padding: 0.75rem 1rem;
      background: rgba(3, 2, 1, 0.7);
      border: 1px solid var(--warm-brown);
      border-radius: var(--radius-sm);
      color: var(--ivory);
      font-size: 0.95rem;
    }

    .calc-select:focus {
      border-color: var(--amber);
    }

    /* Calculator Summary Sticky Card */
    .calc-summary-card {
      position: sticky;
      top: calc(var(--header-h) + 20px);
      background: linear-gradient(160deg, #190B05 0%, #0B0704 100%);
      border: 1px solid rgba(222, 128, 38, 0.4);
      border-radius: var(--radius-lg);
      padding: 2rem;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6), 0 0 24px rgba(222, 128, 38, 0.15);
    }

    .calc-summary-header {
      padding-bottom: 1.25rem;
      border-bottom: 1px solid rgba(89, 43, 14, 0.5);
      margin-bottom: 1.25rem;
    }

    .calc-summary-title {
      font-size: 0.88rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--champagne);
      margin-bottom: 0.5rem;
    }

    .calc-summary-total {
      font-family: var(--font-display);
      font-size: 2.5rem;
      font-weight: 800;
      color: var(--ivory);
      line-height: 1.1;
      display: flex;
      align-items: baseline;
      gap: 0.35rem;
    }

    .calc-summary-note {
      font-size: 0.82rem;
      color: var(--soft-beige);
      margin-top: 0.35rem;
    }

    .calc-summary-list {
      display: flex;
      flex-direction: column;
      gap: 0.65rem;
      margin-bottom: 1.5rem;
      max-height: 220px;
      overflow-y: auto;
      padding-right: 0.4rem;
    }

    .calc-summary-row {
      display: flex;
      justify-content: space-between;
      font-size: 0.88rem;
      color: var(--soft-beige);
    }

    .calc-summary-row span:last-child {
      font-weight: 700;
      color: var(--ivory);
    }

    .calc-inclusions {
      padding-top: 1rem;
      border-top: 1px solid rgba(89, 43, 14, 0.35);
      margin-bottom: 1.6rem;
    }

    .calc-inclusions-title {
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--champagne);
      margin-bottom: 0.5rem;
    }

    .calc-inclusions-list {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      font-size: 0.82rem;
      color: var(--soft-beige);
    }

    .calc-inclusions-list li {
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .calc-inclusions-list svg {
      color: var(--amber);
      width: 14px;
      height: 14px;
    }

    .calc-actions {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    /* ==========================================================================
       12. FILTERABLE PORTFOLIO SHOWCASE GALLERY & LIGHTBOX
       ========================================================================== */
    .gallery-filters {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 0.65rem;
      margin-bottom: 2.5rem;
      width: 100%;
      max-width: 100%;
      min-width: 0;
    }

    @media (max-width: 640px) {
      .gallery-filters {
        display: flex;
        flex-wrap: wrap;
        justify-content: center;
        gap: 0.5rem;
        margin-bottom: 1.5rem;
        width: 100%;
        max-width: 100%;
        box-sizing: border-box;
      }
      .gallery-filter-btn {
        padding: 0.45rem 0.85rem;
        font-size: 0.8rem;
      }
      .lightbox {
        padding: 1rem;
      }
      .lightbox__close {
        top: 14px;
        right: 14px;
        width: 40px;
        height: 40px;
      }
      .lightbox__nav-btn {
        width: 40px;
        height: 40px;
      }
      .lightbox__nav-btn--prev { left: 8px; }
      .lightbox__nav-btn--next { right: 8px; }
      .lightbox__img {
        max-height: 55vh;
      }
      .lightbox__title {
        font-size: 1.15rem;
      }
      .lightbox__desc {
        font-size: 0.84rem;
        margin-bottom: 0.75rem;
      }
    }

    .gallery-filter-btn {
      padding: 0.6rem 1.25rem;
      border-radius: 999px;
      font-size: 0.88rem;
      font-weight: 700;
      background: rgba(25, 11, 5, 0.7);
      border: 1px solid var(--warm-brown);
      color: var(--soft-beige);
      transition: all 0.2s ease;
    }

    .gallery-filter-btn:hover {
      border-color: var(--amber);
      color: #fff;
    }

    .gallery-filter-btn.is-active {
      background: linear-gradient(135deg, var(--amber) 0%, var(--burnt-gold) 100%);
      border-color: var(--light-gold);
      color: #fff;
      box-shadow: 0 4px 16px rgba(222, 128, 38, 0.35);
    }

    .gallery-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.8rem;
    }

    @media (min-width: 640px) {
      .gallery-grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (min-width: 1024px) {
      .gallery-grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .gallery-card {
      position: relative;
      border-radius: var(--radius);
      overflow: hidden;
      background: var(--espresso);
      border: 1px solid var(--warm-brown);
      cursor: pointer;
      aspect-ratio: 4 / 3;
      transition: all 0.35s var(--ease);
    }

    .gallery-card:hover {
      transform: translateY(-5px);
      border-color: var(--amber);
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.7), 0 0 24px rgba(222, 128, 38, 0.25);
    }

    .gallery-card__img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      transition: transform 0.6s var(--ease);
    }

    .gallery-card:hover .gallery-card__img {
      transform: scale(1.08);
    }

    .gallery-card__overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, transparent 40%, rgba(3, 2, 1, 0.95) 100%);
      display: flex;
      flex-direction: column;
      justify-content: flex-end;
      padding: 1.4rem;
      transition: opacity 0.3s ease;
    }

    .gallery-card__category {
      font-size: 0.75rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--light-gold);
      margin-bottom: 0.25rem;
    }

    .gallery-card__title {
      font-size: 1.15rem;
      font-weight: 700;
      color: var(--ivory);
      margin-bottom: 0.2rem;
    }

    .gallery-card__venue {
      font-size: 0.82rem;
      color: var(--soft-beige);
    }

    .gallery-card__zoom {
      position: absolute;
      top: 14px;
      right: 14px;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(3, 2, 1, 0.7);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(203, 164, 130, 0.3);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--light-gold);
      opacity: 0;
      transform: scale(0.8);
      transition: all 0.25s var(--ease);
    }

    .gallery-card:hover .gallery-card__zoom {
      opacity: 1;
      transform: scale(1);
    }

    /* Fullscreen Lightbox Modal */
    .lightbox {
      position: fixed;
      inset: 0;
      background: rgba(3, 2, 1, 0.95);
      backdrop-filter: blur(20px);
      z-index: 1000;
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      padding: 1.5rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }

    .lightbox.is-open {
      opacity: 1;
      pointer-events: auto;
    }

    .lightbox__close {
      position: absolute;
      top: 24px;
      right: 24px;
      width: 44px;
      height: 44px;
      border-radius: 50%;
      background: rgba(52, 25, 10, 0.7);
      border: 1px solid var(--warm-brown);
      color: var(--ivory);
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 10;
      transition: all 0.2s ease;
    }

    .lightbox__close:hover {
      background: var(--amber);
      color: #000;
      transform: rotate(90deg);
    }

    .lightbox__content {
      position: relative;
      max-width: 960px;
      width: 100%;
      max-height: 80vh;
      display: flex;
      flex-direction: column;
      align-items: center;
    }

    .lightbox__img {
      max-width: 100%;
      max-height: 65vh;
      border-radius: var(--radius);
      object-fit: contain;
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), 0 0 40px rgba(222, 128, 38, 0.2);
      border: 1px solid rgba(203, 164, 130, 0.3);
    }

    .lightbox__caption {
      margin-top: 1.25rem;
      text-align: center;
      max-width: 600px;
    }

    .lightbox__title {
      font-size: 1.3rem;
      font-weight: 700;
      color: var(--ivory);
      margin-bottom: 0.35rem;
    }

    .lightbox__desc {
      font-size: 0.92rem;
      color: var(--soft-beige);
      margin-bottom: 1rem;
    }

    .lightbox__nav-btn {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: rgba(52, 25, 10, 0.7);
      border: 1px solid var(--warm-brown);
      color: var(--ivory);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }

    .lightbox__nav-btn:hover {
      background: var(--amber);
      color: #000;
      transform: translateY(-50%) scale(1.1);
    }

    .lightbox__nav-btn--prev { left: -60px; }
    .lightbox__nav-btn--next { right: -60px; }

    @media (max-width: 1100px) {
      .lightbox__nav-btn--prev { left: 16px; }
      .lightbox__nav-btn--next { right: 16px; }
    }

    /* ==========================================================================
       13. DIRECT EVENT BOOKING & CALLBACK REQUEST FORM
       ========================================================================== */
    .booking-card {
      background: linear-gradient(165deg, #190B05 0%, #0B0704 100%);
      border: 1px solid rgba(222, 128, 38, 0.4);
      border-radius: var(--radius-lg);
      padding: clamp(1.8rem, 4vw, 3rem);
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.7), 0 0 30px rgba(222, 128, 38, 0.12);
    }

    .booking-form {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.5rem;
    }

    @media (min-width: 768px) {
      .booking-form {
        grid-template-columns: 1fr 1fr;
      }
      .booking-full {
        grid-column: 1 / -1;
      }
    }

    .form-group {
      display: flex;
      flex-direction: column;
      gap: 0.45rem;
    }

    .form-label {
      font-size: 0.86rem;
      font-weight: 700;
      color: var(--champagne);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .form-input, .form-select, .form-textarea, .calc-select {
      width: 100%;
      padding: 0.85rem 1.1rem;
      background: rgba(3, 2, 1, 0.8);
      border: 1px solid var(--warm-brown);
      border-radius: var(--radius-sm);
      color: var(--ivory);
      font-size: 16px; /* Prevents iOS Safari auto-zoom on input focus */
      transition: border-color 0.2s ease, box-shadow 0.2s ease;
    }

    @media (max-width: 640px) {
      .booking-card {
        padding: 1.25rem;
      }
      .contact__card {
        padding: 1.25rem;
      }
      .review-card {
        padding: 1.25rem;
      }
      .modal-dialog {
        padding: 1.4rem;
        max-height: 90vh;
        overflow-y: auto;
        -webkit-overflow-scrolling: touch;
      }
      .map-box {
        min-height: 320px;
      }
      .map-box iframe {
        min-height: 320px;
      }
      .map-overlay-card {
        top: 12px;
        left: 12px;
        right: 12px;
        padding: 0.85rem 1rem;
      }
    }

    .form-input:focus, .form-select:focus, .form-textarea:focus {
      border-color: var(--amber);
      box-shadow: 0 0 12px rgba(222, 128, 38, 0.35);
    }

    .form-textarea {
      min-height: 100px;
      resize: vertical;
    }

    /* Checkbox Chips */
    .fx-chips-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem;
      margin-top: 0.2rem;
    }

    .fx-chip-checkbox {
      display: none;
    }

    .fx-chip-label {
      padding: 0.5rem 1rem;
      border-radius: 999px;
      font-size: 0.84rem;
      font-weight: 600;
      background: rgba(52, 25, 10, 0.4);
      border: 1px solid var(--warm-brown);
      color: var(--soft-beige);
      cursor: pointer;
      transition: all 0.2s ease;
      user-select: none;
    }

    .fx-chip-checkbox:checked + .fx-chip-label {
      background: rgba(222, 128, 38, 0.25);
      border-color: var(--amber);
      color: var(--light-gold);
      box-shadow: 0 0 10px rgba(222, 128, 38, 0.3);
    }

    .booking-actions {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1rem;
      margin-top: 1rem;
    }

    @media (min-width: 640px) {
      .booking-actions {
        grid-template-columns: 1fr 1fr;
      }
    }

    /* ==========================================================================
       14. CUSTOMER REVIEWS & ADD REVIEW MODAL
       ========================================================================== */
    .reviews__header {
      display: flex;
      flex-direction: column;
      gap: 1rem;
      margin-bottom: 2.5rem;
    }

    @media (min-width: 768px) {
      .reviews__header {
        flex-direction: row;
        justify-content: space-between;
        align-items: flex-end;
      }
    }

    .reviews-grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.8rem;
    }

    @media (min-width: 768px) {
      .reviews-grid {
        grid-template-columns: repeat(3, 1fr);
      }
    }

    .review-card {
      background: var(--espresso);
      border: 1px solid var(--warm-brown);
      border-radius: var(--radius);
      padding: 1.8rem;
      display: flex;
      flex-direction: column;
      position: relative;
      transition: all 0.3s var(--ease);
    }

    .review-card:hover {
      border-color: var(--amber);
      transform: translateY(-3px);
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.5), 0 0 16px rgba(222, 128, 38, 0.15);
    }

    .review-card__stars {
      display: flex;
      gap: 0.25rem;
      color: var(--amber);
      margin-bottom: 1rem;
    }

    .review-card__text {
      font-size: 0.94rem;
      color: var(--ivory);
      line-height: 1.6;
      margin-bottom: 1.5rem;
      flex: 1;
    }

    .review-card__footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid rgba(89, 43, 14, 0.4);
      padding-top: 1rem;
    }

    .review-card__author {
      font-weight: 700;
      font-size: 0.95rem;
      color: var(--ivory);
    }

    .review-card__meta {
      font-size: 0.8rem;
      color: var(--champagne);
    }

    .review-badge-new {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--light-gold);
      background: rgba(222, 128, 38, 0.15);
      border: 1px solid rgba(203, 164, 130, 0.4);
      padding: 0.15rem 0.5rem;
      border-radius: 999px;
      margin-left: 0.4rem;
    }

    /* Modal dialog */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(3, 2, 1, 0.88);
      backdrop-filter: blur(16px);
      z-index: 1000;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 1.5rem;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.3s ease;
    }

    .modal-backdrop.is-open {
      opacity: 1;
      pointer-events: auto;
    }

    .modal-dialog {
      background: linear-gradient(165deg, #190B05 0%, #0B0704 100%);
      border: 1px solid rgba(222, 128, 38, 0.4);
      border-radius: var(--radius-lg);
      padding: clamp(1.2rem, 4vw, 2.2rem);
      max-width: min(540px, calc(100vw - 28px));
      width: 100%;
      box-sizing: border-box;
      position: relative;
      box-shadow: 0 24px 70px rgba(0, 0, 0, 0.8), 0 0 30px rgba(222, 128, 38, 0.2);
    }

    .modal-dialog .btn {
      white-space: normal;
      word-break: break-word;
      width: 100%;
      box-sizing: border-box;
      text-align: center;
    }

    .modal-close {
      position: absolute;
      top: 20px;
      right: 20px;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(52, 25, 10, 0.7);
      border: 1px solid var(--warm-brown);
      color: var(--ivory);
      display: flex;
      align-items: center;
      justify-content: center;
    }

    .modal-close:hover {
      background: var(--amber);
      color: #000;
    }

    /* Star rating widget in modal */
    .star-rating-select {
      display: flex;
      gap: 0.5rem;
      margin-top: 0.2rem;
    }

    .star-btn {
      color: rgba(203, 164, 130, 0.3);
      cursor: pointer;
      transition: color 0.15s ease, transform 0.15s ease;
    }

    .star-btn.is-active, .star-btn:hover {
      color: var(--amber);
      transform: scale(1.15);
    }

    /* ==========================================================================
       15. SEARCHABLE FAQ ACCORDION
       ========================================================================== */
    .faq-search-wrap {
      max-width: 600px;
      margin: 0 auto 2.5rem;
      position: relative;
    }

    .faq-search-input {
      width: 100%;
      padding: 1rem 1.4rem 1rem 3.2rem;
      background: rgba(25, 11, 5, 0.8);
      border: 1px solid var(--warm-brown);
      border-radius: 999px;
      color: var(--ivory);
      font-size: 1rem;
      transition: all 0.2s ease;
    }

    .faq-search-input:focus {
      border-color: var(--amber);
      box-shadow: 0 0 18px rgba(222, 128, 38, 0.35);
    }

    .faq-search-icon {
      position: absolute;
      left: 1.25rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--champagne);
      pointer-events: none;
    }

    .faq-list {
      max-width: 860px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 1rem;
    }

    .acc {
      background: rgba(25, 11, 5, 0.6);
      border: 1px solid var(--warm-brown);
      border-radius: var(--radius);
      overflow: hidden;
      transition: all 0.25s ease;
    }

    .acc.is-open {
      border-color: var(--amber);
      background: rgba(52, 25, 10, 0.4);
    }

    .acc__btn {
      width: 100%;
      padding: 1.3rem 1.6rem;
      display: flex;
      align-items: center;
      justify-content: space-between;
      gap: 1rem;
      text-align: left;
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--ivory);
    }

    .acc__icon {
      transition: transform 0.3s ease;
      color: var(--amber);
      flex-shrink: 0;
    }

    .acc.is-open .acc__icon {
      transform: rotate(180deg);
    }

    .acc__panel {
      max-height: 0;
      overflow: hidden;
      transition: max-height 0.35s ease;
    }

    .acc.is-open .acc__panel {
      max-height: 400px;
    }

    .acc__body {
      padding: 0 1.6rem 1.4rem;
      color: var(--soft-beige);
      font-size: 0.94rem;
      line-height: 1.65;
    }

    /* ==========================================================================
       16. CONTACT & MAP SECTION
       ========================================================================== */
    .contact__grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 2rem;
    }

    @media (min-width: 992px) {
      .contact__grid {
        grid-template-columns: 1.1fr 1fr;
      }
    }

    .contact__card {
      background: var(--espresso);
      border: 1px solid var(--warm-brown);
      border-radius: var(--radius-lg);
      padding: 2.2rem;
    }

    .contact__items {
      display: flex;
      flex-direction: column;
      gap: 1.4rem;
      margin-top: 1.8rem;
    }

    .contact__item {
      display: flex;
      align-items: flex-start;
      gap: 1rem;
    }

    .contact__item-icon {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: rgba(52, 25, 10, 0.8);
      border: 1px solid rgba(222, 128, 38, 0.35);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--amber);
      flex-shrink: 0;
    }

    .contact__item-label {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--champagne);
      margin-bottom: 0.2rem;
    }

    .contact__item-val {
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--ivory);
    }

    .contact__item-val a:hover {
      color: var(--amber);
    }

    .map-box {
      border-radius: var(--radius-lg);
      overflow: hidden;
      border: 1px solid var(--warm-brown);
      height: 100%;
      min-height: 420px;
      background: #190B05;
      position: relative;
      box-shadow: 0 16px 40px rgba(0, 0, 0, 0.6);
    }

    .map-box iframe {
      width: 100%;
      height: 100%;
      min-height: 420px;
      border: 0;
      display: block;
    }

    .map-overlay-card {
      position: absolute;
      top: 16px;
      left: 16px;
      right: 16px;
      max-width: 380px;
      width: auto;
      box-sizing: border-box;
      background: rgba(11, 7, 4, 0.92);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid rgba(222, 128, 38, 0.4);
      border-radius: var(--radius);
      padding: 1.1rem 1.3rem;
      z-index: 5;
      box-shadow: 0 12px 30px rgba(0, 0, 0, 0.7);
    }

    .map-overlay-title {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--ivory);
      margin-bottom: 0.35rem;
    }

    .map-overlay-address {
      font-size: 0.82rem;
      color: var(--soft-beige);
      line-height: 1.45;
      margin-bottom: 0.85rem;
    }

    .map-overlay-actions {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    /* ==========================================================================
       17. FOOTER
       ========================================================================== */
    .footer {
      background: #030201;
      border-top: 1px solid rgba(89, 43, 14, 0.4);
      padding: 4.5rem 0 3rem;
      position: relative;
      z-index: 1;
    }

    .footer__grid {
      display: grid;
      grid-template-columns: 1fr;
      gap: 2.5rem;
      margin-bottom: 3.5rem;
    }

    @media (min-width: 640px) {
      .footer__grid {
        grid-template-columns: repeat(2, 1fr);
      }
    }

    @media (min-width: 1024px) {
      .footer__grid {
        grid-template-columns: 1.5fr 1fr 1fr 1.2fr;
      }
    }

    .footer__brand p {
      font-size: 0.92rem;
      color: var(--soft-beige);
      margin-top: 1rem;
      line-height: 1.6;
    }

    .footer__title {
      font-size: 0.95rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--light-gold);
      margin-bottom: 1.25rem;
    }

    .footer__list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .footer__list a {
      font-size: 0.92rem;
      color: var(--soft-beige);
    }

    .footer__list a:hover {
      color: var(--amber);
      transform: translateX(4px);
    }

    .footer__bottom {
      padding-top: 2rem;
      border-top: 1px solid rgba(89, 43, 14, 0.3);
      display: flex;
      flex-direction: column;
      gap: 1rem;
      align-items: center;
      text-align: center;
      font-size: 0.88rem;
      color: var(--soft-beige);
    }

    @media (min-width: 768px) {
      .footer__bottom {
        flex-direction: row;
        justify-content: space-between;
        text-align: left;
      }
    }

    /* ==========================================================================
       18. MOBILE DOCK & FLOATING WHATSAPP
       ========================================================================== */
    .dock {
      position: fixed;
      bottom: 0;
      left: 0;
      right: 0;
      background: rgba(3, 2, 1, 0.96);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-top: 1px solid rgba(89, 43, 14, 0.5);
      padding: 0.75rem var(--gutter) max(0.75rem, env(safe-area-inset-bottom, 0px));
      display: flex;
      gap: 0.75rem;
      z-index: 90;
      box-shadow: 0 -8px 24px rgba(0, 0, 0, 0.7);
    }

    .dock .btn {
      flex: 1;
      min-width: 0;
      padding: 0.65rem 0.85rem;
      font-size: 0.86rem;
      white-space: nowrap;
    }

    @media (min-width: 768px) {
      .dock {
        display: none;
      }
    }

    /* Floating WhatsApp Pill */
    .float-wa {
      position: fixed;
      bottom: 24px;
      right: 24px;
      z-index: 89;
      display: none;
      align-items: center;
      gap: 0.65rem;
      padding: 0.75rem 1.3rem;
      border-radius: 999px;
      background: linear-gradient(145deg, var(--espresso) 0%, #0B0704 100%);
      border: 1px solid rgba(222, 128, 38, 0.6);
      color: var(--ivory);
      font-weight: 700;
      font-size: 0.92rem;
      box-shadow: 0 8px 30px rgba(0, 0, 0, 0.8), 0 0 16px rgba(222, 128, 38, 0.25);
      transition: all 0.25s var(--ease);
    }

    .float-wa svg {
      color: var(--amber);
    }

    @media (min-width: 768px) {
      .float-wa {
        display: flex;
      }
    }

    .float-wa:hover {
      background: linear-gradient(145deg, var(--dark-brown) 0%, var(--espresso) 100%);
      border-color: var(--light-gold);
      color: #fff;
      transform: translateY(-3px) scale(1.03);
      box-shadow: 0 12px 34px rgba(0, 0, 0, 0.9), 0 0 24px rgba(222, 128, 38, 0.4);
    }

    /* Toast Notification */
    .toast-container {
      position: fixed;
      bottom: 80px;
      left: 50%;
      transform: translateX(-50%);
      z-index: 2000;
      pointer-events: none;
    }

    .toast {
      background: rgba(25, 11, 5, 0.95);
      border: 1px solid var(--amber);
      color: #fff;
      padding: 0.85rem 1.6rem;
      border-radius: 999px;
      font-size: 0.9rem;
      font-weight: 600;
      box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8), 0 0 20px rgba(222, 128, 38, 0.3);
      display: flex;
      align-items: center;
      gap: 0.6rem;
      opacity: 0;
      transform: translateY(20px);
      transition: all 0.3s var(--ease);
    }

    .toast.is-show {
      opacity: 1;
      transform: translateY(0);
    }

    /* ==========================================================================
       19. MASTER MOBILE (<= 767px) COMPREHENSIVE OVERRIDES
       ========================================================================== */
    @media (max-width: 767px) {
      /* Base & Viewport */
      html, body {
        width: 100% !important;
        max-width: 100vw !important;
        overflow-x: hidden !important;
        position: relative !important;
      }

      main {
        width: 100% !important;
        max-width: 100% !important;
        overflow-x: hidden !important;
      }

      .container {
        width: 100% !important;
        max-width: 100% !important;
        padding-left: 14px !important;
        padding-right: 14px !important;
        box-sizing: border-box !important;
      }

      /* Header */
      .header {
        width: 100% !important;
        max-width: 100vw !important;
      }
      .header .container {
        width: 100% !important;
        max-width: 100% !important;
        padding-left: 14px !important;
        padding-right: 14px !important;
      }
      .header__bar {
        width: 100% !important;
        justify-content: space-between !important;
      }
      .brand {
        min-width: 0 !important;
      }
      .brand__name {
        font-size: 1.05rem !important;
      }
      .header__actions {
        margin-left: auto !important;
        gap: 0.5rem !important;
      }

      /* Hero */
      .hero {
        display: block !important;
        width: 100% !important;
        padding-top: 1.4rem !important;
        padding-bottom: 2.5rem !important;
        min-height: auto !important;
      }
      .hero__inner {
        display: flex !important;
        flex-direction: column !important;
        width: 100% !important;
        gap: 1.8rem !important;
      }
      .hero__copy {
        width: 100% !important;
        max-width: 100% !important;
      }
      .hero__badge {
        font-size: 0.72rem !important;
        padding: 0.35rem 0.75rem !important;
        max-width: 100% !important;
        white-space: normal !important;
        text-align: center !important;
      }
      .hero__title {
        font-size: clamp(1.45rem, 5.5vw, 1.85rem) !important;
        line-height: 1.2 !important;
        word-break: break-word !important;
        overflow-wrap: break-word !important;
        margin-bottom: 1rem !important;
      }
      .hero__lead {
        font-size: 0.94rem !important;
        line-height: 1.55 !important;
        margin-bottom: 1.25rem !important;
      }
      .hero__actions {
        display: flex !important;
        flex-direction: column !important;
        width: 100% !important;
        gap: 0.75rem !important;
      }
      .hero__actions .btn {
        width: 100% !important;
        justify-content: center !important;
      }
      .hero__visual-wrap {
        order: -1 !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
        margin-bottom: 0.5rem !important;
      }
      .hero__visual-card {
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
      }
      .hero__visual-img {
        width: 100% !important;
        height: clamp(230px, 58vw, 300px) !important;
      }

      /* Trust */
      .trust__grid {
        grid-template-columns: 1fr !important;
        gap: 1rem !important;
        width: 100% !important;
      }

      /* Services */
      .services__grid {
        grid-template-columns: 1fr !important;
        gap: 1.4rem !important;
        width: 100% !important;
      }
      .service-card {
        width: 100% !important;
        max-width: 100% !important;
      }

      /* Simulator */
      .sim-wrap {
        width: 100% !important;
        max-width: 100% !important;
      }
      .sim-stage-box {
        height: 260px !important;
        max-height: 40vh !important;
        width: 100% !important;
      }
      .sim-canvas {
        width: 100% !important;
        max-width: 100% !important;
      }
      .sim-header {
        padding: 0.75rem 1rem !important;
      }
      .sim-stage-footer {
        padding: 1rem !important;
        gap: 0.85rem !important;
        width: 100% !important;
        box-sizing: border-box !important;
      }
      .sim-btn-rack {
        display: grid !important;
        grid-template-columns: repeat(2, 1fr) !important;
        gap: 0.5rem !important;
        width: 100% !important;
      }
      .sim-trigger-btn {
        padding: 0.55rem 0.65rem !important;
        font-size: 0.8rem !important;
        justify-content: center !important;
        white-space: nowrap !important;
      }
      .sim-trigger-btn--finale {
        grid-column: 1 / -1 !important;
      }
      .sim-sliders {
        grid-template-columns: 1fr !important;
        gap: 0.75rem !important;
        width: 100% !important;
      }

      /* Calculator */
      .calc-layout {
        grid-template-columns: 1fr !important;
        gap: 1.5rem !important;
        width: 100% !important;
      }
      .calc-box {
        padding: 1.15rem !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
        overflow: hidden !important;
      }
      .calc-presets {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 0.5rem !important;
        margin-bottom: 1.25rem !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
      }
      .calc-preset-chip {
        white-space: normal !important;
        text-align: center !important;
        padding: 0.45rem 0.8rem !important;
        font-size: 0.78rem !important;
      }
      .calc-item {
        padding: 0.9rem !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
      }
      .calc-summary-card {
        position: static !important;
        padding: 1.25rem !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
      }
      .calc-actions {
        flex-direction: column !important;
        width: 100% !important;
      }
      .calc-actions .btn {
        width: 100% !important;
        justify-content: center !important;
      }

      /* Gallery */
      .gallery-filters {
        display: flex !important;
        flex-wrap: wrap !important;
        justify-content: center !important;
        gap: 0.5rem !important;
        margin-bottom: 1.25rem !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
      }
      .gallery-filter-btn {
        white-space: normal !important;
        text-align: center !important;
        padding: 0.45rem 0.8rem !important;
        font-size: 0.78rem !important;
      }
      .gallery-grid {
        grid-template-columns: 1fr !important;
        gap: 1.25rem !important;
        width: 100% !important;
      }
      .gallery-card {
        width: 100% !important;
        max-width: 100% !important;
      }

      /* Booking */
      .booking-card {
        padding: 1.25rem !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
      }
      .booking-form {
        grid-template-columns: 1fr !important;
        gap: 1rem !important;
        width: 100% !important;
      }
      .booking-actions {
        grid-template-columns: 1fr !important;
        gap: 0.75rem !important;
        width: 100% !important;
      }
      .booking-actions .btn {
        width: 100% !important;
        justify-content: center !important;
      }

      /* Reviews */
      .reviews__header {
        flex-direction: column !important;
        align-items: stretch !important;
        gap: 1rem !important;
        width: 100% !important;
      }
      .reviews__header .btn {
        width: 100% !important;
        justify-content: center !important;
      }
      .reviews-grid {
        grid-template-columns: 1fr !important;
        gap: 1.25rem !important;
        width: 100% !important;
      }
      .review-card {
        padding: 1.25rem !important;
        width: 100% !important;
        max-width: 100% !important;
      }

      /* Contact & Map */
      .contact__grid {
        grid-template-columns: 1fr !important;
        gap: 1.5rem !important;
        width: 100% !important;
      }
      .contact__card {
        padding: 1.25rem !important;
        width: 100% !important;
        max-width: 100% !important;
      }
      .map-box {
        min-height: 300px !important;
        width: 100% !important;
        max-width: 100% !important;
      }
      .map-box iframe {
        min-height: 300px !important;
        width: 100% !important;
      }
      .map-overlay-card {
        top: 10px !important;
        left: 10px !important;
        right: 10px !important;
        max-width: calc(100% - 20px) !important;
        width: auto !important;
        padding: 0.85rem 1rem !important;
        box-sizing: border-box !important;
      }

      /* Modals */
      .modal-dialog {
        padding: 1.3rem !important;
        max-width: calc(100vw - 28px) !important;
        width: 100% !important;
        margin: 14px auto !important;
        box-sizing: border-box !important;
      }
      #callback-instant-wa {
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
        justify-content: center !important;
      }
      #callback-instant-wa span {
        white-space: normal !important;
        text-align: center !important;
      }

      /* Footer */
      .footer {
        padding: 3rem 0 calc(2rem + env(safe-area-inset-bottom, 0px)) !important;
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
      }
      .footer__grid {
        grid-template-columns: 1fr !important;
        gap: 1.8rem !important;
        width: 100% !important;
      }
      .footer__bottom {
        flex-direction: column !important;
        gap: 0.75rem !important;
        text-align: center !important;
        padding-top: 1.5rem !important;
        word-break: break-word !important;
      }

      /* Bottom Dock */
      .dock {
        padding: 0.65rem 12px max(0.65rem, env(safe-area-inset-bottom, 0px)) !important;
        gap: 0.6rem !important;
        width: 100% !important;
        max-width: 100vw !important;
        box-sizing: border-box !important;
      }
      .dock .btn {
        flex: 1 1 0 !important;
        min-width: 0 !important;
        padding: 0.65rem 0.4rem !important;
        font-size: 0.82rem !important;
        justify-content: center !important;
        white-space: nowrap !important;
      }
    }
  </style>
'''
