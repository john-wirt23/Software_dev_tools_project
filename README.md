This is a web application tool. It displays visualizations of data from a dataset called "vehicles_us.csv". This dataset contains information regarding vehicle sales advertisments in the United States. Each row of the dataset contains price, model, body type, transmission type and more. The web application includes a histogram, scatterplot, and a bar chart with a checkbox. The Python libraries implemented in this application are as follows:

scipy==1.11.1
pandas==2.2.0
streamlit==1.30.0
plotly.express==0.4.1
altair==5.2.0

In order to launch this project from your own local machine you will need to clone this repository from github.com, pull it to a text editor of your choice (This app was created using VScode.), and create a virtual python environment. Once you activate this environment you will want to install all of the libraries listed above. If you are using VScode be sure to set your Python Interpreter to the virtual environment or 'venv'. You will then have to push your copy of the repository to your github account (or any version control provider of your choice). Once that is accomplished it is advisable to run this application locally using Streamlit. If there are no issues or errors and the components are working as expected you may proceed to launch this app as a web service through a web service provider like 'Render.com'. Be sure to include the following commands in the build and start command respectively:

pip install streamlit & pip install -r requirements.txt
streamlit run app.py


The application is accessible at this url:
https://vehicles-us-project.onrender.com

