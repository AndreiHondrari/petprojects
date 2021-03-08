# Search procedures comparison

## Overview

Typically when you search over a set of data items, for sets that are rather small in size the search is very fast, but as the size of the collection grows substantially the performance of the search starts to be affected.

The search performance varies depending on a number of factors:
- the data structure that keeps the collection
- the grade of order in the collection
- the type of information being searched
- the combination of algorithms used in a search procedure and the order of their usage


## Types of search procedures
- linear search
- divide et impera
- indexed

## Search procedures details

### 1. Linear Search

It simply consists of an iteration over the collection, while comparing the target value against the iterated elements.

In a linear search the order of the items matter only if the target values are very close in value and the search starts from a point close to these values as well.

### 2. Divide et impera

It is based on the recursivity property of functions, and at every node in the call stack the set is split into to and the search function is appled on each half individually. Only when hitting a leaf with a single value will the call be returned to the superior node.

This type of search works only for sorted collections, as to why the set of items in the collection is halved at each recursion level.

### 3. Indexed

In this search mode, the collection is passed to a pre-processing algorithm that will generate a sort of unique identification value for each item in the collection which will map directly to its position in the collection.

The way the search is performed is by generating the unique value for the target value and trying to extract it directly from the index dictionary that has a O(1) access time. That reduces the search time considerably, but the catch is that it takes time to generate the index.

## Conclusion

Depending on the size of the collection you might choose
- linear searching for small collections (search time:  hundreds of milliseconds for 150k items)
- divide et impera for medium-sized collections (search time: reduced to more than 50% of the linear search, for 150k items)
- indexed for large and very large collections (search time: in the order of tens of microseconds for 150k item)

## Drawbacks

- for divide et impera you always have to sort the values when inserting
- for indexing you always have to generate the unique value. Sometimes you might have collisions as to why two different input values might generate the same unique value (due to the nature of the algorithm used to generate that value). In a case of a collision one must simply create lists for mapping unique values and then perform a linear search against these lists. Typically collisions should be rare and the performance impact is minimalistic
