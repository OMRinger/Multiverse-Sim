
class CommunityContribution:
    def __init__(self):
        self.contributions = []

    def add_contribution(self, contributor, contribution):
        self.contributions.append((contributor, contribution))

    def list_contributions(self):
        for contribution in self.contributions:
            print(f"Contributor: {contribution[0]}, Contribution: {contribution[1]}")
