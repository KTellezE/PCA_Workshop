def format_user_message(name, role, last_login_days, is_blocked):
    if name is None or name.strip() == "":
        name = "(sin nombre)"

    if is_blocked:
        return f"{name}: acceso bloqueado"

    if role == "admin":
        if last_login_days is None:
            return f"{name} (admin): último acceso desconocido"
        if last_login_days > 30:
            return f"{name} (admin): inactivo"
        return f"{name} (admin): ok"

    if role == "user":
        if last_login_days is None:
            return f"{name}: último acceso desconocido"
        if last_login_days > 60:
            return f"{name}: inactivo"
        return f"{name}: ok"

    return f"{name}: rol no soportado"