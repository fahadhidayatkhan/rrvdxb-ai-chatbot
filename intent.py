def detect_intent(message: str) -> str:
    message = message.lower()

    if any(word in message for word in ["deal", "discount", "offer", "sale"]):
        return "deals"

    if any(word in message for word in ["order", "track", "delivery"]):
        return "order_tracking"

    if any(word in message for word in ["compare", "difference"]):
        return "comparison"

    if any(word in message for word in ["recommend", "suggest", "gift"]):
        return "recommendation"

    if any(word in message for word in ["price", "cost", "product", "available"]):
        return "product_question"

    return "general"