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
all_tag_list = [] # list for all the tags


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

@app.route("tagsfilter/")
def tag_filtering(tags_list):
    '''a search filter for tags that allows multi-entry searches'''
    tag_filter_helper(tags_list)
    return redirect(url_for("index"))

def tag_filter_helper(tags_list):
    '''helper function of tag filtering algorithm'''
    filter_results = [] # the list of filtered item dicts
    for item in to_do_list:
        this_item_tags = item["tags"] # this a string sperated with '#'
        for tag in tags_list:
            if tag in this_item_tags:
                filter_results.append(item)
                break # continue to the next item on to-do list if one of the current item's tags match any of the indexed tags
    return filter_results

def format_tags(tags_input):
    '''join tag list to a string for display'''
    if tags_input is None or tags_input == "":
        tags = ""
    else:
        tag_list = tags_input.split(" ,")
        all_tag_list.extend(tag_list) # add to a cumulative tags list
        tags = "# " + " #".join(tag_list)
    return tags


if __name__ == "__main__":
    app.run(debug=True)
