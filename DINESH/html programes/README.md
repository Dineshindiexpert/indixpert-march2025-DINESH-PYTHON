# Social Media App

A complete social media application built with Python Flask, featuring all the essential social media features like Instagram and Facebook.

## 🚀 Features

### ✅ User Authentication
- User registration and login
- Password hashing and security
- Session management
- Error handling for login/register failures

### ✅ User Profiles
- Customizable profile pictures
- Bio and personal information
- Private/public account settings
- Profile editing

### ✅ Posts & Content
- Create text and image posts
- Like and comment on posts
- Post feed with chronological ordering
- Image upload support

### ✅ Stories
- Create 24-hour disappearing stories
- Image and text story support
- Story viewer interface

### ✅ Social Features
- Follow/unfollow users
- Private accounts with follow requests
- Accept/reject follow requests
- User discovery and suggestions

### ✅ Real-time Calling
- Audio/video calling between users
- WebRTC implementation
- Screen sharing capability
- Call controls (mute, video toggle, etc.)

### ✅ Account Settings
- Profile management
- Password change
- Privacy settings
- Account deactivation options

## 🛠️ Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite (can be upgraded to PostgreSQL)
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Real-time**: WebRTC for calling
- **File Storage**: Local file system
- **Deployment**: Render.com (free tier)

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

### Local Setup

1. **Clone or download the project**
   ```bash
   # If you have the files locally, navigate to the project directory
   cd your-project-directory
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   python app.py
   ```

4. **Access the app**
   - Open your browser and go to: `http://localhost:5000`
   - You'll see the login page

## 🚀 Deployment on Render (Free)

### Step 1: Prepare for Deployment

1. **Create a `render.yaml` file** (optional but recommended):
   ```yaml
   services:
     - type: web
       name: social-media-app
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: gunicorn app:app
       plan: free
   ```

2. **Ensure your `requirements.txt` is up to date** (already included)

### Step 2: Deploy on Render

1. **Sign up for Render** (free at render.com)

2. **Create a new Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository or upload files

3. **Configure the service**
   - **Name**: `social-media-app` (or any name you prefer)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free

4. **Deploy**
   - Click "Create Web Service"
   - Render will automatically build and deploy your app
   - Your app will be available at: `https://your-app-name.onrender.com`

### Step 3: Environment Variables (Optional)

For production, you should set these environment variables in Render:
- `SECRET_KEY`: A secure random string for session encryption
- `DATABASE_URL`: If using PostgreSQL instead of SQLite

## 📱 How to Use

### 1. Registration
- Visit the app and click "Register"
- Fill in your details (username, email, full name, password)
- Click "Register" to create your account

### 2. Login
- Enter your username and password
- Click "Login" to access your account

### 3. Create Posts
- On the feed page, write your post in the text area
- Optionally upload an image
- Click "Post" to share

### 4. Create Stories
- Click "Create Story" section
- Add text and/or image
- Click "Add to Story" (stories disappear after 24 hours)

### 5. Follow Users
- Visit user profiles
- Click "Follow" to follow them
- For private accounts, your request will be pending until approved

### 6. Make Calls
- Click the "Call" button on any user's post or profile
- Allow camera/microphone access
- Use call controls (mute, video, end call)

### 7. Manage Settings
- Go to Settings from the navigation menu
- Edit your profile, change password, manage privacy

## 🔧 Customization

### Adding Features
- **New post types**: Modify the `Post` model in `app.py`
- **Additional user fields**: Add columns to the `User` model
- **New social features**: Create new routes and templates

### Styling
- Edit CSS in `templates/base.html`
- Modify Bootstrap classes for different looks
- Add custom CSS files in `static/` directory

### Database
- **SQLite**: Good for development and small apps
- **PostgreSQL**: Better for production (update `DATABASE_URL` in Render)

## 🐛 Troubleshooting

### Common Issues

1. **"Module not found" errors**
   - Make sure you've installed requirements: `pip install -r requirements.txt`

2. **Database errors**
   - Delete `social_media.db` file and restart the app (database will be recreated)

3. **Image upload issues**
   - Ensure `static/uploads/` directory exists
   - Check file permissions

4. **Calling not working**
   - Ensure HTTPS is enabled (required for WebRTC)
   - Allow camera/microphone access in browser

5. **Deployment issues on Render**
   - Check build logs in Render dashboard
   - Ensure `gunicorn` is in requirements.txt
   - Verify start command is correct

### Getting Help
- Check the console for error messages
- Review Flask debug output
- Check Render deployment logs

## 🔒 Security Features

- Password hashing with Werkzeug
- Session management
- File upload validation
- SQL injection protection (SQLAlchemy)
- XSS protection (Flask templates)

## 📈 Performance

- **Lightweight**: Minimal dependencies
- **Scalable**: Can be upgraded to PostgreSQL
- **Fast**: SQLite for development, optimized queries
- **Responsive**: Bootstrap 5 for mobile-friendly design

## 🎯 Future Enhancements

- **Real-time messaging**: WebSocket implementation
- **Push notifications**: Browser notifications
- **Advanced search**: User and post search
- **Post categories**: Different types of content
- **Analytics**: User engagement metrics
- **Mobile app**: React Native or Flutter

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Feel free to fork this project and add your own features!

---

**Enjoy your social media app! 🎉** 