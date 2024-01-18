SELECT count(o.id),
       c.login
FROM "Orders" AS o
INNER JOIN "Couriers" AS c ON o."courierId"=c.id
WHERE o."inDelivery" = true
GROUP BY c.login;