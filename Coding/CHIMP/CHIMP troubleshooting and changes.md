# Bugs 
## Replicable:
>[!Info]
>All currently known replicable bugs have been fixed
- ***~~File not found jam***: When an assay file cannot be found by the ticket checker it stops and fails to load any assays~~
	- ~~Potential solutions:~~
		- ~~Properly implement the fail state for that condition this will require some sort of warning to be available should the plate fail to be found~~
	- ~~Implemented solutions:~~
		- ~~As above~~
- ***~~No file selected halts***: In a number of the spaces, when asked to select a file the program will crash if the user fails to select a file (by cancelling) or selects an invalid file~~
	- ~~Potential solutions~~:
		- ~~Add try-except(FileNotFound) block to each section where the user is asked to select a file~~
	- ~~Implemented solution~~:
		- ~~Removed duplication of functions asking user to select a file and set it so that all such requests are routed the same function ~~
		- ~~Did the same for all incidents of asking user for directory as well~~
		- ~~Implemented such for saveasfilename requests as well~~


## Non-replicable:
- User selects file for import into plate bin but no plates appear there
- When demoing app to user a bug was seen with the standard import frame, performed a number of tests of the integer factor protections first testing what happens when the number entered is too high and too low, the protection did not allow the user to request files that were not the correct length, however upon attempting to import the files the final well on the last plate had not been implemented (the plates simply ended on A12) meaning the plates were too long
	- The following tests were implemented to try and replicate the issue:
		- Redoing the exact series of steps that were used during the demo
		- Cancelling during other steps of the process and then trying the import
		- Using the import window with a second import window open

>[!Solution]
>The solution for all the currently known non-replicable bugs seems to be to restart the program, unfortunately these bugs have not been ~~reliably~~ replicated so there is little that can be done to figure out the cause

# Known issues

## Major issues:
- ~~***Edit and undo***: The user is currently able to gain a false negative on the edit check by changing a file, doing the import and then returning the file to its original state. This would cause the file to pass the Hash checks as it would still produce the correct hash but the Laura data would be divorced from the shown data~~
	- ~~Potential solutions:~~
		- ~~Compare creation and modify times: When reading the file read its "created" and "modified" times and if they differ by too large an amount fail the integrity checks~~
			- ~~Pros:~~
				- ~~Simple to implement~~
				- ~~Requires no change to the ticket~~
				- ~~Requires minimal infrastructure~~
				- ~~Requires minimal training~~
			- ~~Cons:~~
				- ~~Creates avenue for false positives~~
				- ~~Could potentially leave avenues to more sophisticated versions of a similar attack pattern~~
		- ~~Server & Client model: The user interface is a client to a central server, this server is able to write to a location within the network that is otherwise not writable to~~
			- ~~Pros:~~
				- ~~Robust solution that closes a number of attack vectors that are not closed ~~~~by comparing the modify times~~
				- ~~Does not necessarily require more training~~
				- ~~Allows greater control and potentially strengthens non-reputability~~
			- ~~Cons:~~
				- ~~Massive overhaul of the program architecture~~
				- ~~Requires much closer cooperation with IT~~
				- ~~Requires much more testing and validation~~
				- ~~Requires much greater safety checks~~
				- ~~IT could just say that this is not an acceptable method~~
				- ~~Likely means that only a few or single instance of the program may operate at a given time~~
	- ~~Implemented solution:~~
		- ~~Compare modify and creation times: The time a file was created vs the time it was modified are compared, if they differ by more than 5 seconds (could likely tighten this window) then the file fails the 'edit check'. If the ticket fails the edit check it will refuse to open just as it would if the hash check fails~~
	- ~~Potential Mitigations: ~~
		- ~~Random spot checks, as now a random portion of files undergo a spot check comparing the Laura files to the TopCount data~~
	- ~~Implemented Mitigations: ~~
		- ~~While the program is not currently in use the above mitigation will be implemented, the spot check may need to be changed such that it could check any well rather than the current acetate wells, possibly meaning a comeback for the randomizer~~
