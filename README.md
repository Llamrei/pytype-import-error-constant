Dependency: pytype

### Expected behaviour:

`pytype package/ --no-cache` has no errors as `python actual_import_check.py` succeeds.

### Actual Behaviour:

Fails with error 

```
File "/package/foo/bar/__init__.py", line 1, in <module>: Can't find module 'bar_mod'. [import-error]
```

However if you change the exported constant `BAR` in /package/foo/bar/__init__.py then pytype will succeed.

I suspect it is something to do with the `.pytype/imports/package.__init__.imports` reading:

```
package/foo/BAR/bar_mod /pytype-import-error-constant/.pytype/pyi/package/foo/BAR/bar_mod.pyi
package/foo/BAR/__init__ /pytype-import-error-constant/.pytype/pyi/package/foo/BAR/__init__.pyi
```
