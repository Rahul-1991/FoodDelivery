# FoodDelivery
This app provides api for fundamental search operations for the delivery trucks based on their location, applicants, expiry dates etc.
The api also provides privision for adding or deleting a truck from the delivery system.

##### Technology Stack
This project is powered by the **Django** web framework of python. 

##### Data Storage
The backend database is hosted on **MongoDb** which is a NoSQL database storing the information about the truck of the delivery system.

##### Data Population in mongoDB
```
python populate_data.py
```

##### Installing instructions
1. Creating Virtual Environment
    ```
    virtualenv venv
    ```
2. Start Virtual Environment
    ```
    source venv/bin/activate
    ```
3. Clone Repo
    ```
    https://github.com/Rahul-1991/FoodDelivery.git
    ```
4. Install dependencies
    ```
    cd FoodDelivery
    pip install -r requirements.txt
    ```
5. Run app
    ```
    python manage.py runserver
    ```

There may be some warnings which can be safely ignored.


##### List of APIs
* Search by name of applicant
    - url - /search/name
    - method - GET
    - params - applicantName (string)
* Search by expiration date, to find whose permits have expired
    - url - /search/expiredPermits
    - method - GET
* Add new food truck entry to the dataset
    - url - /truck/create
    - method - POST
    - params - {key: value}
* Delete new food truck entry to the dataset
    - url - /truck/create
    - method - POST
    - params - {key: value}
* Predict the best truck to assign the job based on location.
    - url - /assignTruck
    - method - POST
    - params - locations (list of locations)

#### Assumptions
For getting the list of trucks whose permit has expired it is assumed that the permit of the truck expires 7 days after its creation.


