import re

# Ejemplo de texto para analizar
text = """
Hoy me siento muy feliz y contento porque logré mis objetivos.
Sin embargo, también tengo algo de miedo por los retos futuros.
A veces me invade la tristeza y melancolía, pero trato de mantenerme positivo.
El enojo y la frustración aparecen cuando las cosas no salen como quiero.
"""

# Expresiones regulares por emoción
emotion_patterns = {
    "Alegría": r'\b(feliz|contento|alegría|sonrisa)\b',
    "Tristeza": r'\b(triste|llanto|melancolía|dolor)\b',
    "Enojo": r'\b(enojo|furia|rabia|frustración)\b',
    "Miedo": r'\b(miedo|temor|pánico|inseguridad)\b'
}

# Detectar emociones en el texto
emotion_counts = {}
for emotion, pattern in emotion_patterns.items():
    matches = re.findall(pattern, text, flags=re.IGNORECASE)
    emotion_counts[emotion] = len(matches)

# Mostrar resultados
print("Detección de emociones en el texto:")
for emotion, count in emotion_counts.items():
    print(f"{emotion}: {count} coincidencias")