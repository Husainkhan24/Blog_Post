import crudop as OP
from flask import *

app=Flask(__name__)

@app.route("/")
def main_fun():
    return render_template("home.html")

@app.route("/authreg")
def auth_reg():
    return render_template("authreg.html")

@app.route ("/authreg", methods=["post"])
def save_data():
    name=request.form["A_Uname"]
    passw=request.form["A_password"]
    city=request.form["A_city"]
    t=(name,passw,city)
    print(t)
    OP.reg_auth(t)
    print("data inserted")
    return redirect("/")

@app.route("/userreg")
def user_reg():
    return render_template("userreg.html")


@app.route("/user_reg",methods=["post"])
def data():
    name=request.form["U_Uname"]
    passw=request.form["U_password"]
    city=request.form["U_city"]
    t=(name,passw,city)
    OP.reg_user(t)
    return redirect("/")

@app.route("/logauth")
def logauth():
    return render_template("logauth.html")

@app.route("/logsave",methods=["post"])
def save_log():
    U_name=request.form["U_name"]
    uname=request.form["uname"]
    password=request.form["Password"]
    t=uname,password
    if U_name=="Author":
        elist=OP.show_auth(t)
        if elist:
            return render_template("/authint.html") 
        else:
            return redirect("/")

@app.route("/addpost")
def add_post():
    return render_template("/addpost.html")

@app.route("/add_post",methods=["post"])
def add_p():
    blogt=request.form["BLOG_TITTLE"]
    blog=request.form["BLOG"]
    t=(blogt,blog)
    OP.add_post(t)
    return render_template("/view.html")

@app.route("/view")
    view=OP.view_post()
    return render_template("/view.html",res=view)    

if __name__=="__main__":
    app.run(debug=True)