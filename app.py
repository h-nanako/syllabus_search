from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    import Paper_syllabuys # Doc2Vecでベクトルを計算させるコードをimport
    name = request.form['name'] # Webで入力された単語
    
    'nameで入力された単語をPaper_syllabusに入れて推薦科目を出力'
    '--------------------------------------------------------'
    word1 = Paper_syllabuys.word(name)
    syllabus_vector2 = Paper_syllabuys.word_vector(word1)
    sylla_sim = Paper_syllabuys.vector(syllabus_vector2)
    '--------------------------------------------------------'

    return render_template('result.html', \
        name=name, \
        syllabus=sylla_sim)

if __name__ == "__main__":
    app.run(debug=False)