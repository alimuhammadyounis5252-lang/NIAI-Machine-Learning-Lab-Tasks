@echo off
echo ========================================================
echo   Push AI Course Tasks to GitHub
echo   Student: Ali Muhammad Younis (886)
echo ========================================================
echo.
set /p REPO_URL="Enter your GitHub Repository URL (e.g., https://github.com/username/repo-name.git): "

if "%REPO_URL%"=="" (
    echo Error: Repository URL cannot be empty!
    pause
    exit /b
)

echo.
echo Setting remote origin to %REPO_URL%...
git remote remove origin 2>nul
git remote add origin %REPO_URL%

echo.
echo Pushing branch 'main' to GitHub...
git push -u origin main

if %ERRORLEVEL% equ 0 (
    echo.
    echo ========================================================
    echo   SUCCESS! Your repository is now live on GitHub!
    echo ========================================================
) else (
    echo.
    echo Failed to push. Please check your GitHub URL and login permissions.
)
echo.
pause
