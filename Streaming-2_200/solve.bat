:: The flag.txt files are numbered flag0.txt through flag4820.txt
@echo off
set /a counter=0
:loop
set /a counter=%counter%+1
if %counter% == 4821 (goto :eof) else (more < secret2.docx:flag%counter%.txt)
goto :loop
