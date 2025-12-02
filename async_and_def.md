# Understanding Normal vs Async Functions in Python

## 1. What is a Normal (`def`) Function?

A **normal function** runs **synchronously**, meaning:

- Code executes line-by-line
- Each step waits until the previous one finishes
- Suitable for simple and fast operations

### Example (Normal Function)

```python
def greet():
    return "Hello"
```

### Execution Flow

```
Line 1 → finish → Line 2 → finish → next...
```

---

## 2. What is an Async (`async def`) Function?

An **async function** is used for **asynchronous programming**.

It allows your program to:

- Not wait for slow operations (API calls, database queries, file I/O)
- Continue running other tasks while waiting

### Syntax

```python
async def function_name():
    await some_async_operation()
```

### Example (Async Function)

```python
import asyncio

async def get_data():
    await asyncio.sleep(2)
    return "Data fetched"
```

### Execution Flow

```
Start → hit await → give control → resume later
```

---

## Simple Difference (Best for Interviews)

| Feature         | Normal Function (`def`) | Async Function (`async def`) |
|-----------------|--------------------------|-------------------------------|
| Execution       | Synchronous               | Asynchronous                  |
| Blocking        | Yes                       | No                            |
| Use Case        | Fast calculations         | API calls, DB queries, I/O    |
| Keyword         | `def`                     | `async def` + `await`         |
| Speed           | Slower for I/O tasks      | Faster for concurrent tasks   |

---

## Real Example to Understand

### Normal Function (Blocking)

```python
import time

def run():
    time.sleep(3)
    return "Done"

print(run())
print("Next work")
```

Output (after 3 seconds delay):

```
Done
Next work
```

---

### Async Function (Non-Blocking)

```python
import asyncio

async def run():
    await asyncio.sleep(3)
    return "Done"

async def main():
    task = asyncio.create_task(run())
    print("Next work immediately")
    print(await task)

asyncio.run(main())

```

Output:

```
Next work immediately
Done
```

The async version does not block the program and continues with other tasks.

---

