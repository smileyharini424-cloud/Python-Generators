# Python Generators

## Explanation

A generator is a special type of function that produces values one at a time using the `yield` keyword. Unlike a normal function that returns all results at once, a generator produces values only when requested.

## Problem Statement

Write a Python program using a generator function to generate numbers from 1 to a given limit one at a time.

## Features

* Demonstrates generator functions
* Uses the `yield` keyword
* Generates values one at a time
* Uses a `for` loop to access generated values
* Demonstrates memory-efficient processing

## How It Works

1. The user enters a limit.
2. The generator function starts from 1.
3. The `yield` keyword produces one number at a time.
4. The function pauses after each `yield`.
5. The next iteration resumes the generator from where it stopped.

## Technologies Used

* Python 3
* Generator Functions
* `yield`

## Program Flow

Start → Get Limit → Create Generator → Generate Values Using `yield` → Display Values → End

## Sample Input

```text id="n5qv6j"
Enter the limit: 5
```

## Sample Output

```text id="gq7b2m"
Generated Numbers:
1
2
3
4
5
```

## Key Learning

* Generators use the `yield` keyword.
* A generator produces values one at a time.
* Generators pause and resume execution.
* They are useful for processing large amounts of data efficiently.

## File Location

```text id="8z0p3x"
Python-Generators/generators.py
```

## Repository Structure

```text id="x5j8ks"
Python-Generators/
│
├── generators.py
└── README.md
```

## Author

V.Harini
