class Filiere:
    """Représente une filière dans l'université."""
    def __init__(self, code, nom, description):
        self.code = code
        self.nom = nom
        self.description = description

    def __repr__(self):
        return f"Filiere({self.code}, {self.nom}, description: {self.description})"


class Student:
    """Représente un étudiant avec plusieurs attributs."""
    def __init__(self, matricule, nom, prenom, age, email, filiere: Filiere):
        self.matricule = matricule
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.email = email
        self.filiere = filiere  # Relation avec une filière

    def __repr__(self):
        return f"Student({self.matricule}, {self.nom}, {self.prenom}, {self.email})"


class University:
    """Classe pour gérer les étudiants et les filières."""
    def __init__(self):
        self.students = []
        self.filieres = []

    # Gestion des étudiants
    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, matricule):
        self.students = [s for s in self.students if s.matricule != matricule]

    def find_student(self, matricule):
        for student in self.students:
            if student.matricule == matricule:
                return student
        return None

    def list_students(self):
        return self.students

    # Gestion des filières
    def add_filiere(self, filiere):
        self.filieres.append(filiere)

    def list_filieres(self):
        return self.filieres
