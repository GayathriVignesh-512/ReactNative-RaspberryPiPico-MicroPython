import machine
import urequests 
from machine import Pin
import network, time
#from dht import DHT11, InvalidChecksum
 
HTTP_HEADERS = {'Content-Type': 'application/json'} 
 
ssid = 'Vigthri'
password = 'vigneshgayathri9599'
 
# Configure Pico W as Station
sta_if=network.WLAN(network.STA_IF)
sta_if.active(True)
 
if not sta_if.isconnected():
    print('connecting to network...')
    sta_if.connect(ssid, password)
    while not sta_if.isconnected():
     pass
print('network config:', sta_if.ifconfig()) 

adc = machine.ADC(4)

# ThingSpeak API Key and URL
api_key = 'BWFT7MI4BKWLHL7E'
thingspeak_url = 'https://api.thingspeak.com/update?api_key=BWFT7MI4BKWLHL7E'

while True:
    ADC_voltage = adc.read_u16() * (3.3 / (65536))
    temperature_celcius = 27 - (ADC_voltage - 0.706)/0.001721
    temp_fahrenheit=32+(1.8*temperature_celcius)
    print("Temperature: {}°C {}°F".format(temperature_celcius,temp_fahrenheit))

    time.sleep_ms(500)  # Send data every 10 minutes (adjust as needed)
    
    dht_readings = {'field1':f"{temperature_celcius}", 'field2':f"{temp_fahrenheit}"} 
    request = urequests.post( thingspeak_url, json = dht_readings, headers = HTTP_HEADERS )  
    request.close() 
    print(dht_readings) 
