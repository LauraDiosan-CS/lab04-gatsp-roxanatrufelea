from tsp.service import Service
from tsp.repo import FileRepository

repo=FileRepository("in.txt")
service=Service(repo)
service.gaTsp()