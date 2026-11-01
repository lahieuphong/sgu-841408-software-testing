package com.example;

import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

public class MathUtilsTest {

    @Test
    public void testFactorialWithPositiveNumber() {
        MathUtils mathUtils = new MathUtils();
        assertEquals(120, mathUtils.factorial(5)); // 5! = 120
    }

    @Test
    public void testFactorialWithZero() {
        MathUtils mathUtils = new MathUtils();
        assertEquals(1, mathUtils.factorial(0)); // 0! = 1
    }

    @Test
    public void testFactorialWithNegativeNumber() {
        MathUtils mathUtils = new MathUtils();
        assertThrows(IllegalArgumentException.class, () -> {
            mathUtils.factorial(-1);
        });
    }
}