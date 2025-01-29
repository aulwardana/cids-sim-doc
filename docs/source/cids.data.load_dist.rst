Load and Distribution of Data
==========================

.. _cids.data.load_dist:

This document explains the code and workflow in the provided Jupyter notebook for distributing non-IID data to clients in a Federated Learning scenario.

1. Function: `load_data(client_id)`
-----------------------------------

**Purpose**:  
Load a unique subset of data for a specific client in a Federated Learning setup, simulating non-IID data distribution.

**Code**:

.. code-block:: python

   def load_data(client_id):
       # Set seed for reproducibility based on client_id
       np.random.seed(client_id)
       indices = np.arange(len(X_df_scl))
       np.random.shuffle(indices)
       
       # Define fraction of data allocated to the client
       fraction = 0.02
       client_data_size = int(fraction * len(X_df_scl))
       client_indices = indices[:client_data_size]
       
       # Extract client-specific data
       X_client = X_df_scl[client_indices]
       y_client = y_df.iloc[client_indices]
       
       return X_client, y_client

**Details**:

- **Seed Initialization**:

  - ``np.random.seed(client_id)`` ensures reproducibility and uniqueness for each client.  
  - The seed is tied to the ``client_id``, guaranteeing different shuffling patterns across clients.

- **Data Shuffling**:

  - ``indices = np.arange(len(X_df_scl))`` generates an array of indices corresponding to the scaled feature dataset.  
  - ``np.random.shuffle(indices)`` randomizes the order of indices.  
  - Each client receives a unique shuffled order due to the client-specific seed.

- **Subset Selection**:

  - ``fraction = 0.02`` specifies that 2% of the total data is allocated to each client. Adjust this value to change the client's data portion.  
  - ``client_data_size`` calculates the number of samples per client.  
  - ``client_indices`` selects the first ``client_data_size`` indices from the shuffled array, ensuring non-overlapping subsets across clients.

- **Data Extraction**:

  - ``X_client`` and ``y_client`` extract features and labels using the client-specific indices.  
  - Assumes ``X_df_scl`` (scaled features) and ``y_df`` (labels) are predefined from prior preprocessing steps.

2. Key Notes
------------

- **Non-IID Simulation**:  

  - The client-specific shuffling ensures each client's data distribution is unique and non-identically distributed.  
  - Suitable for scenarios requiring heterogeneous data partitions (e.g., edge devices with varying data sources).

- **Dependencies**:  

  - Requires ``numpy`` for index manipulation and assumes prior execution of code defining ``X_df_scl`` and ``y_df`` (scaling and splitting steps).

- **Class Distribution**:  

  - The function does not explicitly balance classes. Inherits any class imbalance present in the original dataset.  
  - To address imbalance, additional preprocessing (e.g., stratified sampling) may be required.

- **Adjustability**:  

  - Modify ``fraction`` to control the proportion of data allocated per client.  
  - Example: ``fraction = 0.05`` allocates 5% of the dataset to each client.
