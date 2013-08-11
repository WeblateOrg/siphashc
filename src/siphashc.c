/* 
 * Copyright (c) 2013 elij
 * 
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 * 
 * The above copyright notice and this permission notice shall be included in
 * all copies or substantial portions of the Software.
 * 
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
 * THE SOFTWARE.
**/

#include <stdlib.h>
#include <string.h>
#include <Python.h>
#include <inttypes.h>
#include "siphash/siphash.h"

static PyObject *pysiphash(PyObject *self, PyObject *args) {
    const char *key = NULL;
    const char *plaintext = NULL;

    if (!PyArg_ParseTuple(args, "ss", &key, &plaintext)) {
        return NULL;
    }

    if (strlen(key) != 16) {
        PyErr_SetString(PyExc_ValueError, "key must be exactly 16 chars long");
        return NULL;
    }

    size_t l = strlen(plaintext);
    uint64_t hash = siphash((const unsigned char*)key, (const unsigned char*)plaintext, l);

    PyObject *ret = Py_BuildValue("K", hash);
    return ret;
}

static char siphash_docstring[] = ""
    "siphash(key, plaintext) -> hash\n"
    " - key: must be 16 bytes long (16 chars at 8 bit each)\n"
    " - plaintext: text\n\n"
    "returns computed Siphash-2-4 of the given string and 16 byte key\n";

static PyMethodDef module_methods[] = {
    {"siphash", pysiphash, METH_VARARGS, siphash_docstring},
    {NULL, NULL, 0, NULL} /* sentinel */
};

PyMODINIT_FUNC initsiphashc(void) {
    PyObject *m = Py_InitModule3("siphashc", module_methods, "siphash");
    if (m == NULL)
        return;
}

