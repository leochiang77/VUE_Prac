from db.mysql.base import conn_db, disconn_db
import json
import pandas as pd
from utils.utils import recordTime

tablename = "H_RAW_KPC_LOCAL_CVD"

#@recordTime
def get_cvd_daily_move(**kwargs):

    whereSql = ""
    if "stime" in kwargs : 
        whereSql+= f' and CREATE_TIME > \'{kwargs["stime"]}\''
        
    if "etime" in kwargs : 
        whereSql+= f' and CREATE_TIME < \'{kwargs["etime"]}\''

    if "unitid" in kwargs :
        whereSql+= f' and UNIT_ID = \'{kwargs["unitid"]}\''

    if whereSql:
        whereSql = " where "+whereSql[5:]

    conn, cursor= None, None
    try:
        conn, cursor = conn_db()
        sql = f'''
            SELECT CREATE_TIME,
            REPORT_TIME,
            LOT_ID,
            SHEET_ID,
            CST_ID,
            MODEL_NO,
            PLAN_RECIPE,
            ACTUAL_RECIPE,
            OPERATION_ID,
            UNIT_ID,
            LOGON_TIME,
            DC_ITEM_GROUP,
            ITEM_VALUE005,
            ITEM_VALUE006,
            UPDATE_TIME FROM {tablename} {whereSql} ORDER BY CREATE_TIME
        '''
        #print(sql)
        #df = pd.read_sql(sql, conn)
        #data = df.to_json(orient='records')
        cursor.execute(sql)
        columns = [column[0] for column in cursor.description]
        data = [dict(zip(columns, row)) for row in cursor.fetchall()]
        return data
    except Exception as e:
        raise e
    finally:
        disconn_db(conn, cursor)