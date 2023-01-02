from flask import render_template, Blueprint, request, abort, flash, redirect, url_for
from flask_blog import db
from flask_blog.models import Post
from flask_blog.main.forms import AnnouncementForm
from flask_login import current_user, login_required

main = Blueprint("main", __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get("page", 1, type=int)
    posts = Post.query.filter((Post.announcement == None) | (Post.announcement == False)).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html", posts=posts)


@main.route("/about")
def about():
    return render_template("about.html", title="About")

@main.route("/announcements")
def announcements():
    page = request.args.get("page", 1, type=int)
    announcements = Post.query.filter(Post.announcement == True).order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('announcements.html', title="Announcements", announcements=announcements)


@main.route("/announcements/new", methods=["GET", "POST"])
@login_required
def new_announcement():
    if current_user.email != 'nickcoy615@gmail.com':
        abort(403)
    form = AnnouncementForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data, author=current_user, announcement=True)
        flash("Your Announcement has been created!", "success")
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('main.announcements'))
    return render_template("create_announcement.html", title="New Announcement", form=form, legend='New Announcement')
