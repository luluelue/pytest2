@echo off
for /R %%s in (*.pyc) do (
del %%s
echo delete %%s
)
pause