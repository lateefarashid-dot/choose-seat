import streamlit as st
st.set_page_config(page_title="Cinema Arrays", layout="centered")
st.title("🎬اختر مقعدك في السينما ")
# =========================
# تهيئة Session State
# =========================
if "selected_1D" not in st.session_state:
   st.session_state.selected_1D = None
if "selected_2D" not in st.session_state:
   st.session_state.selected_2D = None
# =========================
# القسم الأول: 1D
# =========================
st.header("🎟 القسم الأول ")
oneD = ["VIP1", "VIP2", "VIP3", "VIP4"]
cols1 = st.columns(len(oneD))
for i, seat in enumerate(oneD):
   with cols1[i]:
       if st.button(seat, key=f"1D_{i}"):
           if st.session_state.selected_1D is None:
               st.session_state.selected_1D = seat
               st.success(f"تم اختيار {seat}")
               st.code(f"VIPsection[{i}]")
           else:
               st.warning("🚫 يمكنك اختيار مقعد واحد فقط من القسم الأول")
st.divider()
# =========================
# القسم الثاني: 2D
# =========================
st.header("🎬 القسم الثاني ")
cinema = [
   ["A1", "A2", "A3", "A4"],
   ["B1", "B2", "B3", "B4"],
   ["C1", "C2", "C3", "C4"],
   ["D1", "D2", "D3", "D4"]
]
for r, row in enumerate(cinema):
   cols2 = st.columns(len(row))
   for c, seat in enumerate(row):
       with cols2[c]:
           if st.button(seat, key=f"2D_{r}_{c}"):
               if st.session_state.selected_2D is None:
                   st.session_state.selected_2D = seat
                   st.success(f"تم اختيار {seat}")
                   st.code(f"cinema[{r}][{c}]")
               else:
                   st.warning("🚫 يمكنك اختيار مقعد واحد فقط من القسم الثاني")
st.divider()
# =========================
# عرض الاختيارات
# =========================
st.subheader("📋 اختياراتك:")
st.write(f"🎟 1D: {st.session_state.selected_1D or '-'}")
st.write(f"🎬 2D: {st.session_state.selected_2D or '-'}")
# =========================
# زر إعادة التعيين
# =========================
if st.button("🔄 إعادة الاختيار"):
   st.session_state.selected_1D = None
   st.session_state.selected_2D = None
   
   





