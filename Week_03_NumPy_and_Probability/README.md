# Week 3 Tasks: Descriptive Statistics, Probability & NumPy Exploratory Data Analysis

**Student Name:** Ali Muhammad Younis (886)  
**Course:** Artificial Intelligence, Machine Learning & Deep Learning  
**Week:** 3  

---

## Overview
This folder contains the complete, tested solutions for all Week 3 syllabus requirements and Annexure-I tasks (Tasks 28 through 40 covering NumPy array manipulation, along with Probability, Correlation, Bayes' Theorem, and Distributions).

---

## Directory Contents & Task Mapping

| Task # | File Name | Description |
|---|---|---|
| **Task 28** | `Task_28_numpy_creating_arrays.py` | Creating 0D, 1D, 2D, and 3D NumPy arrays using `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`, and `np.eye()`. |
| **Task 29** | `Task_29_numpy_array_indexing.py` | 1D, 2D, and 3D element access, negative indexing, and row/column indexing. |
| **Task 30** | `Task_30_numpy_array_slicing.py` | Slicing 1D and 2D arrays with step intervals, negative slicing, and submatrix extraction. |
| **Task 31** | `Task_31_numpy_data_types.py` | Array data types (`int32`, `float64`, `bool_`, strings) and type conversion via `astype()`. |
| **Task 32** | `Task_32_numpy_copy_vs_view.py` | Deep copy vs view memory semantics, data ownership, and inspection with `.base`. |
| **Task 33** | `Task_33_numpy_array_shape.py` | Checking dimensions and shapes of multi-dimensional arrays (`.shape`, `.ndim`). |
| **Task 34** | `Task_34_numpy_array_reshape.py` | Reshaping 1D into 2D and 3D, using unknown dimensions (`-1`), and flattening arrays. |
| **Task 35** | `Task_35_numpy_array_iterating.py` | Iterating multi-dimensional arrays using standard loops, `np.nditer()`, and `np.ndenumerate()`. |
| **Task 36** | `Task_36_numpy_matrix_joining.py` | Array concatenation and stacking via `np.concatenate()`, `np.stack()`, `np.hstack()`, and `np.vstack()`. |
| **Task 37** | `Task_37_numpy_array_splitting.py` | Splitting arrays evenly and unevenly with `np.array_split()`, `np.split()`, and `np.hsplit()`. |
| **Task 38** | `Task_38_numpy_array_searching.py` | Searching arrays with conditions using `np.where()` and binary search with `np.searchsorted()`. |
| **Task 39** | `Task_39_numpy_array_sorting.py` | Sorting numeric, string, and boolean arrays, 2D axis sorting, and `np.argsort()`. |
| **Task 40** | `Task_40_numpy_random_techniques.py` | Random numbers: `randint`, `rand`, `randn`, probability-weighted `choice`, and permutations. |
| **Probability** | `Task_Stats_Probability_Distributions.py` | Pearson/Spearman correlation, marginal/joint/conditional probability, Bayes' Theorem, and Normal/Binomial distributions. |
| **Broadcasting**| `Task_NumPy_Broadcasting_and_Universal_Functions.py`| Broadcasting dimensions, universal math functions (`sqrt`, `exp`, `log`), matrix multiplication, and `.npy`/`.csv` I/O. |
| **Runner** | `run_all_week3.py` | Automated test runner verifying all Week 3 Python scripts. |

---

## How to Run
Run any script individually:
```bash
python Task_28_numpy_creating_arrays.py
```
Or run the entire suite:
```bash
python run_all_week3.py
```
