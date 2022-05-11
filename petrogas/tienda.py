from config import *

def getClientesSimple():
    conn, cur = get_connection()
    cur.execute('select * from clientes')
    rows = cur.fetchall()
    for row in rows:
        print(row[0], row[1], row[2], row[3], row[4])

    cur.close()
    conn.close()

def getClientesSProcedure():
    conn = None
    try:
        conn, cur = get_connection()
        cur.callproc('get_cliente_by_ruc', ('1298765477',))
        # procesar el result set
        row = cur.fetchone()
        while row is not None:
            print(row)
            row = cur.fetchone()
        # cerrar la comunicacion con el servidor de PostgreSQL
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def InsertCliente(id,ruc,razonsocial,nombre,direccion):
    conn = None
    try:
        conn, cur = get_connection()
        cur.callproc('SP_CLIENTE_INS', (id,ruc,razonsocial,nombre,direccion))
        # commit the transaction
        conn.commit()
        # close the cursor
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

def UpdateCliente():
    pass

#InsertCliente('12','1890786500','TU TIENDA.COM','JUAN PEREZ','EN TU BARRIOh');
getClientesSimple()
