package workshop;

public class DiscountCalculatorBefore {
    public static double finalPrice(double price, String segment, boolean hasCoupon, boolean isBlackFriday) {
        if (price < 0) throw new IllegalArgumentException("price");

        double p = price;

        if (segment != null && segment.equals("vip")) {
            p = p * 0.90;
        } else if (segment != null && segment.equals("student")) {
            p = p * 0.95;
        }

        if (hasCoupon) {
            p = p - 50;
        }

        if (isBlackFriday) {
            if (p > 500) p = p * 0.85;
            else p = p * 0.90;
        }

        if (p < 0) p = 0;
        return Math.round(p * 100.0) / 100.0;
    }
}