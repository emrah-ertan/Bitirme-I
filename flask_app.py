# flask_app.py
import os
import shutil

from flask import Flask, render_template, request, jsonify, redirect, send_file
import main

app = Flask(__name__, template_folder="templates", static_url_path='/GeneratedImages', static_folder='GeneratedImages')

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    user_prompt_value = data.get('userPrompt', '')
    step_count = data.get('stepCount', 0)
    scale_value = data.get('scaleValue', 0)
    black_level_value = data.get('blackLevelValue', 0)

    # main.py içindeki run fonksiyonunu ve indir fonksiyonunu çağırma
    main.userPrompt = user_prompt_value
    main.adimSayisi = step_count
    main.olcek = scale_value
    main.blackLevel = black_level_value
    deger = main.run()
    deger2 = main.indir()

    if deger == 1 and deger2 == 1:
        return redirect("/")
    else:
        return 'İşlem başarısız'

@app.route('/download', methods=['POST'])
def download():
    folder_path = 'GeneratedImages'  # Klasörünüzün yolu

    # Klasördeki dosyaları ZIP dosyasına sıkıştır
    shutil.make_archive(folder_path, 'zip', folder_path)

    # ZIP dosyasını indir
    return send_file(f"{folder_path}.zip", as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
