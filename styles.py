# CSS styles module for Galaxy Pyrotech Traders
def get_css():
    return '''
  <style>
    /* ==========================================================================
       1. OFFICIAL PALETTE VARIABLES & SYSTEM (Warm Cream, Forest Green & Gold)
       ========================================================================== */
    :root {
      /* Primary Base Background: Warm Cream / Soft Alabaster */
      --cream-base:       #FBF8F3;
      
      /* Secondary Background / Card Base: Warm Off-White / Crisp White */
      --card-white:       #FFFFFF;
      --card-tint:        #F4EFEA;
      
      /* Primary Accent / Brand Dark: Deep Forest / Emerald Green */
      --forest-green:     #1E342B;
      --forest-hover:     #274338;
      --forest-dark:      #14241E;
      
      /* Secondary Accent / Highlight: Soft Gold / Muted Champagne */
      --soft-gold:        #C4A482;
      --soft-gold-light:  #DFCAAE;
      --soft-gold-dark:   #9E7B54;
      --gold-tint:        rgba(196, 164, 130, 0.15);
      --gold-border:      rgba(196, 164, 130, 0.4);
      
      /* Primary Body Text: Dark Slate / Espresso */
      --text-espresso:    #2A2A2A;
      
      /* Secondary Body Text: Muted Taupe Grey */
      --text-taupe:       #6B655F;
      
      /* Subtle Card & Section Borders */
      --border-subtle:    #E5DFD7;

      /* Semantic Variable Aliases for 100% Component Compatibility */
      --black:            #1E342B;
      --black-soft:       #FBF8F3;
      --espresso:         #FFFFFF;
      --dark-brown:       #F4EFEA;
      --warm-brown:       #E5DFD7;
      --amber:            #1E342B;
      --burnt-gold:       #274338;
      --champagne:        #C4A482;
      --light-gold:       #C4A482;
      --ivory:            #2A2A2A;
      --soft-beige:       #6B655F;
      --muted-brown:      rgba(196, 164, 130, 0.3);

      /* Semantic Tokens */
      --bg-primary:       var(--cream-base);
      --bg-secondary:     var(--card-tint);
      --bg-card:          var(--card-white);
      --bg-elevated:      var(--card-white);
      --border-color:     var(--border-subtle);
      --border-glow:      rgba(196, 164, 130, 0.35);
      --accent:           var(--forest-green);
      --accent-hover:     var(--forest-hover);
      --accent-glow:      rgba(30, 52, 43, 0.2);
      --gold:             var(--soft-gold);
      --text:             var(--text-espresso);
      --text-muted:       var(--text-taupe);

      /* Typography: Classy Serif Headings + Clean Modern Sans Body */
      --font-display:     "Cormorant Garamond", "Playfair Display", Georgia, serif;
      --font-body:        "Plus Jakarta Sans", ui-sans-serif, system-ui, -apple-system, sans-serif;

      /* Dimensions & Transitions */
      --header-h:         68px;
      --gutter:           16px;
      --container:        1240px;
      --radius-sm:        8px;
      --radius:           16px;
      --radius-lg:        24px;
      --ease:             cubic-bezier(0.16, 1, 0.3, 1);
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
      background-color: var(--cream-base);
      color: var(--text-espresso);
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
      background: var(--cream-base);
      color: var(--text-espresso);
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
      opacity: 0.25;
      pointer-events: none;
    }

    .sky__glow--1 {
      top: -10%;
      right: 10%;
      width: 50vw;
      height: 50vw;
      background: radial-gradient(circle, rgba(196, 164, 130, 0.18) 0%, transparent 70%);
    }

    .sky__glow--2 {
      top: 40%;
      left: -15%;
      width: 60vw;
      height: 60vw;
      background: radial-gradient(circle, rgba(30, 52, 43, 0.05) 0%, transparent 70%);
      opacity: 0.2;
    }

    .sky__glow--3 {
      bottom: -10%;
      right: -10%;
      width: 55vw;
      height: 55vw;
      background: radial-gradient(circle, rgba(244, 239, 234, 0.8) 0%, transparent 70%);
      opacity: 0.35;
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
      background: var(--soft-gold);
      box-shadow: 0 0 5px 1px rgba(196, 164, 130, 0.6);
      animation: floatSpark var(--dur, 10s) linear infinite;
      animation-delay: var(--delay, 0s);
    }

    @keyframes floatSpark {
      0% {
        transform: translate3d(0, 0, 0);
        opacity: 0;
      }
      10% {
        opacity: 0.85;
      }
      90% {
        opacity: 0.6;
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
      color: var(--forest-green);
      letter-spacing: -0.01em;
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
      gap: 0.45rem;
      font-family: var(--font-body);
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--forest-green);
      margin-bottom: 0.75rem;
      background: rgba(196, 164, 130, 0.16);
      padding: 0.35rem 0.85rem;
      border-radius: 999px;
      border: 1px solid rgba(196, 164, 130, 0.45);
      max-width: 100%;
      box-sizing: border-box;
      white-space: normal;
      text-align: center;
    }

    .section-tag svg {
      color: var(--soft-gold-dark);
    }

    .section-head h2 {
      font-size: clamp(1.85rem, 5.5vw, 3.2rem);
      letter-spacing: -0.015em;
      margin-bottom: 0.8rem;
      color: var(--forest-green);
    }

    .section-head p {
      color: var(--text-taupe);
      font-size: 1.05rem;
      max-width: 680px;
      margin-left: auto;
      margin-right: auto;
      line-height: 1.65;
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
      background: var(--card-tint);
      border-top: 1px solid var(--border-subtle);
      border-bottom: 1px solid var(--border-subtle);
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
      font-family: var(--font-body);
      font-size: 0.95rem;
      font-weight: 700;
      letter-spacing: 0.01em;
      white-space: nowrap;
      transition: all 0.25s var(--ease);
      cursor: pointer;
      position: relative;
      user-select: none;
    }

    /* Primary CTA Buttons = Deep Forest Green with White/Cream text */
    .btn--primary, .btn--call {
      background: var(--forest-green);
      color: #FFFFFF;
      font-weight: 700;
      border: 1px solid rgba(30, 52, 43, 0.2);
      box-shadow: 0 4px 18px rgba(30, 52, 43, 0.22);
    }

    .btn--primary:hover, .btn--call:hover {
      background: var(--forest-hover);
      color: #FFFFFF;
      box-shadow: 0 8px 26px rgba(30, 52, 43, 0.32);
      transform: translateY(-2px);
    }

    /* WhatsApp Button = Crisp White with Soft Gold Border & Forest Green text */
    .btn--wa {
      background: #FFFFFF;
      color: var(--forest-green);
      font-weight: 700;
      border: 1.5px solid var(--soft-gold);
      box-shadow: 0 4px 14px rgba(30, 52, 43, 0.06);
    }

    .btn--wa svg {
      color: #25D366;
    }

    .btn--wa:hover {
      background: var(--card-tint);
      border-color: var(--forest-green);
      color: var(--forest-green);
      box-shadow: 0 6px 20px rgba(30, 52, 43, 0.12);
      transform: translateY(-2px);
    }

    /* Secondary / Outline Buttons */
    .btn--outline {
      border: 1.5px solid var(--forest-green);
      color: var(--forest-green);
      background: transparent;
    }

    .btn--outline:hover {
      background: var(--forest-green);
      color: #FFFFFF;
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
        box-shadow: 0 4px 18px rgba(30, 52, 43, 0.22);
      }
      50% {
        box-shadow: 0 6px 28px rgba(30, 52, 43, 0.4);
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
      transition: background 0.3s ease, border-color 0.3s ease, backdrop-filter 0.3s ease, box-shadow 0.3s ease;
      background: rgba(251, 248, 243, 0.94);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-bottom: 1px solid var(--border-subtle);
    }

    .header.is-scrolled {
      background: rgba(255, 255, 255, 0.98);
      border-bottom-color: rgba(196, 164, 130, 0.35);
      box-shadow: 0 4px 20px rgba(30, 52, 43, 0.06);
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
      background: linear-gradient(135deg, var(--soft-gold-light) 0%, var(--soft-gold) 50%, var(--forest-green) 100%);
      box-shadow: 0 0 12px rgba(196, 164, 130, 0.35);
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
      font-weight: 700;
      font-size: 1.25rem;
      letter-spacing: -0.01em;
      color: var(--forest-green);
      line-height: 1.15;
      white-space: nowrap;
    }

    .brand__tag {
      font-family: var(--font-body);
      font-size: 0.72rem;
      color: var(--text-taupe);
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
        font-family: var(--font-body);
        font-size: 0.88rem;
        font-weight: 600;
        color: var(--text-espresso);
        position: relative;
        padding: 0.4rem 0.2rem;
        white-space: nowrap;
        letter-spacing: 0.01em;
        transition: color 0.2s ease;
      }

      .nav__list a:hover,
      .nav__list a[aria-current="true"] {
        color: var(--forest-green);
      }

      .nav__list a[aria-current="true"]::after {
        content: "";
        position: absolute;
        bottom: -2px;
        left: 0;
        width: 100%;
        height: 2px;
        background: var(--soft-gold);
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
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      color: var(--forest-green);
      transition: all 0.2s ease;
      user-select: none;
      cursor: pointer;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
    }

    .sound-toggle:hover {
      background: var(--card-tint);
      border-color: var(--soft-gold);
      color: var(--forest-green);
    }

    .sound-toggle.is-active {
      background: rgba(196, 164, 130, 0.18);
      border-color: var(--soft-gold);
      color: var(--forest-green);
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
        font-size: 1.15rem;
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
      border: 1px solid var(--border-subtle);
      background: #FFFFFF;
      color: var(--forest-green);
      flex-shrink: 0;
      box-shadow: 0 2px 6px rgba(0, 0, 0, 0.03);
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
      background: rgba(251, 248, 243, 0.98);
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
      border-bottom: 1px solid var(--border-subtle);
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
      font-size: 1.45rem;
      font-weight: 700;
      color: var(--forest-green);
      display: block;
      border-bottom: 1px solid var(--border-subtle);
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
       ========================================================================== */
    .hero {
      position: relative;
      padding-top: calc(var(--header-h) * 0.4);
      padding-bottom: 5.5rem;
      overflow: hidden;
      min-height: calc(100vh - var(--header-h));
      display: flex;
      align-items: center;
      width: 100%;
      background: var(--cream-base);
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
      color: var(--forest-green);
      background: rgba(196, 164, 130, 0.16);
      border: 1px solid rgba(196, 164, 130, 0.45);
      margin-bottom: 1.5rem;
      box-shadow: 0 2px 8px rgba(30, 52, 43, 0.04);
    }

    .hero__badge-dot {
      width: 8px;
      height: 8px;
      border-radius: 50%;
      background: var(--forest-green);
      box-shadow: 0 0 6px var(--soft-gold);
    }

    .hero__title {
      font-family: var(--font-display);
      font-size: clamp(2.1rem, 4.8vw, 4.4rem);
      font-weight: 700;
      letter-spacing: -0.015em;
      line-height: 1.1;
      margin-bottom: 1.4rem;
      color: var(--forest-green);
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
        font-size: clamp(1.65rem, 6.2vw, 2.1rem);
        line-height: 1.18;
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
      background: linear-gradient(135deg, var(--forest-green) 0%, var(--soft-gold-dark) 50%, var(--soft-gold) 100%);
      -webkit-background-clip: text;
      -webkit-text-fill-color: transparent;
    }

    .hero__lead {
      font-size: clamp(1.05rem, 1.4vw, 1.25rem);
      line-height: 1.65;
      color: var(--text-espresso);
      margin-bottom: 1.5rem;
    }

    .hero__area {
      display: flex;
      align-items: center;
      gap: 0.6rem;
      font-size: 0.92rem;
      color: var(--text-taupe);
      font-weight: 600;
      margin-bottom: 2rem;
    }

    .hero__area svg {
      color: var(--soft-gold-dark);
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
      border-top: 1px solid var(--border-subtle);
    }

    .hero__assure-item {
      display: flex;
      align-items: center;
      gap: 0.5rem;
      font-size: 0.88rem;
      font-weight: 600;
      color: var(--text-taupe);
    }

    .hero__assure-item svg {
      color: var(--soft-gold-dark);
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
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      box-shadow: 0 16px 40px rgba(30, 52, 43, 0.08), 0 0 24px rgba(196, 164, 130, 0.12);
      overflow: hidden;
    }

    .hero__visual-img {
      width: 100%;
      height: 380px;
      object-fit: cover;
      border-radius: calc(var(--radius-lg) - 6px);
      filter: brightness(0.96);
    }

    .hero__visual-caption {
      position: absolute;
      bottom: 24px;
      left: 24px;
      right: 24px;
      padding: 1.2rem;
      background: rgba(30, 52, 43, 0.9);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border-radius: var(--radius);
      border: 1px solid rgba(196, 164, 130, 0.35);
      display: flex;
      align-items: center;
      justify-content: space-between;
      color: #FBF8F3;
    }

    .hero__visual-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: #FBF8F3;
    }

    .hero__visual-sub {
      font-size: 0.8rem;
      color: var(--soft-gold-light);
    }

    .hero__visual-caption .btn {
      background: var(--soft-gold);
      color: var(--forest-green);
      font-weight: 700;
      border: none;
      padding: 0.5rem 1rem;
    }

    .hero__visual-caption .btn:hover {
      background: var(--soft-gold-light);
    }

    .hero__reel-pill {
      position: absolute;
      top: 22px;
      left: 22px;
      display: inline-flex;
      align-items: center;
      gap: 0.45rem;
      padding: 0.45rem 0.9rem;
      background: rgba(30, 52, 43, 0.92);
      backdrop-filter: blur(10px);
      -webkit-backdrop-filter: blur(10px);
      border: 1px solid rgba(196, 164, 130, 0.55);
      border-radius: 999px;
      color: #FBF8F3;
      font-size: 0.78rem;
      font-weight: 700;
      text-decoration: none;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.25);
      z-index: 2;
      transition: all 0.25s var(--ease);
    }

    .hero__reel-pill:hover {
      background: var(--soft-gold);
      color: var(--forest-green);
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(196, 164, 130, 0.4);
    }

    .hero__reel-pill-icon {
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: var(--soft-gold);
      color: var(--forest-green);
      display: inline-flex;
      align-items: center;
      justify-content: center;
      font-size: 0.65rem;
      transition: all 0.2s ease;
    }

    .hero__reel-pill:hover .hero__reel-pill-icon {
      background: var(--forest-green);
      color: var(--soft-gold);
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
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius);
      padding: 1.6rem;
      transition: all 0.3s var(--ease);
      position: relative;
      box-shadow: 0 4px 16px rgba(30, 52, 43, 0.03);
    }

    .trust__cell:hover {
      border-color: var(--soft-gold);
      transform: translateY(-3px);
      box-shadow: 0 12px 28px rgba(30, 52, 43, 0.08);
    }

    .trust__icon {
      width: 44px;
      height: 44px;
      border-radius: 12px;
      background: var(--card-tint);
      border: 1px solid rgba(196, 164, 130, 0.35);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--forest-green);
      margin-bottom: 1rem;
    }

    .trust__cell h3 {
      font-size: 1.15rem;
      margin-bottom: 0.4rem;
      color: var(--forest-green);
      font-family: var(--font-display);
    }

    .trust__cell p {
      font-size: 0.88rem;
      color: var(--text-taupe);
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
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius);
      overflow: hidden;
      display: flex;
      flex-direction: column;
      transition: all 0.3s var(--ease);
      position: relative;
      box-shadow: 0 4px 20px rgba(30, 52, 43, 0.04);
    }

    .service-card:hover {
      border-color: var(--soft-gold);
      transform: translateY(-4px);
      box-shadow: 0 16px 36px rgba(30, 52, 43, 0.09);
    }

    .service-card__media {
      position: relative;
      height: 220px;
      overflow: hidden;
      background: #14241E;
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
      background: rgba(30, 52, 43, 0.88);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      padding: 0.3rem 0.75rem;
      border-radius: 999px;
      font-size: 0.75rem;
      font-weight: 700;
      color: #FBF8F3;
      border: 1px solid rgba(196, 164, 130, 0.5);
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
      background: var(--card-tint);
      border: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--forest-green);
      flex-shrink: 0;
    }

    .service-card h3 {
      font-size: 1.35rem;
      font-weight: 700;
      color: var(--forest-green);
      font-family: var(--font-display);
    }

    .service-card p {
      font-size: 0.92rem;
      color: var(--text-taupe);
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
      border-top: 1px solid var(--border-subtle);
    }

    .service-card__spec {
      font-size: 0.78rem;
      font-weight: 600;
      color: var(--forest-green);
      background: var(--card-tint);
      padding: 0.25rem 0.65rem;
      border-radius: 6px;
      border: 1px solid var(--border-subtle);
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
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      overflow: hidden;
      box-shadow: 0 16px 44px rgba(30, 52, 43, 0.07);
      position: relative;
    }

    .sim-header {
      padding: 1.25rem 1.6rem;
      background: var(--card-tint);
      border-bottom: 1px solid var(--border-subtle);
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
      color: var(--forest-green);
    }

    .sim-status-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: var(--forest-green);
      box-shadow: 0 0 8px var(--soft-gold);
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
      background: #080808;
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
      background: rgba(30, 52, 43, 0.85);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      padding: 0.35rem 0.75rem;
      border-radius: 999px;
      font-size: 0.76rem;
      font-weight: 600;
      color: #FBF8F3;
      border: 1px solid rgba(196, 164, 130, 0.4);
      pointer-events: none;
      transition: opacity 0.5s ease;
      text-align: center;
      white-space: normal;
    }

    .sim-stage-footer {
      padding: 1.4rem 1.6rem;
      background: #FFFFFF;
      border-top: 1px solid var(--border-subtle);
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
      background: var(--card-tint);
      border: 1px solid var(--border-subtle);
      color: var(--text-espresso);
      transition: all 0.2s ease;
    }

    .sim-trigger-btn:hover {
      background: #E5DFD7;
      border-color: var(--forest-green);
      color: var(--forest-green);
      transform: translateY(-2px);
    }

    .sim-trigger-btn.is-active {
      background: var(--forest-green);
      border-color: var(--forest-green);
      color: #FFFFFF;
      box-shadow: 0 4px 16px rgba(30, 52, 43, 0.25);
    }

    .sim-trigger-btn--finale {
      background: var(--forest-green);
      border-color: var(--soft-gold);
      color: #FFFFFF;
      font-weight: 800;
    }

    .sim-sliders {
      display: grid;
      grid-template-columns: 1fr;
      gap: 1.2rem;
      padding-top: 1rem;
      border-top: 1px solid var(--border-subtle);
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
      color: var(--forest-green);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .sim-control-group input[type="range"] {
      width: 100%;
      height: 6px;
      border-radius: 999px;
      background: var(--border-subtle);
      outline: none;
      -webkit-appearance: none;
    }

    .sim-control-group input[type="range"]::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 18px;
      height: 18px;
      border-radius: 50%;
      background: var(--forest-green);
      border: 2px solid var(--soft-gold);
      box-shadow: 0 0 8px rgba(30, 52, 43, 0.25);
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
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 1.8rem;
      width: 100%;
      min-width: 0;
      max-width: 100%;
      box-sizing: border-box;
      overflow: hidden;
      box-shadow: 0 8px 30px rgba(30, 52, 43, 0.05);
    }

    .calc-presets-title {
      font-size: 0.95rem;
      font-weight: 700;
      color: var(--forest-green);
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
      background: var(--card-tint);
      border: 1px solid var(--border-subtle);
      color: var(--text-taupe);
      transition: all 0.2s ease;
    }

    .calc-preset-chip:hover {
      border-color: var(--forest-green);
      color: var(--forest-green);
    }

    .calc-preset-chip.is-active {
      background: var(--forest-green);
      border-color: var(--forest-green);
      color: #FFFFFF;
      box-shadow: 0 4px 14px rgba(30, 52, 43, 0.25);
    }

    .calc-items-grid {
      display: flex;
      flex-direction: column;
      gap: 1.25rem;
      margin-bottom: 2rem;
    }

    .calc-item {
      background: var(--cream-base);
      border: 1px solid var(--border-subtle);
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
      background: var(--card-tint);
      border: 1px solid var(--border-subtle);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--forest-green);
      flex-shrink: 0;
    }

    .calc-item-name {
      font-weight: 700;
      font-size: 1rem;
      color: var(--text-espresso);
    }

    .calc-item-rate {
      font-size: 0.8rem;
      color: var(--text-taupe);
    }

    .calc-item-count-badge {
      font-family: var(--font-body);
      font-size: 1rem;
      font-weight: 800;
      color: var(--forest-green);
      background: #FFFFFF;
      padding: 0.25rem 0.75rem;
      border-radius: 8px;
      border: 1px solid var(--soft-gold);
      min-width: 52px;
      text-align: center;
    }

    .calc-item-range {
      width: 100%;
      height: 6px;
      border-radius: 999px;
      background: var(--border-subtle);
      outline: none;
      -webkit-appearance: none;
    }

    .calc-item-range::-webkit-slider-thumb {
      -webkit-appearance: none;
      width: 20px;
      height: 20px;
      border-radius: 50%;
      background: var(--forest-green);
      border: 2px solid var(--soft-gold);
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
      color: var(--forest-green);
      text-transform: uppercase;
      letter-spacing: 0.05em;
      margin-bottom: 0.4rem;
    }

    .calc-select {
      width: 100%;
      padding: 0.75rem 1rem;
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      color: var(--text-espresso);
      font-size: 0.95rem;
    }

    .calc-select:focus {
      border-color: var(--forest-green);
    }

    /* Calculator Summary Sticky Card — High-Impact Forest Green Banner */
    .calc-summary-card {
      position: sticky;
      top: calc(var(--header-h) + 20px);
      background: var(--forest-green);
      border: 1px solid rgba(196, 164, 130, 0.45);
      border-radius: var(--radius-lg);
      padding: 2rem;
      box-shadow: 0 16px 40px rgba(30, 52, 43, 0.25);
      color: #FBF8F3;
    }

    .calc-summary-header {
      padding-bottom: 1.25rem;
      border-bottom: 1px solid rgba(196, 164, 130, 0.3);
      margin-bottom: 1.25rem;
    }

    .calc-summary-title {
      font-size: 0.88rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--soft-gold);
      margin-bottom: 0.5rem;
    }

    .calc-summary-total {
      font-family: var(--font-display);
      font-size: 2.7rem;
      font-weight: 700;
      color: #FFFFFF;
      line-height: 1.1;
      display: flex;
      align-items: baseline;
      gap: 0.35rem;
    }

    .calc-summary-note {
      font-size: 0.82rem;
      color: var(--soft-gold-light);
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
      color: var(--soft-gold-light);
    }

    .calc-summary-row span:last-child {
      font-weight: 700;
      color: #FFFFFF;
    }

    .calc-inclusions {
      padding-top: 1rem;
      border-top: 1px solid rgba(196, 164, 130, 0.25);
      margin-bottom: 1.6rem;
    }

    .calc-inclusions-title {
      font-size: 0.78rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--soft-gold);
      margin-bottom: 0.5rem;
    }

    .calc-inclusions-list {
      display: flex;
      flex-direction: column;
      gap: 0.35rem;
      font-size: 0.82rem;
      color: #FBF8F3;
    }

    .calc-inclusions-list li {
      display: flex;
      align-items: center;
      gap: 0.4rem;
    }

    .calc-inclusions-list svg {
      color: var(--soft-gold);
      width: 14px;
      height: 14px;
    }

    .calc-actions {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .calc-actions .btn--wa {
      background: #FFFFFF;
      color: var(--forest-green);
      border: 1px solid var(--soft-gold);
    }

    .calc-actions .btn--outline {
      border: 1px solid rgba(196, 164, 130, 0.6);
      color: #FBF8F3;
      background: rgba(255, 255, 255, 0.08);
    }

    .calc-actions .btn--outline:hover {
      background: rgba(255, 255, 255, 0.16);
      border-color: #FFFFFF;
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
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      color: var(--text-taupe);
      transition: all 0.2s ease;
    }

    .gallery-filter-btn:hover {
      border-color: var(--forest-green);
      color: var(--forest-green);
    }

    .gallery-filter-btn.is-active {
      background: var(--forest-green);
      border-color: var(--forest-green);
      color: #FFFFFF;
      box-shadow: 0 4px 14px rgba(30, 52, 43, 0.25);
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
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      cursor: pointer;
      aspect-ratio: 4 / 3;
      transition: all 0.35s var(--ease);
      box-shadow: 0 4px 20px rgba(30, 52, 43, 0.04);
    }

    .gallery-card:hover {
      transform: translateY(-5px);
      border-color: var(--soft-gold);
      box-shadow: 0 16px 36px rgba(30, 52, 43, 0.1);
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
      background: linear-gradient(180deg, transparent 40%, rgba(30, 52, 43, 0.95) 100%);
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
      color: var(--soft-gold);
      margin-bottom: 0.25rem;
    }

    .gallery-card__title {
      font-family: var(--font-display);
      font-size: 1.25rem;
      font-weight: 700;
      color: #FBF8F3;
      margin-bottom: 0.2rem;
    }

    .gallery-card__venue {
      font-size: 0.82rem;
      color: var(--soft-gold-light);
    }

    .gallery-card__zoom {
      position: absolute;
      top: 14px;
      right: 14px;
      width: 36px;
      height: 36px;
      border-radius: 50%;
      background: rgba(251, 248, 243, 0.9);
      backdrop-filter: blur(8px);
      border: 1px solid var(--soft-gold);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--forest-green);
      opacity: 0;
      transform: scale(0.8);
      transition: all 0.25s var(--ease);
    }

    .gallery-card:hover .gallery-card__zoom {
      opacity: 1;
      transform: scale(1);
    }

    /* ======================================================================
       LIVE VIDEO REELS SHOWCASE
       ====================================================================== */
    .reels__grid {
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 1.5rem;
      margin-top: 1.5rem;
    }

    @media (max-width: 991px) {
      .reels__grid {
        grid-template-columns: repeat(2, 1fr);
        gap: 1.25rem;
      }
    }

    .reel-card {
      position: relative;
      border-radius: var(--radius-lg);
      overflow: hidden;
      background: #14241E;
      aspect-ratio: 9 / 16;
      border: 1px solid rgba(196, 164, 130, 0.3);
      box-shadow: 0 10px 30px rgba(30, 52, 43, 0.12);
      cursor: pointer;
      transition: all 0.35s var(--ease);
      display: flex;
      flex-direction: column;
    }

    .reel-card:hover {
      transform: translateY(-8px);
      border-color: var(--soft-gold);
      box-shadow: 0 20px 45px rgba(30, 52, 43, 0.28);
    }

    .reel-card__video {
      width: 100%;
      height: 100%;
      object-fit: cover;
      display: block;
      transition: transform 0.5s var(--ease);
    }

    .reel-card:hover .reel-card__video {
      transform: scale(1.05);
    }

    .reel-card__overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(180deg, rgba(30, 52, 43, 0.35) 0%, transparent 35%, rgba(20, 36, 30, 0.95) 100%);
      display: flex;
      flex-direction: column;
      justify-content: space-between;
      padding: 1.25rem;
      pointer-events: none;
      transition: background 0.3s ease;
    }

    .reel-card__top {
      display: flex;
      align-items: center;
      justify-content: space-between;
      width: 100%;
    }

    .reel-card__badge {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: rgba(30, 52, 43, 0.88);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      color: var(--soft-gold);
      border: 1px solid rgba(196, 164, 130, 0.45);
      border-radius: 999px;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.25rem 0.65rem;
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .reel-card__badge-live {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #E55353;
      box-shadow: 0 0 8px #E55353;
      display: inline-block;
      animation: pulse-dot 1.8s infinite;
    }

    .reel-card__duration {
      background: rgba(0, 0, 0, 0.6);
      color: #FBF8F3;
      border-radius: 999px;
      padding: 0.2rem 0.55rem;
      font-size: 0.72rem;
      font-weight: 600;
    }

    .reel-card__play {
      align-self: center;
      width: 54px;
      height: 54px;
      border-radius: 50%;
      background: rgba(196, 164, 130, 0.92);
      color: var(--forest-green);
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 0 24px rgba(196, 164, 130, 0.6);
      transition: all 0.3s var(--ease);
      opacity: 0.95;
    }

    .reel-card:hover .reel-card__play {
      transform: scale(1.15);
      background: #FFFFFF;
      opacity: 1;
      box-shadow: 0 0 32px rgba(255, 255, 255, 0.8);
    }

    .reel-card__meta {
      display: flex;
      flex-direction: column;
      gap: 0.2rem;
    }

    .reel-card__title {
      font-family: var(--font-display);
      font-size: 1.15rem;
      font-weight: 700;
      color: #FBF8F3;
      line-height: 1.25;
      margin: 0;
    }

    .reel-card__sub {
      font-size: 0.8rem;
      color: var(--soft-gold);
      margin: 0;
    }

    .reel-card__venue {
      font-size: 0.75rem;
      color: var(--soft-gold-light);
      margin: 0;
    }

    /* Video badges on gallery cards */
    .gallery-card--video .gallery-card__video-badge {
      position: absolute;
      top: 14px;
      left: 14px;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      background: rgba(30, 52, 43, 0.9);
      backdrop-filter: blur(8px);
      -webkit-backdrop-filter: blur(8px);
      color: var(--soft-gold);
      border: 1px solid rgba(196, 164, 130, 0.5);
      border-radius: 999px;
      font-size: 0.72rem;
      font-weight: 700;
      padding: 0.25rem 0.65rem;
      z-index: 2;
    }

    /* Lightbox Video */
    .lightbox__video {
      max-width: 90vw;
      max-height: 65vh;
      aspect-ratio: 9 / 16;
      border-radius: var(--radius);
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
      border: 1px solid rgba(196, 164, 130, 0.5);
      outline: none;
      background: #000000;
    }

    /* Fullscreen Lightbox Modal */
    .lightbox {
      position: fixed;
      inset: 0;
      background: rgba(20, 36, 30, 0.96);
      backdrop-filter: blur(20px);
      -webkit-backdrop-filter: blur(20px);
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
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(196, 164, 130, 0.4);
      color: #FBF8F3;
      display: flex;
      align-items: center;
      justify-content: center;
      z-index: 10;
      transition: all 0.2s ease;
    }

    .lightbox__close:hover {
      background: var(--soft-gold);
      color: var(--forest-green);
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
      box-shadow: 0 20px 60px rgba(0, 0, 0, 0.6);
      border: 1px solid rgba(196, 164, 130, 0.4);
    }

    .lightbox__caption {
      margin-top: 1.25rem;
      text-align: center;
      max-width: 600px;
    }

    .lightbox__title {
      font-family: var(--font-display);
      font-size: 1.5rem;
      font-weight: 700;
      color: #FBF8F3;
      margin-bottom: 0.35rem;
    }

    .lightbox__desc {
      font-size: 0.92rem;
      color: var(--soft-gold-light);
      margin-bottom: 1rem;
    }

    .lightbox__nav-btn {
      position: absolute;
      top: 50%;
      transform: translateY(-50%);
      width: 48px;
      height: 48px;
      border-radius: 50%;
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(196, 164, 130, 0.4);
      color: #FBF8F3;
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }

    .lightbox__nav-btn:hover {
      background: var(--soft-gold);
      color: var(--forest-green);
      transform: translateY(-50%) scale(1.1);
    }

    .lightbox__nav-btn--prev { left: -60px; }
    .lightbox__nav-btn--next { right: -60px; }

    @media (max-width: 1100px) {
      .lightbox__nav-btn--prev { left: 16px; }
      .lightbox__nav-btn--next { right: 16px; }
    }

    /* ==========================================================================
       13. DIRECT EVENT BOOKING & CALLBACK REQUEST FORM (High-Impact Banner)
       ========================================================================== */
    .booking-card {
      background: var(--forest-green);
      border: 1px solid rgba(196, 164, 130, 0.45);
      border-radius: var(--radius-lg);
      padding: clamp(1.8rem, 4vw, 3rem);
      box-shadow: 0 20px 60px rgba(30, 52, 43, 0.25);
      color: #FBF8F3;
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
      color: var(--soft-gold);
      text-transform: uppercase;
      letter-spacing: 0.05em;
    }

    .form-input, .form-select, .form-textarea, .calc-select {
      width: 100%;
      padding: 0.85rem 1.1rem;
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-sm);
      color: var(--text-espresso);
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
      border-color: var(--soft-gold);
      box-shadow: 0 0 12px rgba(196, 164, 130, 0.35);
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
      background: rgba(255, 255, 255, 0.1);
      border: 1px solid rgba(196, 164, 130, 0.35);
      color: #FBF8F3;
      cursor: pointer;
      transition: all 0.2s ease;
      user-select: none;
    }

    .fx-chip-checkbox:checked + .fx-chip-label {
      background: var(--soft-gold);
      border-color: var(--soft-gold);
      color: var(--forest-green);
      font-weight: 700;
      box-shadow: 0 0 10px rgba(196, 164, 130, 0.4);
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

    .booking-actions .btn--primary {
      background: var(--soft-gold);
      color: var(--forest-green);
      font-weight: 700;
      border: none;
    }

    .booking-actions .btn--primary:hover {
      background: var(--soft-gold-light);
      color: var(--forest-green);
    }

    .booking-actions .btn--wa {
      background: rgba(255, 255, 255, 0.12);
      border: 1px solid rgba(251, 248, 243, 0.5);
      color: #FBF8F3;
    }

    .booking-actions .btn--wa:hover {
      background: rgba(255, 255, 255, 0.2);
      color: #FFFFFF;
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
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius);
      padding: 1.8rem;
      display: flex;
      flex-direction: column;
      position: relative;
      transition: all 0.3s var(--ease);
      box-shadow: 0 4px 18px rgba(30, 52, 43, 0.04);
    }

    .review-card:hover {
      border-color: var(--soft-gold);
      transform: translateY(-3px);
      box-shadow: 0 12px 30px rgba(30, 52, 43, 0.08);
    }

    .review-card__stars {
      display: flex;
      gap: 0.25rem;
      color: var(--soft-gold-dark);
      margin-bottom: 1rem;
    }

    .review-card__text {
      font-size: 0.94rem;
      color: var(--text-espresso);
      line-height: 1.6;
      margin-bottom: 1.5rem;
      flex: 1;
    }

    .review-card__footer {
      display: flex;
      align-items: center;
      justify-content: space-between;
      border-top: 1px solid var(--border-subtle);
      padding-top: 1rem;
    }

    .review-card__author {
      font-family: var(--font-display);
      font-weight: 700;
      font-size: 1.05rem;
      color: var(--forest-green);
    }

    .review-card__meta {
      font-size: 0.8rem;
      color: var(--text-taupe);
    }

    .review-badge-new {
      display: inline-block;
      font-size: 0.72rem;
      font-weight: 700;
      color: var(--forest-green);
      background: rgba(196, 164, 130, 0.2);
      border: 1px solid var(--soft-gold);
      padding: 0.15rem 0.5rem;
      border-radius: 999px;
      margin-left: 0.4rem;
    }

    /* Modal dialog */
    .modal-backdrop {
      position: fixed;
      inset: 0;
      background: rgba(20, 36, 30, 0.75);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
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
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: clamp(1.2rem, 4vw, 2.2rem);
      max-width: min(540px, calc(100vw - 28px));
      width: 100%;
      box-sizing: border-box;
      position: relative;
      box-shadow: 0 24px 70px rgba(30, 52, 43, 0.2);
      color: var(--text-espresso);
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
      background: var(--card-tint);
      border: 1px solid var(--border-subtle);
      color: var(--forest-green);
      display: flex;
      align-items: center;
      justify-content: center;
      transition: all 0.2s ease;
    }

    .modal-close:hover {
      background: var(--forest-green);
      color: #FFFFFF;
    }

    /* Star rating widget in modal */
    .star-rating-select {
      display: flex;
      gap: 0.5rem;
      margin-top: 0.2rem;
    }

    .star-btn {
      color: rgba(196, 164, 130, 0.35);
      cursor: pointer;
      transition: color 0.15s ease, transform 0.15s ease;
    }

    .star-btn.is-active, .star-btn:hover {
      color: var(--soft-gold-dark);
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
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: 999px;
      color: var(--text-espresso);
      font-size: 1rem;
      transition: all 0.2s ease;
      box-shadow: 0 2px 10px rgba(0, 0, 0, 0.03);
    }

    .faq-search-input:focus {
      border-color: var(--forest-green);
      box-shadow: 0 0 16px rgba(30, 52, 43, 0.12);
    }

    .faq-search-icon {
      position: absolute;
      left: 1.25rem;
      top: 50%;
      transform: translateY(-50%);
      color: var(--text-taupe);
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
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius);
      overflow: hidden;
      transition: all 0.25s ease;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.02);
    }

    .acc:hover {
      border-color: var(--soft-gold);
    }

    .acc.is-open {
      border-color: var(--forest-green);
      box-shadow: 0 4px 16px rgba(30, 52, 43, 0.06);
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
      font-size: 1.15rem;
      color: var(--forest-green);
    }

    .acc__icon {
      transition: transform 0.3s ease;
      color: var(--soft-gold-dark);
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
      color: var(--text-taupe);
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
      background: #FFFFFF;
      border: 1px solid var(--border-subtle);
      border-radius: var(--radius-lg);
      padding: 2.2rem;
      box-shadow: 0 6px 24px rgba(30, 52, 43, 0.05);
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
      background: var(--card-tint);
      border: 1px solid rgba(196, 164, 130, 0.4);
      display: flex;
      align-items: center;
      justify-content: center;
      color: var(--forest-green);
      flex-shrink: 0;
    }

    .contact__item-label {
      font-size: 0.8rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--text-taupe);
      margin-bottom: 0.2rem;
    }

    .contact__item-val {
      font-size: 1.05rem;
      font-weight: 600;
      color: var(--forest-green);
    }

    .contact__item-val a:hover {
      color: var(--soft-gold-dark);
    }

    .map-box {
      border-radius: var(--radius-lg);
      overflow: hidden;
      border: 1px solid var(--border-subtle);
      height: 100%;
      min-height: 420px;
      background: var(--card-tint);
      position: relative;
      box-shadow: 0 8px 24px rgba(30, 52, 43, 0.06);
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
      background: rgba(255, 255, 255, 0.96);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid var(--soft-gold);
      border-radius: var(--radius);
      padding: 1.1rem 1.3rem;
      z-index: 5;
      box-shadow: 0 10px 30px rgba(30, 52, 43, 0.1);
    }

    .map-overlay-title {
      display: flex;
      align-items: center;
      gap: 0.65rem;
      font-family: var(--font-display);
      font-size: 1.05rem;
      font-weight: 700;
      color: var(--forest-green);
      margin-bottom: 0.35rem;
    }

    .map-overlay-address {
      font-size: 0.82rem;
      color: var(--text-taupe);
      line-height: 1.45;
      margin-bottom: 0.85rem;
    }

    .map-overlay-actions {
      display: flex;
      gap: 0.5rem;
      flex-wrap: wrap;
    }

    /* ==========================================================================
       17. FOOTER (Deep Forest Green Brand Dark)
       ========================================================================== */
    .footer {
      background: var(--forest-green);
      border-top: 1px solid rgba(196, 164, 130, 0.35);
      padding: 4.5rem 0 3rem;
      position: relative;
      z-index: 1;
      color: #FBF8F3;
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

    .footer .brand__name {
      color: #FBF8F3;
    }

    .footer .brand__tag {
      color: var(--soft-gold-light);
    }

    .footer__brand p {
      font-size: 0.92rem;
      color: var(--soft-gold-light);
      margin-top: 1rem;
      line-height: 1.6;
    }

    .footer__title {
      font-family: var(--font-display);
      font-size: 1.1rem;
      font-weight: 700;
      text-transform: uppercase;
      letter-spacing: 0.08em;
      color: var(--soft-gold);
      margin-bottom: 1.25rem;
    }

    .footer__list {
      display: flex;
      flex-direction: column;
      gap: 0.75rem;
    }

    .footer__list a {
      font-size: 0.92rem;
      color: #FBF8F3;
      transition: color 0.2s ease, transform 0.2s ease;
    }

    .footer__list a:hover {
      color: var(--soft-gold);
      transform: translateX(4px);
    }

    .footer__bottom {
      padding-top: 2rem;
      border-top: 1px solid rgba(196, 164, 130, 0.2);
      display: flex;
      flex-direction: column;
      gap: 1rem;
      align-items: center;
      text-align: center;
      font-size: 0.88rem;
      color: rgba(251, 248, 243, 0.7);
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
      background: rgba(251, 248, 243, 0.96);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      border-top: 1px solid var(--border-subtle);
      padding: 0.75rem var(--gutter) max(0.75rem, env(safe-area-inset-bottom, 0px));
      display: flex;
      gap: 0.75rem;
      z-index: 90;
      box-shadow: 0 -4px 20px rgba(30, 52, 43, 0.08);
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
      background: #FFFFFF;
      border: 1.5px solid var(--forest-green);
      color: var(--forest-green);
      font-weight: 700;
      font-size: 0.92rem;
      box-shadow: 0 8px 24px rgba(30, 52, 43, 0.12);
      transition: all 0.25s var(--ease);
    }

    .float-wa svg {
      color: #25D366;
    }

    @media (min-width: 768px) {
      .float-wa {
        display: flex;
      }
    }

    .float-wa:hover {
      background: var(--forest-green);
      border-color: var(--soft-gold);
      color: #FFFFFF;
      transform: translateY(-3px) scale(1.03);
      box-shadow: 0 12px 30px rgba(30, 52, 43, 0.22);
    }

    .float-wa:hover svg {
      color: #FFFFFF;
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
      background: var(--forest-green);
      border: 1px solid var(--soft-gold);
      color: #FBF8F3;
      padding: 0.85rem 1.6rem;
      border-radius: 999px;
      font-size: 0.9rem;
      font-weight: 600;
      box-shadow: 0 10px 30px rgba(30, 52, 43, 0.25);
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
        font-size: 1.15rem !important;
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
        font-size: clamp(1.65rem, 6.2vw, 2.1rem) !important;
        line-height: 1.18 !important;
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
      /* Video Reels Mobile */
      .reels__grid {
        grid-template-columns: 1fr !important;
        gap: 1.25rem !important;
        width: 100% !important;
      }
      .reel-card {
        width: 100% !important;
        max-width: 100% !important;
        aspect-ratio: 9 / 14 !important;
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
