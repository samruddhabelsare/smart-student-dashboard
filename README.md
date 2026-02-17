# 🪔 India Student Command Centre

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Matplotlib](https://img.shields.io/badge/Matplotlib-3.7%2B-11557c?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)

**_Where Curiosity Meets Dedication — Powered by Ambition_**

🧡 Work Hard &nbsp;·&nbsp; 🤍 Stay Focused &nbsp;·&nbsp; 💚 Shine Bright

## 🚀 Live Demo

[![Open Streamlit App](https://img.shields.io/badge/Streamlit-Live_App-brightgreen?style=for-the-badge&logo=streamlit)](https://smart-student-dashboard.streamlit.app/)


[Features](#-features) · [Demo](#-demo) · [Installation](#-installation) · [Usage](#-usage) · [Project Structure](#-project-structure) · [Tech Stack](#-tech-stack) · [Author](#-author)

</div>

---

## 📌 Overview

**India Student Command Centre** is a beautifully crafted, India themed interactive dashboard built with **Streamlit**  designed for Indian students to manage their academic identity, analyse CSV datasets, and visualise marks data through stunning charts.

The app combines the spirit of Indian education culture (CBSE boards, JEE/NEET prep, competitive exams) with a clean, professional UI built entirely using core Streamlit elements  no CSS injection, no HTML hacks. The visual identity is inspired by the   saffron, gold, India green, and Ashoka blue.

> *"Coding is Rice plate eating — I don't like Rice as much as Coding."*
> — **Samruddha Belsare**, Developer 🇮🇳

---

## ✨ Features

### 👤 Section 01 — Student Identity Card Builder
- Enter full name, age, date of birth, and city
- Write your personal story — dreams, goals, passions
- Select your **Education Board** from 11 Indian boards (CBSE, ICSE, SSC, RBSE, KSEEB, WBBSE, IB, and more)
- Choose your **Stream** (PCM, PCB, Commerce, Arts, B.Tech, MBBS, LLB, NDA, and more)
- Multi-select **Target Competitive Exams** — JEE, NEET, UPSC, CAT, GATE, CLAT, CUET, NDA, ISRO/DRDO
- Pick your **Peak Study Time** — from Brahmamuhurta Warrior (4AM) to Night Owl Scholar (10PM)
- Slide your **Daily Study Hours** (0–16 hrs)
- Input last exam **Percentage** and get instant **CBSE Grade** (A1 to E) + **Division** auto-calculated
- Click the **Generate Identity Card** button to receive a fully formatted, ASCII-bordered Student Card

### 📂 Section 02 — CSV Data Analyser
- Upload any `.csv` file via drag-and-drop
- Instant **file metadata** display — name, row count, column count, total cells
- Full **interactive data table** with scroll and sort
- Auto-generated **descriptive statistics** for all numeric columns (`df.describe()`)
- Friendly empty-state prompt when no file is uploaded

### 📈 Section 03 — Marks Visualisation Lab
- **Line Chart** — tracks 5 subjects (Mathematics, Science, English, History, Computer) across the full Indian academic year (Apr → Mar)
- **Bar Chart** — side-by-side monthly subject comparison
- **Marigold Edition Matplotlib Chart** — a custom, dark-themed percentage trajectory plot featuring:
  - Saffron `#FF6B00` trajectory line with Gold `#FFB300` diamond markers
  - Ashoka Blue `#0047AB` inner dot overlay (Chakra-inspired)
  - India Green distinction band (≥ 75%), White first-division band (≥ 60%), Gold second-division band (≥ 45%), Lotus pink danger band (< 45%)
  - Annotated percentage values floating above each data point
  - Deep dark saffron background (`#1A0A00`) for a festival-night aesthetic

### 💻 Section 04 — Code Showcase
- Displays a full **CBSE Result Engine** in Python with syntax highlighting
- Covers `get_grade()`, `get_division()`, `generate_marksheet()`, and `print_marksheet()` functions
- ASCII progress bar per subject inside printed output (e.g. `████████░░`)
- Sample output for 4 real-named Indian students

### 🛕 Sidebar — Control Panel
- Live status panel (Online · Study Mode · Topper Rank · Bharat Nation)
- Inspirational campus photograph
- Embedded YouTube motivational video
- Quick dashboard stats panel

---

## 🖥️ Demo

```
╔══════════════════════════════════════════════════════════════════╗
║  🪔 INDIA STUDENT COMMAND CENTRE                                ║
║  ─────────────────────────────────────────────────────────────  ║
║  📊 Profile  ·  📂 CSV Analyser  ·  📈 Charts  ·  💻 Code      ║
╚══════════════════════════════════════════════════════════════════╝
```

> Run the app locally — see [Installation](#-installation) below.

---

## 🗂️ Project Structure

```
india-student-command-centre/
│
├── app.py                      # Main Streamlit application (single file)
├── example_students.csv        # Sample dataset — 35 Indian students
├── README.md                   # This file
└── requirements.txt            # Python dependencies
```

> This is a **single-file Streamlit project** — all logic, UI, and visualisation live in `app.py`.

---

## 🛠️ Tech Stack

| Library | Version | Purpose |
|---|---|---|
| `streamlit` | ≥ 1.32 | Web app framework — UI, layout, widgets |
| `pandas` | ≥ 2.0 | CSV loading, dataframes, `df.describe()` |
| `numpy` | ≥ 1.24 | Random data generation for charts |
| `matplotlib` | ≥ 3.7 | Custom Marigold Edition chart |
| `matplotlib.patches` | (bundled) | Legend patch handles for colour bands |
| `datetime` | (stdlib) | Date-of-birth input and formatting |

---

## 📦 Installation

### Prerequisites

- Python **3.8 or higher**
- `pip` package manager

### Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/india-student-command-centre.git
cd india-student-command-centre
```

### Step 2 — Create a Virtual Environment *(Recommended)*

```bash
# Create virtual environment
python -m venv venv

# Activate — Windows
venv\Scripts\activate

# Activate — macOS / Linux
source venv/bin/activate
```

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:

```bash
pip install streamlit pandas numpy matplotlib
```

### Step 4 — Run the App

```bash
streamlit run app.py
```

The app will open automatically at **`http://localhost:8501`** in your browser.

---

## 📋 requirements.txt

```
streamlit>=1.32.0
pandas>=2.0.0
numpy>=1.24.0
matplotlib>=3.7.0
```

---

## 🚀 Usage

### Running for the First Time

1. Launch the app with `streamlit run app.py`
2. The browser opens at `http://localhost:8501`
3. The **sidebar** loads with the Control Panel, photo, and video
4. Work through the four sections top to bottom

### Using the Student Profile Builder

1. Fill in **Full Name**, **Age**, **Date of Birth**, and **City**
2. Write something in **My Story**
3. Select your **Education Board** and **Stream**
4. Pick your **Target Competitive Exams** (multi-select)
5. Choose your **Peak Study Time** and set **Daily Study Hours**
6. Enter your **Last Exam Percentage**
7. Click **🚀 GENERATE MY IDENTITY CARD**
8. Your formatted card appears with your CBSE grade and division

### Using the CSV Analyser

1. Scroll to **Section 02**
2. Click **Browse files** or drag and drop a `.csv` file
3. The file summary, interactive table, and statistics render instantly
4. Try the included `example_students.csv` for a quick demo

### Reading the Visualisation Charts

| Chart | What It Shows |
|---|---|
| Line Chart | Subject-wise score trends across 12 months (Apr → Mar) |
| Bar Chart | Monthly side-by-side subject comparison |
| Marigold Matplotlib | Percentage trajectory across 9 tests with performance bands |

---

## 📊 Sample Dataset — `example_students.csv`

The included CSV contains **35 Indian students** across Classes 10 and 12 with the following columns:

| Column | Description |
|---|---|
| `Roll No` | Unique student roll number |
| `Student Name` | Full name |
| `Class` | Class 10 or 12 |
| `Section` | A, B, C, or D |
| `City` | Indian city (e.g. Mumbai, Delhi, Kochi) |
| `State` | Indian state |
| `Board` | CBSE / ICSE / State Boards |
| `Mathematics` | Marks out of 100 |
| `Science` | Marks out of 100 |
| `English` | Marks out of 100 |
| `History` | Marks out of 100 |
| `Computer` | Marks out of 100 |
| `Total` | Sum of all subjects |
| `Percentage` | Overall percentage |
| `Grade` | CBSE Grade (A1 – D) |
| `Division` | First / Second / Third Division |
| `Target Exam` | JEE / NEET / UPSC / CAT / GATE etc. |
| `Study Hours Per Day` | Self-reported daily study hours |

---

## 🎨 Design Philosophy

This app's visual identity is built using **zero custom CSS** and **zero HTML injection** — only core Streamlit elements. The "GUI magic" comes entirely from:

| Technique | Effect |
|---|---|
| `╔══╗ ║ ╚══╝` box-drawing characters | Panel borders that feel like real UI cards |
| `✦━━✦` section dividers | Rangoli / geometric decorative borders |
| `◈` repeat symbols | Indian-pattern texture in headers and footers |
| `st.code()` blocks for info panels | Monospace-rendered info boxes that look like tooltips |
| Marigold Matplotlib palette | `#FF6B00` saffron, `#FFB300` gold, `#138808` India green, `#0047AB` Ashoka blue |
| Dark saffron background `#1A0A00` | Festival-night aesthetic on the custom chart |

---

## 🧠 CBSE Grading System Used

| Percentage | Grade | Status |
|---|---|---|
| ≥ 91% | A1 | 🏆 Outstanding |
| 81–90% | A2 | ⭐ Excellent |
| 71–80% | B1 | ✅ Very Good |
| 61–70% | B2 | 👍 Good |
| 51–60% | C1 | 📚 Average |
| 41–50% | C2 | ⚠️ Below Average |
| 33–40% | D | 🔄 Pass — Work Harder |
| < 33% | E | ❌ Fail — Don't Give Up |

| Percentage | Division |
|---|---|
| ≥ 60% | First Division 🥇 |
| 45–59% | Second Division 🥈 |
| 33–44% | Third Division 🥉 |
| < 33% | Compartment / Fail 🔄 |

---

## 🔮 Future Improvements

- [ ] Add student data persistence using `st.session_state`
- [ ] Add subject-wise pie chart for marks distribution
- [ ] Export student identity card as downloadable PDF
- [ ] Add CSV filter — filter by board, state, grade, or exam target
- [ ] Add a Pomodoro-style study timer widget
- [ ] Add support for uploading marksheets in image format (OCR)
- [ ] Dark / Light theme toggle
- [ ] Multilingual support (Hindi, Tamil, Telugu, Marathi)

---

## ⚠️ Known Limitations

- The charts in Section 03 use **randomly generated demo data** — they do not reflect uploaded CSV data
- No data is persisted between sessions (no database or session state)
- The sidebar video requires an active internet connection
- The sidebar image is loaded from Unsplash CDN — requires internet access

---

## 🤝 Contributing

Contributions are welcome! If you are a student who wants to add features or fix bugs:

1. Fork the repository
2. Create a new branch: `git checkout -b feature/your-feature-name`
3. Make your changes in `app.py`
4. Test thoroughly: `streamlit run app.py`
5. Commit: `git commit -m "Add: your feature description"`
6. Push: `git push origin feature/your-feature-name`
7. Open a **Pull Request**

Please keep all additions within the **allowed Streamlit elements** and maintain the Indian aesthetic.

---

## 📄 License

```
MIT License

Copyright (c) 2026 Samruddha Belsare

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

---

## 👨‍💻 Author

<div align="center">

**Samruddha Belsare**

🇮🇳 &nbsp; India &nbsp; · &nbsp; 📅 Built on 17 February 2026

*"Coding is Rice plate eating — I don't like Rice as much as Coding."*

Developed with ❤️ and Large Language Models (LLMs)

---

*Built for every Indian student who needs a clean Streamlit project for their assignment — and ends up building something they are actually proud of.* 🪔

</div>

---

<div align="center">

```
◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
   🪔  INDIA STUDENT COMMAND CENTRE  ·  Powered by Ambition
   Built with  Streamlit  ·  Pandas  ·  NumPy  ·  Matplotlib
   ──────────────────────────────────────────────────────────
            🧡 Work Hard   🤍 Stay Focused   💚 Shine Bright
◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
```

*© 2026 · India Student Command Centre · For every Indian student who dares to dream 🇮🇳*

⭐ If this project helped you, please give it a star on GitHub!

</div>
