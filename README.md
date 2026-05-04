Case Study: Reliable Rentals

A company called Reliable Rentals rents out vehicles at different outlets (locations/sites). Each outlet has a number, address, phone number and a fax number. Each site is allocated a stock of vehicles for hire. The registration number uniquely identifies each vehicle for hire and is used when hiring a vehicle to a client.

Clients may hire vehicles for various periods of time. Each individual hire agreement between a client and the Company is uniquely identified using a hire number. Information stored on the vehicles for hire include: the vehicle registration number, model, make, engine size, capacity, current mileage, daily hire rate, and the current location (outlet) of each vehicle. The data stored on clients includes the client number (unique identifier), name (first and last name), home address, phone number, date of birth, and driving license number.

The data stored on a hire agreement includes the hire number, the client’s number, name, address, and phone number, date the client started the hire period, date the client wishes to terminate the hire period, the vehicle registration number, model and make, the mileage before and after the hire period. Finally, information is stored on the staff based at various outlets including: staff number, name (first and last name), home address, home phone number, date of birth (DOB), sex, date joined the Company, job title, and salary. Each staff member is associated with a single outlet.

1. Develop a conceptual data model reflecting the following requirements:

A. Identify the main entities.

B. Identify the main relationships between the entities identified in "a".

C. Determine the multiplicity constraints for each relationship identified in "b".

D. Identify attributes and associate them with entities or relationships.

E. Determine candidate and primary key attributes for each (strong) entity.

F. Generate the E-R diagram for the conceptual level (no FKs as attributes).

2. Develop a logical data model reflecting the following requirements:

A. Derive relations (and FKs) from the conceptual model.
    
  Include the relational schema (e.g.: Staff(staffID, fName, lName, position, salary)).

B. Validate the logical model using normalization to 3NF.

C. Validate the logical model against 5 user transactions. (Note: These will be then implemented in 3c.)
  
  You must include the query (question) in plain English.

  The majority of queries (questions) should involve more than one entity.

  You must explain verbally what steps you follow using the relationships between the entities (no code!).

D. Define integrity constraints:

  Primary key constraints.

  Referential integrity/Foreign key constraints.

  Alternate key constraints (if any).

  Required data.

  Attribute domain constraints.

  General constraints (if any).

E. Generate the E-R diagram for the logical level (contains FKs as attributes).

3. Implement the database using embedded SQL (Python and SQLite as in the assignment).

A. Develop SQL code to create the entire database schema, reflecting the constraints identified in previous steps.

B. Create at least 5 tuples for each relation in your database.

C. Develop the 5 SQL queries that correspond to Part 2.C using embedded SQL.

D. Upload all the code and documentation (including previous project submissions) to GitHub.
