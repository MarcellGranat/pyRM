# pyRM

Python wrapper to use easily the RM API from [ddvk/rmapi](https://github.com/ddvk/rmapi) [ ]()[https://github.com/ddvk/](https://github.com/ddvk/rmapi?tab=readme-ov-file).

# Install

1.  Follow the installation guide of [ddvk/rmapi](https://github.com/ddvk/rmapi) [ ]()[https://github.com/ddvk/rmapi](https://github.com/ddvk/rmapi?tab=readme-ov-file).
2.  Once done, you only need to modify the `path_to_rmapi` arg of the `upload_to_rm` function.

```{python}
pip install git+ssh://git@github.com/MarcellGranat/pyRM.git
```

```{python}
import pyRM

upload_to_rm(file_name, rm_folder = "books")
```