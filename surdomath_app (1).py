# -*- coding: utf-8 -*-
"""
SurdoMath-Uz / QR-Math: Eshitishida nuqsoni bo'lgan o'quvchilar uchun matematika ta'lim platformasi (1-sinf)
Netlify va Maxsus darslik integratsiyasi
Muallif: PhD tadqiqotchi
"""

import streamlit as st
import pandas as pd

# Sahifa sozlamalari
st.set_page_config(
    page_title="SurdoMath-Uz / QR-Math | 1-sinf Matematika",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar
st.sidebar.title("QR-Math / SurdoMath-Uz")
st.sidebar.markdown("**1-sinf Interaktiv Surdopedagogik Platforma**")

presenter_mode = st.sidebar.checkbox("🖥️ O'qituvchi rejimi (Doska/Proyektor uchun yirik shrift)", value=True)

main_section = st.sidebar.radio(
    "Bo'limni tanlang:",
    [
        "🏫 1-BO'LIM: Maxsus maktab (QR-Math 4 bo'limli metodika)",
        "🔤 2-BO'LIM: O'zbek Daktil Alifbosi va Raqamlar Lug'ati",
        "🎒 3-BO'LIM: Ommaviy va Inklyuziv maktab (I.Repyova darsligi)",
        "📊 4-BO'LIM: O'qituvchi va Diagnostika Paneli"
    ]
)

# Custom CSS
font_scale = "1.2em" if presenter_mode else "1.0em"
card_font = "26px" if presenter_mode else "20px"

st.markdown(f"""
<style>
    body {{
        font-size: {font_scale};
    }}
    .main-title {{
        font-size: 32px !important;
        color: #1E3A8A;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }}
    .sub-title {{
        font-size: 18px !important;
        color: #4B5563;
        text-align: center;
        margin-bottom: 20px;
    }}
    .qr-card {{
        background-color: #F0FDF4;
        border: 2px solid #16A34A;
        padding: 15px;
        border-radius: 12px;
        margin-bottom: 15px;
    }}
    .math-board {{
        background-color: #064E3B;
        color: #FFFFFF;
        font-size: {card_font};
        font-family: 'Courier New', Courier, monospace;
        padding: 20px;
        border-radius: 12px;
        border: 3px solid #10B981;
        text-align: center;
        margin-bottom: 15px;
    }}
    .daktil-badge {{
        background-color: #FEF3C7;
        border: 2px solid #F59E0B;
        padding: 10px;
        border-radius: 8px;
        font-size: 22px;
        font-weight: bold;
        color: #B45309;
        text-align: center;
    }}
</style>
""", unsafe_allow_html=True)

if presenter_mode:
    st.info("🖥️ **O'qituvchi rejimi faol:** Sinf doskasi va proyektor uchun matnlar hamda kartochkalar kattalashtirilgan.")

# =========================================================
# 1-BO'LIM: MAXSUS MAKTAB (QR-MATH METODIKASI)
# =========================================================
if "1-BO'LIM" in main_section:
    st.markdown("""<div class="main-title">🏫 QR-MATH · 0 DAN 9 GACHA BO'LGAN SONLAR</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="sub-title">1-sinf Maxsus darslik va Netlify interaktiv moduli bo'yicha 4 ta metodik bo'lim</div>""", unsafe_allow_html=True)
    
    sub_tabs = st.tabs([
        "1️⃣ 1-bo'lim · Sonlar jadvali",
        "2️⃣ 2-bo'lim · Eshitish va talaffuz",
        "3️⃣ 3-bo'lim · Misollar (Darslikdan)",
        "4️⃣ 4-bo'lim · Mustahkamlash"
    ])
    
    # 1-BO'LIM: SONLAR JADVALI
    with sub_tabs[0]:
        st.subheader("1-bo'lim: Sonlar jadvali (Raqam · Imo-ishora · Yozma · Predmet · Daktil)")
        st.write("Sanoq tartibida raqamlarni tanlang:")
        
        num_selected = st.slider("Sonni tanlang (0 dan 9 gacha):", 0, 9, 3)
        
        daktil_dict = {
            0: {"yozma": "Nol", "daktil": "✊ (Bo'sh qo'l)", "predmet": "⚪ (Bo'sh)", "imo": "Nol ko'rsatgichi"},
            1: {"yozma": "Bir", "daktil": "☝️ B-I-R", "predmet": "🍎 (1 ta olma)", "imo": "1 barmoq ochiq"},
            2: {"yozma": "Ikki", "daktil": "✌️ I-K-K-I", "predmet": "🍎🍎 (2 ta olma)", "imo": "2 barmoq ochiq"},
            3: {"yozma": "Uch", "daktil": "🤟 U-C-H", "predmet": "🍎🍎🍎 (3 ta olma)", "imo": "3 barmoq ochiq"},
            4: {"yozma": "To'rt", "daktil": "🖐️ T-O-'-R-T", "predmet": "🍎🍎🍎🍎 (4 ta olma)", "imo": "4 barmoq ochiq"},
            5: {"yozma": "Besh", "daktil": "🖐️ B-E-S-H", "predmet": "🖐️ (5 ta barmoq)", "imo": "5 barmoq ochiq"},
            6: {"yozma": "O'lti", "daktil": "🖐️☝️ O-'-L-T-I", "predmet": "🍎*6", "imo": "Bosh barmoq bilan 6"},
            7: {"yozma": "Yetti", "daktil": "🖐️✌️ Y-E-T-T-I", "predmet": "🍎*7", "imo": "7 imo-ishorasi"},
            8: {"yozma": "Sakkiz", "daktil": "🖐️🤟 S-A-K-K-I-Z", "predmet": "🍎*8", "imo": "8 imo-ishorasi"},
            9: {"yozma": "To'qqiz", "daktil": "🖐️🖐️ T-O-'-Q-Q-I-Z", "predmet": "🍎*9", "imo": "9 imo-ishorasi"}
        }
        
        data_n = daktil_dict[num_selected]
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown(f"""<div class="math-board"><h1>Raqam: {num_selected}</h1></div>""", unsafe_allow_html=True)
            st.write(f"**Yozilishi:** {data_n['yozma']}")
        with col2:
            st.markdown(f"""<div class="daktil-badge">🤟 Daktil: {data_n["daktil"]}</div>""", unsafe_allow_html=True)
            st.write(f"**Imo-ishora:** {data_n['imo']}")
        with col3:
            st.markdown("""<div class="qr-card">""", unsafe_allow_html=True)
            st.write("**Predmetli (Visual) sanoq:**")
            st.markdown(f"### {data_n['predmet']}")
            st.markdown("""</div>""", unsafe_allow_html=True)

    # 2-BO'LIM: ESHITISH VA TALAFFUZ
    with sub_tabs[1]:
        st.subheader("2-bo'lim: Eshitish va talaffuz malakalari (Eshit va top · Talaffuz qil)")
        st.info("🔊 **Korreksion mashq:** Ovozli tovushni eshiting, labdan o'qing va mos daktil raqamni tanlang.")
        
        target_num = 5
        st.markdown(f"""<div class="daktil-badge">🔊 Audio: "{target_num}" (BESH) tovushi va lab harakati</div>""", unsafe_allow_html=True)
        
        user_choice = st.radio("Eshitgan va labdan o'qigan soningizni tanlang:", [1, 3, 5, 8], horizontal=True)
        if st.button("Tekshirish "):
            if user_choice == target_num:
                st.balloons()
                st.success("🎉 JUDA TO'G'RI! Siz 'BESH' sonini va B-E-S-H daktilini to'g'ri topdingiz!")
            else:
                st.error("❌ Xato! Qayta eshitib ko'ring.")

    # 3-BO'LIM: MISOLLAR DARSLIKDAN
    with sub_tabs[2]:
        st.subheader("3-bo'lim: Misollar darslikdan (Imo-ishora, Daktil, Animatsiya)")
        st.write("Maxsus darslik (5-bet) bo'yicha interaktiv doska misollari:")
        
        st.markdown("""<div class="math-board">""", unsafe_allow_html=True)
        st.markdown("# 3 + 4 + 0 = ?")
        st.markdown("""</div>""", unsafe_allow_html=True)
        
        ex_ans = st.selectbox("Javobingizni tanlang:", [5, 6, 7, 8])
        if st.button("Doskada javobni ko'rish"):
            if ex_ans == 7:
                st.success("✅ To'g'ri! Yechim: 3 + 4 = 7, va 7 + 0 = 7 (Daktil: 7)")
            else:
                st.error("❌ Qayta sanang!")

    # 4-BO'LIM: MUSTAHKAMLASH
    with sub_tabs[3]:
        st.subheader("4-bo'lim: Mustahkamlash (Sonlar zanjiri · Oldingi va keyingi son)")
        st.write("Mantiqiy ketma-ketlikni to'ldiring:")
        
        st.markdown("### Sonlar zanjiri:  `2` ➔ `3` ➔ `?` ➔ `5` ➔ `6`")
        missing_num = st.number_input("Tushirib qoldirilgan sonni kiriting:", 0, 9, 0)
        if st.button("Zanjirni tekshirish"):
            if missing_num == 4:
                st.success("🎉 BARAKALLA! Tushirib qoldirilgan son: 4 (TO'RT)")
            else:
                st.error("❌ Xato! 3 dan keyin va 5 dan oldin qaysi son keladi?")


# =========================================================
# 2-BO'LIM: O'ZBEK DAKTIL ALIFBOSI VA RAQAMLAR LUG'ATI
# =========================================================
elif "2-BO'LIM" in main_section:
    st.markdown("""<div class="main-title">🔤 O'ZBEK DAKTIL ALIFBOSI VA RAQAMLAR LUG'ATI</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="sub-title">Maxsus ta'lim uchun to'liq 28+ daktil harfi va daktil raqamlar katalogi</div>""", unsafe_allow_html=True)
    
    alphabet = [
        "A", "B", "C", "CH", "D", "E", "F", "G", "G'", "H", "I", "J",
        "K", "L", "M", "N", "NG", "O", "O'", "P", "Q", "R", "S", "T", "U", "V", "Y", "Z"
    ]
    
    tab_alf1, tab_alf2 = st.tabs(["🔤 Daktil Alifbosi Harflari", "🔢 Daktil Raqamlar (0-10)"])
    
    with tab_alf1:
        st.subheader("O'zbek Daktil Alifbosi Harflari")
        selected_letter = st.selectbox("Harfni tanlang:", alphabet)
        
        col_l1, col_l2 = st.columns(2)
        with col_l1:
            st.markdown(f"""<div class="math-board"><h1>Harf: {selected_letter}</h1></div>""", unsafe_allow_html=True)
            st.write(f"**Daktil belgisi:** O'zbek daktil alifbosidagi **'{selected_letter}'** harfi va uning bilingval ko'rsatkichi.")
        with col_l2:
            st.markdown(f"""<div class="daktil-badge">🤟 Daktil shakli: {selected_letter}</div>""", unsafe_allow_html=True)
            st.info(f"💡 **Surdopedagogik tavsiya:** O'quvchiga '{selected_letter}' harfini daktil bilan ko'rsatib, labdan o'qishini mashq qildiring.")

    with tab_alf2:
        st.subheader("Daktil Raqamlar (0 dan 10 gacha)")
        nums = list(range(0, 11))
        sel_num = st.select_slider("Raqamni tanlang:", options=nums, value=5)
        
        st.markdown(f"""<div class="daktil-badge"><h2>Raqam: {sel_num}</h2><p>Daktil sanoq ko'rinishi: {"🖐️ " * (sel_num // 5)} {"☝️ " * (sel_num % 5)}</p></div>""", unsafe_allow_html=True)


# =========================================================
# 3-BO'LIM: OMMAVIY VA INKLYUZIV MAKTAB
# =========================================================
elif "3-BO'LIM" in main_section:
    st.markdown("""<div class="main-title">🎒 OMMAVIY VA INKLYUZIV MAKTAB MODULI</div>""", unsafe_allow_html=True)
    st.markdown("""<div class="sub-title">I.Repyova (2023) 1-sinf darsligi va hayotiy shakllar</div>""", unsafe_allow_html=True)
    
    st.write("### 🔴 🟩 🔺 Hayotiy Ob'yektlar va Geometrik Shakllar:")
    c1, c2, c3 = st.columns(3)
    c1.success("🔴 **Doira:** Koptok, Quyosh, Apelsin")
    c2.success("🟩 **Kvadrat:** Oyna, Darcha, Shokolad tili")
    c3.success("🔺 **Uchburchak:** Somsa, Yo'l belgisi, Piramida")


# =========================================================
# 4-BO'LIM: O'QITUVCHI VA DIAGNOSTIKA PANELI
# =========================================================
else:
    st.markdown("""<div class="main-title">📊 O'QITUVCHI VA DIAGNOSTIKA PANELI</div>""", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Sinfdagi o'quvchilar", "12 nafar", "Maxsus sinf")
    col2.metric("O'rtacha o'zlashtirish", "90%", "+16%")
    col3.metric("Foveal diqqat barqarorligi", "4.6 / 5.0", "A'lo")
    
    st.markdown("---")
    chart_data = pd.DataFrame({
        'Kompentensiya': ['Visual Sanoq', 'Daktil Atamalar', 'Amaliy Kattaliklar', 'Siniq Chiziqlar', 'Matnli Masalalar'],
        'O\'zlashtirish (%)': [95, 92, 88, 82, 78]
    })
    st.bar_chart(chart_data.set_index('Kompentensiya'))
