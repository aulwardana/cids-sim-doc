Training Process
==========================

.. _cids.fl.training:

This document explains the code in the provided Jupyter notebook for implementing a Federated Learning (FL) workflow for a Collaborative Intrusion Detection System (CIDS) with Non-IID data.

1. Utility Functions
--------------------

1.1. **Calculate Model Size**  

**Purpose**: Estimate the memory footprint of a model to quantify communication overhead.  

.. code-block:: python

   def calculate_model_size(model):
       total_params = np.sum([np.prod(weights.shape) for weights in model.get_weights()])
       size_in_bytes = total_params * 4  # 32-bit float (4 bytes per parameter)
       return size_in_bytes

**Details**:  

- Sums all trainable parameters in the model.  
- Assumes each parameter is stored as a 32-bit float (4 bytes).  
- Used to measure communication costs during FL aggregation.  

---

1.2. **Calculate F1-Score**  

**Purpose**: Compute the harmonic mean of precision and recall for classification evaluation.  

.. code-block:: python

   def calculate_f1_score(precision, recall):
       f1_score = 2 * (precision * recall) / (precision + recall + 1e-10)
       return f1_score

**Details**:  

- Adds a small epsilon (``1e-10``) to avoid division by zero.  
- Used to evaluate both local and global model performance.  

---

2. Federated Training Function: `cids_federated_training()`
------------------------------------------------------------

**Purpose**:  

Simulate federated learning across distributed nodes with Non-IID data, aggregating model updates while tracking performance metrics and resource usage.

.. code-block:: python

   def cids_federated_training(num_nodes=5, num_rounds=5):
       # Initialization, training loops, aggregation, and evaluation logic

**Parameters**:  

- ``num_nodes``: Number of clients/nodes (default: 5).  
- ``num_rounds``: Federated training iterations (default: 5).  

---

2.1. **Workflow Overview**  

- **Step 1**: Initialize a global model and trackers for metrics (accuracy, precision, recall, F1-score).  
- **Step 2**: For each round:  

  - Distribute global model weights to nodes.  
  - Train local models on node-specific Non-IID data.  
  - Aggregate updated weights using federated averaging.  
  - Evaluate global model performance on a test set.  
  
- **Step 3**: Log metrics (training time, CPU/memory usage, communication overhead, variance in performance).  

---

2.2. **Key Components**  

- **Global Model Initialization**:  

  .. code-block:: python

     global_model = create_model(input_shape=X_df_scl.shape[1])

- **Local Training**:  

  - Data loading using ``load_data(node)`` (Non-IID splits).  
  - Model training with fixed hyperparameters (10 epochs, batch size=1000).  
  - Resource monitoring via ``psutil`` (CPU, memory usage).  

- **Weight Aggregation**:  

  .. code-block:: python

     new_weights = [np.mean([weight[layer] for weight in local_weights], axis=0) for layer in range(len(global_weights))]

- **Communication Overhead**:  

  - Tracks total data transferred between nodes and the server.  
  - Updated after each round:  

    .. code-block:: python

       communication_overhead += num_nodes * model_size  # Server-to-node broadcast

---

2.3. **Tracked Metrics**  

- **Performance Metrics**:  

  - Accuracy, precision, recall, F1-score (local and global).  
  - Variance and standard deviation across nodes to measure consistency.  

- **Resource Utilization**:  

  - Training/prediction time per node.  
  - CPU and memory usage during training.  

- **Communication Costs**:  

  - Model size (in MB) and cumulative overhead across rounds.  

---

3. Simulation Execution
-----------------------

**Purpose**: Run the federated training process and display results.  

.. code-block:: python

   print("Simulation for CIDS with Non-IID Data\\n")
   fl_model, fl_global_accuracies, ..., f1_stds = cids_federated_training()

**Output**:  

- Prints round-wise metrics (training time, prediction time, F1-score).  
- Final communication overhead (e.g., ``Final Communication Overhead: 12.34 MB``).  

---

4. Dependencies and Customization
----------------------------------

- **Libraries**:  

  - ``numpy``, ``tensorflow/keras``, ``psutil``, ``time``, ``sklearn.model_selection.train_test_split``.  

- **Adjustable Parameters**:  

  - ``num_nodes``: Increase to simulate more clients.  
  - ``num_rounds``: Extend for longer training.  
  - ``fraction`` in ``load_data()``: Modify client data allocation.  

- **Model Customization**:  

  - Replace ``create_model()`` with alternative architectures.  
  - Adjust training hyperparameters (epochs, batch size).  

---

5. Notes
--------

- **Non-IID Assumption**: Data splits are client-specific and non-uniform, mimicking real-world edge device scenarios.  
- **Scalability**: The code supports varying numbers of nodes and rounds but may require optimization for large-scale deployments.  
- **Evaluation**: Test data is loaded using ``load_data(num_nodes + 1)``, assuming a reserved client ID for validation.