# This is growth CLI App Documentation 

Python CLI App 😻 for tracking user Activity Growth ![plot](https://user-images.githubusercontent.com/97686098/160928246-46b29292-5c99-4d89-b294-6efb3354ac7f.png)

## Project Setup

### 1. Install Dependencies 

```bash
pip install requirements.txt
```

### 2. Run project

```bash
python3 main.py [START DATE] [End Date]

# or

python main.py [START DATE] [End Date]

# valid example 

python3 main.py 02-01-2022 08-01-2022

```

#### 2.1 Invalid input
in case you pass an invalid date arguments or ones that are not in the json object you should get an empty plot.png that will be updated on the project folder

### 3. Run Tests (Unit test + Network test are in the same file, you can check the logic)

```bash
python3 test_main.py

#or

python test_main.py

```

```bash
...
----------------------------------------------------------------------
Ran 3 tests in 0.698s

OK

```

