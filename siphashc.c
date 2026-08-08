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

#include <Python.h>
#include <stdlib.h>
#include <string.h>
#include "siphash/siphash.h"

#define SIPHASH_GIL_THRESHOLD 8192
#if PY_VERSION_HEX < 0x030B0000
#define SIPHASHC_PYC_FUNCTION_CAST(func) \
    ((PyCFunction)(void (*)(void))(func))
#else
#define SIPHASHC_PYC_FUNCTION_CAST(func) _PyCFunction_CAST(func)
#endif

static int get_immutable_data(
        PyObject *object,
        const char *argument_name,
        const char **data,
        Py_ssize_t *size) {
    if (PyBytes_Check(object)) {
        char *bytes_data;

        if (PyBytes_AsStringAndSize(object, &bytes_data, size) < 0) {
            return 0;
        }
        *data = bytes_data;
        return 1;
    }

    if (PyUnicode_Check(object)) {
        *data = PyUnicode_AsUTF8AndSize(object, size);
        return *data != NULL;
    }

    PyErr_Format(
        PyExc_TypeError,
        "%s must be str or bytes",
        argument_name);
    return 0;
}

static PyObject *pysiphash(
        PyObject *self,
        PyObject *const *args,
        Py_ssize_t nargs) {
    PyObject *key_object;
    PyObject *plaintext_object;
    const char *key = NULL;
    Py_ssize_t key_sz;
    const char *plaintext = NULL;
    Py_ssize_t plain_sz;
    uint64_t hash;

    if (nargs != 2) {
        PyErr_Format(
            PyExc_TypeError,
            "siphash() takes exactly 2 arguments (%zd given)",
            nargs);
        return NULL;
    }
    key_object = args[0];
    plaintext_object = args[1];

    /* Both objects own immutable storage and remain alive for the call. */
    if (!get_immutable_data(key_object, "key", &key, &key_sz) ||
            !get_immutable_data(
                plaintext_object,
                "plaintext",
                &plaintext,
                &plain_sz)) {
        return NULL;
    }

    if (key_sz != 16) {
        PyErr_SetString(
            PyExc_ValueError,
            "key must be exactly 128 bits long (16 chars)");
        return NULL;
    }

#ifdef Py_GIL_DISABLED
    hash = siphash(
        (const unsigned char *)key,
        (const unsigned char *)plaintext,
        plain_sz);
#else
    if (plain_sz >= SIPHASH_GIL_THRESHOLD) {
        Py_BEGIN_ALLOW_THREADS
        hash = siphash(
            (const unsigned char *)key,
            (const unsigned char *)plaintext,
            plain_sz);
        Py_END_ALLOW_THREADS
    } else {
        hash = siphash(
            (const unsigned char *)key,
            (const unsigned char *)plaintext,
            plain_sz);
    }
#endif

    return PyLong_FromUnsignedLongLong(hash);
}

static char siphash_docstring[] = ""
    "Computes Siphash-2-4 of the given string and key\n\n"
    "siphash(key, plaintext) -> hash\n"
    " - key: must be 128 bit long (16 chars at 8 bit each)\n"
    " - plaintext: text\n"
    "returns 64-bit output (python Long)\n";

static PyMethodDef siphashc_methods[] = {
    {"siphash", SIPHASHC_PYC_FUNCTION_CAST(pysiphash), METH_FASTCALL,
     siphash_docstring},
    {NULL, NULL, 0, NULL} /* sentinel */
};

#ifdef Py_TARGET_ABI3T

PyABIInfo_VAR(abi_info);

static PySlot siphashc_slots[] = {
    PySlot_STATIC_DATA(Py_mod_abi, &abi_info),
    PySlot_STATIC_DATA(Py_mod_name, "siphashc"),
    PySlot_STATIC_DATA(Py_mod_methods, siphashc_methods),
    PySlot_STATIC_DATA(Py_mod_gil, Py_MOD_GIL_NOT_USED),
    PySlot_END,
};

PyMODEXPORT_FUNC
PyModExport_siphashc(void)
{
    return siphashc_slots;
}

#else

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
    PyObject *module = PyModule_Create(&moduledef);

#ifdef Py_GIL_DISABLED
    if (module != NULL &&
            PyUnstable_Module_SetGIL(module, Py_MOD_GIL_NOT_USED) < 0) {
        Py_DECREF(module);
        return NULL;
    }
#endif

    return module;
}

#endif
