## Getting Started

This is my implementation for the exercise: Routing of telephone calls

## Installation

1. Install python: https://www.python.org/downloads/. I'm currently using 3.7.9 on my Windows machine.
2. Clone the repo
   ```sh
   git clone https://github.com/Sheldelraze/routing-of-telephone-calls
   ```
3. Install dependency library if needed (I only use `flake8` to check coding convention)
   ```python
   pip install -r requirements.txt
   ```

## Project structure
```
root/
│
├── libs/
│   ├── routing_service.py
│   ├── operator.py
│   ├── operator_repository.py
│   ├── trie.py
│   └── data_loader.py
│
├── tests/
│   ├── __init__.py
│   ├── test_routing_service.py
│   └── test_trie.py
│
├── operator_data/
│   ├── operator_a.txt
│   └── operator_b.txt
│
└── main.py
```

The main code lies in the `libs` folder, I tried to separate it into multiple classes so that each of them has a single responsibility which will make it easier to maintain and extend.

The input date is stored in the `data` folder, each `.txt` file in which represents an operator. The file name is also the name of the operator, each line in the files will contains 2 number: the phone number prefix and the corresponding price per minute (assuming all phone number should follow international convention and the pricing is a positive decimal), all the phone number prefix for each operator should be distinct as well (doesn't make sense if they don't)

## Usage

To run the sample:

```python
python main.py
```


To run the unittest:

```python
python -m unittest
```

## Further discussion

1. What is the time complexity of this implementation?

For this exercise, I'm using the data structure called [`Trie`](https://en.wikipedia.org/wiki/Trie) which has the complexity of creating is `O(M*N*L)` where `M` is the number of operator, `N` is the maximum number of prefix each operator has and `L` is the average length of all phone number, for querying the complexity is `O(L)` which has better scaling compare to the vanilla approach (checking every prefix and see if they match - `O(M*N*L)` again).


2. Regarding memory usage

The problem setter notes that all limitations (number of prefixes, maximum pricing,...) are within reason and the whole dataset can be fitted in memory so I won't focus too much on optimizing memory usage.

3. Data validation

This is not the main point of the problem so I'm just gonna skip it but if I have to I would probably use some 3rd party library such as `mashmallow`, `pydantic`,... to enforce data type and validator if needed

4. Data consistency - scaling

Again for this problem they said not to use any database so I'm just reading from file here and could not implement any data update method (unless we update the data and rerun the program again) but in case I do need to develop a solution for that (which can scale as well), I would probably store the whole dataset in an memory database (such as Redis,...) and have another thread to update it if needed.