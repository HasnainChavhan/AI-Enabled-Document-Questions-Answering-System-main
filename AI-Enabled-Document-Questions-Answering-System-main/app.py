import streamlit as st
from voice_functions import listen, threaded_speak, ask_ollama, stop_tts

st.set_page_config(
    page_title="AI Document Assistant", 
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
st.markdown("""
<div style="text-align: center; padding: 2rem 0; background: linear-gradient(90deg, #667eea 0%, #764ba2 100%); border-radius: 10px; margin-bottom: 2rem;">
    <h1 style="color: white; margin: 0; font-size: 2.5rem; font-weight: 600;">📄 AI Document Assistant</h1>
    <p style="color: #f0f0f0; margin: 0.5rem 0 0 0; font-size: 1.1rem;">Intelligent Voice-Powered Document Analysis</p>
</div>
""", unsafe_allow_html=True)

# Initialize session state
if 'doc_content' not in st.session_state:
    st.session_state.doc_content = ""
if 'response' not in st.session_state:
    st.session_state.response = ""
if 'history' not in st.session_state:
    st.session_state.history = []
if 'paused' not in st.session_state:
    st.session_state.paused = False
if 'user_input' not in st.session_state:
    st.session_state.user_input = ""
if 'text_question' not in st.session_state:
    st.session_state.text_question = ""

# Sidebar
with st.sidebar:
    st.markdown("### 📊 System Status")
    
    # Document status
    if st.session_state.doc_content.strip():
        st.success("✅ Document Loaded")
        doc_length = len(st.session_state.doc_content)
        st.info(f"📄 {doc_length:,} characters")
    else:
        st.warning("⚠️ No Document")
        st.info("Upload a document in Admin Panel")
    
    st.markdown("---")
    st.markdown("### 🎯 Quick Actions")
    
    if st.button("🔄 Clear History", use_container_width=True):
        st.session_state.history = []
        st.rerun()
    
    if st.button("📁 Go to Upload", use_container_width=True):
        st.switch_page("pages/1_Admin_Upload.py")

# Main content area
col1, col2 = st.columns([2, 1])

with col1:
    # Interaction mode selector
    interaction_mode = st.radio(
        "Choose interaction mode:",
        ["💬 Text Chat", "🎤 Voice Chat"],
        horizontal=True
    )
    
    st.markdown("---")
    
    if interaction_mode == "💬 Text Chat":
        st.markdown("### 💬 Text Chat")
        
        # Text input with better styling
        text_input = st.text_input(
            "💭 Ask a question about your document:",
            placeholder="Type your question here... (e.g., Summarize this document)",
            key="text_question",
            help="Ask anything about the uploaded document"
        )
        
        # Send and audio control buttons
        send_col1, send_col2, send_col3 = st.columns([1, 1, 2])
        with send_col1:
            send_button = st.button("📤 Send", use_container_width=True, type="primary")
        with send_col2:
            text_stop_button = st.button("🔇 Stop Audio", use_container_width=True)
        
        # Status area for text chat
        text_status = st.empty()
        
    else:
        st.markdown("### 🎤 Voice Interaction")
        
        # Status area
        status_placeholder = st.empty()
        
        # Control buttons
        button_col1, button_col2, button_col3 = st.columns(3)
        
        with button_col1:
            ask_button = st.button("🎤 Start Listening", use_container_width=True, type="primary")
        
        with button_col2:
            stop_button = st.button("⏹️ Stop Audio", use_container_width=True)
        
        with button_col3:
            end_button = st.button("🔚 End Session", use_container_width=True)

with col2:
    st.markdown("### 💡 Tips")
    
    if interaction_mode == "💬 Text Chat":
        st.info("""
        **Text Chat Mode:**
        1. Upload documents in Admin Panel
        2. Type your question in the text box
        3. Click 'Send' to get AI response
        4. Listen to AI response + view in chat
        
        **Benefits:**
        - Faster typing input
        - Audio + visual output
        - Easy copy/paste
        - Stop audio anytime
        """)
    else:
        st.info("""
        **Voice Chat Mode:**
        1. Upload documents in Admin Panel
        2. Click 'Start Listening'
        3. Ask questions about your document
        4. Listen to AI responses
        
        **Benefits:**
        - Hands-free operation
        - Natural conversation
        - Audio responses
        """)
    
    st.markdown("**Sample questions:**")
    st.markdown("""
    - "Summarize this document"
    - "What are the key points?"
    - "Find information about..."
    - "Explain the main concepts"
    """)

# Define speak_response function
def speak_response(text):
    try:
        stop_tts()
        st.session_state.paused = False
        audio_path = threaded_speak(text)
        if audio_path:
            st.audio(audio_path, format="audio/mp3", autoplay=True)
    except Exception as e:
        st.error(f"Audio generation failed: {str(e)}")

# Conversation History
if st.session_state.history:
    st.markdown("---")
    st.markdown("### 💬 Chat History")
    
    # Create a scrollable chat container
    chat_container = st.container()
    
    with chat_container:
        # Display in chronological order (oldest first)
        for i, (q, r) in enumerate(st.session_state.history):
            # User message
            st.markdown(f"""
            <div style="
                display: flex;
                justify-content: flex-end;
                margin: 1rem 0;
            ">
                <div style="
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    color: white;
                    padding: 0.75rem 1rem;
                    border-radius: 18px 18px 4px 18px;
                    max-width: 70%;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.1);
                    font-size: 0.95rem;
                    line-height: 1.4;
                ">
                    {q}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            # AI response with action buttons
            response_col1, response_col2 = st.columns([4, 1])
            
            with response_col1:
                st.markdown(f"""
                <div style="
                    background: #f7f7f8;
                    color: #374151;
                    padding: 0.75rem 1rem;
                    border-radius: 18px 18px 18px 4px;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                    border: 1px solid #e5e7eb;
                    font-size: 0.95rem;
                    line-height: 1.5;
                    white-space: pre-wrap;
                    margin-bottom: 0.5rem;
                ">
                    <div style="
                        display: flex;
                        align-items: center;
                        margin-bottom: 0.5rem;
                        font-weight: 600;
                        color: #059669;
                        font-size: 0.85rem;
                    ">
                        🤖 AI Assistant
                    </div>
                    {r}
                </div>
                """, unsafe_allow_html=True)
            
            with response_col2:
                # Action buttons for each response
                action_col1, action_col2 = st.columns(2)
                
                with action_col1:
                    if st.button("🔊", key=f"replay_{i}", help="Replay audio", use_container_width=True):
                        speak_response(r)
                
                with action_col2:
                    if st.button("📋", key=f"copy_{i}", help="Copy response", use_container_width=True):
                        st.code(r, language=None)
                        st.success("Response displayed above for copying!")

# Handle interactions based on mode
if interaction_mode == "💬 Text Chat":
    # Handle text chat
    if send_button and text_input.strip():
        user_input = text_input.strip()
        text_status.success(f"✅ **Question:** {user_input}")
        
        if st.session_state.doc_content.strip() == "":
            response = "⚠️ Please upload a document first using the Admin Panel."
        else:
            with st.spinner("🤖 Processing your question..."):
                context = st.session_state['doc_content']
                response = ask_ollama(user_input, context)
        
        st.session_state.response = response
        st.session_state.history.append((user_input, response))
        text_status.success("✅ **Response generated successfully**")
        
        # Read the response aloud in text chat mode too
        speak_response(response)
        st.rerun()
    
    elif send_button and not text_input.strip():
        text_status.warning("⚠️ Please enter a question first.")
    
    # Handle stop audio in text mode
    if 'text_stop_button' in locals() and text_stop_button:
        stop_tts()
        st.session_state.paused = True
        text_status.info("🔇 Audio output stopped.")

else:
    # Handle voice chat
    if 'ask_button' in locals() and ask_button:
        # Show listening status immediately
        status_placeholder.info("🎙️ **LISTENING...** Speak now!")
        
        with st.spinner("🎙️ Listening... Please speak clearly"):
            user_input = listen()

        if "ERROR" not in user_input:
            st.session_state.user_input = user_input
            status_placeholder.success(f"✅ **Heard:** {user_input}")

            if st.session_state.doc_content.strip() == "":
                response = "⚠️ Please upload a document first using the Admin Panel."
            else:
                with st.spinner("🤖 Processing your question..."):
                    context = st.session_state['doc_content']
                    response = ask_ollama(user_input, context)

            st.session_state.response = response
            st.session_state.history.append((user_input, response))
            status_placeholder.success(f"✅ **Response generated successfully**")
            speak_response(response)
            st.rerun()
        else:
            status_placeholder.error("❌ Could not understand your voice. Please try again.")
            st.session_state.response = ""

    if 'stop_button' in locals() and stop_button:
        stop_tts()
        st.session_state.paused = True
        status_placeholder.info("🔇 Audio output stopped.")

    if 'end_button' in locals() and end_button:
        st.session_state.history = []
        st.session_state.response = ""
        st.session_state.user_input = ""
        status_placeholder.success("✅ Session ended. Ready for new conversation.")

# Universal clear history button
st.markdown("---")
clear_col1, clear_col2 = st.columns([1, 1])
with clear_col1:
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.history = []
        st.success("✅ Chat history cleared!")
        st.rerun()

# Professional CSS styling
st.markdown("""
<style>
    /* Main container styling */
    .main .block-container {
        padding-top: 1rem;
        max-width: 1200px;
    }
    
    /* Button styling */
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
        background: linear-gradient(45deg, #007bff, #0056b3);
        color: white;
    }
    
    .stButton > button[kind="primary"]:hover {
        background: linear-gradient(45deg, #0056b3, #004085);
        transform: translateY(-1px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.15);
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #f8f9fa;
    }
    
    /* Chat styling */
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 0.5rem 0;
        animation: fadeIn 0.3s ease-in;
    }
    
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Status messages */
    .stSuccess, .stInfo, .stWarning, .stError {
        border-radius: 8px;
        border: none;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    /* Text input styling */
    .stTextInput > div > div > input {
        border-radius: 20px;
        border: 2px solid #e5e7eb;
        padding: 0.75rem 1rem;
        font-size: 0.95rem;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Custom spacing */
    .element-container {
        margin-bottom: 1rem;
    }
    
    /* Small action buttons */
    .stButton > button:not([kind="primary"]) {
        background: #f8f9fa;
        color: #6c757d;
        font-size: 1.2rem;
        padding: 0.4rem;
        min-height: 2rem;
        width: 100%;
    }
    
    .stButton > button:not([kind="primary"]):hover {
        background: #e9ecef;
        color: #495057;
    }
</style>
""", unsafe_allow_html=True)
