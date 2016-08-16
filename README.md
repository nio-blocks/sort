# Sort
A block for sorting a list of incoming signals.

## Properties
* **Sort Key**: specifies the value by which signals should be sorted by
* **Reverse**: boolean value on whether to reverse the specified sort order
* **Limit**: limit on the number of notified signals

## Dependencies
None

## Commands
None

## Input
Any list of signals.

## Output
Sorted list of signals.

#### Input Signal
```
[
  { 'val': 3 },
  { 'val': 1 },
  { 'val': 2 }
]
```

#### Block Config
```
'sort_by': '{{ $val }}'
```

#### Output Signal
```
[
  { 'val': 1 },
  { 'val': 2 },
  { 'val': 3 }
]
```

## More Examples

#### Input Signal
```
[
  { 'val': 3 },
  { 'val': 1 },
  { 'val': 2 }
]
```

#### Block Config
```
'sort_by': '{{ $val }}',
           'limit': 2
```
            
            
#### Output Signal
```
[
  { 'val': 1 },
  { 'val': 2 }
]
```
