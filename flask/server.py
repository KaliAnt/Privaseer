import os 
import sys
import sqlite3
import time


from flask import jsonify
from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash


app = Flask(__name__) #create app instance


app.config.update(dict(
    FLASK_DEBUG=True,
    DATABASE=os.path.join(app.root_path, 'history.db'),
    SECRET_KEY='development key',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('FLASKR_SETTINGS', silent=True)

def init_db():
    db = get_db()
    with app.open_resource('schema.sql',mode = 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()

def connect_db():
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db

@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()


# ROUTES

@app.route('/createEVNT', methods=['POST'])
def create_events():
    db = get_db()
    
    request_dict = request.get_json()
    if request_dict == None :
        print("Invalid data", sys.stderr) 
        close_db(db)
        return 'OK'

    print(request_dict, sys.stderr)  

    values = [request_dict['name'],
            request_dict['timestamp'],
            request_dict['location']
            ]

    db.execute('insert into entries (name, timestamp, location) values (?,?,?)', values)

    db.commit()
    return 'OK'

@app.route('/profiles', methods=['GET'])
def get_profiles():
<<<<<<< HEAD

    db = get_db()

    with open('../data/data-files/data.txt', "r") as f:
        name=f.readlines()
        print(name, sys.stderr) 
        
    profile={"name" : " ",
            "lastSeen" : " ",
            "location" : 1       
    }
    arr = []
    #select distinct name, timestamp, max(id) from entries
    for row in db.execute('select * from entries'):  
        if row[1] != "unknown" : 
            profile["name"] = row[1]
            profile["lastSeen"] = row[2]
            profile["location"] = 0
            arr.append(profile.copy())
        
    usr = jsonify(arr)
=======
    #with open('../data/data-files/data.txt',"r") as f:
    names = [{   'name' : 'Calina',
                    'isInside' : 0,
                    'lastSeen' : 'now' 
        },
        {   'name' : 'Emese',
                    'isInside' : 1,
                    'lastSeen' : 'now' 
        }    
    ]
    
    usr = jsonify(names)
   #  print names
>>>>>>> a95b3676f2d5cf0f2cd3301bc86e5e4320b6e3d9
    return usr

@app.route('/events', methods=['GET'])
def get_events():
    db = get_db()
    profile={"name" : " ",
            "lastSeen" : " ",
            "location" : 1       
    }
    arr = []
    for row in db.execute('select * from entries'):  
        profile["name"] = row[1]
        profile["lastSeen"] = row[2]
        profile["location"] = 0
        arr.append(profile.copy())
    usr = jsonify(arr)
    return usr

if __name__ == '__main__':
    
    try:
        if sys.argv[1] == 'init':
            print("[ INFO ] Initializing DATABASE...")
            with app.app_context():
                init_db()
        elif sys.argv[1] == 'run':
            print('[ INFO ] Running app...')
            app.run()
    except IndexError:
        print("[ ERROR ] Usage: python ./scriptname init/run")

