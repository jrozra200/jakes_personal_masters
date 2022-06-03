-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Which Crime Scene Report is for the Duck?
SELECT *
FROM crime_scene_reports
WHERE description LIKE '%Humphrey Street%';

-- Which Interviews are for the CS50 Duck?
SELECT interviews.*
FROM interviews
JOIN crime_scene_reports
ON interviews.year = crime_scene_reports.year AND 
    interviews.month = crime_scene_reports.month AND 
    interviews.day = crime_scene_reports.day  
WHERE crime_scene_reports.description LIKE '%Humphrey Street%' AND 
    interviews.transcript LIKE '%bakery%';
    
-- Crime took place at 10:15am
-- Look for security footage between 10:15 and 10:25
-- Here is a list of people who left in the 10 minutes following the crime

SELECT *
FROM people
WHERE license_plate IN (
    SELECT bakery_security_logs.license_plate 
    FROM bakery_security_logs
    JOIN crime_scene_reports
    ON bakery_security_logs.year = crime_scene_reports.year AND 
        bakery_security_logs.month = crime_scene_reports.month AND 
        bakery_security_logs.day = crime_scene_reports.day  
    WHERE crime_scene_reports.description LIKE '%Humphrey Street%' AND 
        bakery_security_logs.hour = 10 AND 
        bakery_security_logs.minute >= 15 AND 
        bakery_security_logs.minute <= 25
);

-- Look for PEOPLE who had ATM withdraws from Leggett Street before 10:15
-- No time stamp... only date.

SELECT people.*
FROM atm_transactions, crime_scene_reports, bank_accounts, people
WHERE atm_transactions.year = crime_scene_reports.year AND 
    atm_transactions.month = crime_scene_reports.month AND 
    atm_transactions.day = crime_scene_reports.day AND
    atm_transactions.account_number = bank_accounts.account_number AND 
    bank_accounts.person_id = people.id AND 
    crime_scene_reports.description LIKE '%Humphrey Street%' AND 
    atm_transactions.atm_location = 'Leggett Street' AND 
    atm_transactions.transaction_type = 'withdraw';

-- Who did they call while they were leaving? Call was while they were leaving 
-- and less than a minute long.

-- Who Were the callers?
SELECT people.* 
FROM phone_calls, crime_scene_reports, people
WHERE phone_calls.year = crime_scene_reports.year AND 
    phone_calls.month = crime_scene_reports.month AND 
    phone_calls.day = crime_scene_reports.day AND
    phone_calls.caller = people.phone_number AND 
    crime_scene_reports.description LIKE '%Humphrey Street%' AND 
    phone_calls.duration < 60;
    
-- Who were the receivers? 
SELECT people.* 
FROM phone_calls, crime_scene_reports, people
WHERE phone_calls.year = crime_scene_reports.year AND 
    phone_calls.month = crime_scene_reports.month AND 
    phone_calls.day = crime_scene_reports.day AND
    phone_calls.receiver = people.phone_number AND 
    crime_scene_reports.description LIKE '%Humphrey Street%' AND 
    phone_calls.duration < 60;
    
-- Look for Passengers on the first plane out of Fiftyville on 7/29
SELECT people.*
FROM passengers
JOIN people
ON passengers.passport_number = people.passport_number
WHERE passengers.flight_id IN (
    SELECT flights.id 
    FROM airports, flights
    WHERE airports.id = flights.origin_airport_id AND 
        airports.city = 'Fiftyville' AND 
        flights.year = 2021 AND 
        flights.month = 7 AND 
        flights.day = 29
    ORDER BY flights.hour ASC,
        flights.minute ASC
    LIMIT 1
);

