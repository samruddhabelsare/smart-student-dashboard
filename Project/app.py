import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from datetime import date

# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
#   🪔  INDIA STUDENT COMMAND CENTRE  🪔
# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈

st.markdown("# 🪔 INDIA STUDENT COMMAND CENTRE")
st.markdown("##### *Where Curiosity Meets Dedication — Powered by Ambition*")

st.markdown(
    """
```
   ✦ ─────────────────────────────────────────────────── ✦
   ◆   📊 Profile   ·   📂 CSV Analyser   ·   📈 Charts  ◆
   ✦ ─────────────────────────────────────────────────── ✦
         🧡  Work Hard   ·   🤍  Stay Focused   ·   💚  Shine
```
"""
)

# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
#   SIDEBAR
# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈

st.sidebar.title("🛕 CONTROL PANEL")

st.sidebar.markdown(
    """
```
  ╭───────────────────────╮
  │  🟠 STATUS  : ONLINE  │
  │  📚 MODE    : STUDY   │
  │  🏆 RANK    : TOPPER  │
  │  🇮🇳 NATION : BHARAT  │
  ╰───────────────────────╯
```
"""
)

st.sidebar.image(
    "https://images.unsplash.com/photo-1532375810709-75b1da00537c?w=400",
    caption="🌅 The Journey of a Thousand Marks Begins Here",
    use_container_width=True,
)

st.sidebar.markdown("---")
st.sidebar.markdown("### 🎬 Today's Motivation")
st.sidebar.video("https://www.youtube.com/watch?v=WuyKxdLcw3w")
st.sidebar.markdown("---")

st.sidebar.markdown(
    """
```
  ⚡ DASHBOARD STATS
  ──────────────────────
  ✅  Sections    :  4
  🎨  Charts      :  3
  📂  CSV Upload  :  YES
  🌐  Language    :  EN
  🇮🇳  Style      :  INDIA
  ──────────────────────
```
"""
)
st.sidebar.markdown("*\"Karm karo, result aayega.\" — Do the work.* 🙏")


# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
#   SECTION 01 — STUDENT PROFILE
# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈

st.markdown("---")

st.markdown(
    """
```
  ✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦
       👤   S E C T I O N   0 1   —   P R O F I L E
  ✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦
```
"""
)

st.markdown("## 🪷 Student Identity Card Builder")
st.markdown("> *Every IAS officer, every IITian, every doctor — started exactly where you are now.*")
st.markdown("---")

# ── Personal Details ──────────────────────────────────────────
st.subheader("🏵️  Personal Details")
st.markdown("*Fill in your details below and claim your identity.*")
st.markdown(" ")

name = st.text_input(
    "✏️  Full Name",
    placeholder="e.g.  Aarav Sharma  /  Priya Patel  /  Rohit Verma"
)
st.markdown(" ")

age = st.number_input("🎂  Age", min_value=5, max_value=100, value=17, step=1)
st.markdown(" ")

dob = st.date_input("📅  Date of Birth", value=date(2007, 8, 15))
st.markdown(" ")

city = st.text_input(
    "🏙️  City / Town",
    placeholder="e.g.  Mumbai · Delhi · Jaipur · Chennai · Bengaluru · Patna"
)
st.markdown(" ")

about = st.text_area(
    "💬  My Story  —  Dreams, Goals & Passions",
    placeholder="I want to become... My dream college is... I am passionate about... My biggest strength is...",
    height=115,
)
st.markdown(" ")

# ── Academic Details ──────────────────────────────────────────
st.markdown("---")
st.subheader("🎯  Academic Profile")
st.markdown(" ")

board = st.selectbox(
    "🏫  Education Board",
    [
        "── Select Your Board ──",
        "📘  CBSE",
        "📗  ICSE / ISC",
        "📙  Maharashtra State Board (SSC / HSC)",
        "📙  Uttar Pradesh Board (UPMSP)",
        "📙  Tamil Nadu State Board (TNBSE)",
        "📙  Rajasthan Board (RBSE)",
        "📙  Karnataka Board (KSEEB)",
        "📙  West Bengal Board (WBBSE)",
        "📙  Andhra Pradesh Board (BSEAP)",
        "📕  IB (International Baccalaureate)",
        "🎓  Undergraduate / College",
    ],
)
st.markdown(" ")

