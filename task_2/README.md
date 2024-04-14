# Regression on Tabular Data

## Python Version
This project requires Python version 3.11.

## Instructions
1. Open a terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:
```
git clone https://github.com/booggi228/test_task_DS.git
```
### Create a Virtual Environment
1. Navigate into the cloned repository.
2. Run the following command to create a virtual environment:
```
python -m venv regression_task
```
4. Activate the virtual environment:
- On Windows:
  ```
  regression_task\Scripts\activate
  ```
- On Mac/Linux:
  ```
  source regression_task/bin/activate
  ```

### Install Requirements
Run the following command to install the required dependencies:
pip install -r requirements.txt

## Notebooks
The 'notebooks' folder contains a Jupyter notebook with Exploratory Data Analysis (EDA) and model selection.

## Training
To run the training script, type the following command in the terminal:
```
python train.py
```

## Inference
To run the inference script, type the following command in the terminal:
```
python predict.py
```

The file with predictions will be stored in the 'output' folder.
