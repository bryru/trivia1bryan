import time 
puntaje = 0
iniciar_trivia = True  
intentos = 0 
print ("\033[32m Bienvenido a mi trivia sobre plantas carnivoras \033[39m")
print ("Veremos que tanto sabes sobre estos hermosos especimenes")
print ("Tienes", puntaje, "puntos")
nombre = input("Ingresa tu nombre: ")
print("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
while iniciar_trivia == True: 
  intentos += 1
  puntaje = 0
  print("\nIntento número:", intentos)
  input("Presiona Enter para continuar")
  print("Primera pregunta...")
  
  print ("1) ¿cual de estas no se considera una planta carnivora?")
  print ("a) genliseas")
  print ("b) arenaría")
  print ("c) utricularias")
  print ("d) dionaea muscipula")
  respuesta_1 = input("\nTu respuesta: ")
  while respuesta_1 not in ("a", "b", "c", "d"):
    respuesta_1 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_1 == "b":
    puntaje += 10
    print ("Muy bien", nombre, "!")
  else:
    print ("Incorrecto", nombre, "!")
  print(nombre, "llevas", puntaje, "puntos")
  # 2
  print("\n1) ¿cual de las siguientes utiliza muscilago como metodo de caza?")
  print("a) sarracenias")
  print("b) nephentes")
  print("c) Aldrovandas")
  print("d) pinguiculas")
  respuesta_2 = input("\nTu respuesta: ")
  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_2 == "a":
    print("Incorrecto!", nombre, "Python es un lenguaje de alto nivel")
  elif respuesta_2 == "b":
    print("Incorrecto!", nombre, "Java es un lenguaje de alto nivel")
  elif respuesta_2 == "c":
    print("Incorrecto!", nombre, "PHP es un lenguaje de alto nivel")
  else:
    puntaje += 10
    print ("Muy bien", nombre, "!")
  print(nombre, "llevas", puntaje, "puntos")
  # 3
  print ("\n1) ¿que planta carnivora a sido capaz de digerir roedores?")
  print ("a) dioneas")
  print ("b) nephentes")
  print ("c) droseras")
  print ("d) cephalotus")
  respuesta_3 = input("\nTu respuesta: ")
  while respuesta_3 not in ("a", "b", "c", "d"):
    respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  if respuesta_3 == "a":
    print ("Totalmente incorrecto! ...")
    puntaje = puntaje / 2
  elif respuesta_3 == "d":
    print ("...")
    puntaje = puntaje + 5
  elif respuesta_3 == "c":
    print ("Incorrecto! ...")
    puntaje = puntaje - 5
  else:
    print ("Correcto! ...")
    puntaje = puntaje * 2
  
  time.sleep(1) 
  print("Jugando...")
  time.sleep(1)
  puntaje = puntaje +20  
  print("Excelente, has obtenido", puntaje, "puntos")
  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":  
   print("\nEspero que lo hayas pasado bien, hasta pronto!")
   iniciar_trivia = False  