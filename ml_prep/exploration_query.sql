SELECT
    product,
    COUNT(*) AS avg_orders,
    AVG(price) AS avg_price
    SUM (high_value_order) AS high_value_order_count
FROM ecommerce_analysis.orders_features
GROUP BY product
ORDER BY 2 DESC, 4 DESC, 3 DESC;
