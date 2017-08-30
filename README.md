Sort
====
Sort a list of incoming signals.

Properties
----------
- **limit**: Limit the number of included ouput signals for each list of input signals.
- **reverse**: Sort in revers order.
- **sort_by**: The value used for sorting on each signal.

Inputs
------
- **default**: Any list of signals.

Outputs
-------
- **default**: Sorted list of signals.

Commands
--------
None

Dependencies
------------
None

Example 1
---------
Block Config
```
'sort_by': '{{ $val }}'
```
Input Signal
```
[
  { 'val': 3 },
  { 'val': 1 },
  { 'val': 2 }
]
```
Output Signal
```
[
  { 'val': 1 },
  { 'val': 2 },
  { 'val': 3 }
]
```

Example 2
---------
Block Config
```
'sort_by': '{{ $val }}',
           'limit': 2
```
Input Signal
```
[
  { 'val': 3 },
  { 'val': 1 },
  { 'val': 2 }
]
```
Output Signal
```
[
  { 'val': 1 },
  { 'val': 2 }
]
```

