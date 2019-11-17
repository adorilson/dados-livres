from datetime import datetime
from flask import render_template, flash, redirect, url_for, request, g
from flask_login import logout_user, current_user, login_user, login_required
from werkzeug.urls import url_parse
from flask_babel import _, get_locale
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from app.models import User

@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()
    g.locale = str(get_locale())
    
@app.route('/', methods=['GET', 'POST']) ## Todas as fontes de todos os usuários
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    posts = [
        {
            'autor': {'nome': 'Daniel'},
            'mensagem': 'Que dia lindo em SP!'
        },
        {
            'autor': {'nome': 'Paula'},
            'mensagem': 'O filme dos Vingadore foi ótimo!'
        }
    ]
    return render_template('index.html', title=(_('Início')), posts=posts)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
	if current_user.is_authenticated:
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.username.data).first() 
		if user is None or not user.check_password(form.password.data):
			flash(_('Nome de usuário ou senha inválidos'))
			return redirect(url_for('login'))
		login_user(user, remember=form.remember_me.data)
		next_page = request.args.get('next')
		if not next_page or url_parse(next_page).netloc != '':
			next_page = url_for('index')
		return redirect(next_page)
	return render_template('login.html', title=(_('Entrar')), form=form)
    
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_('Parabéns, agora você é um usuário registrado!'))
        return redirect(url_for('login'))
    return render_template('register.html', title=(_('Registrar')), form=form)
 
@app.route('/user/<username>') ## Fontes do usuário
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = [
        {'author': user, 'body': 'Test post #1'},
        {'author': user, 'body': 'Test post #2'}
    ]
    return render_template('user.html', user=user, posts=posts) 
    
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
	form = EditProfileForm()
	if form.validate_on_submit():
		current_user.username = form.username.data
		current_user.nickname = form.nickname.data
		current_user.typeUser = form.typeUser.data
		current_user.about_me = form.about_me.data
		db.session.commit()
		flash(_('Suas alterações foram salvas.'))
		return redirect(url_for('edit_profile'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.nickname.data = current_user.nickname
		form.typeUser.data = current_user.typeUser
		form.about_me.data = current_user.about_me
	return render_template('edit_profile.html', title=(_('Editar Perfil')),
                           form=form)


