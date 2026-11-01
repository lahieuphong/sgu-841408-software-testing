package com.example;

import java.util.Scanner;

public class MathUtils {
    // Phương thức tính giai thừa
    public int factorial(int n) {
        if (n < 0) {
            throw new IllegalArgumentException("Number must be non-negative");
        }
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    // Phương thức main để kiểm tra
    public static void main(String[] args) {
        MathUtils mathUtils = new MathUtils();
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter a non-negative integer to calculate its factorial: ");
        int number = scanner.nextInt();

        try {
            int factorial = mathUtils.factorial(number);
            System.out.println("The factorial of " + number + " is " + factorial);
        } catch (IllegalArgumentException e) {
            System.out.println("Error: " + e.getMessage());
        } finally {
            scanner.close();
        }
    }
}