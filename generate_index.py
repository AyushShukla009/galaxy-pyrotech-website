# Generator for Galaxy Pyrotech Traders official fully-functional luxury website
import sys

def get_html_head():
    return '''<!DOCTYPE html>
<!--
  GALAXY PYROTECH TRADERS — Official Luxury Website
  Palette:
    Primary Background: Deep Black (#030201)
    Secondary Background: Espresso Black (#190B05)
    Dark Brown: Rich Coffee Brown (#34190A)
    Warm Brown: Burnt Brown (#592B0E)
    Primary Accent: Warm Amber (#DE8026)
    Secondary Accent: Burnt Gold (#8C4A1A)
    Gold Highlight: Champagne Gold (#CBA482)
    Light Gold: Warm Champagne (#E3C9A8)
    Primary Text: Warm Ivory (#F0EEEC)
    Secondary Text: Soft Beige (#C5B6A7)
  Features:
    - Official Logo Frame & Branding
    - Real Photography Assets (Cold Pyro, Low Fog, Sparkular, Sky Fireworks, Colour Smoke, Varmala Stage)
    - Interactive FX Live Stage Simulator (Cold Pyro, Low Fog, Sparkular, Fireworks, Smoke, Confetti, Finale)
    - Interactive Package & Instant Cost Calculator with WhatsApp quote generator
    - Filterable Portfolio Showcase Gallery with Fullscreen Lightbox Modal
    - Direct Event Booking & 24/7 Instant Callback Request System
    - Interactive Client Review System with "Write a Review" Modal & LocalStorage persistence
    - Live Searchable FAQ Accordion
    - Responsive Sector 22 Noida Google Map Embed
    - Web Audio API Synthesized Pyrotechnic Sound Effects Engine
-->
<html lang="en-IN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
  <meta name="color-scheme" content="light">
  <meta name="theme-color" content="#FBF8F3">

  <title>Galaxy Pyrotech Traders | Luxury Wedding &amp; Event Special Effects Noida &amp; Delhi NCR</title>
  <meta name="description" content="Galaxy Pyrotech Traders delivers luxury special effects for grand weddings, royal varmala entries, receptions, and celebrations across Noida, Greater Noida, Delhi NCR &amp; Pan-India. Cold Pyro, Sparkular, Low Fog Dry Ice, Sky Fireworks &amp; Colour Smoke.">

  <!-- Canonical URL -->
  <link rel="canonical" href="https://galaxypyrotech.com/">

  <!-- Open Graph / Social sharing -->
  <meta property="og:type" content="website">
  <meta property="og:site_name" content="Galaxy Pyrotech Traders">
  <meta property="og:title" content="Galaxy Pyrotech Traders | Luxury Wedding &amp; Event Special Effects">
  <meta property="og:description" content="Premier special effects: Cold Pyro, Low Fog Dry Ice, Sparkular, Sky Fireworks, and Colour Smoke across Noida, Delhi NCR &amp; Destination Weddings.">
  <meta property="og:url" content="https://galaxypyrotech.com/">
  <meta property="og:locale" content="en_IN">
  <meta property="og:image" content="assets/varmala_stage.jpg">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="Galaxy Pyrotech Traders | Luxury Wedding &amp; Event Special Effects">
  <meta name="twitter:description" content="Premier special effects for luxury weddings and events in Noida &amp; Delhi NCR.">
  <meta name="twitter:image" content="assets/varmala_stage.jpg">

  <!-- Favicon: Official Galaxy Pyrotech logo -->
  <link rel="icon" type="image/jpeg" href="assets/logo.jpg">
  <link rel="apple-touch-icon" href="assets/logo.jpg">

  <!-- Fonts: Cormorant Garamond (Editorial Luxury Serif) + Plus Jakarta Sans (Clean Body) -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;0,700;1,500;1,600&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Structured data -->
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Galaxy Pyrotech Traders",
    "url": "https://galaxypyrotech.com/",
    "logo": "assets/logo.jpg",
    "image": "assets/varmala_stage.jpg",
    "telephone": "+919582673570",
    "email": "galaxypyrotech@gmail.com",
    "slogan": "Light up the moments",
    "description": "Luxury special effects for royal weddings, grand varmala entries, stage celebrations and events. Cold Pyro, Low Fog, Sparkular, Sky Fireworks and Colour Smoke.",
    "priceRange": "\u20b9\u20b9",
    "openingHours": "Mo,Tu,We,Th,Fr,Sa,Su 00:00-23:59",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "12, Amaltash Marg, Chaura Raghunathpur, Sector 22",
      "addressLocality": "Noida",
      "addressRegion": "Uttar Pradesh",
      "postalCode": "201307",
      "addressCountry": "IN"
    },
    "geo": {
      "@type": "GeoCoordinates",
      "latitude": "28.5960",
      "longitude": "77.3489"
    },
    "sameAs": [
      "https://www.instagram.com/galaxypyrotechtraders",
      "https://maps.google.com/?q=Galaxy+Pyrotech+Noida"
    ]
  }
  </script>
'''

if __name__ == '__main__':
    print("Head template loaded")
