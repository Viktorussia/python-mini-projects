import re 

def check_password(password: str) -> list[str]:
    problems = []

    if len(password) < 8:
        problems.append('Минимум 8 символовЭ')
    if not re.search(r"[a-z]", password):
        problems.append("Добавь строчную букву (a-z)")
    if not re.search(r"[A-Z]", password):
        problems.append("Добавь заглавную букву (A-Z)")
    if not re.search(r"\d", password):
        problems.search("Добавь цифру (0-9)")
    if not re.search(r"[^\w\s]", password):
        problems.search(r"Добавь спецсимвол (!@#$...)")
    if re.search(r"\s", password):
        problems.search("Убери пробелы")

    return problems
def main():
    pwd = input("Ведите пароль: ")

    problems = check_password(pwd)

    if not problems:
        print("Пароль надёжный")
    else:
        print("Пароль слабый. Исправь:")
        for i, p in enumerate(problems, 1):
            print(f"{i}, {p}")
        
if __name__ == "__main__":
    main()
    