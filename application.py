from flask import Flask,request
from boto.dynamodb2.table import Table
from flask import Flask,render_template
from sqlalchemy.engine.url import make_url
##from flask import Markup
import MySQLdb
import jinja2
import os
import boto
import MySQLdb as mdb
import glob
import datetime, time

import csv
from datetime import datetime
import time
#import pandas as pd
import random
#import memcache
import sys
from flask import request, jsonify


application = Flask(__name__)


def run_sql_file(filename, connection):
    start = time.time()
    file = open(filename, 'r')
    sql = s = " ".join(file.readlines())
    #print "Start executing: " + filename + " at " + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M")) + "\n" + sql
    cursor = connection.cursor()
    cursor.execute(sql)


@application.route('/back',methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def main4():
    return main_main()
    '''return render_template('query.html',
                           title='MAIN',
                           user='mj')'''

@application.route('/new_customer',methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def main123():
    user = {'nickname': 'Miguel'}  # fake user
    mj1=['MJ','Jain','PJ']
    return render_template('new_customer.html',
                           title='New Customer',
                           user=mj1)


@application.route('/sign', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def main1():
    print "mj entered"
    my_res=[]
    name=request.form['name']
    contact=request.form['contact']

    #print "fetching records from My SQL"
    #print "mj updated"
    print "name= ",name
    print "contact=",contact
    platform=os.environ['os_platform']
    print platform
    if platform=='aws':

        connection = mdb.connect(os.environ['db_host'], os.environ['db_user'], os.environ['db_password'], os.environ['db_name'])
        db = MySQLdb.connect(host=os.environ['db_host'], port=3306, db=os.environ['db_name'], user=os.environ['db_user'], passwd=os.environ['db_password'])
    elif platform=='aws-db-on-heroku':

        connection = mdb.connect(os.environ['db_host'], os.environ['db_user'], os.environ['db_password'], os.environ['db_name'])
        db = MySQLdb.connect(host=os.environ['db_host'], port=3306, db=os.environ['db_name'], user=os.environ['db_user'], passwd=os.environ['db_password'])
    
    else:
        #os_db_url=os.environ['CLEARDB_DATABASE_URL']
        print "in heroku db environment"
        url = make_url("mysql://b799d35b9d19e6:ca1bbbea@us-cdbr-iron-east-04.cleardb.net/heroku_655636584c02459?reconnect=true")
        #url = make_url(os_db_url)
        #print "url : "+url
        print url.username, url.password, url.host, url.port, url.database
        connection = mdb.connect(url.host, url.username, url.password, url.database)
        db = MySQLdb.connect(host=url.host, port=3306, db=url.database, user=url.username, passwd=url.password)
    print "calling db migration"
    for filename in glob.iglob('tables/*.sql'):
        print('/tables/%s' % filename)
        run_sql_file(filename, connection)

    #cleardburl='mysql://b799d35b9d19e6:ca1bbbea@us-cdbr-iron-east-04.cleardb.net/heroku_655636584c02459?reconnect=true'

    #print os.environment
    #db = MySQLdb.connect(host='mj1.ccunictkoaw7.us-west-2.rds.amazonaws.com', port=3306, db='mayankdb', user='mayank', passwd='mayank123')
    #db = MySQLdb.connect(host='us-cdbr-iron-east-04.cleardb.net', port=3306, db='heroku_655636584c02459', user='b799d35b9d19e6', passwd='ca1bbbea')
    #db = MySQLdb.connect(host=url.host, port=3306, db=url.database, user=url.username, passwd=url.password)
    #cursor = db.cursor()
    cursor = connection.cursor()
    cursor.execute('insert into Customer (Name,Contact_Number) values(%s,%s)',(name,contact))
    connection.commit();
    ##
    my_res = [];
    for row in cursor.fetchall():
            my_res.append(dict([('loc',row[0]),
                                 ('mag',row[1]),
                                 ('id',row[2])
                                 ]))

    return render_template('results.html',
                           title='results',
                           my_res=my_res)




@application.route('/select_queries', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def queries_1000():
    print "mj entered queries_1000"
    my_res=[]
    #name=requ
    #contaendquest.form['contact']


    #print "fetching records from My SQL"
    #print "mj updated"
    #print "name= ",name
    #print "contact=",contact
    platform=os.environ['os_platform']
    print platform
    if platform=='aws':

        connection = mdb.connect(os.environ['db_host'], os.environ['db_user'], os.environ['db_password'], os.environ['db_name'])
        db = MySQLdb.connect(host=os.environ['db_host'], port=3306, db=os.environ['db_name'], user=os.environ['db_user'], passwd=os.environ['db_password'])
    elif platform=='aws-db-on-heroku':

        connection = mdb.connect(os.environ['db_host'], os.environ['db_user'], os.environ['db_password'], os.environ['db_name'])
        db = MySQLdb.connect(host=os.environ['db_host'], port=3306, db=os.environ['db_name'], user=os.environ['db_user'], passwd=os.environ['db_password'])
    
    else:
        #os_db_url=os.environ['CLEARDB_DATABASE_URL']
        print "in heroku db environment"
        url = make_url("mysql://b799d35b9d19e6:ca1bbbea@us-cdbr-iron-east-04.cleardb.net/heroku_655636584c02459?reconnect=true")
        #url = make_url(os_db_url)
        #print "url : "+url
        print url.username, url.password, url.host, url.port, url.database
        connection = mdb.connect(url.host, url.username, url.password, url.database)
        db = MySQLdb.connect(host=url.host, port=3306, db=url.database, user=url.username, passwd=url.password)
    

    cursor = connection.cursor()
    query_res={}
   
    ##100 Queries 
    start_time = datetime.now()
    query_res['q_100_start_time']=str(start_time)
    count=1
    while count <2:
        cursor.execute("select * from   Customer where name='shraddha'")
        count=count+1
    res=cursor.fetchall()
    end_time = datetime.now()
    q_100_total_execution_time= end_time - start_time
    query_res['q_100_total_execution_time']=str(q_100_total_execution_time)
    query_res['q_100_count']=str(count)

    #print "After Queries  Result = : ", res
    query_res['res']=str(res)

    my_res=query_res
    print "my res before return ",my_res

    return jsonify(query_res)

@application.route('/insert_queries', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def insert_queries():
    print "mj entered insert_queries"
    my_res=[]
    platform=os.environ['os_platform']
    print platform
    if platform=='aws':

        connection = mdb.connect(os.environ['db_host'], os.environ['db_user'], os.environ['db_password'], os.environ['db_name'])
        db = MySQLdb.connect(host=os.environ['db_host'], port=3306, db=os.environ['db_name'], user=os.environ['db_user'], passwd=os.environ['db_password'])
    elif platform=='aws-db-on-heroku':

        connection = mdb.connect(os.environ['db_host'], os.environ['db_user'], os.environ['db_password'], os.environ['db_name'])
        db = MySQLdb.connect(host=os.environ['db_host'], port=3306, db=os.environ['db_name'], user=os.environ['db_user'], passwd=os.environ['db_password'])
    
    else:
        #os_db_url=os.environ['CLEARDB_DATABASE_URL']
        print "in heroku db environment"
        url = make_url("mysql://b799d35b9d19e6:ca1bbbea@us-cdbr-iron-east-04.cleardb.net/heroku_655636584c02459?reconnect=true")
        #url = make_url(os_db_url)
        #print "url : "+url
        print url.username, url.password, url.host, url.port, url.database
        connection = mdb.connect(url.host, url.username, url.password, url.database)
        db = MySQLdb.connect(host=url.host, port=3306, db=url.database, user=url.username, passwd=url.password)
    

    cursor = connection.cursor()
    query_res={}
   
    ##100 Queries 
    name='mayank-sj'
    contact='123456789'
    cursor.execute('insert into Customer (Name,Contact_Number) values(%s,%s)',(name,contact))
    connection.commit();
    query_res['message']='inserted';
    my_res=query_res
    print "my res before return ",my_res

    return jsonify(query_res)



@application.route('/update_query', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def update_query():
    print "mj entered update_query"
    my_res=[]
    platform=os.environ['os_platform']
    print platform
    if platform=='aws':

        connection = mdb.connect(os.environ['db_host'], os.environ['db_user'], os.environ['db_password'], os.environ['db_name'])
        db = MySQLdb.connect(host=os.environ['db_host'], port=3306, db=os.environ['db_name'], user=os.environ['db_user'], passwd=os.environ['db_password'])
    elif platform=='aws-db-on-heroku':

        connection = mdb.connect(os.environ['db_host'], os.environ['db_user'], os.environ['db_password'], os.environ['db_name'])
        db = MySQLdb.connect(host=os.environ['db_host'], port=3306, db=os.environ['db_name'], user=os.environ['db_user'], passwd=os.environ['db_password'])
    
    else:
        #os_db_url=os.environ['CLEARDB_DATABASE_URL']
        print "in heroku db environment"
        url = make_url("mysql://b799d35b9d19e6:ca1bbbea@us-cdbr-iron-east-04.cleardb.net/heroku_655636584c02459?reconnect=true")
        #url = make_url(os_db_url)
        #print "url : "+url
        print url.username, url.password, url.host, url.port, url.database
        connection = mdb.connect(url.host, url.username, url.password, url.database)
        db = MySQLdb.connect(host=url.host, port=3306, db=url.database, user=url.username, passwd=url.password)
    

    cursor = connection.cursor()
    query_res={}
   
    ##100 Queries 
    name='mayank-sj'
    contact='123456789'
    query="update Customer SET Name='Mayank' WHERE Name='Mayank'"
    #print "update query daily: ",query

    cursor.execute(query)
    #cursor.execute('insert into Customer (Name,Contact_Number) values(%s,%s)',(name,contact))
    connection.commit();
    #query_res['message']='inserted';
    query_res['message']='updated';
    my_res=query_res
    print "my res before return ",my_res

    return jsonify(query_res)



@application.route('/cartype', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def c_type():

    return render_template('Car_Type.html',
                           title='Car Type',
                           my_res="mj")


@application.route('/car', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def car_template():

    return render_template('Car.html',
                           title='Car Type',
                           my_res="mj")

@application.route('/new_car', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def car():
    print "mj entered new car"
    #my_res=[]
    operation=request.form['operation']
    print "operation ",operation

    car_model=request.form['model']
    print "model:",car_model

    car_year=request.form['year']
    print "Car Year:",car_year

    c_type=str(request.form['type'])
    print "Car type",c_type

    availablity=request.form['availablity']
    print "availablity ",availablity

    db = MySQLdb.connect(host='mj1.ccunictkoaw7.us-west-2.rds.amazonaws.com', port=3306, db='mayankdb', user='mayank', passwd='mayank123')
    cursor = db.cursor()

    if operation=='new':

        cursor.execute('insert into Car_Details (Model,Year,Type,Available) values(%s,%s,%s,%s)',(car_model,car_year,c_type,availablity))
        db.commit();

    return render_template('new_car_results.html',
                           title='results',
                           my_res=my_res)


@application.route('/daily', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def daily_rent():
    print "entered daily rent"
    return render_template('Daily_Rental.html',
                           title='Car Type',
                           my_res="mj")


@application.route('/weekly', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def daily_rent1():
    print "entered daily rent"
    return render_template('Weekly_Rental.html',
                           title='Car Type',
                           my_res="mj")


@application.route('/return', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def daily_rent2():
    print "entered daily rent"
    return render_template('Return_Car.html',
                           title='Car Type',
                           my_res="mj")

@application.route('/return_car', methods= ['GET', 'POST'])
# Configure the Jinja2 environment.
def car_type1():
    print "mj entered car type"
    my_res=[]

    cust_id=str(request.form['cust_id'])
    print "cust_id:",cust_id
    rent_id=str(request.form['rent_id'])
    print "rent_id:",rent_id
    my_res.append(rent_id)
    my_res.append(cust_id)
    booking_type=request.form['booking_type']
    print "booking_type ",booking_type


    db = MySQLdb.connect(host='mj1.ccunictkoaw7.us-west-2.rds.amazonaws.com', port=3306, db='mayankdb', user='mayank', passwd='mayank123')
    cursor = db.cursor()
    if booking_type=='daily':
        query="update Daily_Rental SET Booking_Status='Completed' WHERE Rent_Id="+rent_id+' And Cust_Id='+cust_id
        print "update query daily: ",query
        cursor.execute(query)
        db.commit()
        query="select Amount_Due from Daily_Rental where Rent_Id="+rent_id+' And Cust_Id='+cust_id
        cursor.execute(query)
        res1=cursor.fetchall()
        for row in res1:
            print "Amt Due :",row[0]
            bill=row[0]



    elif booking_type=='weekly':
        query="update Weekly_Rental SET Booking_Status='Completed' WHERE Rent_Id="+rent_id+' And Cust_Id='+cust_id
        print "update query weekly: ",query
        cursor.execute(query)
        db.commit()
        query="select Amount_Due from Weekly_Rental where Rent_Id="+rent_id+' And Cust_Id='+cust_id
        cursor.execute(query)
        res1=cursor.fetchall()
        for row in res1:
            print "Amt Due :",row[0]
            bill=row[0]

    print "Final Amount due: ",bill
    my_res.append(bill)
    my_res.append('Completed')
    print "my res: ",my_res


    return render_template('return_car_results.html',
                           title='results',
                           my_res=my_res)



@application.route('/')
# Configure the Jinja2 environment.
def main_main():
    #user = {'nickname': 'Miguel'}  # fake user
    mj1=os.environ#['CLEARDB_DATABASE_URL']

    a=''#os.environ['db_host']
    b=''#os.environ['db_port']
	#b#=os.environ['db_port']
    c=''#os.environ['db_instance']
    d=''#os.environ['db_user']
    e=''#os.environ['db_password']
    f=''#os.environ['os_platform']

    return render_template('main_file.html',
                           title='Home',
                           user=mj1,a=a,b=b,c=c,d=d,e=e,f=f)


# run the app.
if __name__ == "__main__":
    application.debug = True
    application.run(threaded=True)