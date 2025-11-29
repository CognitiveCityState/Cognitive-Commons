import os
import sys
import locale
import logging

# ===================== Environment & Encoding Configuration =====================
logging.disable(logging.CRITICAL)

try:
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
except:
    locale.setlocale(locale.LC_ALL, '')

os.environ["PYTHONIOENCODING"] = "utf-8:ignore"
os.environ["LC_ALL"] = "en_US.UTF-8"
os.environ["LANG"] = "en_US.UTF-8"

import gradio as gr
import webbrowser
from datetime import datetime
import io
import threading
from contextlib import redirect_stdout, redirect_stderr

original_stdout = sys.stdout
original_stderr = sys.stderr


class SafeSilentStream(io.BytesIO):
    def write(self, s):
        if isinstance(s, str):
            s = s.encode('utf-8', errors='ignore')
        return super().write(s)

    def isatty(self):
        return False

    def fileno(self):
        return 1

    def flush(self):
        pass

    def close(self):
        pass


sys.path.append(os.path.dirname(os.path.abspath(__file__)))
engine = None
engine_lock = threading.Lock()


def init_engine(api_key):
    global engine
    with engine_lock:
        init_stream = SafeSilentStream()
        os.environ["DASHSCOPE_API_KEY"] = api_key

        with redirect_stdout(init_stream), redirect_stderr(init_stream):
            from RAMTN import StrategicCognitiveEngine
            engine = StrategicCognitiveEngine(confidence_threshold=0.75, max_units=2)

    return "✅ Engine initialized successfully!"


def analyze(expert_case, user_question):
    if not engine:
        return "❌ Please initialize the engine first with a valid API key!"

    try:
        # Preprocess input
        expert_case = expert_case.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')
        user_question = user_question.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')

        analysis_stream = SafeSilentStream()

        with engine_lock:
            sys.stdout = analysis_stream
            sys.stderr = analysis_stream

            # Reinitialize engine
            from RAMTN import StrategicCognitiveEngine
            temp_engine = StrategicCognitiveEngine(confidence_threshold=0.75, max_units=2)

            # Execute core analysis (完整获取报告的步骤)
            extraction_result = temp_engine.extract_strategic_framework(expert_case)
            implantation_result = temp_engine.implant_strategy(user_question)
            full_report = temp_engine.get_comprehensive_report()  # 补上这行！

            # Cleanse report
            full_report = full_report.encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')

            sys.stdout = original_stdout
            sys.stderr = original_stderr

        # Save report
        report_path = os.path.join(os.path.expanduser("~"),
                                   f"ramtn_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md")
        with open(report_path, "wb") as f:
            f.write(full_report.encode('utf-8', errors='ignore'))

        return f"✅ Analysis completed! Report saved to: {report_path}\n\n{full_report}"

    except Exception as e:
        safe_error = str(e).encode('utf-8', errors='ignore').decode('utf-8', errors='ignore')
        return f"❌ Analysis failed: {safe_error}"


# ===================== Gradio Interface =====================
with gr.Blocks() as demo:
    gr.Markdown("# RAMTN Strategic Cognition Analysis System")
    gr.Markdown("### How to Apply for DashScope API Key:")
    gr.Markdown("""
    1. Visit [DashScope Official Website](https://dashscope.aliyun.com/)
    2. Register/login with your Alibaba Cloud account
    3. Navigate to **API Key Management** in the console
    4. Click **Create API Key** and copy the generated key
    5. Paste the key below and initialize the engine

    ⚠️ **Important**: One analysis takes approximately 2-3 minutes. Please be patient!
    """)

    api_key = gr.Textbox(label="DashScope API Key", type="password", placeholder="Paste your API key here...")
    init_btn = gr.Button("Initialize Engine")
    init_status = gr.Textbox(label="Initialization Status", interactive=False)

    expert_case = gr.Textbox(label="Expert Case (Strategic Scenario)", lines=8,
                             placeholder="Enter the strategic case text here...")
    user_question = gr.Textbox(label="Analysis Question", lines=3, placeholder="Enter your strategic question here...")
    analyze_btn = gr.Button("Start Analysis")
    result = gr.Textbox(label="Analysis Result", lines=15)

    init_btn.click(init_engine, inputs=[api_key], outputs=[init_status])
    analyze_btn.click(analyze, inputs=[expert_case, user_question], outputs=[result])

if __name__ == "__main__":
    demo.launch(server_port=8080)
    webbrowser.open("http://localhost:8080")