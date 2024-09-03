from app import app, db
from flask import render_template, redirect, url_for, flash
from models import Task
from datetime import datetime
import forms
import pytz

@app.route('/')
@app.route('/index')
def index():
    tasks = Task.query.all()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['GET', 'POST'])
def add():
    form = forms.AddTaskForm()
    if form.validate_on_submit():
        utc_now = datetime.now(pytz.utc).date()  # Get current UTC date
        t = Task(title=form.title.data, date=utc_now)
        db.session.add(t)
        db.session.commit()
        flash('Task Added to Database')
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit(task_id):
    task = Task.query.get(task_id)
    form = forms.AddTaskForm()
    if task:
        if form.validate_on_submit():
            utc_now = datetime.now(pytz.utc).date()  # Get current UTC date
            task.title = form.title.data
            task.date = utc_now  # Corrected line
            db.session.commit()
            flash('Task has been updated')
            return redirect(url_for('index'))
        form.title.data = task.title
        return render_template('edit.html', form=form, task_id=task_id)
    else:
        flash('Task not found')
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['GET', 'POST'])
def delete(task_id):
    task = Task.query.get(task_id)
    form = forms.DeleteTaskForm()
    if task:
        if form.validate_on_submit():
            db.session.delete(task)
            db.session.commit()
            flash('Task has been deleted')
            return redirect(url_for('index'))
        return render_template('delete.html', form=form, task_id=task_id, title=task.title)
    else:
        flash('Task not found')
    return redirect(url_for('index'))