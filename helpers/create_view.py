def create_view(name, username, name_input, phone_number, pref_country, pref_sphere) -> str:
    return (f"<b>Имя в Telegram:</b> {name}\n<b>Юзернейм в Telegram:</b> {username}\n"
            f"<b>Введенное имя клиента:</b> {name_input}\n<b>Номер телефона:</b> {phone_number}\n"
            f"<b>Предпочтительная страна:</b> {pref_country}\n<b>Предпочтительная сфера:</b> {pref_sphere}")

