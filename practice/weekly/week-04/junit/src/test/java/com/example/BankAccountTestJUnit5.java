package com.example;

import org.junit.jupiter.api.*;

import static org.junit.jupiter.api.Assertions.*;

public class BankAccountTestJUnit5 {
    private BankAccount account;

    @BeforeAll
    public static void setupBeforeAll() {
        System.out.println("Setup Before All - JUnit 5");
    }

    @BeforeEach
    public void setUp() {
        account = new BankAccount(100.0);
    }

    @Test
    public void testDeposit_ValidAmount_IncreasesBalance() {
        account.deposit(50.0);
        assertEquals(150.0, account.getBalance(), 0.01);
    }

    @Test
    public void testDeposit_NegativeAmount_ThrowsException() {
        IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> {
            account.deposit(-10.0);
        });
        assertEquals("Deposit amount must be positive.", exception.getMessage());
    }

    @Test
    public void testWithdraw_ValidAmount_DecreasesBalance() {
        account.withdraw(30.0);
        assertEquals(70.0, account.getBalance(), 0.01);
    }

    @Test
    public void testWithdraw_AmountMoreThanBalance_ThrowsException() {
        IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> {
            account.withdraw(150.0);
        });
        assertEquals("Insufficient funds.", exception.getMessage());
    }

    @Test
    public void testWithdraw_NegativeAmount_ThrowsException() {
        IllegalArgumentException exception = assertThrows(IllegalArgumentException.class, () -> {
            account.withdraw(-20.0);
        });
        assertEquals("Withdrawal amount must be positive.", exception.getMessage());
    }

    @AfterEach
    public void tearDown() {
        account = null; // Giải phóng tài nguyên sau mỗi bài kiểm tra
    }

    @AfterAll
    public static void tearDownAfterAll() {
        System.out.println("Tear Down After All - JUnit 5");
    }
}
