### Hexlet tests and linter status:

[![Actions Status](https://github.com/Kostyanuch-c/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Kostyanuch-c/python-project-50/actions) [![Maintainability](https://api.codeclimate.com/v1/badges/ef2aa50640cef183ef11/maintainability)](https://codeclimate.com/github/Kostyanuch-c/python-project-50/maintainability) [![Python CI](https://github.com/Kostyanuch-c/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/Kostyanuch-c/python-project-50/actions/workflows/pyci.yml) [![Test Coverage](https://api.codeclimate.com/v1/badges/ef2aa50640cef183ef11/test_coverage)](https://codeclimate.com/github/Kostyanuch-c/python-project-50/test_coverage)


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


### Install
+ **Linux:**
 
  ```bash
   python3 -m pip install --user git+https://github.com/Kostyanuch-c/python-project-50.git
  ```
   
   

<details>

<summary>Demonstration</summary>

![gendiff](https://github.com/Kostyanuch-c/python-project-50/assets/98832310/338ffba7-c15e-4af6-8125-3d12565ba27a)

</details>

## GUI Interface

In addition to the command-line interface, the application now includes a graphical user interface (GUI) for easier comparison of JSON and YAML files.

### Running the GUI
 To launch the GUI, run the following command:
  ```bash
   make gendiff_gui
  ```
   
<details>

<summary>Example:</summary>

![MyDiff-_Ubuntu_-2024-10-01-14-02-00](https://github.com/user-attachments/assets/1d923c1a-4f30-4b65-b949-03949bed9089)

</details>
