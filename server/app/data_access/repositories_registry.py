class RepositoriesRegistry:
    def __init__(self, user_repo,  building_repo,tenant_repo,food_routine_repo, transaction_repo):
        self.user_repo = user_repo
        self.building_repo = building_repo
        self.tenant_repo = tenant_repo
        self.food_routine_repo = food_routine_repo
        self.transaction_repo = transaction_repo
