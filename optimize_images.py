import os
import sys

# Ensure vendor PIL is in path
vendor_path = os.path.join(os.path.dirname(__file__), "vendor")
if vendor_path not in sys.path:
    sys.path.insert(0, vendor_path)

from PIL import Image

assets_dir = "assets"
reels_dir = "assets/reels"

# List of files to optimize
total_orig = 0
total_webp = 0
total_jpg = 0

def optimize_file(file_path):
    global total_orig, total_webp, total_jpg
    orig_size = os.path.getsize(file_path)
    total_orig += orig_size
    
    with Image.open(file_path) as im:
        # Convert RGBA/P to RGB if converting to JPG
        if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):
            # For PNG with alpha, keep RGBA for WebP, RGB with white background for JPG
            im_rgba = im.convert('RGBA')
            im_rgb = Image.new('RGB', im_rgba.size, (251, 248, 243))
            im_rgb.paste(im_rgba, mask=im_rgba.split()[3])
        else:
            im_rgb = im.convert('RGB')
            im_rgba = im_rgb

        # Resize if max dimension > 960px (except logo which is small anyway)
        max_dim = 960
        w, h = im_rgb.size
        if max(w, h) > max_dim:
            if w > h:
                new_w = max_dim
                new_h = int(h * (max_dim / w))
            else:
                new_h = max_dim
                new_w = int(w * (max_dim / h))
            im_rgb = im_rgb.resize((new_w, new_h), Image.Resampling.LANCZOS)
            im_rgba = im_rgba.resize((new_w, new_h), Image.Resampling.LANCZOS)

        base_name, _ = os.path.splitext(file_path)
        webp_path = base_name + ".webp"
        jpg_path = base_name + ".jpg"

        # Save WebP
        im_rgba.save(webp_path, format="WEBP", quality=82, method=6)
        webp_size = os.path.getsize(webp_path)
        total_webp += webp_size

        # Save optimized JPG
        im_rgb.save(jpg_path, format="JPEG", quality=82, optimize=True, progressive=True)
        jpg_size = os.path.getsize(jpg_path)
        total_jpg += jpg_size

        reduction = (1 - webp_size / orig_size) * 100
        print(f"{os.path.basename(file_path):<36} {orig_size/1024:>6.1f} KB -> WebP: {webp_size/1024:>5.1f} KB ({reduction:>4.1f}% reduction)")

print("=== OPTIMIZING MAIN ASSETS ===")
for f in sorted(os.listdir(assets_dir)):
    p = os.path.join(assets_dir, f)
    if os.path.isfile(p) and f.lower().endswith(('.jpg', '.jpeg', '.png')) and not f.endswith('.webp'):
        optimize_file(p)

print("\n=== OPTIMIZING REEL POSTERS ===")
for f in sorted(os.listdir(reels_dir)):
    p = os.path.join(reels_dir, f)
    if os.path.isfile(p) and f.lower().endswith(('.jpg', '.jpeg', '.png')) and not f.endswith('.webp'):
        optimize_file(p)

print("\n" + "="*50)
print(f"TOTAL ORIGINAL:   {total_orig / (1024*1024):.2f} MB")
print(f"TOTAL WEBP:       {total_webp / (1024*1024):.2f} MB  (Saved {(1 - total_webp/total_orig)*100:.1f}%)")
print(f"TOTAL OPTIMIZED:  {total_jpg / (1024*1024):.2f} MB")
print("="*50)
