## Fetch take home exercise

### Running with docker
- `docker-compose up --build`

#### Tests
##### Unit tests
1. Run locally `pip install -r requirements.txt && pytest`
2. Run with docker `docker-compose run receipt_api pytest`

##### Integration tests
1. Make sure the application is running on port 8000 either through docker or
   directly.
2. Run `./integration_tests.sh`
