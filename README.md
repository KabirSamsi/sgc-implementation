# CS 4782 Final Project

## Simple Graph Convolutions

Reimplements the model architecture discussed in [Wu et al – Simplifying Graph Convolutional Networks](https://arxiv.org/pdf/1902.07153).

## Members
- Kabir Samsi (kas499)
- Shashank Kalyanaraman (ssk252)
- Neha Arora (na458)
- Sol Jung (sj777)

## Accessing Datasets

Download the following two datasets and store them under `data/` before running:

1) https://drive.google.com/open?id=174vb0Ws7Vxk_QTUtxqTgDHSQ4El4qDHt
2) https://drive.google.com/open?id=19SphVl_Oe8SJ1r87Hr5a6znx3nJu1F2J

## Independent Exploration: Actor Dataset

Cell 8 of the notebook benchmarks SGC and GCN on the Actor heterophilic graph as an independent exploration. **We recommend running this cell in Google Colab**, as the existing notebook is configured to mount Google Drive for loading the dataset files. If this cell is not needed, please comment it out before running. 

The Actor dataset (`actor_nodes.txt` and `actor_edges.txt`) can be downloaded from the Geom-GCN repository: https://github.com/graphdml-uiuc-jlu/geom-gcn/tree/master/new_data/film

Place both files in your Google Drive (or update the `NODE_FILE` / `EDGE_FILE` paths in the cell) before running.
