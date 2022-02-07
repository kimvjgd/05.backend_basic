from flask import Flask, render_template

app = Flask(__name__)

@app.route("/template-basic")
def view_template():
	title_back = '!템플릿!'
	nums_list_back = [1, 2, 3, 4, 5]
	nums_dict_back = { 'one' : 1, 'two' : 2 }
	return render_template("template.html", title = title_back, nums_list = nums_list_back, nums_dict = nums_dict_back)

if __name__ == "__main__":
		app.run(host = "127.0.0.1", port = 5000, debug = True)