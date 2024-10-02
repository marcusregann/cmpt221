"""professor.py: create a table named professors in the marist database"""
from db.db import db

class Professor(db.Model):
lab-3
    __tablename__ = 'professors'
    professor_id = db.Column(db.Integer,primary_key=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    email = db.Column(db.String(40))
    # create relationship with courses table. assoc table name = professor_course
    course = db.relationship('courses', secondary = 'professor_course', back_populates = 'professors')
    def __init__(self, first_name):
        self.first_name=first_name

    __tablename__ = 'Professors'
    ProfessorID = db.Column(db.Integer,primary_key=True, autoincrement=True)

    # create relationship with courses table. assoc table name = ProfessorCourse
    course = db.relationship('Courses', secondary = 'ProfessorCourse', back_populates = 'Professors')
    def __init__(self):
main
        # remove pass and then initialize attributes

    def __repr__(self):
        # add text to the f-string
        return f"""
                PROFESSOR NAME: {self.first_name}
                PROFESSOR LAST NAME:{self.last_name}
                PROFESSOR EMAIL:{self.email}
        """
    
    def __repr__(self):
        return self.__repr__()