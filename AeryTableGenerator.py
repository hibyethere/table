import os
import sqlite3
import sys

import requests

table_data = requests.get('https://asumatoki.kr/table/aery/data.json')
input_json = table_data.json()

level_1 = [x for x in input_json if x['folder'] == 'LEVEL 1']
level_2 = [x for x in input_json if x['folder'] == 'LEVEL 2']
level_3 = [x for x in input_json if x['folder'] == 'LEVEL 3']
level_4 = [x for x in input_json if x['folder'] == 'LEVEL 4']
level_5 = [x for x in input_json if x['folder'] == 'LEVEL 5']
level_6 = [x for x in input_json if x['folder'] == 'LEVEL 6']
level_7 = [x for x in input_json if x['folder'] == 'LEVEL 7']
level_8 = [x for x in input_json if x['folder'] == 'LEVEL 8']
level_9 = [x for x in input_json if x['folder'] == 'LEVEL 9']
level_10 = [x for x in input_json if x['folder'] == 'LEVEL 10']
level_11 = [x for x in input_json if x['folder'] == 'LEVEL 11']
level_12 = [x for x in input_json if x['folder'] == 'LEVEL 12']
level_13 = [x for x in input_json if x['folder'] == 'LEVEL 13']
level_14 = [x for x in input_json if x['folder'] == 'LEVEL 14']
level_15 = [x for x in input_json if x['folder'] == 'LEVEL 15']
level_16 = [x for x in input_json if x['folder'] == 'LEVEL 16']
level_17 = [x for x in input_json if x['folder'] == 'LEVEL 17']
level_18 = [x for x in input_json if x['folder'] == 'LEVEL 18']
level_19 = [x for x in input_json if x['folder'] == 'LEVEL 19']
level_20 = [x for x in input_json if x['folder'] == 'LEVEL 20']
level_20_ = [x for x in input_json if x['folder'] == 'LEVEL 20+']
level_dummy = [x for x in input_json if x['folder'] == 'LEVEL DUMMY']
level_old = [x for x in input_json if x['folder'] == 'OLD CHARTS']

db_path = ''
if getattr(sys, 'frozen', False):
    db_path = os.path.dirname(os.path.abspath(sys.executable)) + '\LR2files\Database\song.db'
else:
    db_path = os.path.dirname(os.path.abspath(__file__)) + '\LR2files\Database\song.db'

print(db_path)
conn = sqlite3.connect(db_path)
cur = conn.cursor()

try:
    conn.execute('DROP TABLE Aery')
except:
    pass

try:
    conn.execute('CREATE TABLE Aery(md5 TEXT, folder TEXT, level TEXT)')
except:
    pass

for e in level_1:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_2:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_3:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_4:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_5:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_6:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_7:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_8:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_9:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_10:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_11:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_12:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_13:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_14:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_15:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_16:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_17:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_18:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_19:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_20:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_20_:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_dummy:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
for e in level_old:
    cur.executemany('INSERT INTO Aery VALUES (?, ?, ?)',
                    [(e['md5'], e['folder'], e['level'])])
    
conn.commit()
conn.close()

header_data = requests.get('https://asumatoki.kr/table/aery/header.json')
last_update = header_data.json()['last_update']

table_folder = 'AeryTable'
isExist = os.path.exists(table_folder)
if not isExist:
    os.makedirs(table_folder) 

level_list = ['1', '2', '3', '4', 
              '5', '6', '7', '8', 
              '9', '10', '11', '12', 
              '13', '14', '15', '16', 
              '17', '18', '19', '20', 
              '20+', 'DUMMY', 'OLD']

for level in level_list:
    if level == 'DUMMY':
        lr2folder = [f"#COMMAND song.hash   in (SELECT md5 FROM Aery WHERE folder = 'LEVEL DUMMY') \n", "#MAXTRACKS 0\n", "#CATEGORY [5KEYS AERY]\n", f"#TITLE LEVEL DUMMY\n", f"#INFORMATION_A LAST UPDATE: {last_update}\n", "#INFORMATION_B\n"]
        f = open(table_folder + f'/0022.lr2folder', 'w')

    elif level == 'OLD':
        lr2folder = [f"#COMMAND song.hash   in (SELECT md5 FROM Aery WHERE folder = 'OLD CHARTS') \n", "#MAXTRACKS 0\n", "#CATEGORY [5KEYS AERY]\n", f"#TITLE OLD CHARTS\n", f"#INFORMATION_A LAST UPDATE: {last_update}\n", "#INFORMATION_B\n"]
        f = open(table_folder + f'/0023.lr2folder', 'w')
        
    else:
        lr2folder = [f"#COMMAND song.hash   in (SELECT md5 FROM Aery WHERE folder = 'LEVEL {level}') \n", "#MAXTRACKS 0\n", "#CATEGORY [5KEYS AERY]\n", f"#TITLE LEVEL {level}\n", f"#INFORMATION_A LAST UPDATE: {last_update}\n", "#INFORMATION_B\n"]
        if level == '20+':
            f = open(table_folder + f'/0021.lr2folder', 'w')
        
        elif int(level) <= 9:
            f = open(table_folder + f'/000{level}.lr2folder', 'w')
            
        else:
            f = open(table_folder + f'/00{level}.lr2folder', 'w')
        
    f.writelines(lr2folder)
    f.close()