CIDS-Sim: Simulator for CIDS based on Federated Learning
===================================

**CIDS-Sim** (Collaborative Intrusion Detection System - Simulator) is a sophisticated simulation platform engineered to replicate, analyze, and optimize CIDS using federated learning methodologies. 
Tailored to address modern cybersecurity challenges, the software supports academic research, technological development, and educational initiatives by simulating realistic, decentralized environments characterized by non-independent and identically distributed (non-IID) data and heterogeneous data distributions. 
These scenarios mirror the complexity of real-world networks, enabling robust testing and validation of CIDS under conditions that reflect actual operational challenges, such as uneven data quality, varying attack patterns, and device diversity.

At its core, CIDS-Sim employs a centralized federated learning architecture that harmonizes privacy preservation with collaborative intelligence. 
By design, sensitive data remains localized on distributed client nodes—such as edge devices, servers, or IoT systems—while global machine learning models are iteratively refined through secure parameter aggregation. 
This approach not only safeguards data confidentiality but also enables organizations to leverage collective insights without compromising proprietary or personal information.

Github: `https://github.com/aulwardana/CIDS-Sim <https://github.com/aulwardana/CIDS-Sim>`_

The simulator is *open-source* and *free to use* for researchers, practitioners in the industry, and educators. 
If you use this software, please provide citation credit to our **publication** available at `this link. <https://github.com/aulwardana/CIDS-Sim>`_

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   tutor/overview
   tutor/installation
   tutor/dataset
   tutor/configuration
   tutor/output
   tutor/future

.. toctree::
   :maxdepth: 1
   :caption: Components

   cids.data.preprocessing
   cids.data.load_dist
   cids.fl.model
   cids.fl.aggregate
   cids.fl.training
   cids.fl.predict
   cids.metric.accuracy
   cids.metric.precision
   cids.metric.recall
   cids.metric.f1_score
   cids.metric.std_dev
   cids.metric.varriance
   cids.metric.train_time
   cids.metric.pred_time
   cids.metric.cpu_memory
   cids.metric.comp_over
   cids.out.log
   cids.out.visual
   cids.out.file