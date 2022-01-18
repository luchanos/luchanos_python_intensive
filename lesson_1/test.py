from datetime import datetime

with open("/Users/nnsviridov/PycharmProjects/AcademicProjects/luchanos_python_intensive/lesson_1/cron_test_file.txt", "w") as f:
    f.write(str(datetime.now()))
