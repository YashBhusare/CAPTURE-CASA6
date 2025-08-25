
import os

# Get the current working directory
current_directory = os.getcwd()

# Define the PBS script content
pbs_script_content = f"""#!/bin/bash
#PBS -N casa_job
#PBS -l nodes=1:ppn=4
#PBS -l walltime=128:00:00
#PBS -o casa_output.log
#PBS -e casa_error.log

# Change to the working directory
cd {current_directory}

# Run CASA with the specified script
/home/ybhusare/Imaging/casa-6.6.0-20-py3.8.el7/bin/casa -c capture-casa6.py
"""

# Save the PBS script to a file
with open("pbs_script.pbs", "w") as file:
    file.write(pbs_script_content)

print("PBS script generated and saved as 'pbs_script.pbs'.")
