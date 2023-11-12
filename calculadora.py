

num1 = int(input("Ingresa un numero"))
num2 = int(input("Ingresa otro numero"))
operacion = input("Ingresa una operacion")

def calculadora (num1,num2,operacion):

 if operacion == "+":
        return  f"El resultado de la suma es:, {num1 + num2}"
 elif operacion == "-":
         return  f"El resultado de la resta es:, {num1 - num2}"
 elif operacion == "*":
         return ( f"El resultado de la multiplicacion es:", {num1 * num2})
 elif operacion == "/":
          if num2 != 0:
             return("no se puede dividir por 0")
          else:
            return f"El resultado de la división es: {num1 / num2}"
 else:
  return("operacion no valida")


resultado = calculadora(num1,num2,operacion)   
print(resultado)