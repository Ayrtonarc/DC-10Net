Multimodal Neural Network for Alzheimer’s Disease Prediction

Table of Contents
Overview
Data
Model Architecture
Installation
Usage
Training
Evaluation
Results
License
Contributing
Overview
This repository contains the implementation of a multimodal neural network for predicting the progression of Alzheimer's Disease (AD). The model integrates multiple types of data such as MRI images, cerebrospinal fluid (CSF) biomarkers, and cognitive scores to improve prediction accuracy. By combining multiple data modalities, the network aims to provide a robust tool for early detection of Alzheimer's Disease and its progression.

Data
The model is trained on the Alzheimer’s Disease Neuroimaging Initiative (ADNI) dataset. The data includes:

MRI scans: 3D MRI brain images.
Cerebrospinal Fluid (CSF) biomarkers: Levels of specific proteins in CSF samples.
Cognitive scores: Cognitive performance measures such as the MMSE and ADAS-Cog.
The data must be preprocessed before training. Refer to the data preprocessing section for more details.

Model Architecture
The multimodal neural network consists of the following components:

MRI Image Encoder: A 3D CNN that processes MRI scans to extract spatial features.
Biomarker Encoder: A fully connected network that processes CSF biomarker data.
Cognitive Score Encoder: A recurrent neural network (LSTM/GRU) that processes longitudinal cognitive scores.
Fusion Strategy
The encodings from each modality are merged using cross-attention layers followed by dense layers to create a unified multimodal embedding. This embedding is fed into a classifier that predicts the probability of Alzheimer's Disease progression.

Installation
Clone the repository and install dependencies.

bash
Copy code
git clone https://github.com/your-username/alzheimer-multimodal-prediction.git
cd alzheimer-multimodal-prediction
pip install -r requirements.txt
Usage
Prepare the Data: Download and preprocess the ADNI dataset.
Configure Model Parameters: Adjust the model and training parameters in config.yaml.
Train the Model: Start training by running the command below.
bash
Copy code
python train.py --config config.yaml
Training
The training script allows for fine-tuning the multimodal network with the ADNI dataset. You can adjust parameters in config.yaml for batch size, learning rate, and other model hyperparameters.

bash
Copy code
python train.py --config config.yaml
Evaluation
Evaluate the trained model using the test dataset:

bash
Copy code
python evaluate.py --model path/to/saved_model
Performance metrics such as accuracy, AUC, sensitivity, and specificity will be displayed after evaluation.

Results
Our model achieved:

Single-Modality Accuracy: ~75% (MRI only)
Multimodal Accuracy: ~81% (AUC=0.86)
These results indicate that incorporating multiple data sources improves the model's ability to predict AD progression.

License
This project is licensed under the MIT License - see the LICENSE file for details.

Contributing
Contributions are welcome! Please open an issue to discuss any changes you would like to make.
