# Introduction

This a collection of experimental Pythong scripts.

# Format and lint Python scripts automatically #

## Requirements ##

Recent versions of cmake, flake8, mypy, and yapf.

## Steps ##

**Configure CMake build**

``` shell
cmake ./
```

**Check syntax using yapf**

Run `make` command to format and to lint all Python files.

``` shell
make
```

Or we can lint or format separately

``` shell
make fmt
make lint
```

Below is the sample output

``` shell
(use_python3) [hdang@hdang-lx2 python]$ make
[100%] Lint Python files with flake8, yapf, and mypy.
/home/tsi/hdang/working/python/examples/numpy_tests.py:1:1: F401 'numpy' imported but unused
/home/tsi/hdang/working/python/examples/numpy_tests.py:2:1: F401 'csv' imported but unused
/home/tsi/hdang/working/python/examples/plot1.py:11:1: E741 ambiguous variable name 'l'
/home/tsi/hdang/working/python/examples/test_sqlite.py:2:1: F401 'os.remove' imported but unused
/home/tsi/hdang/working/python/examples/test_sqlite.py:14:1: E722 do not use bare 'except'
make[2]: *** [CMakeFiles/lint.dir/build.make:93: .pylint_stamp] Error 1
make[1]: *** [CMakeFiles/Makefile2:123: CMakeFiles/lint.dir/all] Error 2
make: *** [Makefile:103: all] Error 2
```

