using Xunit;

namespace InvoiceLib.Tests;

public class EquivalenceTests
{
    [Fact]
    public void Matrix_equivalence()
    {
        decimal[] subtotals = { 0m, 10m, 100m, 500m, 1000m };
        bool[] flags = { false, true };

        foreach (var s in subtotals)
        foreach (var vip in flags)
        foreach (var coupon in flags)
        foreach (var intl in flags)
        {
            var b = InvoiceLib.InvoiceCalculatorBefore.Total(s, vip, coupon, intl);
            var a = InvoiceLib.InvoiceCalculatorAfter.Total(s, vip, coupon, intl);
            Assert.Equal(b, a);
        }
    }
}