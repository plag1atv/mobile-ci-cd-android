# Базовый образ с Java, Gradle и Android SDK
FROM cangol/android-gradle:latest

# Рабочая директория внутри контейнера
WORKDIR /opt/workspace

# По умолчанию просто показываем подсказку
CMD ["bash", "-c", "echo 'Используй: docker run ... ./gradlew build'"]