# MapReduce-Implementation

This repository talks about the map reduce implementation done with the help of hadoop in python.

* MapReduce consists of two distinct tasks – Map and Reduce.
* As the name MapReduce suggests, the reducer phase takes place after the mapper phase has been completed.
* So, the first is the map job, where a block of data is read and processed to produce key-value pairs as intermediate outputs.
* The output of a Mapper or map job (key-value pairs) is input to the Reducer.
* The reducer receives the key-value pair from multiple map jobs.
* Then, the reducer aggregates those intermediate data tuples (intermediate key-value pair) into a smaller set of tuples or key-value pairs which is the final output.
