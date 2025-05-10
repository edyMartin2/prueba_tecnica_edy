CREATE VIEW daily_company_totals AS
SELECT
    c.company_name,
    ch.transaction_date,
    SUM(ch.amount::numeric) AS total_amount
FROM
    charges ch
JOIN
    companies c ON ch.company_id = c.company_id
GROUP BY
    c.company_name,
    ch.transaction_date
ORDER BY
    ch.transaction_date, c.company_name;
