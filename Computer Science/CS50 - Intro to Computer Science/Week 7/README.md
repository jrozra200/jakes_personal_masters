# Week 7 - SQL

## Notes

- csv files are flat file databases
- using `set()` in python: `.add()` instead of `.append()` (which is for a list 
`[]`)
- `sorted()` will organize the list/dictionary in alphabetical order
    - `sorted(, reverse = True)` to do it in reverse alphabetical order
    - `sorted(, key = get_value)` to do it by key (where `get_value`) is a 
    function that returns the value given the key
        - `sorted(, key = lambda title: titles[title])` creates a lambda 
        function that does the same thing as the previous line
- SQL index lets you do better than linear search - does "something" with data 
structures to speed things up
    - Relational databases often uses a B tree (not binary) - very wide and 
    shallow tree
- SQL Injection Attacks: When you don't sanitize your "inputs," you can 
accidentally (or intentionally) alter the SQL code
- Race conditions: when code is run "efficiently" and there are conflicts due 
to multiple users doing the same action at the same time