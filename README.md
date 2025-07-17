#  Sleep-Based Mood Prediction App

This project is a **machine learning-powered web app** that predicts your **mood** based on your **sleep habits** using a trained **K-Nearest Neighbors (KNN)** model with a **Flask** backend and a simple **HTML + jQuery** frontend.

---

##  Features

- Predicts mood states: `HAPPY`, `JOYFUL`, `PEACEFUL`, or `SLEEPY`
- Input fields for:
  - **Bedtime** (e.g. 23 for 11 PM)
  - **Quality of Sleep** (scale 1–10)
  - **Pre-bed Technology Use** (Yes/No or 1/0)
  - **Wake-up Time** (e.g. 6.5 for 6:30 AM)
- Fully local and lightweight
- Accepts both `"yes"/"no"` and `1/0` for tech input

---

##  Tech Stack

- **Python 3**
- **Flask**
- **scikit-learn**
- **HTML5 / CSS3**
- **JavaScript / jQuery**

---

##  Model Info

- Algorithm: **K-Nearest Neighbors**
- Input Features:
  - `bed_time`
  - `quali_ty`
  - `prebed_tech`
  - `Wake_up`
- Output: Predicted mood class (0 to 3 mapped to moods)

---


