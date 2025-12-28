FROM python:3.11-slim

# تحديد مجلد العمل داخل الكونتينر
WORKDIR /app

# نسخ ملفات المشروع
COPY . /app

# تثبيت المتطلبات
RUN pip install --no-cache-dir -r requirements.txt

# فتح البورت اللي Replit بيستخدمه
EXPOSE 8080

# تشغيل التطبيق
CMD ["python", "main.py"]
