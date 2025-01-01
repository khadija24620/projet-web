from flask import Flask, request, redirect, url_for ,render_template_string, render_template
app=Flask(__name__) 

@app.route('/')
def home():
    return render_template('projet web.html')

@app.route('/Desert_animals')
def Desert_animals():
    return render_template('pictures-inter.html')

@app.route('/Fennec_Fox')
def Fennec_Fox():
    return render_template('page2.html')

@app.route('/Meerkats')
def Meerkats():
    return render_template('page3.html')

@app.route('/Albino_hedgehogs')
def Albino_hedgehogs():
    return render_template('page4.html')




@app.route('/Forest_animals')
def Forest_animals():
    return render_template('inter2.html')

@app.route('/Black_Leopard')
def Black_Leopard():
    return render_template('LEOPARD.html')

@app.route('/Philippine_Eagle')
def Philippine_Eagle():
    return render_template('eagle.html')

@app.route('/Poison_Dart_Frog')
def Poison_Dart_Frog():
    return render_template('frog.html')



@app.route('/Sea_animals')
def Sea_animals():
    return render_template('inter3.html')
@app.route('/pink_dolphine')
def pink_dolphine():
    return render_template('dolphine.html')

@app.route('/symphysodon')
def symphysodon():
    return render_template('symphysodon.html')

@app.route('/dragonfish')
def dragonfish():
    return render_template('dragonfish.html')


@app.route('/Snow_animals')
def Snow_animals():
    return render_template('Snow animals.html')


@app.route('/form')
def form():
    return render_template('form.html')


@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name', 'utilisateur')
    # Rediriger vers la page du quiz avec le nom de l'utilisateur
    return redirect(url_for('quiz', name=name))

@app.route('/quiz', methods=['GET','POST'])
def quiz():
    name = request.args.get('name', 'utilisateur')
    if request.method == 'GET':
        return render_template('quiz.html',name=name)
    else:
        return redirect(url_for('quiz_submit', name=name))
@app.route('/quiz_submit', methods=['POST'])
def quiz_submit():  
    name = request.args.get('name', 'utilisateur') 
    answers = {
    'q1': 'a',  # Autruche
    'q2': 'b',  # Tortue des Galápagos
    'q3': 'c',  # Vache
    'q4': 'a',  # Cheval
    'q5': 'b',  # Chauve-souris bourdon
    'q6': 'c'   # Hippocampe
    }
    score = 0  
    incorrect_answers = {}


    if request.method == 'POST':
        # Vérifie les réponses données par l'utilisateur
        for question, correct_answer in answers.items():
            user_answer = request.form.get(question)
            if user_answer == correct_answer:
                score = score + 1 
            else:
                incorrect_answers[question] = correct_answer  # Ajoute les bonnes réponses


    return render_template_string('''<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Adventures into the Heart of Wildlife</title>
    <link rel="icon" href="{{url_for('static',filename='logo.png')}}" type="image/png">
    <link rel="stylesheet" href="{{url_for('static',filename='bootstrap.css')}}">
    <link rel="stylesheet" href="{{url_for('static',filename='quiz.css')}}">
    <style>
        body {
            background-image: url("{{ url_for('static', filename='quiz.jpg') }}");
            background-size: cover;
            background-position: center;
            margin: 0;
            padding: 0;
            font-size: 25px;
            color: white;
            text-align: justify;
            line-height: 1.6;
            display: flex;
            flex-direction: column;
            align-items: center;
            box-sizing: border-box;
        }

        h1 {
            color: rgb(107, 129, 8);
            font-family: 'Times New Roman', Times, serif;
            text-shadow: 2px 5px 4px rgb(168, 218, 90);
            margin-bottom: 0.5em;
        }

        .content {
            width: 80%;
            padding: 20px;
            background: rgba(0, 0, 0, 0.5);
            border-radius: 15px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
            margin: 20px 0;
            margin-top: 100px;                     

            overflow-wrap: break-word; /* Pour éviter que le texte ne déborde */
        }

        .result-container {
            border: 2px solid rgba(200, 255, 2, 0.4);
            box-shadow: 5px 5px 5px rgba(175, 250, 0, 0.63);
            color: whitesmoke;
            font-size: large;
            line-height: 1.6;
            margin-bottom: 50px;
            padding: 2%;
            display: flex;
            justify-content: center;
            width: auto; 
        }

        h3 {
            color: blue;
            font-size: 3rem;
            padding-bottom: 50px;

        }
    </style>
</head>
<body>
    <div class="content">
        <h1>Thank you for your visit!</h1>
        
        {% if score is not none %}
            <h2><b>Your score is: {{ score }}/6</b></h2>
            {% if incorrect_answers %}
                <div class="result-container">
                    The correct answers are:
                    {% for question, correct_answer in incorrect_answers.items() %}
                        <br>🐾Question {{ question[-1] }}: correct answer is "{{ correct_answer.upper() }}".
                    {% endfor %}
                </div>                 
            {% else %}
                <h3>Congratulations, all your answers are correct!</h3>
            {% endif %}
        {% endif %}
    </div>
</body>
</html>''', name=name, score=score, incorrect_answers=incorrect_answers)


@app.route('/Animation')
def Animation():
    return render_template('animation.html')


@app.route('/Conservation')
def Conservation():
    return render_template('Conservation.html')


if __name__ == '__main__':
    app.run(debug=True)
