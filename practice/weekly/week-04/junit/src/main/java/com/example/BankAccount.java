package com.example;

public class BankAccount {
    private double balance;

    public BankAccount(double initialBalance) {
        if (initialBalance < 0) {
            throw new IllegalArgumentException("Initial balance cannot be negative.");
        }
        this.balance = initialBalance;
    }

    public void deposit(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Deposit amount must be positive.");
        }
        balance += amount;
    }

    public void withdraw(double amount) {
        if (amount <= 0) {
            throw new IllegalArgumentException("Withdrawal amount must be positive.");
        }
        if (amount > balance) {
            throw new IllegalArgumentException("Insufficient funds.");
        }
        balance -= amount;
    }

    public double getBalance() {
        return balance;
    }

    // Phương thức main để thử nghiệm lớp BankAccount
    public static void main(String[] args) {
        // Tạo một tài khoản ngân hàng với số dư ban đầu
        BankAccount account = new BankAccount(100.0);
        
        // Hiển thị số dư ban đầu
        System.out.println("Initial balance: " + account.getBalance());

        // Thực hiện gửi tiền
        account.deposit(50.0);
        System.out.println("Balance after deposit of 50.0: " + account.getBalance());

        // Thực hiện rút tiền
        account.withdraw(30.0);
        System.out.println("Balance after withdrawal of 30.0: " + account.getBalance());

        // Thử rút số tiền lớn hơn số dư
        try {
            account.withdraw(150.0);
        } catch (IllegalArgumentException e) {
            System.out.println("Exception: " + e.getMessage());
        }

        // Thử gửi số tiền âm
        try {
            account.deposit(-20.0);
        } catch (IllegalArgumentException e) {
            System.out.println("Exception: " + e.getMessage());
        }

        // Hiển thị số dư cuối cùng
        System.out.println("Final balance: " + account.getBalance());
    }
}
