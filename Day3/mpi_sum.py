from mpi4py import MPI

comm = MPI.COMM_WORLD()

rank = comm.Get_rank()

size = comm.Get_size()

# mpirun -n 5 python mpi_sum.py



local_value = rank

total_value = comm.reduce(local_value, op = MPI.SUM, root = 0)

if rank == 0:
	print(f"Total sum = {total_sum}")

