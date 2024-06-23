# Python - Object-Relational Mapping

This repository contains a series of Python scripts and modules that demonstrate object-relational mapping (ORM) concepts and techniques. Each script connects to a MySQL database, performs various database operations, and outputs results as specified. Below is a description of each task and its corresponding file.

## Tasks

### 0. Get all states
Write a script that lists all states from the database `hbtn_0e_0_usa`.
- The script takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the MySQLdb module to connect to a MySQL server running on localhost at port 3306.
- Results are sorted in ascending order by `states.id`.

**File**: `0-select_states.py`

### 1. Filter states
Write a script that lists all states with a name starting with `N` (upper N) from the database `hbtn_0e_0_usa`.
- The script takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the MySQLdb module to connect to a MySQL server running on localhost at port 3306.
- Results are sorted in ascending order by `states.id`.

**File**: `1-filter_states.py`

### 2. Filter states by user input
Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.
- The script takes 4 arguments: MySQL username, MySQL password, database name, and state name searched.
- Uses the MySQLdb module to connect to a MySQL server running on localhost at port 3306.
- Results are sorted in ascending order by `states.id`.

**File**: `2-my_filter_states.py`

### 3. SQL Injection...
Write a script that takes in arguments and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument. The script must be safe from MySQL injections.
- The script takes 4 arguments: MySQL username, MySQL password, database name, and state name searched.
- Uses the MySQLdb module to connect to a MySQL server running on localhost at port 3306.
- Results are sorted in ascending order by `states.id`.

**File**: `3-my_safe_filter_states.py`

### 4. Cities by states
Write a script that lists all cities from the database `hbtn_0e_4_usa`.
- The script takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the MySQLdb module to connect to a MySQL server running on localhost at port 3306.
- Results are sorted in ascending order by `cities.id`.

**File**: `4-cities_by_state.py`

### 5. All cities by state
Write a script that takes in the name of a state as an argument and lists all cities of that state, using the database `hbtn_0e_4_usa`.
- The script takes 4 arguments: MySQL username, MySQL password, database name, and state name.
- Uses the MySQLdb module to connect to a MySQL server running on localhost at port 3306.
- Results are sorted in ascending order by `cities.id`.

**File**: `5-filter_cities.py`

### 6. First state model
Write a Python file that contains the class definition of a State and an instance `Base = declarative_base()`.
- The State class:
  - Inherits from Base.
  - Links to the MySQL table `states`.
  - Has class attributes `id` (auto-generated, unique integer, primary key) and `name` (string with maximum 128 characters).
- Uses the SQLAlchemy module.
- Connects to a MySQL server running on localhost at port 3306.

**File**: `model_state.py`

### 7. All states via SQLAlchemy
Write a script that lists all State objects from the database `hbtn_0e_6_usa`.
- The script takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the SQLAlchemy module.
- Imports State and Base from `model_state`.
- Connects to a MySQL server running on localhost at port 3306.
- Results are sorted in ascending order by `states.id`.

**File**: `7-model_state_fetch_all.py`

### 8. First state
Write a script that prints the first State object from the database `hbtn_0e_6_usa`.
- The script takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the SQLAlchemy module.
- Imports State and Base from `model_state`.
- Connects to a MySQL server running on localhost at port 3306.
- Displays the state with the lowest `states.id`. If the table is empty, prints `Nothing`.

**File**: `8-model_state_fetch_first.py`

### 9. Contains `a`
Write a script that lists all State objects that contain the letter `a` from the database `hbtn_0e_6_usa`.
- The script takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the SQLAlchemy module.
- Imports State and Base from `model_state`.
- Connects to a MySQL server running on localhost at port 3306.
- Results are sorted in ascending order by `states.id`.

**File**: `9-model_state_filter_a.py`

### 10. Get a state
Write a script that prints the State object with the name passed as argument from the database `hbtn_0e_6_usa`.
- The script takes 4 arguments: MySQL username, MySQL password, database name, and state name to search.
- Uses the SQLAlchemy module.
- Imports State and Base from `model_state`.
- Connects to a MySQL server running on localhost at port 3306.
- Displays the `states.id` of the matching state. If no state matches, prints `Not found`.

**File**: `10-model_state_my_get.py`

### 11. Add a new state
Write a script that adds the State object “Louisiana” to the database `hbtn_0e_6_usa`.
- The script takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the SQLAlchemy module.
- Imports State and Base from `model_state`.
- Connects to a MySQL server running on localhost at port 3306.
- Prints the new `states.id` after creation.

**File**: `11-model_state_insert.py`

### 12. Update a state
Write a script that changes the name of a State object from the database `hbtn_0e_6_usa`.
- The script takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the SQLAlchemy module.
- Imports State and Base from `model_state`.
- Connects to a MySQL server running on localhost at port 3306.
- Changes the name of the State where `id` is 2 to "New Mexico".

**File**: `12-model_state_update_id_2.py`

### 13. Delete states
Write a script that deletes all State objects with a name containing the letter `a` from the database `hbtn_0e_6_usa`.
- The script takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the SQLAlchemy module.
- Imports State and Base from `model_state`.
- Connects to a MySQL server running on localhost at port 3306.

**File**: `13-model_state_delete_a.py`

### 14. Cities in state
Write a Python file similar to `model_state.py` named `model_city.py` that contains the class definition of a City.
- The City class:
  - Inherits from Base (imported from `model_state`).
  - Links to the MySQL table `cities`.
  - Has class attributes `id` (auto-generated, unique integer, primary key), `name` (string of 128 characters), and `state_id` (integer, foreign key to `states.id`).
- Uses the SQLAlchemy module.
  
Write a script that prints all City objects from the database `hbtn_0e_14_usa`.
- The script takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the SQLAlchemy module.
- Imports State and Base from `model_state`.
- Connects to a MySQL server running on localhost at port 3306.
- Results are sorted in ascending order by `cities.id`.

**Files**: `model_city.py`, `14-model_city_fetch_by_state.py`

### 15. City relationship
Improve the files `model_city.py` and `model_state.py`, and save them as `relationship_city.py` and `relationship_state.py`.
- The City class remains unchanged.
- The State class:
  - Adds a class attribute `cities` representing a relationship with the City class.
  - If a State object is deleted, all linked City objects are also deleted.
  - The reference from a City object to its State is named `state`.
- Uses the SQLAlchemy module.
  
Write a script that creates the State “California” with the City “San Francisco” in the database `hbtn_0e_100_usa`.
- The script takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the SQLAlchemy module.
- Connects to a MySQL server running on localhost at port 3306.
-

 Uses the `cities` relationship for all State objects.

**Files**: `relationship_city.py`, `relationship_state.py`, `100-relationship_states_cities.py`

### 16. List relationship
Write a script that lists all State objects and corresponding City objects from the database `hbtn_0e_101_usa`.
- The script takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the SQLAlchemy module.
- Connects to a MySQL server running on localhost at port 3306.
- Uses one query to the database.
- Uses the `cities` relationship for all State objects.
- Results are sorted in ascending order by `states.id` and `cities.id`.

**File**: `101-relationship_states_cities_list.py`

### 17. From city
Write a script that lists all City objects from the database `hbtn_0e_101_usa`.
- The script takes 3 arguments: MySQL username, MySQL password, and database name.
- Uses the SQLAlchemy module.
- Connects to a MySQL server running on localhost at port 3306.
- Uses one query to the database.
- Uses the `state` relationship to access the State object linked to the City object.
- Results are sorted in ascending order by `cities.id`.

**File**: `102-relationship_cities_states_list.py`
