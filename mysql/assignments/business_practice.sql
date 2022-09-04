-- find all the clients, billing and charged date
SELECT clients.first_name, clients.last_name,  billing.amount, billing.charged_datetime
FROM clients
JOIN billing ON clients.id = billing.clients_id;

-- list all the domain name and leads for each site
SELECT sites.domain_name, leads.first_name, leads.last_name
FROM sites
JOIN leads ON sites.id = leads.sites_id;

-- get the name of clients , their sites , and first, last names of the leads whose involve
SELECT clients.first_name AS client_first, clients.last_name AS client_last, sites.domain_name, leads.first_name, leads.last_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
JOIN leads ON sites.id = leads.sites_id;

-- LEFT & RIGHT JOIN
SELECT clients.first_name, clients.last_name, sites.domain_name
FROM clients
LEFT JOIN sites ON clients.id = sites.clients_id;


-- GROUP BY 
-- SUM MAX MIN AVG
SELECT clients.first_name, clients.last_name,  SUM(billing.amount)
FROM clients
JOIN billing ON clients.id = billing.clients_id
GROUP BY clients.id;

-- LIST ALL DOMAIN NAMES ASSOCIATES WITH EACH CLIENTS
SELECT GROUP_CONCAT(sites.domain_name) as domians, clients.first_name, clients.last_name
FROM clients
JOIN sites ON clients.id = sites.clients_id
GROUP BY clients.id;

-- COUNT
-- FIND THE TOTAL NUMBERS OF LEADS FOR EACH SITES
SELECT sites.domain_name, COUNT(leads.id)
FROM sites
JOIN leads ON sites.id = leads.sites_id
GROUP BY sites.id;