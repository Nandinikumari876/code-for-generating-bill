import mysql.connector
import datetime

# MySQL se connection
con = mysql.connector.connect(
    host="localhost",
    user="root",
    password="nannu@987",
    database="shopping"
)

cursor = con.cursor()

def shopping():
    id=int(input(" enter product id :"))
    n=str( id)
    pr_name=input(" enter product name:")
    m=str( pr_name)
    pr_price=float(input(" enter price :"))
    q=str(pr_price)
    pr_quantity=float(input(" enter quantity :"))
    b=str(pr_quantity)
    ammount=pr_price*pr_quantity
    o=str(ammount)
    sql='''insert into record 
    values(%s,%s,%s,%s,%s)'''
    values=(id,pr_name,pr_price,pr_quantity,ammount)
    cursor.execute(sql,values)
    
    print(" ✅data insert successfully")
    
    
    t=datetime.datetime.now()
    d=str(t)
    
    x=open(n+".txt","w")

    y=x.write("order id:"+n+"\nname:"+m+"\nquantity:"+q+"\namount:"+o+"\ndate_time:"+d) 
    con.commit()
    x.close()

shopping()