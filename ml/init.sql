CREATE TABLE currency_tb (
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL,
abbreviation VARCHAR(10) NOT NULL
);


CREATE TABLE continent_tb(
id SERIAL PRIMARY KEY,
name VARCHAR(255) NOT NULL
);


CREATE TABLE country_tb(
id SERIAL PRIMARY KEY,
id_continent INT REFERENCES continent_tb(id),
id_currency INT REFERENCES currency_tb(id),
name VARCHAR(255) NOT NULL,
abbreviation VARCHAR(5) NOT NULL,
medium_sallary FLOAT NOT NULL,
minimum_sallary FLOAT NOT NULL
);


CREATE TYPE school_level_enum AS ENUM(
    'NONE',
    'FUNDAMENTAL',
    'FUNDAMENTAL_II',
    'MID_SCHOOL',
    'SUPERIOR',
    'POSTGRADUATE',
    'MASTER',
    'DOCTORATE'
);


CREATE TABLE school_level_tb (
id SERIAL PRIMARY KEY,
title school_level_enum NOT NULL
);


CREATE TABLE risk_level_tb(
id SERIAL PRIMARY KEY,
risk INT NOT NULL,
title VARCHAR(255) NOT NULL
);


CREATE TABLE brand_tb(
id SERIAL PRIMARY KEY,
id_country INT REFERENCES country_tb(id),
name VARCHAR(255) NOT NULL
);


CREATE TYPE brand_category_enum AS ENUM(
'NONE',
'FINANCE',
'FITNESS',
'FOOD',
'TECHNOLOGY',
'MUSIC',
'CONSTRUCTION',
'ENTERTAINMENT',
'HEALTHY',
'THEATER',
'MOVIE',
'EDUCATION',
'MARKETING',
'ELECTRICAL'
);
CREATE TABLE brand_category_tb(
id SERIAL PRIMARY KEY,
id_brand INT REFERENCES brand_tb(id),
title brand_category_enum NOT NULL
);


CREATE TABLE stocks_tb (
id SERIAL PRIMARY KEY,
id_risk INT REFERENCES risk_level_tb(id),
id_brand INT REFERENCES brand_tb(id),
stock_name VARCHAR(255) NOT NULL,
amount_avg FLOAT NOT NULL
);


CREATE TABLE ecommerce_tb(
id SERIAL PRIMARY KEY,
id_brand INT REFERENCES brand_tb(id),
name VARCHAR(255) NOT NULL,
url VARCHAR(255) NOT NULL
);


CREATE TABLE birthdate_tb(
    id SERIAL PRIMARY KEY,
    day INT NOT NULL,
    month INT NOT NULL,
    year INT NOT NULL
);


CREATE TYPE mobile_device_os_enum AS ENUM(
    'IOS',
    'ANDROID'
);

CREATE TYPE gender_enum AS ENUM(
    'MALE',
    'FEMALE',
    'OTHER'
);


CREATE TYPE job_category_enum AS ENUM(
    'TECHNOLOGY',
    'FITNESS'
);


CREATE TABLE risk_profile_tb(
    id SERIAL PRIMARY KEY,
    risk INT NOT NULL,
    title VARCHAR(255) NOT NULL
);


CREATE TABLE data_tb(
    id SERIAL PRIMARY KEY,
    id_birthdate INT REFERENCES birthdate_tb(id),
    id_country INT REFERENCES country_tb(id),
    id_currency INT REFERENCES currency_tb(id),
    id_most_used_ecommerce INT REFERENCES ecommerce_tb(id),
    id_risk_profile INT REFERENCES risk_profile_tb(id),
    id_school_level INT REFERENCES school_level_tb(id),
    id_last_stock INT REFERENCES stocks_tb(id),
    id_pretend_stock INT REFERENCES stocks_tb(id),

    fullname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    ddd VARCHAR(255) NOT NULL,
    phone VARCHAR(255) NOT NULL,
    gender gender_enum NOT NULL,

    current_amount FLOAT NOT NULL DEFAULT 0,
    amount_avg_per_month FLOAT NOT NULL DEFAULT 0,

    already_invested BOOLEAN DEFAULT FALSE,
    technology_knowledge_level INT NOT NULL DEFAULT 0,

    use_ecommerce BOOLEAN DEFAULT FALSE,
    mobile_device_os mobile_device_os_enum NOT NULL,

    current_job_category job_category_enum NOT NULL
);