from datetime import datetime

class Student:
    def __init__(self, id, name, age, email, interests=None, achievements=None, courses=None):
        self.id = id
        self.name = name
        self.age = age
        self.email = email
        self.interests = interests or []
        self.achievements = achievements or []
        self.courses = courses or []
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'email': self.email,
            'interests': self.interests,
            'achievements': self.achievements,
            'courses': self.courses,
            'created_at': self.created_at,
            'updated_at': self.updated_at
        }

    def update(self, name=None, age=None, email=None, interests=None, achievements=None, courses=None):
        if name is not None:
            self.name = name
        if age is not None:
            self.age = age
        if email is not None:
            self.email = email
        if interests is not None:
            self.interests = interests
        if achievements is not None:
            self.achievements = achievements
        if courses is not None:
            self.courses = courses
        self.updated_at = datetime.now().isoformat()
