# from http.client import HT, HTTPResponse
import uuid
from database import *
from flask import *

admin=Blueprint('admin',__name__)



@admin.route('/admin_home')
def admin_home():
    return render_template('admin_pages/admin_home.html')


@admin.route('/admin_mng_dpt',methods=['get','post'])

def admin_mng_dpt():
    data={}
    q1="select * from department"
    data['dep']=select(q1)
    if'submit' in request.form:
        dpt_name= request.form['dname']
        contact_no = request.form['contact']
        email = request.form['email']
        q = "insert into department values(NULL,'%s','%s','%s')"%(dpt_name,contact_no,email)
        insert(q)
    return render_template('admin_pages/admin_mng_dpt.html',data=data)

@admin.route('/admin_mng_staff',methods=['get','post'])
def admin_mng_staff():
    data={}
    sv = "select * from staff"
    data['staff']=select(sv)
    if 'submit' in request.form:
        first_name = request.form['FIRSTNAME']
        last_name = request.form['LASTNAME']
        contact_no=request.form['contact']
        place = request.form['PLACE']
        gender = request.form['gender']
        image = request.files['image']
        username = request.form['username']
        password = request.form['password']
        path="static/"+str(uuid.uuid4())+image.filename
        image.save(path)
        n = "insert into login values(NULL,'%s','%s','staff')"%(username,password)
        n1=insert(n)
        m=" insert into staff values(NULL,'%s','%s','%s','%s','%s','%s','%s')"%(n1,first_name,last_name,contact_no,place,gender,path)
        insert(m)
       
    return render_template('admin_pages/admin_mng_staff.html',data=data)

@admin.route('/admin_mng_notify',methods=['get','post'])
def admin_mng_notify():
    data={}
    if 'submit' in request.form:
        title =request.form['title']
        description =request.form['description']
        date =request.form['date']
        time=request.form['time']
        a= "insert into notification values(NULL,'%s','%s','%s','%s')"%(title,date,time,description)
        insert(a)

    t="select * from notification"
    data['notify']=select(t)

    return render_template('admin_pages/admin_mng_notify.html',data=data)

@admin.route('/admin_mng_complaint',methods=['get','post'])
def admin_mng_complaint():
    data={}
    ar="SELECT * FROM `complaint`"
    data['com']=select(ar)
    if 'reply' in request.args:
        ar="SELECT * FROM `complaint`"
        data['com1']=select(ar)
    if 'submit' in request.form:
        reply=request.form['reply']
        cid=request.args['cid']
        q="update complaint set reply='%s' where complaint_id='%s'"%(reply,cid)
        update(q)

    return render_template('admin_pages/admin_mng_complaint.html',data=data)

@admin.route('/admin_mng_file',methods=['get','post'])
def admin_mng_file():
    data={}
    q = "select * from file"
    data['view']=select(q)
    if 'submit' in request.form:
        file=request.files['file']
        path='static/'+str(uuid.uuid4())+file.filename
        file.save(path)
        title=request.form['title']
        description=request.form['description']
        f="insert into file values(NULL,'%s','%s','%s')" %(path,title,description)
        insert(f)

    return render_template('admin_pages/admin_mng_file.html',data=data)

@admin.route('/admin_mng_manager',methods=['get','post'])
def admin_mng_manager():
    data={}
    q="select * from staff"
    data['staff']=select(q)
    if 'sid' in request.args:
        sid=request.args['sid']
        ar = "select * from manager where staff_id ='%s'"%(sid)
        result=select(ar)
        if result:
            return """<script>alert('is already a manager');window.location='admin_mng_manager'</script>"""
        else:
            q1="SELECT * FROM `login` INNER  JOIN `staff` USING(`login_id`) where staff_id='%s'"%(sid)
            res = select(q1)
            lidd = res[0]['login_id']
           
            g="insert into manager values(NULL,'%s')"%(sid)
            insert(g)
            
            q3 ="update login set usertype='manager' where login_id='%s'"%(lidd)
            update(q3)
            
            return """<script>alert('successfully added as manager');window.location='admin_mng_manager'</script>"""
    return render_template('admin_pages/admin_mng_manager.html',data=data)

from datetime import datetime
@admin.route('/admin_mng_work',methods=['get','post'])
def admin_mng_work():
    data={}
    q1="select * from staff"
    data['staffs']= select(q1)
    q3="SELECT * FROM `work` INNER  JOIN `staff` USING(`staff_id`) "
    data['wrk']=select(q3)
   
    if 'submit' in request.form:

         st=request.form['st']
         report=request.form['report']
         date=datetime.now().date()

         q1="insert into work values(NULL,'%s','%s','%s')"%(st,report,date)
         insert(q1)
         return """<script>alert('successfully added ');window.location='/admin_mng_work'</script>"""

    if 'action' in request.args:
         action=request.args['action']
         work_id=request.args['work_id']

    else: 
         action=None
    if action=='delete':
         q3="delete from work where work_id='%s'"%(work_id)
         res3=delete(q3)
         return """

<script>alert('successfully deleted.....');
window.location.href='/admin_mng_work'</script>
"""
    if action=='update':
              q4="select * from work where work_id='%s'"%(work_id)
              res4=select(q4)
              data['updates']=res4

    if 'update'in request.form:
        

        st=request.form['st']
        report=request.form['report']
        date=datetime.now().date()
        
       
        
        q5="update work set report='%s',staff_id='%s',date='%s'"%(report,st,date)
        res5=update(q5)  
        return """

<script>alert('successfully updated.....');
window.location.href='admin_mng_work'</script>
"""       


    
    return render_template('admin_pages/admin_mng_work.html',data=data)