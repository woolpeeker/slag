
CREATE TABLE cpus(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    brand VARCHAR(64) NOT NULL,
    series VARCHAR(64) NOT NULL,
    lithography INT NOT NULL,
    core INT NOT NULL,
    threads INT NOT NULL,
    base_frequency DOUBLE NOT NULL,
    max_frequency DOUBLE NOT NULL,
    socket VARCHAR(64) NOT NULL,
    tdp INT NOT NULL,
    price FLOAT,
    update_date DATETIME NOT NULL,
    PRIMARY KEY (`id`)
);

--insert test data
INSERT INTO cpus SET
name = 'Intel® Core™ i9-9900K Processor',
brand = 'Intel',
series = 'Core',
lithography = 14,
core = 8,
threads = 16,
base_frequency = 3.6,
max_frequency = 5.0,
socket = 'FCLGA1151',
tdp = 95,
price = 4099,
update_date = '2019-06-05 00:00:00';

INSERT INTO cpus SET
name = 'AMD Ryzen™ 9 3900X',
brand = 'AMD',
series = 'Ryzen',
lithography = 7,
core = 12,
threads = 24,
base_frequency = 3.8,
max_frequency = 4.6,
socket = 'AM4',
tdp = 105,
price = NULL,
update_date = '2019-06-05 00:00:00';