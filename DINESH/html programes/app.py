from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
from datetime import datetime, timedelta
import uuid
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-change-this-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///social_media.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Ensure upload folder exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(120), nullable=False)
    full_name = db.Column(db.String(120), nullable=False)
    bio = db.Column(db.Text, default='')
    profile_picture = db.Column(db.String(200), default='default.jpg')
    is_private = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    posts = db.relationship('Post', backref='author', lazy=True)
    stories = db.relationship('Story', backref='author', lazy=True)
    comments = db.relationship('Comment', backref='author', lazy=True)
    likes = db.relationship('Like', backref='user', lazy=True)
    
    # Follow relationships
    followers = db.relationship('Follow', foreign_keys='Follow.followed_id', backref='followed', lazy=True)
    following = db.relationship('Follow', foreign_keys='Follow.follower_id', backref='follower', lazy=True)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    image = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationships
    comments = db.relationship('Comment', backref='post', lazy=True, cascade='all, delete-orphan')
    likes = db.relationship('Like', backref='post', lazy=True, cascade='all, delete-orphan')

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    image = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Like(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Follow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    follower_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    followed_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, accepted, rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Helper functions
def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'mp4', 'mov'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def save_file(file):
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], unique_filename))
        return unique_filename
    return None

def is_following(follower_id, followed_id):
    follow = Follow.query.filter_by(follower_id=follower_id, followed_id=followed_id, status='accepted').first()
    return follow is not None

def can_view_posts(viewer_id, post_user_id):
    if viewer_id == post_user_id:
        return True
    user = User.query.get(post_user_id)
    if not user.is_private:
        return True
    return is_following(viewer_id, post_user_id)

