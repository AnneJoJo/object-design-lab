
# 🧠 Python Algorithm Cheatsheet

Optimized for interviews, online assessments, and memory recall. No AI dependency, just pure structure + syntax clarity.

---

## 🔹 Core Data Structures (with usage patterns)

```python
# List comprehension
evens = [x for x in nums if x % 2 == 0]

# Set: deduplication + O(1) lookup
seen = set()
if x in seen: ...

# Dict: counting / grouping
from collections import defaultdict, Counter
freq = Counter(nums)
group = defaultdict(list)
for k, v in pairs:
    group[k].append(v)

# Stack
stack = []
stack.append(x)
val = stack.pop()

# Queue
from collections import deque
q = deque()
q.append(x)
q.popleft()

# Priority Queue (Min-Heap)
import heapq
heap = []
heapq.heappush(heap, val)
min_val = heapq.heappop(heap)
```

---

## 🔹 Commonly Forgotten Built-ins & Idioms

```python
# Sort by value or custom key
sorted(items)                  # ascending
sorted(items, reverse=True)    # descending
sorted(pairs, key=lambda x: x[1])  # by 2nd element

# String / list manipulations
" ".join(list_of_str)
s.split(",")
s.strip()
list(reversed(arr))   # reverse copy

# Enumerate with index
for i, val in enumerate(arr): ...

# Zip for transpose / parallel traversal
for a, b in zip(list1, list2): ...

# List flattening
flat = [x for row in grid for x in row]
```

---

## 🔹 Functions & Patterns

```python
# DFS template
def dfs(node, visited):
    if node in visited: return
    visited.add(node)
    for neighbor in graph[node]:
        dfs(neighbor, visited)

# BFS template
from collections import deque
def bfs(start):
    q = deque([start])
    visited = set([start])
    while q:
        node = q.popleft()
        for nei in graph[node]:
            if nei not in visited:
                visited.add(nei)
                q.append(nei)

# Sliding Window
left = 0
for right in range(len(arr)):
    while window_invalid():
        left += 1
    update_result()

# 2-pointer (sorted array)
i, j = 0, len(arr) - 1
while i < j:
    if arr[i] + arr[j] == target: ...
    elif arr[i] + arr[j] < target: i += 1
    else: j -= 1
```

---

## 🔹 Common Pitfalls to Avoid

| ❌ Mistake                        | ✅ Correction                            |
|----------------------------------|------------------------------------------|
| `for i in range(len(arr)): arr[i]` | Prefer `for x in arr:` unless index needed |
| `dict.get(k)` returns error       | Use `dict.get(k, default)`              |
| `if x in list:` (O(n))            | Use `if x in set()`                     |
| `for k, v in dict:`               | Use `dict.items()` for key-value pairs  |
| Modifying list during iteration   | Use `.copy()` or iterate over a slice   |

---

## 🔹 Input/Output Tips

```python
# Read input from string (for local testing)
data = """3
1 2 3
"""
lines = data.strip().split("\n")

# Read input from stdin
import sys
lines = sys.stdin.read().splitlines()

# Convert to int list
arr = list(map(int, lines[0].split()))
```