stream = st.selectbox(
    "🔬  Stream / Specialisation",
    [
        "── Select Your Stream ──",
        "⚛️  PCM  —  Physics · Chemistry · Maths",
        "🧬  PCB  —  Physics · Chemistry · Biology",
        "💹  Commerce with Mathematics",
        "📊  Commerce without Mathematics",
        "📝  Humanities / Arts",
        "💻  Computer Science Engineering (B.Tech / B.E.)",
        "🏥  MBBS / BDS (Medical)",
        "⚖️  BA LLB / BBA LLB (Law)",
        "🏦  B.Com / MBA / BBA",
        "🎨  B.Des / Fine Arts / Architecture",
        "🛰️  Defence — NDA / CDS Prep",
    ],
)
st.markdown(" ")

target_exams = st.multiselect(
    "🎯  Target Competitive Exams  (select all you are preparing for)",
    [
        "📐 JEE Mains",
        "📐 JEE Advanced",
        "🩺 NEET UG",
        "📋 UPSC Civil Services (IAS/IPS/IFS)",
        "💼 CAT / XAT (MBA)",
        "🏦 IBPS / SBI Bank PO",
        "💻 GATE",
        "⚖️ CLAT (Law Entrance)",
        "🎓 CUET (Central Universities)",
        "🚂 SSC / Railway NTPC",
        "🛡️ NDA / CDS (Defence)",
        "📡 ISRO / DRDO (Research)",
    ],
    default=["📐 JEE Mains"],
)
st.markdown(" ")

study_slot = st.radio(
    "🕐  Your Peak Study Time",
    [
        "🌄  Brahmamuhurta Warrior  (4 AM – 8 AM)",
        "☀️  Morning Champion       (8 AM – 1 PM)",
        "🌤️  Afternoon Grinder      (1 PM – 6 PM)",
        "🌆  Evening Thinker        (6 PM – 10 PM)",
        "🌙  Night Owl Scholar      (10 PM – 2 AM)",
    ],
)
st.markdown(" ")

daily_hours = st.slider(
    "⏱️  Daily Study Hours",
    min_value=0, max_value=16, value=7, step=1
)
st.markdown(" ")

percentage = st.number_input(
    "📊  Last Exam Percentage / Marks  (%)",
    min_value=0.0, max_value=100.0, value=78.5, step=0.5
)
st.markdown(" ")

st.markdown(
    """
```
  ╔══════════════════════════════════════════════════════╗
  ║   All set?  Hit the button below to generate your   ║
  ║        🪔  OFFICIAL STUDENT IDENTITY CARD  🪔        ║
  ╚══════════════════════════════════════════════════════╝
```
"""
)

