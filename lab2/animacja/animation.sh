#!/bin/bash
#SBATCH -p plgrid-testing
#SBATCH -N 1
#SBATCH --ntasks-per-node=10
#SBATCH --array=1-10
povray Subset_Start_Frame=$SLURM_ARRAY_TASK_ID Subset_End_Frame=$((SLURM_ARRAY_TASK_ID+1)) animation_a_.ini
