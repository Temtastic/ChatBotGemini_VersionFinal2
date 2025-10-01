from typing import List, Dict

def build_system_prompt(role_instructions:str) -> str:
    base = (
        "sos un chatbot de consola que responde en español de forma clara y útil."
        "si el usuario pide codigo, inclui explicaciones breves"
        "evita informacion inventada, y pedi aclaraciones si faltan datos."
    )
    return base + f"contexto de rol: {role_instructions}"

def collapse_history(history: List[Dict[str, str]]) -> List[Dict[str, str]]:
    #mantiene formato {"role": "user", "content": "..."}
    return history