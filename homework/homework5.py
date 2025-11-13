class User:
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin

def admin_only(func):
    def wrapper(user):
        if user.is_admin:
            print(f"[Доступ разрешен] Пользователь {user.name} - администратор.")
            return func(user)
        else:
            error = PermissionError("Доступ запрещен! Только админ может выполнить эту операцию.")
            print(error)
            return None
    return wrapper

@admin_only
def delete_database(user):
    print("База данных удалена.")

admin = User("Алексей", is_admin=True)
user = User("Мария", is_admin=False)
delete_database(admin)
print()
delete_database(user)
print()

