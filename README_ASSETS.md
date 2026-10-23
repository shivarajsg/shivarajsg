# Profile Assets & Maintenance Guide

This document explains the assets and deployment steps for Shivaraj's GitHub profile README repository (`shivarajsg/shivarajsg`).

---

## 📂 Repository Structure

```
shivarajsg/
├── assets/
│   └── header.svg            # Custom, lightweight vector hero banner (pure SVG, 0 dependencies)
├── README.md                 # The main GitHub profile showcase
└── README_ASSETS.md          # Asset documentation and deployment instructions
```

---

## 🎨 Asset Details: `assets/header.svg`

- **Format:** Pure SVG (`<svg viewBox="0 0 840 200">`)
- **Dimensions:** 840px × 200px (responsive on all screen sizes, desktop & mobile)
- **Design Aesthetic:** Deep slate/obsidian (`#0b0f19` to `#0f172a`) with subtle 24px grid overlay, rounded corners (`rx="14"`), and glowing electric cyan (`#38bdf8`) / indigo (`#818cf8`) accents.
- **Typography:** Uses native system font stack (`-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif`), guaranteeing instant rendering with 0 external font latency or blocking.
- **File size:** ~3.5 KB (extremely lightweight, loads instantly).

### Modifying the Banner
To edit the banner text, colors, or pills:
1. Open `assets/header.svg` in any code editor.
2. Edit the `<text>` elements (e.g. your name, title, or pill labels).
3. The linear gradients `cyan-glow` and `bg-grad` in the `<defs>` section control the color scheme.

---

## 🚀 Step-by-Step Deployment Guide

Since the special profile repository `shivarajsg/shivarajsg` does not exist yet on GitHub, follow these 3 quick steps to activate your profile:

### Step 1: Create the Special Profile Repository on GitHub
1. Go to **[https://github.com/new](https://github.com/new)**.
2. In the **Repository name** field, type: `shivarajsg`
   > *GitHub will display a green banner stating: "You found a secret! shivarajsg/shivarajsg is a special repository that you can use to add a README.md to your GitHub profile."*
3. Make sure the repository visibility is set to **Public**.
4. Check **Add a README file** (or leave it unchecked if you are pushing via Git).
5. Click **Create repository**.

### Step 2: Push or Upload Files
From this local folder (`c:\Users\KumarShiva\Downloads\self_readme`):

#### Option A: Using Git CLI
```bash
cd c:\Users\KumarShiva\Downloads\self_readme
git init
git checkout -b main
git remote add origin https://github.com/shivarajsg/shivarajsg.git
git add README.md assets/header.svg README_ASSETS.md
git commit -m "docs: launch premium developer profile README and assets"
git push -u origin main
```

#### Option B: GitHub Web UI
1. Navigate to your new `shivarajsg/shivarajsg` repository on GitHub.
2. Click **Add file** → **Upload files**.
3. Drag and drop `README.md`, `README_ASSETS.md`, and the `assets/` folder (with `header.svg`).
4. Commit changes directly to `main`.

### Step 3: Verify Your Profile
Visit **[https://github.com/shivarajsg](https://github.com/shivarajsg)**. Your new profile portfolio will immediately be live!
