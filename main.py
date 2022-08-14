from utils import load_candidates, get_candidate, get_candidates_by_name, get_candidates_by_skill
from flask import Flask, render_template

raw = "candidates.json"
file = load_candidates(raw)

app = Flask(__name__)

@app.route("/")
def all_users():
    return render_template("list.html", item=file)

@app.route("/candidate/<int:x>")
def get_one(x):
    item = get_candidate(x, file)
    if item:
        return render_template("the_one.html", item=item)
    else:
        return "Not found"

@app.route("/search/<candidate_name>")
def get_search(candidate_name):
    candi = get_candidates_by_name(candidate_name, file)
    count_name = len(candi)
    if candi:
        return render_template("search.html", item=candi, count_name=count_name)
    else:
        return "Not found"

@app.route("/skill/<skill_name>")
def get_skill(skill_name):
    skill = get_candidates_by_skill(skill_name, file)
    count_skill = len(skill)
    if skill:
        return render_template("skill.html", item=skill, count_skill=count_skill)
    else:
        return "Not found"

if __name__ == '__main__':
    app.run(port=5000)