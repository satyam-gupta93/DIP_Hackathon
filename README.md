# 🛰️ Satellite Image Enhancement using CLAHE (Contrast Limited Adaptive Histogram Equalization)

This project applies **CLAHE (Contrast Limited Adaptive Histogram Equalization)** and **RGB Histogram Equalization** techniques to enhance the contrast and visibility of features in **satellite images**.  
It improves local contrast and reveals fine terrain or land-cover details that are otherwise hidden in low-contrast imagery.

---

## 🌍 Overview

Satellite images often suffer from uneven lighting, haze, or poor contrast — making terrain or vegetation boundaries difficult to detect.  
By using CLAHE, we enhance local brightness variations, improving the visibility of subtle features like:

- Dunes, ridges, or erosion lines  
- Vegetation and barren land differences  
- Water body boundaries  
- Urban vs. non-urban texture  
- Geological structures or soil types  

The method is especially useful as a **preprocessing step** before:
- Land cover classification  
- Change detection  
- Crop/vegetation monitoring  
- Disaster analysis  
- Deep learning model training  

---

## ⚙️ How It Works

1. Convert the image to **LAB color space** and apply **CLAHE** on the **L (lightness)** channel.  
2. Apply **RGB Histogram Equalization** to further normalize contrast across channels.  
3. Merge the processed channels and save the enhanced image.  
4. The final image highlights fine-scale terrain textures and improves local contrast.

---

## 🧠 Applications of CLAHE in Remote Sensing

| Application | Purpose |
|--------------|----------|
| **Land Use / Land Cover Classification** | Improves separability between vegetation, soil, and urban areas. |
| **Change Detection** | Reduces illumination bias for before-after comparisons. |
| **Vegetation Monitoring** | Enhances NDVI or crop stress mapping. |
| **Geological Mapping** | Reveals ridges, folds, or erosion lines. |
| **Water Body Extraction** | Highlights boundaries of lakes, rivers, and wetlands. |
| **Disaster Assessment** | Enhances visibility of burnt, flooded, or landslide-affected regions. |

---

