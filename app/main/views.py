from flask import render_template,redirect,url_for,abort,request
from . import main
from .forms import UpdateProfile,PitchForm,CategoryForm,CommentForm,UpvoteForm,DownvoteForm
from .. import db,photos
from ..models import User,Pitch,Category,Comment,Upvote,Downvote
from flask_login import login_required,current_user
import markdown2 

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    
   
    title = 'Home - Welcome to The best Pitches Website'
    category = Category.get_categories()
    return render_template('index.html', title = title,category = category)

@main.route('/add/category', methods=['GET','POST'])
@login_required
def new_category():
    '''
    View new group route function that returns a page with a form to create a category
    '''
    form = CategoryForm()

    if form.validate_on_submit():
        cat_name = form.name.data
        new_category = Category(cat_name=cat_name)
        new_category.save_category()

        return redirect(url_for('.index'))

    
    title = 'New category'
    return render_template('new_category.html', category_form = form,title=title)


@main.route('/category/<int:id>')
def category(id):
    category1 = Category.query.get(id)
    pitches = Pitch.query.filter_by(category=category1).all()

    
    return render_template('category.html', pitches=pitches, category=category1)
    


@main.route('/category/view_pitch/add/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
    '''
    Function to check Pitches form and fetch data from the fields
    '''                                             
    form = PitchForm()
    category = Category.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        content = form.content.data
        new_pitch= Pitch(content=content,category= category,user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id=id))


    title = 'New Pitch'
    return render_template('new_pitch.html', title = title, pitch_form = form, category = category)


@main.route('/category/view_pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def view_pitch(id):
    '''
    Function the returns a single pitch for comment to be added
    '''

    print(id)
    pitches = Pitch.query.get(id)

    if pitches is None:
        abort(404)
   
    return render_template('pitch.html', pitches=pitches,category_id=id)

@main.route('/comment/new/<int:pitch_id>', methods = ['GET','POST'])
@login_required
def new_comment(pitch_id):
    form = CommentForm()
    pitch=Pitch.query.get(pitch_id)
    if form.validate_on_submit():
        description = form.description.data

        new_comment = Comment(description = description, user_id = current_user._get_current_object().id, pitch_id = pitch_id)
        db.session.add(new_comment)
        db.session.commit()


        return redirect(url_for('.new_comment', pitch_id= pitch_id))

    all_comments = Comment.query.filter_by(pitch_id = pitch_id).all()
    return render_template('comment.html', form = form, comment = all_comments, pitch = pitch )


@main.route('/pitch/upvote/<int:pitch_id>/upvote', methods = ['GET', 'POST'])
@login_required
def upvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_upvotes = Upvote.query.filter_by(pitch_id= pitch_id)
    
    if Upvote.query.filter(Upvote.user_id==user.id,Upvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))


    new_upvote = Upvote(pitch_id=pitch_id, user = current_user)
    new_upvote.save_upvotes()
    return redirect(url_for('main.index'))

@main.route('/pitch/downvote/<int:pitch_id>/downvote', methods = ['GET', 'POST'])
@login_required
def downvote(pitch_id):
    pitch = Pitch.query.get(pitch_id)
    user = current_user
    pitch_downvotes = Downvote.query.filter_by(pitch_id= pitch_id)
    
    if Downvote.query.filter(Downvote.user_id==user.id,Downvote.pitch_id==pitch_id).first():
        return  redirect(url_for('main.index'))


    new_downvote = Downvote(pitch_id=pitch_id, user = current_user)
    new_downvote.save_downvotes()
    return redirect(url_for('main.index'))


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



@main.route('/test/<int:id>')  
def test(id):
    '''
    this is route for basic testing
    '''
    blog =blog.query.filter_by(id=1).first()
    return render_template('test.html',Blog= Blog)