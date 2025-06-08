
---
# Julep City Fun Facts Workflow

This workflow takes a list of city names as input and returns fun “Did you know?” style facts about each city, using Wikipedia as the source.

### How it works:

1. **Search Wikipedia:** For each city, it fetches a summary from Wikipedia.
2. **Extract facts:** It reads each city summary and pulls out three interesting and surprising facts.
3. **Pair data:** It pairs each city with its extracted facts.
4. **Format paragraphs:** It creates the “Did you know about \[City]?” followed by the facts.
5. **Combine output:** It joins all city paragraphs into a single final message for easy reading.

---

This makes it super simple to get cool facts about any list of cities you provide!


## How to Use

1. Open the Python notebook (`julep_city_facts.ipynb`).
2. Run the notebook cells.
3. input your list of city names as an array (in the first line maybe, or on the later cell where locations are defined), for example:
   ```python
   ["New York", "London", "Paris"]


Future updates: will add a Reddit feature to find really quirky facts lol