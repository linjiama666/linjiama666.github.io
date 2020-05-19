# Connect MySQL
import pymysql
import json
from urllib.parse import quote
from tqdm import tqdm as tqdm

try:
    db = pymysql.connect(
        host = "34.80.23.11",
        port=3306,
        user = "root",
        password = "gama.net",
        database = "kloud_test",
    )
    cursor=db.cursor()

    code = 1
    num = 2
    enc = {}
    while code <=5000:
        sql = f"""select behavior from behaviorMapping_cb5 limit {num}, {num+1000}"""
        cursor.execute(sql)
        behavior = list(set([x[0] for x in cursor.fetchall()]))

        for behav in tqdm(behavior,ncols=50,desc='[getCompUUID]'):
            # print(behav)
            if code <=5000:
                d = json.loads(behav)
                # print(d)
                key = "{\"element_url\":\"" + quote(d["attrUrl"], safe='~@#$&!+=;.?/') + "\",\"elementClasses\":\"" + quote(d["attrClass"], safe='~@#$&!+=;.?/') + "\",\"elementId\":\"" + quote(d["attrId"], safe='~@#$&!+=;.?/') + "\",\"elementText\":\"" + quote(d["attrText"], safe='~@#$&!+=;.?/') + "\",\"dataanalyticsID\":\"" + quote(str(d["attrDataana"]), safe='~@#$&!+=;.?/') + "\"}"
                if key not in enc:
                    enc[key] = code
                    code+=1
            else:
                break
        num+=1000
    print("idx = ",code)
    # enc = sorted(enc.items(), key=lambda d: d[1]) 
    with open('encode.json', 'w') as fp:
        json.dump(enc, fp)
except Exception as e:
    print("error")
finally:
    db.close()
    print('db closed')