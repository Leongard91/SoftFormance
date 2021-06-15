raw_input = input('Enter coma-separated passwords: ')
inp_list = raw_input.split(',')
verificated_list_of_passwords = list()
for password in inp_list:
    validation_count = 0
    # Length and space validation
    if not 4 <= len(password) <= 6 or ' ' in password:
        continue
    
    # validation_0_9
    for i in '0123456789':
        if i in password: 
            validation_count += 1
            break

    # validation_A_Z
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        if i in password: 
            validation_count += 1
            break

    # validation_a_z
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i in password: 
            validation_count += 1
            break

    # validation_others
    for i in '*#+@':
        if i in password: 
            validation_count += 1
            break
    
    if validation_count != 4: continue
    else: verificated_list_of_passwords.append(password)

print(','.join(verificated_list_of_passwords))

    