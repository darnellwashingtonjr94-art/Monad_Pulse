class RiskManagementGuard:
    def __init__(self, max_drawdown_limit=0.05):
        self.max_drawdown = max_drawdown_limit

    def check_position_safety(self, current_equity, peak_equity):
        drawdown = (peak_equity - current_equity) / peak_equity
        if drawdown >= self.max_drawdown:
            return False # Trigger emergency flatten
        return True
