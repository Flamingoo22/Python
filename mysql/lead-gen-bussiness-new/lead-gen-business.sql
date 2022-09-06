-- 1. What query would you run to get the total revenue for March of 2012?
-- SELECT SUM(billing.amount) AS revenue
-- FROM billing
-- WHERE billing.charged_datetime > '2012/02/28' AND billing.charged_datetime < '2012/04/01';
-- 2. What query would you run to get total revenue collected from the client with an id of 2?
-- SELECT clients.client_id, sum(billing.amount) AS revenue
-- FROM billing
-- JOIN clients
-- ON billing.client_id = clients.client_id
-- WHERE clients.client_id = 2;

-- 3. What query would you run to get all the sites that client with an id of 10 owns?
-- SELECT clients.client_id, sites.domain_name AS 'Total Sites'
-- FROM sites
-- JOIN clients
-- ON sites.client_id = clients.client_id
-- WHERE clients.client_id = 10;
-- 4. What query would you run to get total # of sites created per month per year for the client with an id of 1? What about for client with an id of 20?
-- SELECT clients.client_id, sites.domain_name, sites.created_datetime
-- FROM clients
-- JOIN sites
-- ON clients.client_id = sites.client_id
-- WHERE clients.client_id = 1 OR clients.client_id = 20
-- GROUP BY sites.created_datetime
-- 5. What query would you run to get the total # of leads generated for each of the sites between January 1, 2011 to February 15, 2011?
-- SELECT sum(leads.leads_id), sites.domain_name
-- FROM leads
-- JOIN sites
-- ON leads.site_id = sites.site_id
-- WHERE sites.created_datetime > '2011/01/01' AND sites.created_datetime < '2011/02/15'
-- GROUP BY sites.domain_name
-- 6. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients between January 1, 2011 to December 31, 2011?

-- 7. What query would you run to get a list of client names and the total # of leads we've generated for each client each month between months 1 - 6 of Year 2011?

-- 8. What query would you run to get a list of client names and the total # of leads we've generated for each of our clients' sites between January 1, 2011 to December 31, 2011? Order this query by client id.  Come up with a second query that shows all the clients, the site name(s), and the total number of leads generated from each site for all time.

-- 9. Write a single query that retrieves total revenue collected from each client for each month of the year. Order it by client id.  First try this with integer month, second with month name.  A SELECT subquery will be needed for the second challenge.  Look at this for a hint.

-- 10. Write a single query that retrieves all the sites that each client owns. Group the results so that all of the sites for each client are displayed in a single field. It will become clearer when you add a new field called 'sites' that has all the sites that the client owns. (HINT: use GROUP_CONCAT)