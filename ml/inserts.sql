-- Inserindo uma moeda
INSERT INTO currency_tb(name, abbreviation)
VALUES ('REAL', 'BRL'),
       ('DOLAR', 'USD');



-- Inserindo um continente
INSERT INTO continent_tb(name)
VALUES ('AFRICA'),
       ('AMERICA'),
       ('EUROPE'),
       ('ASIA'),
       ('OCEANIA'),
       ('ANTARCTICA');



-- Inserindo um país
INSERT INTO country_tb(id_continent, id_currency, name, abbreviation, medium_sallary, minimum_sallary)
VALUES (2, 1, 'BRAZIL', 'BRA', 2.600, 1.300),
       (2, 2, 'UNITED STATES', 'USA', 2.600, 1.300);



-- Inserindo um nível de risco
INSERT INTO risk_level_tb(risk, title)
VALUES (0, 'EXTRA_LOW'),
       (1, 'LOW'),
       (2, 'MID'),
       (3, 'HIGH'),
       (4, 'EXTRA_HIGH');



-- Inserindo um nível de risco para perfil
INSERT INTO risk_profile_tb(risk, title)
VALUES (0, 'EXTRA_LOW'),
       (1, 'LOW'),
       (2, 'MID'),
       (3, 'HIGH'),
       (4, 'EXTRA_HIGH');



-- Inserindo uma marca (NIKE)
INSERT INTO brand_tb(id_country, name)
VALUES (2, 'Nike');

INSERT INTO brand_category_tb(id_brand, title)
VALUES (1, 'FITNESS'), (1, 'HEALTHY');


-- Inserindo uma instancia
INSERT INTO birthdate_tb(day, month, year) VALUES (03, 06, 2004);

INSERT INTO school_level_tb(title)
VALUES ('NONE'), ('FUNDAMENTAL'),
    ('FUNDAMENTAL_II'),
    ('MID_SCHOOL'),
    ('SUPERIOR'),
    ('POSTGRADUATE'),
    ('MASTER'),
    ('DOCTORATE');

INSERT INTO stocks_tb(id_risk, id_brand, stock_name, amount_avg)
VALUES (2, 1, 'NKE', 50.0);

INSERT INTO data_tb(
    id_birthdate,
    id_country,
    id_currency,
    id_most_used_ecommerce,
    id_risk_profile,
    id_school_level,
    id_last_stock,
    id_pretend_stock,
    fullname,
    email,
    ddd,
    phone,
    gender,
    mobile_device_os,
    current_job_category
) VALUES
  (1, -- ID birthdate
   1, -- ID country
   1, -- ID currency
   NULL, -- ID most used ecommerce
   4, -- ID risk profile
   4, -- ID school level
   1, -- ID last stock
   1, -- ID pretend stock
   'Carlos Alberto Barcelos do Amaral',
   'carlosabdoamaral@gmail.com',
   '48',
   '999734977',
   'MALE',
   'IOS',
   'TECHNOLOGY')
;