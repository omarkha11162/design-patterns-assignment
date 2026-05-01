# Design Patterns Assignment

## 📌 Project Description
This project is a Smart Task Management System implemented in Python.  
It demonstrates the use of three design patterns to solve common software design problems.

## 🧩 Design Patterns Used

### 1. Singleton Pattern
- Ensures only one instance of TaskManager exists.
- Used to manage all tasks centrally.

### 2. Factory Method Pattern
- Used to create different types of tasks (Work / Personal).
- Encapsulates object creation logic.

### 3. Observer Pattern
- Allows users to receive notifications when tasks are updated.
- Implements a notification system.

## 🏗️ Project Structure
- `TaskManager` → Singleton
- `TaskFactory` → Factory
- `NotificationSystem` → Observer
- `main.py` → main execution file

## ▶️ How to Run
```bash
python main.py
