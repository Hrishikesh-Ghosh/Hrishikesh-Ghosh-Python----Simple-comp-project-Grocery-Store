#PYTHON CODE
l_or_e='''GROCERY SHOP OPTIONS-
1.	login
2.      exit
'''

options1='''CUSTOMER OPTIONS-
1.	Billing
2.	Item ﬁnd
'''

options2='''OWNER OPTIONS-
1.	Item ﬁnd
2.	Add new item
3.	update no. in stock
4.	Show stock
5.      Bills
6.      logout
'''

billing='''BILLING OPTIONS-
1.	add product to bill
2.	delete product from bill
3.	show bill
4.	total bill'''

ad_bill='''ADD PRODUCT OPTIONS-
1.	continue
2.      stop
'''

coro='''
1.owner
2.customer'''

def itemﬁnd(p):
# qw1=product()
# cur.execute(qw1) # conn.commit()
    ﬁle=open("AILES.txt","r")
    while ﬁle:
        line=ﬁle.readline()
        #print(line)
        if line == "":
            break
        #line=line[0:7] #print(line)

        qwr2="select product from {} where product='{}'".format(line,p)
        cur.execute(qwr2)
        product=cur.fetchall()
        if product==[]:
            continue
 
        #print(product)
        try:
            pro=product[0][0]
            if p==pro:
                print(p,"can be found in",line)
                break
        except:
            continue
    ﬁle.close()


#####################MAIN START
    
