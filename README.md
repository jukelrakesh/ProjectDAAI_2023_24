# Multimodal Egocentric Action Recognition

## Overview
This project investigates feature extraction and action recognition in egocentric vision utilizing pre-trained models. Various dimensionality reduction techniques, including PCA and tSNE, are applied to understand their effect on training. A simple classifier is then created and trained with the extracted features for evaluation.

## Repository Structure
```md
ProjectDAAI_2023_24/
│── data/               # Dataset and pre-processed features
│── models/             # Pre-trained models and trained classifiers
│── notebooks/          # Jupyter notebooks for experiments and analysis
│── scripts/            # Python scripts for feature extraction and training
│── results/            # Output results, plots, and evaluation metrics
│── README.md           # Project documentation (this file)
│── requirements.txt    # List of dependencies
```

## Dataset
The project uses the **EPIC-Kitchens-55** dataset, a large-scale egocentric video benchmark recorded by 32 participants in their native kitchen environments. The study focuses on **participant P08**, using only RGB frames.

## Methodology
1. **Video Sampling Strategies:**
   - **Dense Sampling:** Selecting frames close to each other to preserve temporal dynamics.
   - **Uniform Sampling:** Spreading frame selection evenly throughout the video.

2. **Feature Extraction:**
   - Using a pre-trained **I3D-Inception-v1** model to extract spatial and temporal features.

3. **Dimensionality Reduction:**
   - **PCA (Principal Component Analysis):** Focuses on global variance.
   - **tSNE (t-Distributed Stochastic Neighbor Embedding):** Emphasizes local variance.

4. **Classifier Training:**
   - A fully connected layer with:
     - Input Layer: 1024 neurons
     - Hidden Layer: 512 neurons
     - Output Layer: 8 neurons (corresponding to action classes)
     - ReLU activation and dropout layers for regularization

## Results
- **Dense Sampling** achieved **92.12% accuracy**, outperforming uniform sampling.
- **Classifier Accuracy:**
  - Best accuracy achieved: **56.09%**
  - Average accuracy: **48.75%**

## Requirements
Install dependencies using:
```bash
pip install -r requirements.txt
```

## How to Run
1. **Preprocess Data:** Extract frames and prepare features.
2. **Feature Extraction:** Run `scripts/extract_features.py`.
3. **Train Classifier:** Run `scripts/train_classifier.py`.
4. **Evaluate Model:** Analyze results in `notebooks/evaluation.ipynb`.

## Future Work
- Experiment with different **sampling stride values**.
- Improve classifier with **additional hidden layers**.
- Explore different **dropout rates** to prevent overfitting.

## Contributors
- Jukel Rakesh (s308039)
- Aswin Prasannakumar (s314443)
- Juan Perez de la Calle (s321372)

## References
Refer to `DAAI_Report.pdf` for detailed explanations and citations.

---
For any questions or contributions, feel free to open an issue or submit a pull request!

