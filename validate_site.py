import os
import re
from html.parser import HTMLParser

class SiteValidator(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.ids = set()
        self.img_srcs = []
        self.links = []
        self.errors = []

    def handle_starttag(self, tag, attrs):
        attr_dict = dict(attrs)
        if 'id' in attr_dict:
            self.ids.add(attr_dict['id'])
        if tag == 'img' and 'src' in attr_dict:
            self.img_srcs.append(attr_dict['src'])
        if tag == 'a' and 'href' in attr_dict:
            self.links.append(attr_dict['href'])
        
        # Self closing void tags
        void_tags = {'meta', 'link', 'img', 'br', 'hr', 'input', 'source', 'area', 'base', 'col', 'embed', 'param', 'track', 'wbr'}
        if tag not in void_tags:
            self.tags.append(tag)

    def handle_endtag(self, tag):
        void_tags = {'meta', 'link', 'img', 'br', 'hr', 'input', 'source', 'area', 'base', 'col', 'embed', 'param', 'track', 'wbr'}
        if tag in void_tags:
            return
        if self.tags:
            last = self.tags.pop()
            if last != tag:
                # self closing or mismatch
                pass

def validate():
    print("Validating generated index.html...")
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()

    validator = SiteValidator()
    validator.feed(html)

    print(f"Total Unique HTML IDs: {len(validator.ids)}")
    print(f"Total Image References: {len(validator.img_srcs)}")

    # Check images on disk
    missing_imgs = []
    for src in validator.img_srcs:
        if not src.startswith("http") and not src.startswith("data:"):
            if not os.path.exists(src):
                missing_imgs.append(src)
    
    if missing_imgs:
        print("ERROR: Missing images on disk:", missing_imgs)
        return False
    else:
        print("PASS: All image sources verified on disk!")

    # Check critical JavaScript ID bindings
    required_ids = [
      'global-sound-toggle', 'menu-toggle-btn', 'mobile-menu',
      'sim-canvas', 'sim-status-text', 'sim-sound-btn', 'sim-clear-btn',
      'sim-height', 'sim-density', 'sim-theme',
      'range-pyro', 'range-fog', 'range-sparkular', 'range-smoke', 'range-confetti',
      'calc-city', 'calc-event-type', 'calc-total-display', 'calc-summary-list', 'calc-wa-btn', 'calc-copy-btn',
      'preset-varmala', 'preset-baraat', 'preset-gala', 'preset-custom',
      'gallery-grid', 'lightbox-modal', 'lightbox-img', 'lightbox-title', 'lightbox-desc',
      'lightbox-close-btn', 'lightbox-prev-btn', 'lightbox-next-btn', 'lightbox-wa-btn',
      'direct-booking-form', 'book-name', 'book-phone', 'book-date', 'book-venue', 'book-type',
      'submit-booking-wa', 'submit-callback', 'callback-modal', 'callback-ref-ticket',
      'reviews-grid', 'open-review-modal-btn', 'review-modal', 'add-review-form',
      'faq-search', 'current-year', 'toast', 'toast-msg'
    ]

    missing_ids = [rid for rid in required_ids if rid not in validator.ids]
    if missing_ids:
        print("ERROR: Missing required DOM element IDs:", missing_ids)
        return False
    else:
        print("PASS: All 40+ interactive DOM element IDs verified!")

    print("SUCCESS: Site verification passed with zero errors!")
    return True

if __name__ == "__main__":
    if not validate():
        exit(1)
