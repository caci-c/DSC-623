import sqlite3
import pandas as pd

# Connect to existing database file in current directory
# If file does not exist, create it in the current directory
db_connect = sqlite3.connect('final_project.db')

# Enable foreign keys
db_connect.execute("PRAGMA foreign_keys = ON;")

# Instantiate cursor object for executing queries
cursor = db_connect.cursor()

# Drop tables
cursor.execute("DROP TABLE IF EXISTS HireAgreement")
cursor.execute("DROP TABLE IF EXISTS Vehicle")
cursor.execute("DROP TABLE IF EXISTS Staff")
cursor.execute("DROP TABLE IF EXISTS Client")
cursor.execute("DROP TABLE IF EXISTS Outlet")

# Create table
query_outlet = """
CREATE TABLE IF NOT EXISTS Outlet (
    outletNo INTEGER PRIMARY KEY,
    address VARCHAR(255) NOT NULL UNIQUE,
    phone VARCHAR(20) NOT NULL UNIQUE
        CHECK (phone GLOB '+[0-9]*'),
    fax VARCHAR(20) NOT NULL UNIQUE
        CHECK (fax GLOB '+[0-9]*'),
    CHECK (outletNo BETWEEN 1 AND 99999)
);
"""
cursor.execute(query_outlet)

query_vehicle = """
CREATE TABLE IF NOT EXISTS Vehicle (
    registrationNo VARCHAR(15) PRIMARY KEY,
    model VARCHAR(50) NOT NULL,
    make VARCHAR(30) NOT NULL,
    engineSize REAL NOT NULL 
        CHECK(engineSize BETWEEN .1 AND 10.0),
    capacity INTEGER NOT NULL
        CHECK(capacity BETWEEN 1 AND 20),
    mileage INTEGER NOT NULL 
        CHECK(mileage BETWEEN 0 AND 999999),
    dailyHireRate REAL NOT NULL 
        CHECK(dailyHireRate BETWEEN .1 AND 9999.99),
    outletNo INTEGER NOT NULL,
    FOREIGN KEY(outletNo) REFERENCES Outlet(outletNo)
        ON UPDATE CASCADE
        ON DELETE NO ACTION
);
"""
cursor.execute(query_vehicle)

query_client = """
CREATE TABLE IF NOT EXISTS Client (
    clientNo INTEGER PRIMARY KEY 
        CHECK(clientNo BETWEEN 1 AND 999999),
    fName VARCHAR(15) NOT NULL,
    lName VARCHAR(15) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL
        CHECK (phone GLOB '+[0-9]*'),
    DOB DATE NOT NULL
        CHECK(DOB<CURRENT_DATE AND CURRENT_DATE-DOB>21),
    licenseNo VARCHAR(25) NOT NULL UNIQUE
);
"""
cursor.execute(query_client)

query_hireAgreement = """
CREATE TABLE IF NOT EXISTS HireAgreement (
    hireNo INTEGER PRIMARY KEY 
        CHECK(hireNo BETWEEN 1 AND 999999),
    agreementStart DATE NOT NULL
        CHECK(agreementStart<=CURRENT_DATE),
    agreementEnd DATE NOT NULL
        CHECK(agreementEnd>CURRENT_DATE),
    startingMileage INTEGER NOT NULL
        CHECK(startingMileage BETWEEN 0 AND 999999),
    endingMileage INTEGER NOT NULL
        CHECK(endingMileage BETWEEN 0 AND 999999),
    clientNo INTEGER NOT NULL,
    registrationNo VARCHAR(15) NOT NULL,
    FOREIGN KEY(clientNo) REFERENCES Client(clientNo)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    FOREIGN KEY(registrationNo) REFERENCES Vehicle(registrationNo)
        ON UPDATE CASCADE
        ON DELETE NO ACTION,
    UNIQUE(registrationNo, agreementStart),
    CHECK(endingMileage>=startingMileage)
);
"""
cursor.execute(query_hireAgreement)

query_staff = """
CREATE TABLE IF NOT EXISTS Staff (
    staffNo INTEGER PRIMARY KEY 
        CHECK(staffNo BETWEEN 1 AND 999999),
    fName VARCHAR(15) NOT NULL,
    lName VARCHAR(15) NOT NULL,
    address VARCHAR(255) NOT NULL,
    phone VARCHAR(20) NOT NULL
        CHECK (phone GLOB '+[0-9]*'),
    DOB DATE
        CHECK(DOB<CURRENT_DATE),
    sex CHAR(1) 
        CHECK(sex IN('M','F')),
    outletNo INTEGER NOT NULL,
    FOREIGN KEY(outletNo) REFERENCES Outlet(outletNo)
        ON UPDATE CASCADE ON DELETE SET DEFAULT
);
"""

