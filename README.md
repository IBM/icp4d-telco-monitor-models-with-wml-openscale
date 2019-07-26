# Monitor your ML Models using Watson OpenScale

## Pre-requisites
* [IBM Cloud Pak for Data]() Or [IBM Cloud Account](https://cloud.ibm.com/)


## Steps
1. [Create a new Watson Studio Project]()
2. [Add a new Watson Machine Learning Model]()
3. [Build your own Machine Learning Model with WML Model Builder]()
4. [Save and Deploy your WML Model]()
5. [Create a new Watson OpenScale instance on IBM Cloud]()
6. [Create a new Watson Studio Python Notebook]()
7. [Configure Credentials in your Notebook]()
8. [Run the Inital Scoring and Payload Logging]()
9. [Configure the Quality and Fairness Monitors on Watson OpenScale]()
10. [Add Feedback Data to setup your dashboard on Watson OpenScale]()


### 1. Create a new Watson Studio Project

* On IBM Cloud create a new [Watson Studio](https://cloud.ibm.com/catalog/services/watson-studio)

  ![](doc/src/gif/Create_Watson_Studio.gif)
  
* Make sure to set the location to `Dallas`, select the appropriate plan and hit Create.
* Go to your [IBM Cloud Dashboard](https://cloud.ibm.com/)
* Click on `resources>services` select your Watson Studio Service and click on `Get Started`.
* Create a new Project as shown below-
  
  ![](doc/src/gif/Create_Project.gif)
  
* If you don't have a Cloud Object Storage Instance then follow the onscreen steps to create a new Cloud Object Storage Instance.

### 2. Add a new Watson Machine Learning Model

* Click on `Add to Project` and select `Watson Machine Learning` option.
* If you already have a WML instance, make sure it is in the `Dallas` region. If not, follow the steps as below-
  ![](doc/src/gif/Create_WML.gif)

```Note: Ensure your WML region is Dallas```
* Select `model type> model builder`
* Select `runtime> Default Spark Scala 2.11`
* Select the `Manual` option
  ![](doc/src/images/create_model.png)
* Give your model a name and hit create.

### 3. Build your own Machine Learning Model with WML Model Builder

* Clone the repo using the `Clone or Download` button or by typing the below command in a desired directory in your command line.

```
    git clone https://github.com/IBM/icp4d-telco-monitor-models-with-wml-openscale.git
```
* In your IBM Cloud, open the created model. Click on `Add Data Assets`. Navigate to the `dataset` folder in the downloaded repo, add the file and select the file. 

  ![](doc/src/images/add_data.png)
  
* Once your dataset is loaded, setup the Target Column, Feature Column, Type of Classification or Regeression and an Estimator.

  ![](doc/src/gif/Create_Model.gif)
  
```
  Note: The parameters you set will be different from the above steps, in case of a different dataset and use-case.
```
* Once the model is trained click on `Save` and store your model.

  
