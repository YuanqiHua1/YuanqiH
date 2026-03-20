from mpi4py import MPI

comm = MPI.COMM_WORLD

rank = comm.Get_rank()

size = comm.Get_size()

# mpirun -n 2 python mpi_ranks.py
if rank == 0:
	print(f'(Process rank {rank} : yestoday)')

elif rank == 1:
	print(f'(Process rank {rank} : today)')


else:
	print(f'(Process rank {rank} ：tomorrow)')


