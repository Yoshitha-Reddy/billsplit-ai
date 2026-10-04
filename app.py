import streamlit as st
from google import genai
from google.genai import types
import json, os
from dotenv import load_dotenv
load_dotenv()

st.set_page_config(page_title="BillSplit", page_icon="🧾", layout="centered")

st.markdown("""
<style>
    .stApp { background: #F6F7FF!important; }
    header, [data-testid="stDecoration"] { display: none!important; }
    .hero {
        background: linear-gradient(135deg, #4F46E5 0%, #8B5CF6 100%);
        padding: 28px; border-radius: 22px; text-align: center; color: white;
        box-shadow: 0 10px 25px rgba(79,70,229,0.25); margin-bottom: 20px;
    }
    .hero h1 { color: white!important; font-size: 32px!important; margin: 0!important; }
    .card {
        background: white!important; padding: 24px!important; border-radius: 20px!important;
        box-shadow: 0 2px 15px rgba(0,0,0,0.05)!important; border: 1px solid #EEF2FF!important;
        margin-bottom: 16px!important;
    }
    .item-row {
        display: flex; justify-content: space-between;
        padding: 12px 0; border-bottom: 1px solid #F1F5F9;
        color: #334155;
    }
</style>
""", unsafe_allow_html=True)

API_KEY = os.getenv("GEMINI_API_KEY") or "PASTE_YOUR_KEY_HERE"
client = genai.Client(api_key=API_KEY) if API_KEY and "PASTE" not in API_KEY else None
if "data" not in st.session_state:
    st.session_state.data = None

st.markdown('<div class="hero"><h1>🧾 BillSplit</h1><p style="color:#DDD6FE; margin:8px 0 0 0;">Scan • Split • Share</p></div>', unsafe_allow_html=True)

# UPLOAD SECTION
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown("**📸 Upload Receipt**")
uploaded = st.file_uploader("", type=["jpg","jpeg","png"], label_visibility="collapsed")

if uploaded and not st.session_state.data:
    st.image(uploaded, use_container_width=True)
    if st.button("✨ Scan Bill with AI", use_container_width=True, type="primary"):
        if not client:
            st.error("Add GEMINI_API_KEY in .env file")
        else:
            with st.spinner("AI reading your bill..."):
                try:
                    img_part = types.Part.from_bytes(data=uploaded.getvalue(), mime_type=uploaded.type)
                    res = client.models.generate_content(
                        model="gemini-3-flash-preview",
                        contents=["Extract to JSON: {\"restaurant\":\"Name\", \"items\":[{\"name\":\"Biryani\",\"price\":300},{\"name\":\"Coke\",\"price\":90}], \"total\":390} Only JSON, no markdown", img_part]
                    )
                    txt = res.text.replace("```json","").replace("```","").strip()
                    st.session_state.data = json.loads(txt)
                    st.rerun()
                except Exception as e:
                    st.error(f"Error: {e}")
else:
    if not st.session_state.data:
        st.info("👆 Upload a bill image to start")
st.markdown('</div>', unsafe_allow_html=True)

# RESULT SECTION
if st.session_state.data:
    data = st.session_state.data
    
    # Bill Details
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown(f"### 🏨 {data.get('restaurant','Your Bill')}")
    for it in data.get("items",[]):
        st.markdown(f"<div class='item-row'><span>{it.get('name')}</span><b>₹{it.get('price')}</b></div>", unsafe_allow_html=True)
    st.markdown(f"<div style='display:flex; justify-content:space-between; padding-top:16px; font-weight:800; font-size:19px; color:#1E293B;'><span>Total</span><span>₹{data.get('total',0)}</span></div>", unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # SPLIT SECTION - WITH SLIDER
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### 👥 Split Between")
    
    people = st.slider("Number of people", min_value=2, max_value=10, value=3)
    names_text = st.text_input(f"Names of {people} people (comma)", value="You, Asha, Ravi")
    names_list = [n.strip() for n in names_text.split(",") if n.strip()]
    
    total = float(data.get('total', 0))
    count = people
    per_person = total / count if count else 0
    
    # Big amount card
    st.markdown(f"""
    <div style='background:linear-gradient(135deg,#4F46E5,#8B5CF6); color:white; padding:20px; border-radius:16px; text-align:center; margin:16px 0;'>
        <div style='opacity:0.85; font-size:13px; letter-spacing:1px;'>EACH PAYS</div>
        <div style='font-size:32px; font-weight:800; margin-top:4px;'>₹{per_person:.0f}</div>
        <div style='opacity:0.8; font-size:12px; margin-top:4px;'>{count} people • Total ₹{total:.0f}</div>
    </div>
    """, unsafe_allow_html=True)

    # Individual breakdown
    if names_list:
        cols = st.columns(min(len(names_list), 3))
        for i, name in enumerate(names_list[:6]):
            with cols[i % 3]:
                st.markdown(f"<div style='background:#F8FAFF; border:1px solid #E0E7FF; padding:10px; border-radius:12px; text-align:center; margin-bottom:8px;'><div style='font-size:12px; color:#64748B;'>{name}</div><div style='font-weight:700; color:#4F46E5;'>₹{per_person:.0f}</div></div>", unsafe_allow_html=True)

    if st.button("📲 Share on WhatsApp", use_container_width=True, type="primary"):
        st.balloons()
        msg = f"🧾 BillSplit\n🏨 {data.get('restaurant','Bill')}\n💰 Total: ₹{total:.0f}\n👥 {count} people\nEach: ₹{per_person:.0f}\n\n" + "\n".join([f"• {n}: ₹{per_person:.0f}" for n in names_list])
        st.code(msg)
        st.success("✅ WhatsApp message ready! (Simulated)")
        
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("🔄 Scan New Bill", use_container_width=True):
        st.session_state.data = None
        st.rerun()

st.markdown("<p style='text-align:center; color:#94A3B8; font-size:11px; margin-top:20px;'>© 2026 BillSplit • Premium Edition</p>", unsafe_allow_html=True)