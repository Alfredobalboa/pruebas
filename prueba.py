import subprocess
from io import open

def comando():
    response = subprocess.run(["netsh", "wlan", "show", "profile"],
                              capture_output=True,
                              text=True
                              )
    return response.stdout

variable1 = comando() 

def obtenerNombres(variable1):
    x = ""
    contructor = ""
    for i in variable1:
        x += i
        if "Perfil de todos los usuarios     : " in x:
            contructor += i

    contructor = contructor.replace("Perfil de todos los usuarios     : ","")
    contructor = contructor.split("\n")
    for i in range(len(contructor)):
        contructor[i] = contructor[i].strip()
    del contructor[-1]
    del contructor[-1]
    return contructor

def obtenerSalidaClaves(variable2):
    listaClaves=[]
    for i in range(len(variable2)):
        response = subprocess.run(["netsh", "wlan", "show", "profile",f'name={variable2[i]}',"key=clear"],
                            capture_output=True,
                            text=True
                            )
        x= ""
        contructor = ""
        for i in response.stdout:
            x += i
            if "Contenido de la clave  : " in x:
                contructor += i
                if i == "\n":
                    break
        contructor = contructor.replace("\n","")
        listaClaves.append(contructor)

        
    return listaClaves
variable1 = comando() 

variable2 = obtenerNombres(variable1)

variable3 = obtenerSalidaClaves(variable2)

contraseñas = ""

for i in range(len(variable2)):
    contraseñas += f"Usuario: {variable2[i]}\nContraseña: {variable3[i]}\n-----------------------------------------------\n"
archivo = open("contraseñas.txt","w")
archivo.write(contraseñas)
archivo.close()