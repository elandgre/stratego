# stratego
an AI to play stratego

## Dependencies:
- pytest
- numpy

## Running
The lazy way:
- `make frontend` will run the frontend
- `make` or `make stratego` will run the backend
- `make test` will run all the tests
- `make tournement` will run the trournement of all the AIs
- `make train<AI NAME>` will run the training for an AI
- `make clean` will delete all the .pyc files

The python way:
- just the backend
`python game/play.py`

- just the tests
`python -m pytest`

## Testing
- Whats the current testing framwork to test?
  - pytest[https://docs.pytest.org/en/latest/getting-started.html]

- how do I add a new script of tests?
  - add a new file in the tests directory and name it "test_<what your testing here>.py"
     - note: the name must start with test
 
- how do I add a test to one of the testing scripts?
  - add a function named "test_<what I want to test>"
    - note0 : the function name must start with test or _test
    - note1 : you can put other funcitons in the test scripts, but they will not be run unless called by a function that starts with test
    - note2 : you can print in testing functions, but it will not be writen to stdout unless the test fails
    - note3 : a test fails on any error
  
- how do I run my new tests?
  - as long as you stick to the naming guidlines above the test should be automatically run with the others, so just run `make test` like normal
