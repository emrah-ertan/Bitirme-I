# flask_app.py
import shutil
from flask import Flask, render_template, request, jsonify, send_file
import main

app = Flask(__name__, template_folder="templates", static_url_path='/GeneratedImages', static_folder='GeneratedImages')

@app.after_request
def add_header(response):
    response.cache_control.no_cache = True
    response.cache_control.no_store = True
    response.cache_control.must_revalidate = True
    response.cache_control.max_age = 0
    return response

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

    if user_prompt_value != '':
        main.userPrompt = user_prompt_value
    if int(step_count) != 0:
        main.adimSayisi = step_count
    main.olcek = scale_value
    main.blackLevel = black_level_value
    deger = main.run()
    deger2 = main.indir()

    if deger == 1 and deger2 == 1:
        return jsonify({'success': True})
    else:
        return jsonify({'success': False, 'message': 'İşlem başarısız'})


@app.route('/download', methods=['POST'])
def download():
    # İndirme İşlemi:
    folder_path = 'GeneratedImages'  # klasör yolu
    # klasördeki dosyaları zip haline getirir
    shutil.make_archive(folder_path, 'zip', folder_path)
    # zip'i indirir
    return send_file(f"{folder_path}.zip", as_attachment=True)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)