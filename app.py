import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import cv2
import numpy as np
import os
from tkinter import ttk

# --- Ripeness Analysis Function ---
def analyze_sugarcane_ripeness(image_path):
    original_cv_img = cv2.imread(image_path)
    if original_cv_img is None:
        return "Error: Image not found", None, None, None, 0, 0, 0

    # Preprocessing: smooth image
    blurred = cv2.GaussianBlur(original_cv_img, (5, 5), 0)
    hsv_image = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    # Define color ranges
    unripe_lower = np.array([35, 40, 40])
    unripe_upper = np.array([85, 255, 255])
    ripe_lower = np.array([10, 100, 20])
    ripe_upper = np.array([30, 255, 255])

    # Create masks
    unripe_mask = cv2.inRange(hsv_image, unripe_lower, unripe_upper)
    ripe_mask = cv2.inRange(hsv_image, ripe_lower, ripe_upper)

    unripe_pixels = cv2.countNonZero(unripe_mask)
    ripe_pixels = cv2.countNonZero(ripe_mask)
    total_pixels = unripe_pixels + ripe_pixels

    ripeness_percentage = (ripe_pixels / total_pixels) * 100 if total_pixels > 0 else 0

    # Determine grade
    if ripeness_percentage < 30:
        grade = "Unripe"
    elif ripeness_percentage < 70:
        grade = "Partially Ripe"
    else:
        grade = "Fully Ripe"

    result_text = f"Ripeness: {ripeness_percentage:.2f}% ({grade})"
    return result_text, original_cv_img, ripe_mask, unripe_mask, ripeness_percentage, ripe_pixels, unripe_pixels

# --- GUI Functions ---
tk_original_img = None
tk_ripe_mask_img = None
tk_unripe_mask_img = None
current_result = None

def select_image():
    global tk_original_img, tk_ripe_mask_img, tk_unripe_mask_img, current_result

    path = filedialog.askopenfilename(title="Select Sugarcane Image", filetypes=[("Image Files", "*.jpg *.png *.jpeg")])
    if not path:
        return

    result_text, original_cv_img, ripe_mask, unripe_mask, ripeness_pct, ripe_pixels, unripe_pixels = analyze_sugarcane_ripeness(path)

    result_label.config(text=result_text)
    ripe_count_label.config(text=f"Ripe Pixels: {ripe_pixels}")
    unripe_count_label.config(text=f"Unripe Pixels: {unripe_pixels}")

    progress_bar["value"] = ripeness_pct
    progress_label.config(text=f"{ripeness_pct:.1f}%")

    current_result = (path, ripeness_pct, result_text)

    if original_cv_img is not None:
        def to_tk(img_cv):
            rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB) if len(img_cv.shape) == 3 else cv2.cvtColor(img_cv, cv2.COLOR_GRAY2RGB)
            pil_img = Image.fromarray(rgb)
            pil_img.thumbnail((500, 500))  # Larger size
            return ImageTk.PhotoImage(pil_img)

        tk_original_img = to_tk(original_cv_img)
        tk_ripe_mask_img = to_tk(ripe_mask)
        tk_unripe_mask_img = to_tk(unripe_mask)

        original_label.config(image=tk_original_img, text="Sugarcane Original")
        ripe_label.config(image=tk_ripe_mask_img, text="Ripe Regions (Yellow/Brown)")
        unripe_label.config(image=tk_unripe_mask_img, text="Unripe Regions (Green)")
    else:
        messagebox.showerror("Error", "Failed to process image!")

def save_report():
    if not current_result:
        messagebox.showwarning("No Result", "Analyze an image before saving report.")
        return

    path, ripeness_pct, result_text = current_result
    base_name = os.path.basename(path)
    report_content = (
        f"--- Sugarcane Ripeness Report ---\n"
        f"Image: {base_name}\n"
        f"{result_text}\n\n"
        f"Analysis Completed Successfully."
    )
    report_file = "sugarcane_report.txt"
    with open(report_file, "w") as f:
        f.write(report_content)

    messagebox.showinfo("Saved", f"Report saved as '{report_file}' in current folder.")

# --- Tkinter Window Setup ---
root = tk.Tk()
root.title("🌾 Smart Sugarcane Ripeness Checker")
root.state("zoomed")  # Fullscreen
root.configure(bg="#E8F5E9")  # Premium light green

# --- Title Frame ---
title_frame = tk.Frame(root, bg="#A5D6A7", bd=3, relief="ridge")
title_frame.pack(fill="x", pady=10)
title = tk.Label(title_frame, text="🌿 Smart Sugarcane Ripeness Checker 🌿",
                 font=("Helvetica", 26, "bold"), bg="#A5D6A7", fg="#1B5E20")
title.pack(pady=10)

# --- Image Display Frame ---
image_frame = tk.Frame(root, bg="#C8E6C9", bd=3, relief="groove")
image_frame.pack(pady=20)

original_label = tk.Label(image_frame, text="Sugarcane Original", 
                          font=("Helvetica", 14, "bold"), bg="#C8E6C9", compound="top")
ripe_label = tk.Label(image_frame, text="Ripe Regions (Yellow/Brown)", 
                      font=("Helvetica", 14, "bold"), bg="#C8E6C9", compound="top")
unripe_label = tk.Label(image_frame, text="Unripe Regions (Green)", 
                        font=("Helvetica", 14, "bold"), bg="#C8E6C9", compound="top")

original_label.pack(side="left", padx=20)
ripe_label.pack(side="left", padx=20)
unripe_label.pack(side="left", padx=20)

# --- Result Frame ---
result_frame = tk.Frame(root, bg="#E8F5E9", height=80)
result_frame.pack(pady=10, fill="x")
result_label = tk.Label(result_frame, text="Result will appear here",
                        font=("Helvetica", 20, "bold"), bg="#E8F5E9", fg="#1B5E20")
result_label.pack()

# --- Progress Bar Frame ---
progress_frame = tk.Frame(root, bg="#E8F5E9")
progress_frame.pack(pady=10)
style = ttk.Style()
style.theme_use("clam")
style.configure("green.Horizontal.TProgressbar", troughcolor="#C8E6C9", background="#2E7D32", thickness=28)
progress_bar = ttk.Progressbar(progress_frame, length=500, maximum=100, style="green.Horizontal.TProgressbar")
progress_bar.pack(side="left", padx=10)
progress_label = tk.Label(progress_frame, text="0%", font=("Helvetica", 14, "bold"), bg="#E8F5E9", fg="#1B5E20")
progress_label.pack(side="left")

# --- Pixel Stats Frame ---
stats_frame = tk.Frame(root, bg="#E8F5E9")
stats_frame.pack(pady=10)
ripe_count_label = tk.Label(stats_frame, text="Ripe Pixels: 0", font=("Helvetica", 14), bg="#E8F5E9")
unripe_count_label = tk.Label(stats_frame, text="Unripe Pixels: 0", font=("Helvetica", 14), bg="#E8F5E9")
ripe_count_label.pack()
unripe_count_label.pack()

# --- Button Frame ---
button_frame = tk.Frame(root, bg="#E8F5E9")
button_frame.pack(pady=15)
load_btn = tk.Button(button_frame, text="📷 Load Image", font=("Helvetica", 16),
                     command=select_image, bg="#43A047", fg="white", padx=20, pady=8)
load_btn.pack(side="left", padx=15)
save_btn = tk.Button(button_frame, text="💾 Save Report", font=("Helvetica", 16),
                     command=save_report, bg="#2E7D32", fg="white", padx=20, pady=8)
save_btn.pack(side="left", padx=15)

root.mainloop()
