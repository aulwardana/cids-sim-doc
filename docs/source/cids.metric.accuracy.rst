Accuracy Measurement
==========================

.. _cids.metric.accuracy:

The code measures accuracy at **two levels**:  

1. **Local validation** (per client/node).  
2. **Global evaluation** (aggregated model on a test set).  

---

### 1. **Local Accuracy Measurement**  
**When**: After training a client's local model in each federated round.  
**How**:  

- Uses Keras' ``model.evaluate()`` on the client's validation set (split from their local data).  
- Accuracy is calculated as:  

  .. math::  
     \\text{Accuracy} = \\frac{\\text{Correct Predictions}}{\\text{Total Samples}}  

- For binary classification, predictions are thresholded at 0.5 (sigmoid output).  

**Code Workflow**:  

.. code-block:: python

   loss, accuracy, precision, recall = model.evaluate(X_val, Y_val, verbose=0)  
   local_accuracies.append(accuracy)  # Stored for variance analysis  

**Key Notes**:  

- Tracked per client to measure node-specific performance.  
- Used to compute **cross-node variance and standard deviation** (e.g., ``accuracy_variances``).  

---

### 2. **Global Accuracy Measurement**  
**When**: After aggregating client weights into the global model in each round.  
**How**:  

- Evaluates the global model on a reserved test set (loaded via ``load_data(num_nodes + 1)``).  
- Uses the same ``model.evaluate()`` method as above.  

**Code Workflow**:  

.. code-block:: python

   loss, accuracy, precision, recall = model.evaluate(X_test, Y_test, verbose=0)  
   global_accuracies.append(accuracy)  # Tracked across rounds  

**Key Notes**:  

- Test data is **static** and assumed to represent a realistic evaluation scenario.  
- Reflects the global model’s generalization ability.  

---

### 3. **Technical Details**  

- **Metric Source**:  

  - Keras’ ``binary_accuracy`` (default for binary classification with sigmoid output).  
  - Threshold: Predictions ≥ 0.5 are classified as ``1`` (anomaly), else ``0`` (normal).  

- **Dependencies**:  

  - Requires labels (``Y_val``, ``Y_test``) to be binary (0 or 1).  
  - Test data (``X_test, Y_test``) must match the preprocessing of ``X_df_scl``.  

- **Limitations**:  

  - Test set is derived from a single client (``num_nodes + 1``), which may not reflect all data distributions in Non-IID settings.  
  - No explicit handling of class imbalance (inherits imbalance from the dataset).  

---

### 4. **Performance Analysis**  

- **Local Variance**:  

  .. code-block:: python

     accuracy_variance = np.var(local_accuracies)  # Measures consistency across nodes  
     accuracy_std = np.std(local_accuracies)  

- **Global Trends**:  

  - ``global_accuracies`` shows how the aggregated model improves over rounds.  
  - Printed after each round (e.g., ``Round 1: Accuracy 0.9234``).  

--- 

### 5. **Customization**  

- To modify the accuracy calculation (e.g., for imbalanced data): 
 
  - Replace ``metrics=['accuracy']`` with custom metrics (e.g., ``tf.keras.metrics.BinaryAccuracy(threshold=...)``).  
  - Use weighted accuracy or F1-score as the primary metric.  

This implementation focuses on **standard classification accuracy**, with additional metrics (precision, recall, F1) for comprehensive evaluation.


