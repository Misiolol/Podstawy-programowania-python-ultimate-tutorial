def temperature_converter(temperature :float, from_scale, to_scale):
    celsius_error = -273.15
    kelvin_error = 0
    fahrenheit_error = -459.67
    
    if from_scale == "Celsius":
        celsius = temperature
        if celsius < celsius_error:
            return "NO"
    elif from_scale == "Kelvin":
        celsius = temperature - 273.15
        if temperature < kelvin_error:
            return "NO"
    elif from_scale == "Fahrenheit":
        celsius = (temperature - 32) * 5 / 9
        if temperature < fahrenheit_error:
            return "NO"
    
    # from given to celcius


    # from celcius to expected

    if to_scale == "Celsius":
        return f"{celsius:.2f}"
    elif to_scale == "Kelvin":
        kelvin = celsius + 273.15
        return f"{kelvin:.2f}"
    elif to_scale == "Fahrenheit":
        fahrenheit = celsius * 9 / 5 + 32
        return f"{fahrenheit:.2f}"

def main():
    solutions = []

    num = int(input())
    for _ in range(num):
        input_data = input().split()
        temperature = float(input_data[0])
        from_scale = input_data[1]  
        to_scale = input_data[2]   
        
        result = temperature_converter(temperature, from_scale, to_scale)
        solutions.append(result)


    for i in range(len(solutions)):
        print(solutions[i])

main()