##### cythonize
- cythonize -b hello.pyx
- cythonize_1
- on the top of the pyx set
```
- cpdef double means return type of the function should be double
```
```python
import hello
hello.hi()
```

##### cythonize with annotate
- cythonize -b -a taxcode.pyx

##### pyximport auto rebuild
- in pyximport_auto_rebuild folder
```python
#main.py
import pyximport
pyximport.install(language_level=3)
import fastcode
print(fastcode.f1(1))
```
```python
#fastcode.pyx
cpdef f1(long x):
    return x+1
```

##### profiling
- cythonize -b taxcode.pyx
- py -m cProfile -o prof2 main.py
- py -m pstats prof2

```
help
strip
sort tottime
stats 10
```
`
