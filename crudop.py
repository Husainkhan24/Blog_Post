import pymysql as p
def con():
    return p.connect(user="root",password="",host="localhost",database="db12")

def reg_auth(t):
    fc=con()
    cur=fc.cursor()
    q='insert into Author(A_uname,A_password,A_city) values(%s,%s,%s)'
    cur.execute(q,t)
    print("data inserted")
    fc.commit()
    fc.close()

def reg_user(t):
    fc=con()
    cur=fc.cursor()
    q='insert into User(U_name,U_password,U_city) values(%s,%s,%s)'
    cur.execute(q,t)
    print("data inserted")
    fc.commit()
    fc.close()

def show_auth(t):
    fc=con()
    cur=fc.cursor()
    q='select * from Author where A_uname=%s and A_password=%s'
    cur.execute(q,t)
    elist=cur.fetchall()
    fc.commit()
    fc.close()
    return elist

def show_user():
    fc=con()
    cur=fc.cursor()
    q='select * from User'
    cur.execute(q)
    elist=cur.fetchall()
    fc.commit()
    fc.close()
    return elist

def log_auth():
    fc=con()
    cur=fc.cursor()
    q='select * from Author'
    cur.execute(q)
    elist=cur.fetchall()
    return elist

def add_post(t):
    fc=con()
    cur=fc.cursor()
    q='insert into Author_post(P_uname, p_title, p_post) values(%s,%s,%s)'
    cur.execute(q)
    print("post insertde")
    fc.commit()
    fc.close()

def view_post():
    fc=con()
    cur=fc.cursor()
    q='select * from Author post'
    cur.execute(q)
    elist=cur.fetchall()
    return elist