# tesserocr
We will be using a python wrapper for Tesseract OCR called [tesserocr](https://github.com/sirfz/tesserocr).
You can also look at [this tutorial](https://medium.com/better-programming/beginners-guide-to-tesseract-ocr-using-python-10ecbb426c3d) for more information.
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

![alt text](https://github.com/michaelfong2017/tesserocr/blob/master/documentation/images/jupyter_env.jpeg?raw=true)

## Usage
1. Create a PyTessBaseAPI object and assign it to a variable.

```python
with PyTessBaseAPI(path='/Users/michael/opt/anaconda3/envs/tesserocr_env/share/tessdata/', lang='eng') as api:
    # Usage below...
```

2. Tesseract API methods are called via this class object.

```python
# Usage below...
print(api.GetAvailableLanguages())
for img in images:
    api.SetImageFile(img)
    print(api.GetUTF8Text())

# Tesseract API methods are called in this way.
# api.Xxxxxx
# api.Yyyyyy
# api.Zzzzzz
```

## Example
Please refer to [my jupyter notebook example](https://github.com/michaelfong2017/tesserocr/blob/master/src/example.ipynb).

## API documentation
All interfaces can be found in the [Python wrapper around the Tesseract-OCR C++ API](https://github.com/sirfz/tesserocr/blob/master/tesserocr.pyx).
This module provides a wrapper class :class:`PyTessBaseAPI` to call Tesseract API methods.
This module also provides other helper functions.

### Initialization of class PyTessBaseAPI
```python
    def InitFull(self, path=_DEFAULT_PATH, lang=_DEFAULT_LANG,
                 OcrEngineMode oem=OEM_DEFAULT, list configs=[],
                 dict variables={}, bool set_only_non_debug_params=False):
        """Initialize the API with the given parameters (advanced).
        It is entirely safe (and eventually will be efficient too) to call
        :meth:`Init` multiple times on the same instance to change language, or just
        to reset the classifier.
        Page Segmentation Mode is set to :attr:`PSM.AUTO` after initialization by default.
        Args:
            path (str): The name of the parent directory of tessdata.
                Must end in /.
            lang (str): An ISO 639-3 language string. Defaults to 'eng'.
                The language may be a string of the form [~]<lang>[+[~]<lang>]* indicating
                that multiple languages are to be loaded. Eg hin+eng will load Hindi and
                English. Languages may specify internally that they want to be loaded
                with one or more other languages, so the ~ sign is available to override
                that. Eg if hin were set to load eng by default, then hin+~eng would force
                loading only hin. The number of loaded languages is limited only by
                memory, with the caveat that loading additional languages will impact
                both speed and accuracy, as there is more work to do to decide on the
                applicable language, and there is more chance of hallucinating incorrect
                words.
            oem (int): OCR engine mode. Defaults to :attr:`OEM.DEFAULT`.
                See :class:`OEM` for all available options.
            configs (list): List of config files to load variables from.
            variables (dict): Extra variables to be set.
            set_only_non_debug_params (bool): If ``True``, only params that do not contain
                "debug" in the name will be set.
        Raises:
            :exc:`RuntimeError`: If API initialization fails.
        """
        cdef:
            bytes py_path = _b(path)
            bytes py_lang = _b(lang)
            cchar_t *cpath = py_path
            cchar_t *clang = py_lang
            int configs_size = len(configs)
            char **configs_ = <char **>malloc(configs_size * sizeof(char *))
            GenericVector[STRING] vars_vec
            GenericVector[STRING] vars_vals
            cchar_t *val
            STRING sval

        for i, c in enumerate(configs):
            c = _b(c)
            configs_[i] = c

        for k, v in variables.items():
            k = _b(k)
            val = k
            sval = val
            vars_vec.push_back(sval)
            v = _b(v)
            val = v
            sval = val
            vars_vals.push_back(sval)

        with nogil:
            try:
                self._init_api(cpath, clang, oem, configs_, configs_size, &vars_vec, &vars_vals,
                               set_only_non_debug_params, PSM_AUTO)
            finally:
                free(configs_)

    def Init(self, path=_DEFAULT_PATH, lang=_DEFAULT_LANG,
             OcrEngineMode oem=OEM_DEFAULT):
        """Initialize the API with the given data path, language and OCR engine mode.
        See :meth:`InitFull` for more initialization info and options.
        Args:
            path (str): The name of the parent directory of tessdata.
                Must end in /. Uses default installation path if not specified.
            lang (str): An ISO 639-3 language string. Defaults to 'eng'.
                See :meth:`InitFull` for full description of this parameter.
            oem (int): OCR engine mode. Defaults to :attr:`OEM.DEFAULT`.
                See :class:`OEM` for all available options.
        Raises:
            :exc:`RuntimeError`: If API initialization fails.
        """
        cdef:
            bytes py_path = _b(path)
            bytes py_lang = _b(lang)
            cchar_t *cpath = py_path
            cchar_t *clang = py_lang
        with nogil:
            self._init_api(cpath, clang, oem, NULL, 0, NULL, NULL, False, PSM_AUTO)
```
