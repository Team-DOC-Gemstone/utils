#!/bin/bash

#SBATCH --job-name=dicom-npy-conversion
#SBATCH --output=npy-conversion-output.txt
#SBATCH --error=npy-conversion.err
#SBATCH --time=6:00:00
#SBATCH --mem=8gb
#SBATCH --ntasks=1
#SBATCH --account=class
#SBATCH --partition=class

cd /fs/classhomes/spring2024/gems497/ge497000/utils
source /fs/classhomes/spring2024/gems497/ge497000/team-doc/bin/activate
srun bash -c "python3 convert_to_npy_general.py" &
wait
