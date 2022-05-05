import mpy_csv

def get_training_procedures(assigned_roles, employee_name):
    procs = []
    unique_procs = []
    csvfile = mpy_csv.Csv.csv_to_array("./Book1.csv")
    # print(csvfile[0][1])
    for i in range(len(csvfile)):
        for role in assigned_roles:
            if role in csvfile[i][6]:
                procs.append(csvfile[i][1])

    for word in procs:
        if word not in unique_procs:
            unique_procs.append(word)

    print(f'The procedures to be trained for {employee_name} are: {unique_procs}')

def add_roles(assigned_roles):
    role = str(input('add roles or "q" to quit adding and get the procedures list: '))
    if (role == 'q' or role == 'Q'):
        print(f"goodbye the roles filtered for are: {assigned_roles}")
        return assigned_roles
    elif (role != 'q' or role != 'Q'):
        assigned_roles.append(role)
        print(assigned_roles)
        add_roles(assigned_roles)



if __name__ == '__main__':
    assigned_roles = []
    employee_name = str(input('What is the employee name: '))
    add_roles(assigned_roles)
    get_training_procedures(assigned_roles, employee_name)



