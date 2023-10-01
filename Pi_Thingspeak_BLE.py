import machine
import time
import ujson
import bluetooth

# Configure the onboard temperature sensor
temp_sensor = machine.ADC(machine.ADC.CORE_TEMP)


while True:
    # Read the temperature sensor value
    sensor_value = temp_sensor.read_u16() * (3.3 / (65536))

    # Convert the sensor value to temperature in degrees Celsius
    temperature_celsius = 27 - (sensor_value - 0.706)/0.001721

    # Convert Celsius to Fahrenheit
    temperature_fahrenheit = (temperature_celsius * 9/5) + 32

    # Print the temperature in both Celsius and Fahrenheit
    print("Temperature in C: {:.2f}°C".format(temperature_celsius))
    print("Temperature in F: {:.2f}°F".format(temperature_fahrenheit))
    print("<...>")
    time.sleep_ms(500)
    
    #BLE
    # Prepare data to send
    data = {"temperature in C": temperature_celsius, "temperature in F": temperature_fahrenheit}

    # Convert data to JSON
    data_json = ujson.dumps(data)


