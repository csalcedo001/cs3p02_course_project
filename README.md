# CS3P01 - Cloud Computing: Final Course Project

## Project Description

The project consists in developing a complete and functional Kubeflow pipeline for a real research project in Machine Learning. This project should consider:

- Data generation / retrieval.
- Training of multiple models.
- Compare models on the test phase with plots.
- Hyperparameter tuning with Katib.

In detail, the project considers the classification task for the XOR problem. In this task, points are drawn uniformly at random in the range [0, 1] in a 2D plane (although an implementation can be extended to _n_ dimensions). Each point has a label corresponding to the XOR operator of the rounded values of the point's coordinates in the plane (check the image from scatter plots for a reference). The idea is to obtain a model that can correctly classify each sample point as belonging to each quadrant of the XOR operator.

Theoretically, a linear model should not be able to learn a set of parameters that solves the XOR problem because points are spread in a way that makes it impossible for a single line to divide appropriately. In contrast, a non-linear model with higher capacity (such as a neural network with hidden layers) should be able to correctly classify points for the XOR problem with almost perfect accuracy. In this project we use Kubeflow as the framework in which this whole machine learning research workflow takes place.

## Project Steps

### Summary

- Docker image with saved state of the current version of the project.
- Pipeline with multiple components:
    - XOR generator component: Generates points samples and returns both a training set and test set.
    - Sample scatter plot component: Loads the training and test set and makes a scatter plot of the sampled points. This is conditioned on the variable _dims_, which should be equal to 2 for the plot to be generated.
    - Train component: Loads the training set, instantiates a neural network model given a configuration, trains the model with the dataset, and saves the model weights and training metrics to a folder.
    - Training plots component: Loads training metrics from two models and generates a plot that compares both models on each of the metrics.
- Manual parameter configuration for runs using Kubeflow's Central Dashboard.

### Dataset

The dataset consists of a training set and test set of points obtained from the the XOR generator. In particular, we sampled 10000 points for the training set and 1000 points for the test set.

_Training (10000 samples):_

![](data/sample_scatter_train.png)


_Testing (1000 samples):_

![](data/sample_scatter_test.png)

### Models

This project considered two simple neural network architectures for the classification task: a model with no hidden layers, and a model with one hidden layer.

![](data/models.png)

### Training

Both models were trained for 1000 epochs with identical hyperparameters, with the only difference in the number of hidden layers. There are two metrics that are recorded during training for both models: the training loss and the training accuracy.

![](data/training_loss.png)

![](data/training_acc.png)

_Note_: The training accuracy plot has the wrong scaling in the y-axis because the accuracy metric should have been normalized over the number of samples in the training set. This would result in values in the range [0, 1], which is the usual range for the accuracy.

The results from this experiment show that a neural network with a hidden layer is able to learn faster and more accurately than a neural network with no hidden layers. This means that higher capacity


## Kubeflow

This project used Kubeflow to enable a simple transition from python scripts to a more ellaborate pipeline of components. Kubeflow allowed for conteinerized components that could be connected together easily through Kubeflow Pipelines interface for Python. Although this project wasn't launched in a public domain, Kubeflow allows for portable experiments that could have been configured and runned from different devices through Kubeflow Central Dashboard.

### Docker Hub

The latest image of the project can be found at [Docker Hub](https://hub.docker.com/r/cesarsalcedo/cs3p02_kubeflow_project/tags).

### Pipeline

The pipeline for this machine learning workflow is described by the script in `pipeline.py`. The resulting YAML file describes a pipeline that can be visualized as in the following graph:

![](data/pipeline.png)

### Runs

Runs were executed successfully using Kubeflow Central Bashboard. Kubeflow makes experiment configuration and launching easy by providing an interface to the pipeline parameters. By using this interface, it was possible to set the configuration for the experiments (setting the number of samples for the training and test set, the number of dimensions of the dataset, and the number of training epochs). A successful run produces the following execution graph:

![](data/run.png)


## Future work

- Automate hyperparameter tunning via Katib
