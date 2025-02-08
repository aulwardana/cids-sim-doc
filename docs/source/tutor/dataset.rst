.. _dataset:

Dataset
===========

.. note::

    CoAt-Set Publication: https://www.sciencedirect.com/science/article/pii/S2352340925000861

The CoAt-Set dataset is a transformed, specialized dataset designed to support collaborative anomaly detection within Collaborative Intrusion Detection Systems (CIDS). This dataset extract coordinated attack behaviors from established sources like CIC-ToN-IoT, CIC-IDS2017, CIC-UNSW-NB15, CSE-CIC-IDS2018, CIC-BoT-IoT, Distrinet-CIC-IDS2017, and NF-UQ-NIDS, refining these raw datasets into a format specifically designed for collaborative anomaly detection. CoAt-Set highlights coordinated attack situations, such as widespread, stealthy scanning, worm outbreaks, and distributed denial-of-service (DDoS) attacks, all of which mirror high-impact, realistic threats that are frequently found in today’s complex networks.

In creating CoAt-Set, the data was restructured and relabeled to represent collaborative security environments for CIDS better. This involved organizing attack behaviors in ways that offer clear annotations and insightful traffic features, which is invaluable for training and testing systems aimed at identifying anomalies across multiple networks. The focus on collaborative contexts means that CoAt-Set is well-suited for researchers and developers who need a dataset that goes beyond isolated attack patterns, instead offering a perspective on the kinds of threats that might span across different segments of a network. CoAt-Set integrates well with common neural network algorithms, allowing researchers to easily plug it into various neural network models and algorithms. The dataset also has broader uses, as it supports development of collaborative machine learning algorithms and can be used to simulate and test attacks across networks with varying configurations. 

A usage example of CoAt-Set in practice is in multi-agent CIDS setups where each agent analyzes non-IID data for distributed learning. For instance, the NF-UQ-NIDS dataset, created from multiple data sources, allows extraction of coordinated attack patterns, saved as "CoAt_NF-UQ-NIDS-V2.parquet." This version is useful for creating non-IID scenarios within a single dataset, then distributing it across agents for collaborative learning. Each agent can independently learn from its unique data, making this a powerful tool for distributed security research.

To further increase heterogeneity, each CIDS agent can be assigned a different CoAt-Set version, such as "CoAt_CIC-BoT-IoT-V2.parquet," "CoAt_CIC-IDS2017-V2.parquet," "CoAt_CIC-ToN-IoT-V2.parquet," "CoAt_CIC-UNSW-NB15_Feeded-V2.parquet," and "CoAt_CSE-CIC-IDS2018_Feeded.parquet." Each dataset represents a unique network environment, with each agent positioned in a distinct network segment to detect coordinated attacks. This diversity enables CIDS agents to capture a range of attack patterns, supporting the development of robust, flexible intrusion detection strategies across heterogeneous networks.

**Download The Dataset**

Please download the dataset using link below: 

.. note::

    CoAt-Set Download Link: https://data.mendeley.com/datasets/28tmfg3rzb/2

After download, you can put all the dataset files in ``dataset`` folder.