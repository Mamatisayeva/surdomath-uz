# -*- coding: utf-8 -*-
"""
SurdoMath-Uz: Eshitishida nuqsoni bo'lgan o'quvchilar uchun matematika ta'lim platformasi (1-sinf)
Muallif: PhD tadqiqotchi
Ixtisoslik: 13.00.03 – Maxsus pedagogika (surdopedagogika)
"""

import streamlit as st

# Sahifa sozlamalari
st.set_page_config(
    page_title="SurdoMath-Uz | 1-sinf Matematika",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Maxsus CSS stillari
st.markdown("""
<style>
    .main-title {
        font-size: 32px !important;
        color: #1E3A8A;
        font-weight: bold;
        text-align: center;
        margin-bottom: 5px;
    }
    .sub-title {
        font-size: 18px !important;
        color: #4B5563;
        text-align: center;
        margin-bottom: 25px;
    }
    .module-card {
        background-color: #F3F4F6;
        border-left: 6px solid #2563EB;
        padding: 15px;
        border-radius: 8px;
        margin-bottom: 15px;
    }
    .daktil-box {
        background-color: #FEF3C7;
        border: 2px dashed #D97706;
        padding: 10px;
        border-radius: 8px;
        font-size: 18px;
        text-align: center;
        font-weight: bold;
    }
    .sim-box {
        background-color: #E0F2FE;
        border: 2px solid #0284C7;
        padding: 20px;
        border-radius: 12px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Yon panel (Sidebar) - Bo'limlarni tanlash
st.sidebar.title("SurdoMath-Uz")
st.sidebar.markdown("**1-sinf Matematika Platformasi**")

main_section = st.sidebar.radio(
    "Ta'lim bo'limini tanlang:",
    [
        "🏫 1-BO'LIM: Maxsus maktab-internatlari uchun (U.Fayziyeva darsligi)",
        "🎒 2-BO'LIM: Ommaviy va Inklyuziv maktab uchun (I.Repyova darsligi)",
        "📊 3-BO'LIM: O'qituvchi va Diagnostika Paneli (Monitoring)"
    ]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Eslatish:** Platforma eshitishida nuqsoni bo'lgan o'quvchilarning visual-spatial (ko'rgazmali-fazoviy) tafakkuri va daktil-imo-ishora nutqiga moslashtirilgan.")


# ==========================================
# 1-BO'LIM: MAXSUS MAKTAB-INTERNATLARI UCHUN
# ==========================================
if "1-BO'LIM" in main_section:
    st.markdown('<div class="main-title">🏫 MAXSUS MAKTAB-INTERNATLARI UCHUN MODUL</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">U.Fayziyeva (2024) 1-sinf "Maxsus Matematika" darsligi asosida yaratilgan korreksion-didaktik interfeys</div>', unsafe_allow_html=True)
    
    sub_tab = st.tabs([
        "📖 Visual-Daktil Lug'at", 
        "🤟 Daktil Sanagich (0-20)", 
        "⚖️ Amaliy Kattaliklar (Kg, Litr, Cm)", 
        "🍎 Visual Arifmetik Masalalar"
    ])
    
    # 1.1 Visual-Daktil Lug'at
    with sub_tab[0]:
        st.subheader("📖 Maxsus Matematik Atamalarning Bilingval Visual-Daktil Lug'ati")
        st.write("Eshitishida nuqsoni bo'lgan o'quvchilar uchun matematik atamalarning matnli, visual va daktil ko'rinishi:")
        
        terms = {
            "Son va Raqam": {
                "emoji": "🔢",
                "daktil": "С-О-Н / Р-А-Қ-А-М",
                "definition": "Narsalarning sanoqdagi tartibi va miqdorini bildiruvchi belgi.",
                "visual": "🍎 🍎 🍎 = 3 ta olma (Son: 3)"
            },
            "Qo'shish ( + )": {
                "emoji": "➕",
                "daktil": "Қ-Ў-Ш-И-Ш",
                "definition": "Ikki yoki undan ortiq guruhdagi narsalarni birga to'plash va ko'paytirish.",
                "visual": "🔴🔴 + 🔴 = 🔴🔴🔴 (2 + 1 = 3)"
            },
            "Ayirish ( - )": {
                "emoji": "➖",
                "daktil": "А-Й-И-Р-И-Ш",
                "definition": "Mavjud narsalar guruhidan ma'lum miqdorni kamaytirish yoki olib tashlash.",
                "visual": "🐤🐤🐤 - 🐤 = 🐤🐤 (3 - 1 = 2)"
            },
            "Kilogramm ( kg )": {
                "emoji": "⚖️",
                "daktil": "К-И-Л-О-Г-Р-А-М-М",
                "definition": "Narsalarning og'irligi va massasini o'lchaydigan birlik.",
                "visual": "📦 1 kg tarozi toshi = 1 kg Un xaltasi"
            },
            "Litr ( l )": {
                "emoji": "🥛",
                "daktil": "Л-И-Т-Р",
                "definition": "Suyuqliklar (suv, sut, sharbat) hajmini o'lchaydigan birlik.",
                "visual": "🫗 1 litrli idishdagi suv"
            },
            "Santimetr ( cm )": {
                "emoji": "📏",
                "daktil": "С-А-Н-Т-И-М-Е-Т-Р",
                "definition": "Uzunlikni chizg'ich yordamida o'lchaydigan kichik birlik.",
                "visual": "✏️ Qalam uzunligi = 8 cm"
            }
        }
        
        selected_term = st.selectbox("Atamani tanlang:", list(terms.keys()))
        t_data = terms[selected_term]
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"### {t_data['emoji']} {selected_term}")
            st.markdown(f"<div class='daktil-box'>🤟 Daktil yozilishi: {t_data['daktil']}</div>", unsafe_allow_html=True)
            st.write(f"**Tushuncha:** {t_data['definition']}")
        with col2:
            st.markdown("<div class='sim-box'>", unsafe_allow_html=True)
            st.markdown("#### Visual Tasvir:")
            st.markdown(f"### {t_data['visual']}")
            st.markdown("</div>", unsafe_allow_html=True)

    # 1.2 Daktil Sanagich (0-20)
    with sub_tab[1]:
        st.subheader("🤟 Bilingval Daktil va Barmoqlar Sanagichi (0 dan 20 gacha)")
        num = st.slider("Sanoqni tanlang:", 0, 20, 5)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric(label="Tanlangan Son", value=num)
            st.write(f"**Sonning tarkibi:** {num // 10} ta o'nlik va {num % 10} ta birlik")
            
            if num > 0:
                visual_representation = "🖐️ " * (num // 5) + "☝️ " * (num % 5)
            else:
                visual_representation = "✊ (Nol - Bo'sh)"
            st.markdown(f"### Visual Sanoq: {visual_representation}")
            
        with col_b:
            st.markdown("<div class='daktil-box'>", unsafe_allow_html=True)
            st.write("🤟 Imo-ishora va daktil ko'rsatgichi:")
            st.markdown(f"## Son: **{num}**")
            if num <= 10:
                st.write(f"Barmoqlar bilan ko'rsatish: **{num} ta barmoq ochiq**")
            else:
                st.write(f"1 ta to'liq o'nlik (10) va **{num-10} ta birlik barmoq**")
            st.markdown("</div>", unsafe_allow_html=True)

    # 1.3 Amaliy Kattaliklar Simulyatori
    with sub_tab[2]:
        st.subheader("⚖️ Amaliy Kattaliklar va O'lchov Birliklari Simulyatori")
        st.write("Maxsus darslikdagi **Kilogramm (tarozi)** va **Litr (idishlar)** mavzulari bo'yicha interaktiv mashq:")
        
        sim_type = st.radio("Simulyator turini tanlang:", ["⚖️ Tarozi va Kilogramm (kg)", "🥛 Idishlar va Litr (l)"])
        
        if "Tarozi" in sim_type:
            st.markdown("<div class='sim-box'>", unsafe_allow_html=True)
            st.markdown("### ⚖️ Interaktiv Tarozi Simulyatori")
            st.write("Chap va o'ng pallani tenglashtiring (Muvozanat hosil qiling):")
            
            col1, col2 = st.columns(2)
            with col1:
                left_weight = st.number_input("Chap palla (Meva/Mahsulot, kg):", 1, 10, 3)
                st.write("📦 Meva og'irligi:", "🍎 " * left_weight, f"({left_weight} kg)")
            with col2:
                right_weight = st.number_input("O'ng palla (Tarozi toshlari, kg):", 1, 10, 1)
                st.write("⚓ Tarozi toshlari:", "🏋️ " * right_weight, f"({right_weight} kg)")
                
            if left_weight == right_weight:
                st.success("✅ BARAKALLA! Tarozi pallalari tenglashdi (Muvozanat hosil bo'ldi)!")
            elif left_weight > right_weight:
                st.warning("⚠️ Chap palla og'irroq! O'ng pallaga yana tarozi toshini qo'shing.")
            else:
                st.info("ℹ️ O'ng palla og'irroq! Tarozi toshini kamaytiring.")
            st.markdown("</div>", unsafe_allow_html=True)
            
        else:
            st.markdown("<div class='sim-box'>", unsafe_allow_html=True)
            st.markdown("### 🥛 Interaktiv Litr va Suyuqlik Hajmi Simulyatori")
            litr = st.slider("Katta idishga necha litr suv quyasiz?", 1, 10, 4)
            st.write("Suv hajmi:", "🫗 " * litr, f"({litr} Litr)")
            st.info(f"💡 Uzoqroq ushlab tursangiz: {litr} Litr suv = {litr} ta 1-litrli bankani to'ldiradi!")
            st.markdown("</div>", unsafe_allow_html=True)

    # 1.4 Visual Arifmetik Masalalar
    with sub_tab[3]:
        st.subheader("🍎 Visual va Animatsiyali Arifmetik Masalalar")
        st.write("Eshitishida nuqsoni bo'lgan o'quvchilar uchun matnsiz, visual animatsion masalalar:")
        
        st.markdown("""
        **Masala Sharti:**
        Daraxtda **4 ta olma** bor edi. Shamol esib, **2 ta olma** yerga tushdi. Daraxtda nechta olma qoldi?
        """)
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### 🌳 Daraxtdagi olmalar:")
            st.markdown("### 🍎 🍎 🍎 🍎  ( 4 ta )")
            st.markdown("#### 🍃 Yerga tushgan olmalar:")
            st.markdown("### 🔻 🍎 🍎  ( 2 ta )")
            
        with col2:
            user_ans = st.number_input("Javobingizni kiriting:", 0, 10, 0)
            if st.button("Javobni tekshirish"):
                if user_ans == 2:
                    st.success("🎉 JUDA TO'G'RI! Yechim: 4 - 2 = 2 (ta olma qoldi)")
                else:
                    st.error("❌ Qayta sanab ko'ring. 4 tadan 2 tasi olib tashlendi.")


# ==========================================
# 2-BO'LIM: OMMAVIY VA INKLYUZIV MAKTAB UCHUN
# ==========================================
elif "2-BO'LIM" in main_section:
    st.markdown('<div class="main-title">🎒 OMMAVIY VA INKLYUZIV MAKTAB UCHUN MODUL</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">I.Repyova (2023) 1-sinf "Matematika" darsligi asosida yaratilgan interaktiv mantiqiy interfeys</div>', unsafe_allow_html=True)
    
    sub_tab2 = st.tabs([
        "🧩 Mantiqiy-Fazoviy Munosabatlar", 
        "🔢 Toq va Juft Sonlar", 
        "📐 Geometrik Chiziqlar va Siniq Chiziq", 
        "🤖 Surdo-Assistentli Mantiqiy Masalalar"
    ])
    
    # 2.1 Mantiqiy-Fazoviy Munosabatlar
    with sub_tab2[0]:
        st.subheader("🧩 Mantiqiy-Fazoviy Tushunchalar (Baland/Past, Uzun/Qisqa)")
        st.write("Ommaviy darslikdagi mantiqiy taqqoslash mashqlari:")
        
        item_choice = st.selectbox("Taqqoslash turini tanlang:", ["Uzun va Qisqa qalamlar", "Baland va Past uylar"])
        
        if "qalamlar" in item_choice:
            st.markdown("### ✏️ Qalamlarni taqqoslang:")
            st.write("1-Qalam: ✏️✏️✏️✏️✏️✏️ (Uzun - 12 cm)")
            st.write("2-Qalam: ✏️✏️✏️ (Qisqa - 6 cm)")
            ans = st.radio("Qaysi qalam UZUNROQ?", ["1-Qalam", "2-Qalam"])
            if ans == "1-Qalam":
                st.success("✅ To'g'ri! 1-Qalam 2-Qalamdan uzunroq.")
        else:
            st.markdown("### 🏢 Uylarni taqqoslang:")
            st.write("A-Bino: 🏢🏢🏢 (9 qavatli - Baland)")
            st.write("B-Bino: 🏠 (1 qavatli - Past)")
            ans = st.radio("Qaysi bino BALANDROQ?", ["A-Bino", "B-Bino"])
            if ans == "A-Bino":
                st.success("✅ To'g'ri! A-Bino baland bino hisoblanadi.")

    # 2.2 Toq va Juft Sonlar
    with sub_tab2[1]:
        st.subheader("🔢 Toq va Juft Sonlar Simulyatsiyasi")
        st.write("Darslikdagi Juft (2, 4, 6, 8, 10) va Toq (1, 3, 5, 7, 9) sonlarni ajratish moduli:")
        
        num_check = st.number_input("Sonni kiriting (1 dan 20 gacha):", 1, 20, 4)
        
        if num_check % 2 == 0:
            st.markdown(f"<div class='sim-box'><h2>🟢 {num_check} - JUFT SON</h2><p>Chunki uni 2 tadan juftlab ajratish mumkin! (Juftliklar: {'👫 ' * (num_check//2)})</p></div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='sim-box'><h2>🔴 {num_check} - TOQ SON</h2><p>Chunki 2 tadan juftlaganda 1 ta son juftsiz qolib ketadi! (Juftliklar: {'👫 ' * (num_check//2)} + 🧍)</p></div>", unsafe_allow_html=True)

    # 2.3 Geometrik Chiziqlar va Siniq Chiziq
    with sub_tab2[2]:
        st.subheader("📐 Geometrik Chiziqlar va Siniq Chiziq")
        st.write("To'g'ri chiziq, Kesma hamda Siniq chiziq va uning uchlarini o'rganish:")
        
        st.markdown("""
        * **To'g'ri chiziq:** Boshi va oxiri yo'q chiziq.
        * **Kesma:** Ikki tomonidan nuqta bilan chegaralangan to'g'ri chiziq bo'lagi.
        * **Siniq chiziq:** Bir nechta kesmalardan tashkil topgan va bir to'g'ri chiziqda yotmaydigan chiziq.
        """)
        
        segment_count = st.slider("Siniq chiziq nechta kesmadan (bo'g'indan) iborat bo'lsin?", 2, 6, 3)
        st.write("Siniq chiziq ko'rinishi:", "📈 " * segment_count)
        st.write(f"Ushbu siniq chiziqda **{segment_count} ta bo'g'in** va **{segment_count + 1} ta uch (nuqta)** bor.")

    # 2.4 Surdo-Assistentli Mantiqiy Masalalar
    with sub_tab2[3]:
        st.subheader("🤖 Surdo-Assistentli Mantiqiy Masalalar")
        st.write("Inklyuziv sinflarda eshitishida nuqsoni bo'lgan o'quvchi uchun soddalashtirilgan vizual masala:")
        
        st.info("🤖 **Surdo-Assistent tushuntirishi:** Masalani daktil va vizual belgilarda o'qing!")
        st.write("**Mantiqiy shart:** Akmalda 5 ta ko'k shar, Umidada esa Akmalnikidan 2 ta KO'PROQ shar bor. Umidada nechta shar bor?")
        
        st.markdown("Akmal: 🎈🎈🎈🎈🎈 (5 ta)")
        st.markdown("Umida: 🎈🎈🎈🎈🎈 + 🎈🎈 (5 + 2)")
        
        ans_m = st.number_input("Umidaning sharlar sonini kiriting:", 0, 15, 0)
        if st.button("Tekshirish"):
            if ans_m == 7:
                st.success("🎉 JUDA TO'G'RI! Yechim: 5 + 2 = 7 ta shar.")
            else:
                st.error("❌ Qayta urinib ko'ring (5 ga 2 ni qo'shing).")


# ==========================================
# 3-BO'LIM: O'QITUVCHI VA DIAGNOSTIKA PANELI
# ==========================================
else:
    st.markdown('<div class="main-title">📊 OQITUVCHI VA DIAGNOSTIKA PANELI</div>', unsafe_allow_html=True)
    st.markdown('<div class="sub-title">Oquvchilarning foveal diqqati va matematik ozlashtirish korsatkichlari monitoringi</div>', unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Sinfdagi o'quvchilar", "12 nafar", "Maxsus sinf")
    col2.metric("O'rtacha o'zlashtirish", "86%", "+12%")
    col3.metric("Foveal diqqat barqarorligi", "4.2 / 5.0", "Yuqori")
    
    st.markdown("---")
    st.subheader("📈 O'quvchilarning Matematik Kompetensiyalari Kesimida Tahlil")
    
    import pandas as pd
    chart_data = pd.DataFrame({
        'Kompentensiya/Soha': ['Visual Sanoq', 'Daktil Atamalar', 'Amaliy Kattaliklar (kg/l)', 'Siniq Chiziqlar', 'Matnli Masalalar'],
        'Ozlashtirish Darajasi (%)': [92, 88, 85, 78, 72]
    })
    
    st.bar_chart(chart_data.set_index('Kompentensiya/Soha'))
    st.success("💡 **Korreksion Xulosa:** Visual-daktil va simulyatorli usul matnli masalalarni o'zlashtirish ko'rsatkichini 18% ga oshirdi.")
