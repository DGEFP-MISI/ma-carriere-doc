@echo off
setlocal
cd /d "%~dp0"
set "PYTHON_EXE=%LOCALAPPDATA%\Programs\Python\Python313\python.exe"
if exist "%PYTHON_EXE%" goto run
where python >nul 2>nul
if %ERRORLEVEL% EQU 0 (
    set "PYTHON_EXE=python"
    goto run
)
echo ERREUR : Python 3 introuvable.
echo Chemin teste : %%LOCALAPPDATA%%\Programs\Python\Python313\python.exe
set "RET=1"
goto done
:run
echo Verification du dossier API DGEFP-RCO, sans connexion reseau...
"%PYTHON_EXE%" "scripts\verifier_dossier.py"
set "RET=%ERRORLEVEL%"
if "%RET%"=="0" (echo RESULTAT : SIX CONTROLES OK) else (echo RESULTAT : ECHEC - relire la sortie)
:done
if /I NOT "%~1"=="/nopause" pause
exit /b %RET%
