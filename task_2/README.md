Regression on the tabular data.

Python version 3.11

Instructions:
Open a terminal or command prompt.
Navigate to the directory where you want to clone the repository.
Run the following command to clone the repository:
git clone <repository_url>

Create a Virtual Environment:

Navigate into the cloned repository.
Run the following command to create a virtual environment:
python -m venv regression_task

On windows:
regression_task\Scripts\activate

On Mac/Linux:
source regression_task/bin/activate

Install Requirements:

pip install -r requirements.txt

In 'notebooks' folder there is a notebook with EDA and model selection part.

For running the training script type:
python train.py

For running the inference script type:
python predict.py

File with prediction will be stored in 'output' folder.