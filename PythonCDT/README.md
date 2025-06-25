# PythonCDT

Python bindings for [CDT: C++ library for constrained Delaunay triangulation](https://github.com/artem-ogre/CDT) implemented with [pybind11](https://github.com/pybind/pybind11)

***If PythonCDT helped you please consider adding a star on [GitHub](https://github.com/artem-ogre/PythonCDT). This means a lot to the authors*** 🤩
## Building

### Pre-conditions
- Clone with submodules: `git clone --recurse-submodules https://github.com/artem-ogre/PythonCDT.git`
- Make sure packages from requirements.txt are available.

```bash
# build the wheel and install the package with pip
pip3 install .
# run tests
pytest ./cdt_bindings_test.py
```

## License
[Mozilla Public License, v. 2.0](https://www.mozilla.org/en-US/MPL/2.0/FAQ/)

## Contributors
- [SioulisChris](https://github.com/SioulisChris): fixing the tests on Windows
