import git
from Importer import *
repo1 = git.Repo("Path/PrivateProject1/.git")
mock_repo = git.Repo("Path/MockProjects/.git")
importer = ImporterFromRepository([repo1], mock_repo)
importer.set_author(['work@email.ru', 'personal@email.ru'])
importer.import_repository()
