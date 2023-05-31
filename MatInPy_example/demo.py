import matlab.engine

# start a matlab process
mat_eng = matlab.engine.start_matlab()

# call matlab build-in fuction `isprime`
print(mat_eng.isprime(37))

# create a matlab array from python
array_1d = matlab.double([1, 2, 3, 4, 5])
print(mat_eng.sqrt(array_1d))
# index into an array
print(array_1d[0])  # [1.0,2.0,3.0,4.0,5.0]
print(array_1d[0][1])  # 2.0

# create a multidimensional matlab array
array_2d = matlab.double([[1, 2, 1], [3, 4, 3]])
print(mat_eng.sqrt(array_2d))
# slice a array
print(array_2d[1][0:2])  # [3.0,4.0]
# reshape an array
array_2d.reshape((3, 2))
print(array_2d)  # [[1.0,4.0],[3.0,1.0],[2.0,3.0]]

# create a complex array
array_complex = matlab.double([1+1j, 2+2j, 3+3j], is_complex=True) 

# call a usr defined function
path_dir = "G:\\Documents\\Python\\pyqt_sample\\MatInPy"
mat_eng.addpath(path_dir)
print(mat_eng.single_return(1.0, 2.0, nargout=1))
# call a usr defined function with multiple returns
print(mat_eng.multi_return(4.0, 9.0, nargout=2))  # (2.0, 3.0)

# exit matlab process
mat_eng.quit()