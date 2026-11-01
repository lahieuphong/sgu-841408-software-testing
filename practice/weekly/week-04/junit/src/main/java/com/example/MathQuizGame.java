package com.example;

import java.util.Random;
import java.util.Scanner;
import java.util.concurrent.TimeUnit;

public class MathQuizGame {
    private static final int TIME_LIMIT = 30; // Time limit in seconds
    private static final int NUMBER_OF_QUESTIONS = 10; // Number of questions to ask

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Random random = new Random();
        int score = 0;

        System.out.println("Welcome to the Math Quiz Game!");
        System.out.println("You have " + TIME_LIMIT + " seconds to answer " + NUMBER_OF_QUESTIONS + " questions.");
        System.out.println("Get ready...");

        // Start a timer in a new thread
        Timer timer = new Timer(TIME_LIMIT);
        Thread timerThread = new Thread(timer);
        timerThread.start();

        for (int i = 0; i < NUMBER_OF_QUESTIONS; i++) {
            if (timer.isTimeUp()) {
                break; 
            }
            // Generate two random numbers and an operator
            int num1 = random.nextInt(100);
            int num2 = random.nextInt(100);
            String operator = getRandomOperator();
            int correctAnswer = calculateAnswer(num1, num2, operator);

            // Ask the question
            System.out.print("Question " + (i + 1) + ": " + num1 + " " + operator + " " + num2 + " = ");
            int userAnswer = scanner.nextInt();

            // Check the answer
            if (userAnswer == correctAnswer) {
                score++;
                System.out.println("Correct!");
            } else {
                System.out.println("Incorrect! The correct answer is " + correctAnswer);
            }
        }

        // End of the game
        System.out.println("Time's up! Your score: " + score + "/" + NUMBER_OF_QUESTIONS);
        scanner.close();
    }

    private static String getRandomOperator() {
        Random random = new Random();
        int operatorIndex = random.nextInt(4); 
        switch (operatorIndex) {
            case 0:
                return "+";
            case 1:
                return "-"; 
            case 2:
                return "*"; 
            case 3:
                return "/"; 
            default:
                return "+"; 
        }
    }

    private static int calculateAnswer(int num1, int num2, String operator) {
        switch (operator) {
            case "+":
                return num1 + num2;
            case "-":
                return num1 - num2;
            case "*":
                return num1 * num2;
            case "/":
                return num2 != 0 ? num1 / num2 : 0; 
            default:
                return 0;
        }
    }
}

class Timer implements Runnable {
    private final int timeLimit;
    private boolean timeUp;

    public Timer(int timeLimit) {
        this.timeLimit = timeLimit;
        this.timeUp = false;
    }

    @Override
    public void run() {
        try {
            TimeUnit.SECONDS.sleep(timeLimit);
            timeUp = true;
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }

    public boolean isTimeUp() {
        return timeUp;
    }
}
