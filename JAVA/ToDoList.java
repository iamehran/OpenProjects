// This program allows users to add tasks, view tasks, mark tasks as completed, and exit the program.

import java.util.ArrayList;
import java.util.Scanner;

class Task {
    String description;
    boolean isCompleted;

    Task(String description) {
        this.description = description;
        this.isCompleted = false;
    }
}

public class ToDoList {
    private static ArrayList<Task> tasks = new ArrayList<>();

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        while (true) {
            System.out.println("1. Add Task");
            System.out.println("2. View Tasks");
            System.out.println("3. Mark Task as Completed");
            System.out.println("4. Exit");
            System.out.print("Enter your choice: ");
            int choice = scanner.nextInt();
            scanner.nextLine();  // Consume the newline character after nextInt()

            switch (choice) {
                case 1:
                    System.out.print("Enter task description: ");
                    String description = scanner.nextLine();
                    Task task = new Task(description);
                    tasks.add(task);
                    System.out.println("Task added successfully!");
                    break;
                case 2:
                    if (tasks.isEmpty()) {
                        System.out.println("No tasks found.");
                    } else {
                        System.out.println("Tasks:");
                        for (int i = 0; i < tasks.size(); i++) {
                            Task currentTask = tasks.get(i);
                            System.out.println((i + 1) + ". " + (currentTask.isCompleted ? "[Completed] " : "") + currentTask.description);
                        }
                    }
                    break;
                case 3:
                    System.out.print("Enter the task number to mark as completed: ");
                    int taskNumber = scanner.nextInt();
                    if (taskNumber >= 1 && taskNumber <= tasks.size()) {
                        Task selectedTask = tasks.get(taskNumber - 1);
                        selectedTask.isCompleted = true;
                        System.out.println("Task marked as completed!");
                    } else {
                        System.out.println("Invalid task number.");
                    }
                    break;
                case 4:
                    System.out.println("Exiting program. Goodbye!");
                    System.exit(0);
                    break;
                default:
                    System.out.println("Invalid choice. Please try again.");
                    break;
            }
        }
    }
}
