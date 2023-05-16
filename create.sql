USE ict158;


DROP TABLE IF EXISTS IpRecords;
DROP TABLE IF EXISTS Cities ;

CREATE TABLE Cities (
    `key` INT PRIMARY KEY,
    firstName VARCHAR(255),
    asciiName VARCHAR(255),
    altNames TEXT,
    latitude DECIMAL(10, 8),
    longitude DECIMAL(11, 8),
    featureClass VARCHAR(255),
    featureCode VARCHAR(255),
    countryCode VARCHAR(255),
    altCountryCode VARCHAR(255),
    admin1code VARCHAR(255),
    admin2code VARCHAR(255),
    admin3code VARCHAR(255),
    admin4code VARCHAR(255),
    population INT,
    elevation INT,
    digitalElevationModel INT,
    timezone VARCHAR(255),
    modificationDate DATE,
    altNamesSel VARCHAR(255),
    adminXcode VARCHAR(255),
    areaCode VARCHAR(255)
);



CREATE TABLE IpRecords (
    id INT PRIMARY KEY AUTO_INCREMENT,
    version INT,
    ip VARCHAR(255),
    searchPageCount INT,
    autoSearchCount INT,
    searchCount INT,
    passFailedCount INT,
    passRecoveryCount INT,
    languageTag VARCHAR(255),
    userAgent VARCHAR(255),
    lastAccessTime DATETIME,
    isAdmin BOOLEAN,
    crawlCount INT,
    crawlManCount INT,
    badCrawlManCount INT,
    hackManCount INT,
    blackErrorCount INT,
    whiteErrorCount INT,
    errorHistory VARCHAR(255),
    searchHistory VARCHAR(255),
    countryGuess VARCHAR(255),
    cityGuessSafe INT,
    cityGuess INT,
    FOREIGN KEY (cityGuess) REFERENCES Cities(`key`)
);
