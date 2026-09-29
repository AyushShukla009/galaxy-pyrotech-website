# 🎆 Galaxy Pyrotech — Luxury Special Effects & Pyrotechnics

> **Transform Your Event Into A Royal Spectacle**  
> Premier special effects for luxury weddings, royal varmala entries, grand sangeets, and celebrations across Delhi NCR & Pan-India.

[![Live Website](https://img.shields.io/badge/Live_Site-galaxy--pyrotech.vercel.app-DE8026?style=for-the-badge&logo=vercel&logoColor=white)](https://galaxy-pyrotech.vercel.app)
[![License](https://img.shields.io/badge/License-Proprietary-black?style=for-the-badge)](LICENSE)

---

## 🌟 Overview

**Galaxy Pyrotech** is a high-converting, mobile-first web experience crafted for India's premier luxury event special effects company based in Sector 22, Noida. 

Featuring an evocative dark-luxury aesthetic inspired by palace nights, golden embers, and royal celebrations:
- **Base Canvas:** Deep Charcoal Onyx (`#030201`, `#190B05`)
- **Accent Ember & Glow:** Imperial Flame Gold (`#DE8026`, `#E99B4C`)
- **Luxury Muted Gold:** Warm Champagne Stone (`#CBA482`)
- **Typography & High Contrast:** Warm Pearl White (`#F0EEEC`)

---

## ✨ Features

- **Mobile-Optimized Hero:** Visual stage showcase card positioned at the very top on mobile view for immediate emotional impact, followed by high-converting value proposition copy and instant CTAs.
- **Interactive Budget & Package Calculator:** Real-time quote generator calculating custom package costs with multi-service selection, guest count scaling, and WhatsApp prefilled dispatch.
- **Visual Portfolio & Before/After Showcase:** High-resolution interactive visual gallery featuring royal palace entries, sparkular waterfalls, dry ice low fog, and grand sky fireworks.
- **Sound & Ambient FX:** Embedded audio experience toggled via ambient sound player with volume controls.
- **Instant Inquiry Modals & Lead Capture:** Seamless one-tap WhatsApp integration, direct telephonic booking, and interactive inquiry submission form.
- **100% Zero-Dependency Standalone Build:** Generates an ultra-fast, self-contained single-page architecture with inline luxury CSS and optimized scripts.

---

## 📸 Services Offered

1. **Smokeless Cold Pyro & Sparkular Fountains** — 100% cold-spark indoor/outdoor safe stage effects.
2. **Heavy Low Fog (Dry Ice Clouds)** — Cloud-walk romantic stage ambiance for varmalas and first dances.
3. **Grand Aerial Sky Fireworks** — Licensed, synchronized palace sky displays for royal celebrations.
4. **Varmala Special Entry Packages** — Synchronized revolving stage, sparkular waterfalls, and paper confetti blasts.
5. **Colour Smoke & Daytime SFX** — Vibrant daytime smoke trails for haldi ceremonies and baraat entries.
6. **CO2 Jets & Stadium Confetti Blasters** — High-energy bursts for sangeet nights and afterparties.

---

## 🚀 Live Deployment

The website is continuously deployed on Vercel:
🔗 **[https://galaxy-pyrotech.vercel.app](https://galaxy-pyrotech.vercel.app)**

---

## 🛠️ Project Structure

```
├── assets/                  # High-resolution optimized imagery & brand logo
│   ├── logo.jpg             # Circular gold Galaxy Pyrotech emblem
│   ├── varmala_stage.jpg    # Palace varmala stage showcase
│   ├── wedding_entry.jpg    # Bride/groom royal entry with cold sparks
│   ├── low_fog.jpg          # Dry ice heavy cloud effect
│   ├── sparkular_stage.jpg  # Indoor safe cold fireworks
│   ├── sky_fireworks.jpg    # High-altitude palace fireworks
│   └── colour_smoke.jpg     # Daytime colour smoke trails
├── index.html               # Production-ready compiled single-page website
├── content.py               # Modular HTML section components & semantic content
├── styles.py                # Luxury design system, typography, & mobile overrides
├── scripts.py               # Interactive JS (calculator, audio, modals, analytics)
├── assemble_website.py      # Build script to compile source modules into index.html
├── validate_site.py         # Automated QA suite (ID conflicts, broken links, images)
├── vercel.json              # Vercel deployment routing configuration
└── README.md
```

---

## 💻 Local Development & Build

1. **Rebuild `index.html` from source:**
   ```bash
   python3 assemble_website.py
   ```

2. **Run validation tests:**
   ```bash
   python3 validate_site.py
   ```

3. **Preview locally:**
   ```bash
   python3 -m http.server 8000
   ```
   Open `http://localhost:8000` in your browser.

---

## 📞 Contact & Bookings

- **Location:** Sector 22, Noida, Uttar Pradesh 201301
- **Service Coverage:** Noida, Greater Noida, Delhi NCR, and Destination Weddings across India
- **WhatsApp / Phone:** Direct inquiries available via website CTAs

---

© 2026 Galaxy Pyrotech. All rights reserved.
