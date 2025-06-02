import re

# Ejemplo de dataset: registros de sensores desestructurados
sensor_logs = """
Sensor1: Temp=23.5C Humidity=45% Timestamp=2025-06-01 12:34:56
Random text here, ignore this line.
Sensor2: Humidity=50% Temp=25.1C Timestamp=2025-06-01 12:35:01
Sensor3: Timestamp=2025-06-01 12:36:22 Temp=22.8C Humidity=40%
Another random line with no data.
Sensor4: Temp=24.0C Timestamp=2025-06-01 12:37:45 Humidity=55%
"""

def extract_sensor_data(logs):
    # Expresión regular para valores de temperatura
    temp_pattern = r'Temp=([0-9.]+)C'
    # Expresión regular para valores de humedad
    humidity_pattern = r'Humidity=([0-9]+)%'
    # Expresión regular para timestamps
    timestamp_pattern = r'Timestamp=(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})'

    # Extraer temperaturas
    temperatures = re.findall(temp_pattern, logs)
    # Extraer humedades
    humidities = re.findall(humidity_pattern, logs)
    # Extraer timestamps
    timestamps = re.findall(timestamp_pattern, logs)

    return temperatures, humidities, timestamps

# Extraer información del dataset de registros de sensores
temperatures, humidities, timestamps = extract_sensor_data(sensor_logs)

# Mostrar resultados
print("Temperaturas detectadas:")
print(temperatures)

print("\nHumedades detectadas:")
print(humidities)

print("\nTimestamps detectados:")
print(timestamps)