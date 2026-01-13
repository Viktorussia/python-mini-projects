# time_convert.py
# Перевод секунд в формат ЧЧ:ММ:СС

seconds = int(input("Ведите количество секунд: "))

hours = seconds // 3600
minutes = (seconds % 3600) // 60
secs = seconds % 60

print(f"{hours:02d}:{minutes:02d}:{secs:02d}")