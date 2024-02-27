from flask import *
from database import *
public=Blueprint('public',__name__)


@public.route('/')
def public_home():
    return render_template('public_pages/public_home.html')

@public.route('/login',methods=['get','post'])
def logins():
    if 'submit' in request.form:
        username=request.form['username']
        password=request.form['password']
        q="select * from login where username='%s' and password='%s'"%(username,password)
        res=select(q)
        if res:
            session['lid']=res[0]['login_id']
            if res[0]['usertype']=='admin':
                return redirect(url_for('admin.admin_home'))
            elif res[0]['usertype']=='user':
                u="select * from user where login_id='%s'"%(session['lid'])
                result=select(u)
                if result:
                     session['uid']=result[0]['user_id']
                     
                     return redirect(url_for('user.user_home'))
            elif res[0]['usertype']=='manager':
                u1="SELECT * FROM  `staff`  where login_id='%s'"%(session['lid'])
                result1=select(u1)
                if result1:
                     session['mid']=result1[0]['staff_id']
                     return redirect(url_for('manager.manager_home'))
            elif res[0]['usertype']=='staff':
                u1="SELECT * FROM  `staff`  where login_id='%s'"%(session['lid'])
                result1=select(u1)
                if result1:
                     session['sid']=result1[0]['staff_id']
                     return redirect(url_for('staff.staff_home'))
    return render_template('public_pages/login.html')

