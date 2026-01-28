namespace InvoiceLib;

public static class InvoiceCalculatorBefore
{
    public static decimal Total(decimal subtotal, bool isVip, bool hasCoupon, bool isInternational)
    {
        if (subtotal < 0) throw new ArgumentException("subtotal");

        var t = subtotal;

        if (isInternational)
        {
            t = t + (t * 0.16m);
        }

        if (isVip)
        {
            t = t * 0.90m;
        }

        if (hasCoupon)
        {
            t = t - 50m;
        }

        if (t < 0) t = 0;
        return Math.Round(t, 2);
    }
}