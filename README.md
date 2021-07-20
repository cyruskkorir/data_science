## Jacaranda Health

- This API service posts data to mongodb, retrieves data from from database and updates records in db

-**Disclaimer**: The project was built in windows enviroment

## Getting started

- clone the repo: `https://github.com/cyruskkorir/data_science.git`
- `cd` root directory
- Create `.env` file and add variables as shown in `env.sample` file
- Connect the flask App to MongoDb using `MONGO_URI`
- create and activate virtualenv:
  - In windows:
    - `virtualenv <env name>`
    - `<env name>\Scripts\activate`
  - In linux / mac:
    - `python -m venv <env name>`
    - `source <env name>\bin\activate`
- Run `pip -r install requirements.txt` to install all app dependencies
- Run the development server: `python run.py`
- Test the API endpoints in postman
