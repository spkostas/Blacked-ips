{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "intimate-jungle",
   "metadata": {},
   "outputs": [],
   "source": [
    "import IP2Location\n",
    "import csv,json\n",
    "import pathlib\n",
    "import requests\n",
    "from urllib.request import urlopen\n",
    "import pandas as pd\n",
    "from git import Repo\n",
    "import os\n",
    "import sqlite3\n",
    "r = Repo('/home/dakes/blacklisted_ipsets/')\n",
    "import re\n",
    "import datetime\n",
    "import sqlite3\n",
    "plus = \"^\\+\\d{1}\"\n",
    "minus = \"^\\-\\d{1}\"\n",
    "IP2LocObj = IP2Location.IP2Location()\n",
    "IP2LocObj.open('/home/dakes/Downloads/Jupyter_scripts/IP2LOCATION-LITE-DB5.BIN')\n",
    "ff=[] \n",
    "allo=[]\n",
    "x = datetime.datetime.now()\n",
    "#print(x.year*10000+x.month*100 + x.day)\n",
    "#print(x.year)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "higher-declaration",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "20210610\n",
      "2021\n"
     ]
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "promotional-artwork",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Fetching origin\n",
      "remote: Enumerating objects: 2615, done.\u001b[K\n",
      "remote: Counting objects: 100% (2284/2284), done.\u001b[K\n",
      "remote: Compressing objects: 100% (1010/1010), done.\u001b[K\n",
      "remote: Total 2615 (delta 1410), reused 1920 (delta 1274), pack-reused 331\u001b[K\n",
      "Receiving objects: 100% (2615/2615), 21.03 MiB | 2.46 MiB/s, done.\n",
      "Resolving deltas: 100% (1440/1440), completed with 45 local objects.\n",
      "From https://github.com/firehol/blocklist-ipsets\n",
      " + f28afc4...fc266f7 master     -> origin/master  (forced update)\n",
      " + 103847d...18ed3ea gh-pages   -> origin/gh-pages  (forced update)\n"
     ]
    }
   ],
   "source": [
    "#daily fetch\n",
    "!git fetch --all"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "refined-sunglasses",
   "metadata": {},
   "outputs": [],
   "source": [
    "fnames=[]\n",
    "for path in pathlib.Path(\"/home/dakes/blacklisted_ipsets\").iterdir():\n",
    "    if str(path).endswith('.netset') or str(path).endswith('.ipset'):\n",
    "        df = pd.read_csv(path,sep=\";ofi\",index_col=False,engine='python')\n",
    "        for line in df.iterrows():\n",
    "                if \"# Category\" in line[1][0] :\n",
    "                            if \"malware\" not in line[1][0] and \"spam\" not in line[1][0] and \"attacks\" not in line[1][0]:  \n",
    "                                break\n",
    "                            else:\n",
    "                                fnames.append(str(path).replace(\"/home/dakes/blacklisted_ipsets/\",\"\"))\n",
    "#print((fnames))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "empirical-differential",
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "177\n",
      "0\n"
     ]
    }
   ],
   "source": [
    "        with open(\"/home/dakes/description.json\",'r') as jsf:\n",
    "            descr = json.load(jsf,strict = False)\n",
    "        files=[]\n",
    "        removed=[]\n",
    "    #with open('blacklisted_ipsets.csv', 'a', newline='') as csvfile:\n",
    "        #spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)\n",
    "        #spamwriter.writerow(['Name','Maintainer','Maintainer URL','Tracker List Url','Source File Date','File Update','Last update','IPs'])#+x.month*100 + x.day)\n",
    "        for path in pathlib.Path(\"/home/dakes/blacklisted_ipsets\").iterdir():\n",
    "            if str(path).endswith('.netset') or str(path).endswith('.ipset'):\n",
    "                diff_cut=[]\n",
    "                df = pd.read_csv(path,sep=\";ofi\",index_col=False,engine='python')\n",
    "                for line in df.iterrows():\n",
    "                        if \"# Category\" in line[1][0] :\n",
    "                            if \"malware\" not in line[1][0] and \"spam\" not in line[1][0] and \"attacks\" not in line[1][0]:  \n",
    "                                break\n",
    "                            else:\n",
    "                                category = line[1][0].replace(\"# Category      : \",\"\")\n",
    "                        if \"# Maintainer      :\" in line[1][0]:\n",
    "                            maintainer = line[1][0].replace(\"# Maintainer      : \",\"\")\n",
    "                        if \"# Maintainer URL  :\" in line[1][0]:\n",
    "                            maintainerURL = line[1][0].replace(\"# Maintainer URL  : \",\"\")\n",
    "                        if \"# List source URL :\" in line[1][0]:\n",
    "                            listSourceUrl = line[1][0].replace(\"# List source URL : \",\"\")\n",
    "                        if \"# Source File Date:\" in line[1][0]:\n",
    "                            sourceFileDate = line[1][0].replace(\"# Source File Date: \",\"\")\n",
    "                        if \"# This File Date  :\" in line[1][0]:\n",
    "                            recentFileUpdate = line[1][0].replace(\"# This File Date  : \",\"\")\n",
    "                            name = str(path).replace('/home/dakes/blacklisted_ipsets/','')\n",
    "                            diff = r.git.diff(\"@{upstream}\",name)\n",
    "                            source = str(path)\n",
    "                            des = source.replace(\"/home/dakes/blacklisted_ipsets/\",\"\")\n",
    "                            des = des.replace('.ipset',\"\")\n",
    "                            des = des.replace('.netset',\"\")\n",
    "                            for line in diff.splitlines():\n",
    "                                if re.findall(plus,line): #create today's list\n",
    "                                    line = line.split('/',1)[0]\n",
    "                                    line = \".\".join(line.split('.')[0:-1])\n",
    "                                    line = line +'.1'     \n",
    "                                    diff_cut.append(line.replace('+',\"\"))\n",
    "                                #elif re.findall(minus,line): #removes last day of the week and (-) of other days\n",
    "                                    #diff_cut.append(line.replace('+',\"\"))\n",
    "                                    #diff_cut.append(line.replace('-',\"\"))\n",
    "                                    #diff_cut.append(line)\n",
    "                                    #for element in data:\n",
    "                                    #    if datetime.datetime.now() - element['properties']['datetime'] > 7:\n",
    "                                    #        element.pop()\n",
    "                                    #    if element['properties']['ip']== line:\n",
    "                                    #        element.pop()\n",
    "                                    #diff_cut.append(line.replace('-',\"\"))\n",
    "                                    \n",
    "                            #spamwriter.writerow([name.replace('/home/dakes/blacklisted_ipsets/',''),maintainer,maintainerURL,listSourceUrl,sourceFileDate,recentFileUpdate,(x.month*100+x.day),','.join(diff_cut)])\n",
    "                            files.append((name,maintainer,maintainerURL,listSourceUrl,sourceFileDate,recentFileUpdate,diff_cut,descr[des]))                    \n",
    "                            break\n",
    "print(len(files))\n",
    "print(len(removed))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "sixth-underwear",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "'def create_connection(db_file):\\n    \"\"\" create a database connection to the SQLite database\\n        specified by db_file\\n    :param db_file: database file\\n    :return: Connection object or None\\n    \"\"\"\\n    conn = None\\n    try:\\n        conn = sqlite3.connect(db_file)\\n        return conn\\n    except Error as e:\\n        print(e)\\n\\n    return conn\\n\\n\\ndef create_table(conn, create_table_sql):\\n    \"\"\" create a table from the create_table_sql statement\\n    :param conn: Connection object\\n    :param create_table_sql: a CREATE TABLE statement\\n    :return:\\n    \"\"\"\\n    try:\\n        c = conn.cursor()\\n        c.execute(create_table_sql)\\n    except Error as e:\\n        print(e)\\n'"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "'''def create_connection(db_file):\n",
    "    \"\"\" create a database connection to the SQLite database\n",
    "        specified by db_file\n",
    "    :param db_file: database file\n",
    "    :return: Connection object or None\n",
    "    \"\"\"\n",
    "    conn = None\n",
    "    try:\n",
    "        conn = sqlite3.connect(db_file)\n",
    "        return conn\n",
    "    except Error as e:\n",
    "        print(e)\n",
    "\n",
    "    return conn\n",
    "\n",
    "\n",
    "def create_table(conn, create_table_sql):\n",
    "    \"\"\" create a table from the create_table_sql statement\n",
    "    :param conn: Connection object\n",
    "    :param create_table_sql: a CREATE TABLE statement\n",
    "    :return:\n",
    "    \"\"\"\n",
    "    try:\n",
    "        c = conn.cursor()\n",
    "        c.execute(create_table_sql)\n",
    "    except Error as e:\n",
    "        print(e)\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "several-engineer",
   "metadata": {},
   "outputs": [],
   "source": [
    "#after fetching and storing re-init repo to original state\n",
    "!git reset --hard origin/master\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "naked-determination",
   "metadata": {},
   "outputs": [],
   "source": [
    "'''\n",
    "database = r\"SQLite_Python.db\"\n",
    "\n",
    "sql_create_projects_table = \"\"\" CREATE TABLE IF NOT EXISTS ipsets (\n",
    "                                        id integer PRIMARY KEY,\n",
    "                                        name text NOT NULL,\n",
    "                                        begin_date text,\n",
    "                                        end_date text\n",
    "                                    ); \"\"\"\n",
    "conn = create_connection(database)\n",
    "\n",
    "# create tables\n",
    "if conn is not None:\n",
    "    create_table(conn, sql_create_projects_table)\n",
    "\n",
    "sqliteConnection = sqlite3.connect('SQLite_Python.db',\n",
    "                                           detect_types=sqlite3.PARSE_DECLTYPES |\n",
    "                                                        sqlite3.PARSE_COLNAMES)\n",
    "cursor = sqliteConnection.cursor()\n",
    "x = datetime.datetime.now()\n",
    "print(x.year*10000+x.month*100 + x.day)\n",
    "print(x.year)\n",
    "#cursor.execute(\"INSERT INTO ips VALUES (?,?,?,?,?)\",(x,'192.168.1.1',\"zeus.ipset\",\"ipblock\",\"https://github.com\"))\n",
    "#sqliteConnection.commit()\n",
    "for row in cursor.execute('SELECT * FROM projects'):\n",
    "    print(row)\n",
    "\n",
    "cursor.close()\n",
    "except sqlite3.Error as error:\n",
    "    print(\"Error while working with SQLite\", error)\n",
    "finally:\n",
    "    if (sqliteConnection):\n",
    "        sqliteConnection.close()\n",
    "        print(\"sqlite connection is closed\")\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "precious-retirement",
   "metadata": {},
   "outputs": [],
   "source": [
    "features=[]\n",
    "for i in files:\n",
    "\n",
    "    if not i[6] or i[6]=='127.0.0.1' or i[6]=='192.168.1.1':\n",
    "        continue\n",
    "    else:\n",
    "        for ip in i[6]:\n",
    "            rec =  IP2LocObj.get_all(ip)\n",
    "            #print(\".\".join(ip.split('.')[0:-1])+'.*')\n",
    "            features.append(({\n",
    "                                  \"type\": \"Feature\",\n",
    "                                  \"properties\": {\n",
    "                                    \"location\": rec.city,\n",
    "                                    \"source\":\"https://github.com/firehol/blocklist-ipsets/blob/master/\"+i[0].replace('/home/dakes/blacklisted_ipsets/',''),\n",
    "                                    \"ip\": \".\".join(rec.ip.split('.')[0:-1])+'.*',\n",
    "                                    \"maintainer\":i[1],\n",
    "                                    \"category\" : \"malware\",\n",
    "                                    \"description\": i[7],\n",
    "                                    \"alt1\": \"extreme-ip-lookup.com/\"+rec.ip,\n",
    "                                    \"alt2\":\"talosintelligence.com/reputation_center/lookup?search=\"+rec.ip\n",
    "                                    #\"0datetime\":i[7]\n",
    "                                  },\n",
    "                                  \"geometry\": {\n",
    "                                    \"type\": \"Point\",\n",
    "                                    \"coordinates\": [float(rec.longitude), float(rec.latitude)]\n",
    "                                  }\n",
    "                                }))\n",
    "len(features)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "upper-gospel",
   "metadata": {},
   "outputs": [],
   "source": [
    "with open(\"cut2_7.json\",\"w\") as f: #edit your  path\n",
    "    json.dump(features,f,indent=4) \n",
    "f.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "hydraulic-sphere",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "disabled-karen",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Connected to SQLite\n",
      "Error while working with SQLite table new_developers already exists\n",
      "sqlite connection is closed\n"
     ]
    }
   ],
   "source": [
    "'''import datetime\n",
    "import sqlite3\n",
    "\n",
    "def addDeveloper(id, name, joiningDate):\n",
    "    try:\n",
    "        sqliteConnection = sqlite3.connect('SQLite_Python.db',\n",
    "                                           detect_types=sqlite3.PARSE_DECLTYPES |\n",
    "                                                        sqlite3.PARSE_COLNAMES)\n",
    "        cursor = sqliteConnection.cursor()\n",
    "        print(\"Connected to SQLite\")\n",
    "\n",
    "        cursor = sqliteConnection.cursor()\n",
    "        cursor.execute(sqlite_create_table_query)\n",
    "\n",
    "        # insert developer detail\n",
    "        sqlite_insert_with_param = \"\"\"INSERT INTO 'new_developers'\n",
    "                          ('id', 'name', 'joiningDate') \n",
    "                          VALUES (?, ?, ?);\"\"\"\n",
    "\n",
    "        data_tuple = (id, name, joiningDate)\n",
    "        cursor.execute(sqlite_insert_with_param, data_tuple)\n",
    "        sqliteConnection.commit()\n",
    "        print(\"Developer added successfully \\n\")\n",
    "\n",
    "        # get developer detail\n",
    "        sqlite_select_query = \"\"\"SELECT name, joiningDate from new_developers where id = ?\"\"\"\n",
    "        cursor.execute(sqlite_select_query, (1,))\n",
    "        records = cursor.fetchall()\n",
    "\n",
    "        for row in records:\n",
    "            developer = row[0]\n",
    "            joining_Date = row[1]\n",
    "            print(developer, \" joined on\", joiningDate)\n",
    "            print(\"joining date type is\", type(joining_Date))\n",
    "\n",
    "        cursor.close()\n",
    "\n",
    "    except sqlite3.Error as error:\n",
    "        print(\"Error while working with SQLite\", error)\n",
    "    finally:\n",
    "        if (sqliteConnection):\n",
    "            sqliteConnection.close()\n",
    "            print(\"sqlite connection is closed\")\n",
    "\n",
    "addDeveloper(1, 'Kostas', datetime.datetime.now())\n",
    "'''"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "mexican-trout",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
