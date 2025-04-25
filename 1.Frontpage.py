import streamlit as st

# --- Page config ---
st.set_page_config(
    page_title="Lever Dashboard",
    page_icon="🧬",
    layout="centered"
)

# --- Title ---
st.title("🧬 Welkom op het Lever Dashboard!")
st.markdown("---")

# --- Wat ---
st.header("🔍 Wat?")
st.markdown("• 🧪 Apps voor de geïnteresseerden in hepatologie en levertransplantatie.")

# --- Waarom ---
st.header("❓ Waarom?")
st.markdown("• 🧠 Omdat hersenen beter werken als processor dan als harde schijf.")

# --- Wie ---
st.header("👥 Wie?")
st.markdown("• 🔜 **VOLGT**")

# --- Disclaimers ---
st.markdown("---")
st.subheader("⚠️ Disclaimers:")
st.markdown(
    """
    - 🛠️ Dit is een hobby project bedoeld als naslagwerk  
    - 🚫 Deze apps zijn **géén officieel medisch advies**  
    - 📜 Er kunnen **geen rechten** aan worden ontleend  
    - 📬 Bij vragen, bugs, voorstellen of verbeterpunten: **EMAIL**
    """
)
