from flask import render_template,redirect,url_for,abort,request
from . import main
# from ..request import get_movies,get_movie,search_movie
from .forms import UpdateProfile
from .. import db,photos
from ..models import User 
from flask_login import login_required,current_user
import markdown2 

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    title = 'Home - Welcome to The best Pitches Website'
    return render_template('index.html', title = title)

@main.route('/category/<int:id>')
def category(id):

    '''
    View Category page function that returns the page where you add pitch
    '''
    category = get_category(id)
    cat_name = f'{category.cat_name}'
    pitch = Pitch.get_pitch(category.id)
   

    return render_template('categories.html',cat_name = cat_name,category = category,pitch = pitch)

@main.route('/category/pitch/new/<int:id>', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    form = PitchForm()
    category = get_category(id)

    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        
           # Updated pitch instance
        new_pitch = Pitch(category_id=category.id,cat_name=cat_name,category_pitch=review,user=current_user)

        # save pitch method
        new_pitch.save_pitch()
        return redirect(url_for('.category',id = category.id ))

    cat_name = f'{category.cat_name} pitch'
    return render_template('new_pitch.html',cat_name = cat_name, pitch_form=form, category=category)

@main.route('/pitch/<int:id>')
def single_pitch(id):
    pitch=Pitch.query.get(id)
    if pitch is None:
        abort(404)
    format_pitch = markdown2.markdown(pitch.category_pitch,extras=["code-friendly", "fenced-code-blocks"])
    return render_template('pitch.html',pitch = pitch,format_pitch=format_pitch)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))