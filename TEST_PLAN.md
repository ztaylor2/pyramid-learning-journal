# Plan for Testing

***

### What to Test
- Test views
  - Test each view returns response
  - Test each view return 200 OK
    - Update this to returns dict 
  - Test each view returns propper content
    - Update to returns propper number of templates
  - Test views return correct keys
  - After addition of DB test if num templates is equal to query count
  - Test view is empty when DB is emtpy 
- Test database
  - Create test database configuration fixture
  - Create a test database session fixture
  - Create a dummy request fixture
  - Test if we add one model to test DB that there is one model in test DB
  - Use faker to create fake models for test DB
  - Create fixture for adding those models
  - Add database info to test app fixture
  - Send query to test database and see if it exists
  - Send query to test database for specific entry
- Functional tests
  - Create fixture for app for testing
  - Use it to check if views have correct html in them
  - Check home view returns correct number of entires 
