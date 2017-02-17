from git import Repo
from git import RemoteProgress

from var_dump import var_dump

class Gitter(object):

	repo = object	

	def __init__(self,elpath):		
		self.repo= Repo(elpath)

	def pull(self,branch):
		repo= self.repo
		repo_heads = repo.heads				
		o = repo.remotes.origin
		o.pull(repo_heads[branch])

	def listCommits(self,branch):
		self.pull(branch)
		repo= self.repo
		master = repo.head.reference
		try:
			commit_ids = repo.git.rev_list(repo.branches[branch]).splitlines()
		except:
			return "error"
		
		commits = []
		for commit_id in commit_ids[::-1]:  #start with the oldest commit
			commit = repo.commit(commit_id)
			commits.append(commit)

		return commits		

	def pushTo(self,remote,branch):
		self.pull(branch)
		repo= self.repo
		repo_heads = repo.heads				
		o = repo.remotes[remote]
		try:					
			este= o.push(progress=MyProgressPrinter())
			print("------")
			var_dump(list(este))
			print(este[0].summary)			
			print("------")
		except:
			return "mal"
		return este[0].summary

class MyProgressPrinter(RemoteProgress):
	def update(self, op_code, cur_count, max_count=None, message=''):
		print(op_code, cur_count, max_count, cur_count / (max_count or 100.0), message or "NO MESSAGE")

