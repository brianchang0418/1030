from flask import Flask, render_template, abort

app = Flask(__name__)

# 假資料（可想像成資料庫資料）
posts = [
    {
        "id": 1,
        "title": "我的第一篇文章",
        "author": "小明",
        "content": "這是我用 Flask 建立的第一篇部落格文章！"
    },
    {
        "id": 2,
        "title": "Flask 模板教學",
        "author": "小華",
        "content": "今天來介紹 Flask 的模板系統 Jinja2，讓你輕鬆生成動態 HTML。"
    },
    {
        "id": 3,
        "title": "Python 與 Web 開發",
        "author": "小美",
        "content": "Python 是非常適合初學者的語言，搭配 Flask 更能快速開發網站。"
    },
]

@app.route("/")
def index():
    return render_template("index.html", posts=posts)

@app.route("/post/<int:post_id>")
def post(post_id):
    post = next((p for p in posts if p["id"] == post_id), None)
    if post is None:
        abort(404)
    return render_template("post.html", post=post)

if __name__ == "__main__":
    app.run(debug=True)
