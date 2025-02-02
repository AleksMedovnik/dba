import subprocess
import datetime
import schedule
import time

def backup():
    backup_filename = f"mydb_backup_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.dump"
    backup_command = f"docker exec -t postgres-container pg_dump -U dba_admin -F c -f /backups/{backup_filename} mydb"

    try:
        subprocess.run(backup_command, shell=True, check=True)
        print(f"✅ Бэкап успешно создан: {backup_filename}")
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка при создании бэкапа: {e}")

# Запускаем бэкап каждый день в 02:00
schedule.every().day.at("02:00").do(backup)

print("⏳ Планировщик запущен. Ожидание следующего запуска...")

while True:
    schedule.run_pending()
    time.sleep(60)  # Проверять каждую минуту
