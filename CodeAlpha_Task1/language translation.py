# ============================================
# CodeAlpha Internship - Task 1
# Language Translation Tool
# Made by: Muhammad Jan
# ============================================

# Step 1: Libraries import karo
from deep_translator import GoogleTranslator
import gradio as gr

# Step 2: Languages ki list banao
LANGUAGES = {
    "English": "en",
    "Urdu": "ur",
    "French": "fr",
    "German": "de",
    "Spanish": "es",
    "Arabic": "ar",
    "Chinese": "zh-CN",
    "Japanese": "ja",
    "Hindi": "hi",
    "Turkish": "tr"
}

# Step 3: Translate karne wala function banao
def translate_text(text, source_lang, target_lang):
    
    # Check 1: Kya user ne kuch likha?
    if not text.strip():
        return "⚠️ Please enter some text first!"
    
    # Check 2: Kya dono languages same hain?
    if source_lang == target_lang:
        return "⚠️ Please select different languages!"
    
    # Check 3: Translate karo Google se
    try:
        # Source language ka code lo
        src_code = LANGUAGES[source_lang]
        
        # Target language ka code lo
        tgt_code = LANGUAGES[target_lang]
        
        # Google se translate karo
        result = GoogleTranslator(
            source=src_code,
            target=tgt_code
        ).translate(text)
        
        # Result wapas bhejo
        return result
    
    # Agar koi error aaye
    except Exception as error:
        return f"❌ Error: {str(error)}"


# Step 4: UI banao - Gradio se
with gr.Blocks(
    title="Language Translation Tool",
    theme=gr.themes.Soft()
) as app:
    
    # Title dikhao
    gr.Markdown("# 🌐 Language Translation Tool")
    gr.Markdown("#### CodeAlpha AI Internship | Muhammad Jan")
    gr.Markdown("---")
    
    # Language selection row
    with gr.Row():
        
        # Source language dropdown
        source_lang = gr.Dropdown(
            choices=list(LANGUAGES.keys()),
            value="English",
            label="🔤 From Language"
        )
        
        # Target language dropdown
        target_lang = gr.Dropdown(
            choices=list(LANGUAGES.keys()),
            value="Urdu",
            label="🌍 To Language"
        )
    
    # Input text box
    input_text = gr.Textbox(
        lines=5,
        placeholder="Type your text here...",
        label="✏️ Enter Text"
    )
    
    # Translate button
    translate_btn = gr.Button(
        "🔁 Translate Now",
        variant="primary",
        size="lg"
    )
    
    # Output text box
    output_text = gr.Textbox(
        lines=5,
        label="✅ Translated Text",
        interactive=False
    )
    
    # Clear button
    clear_btn = gr.Button(
        "🗑️ Clear",
        variant="secondary"
    )
    
    gr.Markdown("---")
    gr.Markdown("*Built with Python & Gradio | Powered by Google Translate*")
    
    # Button actions
    translate_btn.click(
        fn=translate_text,
        inputs=[input_text, source_lang, target_lang],
        outputs=output_text
    )
    
    clear_btn.click(
        fn=lambda: ("", ""),
        inputs=[],
        outputs=[input_text, output_text]
    )

# Step 5: App chalao!
app.launch(share=True)