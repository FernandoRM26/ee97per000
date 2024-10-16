import sqlite3

def connSQL():
    conn = sqlite3.connect('db/ee97per000.db')
    cursor = conn.cursor()
    return conn, cursor

def ee97per001_sql(sql, parm, flag):
    conn, ee97per001 = connSQL()
    if flag == 'I': # Insert
        ee97per001.execute(sql, parm)
        conn.commit()
        conn.close()

        # Crea un nuevo integrante
        nombre = f"{parm [1]} {parm[2]} {parm[3]} {parm[4]}"
        sql = "INSERT INTO ee97per091 (NOMBRE, APODO, CARGO) VALUES (?, ?, ?);"
        ee97per091_sql(sql, (nombre, 'NULL', 'NULL'), flag)


    elif flag == 'Q':
        if parm:
            ee97per001.execute(sql,parm)
            results = ee97per001.fetchone() 
        else:
            ee97per001.execute(sql)
            results = ee97per001.fetchall() 
        conn.commit()
        conn.close()
        return results

def ee97per091_sql(sql, parm, flag):
    conn, ee97per091 = connSQL()
    if flag == 'I':
        ee97per091.execute(sql,parm)
        conn.commit()       
        conn.close()
    elif flag == 'Q':
        if parm:
            ee97per091.execute(sql,parm)
            results = ee97per091.fetchone()
        else:
            ee97per091.execute(sql)
            results = ee97per091.fetchall()
        return results
    elif flag == 'D':
        if parm:
            ee97per091.execute(sql,parm)
        else:
            pass
        conn.commit()
        conn.close()