### Hexlet tests and linter status:

[![Actions Status](https://github.com/Kostyanuch-c/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Kostyanuch-c/python-project-50/actions) [![Maintainability](https://qlty.sh/gh/Kostyanuch-c/projects/Gendiff/maintainability.svg)](https://qlty.sh/gh/Kostyanuch-c/projects/Gendiff) [![Python CI](https://github.com/Kostyanuch-c/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Kostyanuch-c/python-project-50/actions/workflows/pyci.yml) [![Code Coverage](https://qlty.sh/gh/Kostyanuch-c/projects/Gendiff/coverage.svg)](https://qlty.sh/gh/Kostyanuch-c/projects/Gendiff)


# Generate difference 
## description

The function ***gendiff*** allows you to determine the difference between two files
and display their differences. 

To use it, type the command in this view
***gendiff <path_to_file_1> <path_to_file_2>***

**Supported input file types**
* .json, .yaml, .yml.

**Possible output formats** 
* stylish, plain, json
 
The default output format is **stylish** but you can define supported output with the optional key.
To use another output additionally type option key -f or --format

In addition to the command-line interface, the application now includes a graphical
user interface (GUI) for easier comparison of JSON and YAML files.

## Install as a Python package
+ **Linux:**
 
```bash
python3 -m pip install --user git+https://github.com/Kostyanuch-c/Gendiff.git
``` 
### Run
+ **CLI**
```bash
gendiff [-h] [-f FORMAT] first_file second_file
``` 
+ **GUI**
```bash
gendiff_gui
``` 
<details>

<summary>Demonstration</summary>

![gendiff](https://github.com/Kostyanuch-c/python-project-50/assets/98832310/338ffba7-c15e-4af6-8125-3d12565ba27a)

</details>

### !Notes for using the package without cloning!

If you install gendiff as a package via pip or poetry, the GUI requires a Python interpreter with tkinter installed.

On Ubuntu, you can ensure tkinter is present by installing:
 ```bash
sudo apt install python3-tk
  ``` 

If tkinter is missing, the GUI will not run, even if the package is installed.

## Run from cloned repository


### 1. Preparing to run 

 ```bash
  git clone https://github.com/Kostyanuch-c/Gendiff.git
  cd Gendiff
 ```

### 2. Install dependencies

```bash
make install
```

### 3. Running 
+ **CLI**

```bash
make gendiff
```

+ **GUI**

```bash
make gendiff_gui
```
   
  <details>

  <summary>Example:</summary>

  ![MyDiff-_Ubuntu_-2024-10-01-14-02-00](https://github.com/user-attachments/assets/1d923c1a-4f30-4b65-b949-03949bed9089)

  </details>
