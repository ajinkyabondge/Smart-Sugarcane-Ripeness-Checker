# 🌾 Smart-Sugarcane-Ripeness-Checker

An **intelligent Python-based tool** that analyzes sugarcane images to instantly determine ripeness using **HSV color detection**.  
It provides **accurate, non-destructive, and real-time results**, classifying canes as **Unripe, Partially Ripe, or Fully Ripe** through a clean, interactive **Tkinter GUI** — bridging **technology and agriculture**.

---

## 🎯 Objective
To build a system that detects the **ripeness of sugarcane** using **image color analysis (HSV model)** and classifies it as:
- **Unripe**
- **Partially Ripe**
- **Fully Ripe**

---

## ⚙️ How It Works
1. The image of a sugarcane stalk is loaded using **OpenCV**.  
2. It’s converted from **BGR → HSV** (Hue, Saturation, Value) — ideal for consistent color detection.  
3. Two color ranges are defined:  
   - 🟩 **Green → Unripe**  
   - 🟨 **Yellow/Brown → Ripe**  
4. Masks are created to identify ripe and unripe regions.  
5. The program counts the pixels in each color range and calculates ripeness using:  
   ripeness_percentage = (ripe_pixels / total_pixels) * 100
6. Based on the percentage, the cane is classified as:
    - <30% → Unripe
    - 30–70% → Partially Ripe
    - >70% → Fully Ripe

## 🧩 Key Features :

✅ Non-destructive & real-time ripeness detection
✅ No machine learning or dataset required
✅ Accurate color-based HSV analysis
✅ Beautiful Tkinter GUI with progress bar visualization
✅ Option to save analysis reports in .txt format
✅ Works completely offline

## 🛠️ Tech Stack :
  - Python 3
  - OpenCV
  - NumPy
  - Pillow (PIL)
  - Tkinter
  - ttk (for modern widgets)

## 🖼️ Output Screenshots :
