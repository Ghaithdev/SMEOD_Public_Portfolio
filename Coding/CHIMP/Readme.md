>[!Info]
>This program has had all proprietary and sensitive information removed from it, it may not run correctly without modification on other devices due to changes that needed to be made to make sure no process of the company this was produced for has been exposed.
# Overview
## Process 
### Process before
Previously samples were run on a Mass Spec then collected and then counted on a device known as a TC. The counting process creates raw ascii files (these ascii files ) that need to be split into smaller chunks called plates and strung together to reflect the samples that the data was extracted from (creating what are called sample files). These sample files have to be saved onto a drive on which standard users have write permissions. These sample files were then imported into a write only database program, the database was then used to generate data printouts. The fact that users are able to  files in this drive where sample files are stored means that the data could no longer be considered to have integrity and thus all the printouts had to be manually compared to the ascii files in a lengthy process that consumed a lot of the time of highly skilled scientists.

### How this program changed the process
This program attempts to simplify/remove two parts of the above process, the importer part of the program automates the construction of the ascii files and importantly creates hashes of the files in order to preserve integrity, these hashes were stored in a "Ticket" file with its own hash. The second part of the process uses these ticket files to replace the time consuming manual cross-checking process described in the above paragraph

## How does the app work
### Importer
The app uses the Python Tkinter library to create a GUI with which the user interacts, the program asks the user for files to read, opens the given files and stores the values within those files within a series of dictionaries with content split based on parameters given by the user. The dictionaries are then manipulated by the user to produce output data according to what the user requests. This data is then added to sample files and each files hash is generated, a ticket file is generated describing the parameters used to create the sample files and storing the hashes for the sample files, the ticket file is then read and its hash stored in the file. 
### Checker
The user tells the checker which tickets they wish to audit, the ticket checker reads the ticket and validates the ticket hash, checker then uses the paths stored in the ticket file to find the relevant files. It then reads the sample files mentioned in the tickets, checking both that the file content matches the hash and that the "created" and "modified" times are within 5 seconds of one another (i.e. it is checking that the file has not been opened or saved). Once these checks are done the GUI displays the information within the ticket to allow the user to check that it shows what they think it should
