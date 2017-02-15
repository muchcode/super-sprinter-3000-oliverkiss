from connect import ConnectDatabase
from models import Story
from flask import Flask, request, redirect, url_for, render_template


app = Flask(__name__)


def init_db():
    ConnectDatabase.db.connect()
    ConnectDatabase.db.create_tables([Story], safe=True)


@app.route('/', methods=['GET'])
@app.route('/list', methods=['GET'])
def show_stories():
    stories = Story.select()
    return render_template('list.html', stories=stories)


@app.route('/form', methods=['GET'])
def display_add_story_form():
    story = []
    return render_template('form.html', us_story=story, header="Add new Story", button="Create")


@app.route('/story/', methods=['POST'])
def add_story():
    new_story = Story.create(story_title=request.form['story_title'],
                             user_story=request.form['user_story'],
                             acceptance_criteria=request.form['acceptance_criteria'],
                             business_value=request.form['business_value'],
                             estimation=request.form['estimation'],
                             status=request.form['status'])
    return redirect(url_for('show_stories'))


@app.route('/story/<story_id>', methods=['GET', 'POST'])
def edit_story(story_id):
    if request.method == 'GET':
        story = Story.get(Story.id == story_id)
        return render_template('form.html', us_story=story, header="Edit Story", button="Update")
    else:
        edit_story = Story.update(story_title=request.form['story_title'],
                                  user_story=request.form['user_story'],
                                  acceptance_criteria=request.form['acceptance_criteria'],
                                  business_value=request.form['business_value'],
                                  estimation=request.form['estimation'],
                                  status=request.form['status']).where(Story.id == story_id)
        edit_story.execute()
        return redirect(url_for('show_stories'))



@app.route('/delete/<story_id>', methods=['GET'])
def delete_story(story_id):
    delete_story = Story.select().where(Story.id == story_id).get()
    delete_story.delete_instance()
    delete_story.save()
    return redirect(url_for('show_stories'))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)