# Routes
@app.route('/')
def index():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return redirect(url_for('feed'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        full_name = request.form['full_name']
        
        # Check if user already exists
        if User.query.filter_by(username=username).first():
            flash('Username already exists!', 'error')
            return render_template('register.html')
        
        if User.query.filter_by(email=email).first():
            flash('Email already registered!', 'error')
            return render_template('register.html')
        
        # Create new user
        user = User(
            username=username,
            email=email,
            password_hash=generate_password_hash(password),
            full_name=full_name
        )
        db.session.add(user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        
        if user and check_password_hash(user.password_hash, password):
            session['user_id'] = user.id
            session['username'] = user.username
            flash('Login successful!', 'success')
            return redirect(url_for('feed'))
        else:
            flash('Invalid username or password!', 'error')
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('Logged out successfully!', 'success')
    return redirect(url_for('login'))

@app.route('/feed')
def feed():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user_id = session['user_id']
    user = User.query.get(user_id)
    
    # Get posts from users that the current user follows
    following_ids = [f.followed_id for f in user.following if f.status == 'accepted']
    following_ids.append(user_id)  # Include own posts
    
    posts = Post.query.filter(Post.user_id.in_(following_ids)).order_by(Post.created_at.desc()).all()
    
    # Get stories from followed users
    stories = Story.query.filter(Story.user_id.in_(following_ids)).filter(
        Story.created_at >= datetime.utcnow() - timedelta(hours=24)
    ).order_by(Story.created_at.desc()).all()
    
    return render_template('feed.html', posts=posts, stories=stories, user=user)

@app.route('/profile/<username>')
def profile(username):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    profile_user = User.query.filter_by(username=username).first()
    if not profile_user:
        flash('User not found!', 'error')
        return redirect(url_for('feed'))
    
    current_user = User.query.get(session['user_id'])
    
    # Get posts that the current user can view
    if can_view_posts(session['user_id'], profile_user.id):
        posts = Post.query.filter_by(user_id=profile_user.id).order_by(Post.created_at.desc()).all()
    else:
        posts = []
    
    # Check follow status
    follow_status = None
    if session['user_id'] != profile_user.id:
        follow = Follow.query.filter_by(follower_id=session['user_id'], followed_id=profile_user.id).first()
        if follow:
            follow_status = follow.status
    
    return render_template('profile.html', profile_user=profile_user, posts=posts, 
                         current_user=current_user, follow_status=follow_status)

@app.route('/create_post', methods=['POST'])
def create_post():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    content = request.form['content']
    image = request.files.get('image')
    
    if not content and not image:
        flash('Post must have content or image!', 'error')
        return redirect(url_for('feed'))
    
    image_filename = None
    if image:
        image_filename = save_file(image)
    
    post = Post(
        content=content,
        image=image_filename,
        user_id=session['user_id']
    )
    db.session.add(post)
    db.session.commit()
    
    flash('Post created successfully!', 'success')
    return redirect(url_for('feed'))

@app.route('/create_story', methods=['POST'])
def create_story():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    content = request.form.get('content', '')
    image = request.files.get('image')
    
    if not content and not image:
        flash('Story must have content or image!', 'error')
        return redirect(url_for('feed'))
    
    image_filename = None
    if image:
        image_filename = save_file(image)
    
    story = Story(
        content=content,
        image=image_filename,
        user_id=session['user_id']
    )
    db.session.add(story)
    db.session.commit()
    
    flash('Story created successfully!', 'success')
    return redirect(url_for('feed'))

@app.route('/like_post/<int:post_id>', methods=['POST'])
def like_post(post_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    
    existing_like = Like.query.filter_by(user_id=session['user_id'], post_id=post_id).first()
    
    if existing_like:
        db.session.delete(existing_like)
        db.session.commit()
        return jsonify({'liked': False})
    else:
        like = Like(user_id=session['user_id'], post_id=post_id)
        db.session.add(like)
        db.session.commit()
        return jsonify({'liked': True})

@app.route('/comment_post/<int:post_id>', methods=['POST'])
def comment_post(post_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    content = request.form['content']
    if not content:
        flash('Comment cannot be empty!', 'error')
        return redirect(url_for('feed'))
    
    comment = Comment(
        content=content,
        user_id=session['user_id'],
        post_id=post_id
    )
    db.session.add(comment)
    db.session.commit()
    
    flash('Comment added successfully!', 'success')
    return redirect(url_for('feed'))

@app.route('/follow/<int:user_id>', methods=['POST'])
def follow_user(user_id):
    if 'user_id' not in session:
        return jsonify({'error': 'Not logged in'}), 401
    
    if session['user_id'] == user_id:
        return jsonify({'error': 'Cannot follow yourself'}), 400
    
    existing_follow = Follow.query.filter_by(follower_id=session['user_id'], followed_id=user_id).first()
    
    if existing_follow:
        db.session.delete(existing_follow)
        db.session.commit()
        return jsonify({'following': False})
    else:
        user = User.query.get(user_id)
        status = 'accepted' if not user.is_private else 'pending'
        
        follow = Follow(follower_id=session['user_id'], followed_id=user_id, status=status)
        db.session.add(follow)
        db.session.commit()
        
        return jsonify({'following': True, 'status': status})

@app.route('/settings')
def settings():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    return render_template('settings.html', user=user)

@app.route('/update_profile', methods=['POST'])
def update_profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    
    user.full_name = request.form['full_name']
    user.bio = request.form['bio']
    user.is_private = 'is_private' in request.form
    
    # Handle profile picture upload
    profile_picture = request.files.get('profile_picture')
    if profile_picture:
        filename = save_file(profile_picture)
        if filename:
            user.profile_picture = filename
    
    db.session.commit()
    flash('Profile updated successfully!', 'success')
    return redirect(url_for('settings'))

@app.route('/change_password', methods=['POST'])
def change_password():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    current_password = request.form['current_password']
    new_password = request.form['new_password']
    
    if not check_password_hash(user.password_hash, current_password):
        flash('Current password is incorrect!', 'error')
        return redirect(url_for('settings'))
    
    user.password_hash = generate_password_hash(new_password)
    db.session.commit()
    flash('Password changed successfully!', 'success')
    return redirect(url_for('settings'))

@app.route('/follow_requests')
def follow_requests():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.get(session['user_id'])
    pending_requests = Follow.query.filter_by(followed_id=user.id, status='pending').all()
    
    return render_template('follow_requests.html', requests=pending_requests)

@app.route('/handle_follow_request/<int:request_id>/<action>', methods=['POST'])
def handle_follow_request(request_id, action):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    follow_request = Follow.query.get(request_id)
    if not follow_request or follow_request.followed_id != session['user_id']:
        flash('Invalid request!', 'error')
        return redirect(url_for('follow_requests'))
    
    if action == 'accept':
        follow_request.status = 'accepted'
        flash('Follow request accepted!', 'success')
    elif action == 'reject':
        follow_request.status = 'rejected'
        flash('Follow request rejected!', 'success')
    
    db.session.commit()
    return redirect(url_for('follow_requests'))

@app.route('/call/<username>')
def call(username):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    user = User.query.filter_by(username=username).first()
    if not user:
        flash('User not found!', 'error')
        return redirect(url_for('feed'))
    
    return render_template('call.html', user=user)

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True) 