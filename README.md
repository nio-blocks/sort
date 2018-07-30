Sort
====
The Sort block orders a list of incoming signals based on the attribute configured in the **sort key** property.

Properties
----------
- **limit**: Limit the length of the the emitted signal list after sorting. If the incoming list is longer than the limit, all items after the limit length will be discarded.
- **reverse**: If true (checked) the list will be sorted in reverse order.
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

