# from http.client import HT, HTTPResponse
import uuid
from database import *
from flask import *
import datetime

manager=Blueprint('manager',__name__)

@manager.route('/manager_home')
def manager_home():
    return render_template('manager_pages/manager_home.html')

@manager.route('/upload_file',methods=['get','post'])

def upload_file():
    data={}
    q1="select * from upload_file"
    data['upload_file']=select(q1)

    if 'submit' in request.form:
        file1= request.files['filess']
        title = request.form['title']
        description= request.form['description']
        path="static/"+str(uuid.uuid4())+file1.filename
        file1.save(path)
        q = "insert into upload_file values(NULL,'%s','%s','%s')"%(path,title,description)
        insert(q)
        return """

<script>alert('successfully Added.....');
window.location.href='upload_file'</script>
"""
    return render_template('manager_pages/upload_files.html',data=data)



@manager.route('/mngr_view_works',methods=['get','post'])

def mngr_view_works():
    data={}
    q1="SELECT * FROM `manager` INNER  JOIN `work` USING(`staff_id`) where staff_id='%s'"%(session['mid'])
    res=select(q1)
    data['view']=res
    return render_template('manager_pages/mngr_view_works.html',data=data)


@manager.route('/mngr_view_noti',methods=['get','post'])

def mngr_view_noti():
    data={}
    q1="select * from notification"
    res=select(q1)
    data['view']=res
    return render_template('manager_pages/mngr_view_noti.html',data=data)



@manager.route('/mngr_sent_cmplt',methods=['get','post'])

def mngr_sent_cmplt():
    
    date1=datetime.datetime.now()
    date_only=date1.date()
    time_only=date1.time()
    data={}
    q1="select * from complaint where staff_id='%s'"%(session['mid'])
    data['cmp']=select(q1)

    if 'submit' in request.form:
        cmplt= request.form['cmplt']
      
       
        q = "insert into complaint values(NULL,'%s','%s','%s','%s','%s')"%('pending',cmplt,date_only,'pending',session['mid'])
        insert(q)
        print()
        return """

<script>alert('successfully Sent.....');
window.location.href='mngr_sent_cmplt'</script>
"""
    return render_template('manager_pages/mngr_sent_cmplt.html',data=data)





@manager.route('/mngr_mange_tsk',methods=['get','post'])

def mngr_mange_tsk():
    
    
    date1=datetime.datetime.now()
    date_only=date1.date()
    time_only=date1.time()
    data={}
    q1="select * from task where manager_id='%s'"%(session['mid'])
    data['task']=select(q1)

    if 'submit' in request.form:
        tasks= request.form['task']
       
        q = "insert into task values(NULL,'%s','%s')"%(tasks,session['mid'])
        insert(q)
        print()
        return """

<script>alert('successfully Added.....');
window.location.href='mngr_mange_tsk'</script>
"""
    return render_template('manager_pages/mngr_mange_tsk.html',data=data)







@manager.route('/assign_task',methods=['get','post'])

def assign_task():
    task_id=request.args['task_id']

    
    date1=datetime.datetime.now()
    date_only=date1.date()
    time_only=date1.time()
    data={}
    q1="select * from staff "
    data['staff']=select(q1)

    if 'submit' in request.form:
        staff= request.form['staff']
       
        q = "insert into task_assign values(NULL,'%s','%s','%s','%s')"%(staff,date_only,'pending',task_id)
        insert(q)
        print()
        return """

<script>alert('successfully Added.....');
window.location.href='mngr_mange_tsk'</script>
"""
    return render_template('manager_pages/assign_task.html',data=data)







@manager.route('/mngr_view_report',methods=['get','post'])

def mngr_view_report():
    data={}
    q1="SELECT * FROM `task_assign` INNER  JOIN `staff` USING(`staff_id`) INNER  JOIN `task` USING(`task_id`) where manager_id='%s'"%(session['mid'])
    res=select(q1)
    data['view']=res
    return render_template('manager_pages/mngr_view_report.html',data=data)