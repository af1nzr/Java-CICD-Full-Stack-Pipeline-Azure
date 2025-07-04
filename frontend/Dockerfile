# frontend/Dockerfile

# Build stage
FROM maven:3.9.4-eclipse-temurin-17 AS build
WORKDIR /app

# Copy project files
COPY pom.xml .
COPY src ./src

# Build the project (skip tests to speed up)
RUN mvn clean package -DskipTests

# Rename the JAR for consistency
RUN mv target/*.jar app.jar

# Run stage
FROM eclipse-temurin:17
WORKDIR /app
COPY --from=build /app/app.jar app.jar
EXPOSE 80
CMD ["java", "-jar", "app.jar", "--server.port=80"]
