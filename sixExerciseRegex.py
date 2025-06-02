import re

# Ejemplo de entradas de usuario
user_inputs = [
    "SELECT * FROM users WHERE username = 'admin'; --",
    "DROP TABLE users;",
    "Normal text without SQL commands.",
    "' OR '1'='1",
    "INSERT INTO users (username, password) VALUES ('admin', '1234');",
    "DELETE FROM users WHERE id = 1;",
    "Safe input with no malicious content."
]

# Expresión regular para detectar patrones de SQL Injection
sql_injection_pattern = r'\b(SELECT|DROP|INSERT|DELETE|UPDATE|UNION|--|;|\'|\"|OR|AND)\b'

# Analizar entradas de usuario
def detect_sql_injection(inputs):
    for i, input_text in enumerate(inputs):
        matches = re.findall(sql_injection_pattern, input_text, flags=re.IGNORECASE)
        if matches:
            print(f"Posible SQL Injection detectado en entrada {i + 1}: {matches}")
        else:
            print(f"Entrada {i + 1} es segura.")

# Ejecutar análisis
detect_sql_injection(user_inputs)