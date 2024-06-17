def validarPrimervalor(min_len):
 aux = 0
 while aux < 3:
    try:
        password = input('ingresa una contraseña (debe comenzar con numero): ')
        validar = float(password[0])
        if len(password) >= min_len:
          return password, aux
          break
        else:
         print('la contraseña no cumple con la longitud minima')
         aux += 1
    except ValueError:
       print('recuerda que la contraseña debe comenzar con un numero')
       aux += 1

 print('excediste el numero de intentos permitidos')
 return password,aux
    
def corroborarContraseña(min_len):
  password,intentos = validarPrimervalor(min_len)
  if intentos < 3:
    aux = 0 
    while aux < 3:
       password_2 = input('ingresa la contraseña nuevamente: ')
       if password_2 == password:
        print('contraseña correcta')
        return password
        break
       else:
         print('Contraseña incorrecta, intenta de nuevo')
         aux += 1

    print('Excediste el numero de intentos,vuelve a intentar en 24 horas')
    
corroborarContraseña(6)        
    