def generate_recommendation(
    predicted_price,
    current_price
):

    change_percent = (
        (
            predicted_price
            - current_price
        )
        /
        current_price
    ) * 100

    if change_percent > 3:
        return "🟢 BUY"

    elif change_percent < -3:
        return "🔴 SELL"

    else:
        return "🟡 HOLD"