from flask import Flask, url_for,render_template,request, redirect
import csv

app = Flask(__name__)



@app.route("/")
def my_home():
    return render_template('index.html')

@app.route('/<string:page_name>')
def my_index(page_name):
    return render_template(page_name)


def write_to_csv(data):
  with open('database.csv', mode = 'a') as database2:
    email   = data["email"]
    subject = data["subject"]
    message = data["message"]
    csv.writer= csv.writer(database2, delimiter='',quotechar='|', newline = '',quoting = csv.QUOTE_MINIMAL)

    csv.writer.writerow([email,subject,message])

@app.route("/submit_form", methods=["POST","GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("/thankyou.html")
    else:
        return "SOMETHING WENT WRONG. TRY AGAIN!"


#@app.route("/about.html")
#def my_about():
#    return render_template('about.html')

#@app.route("/works.html")
#def my_works():
#    return render_template('works.html')


#@app.route("/contact.html")
#def my_contact():
#    return render_template('contact.html')

#@app.route("/favicon.ico")
#def IconWebsite():
#    return render_template('sunnycastsummer.ico')