-- LETS TRIANGULATE: Here's the theif
SELECT a.*
FROM (
    SELECT *
    FROM people
    WHERE license_plate IN (
        SELECT bakery_security_logs.license_plate 
        FROM bakery_security_logs
        JOIN crime_scene_reports
        ON bakery_security_logs.year = crime_scene_reports.year AND 
            bakery_security_logs.month = crime_scene_reports.month AND 
            bakery_security_logs.day = crime_scene_reports.day  
        WHERE crime_scene_reports.description LIKE '%Humphrey Street%' AND 
            bakery_security_logs.hour = 10 AND 
            bakery_security_logs.minute >= 15 AND 
            bakery_security_logs.minute <= 25
    )
) a
JOIN (
    SELECT people.*
    FROM atm_transactions, crime_scene_reports, bank_accounts, people
    WHERE atm_transactions.year = crime_scene_reports.year AND 
        atm_transactions.month = crime_scene_reports.month AND 
        atm_transactions.day = crime_scene_reports.day AND
        atm_transactions.account_number = bank_accounts.account_number AND 
        bank_accounts.person_id = people.id AND 
        crime_scene_reports.description LIKE '%Humphrey Street%' AND 
        atm_transactions.atm_location = 'Leggett Street' AND 
        atm_transactions.transaction_type = 'withdraw'
) b
ON a.name = b.name
JOIN (
    SELECT people.*
    FROM passengers
    JOIN people
    ON passengers.passport_number = people.passport_number
    WHERE passengers.flight_id IN (
        SELECT flights.id 
        FROM airports, flights
        WHERE airports.id = flights.origin_airport_id AND 
            airports.city = 'Fiftyville' AND 
            flights.year = 2021 AND 
            flights.month = 7 AND 
            flights.day = 29
        ORDER BY flights.hour ASC,
            flights.minute ASC
        LIMIT 1
    )
) c
ON a.name = c.name 
JOIN (
    SELECT people.* 
    FROM phone_calls, crime_scene_reports, people
    WHERE phone_calls.year = crime_scene_reports.year AND 
        phone_calls.month = crime_scene_reports.month AND 
        phone_calls.day = crime_scene_reports.day AND
        phone_calls.caller = people.phone_number AND 
        crime_scene_reports.description LIKE '%Humphrey Street%' AND 
        phone_calls.duration < 60
) d
ON a.name = d.name;

-- He went to: 

SELECT * 
FROM airports
WHERE airports.id IN (
    SELECT flights.destination_airport_id 
    FROM airports, flights
    WHERE airports.id = flights.origin_airport_id AND 
        airports.city = 'Fiftyville' AND 
        flights.year = 2021 AND 
        flights.month = 7 AND 
        flights.day = 29
    ORDER BY flights.hour ASC,
        flights.minute ASC
    LIMIT 1
);

-- His Accomplice: 
SELECT people.* 
FROM phone_calls, crime_scene_reports, people
WHERE phone_calls.year = crime_scene_reports.year AND 
    phone_calls.month = crime_scene_reports.month AND 
    phone_calls.day = crime_scene_reports.day AND
    phone_calls.receiver = people.phone_number AND 
    crime_scene_reports.description LIKE '%Humphrey Street%' AND 
    phone_calls.duration < 60 AND 
    phone_calls.caller IN (
        SELECT a.phone_number
        FROM (
            SELECT *
            FROM people
            WHERE license_plate IN (
                SELECT bakery_security_logs.license_plate 
                FROM bakery_security_logs
                JOIN crime_scene_reports
                ON bakery_security_logs.year = crime_scene_reports.year AND 
                    bakery_security_logs.month = crime_scene_reports.month AND 
                    bakery_security_logs.day = crime_scene_reports.day  
                WHERE crime_scene_reports.description LIKE '%Humphrey Street%' AND 
                    bakery_security_logs.hour = 10 AND 
                    bakery_security_logs.minute >= 15 AND 
                    bakery_security_logs.minute <= 25
            )
        ) a
        JOIN (
            SELECT people.*
            FROM atm_transactions, crime_scene_reports, bank_accounts, people
            WHERE atm_transactions.year = crime_scene_reports.year AND 
                atm_transactions.month = crime_scene_reports.month AND 
                atm_transactions.day = crime_scene_reports.day AND
                atm_transactions.account_number = bank_accounts.account_number AND 
                bank_accounts.person_id = people.id AND 
                crime_scene_reports.description LIKE '%Humphrey Street%' AND 
                atm_transactions.atm_location = 'Leggett Street' AND 
                atm_transactions.transaction_type = 'withdraw'
        ) b
        ON a.name = b.name
        JOIN (
            SELECT people.*
            FROM passengers
            JOIN people
            ON passengers.passport_number = people.passport_number
            WHERE passengers.flight_id IN (
                SELECT flights.id 
                FROM airports, flights
                WHERE airports.id = flights.origin_airport_id AND 
                    airports.city = 'Fiftyville' AND 
                    flights.year = 2021 AND 
                    flights.month = 7 AND 
                    flights.day = 29
                ORDER BY flights.hour ASC,
                    flights.minute ASC
                LIMIT 1
            )
        ) c
        ON a.name = c.name 
        JOIN (
            SELECT people.* 
            FROM phone_calls, crime_scene_reports, people
            WHERE phone_calls.year = crime_scene_reports.year AND 
                phone_calls.month = crime_scene_reports.month AND 
                phone_calls.day = crime_scene_reports.day AND
                phone_calls.caller = people.phone_number AND 
                crime_scene_reports.description LIKE '%Humphrey Street%' AND 
                phone_calls.duration < 60
        ) d
        ON a.name = d.name
    );