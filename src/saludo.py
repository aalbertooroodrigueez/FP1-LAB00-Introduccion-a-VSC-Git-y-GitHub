from datetime import datetime

hora_actual = datetime.now().hour
<<<<<<< HEAD
nombre = input("¿Cuál es tu nombre? ")
if hora_actual < 12:
  print("Buenos días, " nombre)
elif hora_actual 12 <= hora_actual < 20:
  print(f"Buenas tardes, " nombre)
elif hora_actual <= 23:
  print(f"Buenas noches, " nombre)
=======

nombre = input("¿Cuál es tu nombre? ")

if hora_actual < 12:
    print(f"Buenos días,  {nombre}")
elif 12 <= hora_actual < 20:
     print(f"Buenas tardes, {nombre}")
else:
    print(f"Buenas noches,  {nombre}")    
>>>>>>> 40a3cb5 (Añadir saludo segun la hora)
