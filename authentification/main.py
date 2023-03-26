from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Stocke les noms d'utilisateur et les mots de passe dans un dictionnaire pour cet exemple
users = {'yannis': 'mdp'}
print(users)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Récupère le nom d'utilisateur et le mot de passe saisis
        username = request.form['username']
        password = request.form['password']
        
        # Vérifie si l'utilisateur est dans la base de données et si le mot de passe correspond
        if username in users and users[username] == password:
            # Si l'utilisateur est authentifié, redirige vers la page d'accueil
            #return render_template('index.html',username=username)
            #return redirect(url_for('index'))
            return redirect('/main')
        else:
            # Sinon, affiche un message d'erreur
            return render_template('login.html', error='Mauvais nom d\'utilisateur ou mot de passe.')
    else:
        # Affiche la page de connexion
        return render_template('login.html', error=None)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Récupère le nom d'utilisateur et le mot de passe saisis
        username = request.form['username']
        password = request.form['password']
        
        # Vérifie si le nom d'utilisateur existe déjà
        if username in users:
            # Si le nom d'utilisateur existe déjà, affiche un message d'erreur
            return render_template('register.html', error='Nom d\'utilisateur déjà utilisé.')
        else:
            # Sinon, ajoute le nouvel utilisateur à la base de données et redirige vers la page de connexion
            users[username] = password
            print(users)
            return redirect(url_for('login'))
    else:
        # Affiche la page d'inscription
        return render_template('register.html', error=None)

@app.route('/index')
def index():
    # Affiche la page d'accueil
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port="8080")