if st.button("🚀  GENERATE MY IDENTITY CARD"):
    if name.strip() == "":
        st.write("⚠️  Please enter your **Full Name** to proceed!")
    else:
        exams_str = "  ·  ".join(target_exams) if target_exams else "Not decided yet"
        # CBSE-style grade
        if   percentage >= 91: grade = "A1 🏆"
        elif percentage >= 81: grade = "A2 ⭐"
        elif percentage >= 71: grade = "B1 ✅"
        elif percentage >= 61: grade = "B2 👍"
        elif percentage >= 51: grade = "C1 📚"
        elif percentage >= 41: grade = "C2 ⚠️"
        else:                  grade = "Need to work harder 💪"

        if   percentage >= 60: division = "First Division 🥇"
        elif percentage >= 45: division = "Second Division 🥈"
        elif percentage >= 33: division = "Third Division 🥉"
        else:                  division = "Compartment — Keep Going! 🔄"

        st.success(
            f"""
🪔  IDENTITY CARD GENERATED!

  ╔══════════════════════════════════════════════════════╗
  ║              🇮🇳  STUDENT IDENTITY CARD             ║
  ╠══════════════════════════════════════════════════════╣
  ║  👤  Name         :  {name}
  ║  🎂  Age          :  {int(age)} years
  ║  📅  Date of Birth:  {dob.strftime("%d %B %Y")}
  ║  🏙️  City         :  {city if city.strip() else "India 🇮🇳"}
  ║  🏫  Board        :  {board}
  ║  🔬  Stream       :  {stream}
  ║  📊  Last Score   :  {percentage}%  →  Grade {grade}
  ║  🏅  Division     :  {division}
  ║  ⏱️  Study Hours  :  {daily_hours} hrs/day  ·  {study_slot}
  ║  🎯  Target Exams :  {exams_str}
  ╚══════════════════════════════════════════════════════╝

  🌟 Welcome, {name.split()[0]}!  Your card is ready.
  India is proud of every student who dares to dream big!
  Keep going — the result will honour your hard work. 🙏🇮🇳
            """
        )

# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
#   SECTION 02 — CSV ANALYSER
# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈

st.markdown("---")

st.markdown(
    """
```
  ✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦
      📂   S E C T I O N   0 2   —   C S V   T O O L
  ✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦
```
"""
)

st.markdown("## 📂 Data Analyser — Upload & Explore")
st.markdown("> *Numbers don't lie. Let your marks tell the real story.*")
st.markdown("---")

st.subheader("📤  Upload Your CSV File")
st.markdown(
    """
```
  ╭──────────────────────────────────────────────────╮
  │  ✅  Accepted Format    :  .csv                  │
  │  💡  Try This           :  example_students.csv  │
  │  🔒  Privacy            :  Local processing only │
  │  📌  Works With         :  Any marks / data CSV  │
  ╰──────────────────────────────────────────────────╯
```
"""
)

uploaded_file = st.file_uploader("📁  Choose your CSV file", type=["csv"])
st.markdown(" ")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    rows, cols = df.shape

    st.subheader("🗂️  File Summary")
    st.markdown(
        f"""
```
  ╔═══════════════════════════════════════════════════╗
  ║   ✅  FILE LOADED SUCCESSFULLY!                  ║
  ╠═══════════════════════════════════════════════════╣
  ║   📄  File      :  {uploaded_file.name:<30}║
  ║   📏  Rows      :  {rows:<30,}║
  ║   📐  Columns   :  {cols:<30}║
  ║   🧩  Total Cells:  {rows * cols:<29,}║
  ╚═══════════════════════════════════════════════════╝
```
"""
    )

    st.subheader("📋  Interactive Data Table")
    st.markdown("*Scroll · Sort · Explore — your entire dataset below:*")
    st.dataframe(df)

    st.markdown("---")
    st.subheader("📊  Statistical Summary")
    st.markdown("*Auto-generated stats for all numeric columns:*")
    st.dataframe(df.describe())

else:
    st.markdown(
        """
```
  ╔════════════════════════════════════════════════════╗
  ║   📭  NO FILE UPLOADED YET                        ║
  ║                                                    ║
  ║   Once you upload a .csv file, you will see:      ║
  ║     ◆  Full interactive data table                ║
  ║     ◆  Auto statistics for numeric columns        ║
  ║     ◆  Row, column & cell counts                  ║
  ║                                                    ║
  ║   💡  Download example_students.csv first!        ║
  ╚════════════════════════════════════════════════════╝
```
"""
    )

# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
#   SECTION 03 — VISUALISATION LAB
# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈

st.markdown("---")

st.markdown(
    """
```
  ✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦
     📈   S E C T I O N   0 3   —   V I S U A L S
  ✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦
```
"""
)

st.markdown("## 🎨 Marks Visualisation Lab")
st.markdown("> *See your academic performance painted in the colours of India.*")
st.markdown("---")

