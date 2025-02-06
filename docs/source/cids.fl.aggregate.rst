Aggregation Algorithm
==========================

.. _cids.fl.aggregate:

The default method for aggregation algorithm in this simulator is ``Federated Averaging (FedAvg)``. You can modify the aggregation algorithm in the simulator by modify this code:

.. code-block:: python
   
   #Modify this code to change FedAvg with other aggregation algorithm or you can invent your own aggregation algorithm
   new_weights = [np.mean([weight[layer] for weight in local_weights], axis=0) for layer in range(len(global_weights))]


You can also refer other aggregation algorithm concept from list of research below:
1. https://www.sciencedirect.com/science/article/pii/S0167739X23003333
2. 
