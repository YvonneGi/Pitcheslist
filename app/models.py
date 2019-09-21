from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    password_hash = db.Column(db.String(255))
    pass_secure = db.Column(db.String(255))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pitches = db.relationship('Pitch',backref = 'user',lazy="dynamic")
    comments = db.relationship('Comment', backref = 'user', lazy = "dynamic")
    
    
    def __repr__(self):
      return f'User {self.username}'

    
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

        
class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer,primary_key = True)
    cat_name = db.Column(db.String(255))
    pitches = db.relationship('Pitch',backref = 'category',lazy="dynamic")
    
    @classmethod
    def get_categories(cls):
        
        categories = Category.query.all()
        return categories 

    def save_category(self):
        db.session.add(self)
        db.session.commit() 
    

class Pitch(db.Model):
    __tablename__ = 'pitches'

    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    category_id = db.Column(db.Integer,db.ForeignKey('category.id'))
    pitch = db.Column(db.String(255))
    content = db.Column(db.String(255))
    comments = db.relationship('Comment', backref = 'pitches', lazy = "dynamic")
    

    def save_pitch(self):
        '''
        Function that saves pitches
        '''
        db.session.add(self)
        db.session.commit()
    
    @classmethod
    def get_all_pitches(cls):
       
        return Pitch.query.all()

    @classmethod
    def get_pitches_by_category(cls,id):
        
        return Pitch.query.filter_by(category_id=id).all()

    @classmethod
    def clear_pitches(cls):
        Pitch.all_pitches.clear()
        
class Comment(db.Model):

    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key = True)
    feedback = db.Column(db.String)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    votes = db.relationship('Vote', backref = 'comments', lazy = "dynamic")

    def save_comment(self):
        '''
        Function that saves comments
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Comments.query.order_by(Comments.time_posted.desc()).filter_by(pitches_id=id).all()
        return comment

class Vote(db.Model):

    __tablename__ = 'votes'
    
    id = db.Column(db.Integer, primary_key = True)
    vote = db.Column(db.Integer)
    pitch_id = db.Column(db.Integer, db.ForeignKey('pitches.id'))
    comment_id = db.Column(db.Integer, db.ForeignKey('comments.id'))

    def save_vote(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_votes(cls,user_id,pitches_id):
        votes = Vote.query.filter_by(user_id=user_id, pitches_id=pitches_id).all()
        return votes
    