param(
    [String]$path="C:\Users\erik_\Desktop\Practicas Pc\PIA\*.*"
)

function Get-ScriptDirectory {
    Split-Path -Parent $PSCommandPath
}

$Ruta = Get-ScriptDirectory
$salida = "Hash-FileNames.txt"
$SalidaFile = $ruta+"\hash\"+$salida
$testFolder = $ruta+"\hash"
$exist = Test-Path $testFolder

if ($exist -eq $True){
    Remove-Item $testFolder -Recurse
    New-Item -Path $ruta -Name "hash" -ItemType "directory"
    Get-FileHash -Path $path -Algorithm SHA512 | Format-List | Out-File $SalidaFile
}
else
{
    New-Item -Path $ruta -Name "hash" -ItemType "directory"
    Get-FileHash -Path $path -Algorithm SHA512 | Format-List | Out-File $SalidaFile
}
