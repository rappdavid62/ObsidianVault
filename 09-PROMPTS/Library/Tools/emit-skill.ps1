# emit-skill.ps1
# PowerShell wrapper for the improved emit-skill.py
#
# Usage examples (after adding to your PATH or running from the Tools folder):
#   .\emit-skill.ps1 daily-job-search
#   .\emit-skill.ps1 daily-job-search low-energy-execution --with-master
#   .\emit-skill.ps1 --daily --clip
#   .\emit-skill.ps1 --list
#   .\emit-skill.ps1 --search job

param(
    [Parameter(ValueFromRemainingArguments=$true)]
    [string[]]$Args
)

$scriptDir = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonScript = Join-Path $scriptDir "emit-skill.py"

& python $pythonScript @Args
