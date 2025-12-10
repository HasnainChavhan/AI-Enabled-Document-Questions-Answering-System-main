import streamlit as st
import os
import docx
from PyPDF2 import PdfReader

st.set_page_config(
    page_title="Document Upload", 
    page_icon="📁",
    layout="wide"
)

# Header
st.markdown("""
<div style="text-align: center; padding: 2rem 0; background: linear-gradient(90deg, #28a745 0%, #20c997 100%); border-radius: 10px; margin-bottom: 2rem;">
    <h1 style="color: white; margin: 0; font-size: 2.5rem; font-weight: 600;">📁 Document Upload Center</h1>
    <p style="color: #f0f0f0; margin: 0.5rem 0 0 0; font-size: 1.1rem;">Upload and manage your documents for AI analysis</p>
</div>
""", unsafe_allow_html=True)

UPLOAD_DIR = "uploaded_docs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

def extract_text(file_path, file_type):
    if file_type == "text/plain":
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    elif file_type == "application/pdf":
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            return "\n".join([p.extract_text() for p in reader.pages if p.extract_text()])
    elif file_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("### 📄 Upload Documents")
    uploaded_files = st.file_uploader(
        "Select one or more documents to upload",
        type=["txt", "pdf", "docx"],
        accept_multiple_files=True,
        help="Supported formats: TXT, PDF, DOCX. Multiple files will be combined."
    )

with col2:
    st.markdown("### 📊 Upload Statistics")
    
    # Show existing files
    existing_files = [f for f in os.listdir(UPLOAD_DIR) if f.endswith(('.txt', '.pdf', '.docx'))]
    if existing_files:
        st.success(f"✅ {len(existing_files)} files in storage")
        with st.expander("View stored files"):
            for file in existing_files:
                st.text(f"📄 {file}")
    else:
        st.info("📂 No files uploaded yet")

if uploaded_files:
    with st.spinner("🔄 Processing uploaded files..."):
        all_text = ""
        saved_files = []
        
        progress_bar = st.progress(0)
        
        for i, file in enumerate(uploaded_files):
            # Update progress
            progress_bar.progress((i + 1) / len(uploaded_files))
            
            save_path = os.path.join(UPLOAD_DIR, file.name)
            with open(save_path, "wb") as f:
                f.write(file.getbuffer())
            saved_files.append(file.name)
            
            # Extract text with error handling
            try:
                extracted_text = extract_text(save_path, file.type)
                all_text += extracted_text + "\n\n"
                st.success(f"✅ Processed: {file.name} ({len(extracted_text)} characters)")
            except Exception as e:
                st.error(f"❌ Failed to process {file.name}: {str(e)}")
        
        progress_bar.empty()
    
    st.session_state.doc_content = all_text
    st.session_state.uploaded_files = saved_files
    
    # Summary
    st.markdown("---")
    st.markdown("### 🎉 Upload Complete")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Files Uploaded", len(saved_files))
    with col2:
        st.metric("Total Characters", f"{len(all_text):,}")
    with col3:
        st.metric("Words (approx)", f"{len(all_text.split()):,}")
    
    if st.button("🎤 Go to Voice Chat", type="primary", use_container_width=True):
        st.switch_page("app.py")

# Reload saved files on refresh
elif 'uploaded_files' in st.session_state:
    with st.spinner("🔄 Loading previously uploaded documents..."):
        all_text = ""
        loaded_count = 0
        
        for file_name in st.session_state.uploaded_files:
            file_path = os.path.join(UPLOAD_DIR, file_name)
            if os.path.exists(file_path):
                file_type = "application/pdf" if file_name.endswith(".pdf") else (
                    "application/vnd.openxmlformats-officedocument.wordprocessingml.document" if file_name.endswith(".docx") else "text/plain"
                )
                try:
                    all_text += extract_text(file_path, file_type) + "\n\n"
                    loaded_count += 1
                except Exception as e:
                    st.warning(f"⚠️ Could not reload {file_name}: {str(e)}")
        
        st.session_state.doc_content = all_text
        
        if loaded_count > 0:
            st.info(f"📄 Loaded {loaded_count} previously uploaded documents ({len(all_text):,} characters)")
            
            if st.button("🎤 Continue to Voice Chat", type="primary", use_container_width=True):
                st.switch_page("app.py")
else:
    st.markdown("### 🚀 Getting Started")
    st.info("""
    **Welcome to the Document Upload Center!**
    
    1. 📁 Select your documents using the file uploader above
    2. 🔄 Wait for processing to complete
    3. 🎤 Navigate to the Voice Chat to start asking questions
    
    **Supported file types:** PDF, DOCX, TXT
    """)

# Add professional styling
st.markdown("""
<style>
    .main .block-container {
        padding-top: 1rem;
        max-width: 1200px;
    }
    
    .stButton > button {
        border-radius: 8px;
        border: none;
        padding: 0.6rem 1.2rem;
        font-weight: 600;
        font-size: 0.95rem;
        transition: all 0.3s ease;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .stButton > button[kind="primary"] {
        background: linear-gradient(45deg, #28a745, #20c997);
        color: white;
    }
    
    .stButton > button[kind="primary"]:hover {
        background: linear-gradient(45deg, #20c997, #17a2b8);
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    .stSuccess, .stInfo, .stWarning, .stError {
        border-radius: 8px;
        border: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)
