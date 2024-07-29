# BlockfuseLabs-Test
Blockfuse Labs Cohort One Test

## How to Run Each Section Project Locally

## SECTION A: Number 1
### Prerequisites

Make sure you have the following installed on your machine:

- Python 3.x

### Installation

1. **Clone the Repository**

   First, clone the repository to your local machine using git:

   ```bash
   git clone https://github.com/Cyberking99/BlockfuseLabs-Test.git
   ```

2. **Navigate to the Project Directory**

   Change your current directory to the project directory:

   ```bash
   cd BlockfuseLabs-Test/Section-A
   ```

### Running the Project

To run the project, use the following command:

```bash
python section-a-1.py
```

## SECTION B: Number 1
### Prerequisites

Make sure you have the following installed on your machine:

- PHP
- MySQL
- Composer

**NOTE:** *I am using XAMPP as my server*

### Installation

1. **Clone the Repository**

   First, clone the repository to your local machine using git:

   ```bash
   git clone https://github.com/Cyberking99/BlockfuseLabs-Test.git
   ```

2. **Navigate to the Project Directory**

   Change your current directory to the project directory:

   ```bash
   cd BlockfuseLabs-Test/Section-B
   ```

3. **Install Dependencies**

   Run the composer install command to install the dependencies:

   ```bash
   composer install
   ```

4. **Setup Environment Variable (for database)**
   You can rename the .env.example file to .env or run this command:

   ```bash
   cp .env.example .env
   ```

5. **Replace Database (MySQL) Details**

   Update the .env file with your local environment settings:

   *DB_CONNECTION*: The type of database you're using (e.g., mysql, pgsql).
   *DB_HOST*: The host of your database (usually 127.0.0.1).
   *DB_PORT*: The port your database is running on (default for MySQL is 3306).
   *DB_DATABASE*: The name of your database.
   *DB_USERNAME*: Your database username.
   *DB_PASSWORD*: Your database password.

   **Example:**
   DB_CONNECTION=mysql
   DB_HOST=127.0.0.1
   DB_PORT=3306
   DB_DATABASE=blockfuselabs_library
   DB_USERNAME=root
   DB_PASSWORD=

6. **Run Migration**
   
   ```bash
   php artisan migrate
   ```

### Running the Project

To run the project, use the following command: