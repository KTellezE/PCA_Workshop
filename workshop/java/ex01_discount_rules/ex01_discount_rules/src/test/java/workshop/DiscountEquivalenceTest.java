package workshop;

import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class DiscountEquivalenceTest {

    @Test
    void equivalence_matrix() {
        double[] prices = {0, 10, 500, 501, 1000};
        String[] segs = {null, "vip", "student", "other"};
        boolean[] flags = {false, true};

        for (double price : prices) {
            for (String seg : segs) {
                for (boolean coupon : flags) {
                    for (boolean bf : flags) {
                        double b = DiscountCalculatorBefore.finalPrice(price, seg, coupon, bf);
                        double a = DiscountCalculatorAfter.finalPrice(price, seg, coupon, bf);
                        assertEquals(b, a, 0.0001);
                    }
                }
            }
        }
    }
}