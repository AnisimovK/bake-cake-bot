def create_start_message(username: str) -> str:
    greeting_msg = f"""
Привет, {username}!

Telegram-бот тортов на заказ. Принимает заказы на торты, собранные самим покупателем.

Если вам интересны наши услуги, пожалуйста, пройдите регистрацию.
Для этого согласитесь на обработку персональных данных.
"""
    return greeting_msg