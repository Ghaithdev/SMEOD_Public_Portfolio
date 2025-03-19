# Prompt the user for a directory name and store it in $fhand 
$fhand = Read-Host "Enter a directory name"
$newfname=($fhand + '_txts')

# Check if the directory exists
if (Test-Path -Path $fhand -PathType Container) {
    # Get all the files in the $fhand directory and store the results in $files
    $files = Get-ChildItem -Path $fhand | Where-Object { $_.Extension -eq ".docx" }

    # Create an empty directory named fhand_txts in the same location as $fhand
    $copyDestination = $newfname
    New-Item -Path $copyDestination -ItemType Directory

    # Loop through each DOCX file in $files, read its content, and save to a .txt file
    foreach ($file in $files) {
        Write-Host "File Name: $($file.Name)"
        
        # Create the path for the corresponding .txt file in the fhand_txts folder
        $txtFilePath = Join-Path -Path $copyDestination -ChildPath ($file.BaseName + ".txt")

        # Create a COM object for Microsoft Word
        $word = New-Object -ComObject Word.Application

        # Open the DOCX file
        $doc = $word.Documents.Open($file.FullName)

        # Read the content and save it to the .txt file
        $content = $doc.Content.Text
        $content | Set-Content -Path $txtFilePath -Force

        # Close the document and release the COM objects
        $doc.Close()
        [System.Runtime.Interopservices.Marshal]::ReleaseComObject($doc) | Out-Null
        [System.Runtime.Interopservices.Marshal]::ReleaseComObject($word) | Out-Null
        [System.GC]::Collect()
        [System.GC]::WaitForPendingFinalizers()
        
        Write-Host "File content saved to: $txtFilePath"
    }
} else {
    Write-Host "The directory '$fhand' does not exist."
}