# ── Seed & data ───────────────────────────────────────────────
np.random.seed(21)
months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep",
          "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]

subject_data = pd.DataFrame(
    {
        "Mathematics 📐": np.random.randint(55, 100, 12),
        "Science 🔬":      np.random.randint(52, 99,  12),
        "English 📝":      np.random.randint(58, 98,  12),
        "History 📜":      np.random.randint(60, 97,  12),
        "Computer 💻":     np.random.randint(65, 100, 12),
    },
    index=months,
)

# ── Line Chart ────────────────────────────────────────────────
st.subheader("📉  Subject Score Trends — Academic Year  (Line Chart)")
st.markdown(
    """
```
  READING GUIDE
  ──────────────────────────────────────────────────────────
  Each line = one subject tracked across Apr → Mar (1 year).
  Rising line = Improvement 📈  |  Falling = Time to grind!
  ──────────────────────────────────────────────────────────
```
"""
)
st.line_chart(subject_data)
st.markdown("---")

# ── Bar Chart ─────────────────────────────────────────────────
st.subheader("📊  Monthly Subject Comparison — (Bar Chart)")
st.markdown(
    """
```
  READING GUIDE
  ──────────────────────────────────────────────────────────
  Each cluster of bars = one month of the academic year.
  Tallest bar per month = your strongest subject that month.
  ──────────────────────────────────────────────────────────
```
"""
)
st.bar_chart(subject_data)
st.markdown("---")

# ── Matplotlib — Marigold / Rangoli Palette ───────────────────
st.subheader("🪔  Percentage Trajectory — Marigold Edition  (Matplotlib)")
st.markdown(
    """
```
  ╭────────────────────────────────────────────────────────╮
  │  🌼  Chart inspired by the marigold festival lamps     │
  │  🟠  Saffron line   =  Your percentage journey         │
  │  💚  Green band     =  Distinction zone  ( ≥ 75% )     │
  │  🤍  White band     =  First Division    ( ≥ 60% )     │
  │  🔴  Red band       =  Needs attention   ( < 45% )     │
  │  🔵  Ashoka dots    =  Each test score annotated       │
  ╰────────────────────────────────────────────────────────╯
```
"""
)

np.random.seed(14)
test_labels = [f"Test {i}" for i in range(1, 10)]
pct = np.clip(np.cumsum(np.random.uniform(-1.2, 3.8, 9)) + 56, 32, 100)

# Marigold / Rangoli palette
SAFFRON  = "#FF6B00"
GOLD     = "#FFB300"
INDIA_GN = "#138808"
LOTUS    = "#E8336D"
ASHOKA   = "#0047AB"
CREAM    = "#FFF8E7"
DARK_BG  = "#1A0A00"
MID_BG   = "#2A1200"

fig, ax = plt.subplots(figsize=(11, 5.5))
fig.patch.set_facecolor(DARK_BG)
ax.set_facecolor(MID_BG)

# Performance bands
ax.axhspan(75, 105, alpha=0.10, color=INDIA_GN)
ax.axhspan(60, 75,  alpha=0.07, color="#FFFFFF")
ax.axhspan(45, 60,  alpha=0.07, color=GOLD)
ax.axhspan(0,  45,  alpha=0.10, color=LOTUS)

# Band labels
ax.text(8.6, 77,  "Distinction ✦", color=INDIA_GN, fontsize=7.5, alpha=0.85, fontweight="bold")
ax.text(8.6, 62,  "First Div ✦",   color="#cccccc",fontsize=7.5, alpha=0.75, fontweight="bold")
ax.text(8.6, 47,  "Second Div ✦",  color=GOLD,    fontsize=7.5, alpha=0.75, fontweight="bold")
ax.text(8.6, 34,  "Below ✦",       color=LOTUS,   fontsize=7.5, alpha=0.75, fontweight="bold")

