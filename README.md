# DUMMY_SVC

This project is a basic discount code generate and assign service
which can be used as a template for Docker compose - Django - Postgresql - PyTest implementations

---

## Useful Commands

- **Make build** >> to build docker compose
- **Make test** >> to run test cases (pytest)
- **Make start** >> to start and detach docker compose
- **Make stop** >> to stop docker compose
- **Make status** >> to check status of docker containers
- **Make clean** >> to clear up docker images
- **Make showmigrations** >> to check created Django migrations
- **Make makemigrations** >> to create new Django migrations if changes made
- **Make migrate** >> to make migrations did not make yet

---

### Api Docs

- **URL:** \
  /discount_code/brand/<int:brand_id>/<int:campaign_id>/
  - **Method:** \
    `POST`
- **URL Params:**

  **Required:** `brand_id=[integer]`, `campaign_id=[integer]`

- **Data Params:**

  - `discount_type=[char]` required (choice "P" for percentile and "F" for fixed amount)
  - `discount_amount=[decimal]` required
  - `expire_date=[date_time]` required
  - `code_count=[integer]` required

- **Data Example:**
  ```json
  {
    "discount_type": "P",
    "discount_amount": 20.0,
    "expire_date": "2022-01-31 00:00:00",
    "code_count": 200
  }
  ```
- **Success Response:**

  - **Code:** 201 <br />
    **Content:**
    ```json
    {
      "status": "success",
      "data": {
        "brand_id": 1,
        "campaign_id": 1,
        "created_code_number": 200
      }
    }
    ```
  - **Error Response:**
    - **Code:** 404 NOT FOUND <br />

---

- **URL:** \
  /customer/<int:customer_id>/<int:campaign_id>/
- **Method:** \
  `GET`
- **URL Params:**

  **Required:** `customer_id=[integer]`, `campaign_id=[integer]`

- **Success Response:**

  - **Code:** 200 <br />
    **Content:**
    ```json
    {
      "status": "success",
      "data": {
        "code": "103905416153051153966222658313242377225439189869384833454241926656591129727117",
        "expire_date": "2022-01-31T00:00:00"
      }
    }
    ```
  - **Error Response:**
    - **Code:** 404 NOT FOUND <br />