while True:
    print(l_or_e)
    inst1=input('instruction:')

    if inst1=='1':
        for i in range(1):
            print(coro)
            coroi=input('instruction:')
            if coroi=='1' :
                usr=input('username:')
                pasw=input('password:')
                if usr=='owner' and pasw=='password':
            #        qw='use product'
             #       cur.execute(qw)
              #      conn.commit()
                    while True:
                        print(options2)
                        inst2=input('instruction:')
                        # qw=product()
                        # cur.execute(qw) # conn.commit()
                        if inst2=='1':
                            p=input('product to ﬁnd:')
                            itemﬁnd(p)
                        if inst2=='2':
                            prod_id=int(input('product id:'))
                            prod_name=input('Product Name:')
                            prod_num=int(input('no_of_product:'))
                            prod_cost=int(input('Cost:'))
                            ail=input('Aile:')
                            qwr2="insert into {} values('{}','{}','{}','{}')".format(ail,prod_id,prod_name,prod_num,prod_cost)
                            cur.execute(qwr2)
                            conn.commit()
                            print("DONE")
                        if inst2=='3':
                            ail=input('Aile:')
                            prod_id=int(input('product ID:'))
                            stoc=int(input('new product stock:'))
                            qwr2='update {} set no_of_items="{}" where product_id="{}"'.format(ail,stoc,prod_id)
                            cur.execute(qwr2)
                            conn.commit()
                            print('DONE')
                        if inst2=='4':
                            # qw1=product() # ext(qw1)
                            ﬁle1=open("AILES.txt","r")
                            print("product_id","product_name","product amount","product_cost")
                            while ﬁle1:
                                line = ﬁle1.readline()
                                print(line)
                                if line == "":
                                    break
                                qw1="use product"
                                cur.execute(qw1)
                                conn.commit()
                                qwr1="select * from {}".format(line)
                                cur.execute(qwr1)
                                data=cur.fetchall()
                                for row in data:
                                    print(row)
                            ﬁle1.close() #space()
                        if inst2=='5':
                            cust=open("bill.txt","r")
                            u=cust.read()
                            print(u)
                            cust.close()

                            cus_b=input('customer bill you want to see:')
                            ﬁle=open(cus_b,'r')
                            bills=ﬁle.read()
                            print(bills)
                            ﬁle.close()

                        if inst2=='6':
                            break
                else:
                    print('invalid password or username')
            if coroi=='2':
                print(options1)
                inst2=input("instruction:")
                if inst2=='1':
                    name=input('customer name:')
                    f='bill{}.txt'.format(name)
                    cust=open(f,"a")
                    d=f+'/n'
                    cust.write(d)
                    cust.close()
                    bill=[]
                    while True:
                        print(billing)
                        inp3=input("instuction:")
                        if inp3=='1':
                            while True:
                                product_id=int(input("product ID:"))
                                num=int(input("no of product:"))
                                ﬁle=open("AILES.txt","r")
                                while ﬁle:
                                    line = ﬁle.readline()
                                    if line == "":
                                        break
                                    qwr1="use product"
                                    cur.execute(qwr1)
                                    conn.commit()

                                    qwr="select product_id from {} where product_id='{}'".format(line,product_id)
                                    cur.execute(qwr)
                                    d=cur.fetchall()
                                    #print(d)
                                    if d==[]:
                                        continue
                                    try:
                                        k=d[0][0]
                                        #print(k)
                                        if k==product_id:
                                            pr=[product_id,num]
                                            print(pr)
                                            bill=bill+[pr]
                                            #print(bill)
                                            break
                                        else:
                                            continue
                                    except:
                                        pass
                                ﬁle.close()

                                print(ad_bill)
                                ip2=input('insruction:')
                                if ip2=='1':
                                    continue
                                if ip2=='2':
                                    break
                        if inp3=='2':
                            product_id=int(input("product ID:"))
                            for u in bill:
                                if u[0]==product_id:
                                    bill.remove(u)
                                    break
                                else:
                                    continue
                        if inp3=='3':
                            print('product_id','product','no_of_product','cost',sep="|")
                            for u in bill:
                                #print(u)
                                ﬁle=open("AILES.TXT",'r')
                                while ﬁle:
                                    line = ﬁle.readline()
                                    if line == "":
                                        break
                                    qwr1="use product"
                                    cur.execute(qwr1)
                                    conn.commit()
                                    qw_select="select * from {} where product_id='{}'".format(line,u[0])
                                    cur.execute(qw_select)
                                    data=cur.fetchall()
                                    if data==[]:
                                        continue
                                    else:
                                        print(data[0][0],data[0][1],u[1],data[0][3],sep="|")
                                ﬁle.close()
                        if inp3=='4':
                            am_bill=0
                            print(bill)

                            import datetime as date
                            time = date.datetime.now()
                            time='{}\n'.format(time)
                            cus=open(f,'a')
                            cus.write(time)
                            cus.ﬂush()
                            print('product_id','product','no_of_product','cost',sep="|")

                            prodil='product_id'+'product'+'no_of_product'+'cost\n'
                            cus.write(prodil)
                            cus.ﬂush()

                            for u in bill:
                                #print(u)
                                ﬁle=open("AILES.TXT",'r')
                                while ﬁle:
                                    line = ﬁle.readline()
                                    if line == "":
                                        break
                                    qwr1="use product"
                                    cur.execute(qwr1)
                                    conn.commit()

                                    qw_select="select * from {} where product_id='{}'".format(line,u[0])
                                    cur.execute(qw_select)

                                    data=cur.fetchall()
                                    if data==[]:
                                        continue
                                    else:
                                        print(data[0][0],data[0][1],u[1],data[0][3],sep='|',end='\n')
                                        j='{},{},{},{}\n'.format(data[0][0],data[0][1],u[1],data[0][3])
                                        cus.write(j)
                                        cus.ﬂush()
                                        its_cst=u[1]*data[0][3]
                                        am_bill=am_bill+its_cst
                                        n_num=data[0][2]-u[1]
                                        qw_up='update {} set no_of_items={} where product_id={}'.format(line,n_num,u[0])
                                        cur.execute(qw_up)
                                        conn.commit()
                                ﬁle.close()
                                print('BILL:',am_bill,end='\n')
                                hmm='BILL:'+'{}\n'.format(am_bill)
                                cus.write(hmm)
                                cus.ﬂush()
                                cus.close()
                                break

                            #End For U
                if inst2=='2':
                    p=input('product to ﬁnd:')
                    itemﬁnd(p)
                    break
    elif inst1=='2':
        break
    else:
        print('invalid')
