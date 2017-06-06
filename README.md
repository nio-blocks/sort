Sort
=============
A block for sorting a list of incoming signals.

Properties
-------------
* **sort_key**: specifies the value by which signals should be sorted by
* **reverse**: boolean value on whether to reverse the specified sort order
* **limit**: limit on the number of notified signals

Dependencies
-------------
None

Commands
-------------
None

Input
-------------
Any list of signals.

Output
-------------
Sorted list of signals.

Example 1 - Input Signal
-------------
```
[
  { 'val': 3 },
  { 'val': 1 },
  { 'val': 2 }
]
```

Example 1 - Block Config
-------------
```
'sort_by': '{{ $val }}'
```

Example 1 - Output Signal
-------------
```
[
  { 'val': 1 },
  { 'val': 2 },
  { 'val': 3 }
]
```

Example 2 - Input Signal
-------------
```
[
  { 'val': 3 },
  { 'val': 1 },
  { 'val': 2 }
]
```

Example 2 - Block Config
-------------
```
'sort_by': '{{ $val }}',
           'limit': 2
```
            
            
Example 2 - Output Signal
-------------
```
[
  { 'val': 1 },
  { 'val': 2 }
]
```
