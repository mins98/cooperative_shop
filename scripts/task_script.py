from xmlrpc import client
from datetime import date
url='http://localhost:8069'
db='training'
username='minsor2010@hotmail.com'
password='admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models =  client.ServerProxy("{}/xmlrpc/2/object".format(url))
model_access = models.execute_kw(db, uid, password,
                                 'cooperative_shop.task', 'check_access_rights',
                                 ['write'], {'raise_exception': False})
print(model_access)

#task = models.execute_kw(db, uid, password,'cooperative_shop.task', 'search_read',[[['state','in',['ready']]]])
#print(task)

#task = models.execute_kw(db, uid, password,'cooperative_shop.task', 'search_read',[[['state','in',['draft']]]])
#print(task)

volunter = models.execute_kw(db, uid, password,'res.partner', 'search_read',[[['id','=','8']]], {'fields': ['id','name', 'tasks_ids']})
volunter  =volunter[0]
actualDate= date.today()
xmlrpc_dob = actualDate.strftime("%Y%m%dT%H:%M:%S")
tasks = models.execute_kw(db, uid, password,'cooperative_shop.task', 'search_read',[[['state','!=','draft'],['start_time','>=',xmlrpc_dob]]], {'fields': ['id','name','start_time','stop_time','volunteers_ids']})


if len(tasks)>0:
    task1=tasks[0]
    if volunter['tasks_ids']==[]:
        tasks_ids=volunter['tasks_ids']
        tasks_ids.append(task1['id'])
        models.execute_kw(db, uid, password, 'res.partner', 'write', [[volunter['id']], {'tasks_ids': tasks_ids}])
        
        volunteers_ids=task1['volunteers_ids']
        volunteers_ids.append(volunter['id'])
        models.execute_kw(db, uid, password, 'cooperative_shop.task', 'write', [[task1['id']], {'volunteers_ids': volunteers_ids}])
        
        print ("Ready")
    else:
        print ("Have tasks")    
else:
    print ("No avalibre tasks")    
    
volunter = models.execute_kw(db, uid, password,'res.partner', 'search_read',[[['id','=','8']]], {'fields': ['id','name', 'tasks_ids']})                 
print(volunter)