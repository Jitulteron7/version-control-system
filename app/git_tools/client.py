from .commands.base import BaseCommand

class GitClient:
    def run(self, command:BaseCommand):
        command.execute()