# Reference lines
ax.axhline(75, color=INDIA_GN, linestyle="--", linewidth=1.2, alpha=0.55)
ax.axhline(60, color="#cccccc", linestyle="--", linewidth=1.0, alpha=0.45)
ax.axhline(45, color=GOLD,     linestyle="--", linewidth=1.0, alpha=0.45)

# Glow fill
ax.fill_between(range(len(test_labels)), pct, 30, alpha=0.18, color=SAFFRON)

# Main trajectory line
ax.plot(range(len(test_labels)), pct,
        color=SAFFRON, linewidth=3.5, zorder=6,
        marker="D", markersize=9,
        markerfacecolor=GOLD, markeredgecolor=SAFFRON, markeredgewidth=2)

# Ashoka-blue annotation dots (inner ring effect)
ax.plot(range(len(test_labels)), pct,
        color=ASHOKA, linewidth=0, zorder=7,
        marker="o", markersize=4, markerfacecolor=ASHOKA)

# Score annotations
for i, p in enumerate(pct):
    ax.annotate(
        f"{p:.1f}%",
        (i, p),
        textcoords="offset points",
        xytext=(0, 15),
        ha="center",
        fontsize=8.5,
        color=CREAM,
        fontweight="bold",
    )

# Styling
ax.set_title(
    "🪔  Student Percentage Trajectory  ·  Marigold Edition  🌼",
    color=GOLD, fontsize=13.5, fontweight="bold", pad=20
)
ax.set_xlabel("Tests / Exams", color="#bbbbbb", fontsize=11)
ax.set_ylabel("Percentage  (%)", color="#bbbbbb", fontsize=11)
ax.set_xticks(range(len(test_labels)))
ax.set_xticklabels(test_labels, color="#cccccc", fontsize=9.5)
ax.set_yticks([30, 45, 60, 75, 90, 100])
ax.set_yticklabels(["30%", "45%", "60%", "75%", "90%", "100%"], color="#cccccc")
ax.set_ylim(28, 112)
ax.set_xlim(-0.3, 9.2)

for spine in ax.spines.values():
    spine.set_edgecolor("#5A2D00")

p1 = mpatches.Patch(color=INDIA_GN, alpha=0.7, label="Distinction ≥ 75%")
p2 = mpatches.Patch(color="#FFFFFF", alpha=0.5, label="First Division ≥ 60%")
p3 = mpatches.Patch(color=GOLD,     alpha=0.7, label="Second Division ≥ 45%")
p4 = mpatches.Patch(color=LOTUS,    alpha=0.7, label="Needs Attention < 45%")
ax.legend(
    handles=[p1, p2, p3, p4],
    facecolor="#2A1200", labelcolor="white",
    fontsize=8.5, loc="upper left",
    framealpha=0.85
)
ax.grid(axis="y", linestyle="--", alpha=0.10, color="#ffffff")
plt.tight_layout()
st.pyplot(fig)

# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
#   SECTION 04 — CODE SHOWCASE
# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈

st.markdown("---")

st.markdown(
    """
```
  ✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦
      💻   S E C T I O N   0 4   —   C O D E
  ✦━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━✦
```
"""
)

st.markdown("## 🐍 Code Showcase — CBSE Result Engine")
st.markdown("> *Real Python. Real Logic. The foundation of every coder starts here.*")
st.markdown("---")

st.subheader("🔍  CBSE Style Marksheet Generator")
st.markdown(
    """
```
  ╭──────────────────────────────────────────────────────╮
  │  What this code does:                               │
  │    ◆  Takes student names & subject marks (dict)    │
  │    ◆  Calculates total, percentage, grade           │
  │    ◆  Assigns CBSE grade (A1 to E) + Division       │
  │    ◆  Prints a formatted CBSE-style result card     │
  ╰──────────────────────────────────────────────────────╯
```
"""
)

