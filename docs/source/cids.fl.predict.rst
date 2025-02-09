Prediction Process
==========================

.. _cids.fl.predict:

The code includes **two main prediction phases**: local validation during client training and global evaluation of the aggregated model. Below is a detailed breakdown:

1. **Local Validation Prediction (Per Node)**
---------------------------------------------

**Purpose**:  

Evaluate each client's locally updated model on its validation set to measure node-specific performance.

**Code Snippet**:  

.. code-block:: python

   # Inside the node training loop:
   start_pred_time = time.time()
   loss, accuracy, precision, recall = model.evaluate(X_val, Y_val, verbose=0)
   end_pred_time = time.time()
   local_prediction_time = end_pred_time - start_pred_time

**Steps**:  

- **Input**: Validation data ``(X_val, Y_val)`` split from the client's local dataset.  
- **Prediction**: Uses Keras ``model.evaluate()`` to compute predictions and metrics (accuracy, precision, recall).  
- **Timing**: Measures prediction latency for the local model.  
- **F1-Score Calculation**:  

  .. code-block:: python

     f1_score = calculate_f1_score(precision, recall)  # Uses precision and recall from evaluation

**Key Metrics Tracked**:  

- Local accuracy, precision, recall, F1-score.  
- Local prediction time (``local_prediction_times`` list).  

---

2. **Global Model Prediction (Per Round)**
------------------------------------------
**Purpose**:  

Evaluate the aggregated global model on a reserved test set after each federated round.

**Code Snippet**:  

.. code-block:: python

   # After weight aggregation in each round:
   start_glob_pred_time = time.time()
   loss, accuracy, precision, recall = model.evaluate(X_test, Y_test, verbose=0)
   end_glob_pred_time = time.time()
   global_pred_time = end_glob_pred_time - start_glob_pred_time

**Steps**:  

- **Test Data**: Loaded using ``X_test, Y_test = load_data(num_nodes + 1)``, assuming client ``num_nodes + 1`` is reserved for testing.  
- **Prediction**: Uses the updated global model to infer on the test set.  
- **Timing**: Tracks global prediction latency (stored in ``global_pred_times``).  
- **Metrics**: Logs global accuracy, precision, recall, and F1-score.  

---

3. **Key Observations**
------------------------
- **Prediction Workflow**:  

  - Both local and global predictions are **evaluation-driven**, not standalone inference on new data.  
  - Relies on Keras' ``model.evaluate()``, which internally calls ``predict()`` and computes metrics.  

- **Limitations**:  

  - No explicit ``predict()`` calls – metrics are derived directly from evaluation.  
  - Test data is static (loaded once at initialization) and may not represent real-world streaming data.  

- **Customization**:  

  - To perform inference on new data, add:  

    .. code-block:: python

       predictions = global_model.predict(new_data)  # Outside the training loop

---

4. **Tracked Metrics**
----------------------
- **Local**:  

  - Per-node prediction times, precision, recall, F1.  
  - Variance and standard deviation across nodes.  

- **Global**:  

  - Round-wise prediction times (``global_pred_times``).  
  - Accuracy, precision, recall, F1 (``global_accuracies``, etc.).  

---

5. **Dependencies**  

- Assumes ``X_test/Y_test`` are preprocessed and scaled (matches ``X_df_scl`` format).  
- Requires ``calculate_f1_score()`` for F1 computation.  

This design focuses on **collaborative evaluation** rather than real-time intrusion detection. For deployment, additional logic would be needed to handle live prediction tasks.
