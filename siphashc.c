/*
 * Copyright (c) 2013 Eli Janssen
 * Copyright (c) 2014 Carlo Pires
 * Copyright © 2017–2023 Michal Čihař
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

#define PY_SSIZE_T_CLEAN

#include <stdlib.h>
#include <string.h>
#include <Python.h>
#include "siphash/siphash.h"

static PyObject *pysiphash(PyObject *self, PyObject *args) {
    const char *key = NULL;
    Py_ssize_t key_sz;
    const char *plaintext = NULL;
    Py_ssize_t plain_sz;
    uint64_t hash;

    if (!PyArg_ParseTuple(
            args, "s#s#:siphash",
            &key, &key_sz, &plaintext, &plain_sz)) {
        return NULL;
    }

    if (key_sz != 16) {
        PyErr_SetString(
            PyExc_ValueError,
            "key must be exactly 128 bits long (16 chars)");
        return NULL;
    }

    hash = siphash(
        (const unsigned char*)key,
        (const unsigned char*)plaintext,
        plain_sz);

    return PyLong_FromUnsignedLongLong(hash);
}

static char siphash_docstring[] = ""
    "Computes Siphash-2-4 of the given string and key\n\n"
    "siphash(key, plaintext) -> hash\n"
    " - key: must be 128 bit long (16 chars at 8 bit each)\n"
    " - plaintext: text\n"
    "returns 64-bit output (python Long)\n";

static PyMethodDef siphashc_methods[] = {
    {"siphash", pysiphash, METH_VARARGS, siphash_docstring},
    {NULL, NULL, 0, NULL} /* sentinel */
};

static struct PyModuleDef moduledef = {
    PyModuleDef_HEAD_INIT,
    "siphashc",
    NULL,
    -1,
    siphashc_methods,
    NULL,
    NULL,
    NULL,
    NULL
};

PyObject *
PyInit_siphashc(void)
{
    return PyModule_Create(&moduledef);
}
