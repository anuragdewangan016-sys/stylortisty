# Media Gallery - Host & Share via QR Code

A mobile-friendly photo & video gallery that works globally via QR code.

## Setup Steps

### 1. Add your photos/videos
Place your media files (`.jpg`, `.png`, `.mp4`, etc.) into the `media/` folder.

### 2. Edit `index.html`
Uncomment and fill in the items in the `mediaItems` array:

```js
const mediaItems = [
    { type: "photo", src: "media/your-photo.jpg", title: "Beach Trip", date: "2024" },
    { type: "video", src: "media/your-video.mp4", title: "Birthday Party", date: "2024" },
];
```

### 3. Deploy to GitHub Pages (Free & Global)

1. Create a GitHub account at https://github.com
2. Create a **new repository** named `my-gallery`
3. Push this project to the repo:
   ```bash
   git init
   git add .
   git commit -m "Initial gallery"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/my-gallery.git
   git push -u origin main
   ```
4. Go to **Settings > Pages** in your repo
5. Under "Source", select **Deploy from a branch**, choose `main`, folder `/ (root)`
6. Your gallery is now live at: `https://YOUR_USERNAME.github.io/my-gallery/`

### 4. Generate QR Code

```bash
pip install qrcode[pil]
python generate_qr.py https://YOUR_USERNAME.github.io/my-gallery/
```

This creates `qr_code.png` - print it, share it, anyone can scan it with their phone camera!

## Features
- Works on all phones (camera app scans QR natively)
- Photo grid with lightbox viewer
- Video playback with hover preview
- Filter by photos/videos
- Mobile responsive
- Free hosting via GitHub Pages
