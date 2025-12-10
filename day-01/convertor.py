print("Welcome to python unit convertor!")
print("Choose your number to continue : ")

choice=input(" 1. Temperature \n 2. Distance \n Enter your value : ")

def temperature():
    temperature_choice = input(" 1. Celcius to Kelvin \n 2. Kelvin to Celcius ")

    def celcius_to_kelvin():
            print("Celcius to Kelvin...")
            celcius_input=float(input("Enter your Value : "))
            kelvin_output=celcius_input+273.15

            print(f"Your Input value is {celcius_input}°C. A change of 1°C is exactly equal to a change of 1 K.. \n T(k)=T(c)+273.15 , k = Kelvin and c = Celcious \n Your answer is {kelvin_output}K")
            
            
    def kelvin_to_celcius():
            print("Kelvin to Celcius...")
            kelvin_input=float(input("Enter your value : "))
            celcius_output=kelvin_input-273.15
            print(celcius_output)

    while True:
        try:
            if temperature_choice == "1":
                celcius_to_kelvin()
            elif temperature_choice == "2":
                kelvin_to_celcius()
            else:
                print("Invalid choice!")
            break
        except:
            print("Invalid number! Please enter a numeric value.")


if choice == '1':
     temperature()
