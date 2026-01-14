import csv

def analyze_csv(filename: str):
    total = 0
    count = 0

    with open(filename, newline="", encjding="utf-8") as file:
        reader = csv.DictReader(file)

        for row in reader:
            amount = float(row["amount"])
            total += amount
            count += 1

    average = total / count if count > 0 else 0
    return total, average, count

def main():
    filename = "sample.csv"

    totel, average, count = analyze_csv(filename)

    print("Отчет по CSV-файлу")
    print(f"Количество записей: {count}")
    print(f"Сумма: {totel}")
    print(f"Среднее значение: {average:.2f}")

if __name__ == "__main__":
    main()
    