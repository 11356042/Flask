import os
from flask import Flask, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv

# 1. 初始化與環境變數載入
load_dotenv()
app = Flask(__name__)

# 2. 設定 Gemini Client
# 請確保你的 .env 檔案中有 GEMINI_API_KEY=你的金鑰
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

# 指定剛才從清單中確認過的模型名稱
CURRENT_MODEL = "models/gemini-3-flash-preview"

# --- 診斷函數：啟動時在終端機再次確認 ---
def show_api_status():
    print("\n" + "="*40)
    print("🚀 Flask 專業 AI 系統啟動中...")
    print(f"📡 目前設定模型: {CURRENT_MODEL}")
    print("="*40 + "\n")

# 3. 頁面路由 (Jinja 渲染)
@app.route('/')
def index():
    """渲染首頁，這會用到你的 base.html 與 index.html"""
    return render_template('index.html')

# 4. API 路由 (AI 對話處理)
@app.route('/chat', methods=['POST'])
def chat():
    """處理來自前端的 AJAX 請求"""
    try:
        # 接收前端傳來的 JSON 訊息
        data = request.get_json()
        user_input = data.get('message')

        if not user_input:
            return jsonify({"error": "未收到訊息内容"}), 400

        # 向 Gemini 發送請求
        # 這裡使用了你的清單中確認存在的 models/gemini-2.5-flash
        response = client.models.generate_content(
            model=CURRENT_MODEL,
            contents=user_input
        )

        # 回傳 AI 的回覆文本
        return jsonify({
            "status": "success",
            "reply": response.text
        })

    except Exception as e:
        print(f"❌ 錯誤發生: {str(e)}")
        # 回傳詳細錯誤訊息給前端，方便除錯
        return jsonify({
            "status": "error",
            "error": str(e)
        }), 500

# 5. 程式進入點
if __name__ == '__main__':
    show_api_status()
    # 啟動開發伺服器
    app.run(debug=True)