code_snippet = '''
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#   🇮🇳  CBSE RESULT ENGINE  —  Python Edition
#   Grade System : A1 / A2 / B1 / B2 / C1 / C2 / D / E
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def get_grade(pct: float) -> tuple:
    """Return CBSE grade and status based on percentage."""
    if   pct >= 91: return "A1", "🏆 Outstanding"
    elif pct >= 81: return "A2", "⭐ Excellent"
    elif pct >= 71: return "B1", "✅ Very Good"
    elif pct >= 61: return "B2", "👍 Good"
    elif pct >= 51: return "C1", "📚 Average"
    elif pct >= 41: return "C2", "⚠️  Below Average"
    elif pct >= 33: return "D",  "🔄 Pass — Work Harder"
    else:           return "E",  "❌ Fail — Don't Give Up"


def get_division(pct: float) -> str:
    if   pct >= 60: return "First Division  🥇"
    elif pct >= 45: return "Second Division 🥈"
    elif pct >= 33: return "Third Division  🥉"
    else:           return "Fail — Compartment 🔄"


def generate_marksheet(name: str, marks: dict) -> dict:
    scores    = list(marks.values())
    total     = sum(scores)
    max_marks = len(scores) * 100
    pct       = round((total / max_marks) * 100, 2)
    grade, status = get_grade(pct)

    return {
        "name":     name,
        "marks":    marks,
        "total":    total,
        "max":      max_marks,
        "pct":      pct,
        "grade":    grade,
        "status":   status,
        "division": get_division(pct),
        "topper":   max(marks, key=marks.get),
        "weakest":  min(marks, key=marks.get),
    }


def print_marksheet(r: dict):
    print(f"\\n{'◈' * 50}")
    print(f"    🇮🇳  CBSE MARKSHEET  ·  {r['name']}")
    print(f"{'◈' * 50}")
    for subject, mark in r["marks"].items():
        bar = "█" * (mark // 10) + "░" * (10 - mark // 10)
        print(f"  {subject:<22} :  {mark:>3}/100  {bar}")
    print(f"  {'─' * 44}")
    print(f"  Total      :  {r['total']} / {r['max']}")
    print(f"  Percentage :  {r['pct']}%")
    print(f"  Grade      :  {r['grade']}  →  {r['status']}")
    print(f"  Division   :  {r['division']}")
    print(f"  Best Sub   :  {r['topper']}  🌟")
    print(f"  Focus Sub  :  {r['weakest']}  📖")
    print(f"{'◈' * 50}")


# ── Class 10 — Section A ───────────────────────────
students = {
    "Aarav Sharma": {
        "Mathematics": 95, "Science": 91,
        "English": 88, "Hindi": 93, "Social Sci.": 90
    },
    "Priya Patel": {
        "Mathematics": 72, "Science": 68,
        "English": 75, "Hindi": 80, "Social Sci.": 71
    },
    "Rohit Verma": {
        "Mathematics": 45, "Science": 50,
        "English": 42, "Hindi": 55, "Social Sci.": 38
    },
    "Ananya Krishnan": {
        "Mathematics": 98, "Science": 97,
        "English": 92, "Hindi": 85, "Social Sci.": 94
    },
}

for student_name, subject_marks in students.items():
    result = generate_marksheet(student_name, subject_marks)
    print_marksheet(result)
'''

st.code(code_snippet, language="python")

# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
#   FOOTER
# ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈

st.markdown("---")
st.markdown(
    """
```
  ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
     🪔  INDIA STUDENT COMMAND CENTRE  ·  Powered by Ambition
     Built with  Streamlit  ·  Pandas  ·  NumPy  ·  Matplotlib
     ──────────────────────────────────────────────────────────
     "Coding is Rice plate eating , i dont like Rice as much 
      as Coding"
                                           — Samruddha Belsare 
     ──────────────────────────────────────────────────────────
     " Developed by Samruddha Belsare with LLM's "
                                           Date:17-02-2026 
     ──────────────────────────────────────────────────────────
              🧡 Work Hard   🤍 Stay Focused   💚 Shine Bright
  ◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈◈
```
"""
)
st.markdown("*© 2026 · India Student Command Centre · Built for every Indian student who needs simple Streamit Project for Assignment🪔*")