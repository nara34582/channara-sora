
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/sora_generate', methods=['POST'])
def sora_generate():
    data = request.json
    prompt = data.get('prompt', '')
    mode = data.get('mode', 'image')  # 'image' or 'video'

    # 仮想生成処理（実際には空エンジンと連携する部分）
    if mode == 'video':
        result = f"SORAが動画を生成しました: {prompt}"
    else:
        result = f"SORAが画像を生成しました: {prompt}"

    return jsonify({
        "status": "success",
        "mode": mode,
        "output": result
    })

if __name__ == '__main__':
    app.run(debug=True)
