package com.example;

import org.junit.jupiter.api.*;
import org.junit.jupiter.params.ParameterizedTest;
import org.junit.jupiter.params.provider.CsvSource;
import org.junit.jupiter.api.RepeatedTest;

import static org.junit.jupiter.api.Assertions.*;

public class BankAccountTest {
    private BankAccount account;

    @BeforeAll
    public static void setupBeforeAll() {
        System.out.println("Setup Before All - JUnit 5");
    }

    @BeforeEach
    public void setUp() {
        account = new BankAccount(100.0);
    }

    @ParameterizedTest
    @CsvSource({
        "50.0, 150.0",  // Deposit 50.0, expect balance 150.0
        "20.0, 120.0",  // Deposit 20.0, expect balance 120.0
        "0.0, 100.0"    // Attempt to deposit 0.0, expect balance 100.0 (should throw)
    })
    public void testDeposit(double depositAmount, double expectedBalance) {
        if (depositAmount <= 0) {
            Exception exception = assertThrows(IllegalArgumentException.class, () -> {
                account.deposit(depositAmount);
            });
            assertEquals("Deposit amount must be positive.", exception.getMessage());
        } else {
            account.deposit(depositAmount);
            assertEquals(expectedBalance, account.getBalance(), 0.01);
        }
    }

    @RepeatedTest(3)
    public void testWithdrawValidAmount() {
        account.withdraw(30.0);
        assertEquals(70.0, account.getBalance(), 0.01);
    }

    @ParameterizedTest
    @CsvSource({
        "150.0, Insufficient funds.", // Withdraw more than balance
        "-20.0, Withdrawal amount must be positive." // Withdraw negative amount
    })
    public void testWithdrawInvalidAmount(double withdrawAmount, String expectedMessage) {
        Exception exception = assertThrows(IllegalArgumentException.class, () -> {
            account.withdraw(withdrawAmount);
        });
        assertEquals(expectedMessage, exception.getMessage());
    }

    @AfterEach
    public void tearDown() {
        account = null; // Clear account after each test
    }

    @AfterAll
    public static void tearDownAfterAll() {
        System.out.println("Tear Down After All - JUnit 5");
    }
}
