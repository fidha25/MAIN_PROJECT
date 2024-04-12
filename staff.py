import os
import time
import uuid
from database import *
from flask import *

from sample import filepost,filedecrypt
path=r"C:\Users\hp\OneDrive\Desktop\proj\ezyzip (2)\ezyzip\static\\"

import datetime

staff=Blueprint('staff',__name__)

@staff.route('/staff_home')
def staff_home():
    return render_template('staff_pages/staff_home.html')



@staff.route('/staff_view_task',methods=['get','post'])

def staff_view_task():
    data={}
    q1="SELECT * FROM `task_assign` INNER JOIN `task` USING(`task_id`) where staff_id='%s'"%(session['sid'])
    res=select(q1)
    data['view']=res
    return render_template('staff_pages/staff_view_task.html',data=data)


@staff.route('/staff_view_noti',methods=['get','post'])

def staff_view_noti():
    data={}
    q1="select * from notification"
    res=select(q1)
    data['view']=res
    return render_template('staff_pages/staff_view_noti.html',data=data)



@staff.route('/staff_sent_cmplt',methods=['get','post'])

def staff_sent_cmplt():
    
    date1=datetime.datetime.now()
    date_only=date1.date()
    time_only=date1.time()
    data={}
    q1="select * from complaint where staff_id='%s'"%(session['sid'])
    data['cmp']=select(q1)

    if 'submit' in request.form:
        cmplt= request.form['cmplt']
      
       
        q = "insert into complaint values(NULL,'%s','%s','%s','%s','%s')"%('pending',cmplt,date_only,'pending',session['sid'])
        insert(q)
        print()
        return """

<script>alert('successfully Sent.....');
window.location.href='staff_sent_cmplt'</script>
"""
    return render_template('staff_pages/staff_sent_cmplt.html',data=data)



@staff.route("/upload_image",methods=['get','post'])
def upload_image():
    data={}
    qa="select * from image_upload where staff_id='%s'"%(session['sid'])
    res=select(qa)
    data['view']=res
    print(data)
    id=session['sid']

    if 'submit' in request.form:
        files = request.files["file"]
        original_filename, file_extension = os.path.splitext(files.filename)
        upload_timestamp = time.strftime("%Y%m%d-%H%M%S")
        uploaded_file_path = f"{original_filename}_{upload_timestamp}{file_extension}"
        files.save(path + uploaded_file_path)
        d=original_filename+"_"+upload_timestamp+file_extension
        r1=filepost(uploaded_file_path,id,original_filename,d)
        return redirect(url_for("staff.upload_image"))
    
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=="delete":
        q1="delete from image_upload where upload_id='%s'"%(id)
        delete(q1)
        return """

<script>alert('successfully deleted.....');
window.location.href='/upload_image'</script>
"""


    return render_template("staff_pages/upload_image.html",data=data)      


@staff.route("/share_data",methods=['get','post'])
def share_data():
    data={}
    id=request.args['id']
    qa="select * from staff where staff_id!='%s'"%(session['sid'])
    res=select(qa)
    data['view']=res

    if 'submit' in request.form:
        sid=request.form['sid']
        q1="insert into share_image values(NULL,'%s','%s')"%(id,sid)
        insert(q1)
        return """

<script>alert('successfully shared.....');
window.location.href='/upload_image'</script>
"""
    return render_template('staff_pages/share_image.html',data=data)

@staff.route("/view_shared_data")
def view_shared_data():
    data={}
    qa="select * from share_image inner join image_upload using(upload_id) where share_image.staff_id='%s'"%(session['sid'])
    res=select(qa)
    data['view']=res
    return render_template('staff_pages/view_shared_data.html',data=data)


@staff.route("/decrypt")
def decrypt():
    id = request.args['id']

    qa = "select * from image_upload where upload_id='%s'" % (id)
    print(qa)
    res = select(qa)

    img1 = res[0]['partion_1']
    img2 = res[0]['partion_2']
    img3 = res[0]['partion_3']
    img4 = res[0]['partion_4']

    # Remove leading '/' and ' enc' (with space) from image names
    imgg1 = img1.split('/')[-1].replace(' enc', '').replace('enc', '')
   
    imgg2 = img2.split('/')[-1].replace(' enc', '').replace('enc', '')
    imgg3 = img3.split('/')[-1].replace(' enc', '').replace('enc', '')
    imgg4 = img4.split('/')[-1].replace(' enc', '').replace('enc', '')

    imga1=img1.split('/')[-1]
    imga2=img2.split('/')[-1]
    imga3=img3.split('/')[-1]
    imga4=img4.split('/')[-1]
    print("imgggggg",imgg1)
    print("imgggggg",imgg2)
    print("imgggggg",imgg3)
    print("imgggggg",imgg4)
    res=filedecrypt(imgg1,imgg2,imgg3,imgg4,imga1,imga2,imga3,imga4)

    print(img1, '///////////////////////////////')
    return send_file("C:\\Users\\hp\\OneDrive\\Desktop\\proj\\ezyzip (2)\\ezyzip\\static\\CHECK\\Panorama_image.jpg",as_attachment=True)






@staff.route('/mngr_view_works',methods=['get','post'])

def mngr_view_works():
    data={}
    q1="SELECT * FROM `manager` INNER  JOIN `work` USING(`staff_id`) where staff_id='%s'"%(session['sid'])
    res=select(q1)
    data['view']=res
    return render_template('staff_pages/mngr_view_works.html',data=data)



    








@staff.route('/staff_upload_wrk_report',methods=['get','post'])

def staff_upload_wrk_report():
    data={}
    assign_id=request.args['assign_id']
    q1="select * from task_assign where assign_id='%s'"%(assign_id)
    res=select(q1)

    if 'submit' in request.form:
        report= request.files['report']
      
        path="static/work_report"+str(uuid.uuid4())+report.filename
        report.save(path)
        
        q10="update task_assign set report='%s' where assign_id='%s'"%(path,assign_id)
        update(q10)
        
       
        return """

<script>alert('successfully Added.....');
window.location.href='staff_view_task'</script>
"""
    return render_template('staff_pages/staff_upload_wrk_report.html',data=data)
