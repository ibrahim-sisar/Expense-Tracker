import json
import datetime

time=datetime.datetime.now()
date= time.strftime("%Y-%m-%d")

def add_expense(Description,Amount):
    with open('expense.json','r') as id_number:
        data2=json.load(id_number)
        id_number2=len(data2)+1


    dict={
        'Description':Description,
        'Amount':Amount,
        'date':date,
        'id':id_number2
            }
    with open('expense.json','r') as git_data:
        data=json.load(git_data)
        data[id_number2]=dict
        
    
    with open('expense.json','w') as save:
        json.dump(data,save)
        print(f'Expense added successfully (ID: {id_number2})')  
def delet_expense(id):
    no=id
    with open('expense.json','r') as git_data:
        data=json.load(git_data)
       
        if no in data:
            data.pop(no)
            with open('expense.json','w') as delete:
                json.dump(data,delete)
                print(f'expense deleted successfully')    
def summary():
    with open('expense.json','r') as git_data:
        data=json.load(git_data)
        totel=0
        for expense in data:
            amount=int(data[expense]['Amount'])
            totel=totel+amount
        print(f'Total expenses: {totel}$')
def list():
    with open('expense.json','r') as git_data:
        data=json.load(git_data)
        print('ID  '+'Date       '+' Description  '+'Amount\n')
        for i in data:
            id=data[i]['id']
            date2=data[i]['date']
            Description=data[i]['Description']
            Amount=data[i]['Amount']
            print(f'{id}   {date2}  {Description}    {Amount}')
def summary_m(m):
    with open('expense.json','r') as git_data:
        
        data=json.load(git_data)
        m2=str(m)
        totel=0
        for expense in data:
            m4=str(data[expense]['date']).split('-')[1]
            m3=str(data[expense]['date']).split('-')
            dt = datetime.datetime(int(m3[0]),int(m3[1]),int(m3[2]))
            amount=data[expense]['Amount']
            if m4==m2:
                totel=totel+amount
        print(f'Total expenses for {dt.strftime('%B')} : {totel}$')
           


while True:
    expense=input('$ expense-tracker ')
    
    
    if expense.startswith('add'):
        inp=expense[4:]
        if inp.startswith('--description'):
            Description=inp[15:inp.rfind('--amount')-2]
            inp2=inp[8:]
        if inp2.rfind('--amount') != -1:
            amount=inp2[inp2.rfind('--amount')+9:]
        add_expense(Description,amount)
    elif expense.startswith('delete'):
        inp=expense[7:]

        if inp.startswith('--id'):
            id=inp[5:]
        delet_expense(id)
    elif expense.startswith('summary'):
        inp=expense[8:]

        if inp.startswith('--month'):
            m=inp[8:]
            summary_m(m)
        else:
            summary()
    elif expense.startswith('list'):
        inp=expense[5:]
        list()

        
        
    else:
        print('Unknown input')
    