cursor.execute(query_staff)

# Verify table creation
print("Tables created:")
df_tables = pd.read_sql_query("SELECT name " \
"FROM sqlite_master WHERE type='table';", db_connect)
print(df_tables)

# Insert rows into tables
query_outlet_tuples = """
    INSERT OR IGNORE INTO Outlet(outletNo, address, phone, fax)
    VALUES
        (1, '2300 SW 1st St., Miami, FL 33126', '+13054067717', '+13059578625'),
        (2, '653 N. 23rd Ave.,Miami, FL 38426', '+14722738506', '+19834108259'),
        (3, '1213 S. Brickell Bay Drive, Miami, FL 33131', '+15054666823', '+14724299798'),
        (4, '15 NE 3rd Ct. Circle, Miami, FL 31627', '+15056440522', '+15408489913'),
        (5, '6520 NW Miami Ave., Miami, FL 33459', '+18166686811', '+14722694145')
    ;
    """
cursor.execute(query_outlet_tuples)
print(pd.read_sql_query("SELECT * FROM Outlet", db_connect))

query_vehicle_tuples = """
    INSERT OR IGNORE INTO Vehicle(registrationNo, model, make, engineSize, capacity, mileage, dailyHireRate, outletNo)
    VALUES
        ('72B-NK4', 'Camry', 'Toyota', 2.5, 5, 12450, 55.00, 1),
        ('XJ9-12Q', 'Escalade', 'Cadillac', 6.2, 7, 8200, 150.00, 2),
        ('401-WVZ', 'Model 3', 'Tesla', 0.5, 5, 5100, 95.00, 3),
        ('MK5-928', 'Pacificca', 'Chrysler', 3.6, 8, 34200, 75.00, 4),
        ('821-YPX', 'Versa', 'Nissan', 1.6, 5, 42100, 35.00, 5)
    ;
    """
cursor.execute(query_vehicle_tuples)
print(pd.read_sql_query("SELECT * FROM Vehicle", db_connect))

query_client_tuples = """
    INSERT OR IGNORE INTO Client(clientNo, fName, lName, address, phone, DOB, licenseNo)
    VALUES
        (1, 'Cosimo', 'Medici', '1400 Biscayne Blvd, Miami, FL 33132', '+13055550101', '1985-06-15', 'FL-MED-8506'),
        (2, 'Lorenzo', 'Magnifico', '405 Ocean Dr, Miami Beach, FL 33139', '+17865550202', '1990-01-01', 'FL-MAG-9001'),
        (3, 'Clarice', 'Orsini', '2201 Collins Ave, Miami Beach, FL 33139', '+13055550303', '1992-11-12', 'FL-ORS-9211'),
        (4, 'Giuliano', 'Sforza', '175 SE 25th Rd, Miami, FL 33129', '+17865550404', '1988-03-24', 'FL-SFO-8803'),
        (5, 'Lucrezia', 'Tornabuoni', '9821 Arvida Dr, Coral Gables, FL 33156', '+13055550505', '1975-09-30', 'FL-TOR-7509')
    ;
    """
cursor.execute(query_client_tuples)
print(pd.read_sql_query("SELECT * FROM Client", db_connect))
db_connect.commit()

query_hireAgreement_tuples = """
    INSERT OR IGNORE INTO HireAgreement(hireNo, agreementStart, agreementEnd, startingMileage, endingMileage, clientNo, registrationNo)
    VALUES
        (1, '2026-02-01', '2026-05-10', 12450, 12600, 1, '72B-NK4'),
        (2, '2026-02-02', '2026-05-15', 8200, 8450, 2, 'XJ9-12Q'),
        (3, '2026-02-03', '2026-05-08', 5100, 5200, 3, '401-WVZ'),
        (4, '2026-02-28', '2026-05-20', 34200, 34800, 4, 'MK5-928'),
        (5, '2026-02-16', '2026-05-05', 42100, 42250, 5, '821-YPX')
    ;
    """
cursor.execute(query_hireAgreement_tuples)
print(pd.read_sql_query("SELECT * FROM HireAgreement", db_connect))

