conversation_memory = {}


def get_history(user_id: int):
    return conversation_memory.get(user_id, [])


def save_message(user_id: int, role: str, message: str):
    if user_id not in conversation_memory:
        conversation_memory[user_id] = []

    conversation_memory[user_id].append({
        "role": role,
        "content": message
    })