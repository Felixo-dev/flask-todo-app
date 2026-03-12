from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

# Database Configuration (Creates a file named test.db)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# The Database Model

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    # 0 = Incomplete, 1 = Completed
    status = db.Column(db.Integer, default=0) 
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Task {self.id}>'

# Route: View all tasks & Add a task
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        
        # Simple Validation: Don't add empty tasks
        if not task_content:
            return redirect('/')

        new_task = Todo(content=task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue adding your task'

    else:
        # Sort by date created (newest first)
        tasks = Todo.query.order_by(Todo.date_created.desc()).all()
        return render_template('index.html', tasks=tasks)

# Route: Delete a task
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'
    
@app.route('/done/<int:id>')
def done(id):
    task = Todo.query.get_or_404(id)
    # This toggles it: if it's 0 it becomes 1, if it's 1 it becomes 0
    task.status = 1 if task.status == 0 else 0
    
    try:
        db.session.commit()
        return redirect('/')
    except:
        return 'There was an issue updating your task'    
    
# This section ensures the database is created in a production environment
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)   