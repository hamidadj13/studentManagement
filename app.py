
from flask import Flask, render_template, request, redirect, url_for

from models import Student, Filiere, University

app = Flask(__name__)
university = University()  # Instance pour gérer les étudiants et filières


app = Flask(__name__)

university = University()  

current_matricule = 1000 # Valeur de départ

current_code = 100

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')


# ------ Routes pour les étudiants ------
@app.route('/students')
def list_students():
    students = university.list_students()
    return render_template('student_list.html', students=students)

@app.route('/student/add', methods=['GET', 'POST'])
def add_student():
    global current_matricule  # Utilisez la variable globale pour le matricule

    if request.method == 'POST':
        nom = request.form['nom']
        prenom = request.form['prenom']
        age = request.form['age']
        email = request.form['email']
        filiere_code = request.form['filiere']
        filiere = next((f for f in university.list_filieres() if f.code == filiere_code), None)

        # Générer un matricule automatique et incrémenter
        matricule = f"STU{current_matricule:04d}"  # Exemple : STU1000, STU1001, etc.
        current_matricule += 1  # Incrémenter le matricule

        new_student = Student(matricule, nom, prenom, age, email, filiere)
        university.add_student(new_student)
        return redirect(url_for('list_students'))

    filieres = university.list_filieres()
    return render_template('student_form.html', filieres=filieres)


@app.route('/student/edit/<matricule>', methods=['GET', 'POST'])
def edit_student(matricule):
    student = university.find_student(matricule)
    if request.method == 'POST':
        student.matricule = matricule
        student.nom = request.form['nom']
        student.prenom = request.form['prenom']
        student.age = request.form['age']
        student.email = request.form['email']
        student.filiere = next((f for f in university.list_filieres() if f.code == request.form['filiere']), None)  
        return redirect(url_for('list_students'))
    return render_template('student_form.html', student=student, filieres=university.list_filieres())



@app.route('/student/delete/<matricule>')
def delete_student(matricule):
    university.remove_student(matricule)
    return redirect(url_for('list_students'))

# ------ Routes pour les filières ------
@app.route('/filieres')
def list_filieres():
    filieres = university.list_filieres()
    return render_template('filiere_list.html', filieres=filieres)

@app.route('/filiere/add', methods=['GET', 'POST'])
def add_filiere():

    global current_code
    
    if request.method == 'POST':
        nom = request.form['nom']
        description = request.form['description']

        # Générer un code automatique et incrémenter
        code = f"MAT{current_code}"  # Exemple : MAT100, MAT101, etc.
        current_code += 1  # Incrémenter le code


        new_filiere = Filiere(code, nom, description)
        university.add_filiere(new_filiere)
        return redirect(url_for('list_filieres'))
    return render_template('filiere_form.html')

    

if __name__ == '__main__':
    app.run(debug=True)