query_staff_tuples = """
    INSERT OR IGNORE INTO Staff(staffNo, fName, lName, address, phone, DOB, sex, outletNo)
    VALUES
        (1, 'Ricardo', 'Santos', '882 SW 10th St, Miami, FL 33130', '+13055551010', '1980-04-12', 'M', 1),
        (2, 'Elena', 'Vargas', '1200 West Ave, Miami Beach, FL 33139', '+17865552020', '1992-08-25', 'F', 2),
        (3, 'Marcus', 'Jordan', '450 NE 24th St, Miami, FL 33137', '+13055553030', '1985-11-03', 'M', 3),
        (4, 'Sofia', 'Castillo', '2901 Tiburon Way, Coral Gables, FL 33134', '+17865554040', '1995-01-15', 'F', 4),
        (5, 'David', 'Chen', '1541 Brickell Ave, Miami, FL 33129', '+13055555050', '1978-12-20', 'M', 5)
    ;
    """
cursor.execute(query_staff_tuples)
print(pd.read_sql_query("SELECT * FROM Staff", db_connect))

# Save changes
db_connect.commit()

query_1 = """
SELECT c.fName, c.lName, h.registrationNo, v.make, v.model, 
o.address, o.phone
FROM Client c, HireAgreement h, Vehicle v, Outlet o
WHERE c.clientNo = h.clientNo
AND h.registrationNo = v.registrationNo
AND v.outletNo = o.outletNo
AND AgreementStart BETWEEN '2026-02-01' AND '2026-02-28'
;
"""

cursor.execute(query_1)
query_1_report = pd.read_sql_query(query_1, db_connect)
print(query_1_report)

query_2 = """
SELECT COUNT(s.staffNo)
FROM Staff s, Outlet o, Vehicle v, HireAgreement h
WHERE s.outletNo = o.outletNo
AND o.outletNo = v.outletNo
AND h.registrationNo = v.registrationNo
AND agreementStart = (SELECT MIN(agreementStart) 
    FROM HireAgreement
    WHERE AgreementStart BETWEEN '2026-02-01' AND '2026-02-28')
;
"""

cursor.execute(query_2)
query_2_report = pd.read_sql_query(query_2, db_connect)
print(query_2_report)

query_3 = """
SELECT s.fName, s.lName
FROM Staff s, Outlet o, Vehicle v, HireAgreement h
WHERE s.outletNo = o.outletNo
AND o.outletNo = v.outletNo
AND h.registrationNo = v.registrationNo
AND s.DOB = (SELECT MIN(DOB)
    FROM Staff)
AND endingMileage = (SELECT MAX(endingMileage) 
    FROM HireAgreement
    WHERE AgreementStart BETWEEN '2026-02-01' AND '2026-02-28')
;
"""

query_4 = """
SELECT c.DOB, c.licenseNo
FROM Client c
INNER JOIN HireAgreement h ON c.clientNo = h.clientNo
INNER JOIN Vehicle v ON h.registrationNo = v.registrationNo
INNER JOIN Outlet o ON v.outletNo = o.outletNo
WHERE h.AgreementStart BETWEEN '2020-01-01' AND CURRENT_DATE
GROUP BY c.clientNo, c.DOB, c.licenseNo
ORDER BY COUNT(DISTINCT v.outletNo) DESC
LIMIT 1
;
"""

cursor.execute(query_4)
query_4_report = pd.read_sql_query(query_4, db_connect)
print(query_4_report)

cursor.execute(query_3)
query_3_report = pd.read_sql_query(query_3, db_connect)
print(query_3_report)

query_5_1 = """
SELECT AVG(agreements)
FROM (SELECT COUNT(h.hireNo) AS agreements
    FROM Client c, Outlet o, Vehicle v, HireAgreement h
    WHERE c.clientNo = h.clientNo
    AND o.outletNo = v.outletNo
    AND h.registrationNo = v.registrationNo
    AND h.AgreementStart BETWEEN '2020-01-01' AND CURRENT_DATE
    AND (o.address LIKE '%Florida%' OR o.address LIKE '%FL%')
    GROUP BY v.registrationNo)
;
"""

cursor.execute(query_5_1)
query_5_1_report = pd.read_sql_query(query_5_1, db_connect)
print(query_5_1_report)

query_5_2 = """
SELECT AVG(agreements)
FROM (SELECT COUNT(h.hireNo) AS agreements
    FROM Client c, Outlet o, Vehicle v, HireAgreement h
    WHERE c.clientNo = h.clientNo
    AND o.outletNo = v.outletNo
    AND h.registrationNo = v.registrationNo
    AND h.AgreementStart BETWEEN '2020-01-01' AND CURRENT_DATE
    AND (o.address LIKE '%Florida%' OR o.address LIKE '%FL%')
    GROUP BY c.clientNo)
;
"""

cursor.execute(query_5_2)
query_5_2_report = pd.read_sql_query(query_5_2, db_connect)
print(query_5_2_report)

# Close connection
db_connect.close()