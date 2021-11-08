"""
CS321
Project 3
Yixuan Qiu & Luhang Sun
"""

from flask import Flask, render_template, request, url_for, redirect
import datetime

app = Flask(__name__)

to_do_list = []
content_list = []


@app.route("/")
def index():
    now = datetime.datetime.now()
    today = datetime.date.today()
    curr_time = now.strftime("%H:%M")
    tomorrow = str(today + datetime.timedelta(days=1))
    today = str(today)

    return render_template(
        "base.html",
        title="Home",
        today=today,
        curr_time=curr_time,
        tomorrow=tomorrow,
        to_do_list=to_do_list,
        content_list=content_list,
    )


@app.route("/about")
def about():
    return "A to-do app"


@app.route("/add", methods=["POST"])
def add():
    content = request.form.get("item")
    priority = request.form.get("priority")
    tags_input = request.form.get("tags")
    due_date = request.form.get("due_date")

    now = datetime.datetime.now()
    added_time = now.strftime("%Y-%m-%d, %H:%M")

    # create item dictionary with info above
    item = {}
    item["content"] = content
    item["priority"] = priority
    item["tags"] = format_tags(tags_input)
    item["time"] = added_time
    item["due_date"] = due_date
    item["id"] = content + str(content_list.count(content))

    content_list.append(content)
    to_do_list.append(item)

    return redirect(url_for("index"))


@app.route("/remove/<string:item_id>")
def remove(item_id):
    for item in to_do_list:
        if item["id"] == item_id:
            to_do_list.remove(item)
            break
    return redirect(url_for("index"))


# join tag list to a string for display
def format_tags(tags_input):
    if tags_input is None or tags_input == "":
        tags = ""
    else:
        tag_list = tags_input.split(" ,")
        tags = "# " + " #".join(tag_list)
    return tags


if __name__ == "__main__":
    app.run(debug=True)
