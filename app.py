from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from helper import languages, homework_list, get_key, add_homework
from wtforms.validators import InputRequired

app = Flask(__name__, template_folder='templates')
app.config["SECRET_KEY"] = "mysecret"


class HomeworkForm(FlaskForm):
    text_field = StringField("Comment", validators=[InputRequired()])
    submit = SubmitField("Add Comment")


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/languages/<int:lang_id>', methods=["GET", "POST"])
def language(lang_id):
    lang_key = get_key(languages[lang_id])
    lang_value = languages[lang_id]
    homework_form = HomeworkForm()

    if homework_form.validate_on_submit():
        new_homework_text = homework_form.text_field.data

        add_homework(lang_value, new_homework_text)

        return redirect(url_for("homework", lang_id=lang_key))


    return render_template("language.html", template_lang=lang_value, template_id=lang_key,
                           template_form=homework_form)


@app.route('/languages/<int:lang_id>/homework')
def homework(lang_id):
    lang_name = languages[lang_id]

    return render_template("homework.html", template_lang=lang_name, template_hwork=homework_list)

if __name__ == "__main__":
    app.run(debug=True)
