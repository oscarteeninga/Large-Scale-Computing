#!/bin/bash
#SBATCH -N 1
#SBATCH -p plgrid-testing
#SBATCH --array=1-3
#SBATCH --ntasks-per-node=3
if [ $SLURM_ARRAY_TASK_ID == 1 ]; then
	cat text.txt | head -n 1
elif [ $SLURM_ARRAY_TASK_ID == 2 ]; then
	cat text.txt | head -n 2 | tail -n 1
else
	cat text.txt | tail -n 1
fi

