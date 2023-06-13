#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints information about a Python list object
 * @p: pointer to a Python list object.
 */

void print_python_list_info(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;

	Py_ssize_t i;
	Py_ssize_t size = PyList_Size(p);
	Py_ssize_t allocated = list->allocated;

	PyObject *item;
	const char *typeName;

	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %zd\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = list->ob_item[i];
		typeName = Py_TYPE(item)->tp_name;
		printf("Element %zd: %s\n", i, typeName);
	}
}
