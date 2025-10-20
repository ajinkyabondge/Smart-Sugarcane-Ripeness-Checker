# Smart-Sugarcane-Ripeness-Checker
An intelligent Python-based tool that analyzes sugarcane images to instantly determine ripeness using HSV color detection. It provides accurate, non-destructive, and real-time results, classifying canes as Unripe, Partially Ripe, or Fully Ripe through a clean, interactive Tkinter interface — bridging tech and agriculture.

- Objective :
To build a system that detects the ripeness of sugarcane using image color analysis (HSV model) and classifies it as Unripe, Partially Ripe, or Fully Ripe.

- How It Works :
  1. The image of a sugarcane stalk is loaded using OpenCV.
  2. The image is converted from BGR to HSV (Hue, Saturation, Value) color space — ideal for color detection under varying lighting conditions.
  3. Two color ranges are defined:
        -Green → Unripe
        -Yellow/Brown → Ripe
  4. Masks are created to identify ripe and unripe regions.
  5. The program counts the pixels in each color range to calculate the ripeness percentage using:
       ripeness_percentage = (ripe_pixels / total_pixels) * 100
  6. Based on the percentage, the system grades the sugarcane as:
        - <30% → Unripe
        - 30–70% → Partially Ripe
        - 70% → Fully Ripe

🧩 Key Features :
✅ Non-destructive and real-time ripeness detection
✅ No machine learning or dataset needed
✅ Color-based HSV analysis for accurate results
✅ Beautiful Tkinter GUI with progress bar visualization

🛠️ Tech Stack :
  - Python 3
  - OpenCV
  - NumPy
  - Pillow (PIL)
  - Tkinter
  - ttk (for modern widgets)

🚀 How to Run :
  # 1. Clone the repository
  git clone https://github.com/your-username/Smart-Sugarcane-Ripeness-Checker.git
  cd Smart-Sugarcane-Ripeness-Checker
  
  # 2. Install dependencies
  pip install opencv-python numpy pillow

  # 3. Run the GUI version
  python app.py

  # OR run the basic command-line version
  python checker.py

- OUTPUT SCREENSHOTS :

  

✅ Option to save analysis reports in .txt format
✅ Works completely offline
