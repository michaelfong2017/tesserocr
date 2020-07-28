# tesserocr
You may refer to [this documentation](https://github.com/sirfz/tesserocr).
## Installation
### MacOS
#### 1. Create a conda environment
```console
$ conda create -n tesserocr_env python=3.7
$ conda activate tesserocr_env
```
For more details, please refer to [managing conda environment](https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html).

#### 2. Install tesserocr package
```console
$ conda install -c conda-forge tesserocr
```

#### 3. Add your conda environment to your jupyter notebook
You may refer to [add conda environment to jupyter notebook](https://medium.com/@nrk25693/how-to-add-your-conda-environment-to-your-jupyter-notebook-in-just-4-steps-abeab8b8d084) and [remove virtual environment from jupyter notebook](https://medium.com/analytics-vidhya/create-virtual-environment-using-conda-and-add-it-to-jupyter-notebook-d319a81dfd1).

```console
$ conda install -c anaconda ipykernel
$ python -m ipykernel install --user --name=tesserocr_env
```

#### 4. Start using jupyter notebook
1. Go to your home directory.

```console
$ cd ~
```

2. Start a jupyter notebook server.

```console
$ jupyter notebook
```

3. Navigate to your project directory.
4. Create a jupyter notebook under tesserocr_env.

![alt text](https://github.com/michaelfong2017/tesserocr/tree/master/documentation/images/jupyter_env.jpeg)

## Usage
```python
from tesserocr import PyTessBaseAPI

images = ['sample.jpg', 'sample2.jpg', 'sample3.jpg']

with PyTessBaseAPI() as api:
    for img in images:
        api.SetImageFile(img)
        print(api.GetUTF8Text())
        print(api.AllWordConfidences())
# api is automatically finalized when used in a with-statement (context manager).
# otherwise api.End() should be explicitly called when it's no longer needed.
```