- ***File swap attacks***: This attack is similar to the previous one but using files with the same name to trick the program instead.
	- Potential solutions:
		- Server & Client model: The user interface is a client to a central server, this server is able to write to a location within the network that is otherwise not writable to
			- Pros:
				- Robust solution that closes a number of attack vectors that are not closed by comparing the modify times
				- Does not necessarily require more training
				- Allows greater control and potentially strengthens non-reputability
			- Cons:
				- Massive overhaul of the program architecture
				- Requires much closer cooperation with IT
				- Requires much more testing and validation
				- Requires much greater safety checks
				- IT could just say that this is not an acceptable method
				- Likely means that only a few or single instance of the program may operate at a given time
				- Requires information to travel over a network
		- Have the creation time be part of the checks: Given that the creation time of the imports is attached to the file itself and that the LAURA printout includes a datetime of creation it would be fairly simple to cross check and make sure that the file was created before the LAURA import occurred
			- Pros:
				- This is so much easier to implement that it is frankly comical
				- No major changes to the code
			- Cons:
				- This does require more of the users
				- May require an export or printout from the application
		- Risk Based DI approach: I am advised that it, in order to avoid the program having a document output that it would be best to simply acknowledge that while this sort of attack is possible it is extremely difficult. Further none of the current internal systems are actually 

## No programmatic solution/ no known solution/ implementing solution unlikely
- ***User dependent file paths***: If users have the same share mapped to different drive letters on their device then the filepaths listed within the program and within LAURA are likely to be affected
	- Potential Mitigation:
		- Standardize drive mappings throughout the team and help team members to enact these mappings on all necessary devices
- ***Name clashes***: When user imports two items with the same name the names of the plates clash, this means that only the data contained in the second item is retained. Especially likely for PSNs but can occur with assays and (hypothetically) tickets
	- Potential Mitigation: User training, as long as users do not import plates from different Top Counts or different studies at the same time this cannot occur. Other changes to prevent this would require total rework of the structure of the app that are not really worth the time required to fix
- ***File not found issues***: If one or more of the sample files has been moved or renamed then the program treats this as the file having been edited, there is no way to reroute the program to the new location of the file
	- Potential solution:
		- If a file fails to be found give the user a prompt to select the files new location
		- Issues with the solution:
			- This would invalidate one of the key protections that the program offers
			- This blows up one of the key guardrails in the program for a not huge benefit
	- Potential mitigation: User training, inform users that moving files will cause issues 

## Quality of life
- ***Non integer number of samples in an assay***: A common practice is to count plates for new samples with recounted plates at the end. If the user counts plates in this manner they currently cannot use the standard "Add assay" button to perform their imports.
	- Potential solutions:
		- Training: Suggest to users that if they want to readily be able to use the quickest set up on the importer then they cannot count recounts with their new plates
			- Pros:
				- Very little effort
				- Allows users to make an informed choice about what makes thing easier for them
			- Cons:
				- Alternate methods for building assay text files are more difficult and prone to mistakes
				- Places pressure on users to change their behaviour in order to satisfy 'the app'
				- Is largely doing nothing to solve the problem, although it is notable that this issue exists in the current procedure and thus dealing with this issue should be familiar
		- Implement toggle on add assay pop-up: Create a checkbox that allows user to confirm that they have a non-integer number of samples in their assay and turn off the guardrail if they tick this box
			- Pros:
				- Allows the user flexibility
				- Will be the most satisfying solution for most users
				- Could potentially remove the need for the 'Add Empty Sample' button
			- Cons:
				- Hard to implement, will require rework of the current logic
				- Allows the user to bypass safety rails
				- Could introduce bugs
- ~~***Check button feedback***: A number of the check/validate buttons do not provide positive feedback when the checks are passed~~
	- ~~Potential solutions:~~
		- ~~Just implement positive feedback for a pass~~
	- ~~Solution implemented:~~
		- ~~As above~~

# Discussion

## Ticket naming convention
At least one user has asked that the tickets be named based on the assays that make that ticket up under the belief that this would make it easier to understand what was within the ticket.
I question whether this would actually make it any easier to know which files you had to do the import check for. Either the import checks are done intermittently throughout the process or they are done at the end of the importing process. In the former case I feel like asking the checker to simply check the most recent file is the easiest option but I cannot affirm what the process will look like
